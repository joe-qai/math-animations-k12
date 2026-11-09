# -*- coding: utf-8 -*-
"""本地视频预处理：把 mp4 的索引（moov）挪到文件开头，方便边下边播。

默认只做无损 remux（不重新编码，画质不变）；加 --check 只看状态。

用法：
    python scripts/optimize_videos.py
    python scripts/optimize_videos.py --check
    python scripts/optimize_videos.py --workers 4
"""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
import tempfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VIDEO_DIR = ROOT / "assets" / "videos"


def box_order(path: Path) -> tuple[int, int]:
    """返回 (moov 位置, mdat 位置)，找不到记 -1。"""
    moov = mdat = -1
    size_at = 0
    with path.open("rb") as fh:
        while True:
            fh.seek(size_at)
            head = fh.read(8)
            if len(head) < 8:
                break
            size = int.from_bytes(head[:4], "big")
            kind = head[4:8]
            if kind == b"moov" and moov == -1:
                moov = size_at
            elif kind == b"mdat" and mdat == -1:
                mdat = size_at
            if moov != -1 and mdat != -1:
                break
            if size == 1:  # 64 位扩展长度
                fh.seek(size_at + 8)
                size = int.from_bytes(fh.read(8), "big")
            if size <= 0:
                break
            size_at += size
    return moov, mdat


def is_faststart(path: Path) -> bool:
    moov, mdat = box_order(path)
    return moov != -1 and (mdat == -1 or moov < mdat)


def remux(path: Path) -> tuple[bool, str]:
    if is_faststart(path):
        return True, "skip"
    fd, name = tempfile.mkstemp(suffix=".mp4", dir=str(path.parent))
    os.close(fd)
    tmp = Path(name)
    try:
        proc = subprocess.run(
            [
                "ffmpeg", "-v", "error", "-y",
                "-i", str(path),
                "-map", "0", "-c", "copy",
                "-movflags", "+faststart",
                str(tmp),
            ],
            capture_output=True,
            text=True,
        )
        if proc.returncode != 0 or not tmp.exists() or tmp.stat().st_size == 0:
            return False, (proc.stderr or "ffmpeg failed").strip().splitlines()[-1][:160]
        if not is_faststart(tmp):
            return False, "still not faststart"
        tmp.replace(path)
        return True, "remuxed"
    except Exception as exc:  # noqa: BLE001 - 单文件失败不影响整体
        return False, str(exc)[:160]
    finally:
        if tmp.exists():
            tmp.unlink(missing_ok=True)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="只检查，不修改文件")
    parser.add_argument("--workers", type=int, default=2, help="并行处理数（默认 2）")
    args = parser.parse_args()

    videos = sorted(VIDEO_DIR.glob("*.mp4"))
    if not videos:
        print("没有找到 mp4")
        return 0

    total = sum(p.stat().st_size for p in videos) / 1048576
    pending = [p for p in videos if not is_faststart(p)]
    print(f"共 {len(videos)} 个视频，{total:.1f} MB；未做 faststart {len(pending)} 个")

    if args.check or not pending:
        return 0

    ok = fail = skipped = 0
    with ThreadPoolExecutor(max_workers=max(1, args.workers)) as pool:
        for path, (good, msg) in zip(pending, pool.map(remux, pending)):
            if good:
                if msg == "skip":
                    skipped += 1
                else:
                    ok += 1
                    print(f"  ok   {path.name}")
            else:
                fail += 1
                print(f"  FAIL {path.name}: {msg}")

    print(f"完成：remux {ok}，跳过 {skipped}，失败 {fail}")
    return 0 if fail == 0 else 1


if __name__ == "__main__":
    sys.exit(main())