# -*- coding: utf-8 -*-
"""从成片里恢复章节起点。

原理：每段解说之间，画面在切换、字幕在淡出，音频必然出现一段 1.5 秒以上的静音。
静音的结束点，就是下一段解说的开口时间，也就是章节起点。
"""

from __future__ import annotations

import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VIDEO_DIR = ROOT / "assets" / "videos"
OUT = VIDEO_DIR / "chapters.json"

CHAPTERS = {
    "coushifa": 7,
    "renshi-tuxing": 7,
    "jiao-renshi": 7,
    "tiaoxing-tongji": 7,
    "celiang-shifenmiao": 7,
    "duowei-cheng-yiwei": 7,
    "chufa-yiwei": 7,
    "changfangxing-mianji": 7,
    "fenshu-chubu": 7,
    "xiaoshu-chubu": 7,
    "pingyi-xuanzhuan": 7,
    "dashu-jianfa": 7,
    "xian-yujiao": 7,
    "yun-suanlv": 7,
    "xiaoshu-cheng": 7,
    "pingxing-sibianxing": 7,
    "zimu-biaoshi": 7,
    "fushu-chubu": 7,
    "kenengxing": 7,
    "xiaoshu-chu": 7,
    "yinshu-beishu": 7,
    "fenshu-xingzhi": 7,
    "fenshu-jiajian": 7,
    "fenshu-chengchu": 7,
    "jianyi-fangcheng": 7,
    "pingxing-mianji": 7,
    "tixing-mianji": 7,
    "changfangti-tiji": 7,
    "yuan-zhouchang": 7,
    "yuan-mianji": 7,
    "baifenshu": 7,
    "lianjia-lianjian": 7,
    "renshi-zhongbiao": 7,
    "fenlei-zhengli": 7,
    "chengfa-yiyi": 7,
    "chufa-yiyi": 7,
    "sanjiaoxing-mianji": 7,
    "yiyuan-yici-fangcheng": 7,
    "wanquan-pingfang": 7,
    "dengcha-shulie": 7,
    "gougu-dingli": 9,
}


def silences(video: Path) -> list[tuple[float, float, float]]:
    out = subprocess.run(
        ["ffmpeg", "-v", "info", "-i", str(video),
         "-af", "silencedetect=noise=-45dB:d=0.4", "-f", "null", "NUL"],
        capture_output=True, text=True, errors="ignore",
    )
    text = out.stderr
    starts = [float(m) for m in re.findall(r"silence_start: ([\d.]+)", text)]
    ends = re.findall(r"silence_end: ([\d.]+) \| silence_duration: ([\d.]+)", text)
    result = []
    for (end, dur), start in zip(ends, starts):
        result.append((start, float(end), float(dur)))
    return result


def main() -> None:
    chapters: dict[str, list[float]] = {}
    for lesson, count in CHAPTERS.items():
        video = VIDEO_DIR / f"{lesson}.mp4"
        if not video.exists():
            print(f"[SKIP] {lesson}: no video")
            continue
        long_gaps = [e for (_s, e, d) in silences(video) if d > 1.5]
        need = count - 1
        if len(long_gaps) != need:
            # 兜底：用配音时长累加（适用于音画严丝合缝、几乎没有静音缝的成片）
            audio = ROOT / "video_build" / "audio" / lesson / "timings.json"
            if not audio.exists():
                audio = ROOT / "audio_segments" / "timings.json"
            data = json.loads(audio.read_text(encoding="utf-8"))
            t, points = 0.0, [0.0]
            for seg in data[:-1]:
                t += seg["duration"]
                points.append(round(t, 1))
            print(f"[FALLBACK] {lesson}: using narration timings {points}")
        else:
            points = [0.0] + [round(e, 2) for e in long_gaps[:need]]
        chapters[lesson] = points
        print(f"[OK] {lesson}: {len(points)} chapters {points}")

    OUT.write_text(json.dumps(chapters, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[DONE] {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()