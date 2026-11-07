# -*- coding: utf-8 -*-
"""乘法：3 × 4 到底在数什么。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


class ChengfaScene(NarratedScene):
    lesson = "chengfa-yiyi"

    # 点阵参数
    OX, OY, S = -2.6, 0.35, 1.0

    def construct(self):
        # ================= 0. 三排桌子 =================
        self.section(0, "三排桌子，每排四人")

        rows = VGroup()
        for j in range(3):
            y = 1.5 - j * 1.05
            bar = RoundedRectangle(
                corner_radius=0.12, width=5.2, height=0.78,
                stroke_color=DIM, stroke_width=2,
                fill_color=WHITE, fill_opacity=0.05,
            ).move_to([-1.9, y, 0])
            row = VGroup(bar)
            for i in range(4):
                row.add(
                    Circle(radius=0.145, color=BLUE, fill_opacity=0.95, stroke_width=0)
                    .move_to([-3.75 + i * 0.83, y, 0])
                )
            rows.add(row)

        self.play(LaggedStart(*[FadeIn(r, shift=RIGHT * 0.2) for r in rows],
                              lag_ratio=0.25), run_time=1.6)

        tag_rows = txt("3 排", size=30, color=GOLD).move_to([3.0, 1.55, 0])
        tag_each = txt("每排 4 人", size=30, color=GOLD).move_to([3.0, 0.85, 0])
        question = txt("一共多少人？", size=40, color=CHALK).move_to([3.0, -0.55, 0])
        self.play(FadeIn(tag_rows), FadeIn(tag_each), run_time=0.6)
        self.play(FadeIn(question, shift=UP * 0.1), run_time=0.6)
        self.finish_section()

        # ================= 1. 一个一个数 =================
        self.section(1, "数一数：4、8、12")
        self.play(FadeOut(tag_rows), FadeOut(tag_each), FadeOut(question), run_time=0.4)

        counter = txt("0", size=64, color=GOLD).move_to([3.3, 0.8, 0])
        counter_lab = txt("已经数到", size=26, color=DIM).next_to(counter, UP, buff=0.18)
        self.play(FadeIn(counter), FadeIn(counter_lab), run_time=0.4)

        for j, value in enumerate(["4", "8", "12"]):
            self.play(
                Indicate(rows[j], color=GOLD, scale_factor=1.04),
                run_time=0.85,
            )
            new = txt(value, size=64, color=GOLD).move_to(counter)
            self.play(Transform(counter, new), run_time=0.25)

        hint = txt("每次都数，太慢了", size=28, color=ORANGE).move_to([3.3, -0.8, 0])
        self.play(FadeIn(hint, shift=UP * 0.1), run_time=0.5)
        self.finish_section()

        # ================= 2. 写成乘法 =================
        self.section(2, "三个 4 相加，写成 3 × 4")
        self.play(
            FadeOut(rows), FadeOut(counter), FadeOut(counter_lab), FadeOut(hint),
            run_time=0.6,
        )

        add_line = txt("4 + 4 + 4", size=64, color=CHALK).move_to([0, 0.85, 0])
        add_note = txt("3 个 4 相加", size=30, color=DIM).move_to([0, -0.05, 0])
        self.play(FadeIn(add_line, shift=DOWN * 0.1), run_time=0.8)
        self.play(FadeIn(add_note), run_time=0.4)

        mult_line = txt("3 × 4", size=76, color=GOLD).move_to([0, 0.85, 0])
        mult_note = txt("读作：三乘四", size=30, color=CHALK).move_to([0, -0.05, 0])
        self.play(Transform(add_line, mult_line), Transform(add_note, mult_note), run_time=0.9)

        why = txt("乘法，就是把相同的加数合起来写", size=28, color=GREEN).move_to([0, -1.35, 0])
        self.play(FadeIn(why, shift=UP * 0.1), run_time=0.6)
        self.finish_section()

        # ================= 3. 点阵：3 行 4 列 =================
        self.section(3, "3 行，每行 4 个点")
        self.play(FadeOut(add_line), FadeOut(add_note), FadeOut(why), run_time=0.5)

        dots = VGroup()
        for j in range(3):
            for i in range(4):
                dots.add(self.dot(self.OX + (i - 1.5) * self.S,
                                  self.OY + (1 - j) * self.S,
                                  color=BLUE, r=0.17))
        self.play(LaggedStart(*[GrowFromCenter(d) for d in dots], lag_ratio=0.06), run_time=1.4)

        row_brace = Brace(dots, LEFT, color=GOLD, buff=0.22)
        row_lab = txt("3 行", size=28, color=GOLD).next_to(row_brace, LEFT, buff=0.14)
        col_brace = Brace(dots, UP, color=GOLD, buff=0.22)
        col_lab = txt("每行 4 个", size=28, color=GOLD).next_to(col_brace, UP, buff=0.14)
        self.play(GrowFromCenter(row_brace), FadeIn(row_lab), run_time=0.5)
        self.play(GrowFromCenter(col_brace), FadeIn(col_lab), run_time=0.5)

        eq1 = txt("3 × 4 = 12", size=54, color=GOLD).move_to([3.35, 0.55, 0])
        eq1_note = txt("一共 12 个点", size=28, color=DIM).next_to(eq1, DOWN, buff=0.3)
        self.play(FadeIn(eq1, shift=DOWN * 0.1), run_time=0.7)
        self.play(FadeIn(eq1_note), run_time=0.4)
        self.finish_section()

        # ================= 4. 两种读法 =================
        self.section(4, "3 × 4 和 4 × 3 一样吗？")
        self.play(FadeOut(eq1), FadeOut(eq1_note), run_time=0.4)

        line_a = txt("3 × 4 = 4 + 4 + 4 = 12", size=30, color=CHALK).move_to([2.55, 1.15, 0])
        line_b = txt("4 × 3 = 3 + 3 + 3 + 3 = 12", size=30, color=CHALK).move_to([2.55, 0.2, 0])
        tag_a = txt("3 个 4", size=24, color=GOLD).next_to(line_a, UP, buff=0.22)
        tag_b = txt("4 个 3", size=24, color=GOLD).next_to(line_b, UP, buff=0.22)

        self.play(FadeIn(tag_a), FadeIn(line_a, shift=RIGHT * 0.1), run_time=0.7)
        self.play(FadeIn(tag_b), FadeIn(line_b, shift=RIGHT * 0.1), run_time=0.7)

        same = txt("结果都是 12", size=34, color=GREEN).move_to([2.55, -0.85, 0])
        self.play(FadeIn(same, scale=0.9), run_time=0.5)
        self.finish_section()

        # ================= 5. 转过来看：交换律 =================
        self.section(5, "把点阵转过来：总数没变")
        self.play(FadeOut(line_a), FadeOut(line_b), FadeOut(tag_a), FadeOut(tag_b),
                  FadeOut(same), run_time=0.5)
        self.play(FadeOut(row_brace), FadeOut(row_lab), FadeOut(col_brace), FadeOut(col_lab),
                  run_time=0.35)

        # 转置：3 行 4 列 -> 4 行 3 列
        moves = []
        for idx, d in enumerate(dots):
            j, i = divmod(idx, 4)
            tx = self.OX + (j - 1.0) * self.S
            ty = self.OY + (1.5 - i) * self.S
            moves.append(d.animate.move_to([tx, ty, 0]))
        self.play(*moves, lag_ratio=0.02, run_time=1.5)

        row_brace2 = Brace(dots, LEFT, color=GOLD, buff=0.22)
        row_lab2 = txt("4 行", size=28, color=GOLD).next_to(row_brace2, LEFT, buff=0.14)
        col_brace2 = Brace(dots, UP, color=GOLD, buff=0.22)
        col_lab2 = txt("每行 3 个", size=28, color=GOLD).next_to(col_brace2, UP, buff=0.14)
        self.play(GrowFromCenter(row_brace2), FadeIn(row_lab2), run_time=0.5)
        self.play(GrowFromCenter(col_brace2), FadeIn(col_lab2), run_time=0.5)

        eq2 = txt("4 × 3 = 12", size=48, color=GOLD).move_to([3.3, 0.55, 0])
        law = txt("交换律：交换两个因数，积不变", size=26, color=GREEN).move_to([3.3, -0.45, 0])
        self.play(FadeIn(eq2, shift=DOWN * 0.1), run_time=0.6)
        self.play(FadeIn(law), run_time=0.5)
        self.finish_section()

        # ================= 6. 收束 =================
        self.section(6, "记住：乘法是数出来的")
        self.play(
            FadeOut(dots), FadeOut(row_brace2), FadeOut(row_lab2),
            FadeOut(col_brace2), FadeOut(col_lab2), FadeOut(eq2), FadeOut(law),
            run_time=0.6,
        )

        big = txt("3 × 4 = 12", size=86, color=GOLD).move_to([0, 0.75, 0])
        meaning = txt("3 个 4 相加", size=32, color=CHALK).next_to(big, DOWN, buff=0.45)
        final = txt("乘法 = 相同加数的简便写法", size=30, color=GREEN).next_to(meaning, DOWN, buff=0.4)

        self.play(Write(big), run_time=1.0)
        self.play(FadeIn(meaning, shift=UP * 0.1), run_time=0.5)
        self.play(FadeIn(final, shift=UP * 0.1), run_time=0.5)
        self.finish_section()

        self.play(FadeOut(big), FadeOut(meaning), FadeOut(final), run_time=0.8)