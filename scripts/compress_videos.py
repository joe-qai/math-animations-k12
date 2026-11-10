# -*- coding: utf-8 -*-
"""把本地视频压到 720p，控制仓库与线上站点体积（默认 <1GB 预算）。

只处理指定 id（--ids-file）或目录下的全部 mp4；已经不超过 --max-height 的文件会跳过。
压缩后仍是 H.264 + AAC，浏览器兼容性与原片一致；时长不变，章节时间无需调整。

用法：
    python scripts/compress_videos.py --ids-file missing.txt
    python scripts/compress_videos.py --check
    python scripts/compress_videos.py --workers 3 --crf 28
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import tempfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VIDEO_DIR = ROOT / "assets" / "videos"


def probe(path: Path) -> dict:
    proc = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries",
         "stream=codec_type,width,height:format=duration",
         "-of", "json", str(path)],
        capture_output=True, text=True,
    )
    try:
        data = json.loads(proc.stdout)
    except Exception:
        return {}
    video = next((s for s in data.get("streams", []) if s.get("codec_type") == "video"), {})
    return {
        "height": int(video.get("height") or 0),
        "duration": float(data.get("format", {}).get("duration") or 0),
    }


def compress(path: Path, max_height: int, crf: int, audio_kbps: int) -> tuple[bool, str, int, int]:
    before = path.stat().st_size
    info = probe(path)
    if info.get("height", 0) and info["height"] <= max_height:
        return True, "skip", before, before

    fd, name = tempfile.mkstemp(suffix=".mp4", dir=str(path.parent))
    os.close(fd)
    tmp = Path(name)
    try:
        proc = subprocess.run(
            [
                "ffmpeg", "-v", "error", "-y",
                "-i", str(path),
                "-vf", f"scale=-2:{max_height}",
                "-c:v", "libx264", "-preset", "veryfast", "-crf", str(crf),
                "-pix_fmt", "yuv420p",
                "-c:a", "aac", "-b:a", f"{audio_kbps}k",
                "-movflags", "+faststart",
                str(tmp),
            ],
            capture_output=True, text=True,
        )
        if proc.returncode != 0 or not tmp.exists() or tmp.stat().st_size == 0:
            detail = (proc.stderr or "ffmpeg failed").strip().splitlines()
            return False, (detail[-1] if detail else "ffmpeg failed")[:160], before, before
        after = tmp.stat().st_size
        if after >= before:
            return True, "kept", before, before
        tmp.replace(path)
        return True, "ok", before, after
    except Exception as exc:  # noqa: BLE001
        return False, str(exc)[:160], before, before
    finally:
        if tmp.exists():
            tmp.unlink(missing_ok=True)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dir", default=str(VIDEO_DIR), help="视频目录")
    parser.add_argument("--ids-file", help="每行一个课时 id，只处理这些视频")
    parser.add_argument("--max-height", type=int, default=720)
    parser.add_argument("--crf", type=int, default=28)
    parser.add_argument("--audio", type=int, default=64, help="音频码率 kbps")
    parser.add_argument("--workers", type=int, default=3)
    parser.add_argument("--check", action="store_true", help="只列出待压缩文件")
    args = parser.parse_args()

    video_dir = Path(args.dir)
    if args.ids_file:
        ids = [x.strip() for x in Path(args.ids_file).read_text(encoding="utf-8").splitlines() if x.strip()]
        targets = [video_dir / f"{i}.mp4" for i in ids]
    else:
        targets = sorted(video_dir.glob("*.mp4"))
    targets = [p for p in targets if p.exists()]

    pending = [p for p in targets if probe(p).get("height", 0) > args.max_height]
    total_before = sum(p.stat().st_size for p in targets)
    print(f"目标 {len(targets)} 个视频，{total_before / 1048576:.1f} MB；待压缩 {len(pending)} 个")

    if args.check or not pending:
        for p in pending:
            print(f"  {p.name} {p.stat().st_size / 1048576:.1f} MB")
        return 0

    ok = fail = 0
    before = after = 0
    with ThreadPoolExecutor(max_workers=max(1, args.workers)) as pool:
        futures = [
            pool.submit(compress, p, args.max_height, args.crf, args.audio)
            for p in pending
        ]
        for path, future in zip(pending, futures):
            good, msg, b, a = future.result()
            before += b
            after += a
            if good:
                ok += 1
                print(f"  {msg:4} {path.name} {b / 1048576:.1f} -> {a / 1048576:.1f} MB")
            else:
                fail += 1
                print(f"  FAIL {path.name}: {msg}")

    print(
        f"完成：{ok} 个成功，{fail} 个失败；"
        f"{before / 1048576:.1f} -> {after / 1048576:.1f} MB"
    )
    return 0 if fail == 0 else 1


if __name__ == "__main__":
    sys.exit(main())