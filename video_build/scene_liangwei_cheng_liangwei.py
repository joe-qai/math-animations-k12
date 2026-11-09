# -*- coding: utf-8 -*-
"""两位数乘两位数：23 × 14。三年级下册「乘法」。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


def num_row(s: str, x_right: float, y: float, size: int = 46,
            color: str = CHALK, pitch: float = 0.62) -> VGroup:
    g = VGroup()
    for k, ch in enumerate(s):
        g.add(txt(ch, size=size, color=color).move_to(
            [x_right - pitch * (len(s) - 1 - k), y, 0]))
    return g


class LiangweiChengLiangweiScene(NarratedScene):
    lesson = "liangwei-cheng-liangwei"

    def construct(self):
        # ---------- 0. 生活问题 ----------
        self.section(0, "每排 23 个座位，共 14 排")

        rows = []
        for r in range(14):
            row = VGroup()
            for c in range(23):
                row.add(Square(side_length=0.082, stroke_width=0.6, stroke_color=BG,
                               fill_color=BLUE if r < 10 else GOLD, fill_opacity=0.5
                               ).move_to([-2.95 + c * 0.1, 1.25 - r * 0.1, 0]))
            rows.append(row)
        top10 = VGroup(*rows[:10])
        bottom4 = VGroup(*rows[10:])
        seats = VGroup(*rows)
        self.play(LaggedStart(*[FadeIn(rw, shift=DOWN * 0.06) for rw in rows],
                              lag_ratio=0.06), run_time=1.5)

        seats_lab = txt("每排 23 个", size=28, color=BLUE).move_to([0.85, 1.0, 0])
        rows_lab = txt("一共 14 排", size=28, color=GOLD).move_to([0.85, 0.4, 0])
        self.play(FadeIn(seats_lab), FadeIn(rows_lab), run_time=0.6)

        eq = txt("23 × 14 = ?", size=62, color=GOLD).move_to([-3.0, -1.45, 0])
        q = txt("这个礼堂能坐多少人？", size=32, color=CHALK).move_to([-3.0, -2.35, 0])
        self.play(Write(eq), run_time=0.9)
        self.play(FadeIn(q, shift=UP * 0.1), run_time=0.6)
        self.finish_section()

        # ---------- 1. 估算 ----------
        self.section(1, "先估一估：比 200 大")
        self.play(FadeOut(eq), FadeOut(q), FadeOut(seats_lab), FadeOut(rows_lab),
                  seats.animate.scale(0.78).move_to([-4.55, 0.25, 0]), run_time=0.9)

        e1 = txt("23 ≈ 20", size=44, color=BLUE).move_to([0.6, 1.55, 0])
        e2 = txt("14 ≈ 10", size=44, color=BLUE).move_to([3.9, 1.55, 0])
        e3 = txt("20 × 10 = 200", size=48, color=GOLD).move_to([2.25, 0.5, 0])
        self.play(Write(e1), run_time=0.6)
        self.play(Write(e2), run_time=0.6)
        self.play(Write(e3), run_time=0.8)

        n1 = txt("两个数都估小了", size=30, color=DIM).move_to([2.25, -0.75, 0])
        n2 = txt("答案应该比 200 大", size=36, color=GREEN).move_to([2.25, -1.6, 0])
        self.play(FadeIn(n1), run_time=0.4)
        self.play(FadeIn(n2, shift=UP * 0.1), run_time=0.6)
        self.finish_section()

        # ---------- 2. 拆开算 ----------
        self.section(2, "拆开算：十排 + 四排")
        self.play(FadeOut(e1), FadeOut(e2), FadeOut(e3),
                  FadeOut(n1), FadeOut(n2), run_time=0.55)

        split = txt("14 排 = 10 排 + 4 排", size=46, color=GOLD).move_to([2.2, 2.55, 0])
        self.play(Write(split), run_time=0.8)

        br10 = Brace(top10, RIGHT, color=BLUE, buff=0.08)
        br4 = Brace(bottom4, RIGHT, color=GOLD, buff=0.08)
        l10 = txt("10 排", size=24, color=BLUE).next_to(br10, RIGHT, buff=0.12)
        l4 = txt("4 排", size=24, color=GOLD).next_to(br4, RIGHT, buff=0.12)
        self.play(GrowFromCenter(br10), FadeIn(l10), run_time=0.6)
        self.play(GrowFromCenter(br4), FadeIn(l4), run_time=0.6)

        b1 = label_box("23 × 10 = 230", size=34, color=BLUE).move_to([1.55, 1.15, 0])
        b2 = label_box("23 × 4 = 92", size=34, color=BLUE).move_to([1.55, 0.05, 0])
        self.play(FadeIn(b1, shift=UP * 0.1), run_time=0.6)
        self.play(FadeIn(b2, shift=UP * 0.1), run_time=0.6)

        total = txt("230 + 92 = 322", size=50, color=GOLD).move_to([1.55, -1.55, 0])
        self.play(Write(total), run_time=0.9)

        tip = txt("十排 + 四排，新问题变成旧知识", size=28, color=GREEN).move_to([1.55, -2.55, 0])
        self.play(FadeIn(tip, shift=UP * 0.1), run_time=0.6)
        self.finish_section()

        # ---------- 3. 竖式第一层 ----------
        self.section(3, "竖式：先乘个位")
        sec2 = VGroup(split, br10, br4, l10, l4, b1, b2, total, tip)
        self.play(FadeOut(seats), FadeOut(sec2), run_time=0.6)

        n23 = num_row("23", 1.15, 1.92)
        sgn = txt("×", size=40, color=CHALK).move_to([-0.55, 1.20, 0])
        n14 = num_row("14", 1.15, 1.20)
        r1 = Line([-0.95, 0.80, 0], [1.75, 0.80, 0], color=CHALK, stroke_width=3)
        self.play(Write(n23), run_time=0.5)
        self.play(FadeIn(sgn), Write(n14), run_time=0.6)
        self.play(Create(r1), run_time=0.4)

        h1 = txt("个位：4 × 23", size=30, color=GOLD).move_to([4.35, 1.85, 0])
        self.play(FadeIn(h1), run_time=0.4)

        carry = txt("1", size=24, color=ORANGE).move_to([0.53, 2.42, 0])
        p1 = num_row("92", 1.15, 0.22, color=CHALK)
        self.play(FadeIn(carry, shift=DOWN * 0.1), run_time=0.4)
        self.play(Write(p1), run_time=0.5)

        h1b = txt("3×4=12，写 2 进 1", size=28, color=ORANGE).move_to([4.3, 1.05, 0])
        h1c = txt("2×4+1=9", size=28, color=ORANGE).move_to([4.3, 0.45, 0])
        self.play(FadeIn(h1b), run_time=0.5)
        self.play(FadeIn(h1c), run_time=0.5)

        hint = txt("先只乘个位，十位留到下一层", size=26, color=DIM).move_to([-3.3, -1.4, 0])
        self.play(FadeIn(hint, shift=UP * 0.1), run_time=0.5)
        self.finish_section()

        # ---------- 4. 竖式第二层 ----------
        self.section(4, "再乘十位：第二层要错位")
        self.play(FadeOut(h1), FadeOut(h1b), FadeOut(h1c), FadeOut(hint),
                  FadeOut(carry), run_time=0.45)

        h2 = txt("十位：1 × 23", size=30, color=GOLD).move_to([4.35, 1.85, 0])
        p2 = num_row("23", 0.53, -0.45, color=BLUE)
        self.play(FadeIn(h2), run_time=0.45)
        self.play(Write(p2), run_time=0.6)

        off = Arrow([1.95, -0.45, 0], [1.52, -0.45, 0], color=BLUE,
                    stroke_width=2.5, buff=0, max_tip_length_to_length_ratio=0.35)
        h2b = txt("末位写在十位上", size=28, color=BLUE).move_to([4.35, 0.75, 0])
        h2c = txt("表示 23 个十 = 230", size=28, color=BLUE).move_to([4.2, 0.15, 0])
        self.play(GrowArrow(off), run_time=0.5)
        self.play(FadeIn(h2b), run_time=0.45)
        self.play(FadeIn(h2c), run_time=0.45)

        r2 = Line([-0.95, -0.95, 0], [1.75, -0.95, 0], color=CHALK, stroke_width=3)
        ans = num_row("322", 1.15, -1.55, color=GOLD)
        self.play(Create(r2), run_time=0.4)
        self.play(Write(ans), run_time=0.8)

        fin = txt("92 + 230 = 322", size=34, color=GREEN).move_to([3.6, -1.9, 0])
        self.play(FadeIn(fin), run_time=0.5)
        self.finish_section()

        # ---------- 5. 易错 ----------
        self.section(5, "错位没对齐，答案小十倍")
        self.play(FadeOut(n23), FadeOut(sgn), FadeOut(n14), FadeOut(r1), FadeOut(p1),
                  FadeOut(p2), FadeOut(off), FadeOut(h2), FadeOut(h2b), FadeOut(h2c),
                  FadeOut(r2), FadeOut(ans), FadeOut(fin), run_time=0.6)

        w1 = txt("✗ 不错位：92 + 23 = 115", size=34, color=RED).move_to([-2.9, 1.45, 0])
        w2 = txt("✓ 错位：92 + 230 = 322", size=34, color=GREEN).move_to([-2.9, 0.65, 0])
        self.play(FadeIn(w1), run_time=0.6)
        self.play(FadeIn(w2), run_time=0.6)

        chk = txt("估算检查：322 比 200 大，合理", size=30, color=GOLD).move_to([-2.9, -0.4, 0])
        self.play(FadeIn(chk, shift=UP * 0.1), run_time=0.7)

        m23 = num_row("23", 5.4, 1.05, size=38, pitch=0.52)
        m14 = num_row("14", 5.4, 0.42, size=38, pitch=0.52)
        msgn = txt("×", size=34, color=CHALK).move_to([3.95, 0.42, 0])
        mr1 = Line([3.6, 0.10, 0], [5.85, 0.10, 0], color=CHALK, stroke_width=2.5)
        mp1 = num_row("92", 5.4, -0.5, size=38, pitch=0.52)
        mp2 = num_row("230", 5.4, -1.2, size=38, pitch=0.52, color=GREEN)
        mr2 = Line([3.6, -1.75, 0], [5.85, -1.75, 0], color=CHALK, stroke_width=2.5)
        mans = num_row("322", 5.4, -2.35, size=38, pitch=0.52, color=GOLD)
        box = SurroundingRectangle(mp2, color=GREEN, buff=0.1, stroke_width=2)
        vlab = txt("正确竖式", size=22, color=DIM).move_to([4.7, 1.62, 0])
        self.play(FadeIn(vlab), FadeIn(m23), FadeIn(msgn), FadeIn(m14), Create(mr1), run_time=0.6)
        self.play(FadeIn(mp1), run_time=0.4)
        self.play(Write(mp2), Create(box), run_time=0.7)
        self.play(Create(mr2), Write(mans), run_time=0.7)

        mcap = txt("写全 230，就不会错位", size=24, color=GREEN).move_to([4.7, -2.9, 0])
        self.play(FadeIn(mcap, shift=UP * 0.1), run_time=0.5)
        self.finish_section()

        # ---------- 6. 口诀 ----------
        self.section(6, "三步：拆、乘、错位加")
        err = VGroup(w1, w2, chk, vlab, m23, msgn, m14, mr1, mp1, mp2, mr2, mans, box, mcap)
        self.play(FadeOut(err), run_time=0.55)

        big = txt("23 × 14 = 322", size=58, color=GOLD).move_to([0, 2.15, 0])
        self.play(Write(big), run_time=0.8)

        k1 = label_box("拆开算", size=30, color=CHALK).move_to([-3.4, 0.35, 0])
        k2 = label_box("分层乘", size=30, color=CHALK).move_to([0, 0.35, 0])
        k3 = label_box("错位加", size=30, color=GOLD).move_to([3.4, 0.35, 0])
        self.play(LaggedStart(*[FadeIn(m, shift=UP * 0.1) for m in (k1, k2, k3)],
                             lag_ratio=0.2), run_time=1.2)

        final = txt("先分再合，两位数乘两位数就不难", size=32, color=GREEN).move_to([0, -1.5, 0])
        self.play(FadeIn(final, shift=UP * 0.1), run_time=0.6)
        self.finish_section()

        self.play(FadeOut(big), FadeOut(k1), FadeOut(k2), FadeOut(k3),
                  FadeOut(final), run_time=0.7)
