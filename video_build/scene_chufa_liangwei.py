# -*- coding: utf-8 -*-
"""除数是两位数的除法：84 ÷ 21、96 ÷ 22。四年级上册「除法」。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


def dot_grid(n: int, cols: int, x0: float, y0: float,
             pitch: float = 0.24, radius: float = 0.065,
             color: str = CHALK) -> tuple[VGroup, list[VGroup]]:
    rows: list[VGroup] = []
    all_dots = VGroup()
    for r in range((n + cols - 1) // cols):
        row = VGroup()
        for c in range(cols):
            idx = r * cols + c
            if idx >= n:
                break
            d = Circle(radius=radius, stroke_width=0, fill_color=color,
                       fill_opacity=0.8).move_to(
                [x0 + c * pitch, y0 - r * pitch, 0])
            row.add(d)
            all_dots.add(d)
        rows.append(row)
    return all_dots, rows


class ChufaLiangweiScene(NarratedScene):
    lesson = "chufa-liangwei"

    def construct(self):
        # ---------- 0. 生活问题 ----------
        self.section(0, "84 本书，每班 21 本")

        books, b84rows = dot_grid(84, 21, -5.95, 0.85)
        self.play(LaggedStart(*[FadeIn(d, scale=0.5) for d in books],
                              lag_ratio=0.01), run_time=1.4)
        n84 = txt("84 本", size=32, color=GOLD).move_to([-3.6, 1.35, 0])
        n21 = txt("每班分 21 本", size=30, color=BLUE).move_to([-3.6, -0.35, 0])
        self.play(FadeIn(n84), run_time=0.4)
        self.play(FadeIn(n21, shift=UP * 0.1), run_time=0.5)

        eq = txt("84 ÷ 21 = ?", size=56, color=GOLD).move_to([3.3, 0.75, 0])
        q = txt("能分给几个班？", size=32, color=CHALK).move_to([3.3, -0.25, 0])
        self.play(Write(eq), run_time=0.9)
        self.play(FadeIn(q, shift=UP * 0.1), run_time=0.5)
        self.finish_section()

        # ---------- 1. 估算 ----------
        self.section(1, "先估一估：商大约是 4")
        self.play(FadeOut(n84), FadeOut(n21), FadeOut(eq), FadeOut(q), run_time=0.5)

        e1 = txt("21 ≈ 20", size=42, color=BLUE).move_to([2.0, 1.6, 0])
        e2 = txt("84 里有几个 20？", size=34, color=CHALK).move_to([3.2, 0.7, 0])
        e3 = txt("80 ÷ 20 = 4", size=46, color=GOLD).move_to([3.2, -0.35, 0])
        e4 = txt("商大约就是 4", size=34, color=GREEN).move_to([3.2, -1.35, 0])
        self.play(Write(e1), run_time=0.6)
        self.play(FadeIn(e2), run_time=0.6)
        self.play(Write(e3), run_time=0.8)
        self.play(FadeIn(e4, shift=UP * 0.1), run_time=0.6)
        self.finish_section()

        # ---------- 2. 试商 ----------
        self.section(2, "试商 4：21 × 4 正好 84")
        self.play(FadeOut(e1), FadeOut(e2), FadeOut(e3), FadeOut(e4), run_time=0.5)

        colors = [BLUE, GREEN, GOLD, PURPLE]
        self.play(*[row.animate.set_fill(c, opacity=0.85)
                    for row, c in zip(b84rows, colors)], run_time=1.2)

        legend = VGroup()
        for k, c in enumerate(colors):
            legend.add(VGroup(
                Circle(radius=0.08, stroke_width=0, fill_color=c, fill_opacity=0.9),
                txt(f"第 {k + 1} 个班", size=24, color=DIM),
            ).arrange(RIGHT, buff=0.12))
        legend.arrange(DOWN, aligned_edge=LEFT, buff=0.22).move_to([2.5, 0.9, 0])
        self.play(LaggedStart(*[FadeIn(m, shift=RIGHT * 0.1) for m in legend],
                              lag_ratio=0.15), run_time=1.0)

        f1 = txt("21 × 4 = 84", size=46, color=GOLD).move_to([3.2, -0.9, 0])
        f2 = txt("正好分完，余 0", size=32, color=GREEN).move_to([3.2, -1.85, 0])
        self.play(Write(f1), run_time=0.8)
        self.play(FadeIn(f2, shift=UP * 0.1), run_time=0.5)
        self.finish_section()

        # ---------- 3. 96 ÷ 22 试商 ----------
        self.section(3, "再看 96 ÷ 22：还是试 4")
        self.play(FadeOut(books), FadeOut(legend), FadeOut(f1), FadeOut(f2), run_time=0.6)

        b96, b96rows = dot_grid(96, 22, -5.95, 1.15)
        self.play(LaggedStart(*[FadeIn(d, scale=0.5) for d in b96],
                              lag_ratio=0.01), run_time=1.2)

        eq2 = txt("96 ÷ 22 = ?", size=54, color=GOLD).move_to([3.2, 1.2, 0])
        s1 = txt("22 ≈ 20", size=40, color=BLUE).move_to([2.6, 0.35, 0])
        s2 = txt("96 里约有 4 个 20", size=32, color=CHALK).move_to([3.2, -0.5, 0])
        s3 = txt("还是先试商 4", size=34, color=GREEN).move_to([3.2, -1.4, 0])
        self.play(Write(eq2), run_time=0.8)
        self.play(Write(s1), run_time=0.5)
        self.play(FadeIn(s2), run_time=0.6)
        self.play(FadeIn(s3, shift=UP * 0.1), run_time=0.5)
        self.finish_section()

        # ---------- 4. 乘、减、比 ----------
        self.section(4, "乘一乘、减一减、比一比")
        self.play(FadeOut(eq2), FadeOut(s1), FadeOut(s2), FadeOut(s3), run_time=0.5)

        full = VGroup(*b96rows[:4])
        rest = b96rows[4]
        self.play(full.animate.set_fill(BLUE, opacity=0.5), run_time=0.8)
        self.play(rest.animate.set_fill(GOLD, opacity=0.95), run_time=0.8)

        br = Brace(rest, DOWN, color=GOLD, buff=0.12)
        brl = txt("余 8", size=28, color=GOLD).next_to(br, DOWN, buff=0.12)
        self.play(GrowFromCenter(br), FadeIn(brl), run_time=0.7)

        f1 = txt("22 × 4 = 88", size=42, color=BLUE).move_to([3.2, 1.5, 0])
        f2 = txt("96 − 88 = 8", size=42, color=CHALK).move_to([3.2, 0.6, 0])
        f3 = txt("8 < 22 ✓ 商 4 合适", size=38, color=GREEN).move_to([3.2, -0.45, 0])
        self.play(Write(f1), run_time=0.7)
        self.play(Write(f2), run_time=0.7)
        self.play(FadeIn(f3, shift=UP * 0.1), run_time=0.6)

        res = txt("96 ÷ 22 = 4 …… 8", size=40, color=GOLD).move_to([3.2, -1.55, 0])
        self.play(Write(res), run_time=0.8)
        self.finish_section()

        # ---------- 5. 调商 ----------
        self.section(5, "商大了往下调，商小了往上调")
        self.play(FadeOut(b96), FadeOut(br), FadeOut(brl),
                  FadeOut(f1), FadeOut(f2), FadeOut(f3), FadeOut(res), run_time=0.6)

        l1 = txt("商小了", size=30, color=ORANGE).move_to([-3.5, 1.75, 0])
        l2 = txt("22 × 3 = 66", size=36, color=CHALK).move_to([-3.5, 0.95, 0])
        l3 = txt("96 − 66 = 30", size=36, color=CHALK).move_to([-3.5, 0.25, 0])
        l4 = txt("30 > 22，余数太大", size=30, color=RED).move_to([-3.5, -0.55, 0])
        l5 = txt("→ 把商调大", size=32, color=GREEN).move_to([-3.5, -1.4, 0])
        self.play(FadeIn(l1), run_time=0.4)
        self.play(Write(l2), run_time=0.5)
        self.play(Write(l3), run_time=0.5)
        self.play(FadeIn(l4), run_time=0.5)
        self.play(FadeIn(l5, shift=UP * 0.1), run_time=0.5)

        r1 = txt("商大了", size=30, color=ORANGE).move_to([3.6, 1.75, 0])
        r2 = txt("22 × 5 = 110", size=36, color=CHALK).move_to([3.6, 0.95, 0])
        r3 = txt("110 > 96", size=36, color=CHALK).move_to([3.6, 0.25, 0])
        r4 = txt("乘出来超过被除数", size=30, color=RED).move_to([3.6, -0.55, 0])
        r5 = txt("→ 把商调小", size=32, color=GREEN).move_to([3.6, -1.4, 0])
        self.play(FadeIn(r1), run_time=0.4)
        self.play(Write(r2), run_time=0.5)
        self.play(Write(r3), run_time=0.5)
        self.play(FadeIn(r4), run_time=0.5)
        self.play(FadeIn(r5, shift=UP * 0.1), run_time=0.5)

        div = Line([0, 1.9, 0], [0, -1.9, 0], color=DIM, stroke_width=1.2, stroke_opacity=0.4)
        self.play(Create(div), run_time=0.4)
        self.finish_section()

        # ---------- 6. 口诀 ----------
        self.section(6, "看成整十数，试商四步走")
        self.play(FadeOut(l1), FadeOut(l2), FadeOut(l3), FadeOut(l4), FadeOut(l5),
                  FadeOut(r1), FadeOut(r2), FadeOut(r3), FadeOut(r4), FadeOut(r5),
                  FadeOut(div), run_time=0.6)

        steps = ["看整十", "乘一乘", "减一减", "比一比"]
        chips = VGroup()
        for k, s in enumerate(steps):
            chips.add(label_box(s, size=30, color=GOLD if k == 3 else CHALK))
        chips.arrange(RIGHT, buff=0.55).move_to([0, 0.75, 0])
        self.play(LaggedStart(*[FadeIn(c, shift=UP * 0.1) for c in chips],
                              lag_ratio=0.2), run_time=1.2)

        rule = txt("余数必须比除数小", size=46, color=GREEN).move_to([0, -0.85, 0])
        self.play(Write(rule), run_time=0.9)

        fin = txt("84 ÷ 21 = 4    96 ÷ 22 = 4 …… 8", size=36, color=GOLD).move_to([0, -2.15, 0])
        self.play(FadeIn(fin, shift=UP * 0.1), run_time=0.7)
        self.finish_section()

        self.play(FadeOut(chips), FadeOut(rule), FadeOut(fin), run_time=0.6)
