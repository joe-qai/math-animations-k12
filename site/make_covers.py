# -*- coding: utf-8 -*-
"""生成课时封面：背景取成片抽帧并虚化，标题文字做蒙版，蒙版里放提亮的原图。

- 背景：16:9 裁切 + 高斯模糊 + 压暗
- 蒙版：课时标题（Microsoft YaHei Bold，自动折行、自动缩放）
- 蒙版内：原图提亮后与浅色混合，保证小尺寸卡片上也能看清

用法：python site/make_covers.py [lesson_id ...]
"""

from __future__ import annotations

import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "site"))

from lessons import LESSONS  # noqa: E402

POSTER_DIR = ROOT / "assets" / "videos" / "posters"
COVER_DIR = ROOT / "assets" / "videos" / "covers"
FONT_PATH = Path(r"C:\Windows\Fonts\msyhbd.ttc")

W, H = 1280, 720
PAD = 96  # 文字左右安全边距


def font_size_for(text: str) -> int:
    n = len(text)
    if n <= 4:
        return 132
    if n <= 6:
        return 112
    if n <= 9:
        return 96
    return 88


BREAKS = "：、，,；;· "


def tracked_len(s: str, font: ImageFont.FreeTypeFont, track: int) -> float:
    if not s:
        return 0.0
    return font.getlength(s) + track * (len(s) - 1)


def draw_tracked(draw: ImageDraw.ImageDraw, cx: float, y: float, s: str,
                 font: ImageFont.FreeTypeFont, track: int, fill: int,
                 stroke: int) -> None:
    """逐字绘制，字与字之间留一点空隙，避免粗体汉字笔画粘连。"""
    total = tracked_len(s, font, track)
    x = cx - total / 2
    for ch in s:
        draw.text((x, y), ch, font=font, fill=fill, anchor="lm",
                  stroke_width=stroke, stroke_fill=fill)
        x += font.getlength(ch) + track


def split_even(text: str, font: ImageFont.FreeTypeFont, max_w: int,
               track: int = 0) -> list[str] | None:
    """两行尽量等长；优先在标点处断开。"""
    n = len(text)
    if n < 4:
        return None
    best = None
    for i in range(1, n):
        head, tail = text[:i], text[i:]
        if tracked_len(head, font, track) > max_w or tracked_len(tail, font, track) > max_w:
            continue
        score = abs(i - n / 2)
        if text[i - 1] not in BREAKS:
            score += 2.2  # 非标点处断行略差
        if best is None or score < best[0]:
            best = (score, i)
    if best is None:
        return None
    i = best[1]
    return [text[:i].strip(), text[i:].strip()]


def wrap(text: str, font: ImageFont.FreeTypeFont, max_w: int,
         track: int = 0) -> list[str]:
    if tracked_len(text, font, track) <= max_w:
        return [text]
    even = split_even(text, font, max_w, track)
    if even:
        return even
    lines: list[str] = []
    cur = ""
    for ch in text:
        trial = cur + ch
        if cur and tracked_len(trial, font, track) > max_w:
            lines.append(cur)
            cur = ch
        else:
            cur = trial
    if cur:
        lines.append(cur)
    return lines


def build_cover(lesson: dict) -> bool:
    poster = POSTER_DIR / f"{lesson['id']}.jpg"
    if not poster.exists():
        print(f"[SKIP] {lesson['id']}: no poster")
        return False

    img = Image.open(poster).convert("RGB")
    scale = max(W / img.width, H / img.height)
    img = img.resize((round(img.width * scale), round(img.height * scale)), Image.LANCZOS)
    left = (img.width - W) // 2
    top = (img.height - H) // 2
    img = img.crop((left, top, left + W, top + H))

    # 背景：先缩到极小再放大，彻底抹掉画面结构，只留色块氛围
    small = img.resize((W // 14, H // 14), Image.LANCZOS).filter(ImageFilter.GaussianBlur(6))
    bg = small.resize((W, H), Image.LANCZOS)
    bg = Image.blend(bg, Image.new("RGB", (W, H), (11, 13, 22)), 0.62)

    # 蒙版里：粉笔白到粉笔黄的竖向渐变，保证任何底图上都清晰
    inside = Image.new("RGB", (W, H))
    top_c = (250, 246, 236)
    bot_c = (242, 201, 104)
    px = inside.load()
    for y in range(H):
        t = min(1.0, max(0.0, (y / (H - 1) - 0.35) / 0.65))
        col = tuple(round(top_c[i] + (bot_c[i] - top_c[i]) * t) for i in range(3))
        for x in range(W):
            px[x, y] = col

    # 标题排版
    size = font_size_for(lesson["title"])
    font = ImageFont.truetype(str(FONT_PATH), size)
    track = max(2, round(size * 0.06))
    lines = wrap(lesson["title"], font, W - PAD * 2, track)
    line_h = round(size * 1.26)
    stroke = max(1, round(size * 0.012))
    mid_y = H / 2
    first_y = mid_y + (0 - (len(lines) - 1) / 2) * line_h

    mask = Image.new("L", (W, H), 0)
    draw = ImageDraw.Draw(mask)
    for i, line in enumerate(lines):
        y = first_y + i * line_h
        draw_tracked(draw, W / 2, y, line, font, track, 255, stroke)
    mask = mask.filter(ImageFilter.GaussianBlur(1.1))

    cover = Image.composite(inside, bg, mask)

    COVER_DIR.mkdir(parents=True, exist_ok=True)
    out = COVER_DIR / f"{lesson['id']}.jpg"
    cover.save(out, quality=84, optimize=True)
    print(f"[OK] {lesson['id']:24s} {len(lines)} line(s) {size}px  -> {out.stat().st_size // 1024}KB")
    return True


def main() -> None:
    wanted = set(sys.argv[1:])
    for lesson in LESSONS:
        if wanted and lesson["id"] not in wanted:
            continue
        build_cover(lesson)


if __name__ == "__main__":
    main()