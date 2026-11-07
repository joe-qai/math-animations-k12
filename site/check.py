# -*- coding: utf-8 -*-
"""静态站点自检：链接、视频、题目、章节数量。"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

def check_links() -> None:
    bad = []
    for page in sorted(ROOT.glob("*.html")) + sorted((ROOT / "labs").glob("*.html")):
        text = page.read_text(encoding="utf-8")
        for match in re.finditer(r'(?:href|src)="([^"]+)"', text):
            url = match.group(1)
            if url.startswith(("http", "data:", "#", "mailto:")):
                continue
            target = (page.parent / url.split("#")[0]).resolve()
            if not target.exists():
                bad.append((page.relative_to(ROOT).as_posix(), url))
    print(f"[LINKS] broken={len(bad)}")
    for item in bad[:30]:
        print("   ", item)


def check_pages() -> None:
    import json

    data = {}
    path = ROOT / "assets" / "videos" / "chapters.json"
    if path.exists():
        data = json.loads(path.read_text(encoding="utf-8"))
    lessons = sorted(ROOT.glob("lesson-*.html"))
    print(f"[PAGES] lesson pages={len(lessons)}")
    for page in lessons:
        text = page.read_text(encoding="utf-8")
        q = len(re.findall(r'class="q" data-answer=', text))
        video = re.search(r'<source src="([^"]+)"', text)
        size = (ROOT / video.group(1)).stat().st_size / 1024 / 1024 if video else 0
        has_poster = 'poster="assets/videos/covers/' in text
        print(f"   {page.name:26s} questions={q} video={size:.1f}MB cover={has_poster}")


def check_quiz_answers() -> None:
    import sys
    sys.path.insert(0, str(ROOT / "site"))
    from lessons import LESSONS
    for lesson in LESSONS:
        answers = [q["answer"] for q in lesson["questions"]]
        options = {len(q["options"]) for q in lesson["questions"]}
        print(f"   {lesson['id']:24s} answers={answers} option_counts={sorted(options)}")


if __name__ == "__main__":
    check_links()
    check_pages()
    check_quiz_answers()