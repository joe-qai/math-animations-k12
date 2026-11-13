# -*- coding: utf-8 -*-
"""生成课时封面：直接取成片抽帧（posters）作为封面画面。

标题已经在课程卡片的文字区呈现，封面不再重复叠加标题，改为展示视频内容本身，
信息量更大、也更容易吸引点击。

- 统一裁切 / 缩放到 1280×720（16:9，与卡片封面比例一致）
- 轻微提亮与增饱和，避免缩到卡片尺寸后显得发灰

用法：python site/make_covers.py [lesson_id ...]
"""

from __future__ import annotations

import sys
from pathlib import Path

from PIL import Image, ImageEnhance

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "site"))

from lessons import LESSONS  # noqa: E402

POSTER_DIR = ROOT / "assets" / "videos" / "posters"
COVER_DIR = ROOT / "assets" / "videos" / "covers"

W, H = 1280, 720


def fit_16x9(img: Image.Image) -> Image.Image:
    """等比缩放并居中裁切到 16:9。"""
    scale = max(W / img.width, H / img.height)
    img = img.resize((round(img.width * scale), round(img.height * scale)), Image.LANCZOS)
    left = (img.width - W) // 2
    top = (img.height - H) // 2
    return img.crop((left, top, left + W, top + H))


def build_cover(lesson: dict) -> bool:
    poster = POSTER_DIR / f"{lesson['id']}.jpg"
    if not poster.exists():
        print(f"[SKIP] {lesson['id']}: no poster")
        return False

    img = fit_16x9(Image.open(poster).convert("RGB"))

    # 轻微提亮/增饱和，让缩到卡片尺寸后的画面依然清晰有精神
    img = ImageEnhance.Brightness(img).enhance(1.03)
    img = ImageEnhance.Color(img).enhance(1.12)
    img = ImageEnhance.Contrast(img).enhance(1.04)

    COVER_DIR.mkdir(parents=True, exist_ok=True)
    out = COVER_DIR / f"{lesson['id']}.jpg"
    img.save(out, quality=86, optimize=True)
    print(f"[OK] {lesson['id']:24s} -> {out.stat().st_size // 1024}KB")
    return True


def main() -> None:
    wanted = set(sys.argv[1:])
    for lesson in LESSONS:
        if wanted and lesson["id"] not in wanted:
            continue
        build_cover(lesson)


if __name__ == "__main__":
    main()
