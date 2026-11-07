"""
生成勾股定理讲解的分段配音（每段一个 mp3，便于与画面精确对齐）
"""
import asyncio
import json
import subprocess
from pathlib import Path

import edge_tts

AUDIO_DIR = Path("D:/pythonworkspace/MathAnimations/audio_segments")
VOICE = "zh-CN-YunxiNeural"   # 男声，清晰
RATE = "-8%"                  # 稍微放慢，便于理解

SEGMENTS = [
    "先看一个生活中的问题：一把梯子斜靠在墙上，梯子底端离墙三米，墙高四米。请问，梯子有多长？",
    "我们把地面、墙面和梯子，看成一个直角三角形。两条直角边，分别是三米和四米；斜边，就是梯子的长度。",
    "古人有一个巧妙的办法：在每条边上，都向外画一个正方形。边长是三米的正方形，面积是九；边长是四米的正方形，面积是十六。",
    "九加十六，等于二十五。而二十五，正好是五的平方。所以，梯子长五米。",
    "为什么一定相等呢？我们做个小实验：把这两个正方形，切成一个个边长一米的小方格。",
    "九个小方格，加上十六个小方格，一共是二十五格。",
    "现在，把它们全部搬进斜边上的大正方形。看，正好铺满，一格不剩！",
    "这就说明：两条直角边上的正方形面积之和，等于斜边上的正方形面积。",
    "所以，对任意直角三角形都成立：a 的平方，加 b 的平方，等于 c 的平方。这就是勾股定理。",
]


def duration_of(path: Path) -> float:
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=noprint_wrappers=1:nokey=1", str(path)],
        capture_output=True, text=True,
    )
    return float(out.stdout.strip())


async def main():
    AUDIO_DIR.mkdir(parents=True, exist_ok=True)
    timings = []
    for i, text in enumerate(SEGMENTS):
        path = AUDIO_DIR / f"seg_{i:02d}.mp3"
        communicate = edge_tts.Communicate(text, VOICE, rate=RATE)
        await communicate.save(str(path))
        d = duration_of(path)
        timings.append({"index": i, "file": str(path).replace("\\", "/"),
                        "text": text, "duration": round(d, 3)})
        print(f"seg_{i:02d}: {d:.2f}s  {text[:18]}...")

    (AUDIO_DIR / "timings.json").write_text(
        json.dumps(timings, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    total = sum(t["duration"] for t in timings)
    print(f"\n总时长: {total:.1f}s")


if __name__ == "__main__":
    asyncio.run(main())