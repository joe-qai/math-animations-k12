# -*- coding: utf-8 -*-
"""等差数列求和：倒序相加，一眼看懂。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


class DengchaScene(NarratedScene):
    lesson = "dengcha-shulie"

    S = 0.4
    X0, Y0 = -5.0, -2.2

    def construct(self):
        s = self.S
        x0, y0 = self.X0, self.Y0
        rows = VGroup()
        for k in range(1, 11):
            row = VGroup()
            for i in range(k):
                row.add(self.dot(x0 + (i + 0.5) * s, y0 + (k - 0.5) * s,
                                 color=BLUE, r=0.13))
            rows.add(row)

        # ================= 0. 问题 =================
        self.section(0, "1 加到 10，等于多少？")
        q = VGroup(
            txt("1 + 2 + 3 + … + 10", size=34, color=CHALK),
            txt("= ？", size=44, color=GOLD),
        ).arrange(DOWN, buff=0.25).move_to([2.9, 1.3, 0])
        self.play(FadeIn(q, shift=DOWN * 0.1), run_time=0.8)
        slow = txt("一个一个加，太慢了", size=26, color=ORANGE).move_to([2.9, 0.1, 0])
        self.play(FadeIn(slow), run_time=0.5)
        self.finish_section()

        # ================= 1. 摆成阶梯 =================
        self.section(1, "把 1 到 10 摆成阶梯")
        self.play(FadeOut(q), FadeOut(slow), run_time=0.4)

        self.play(
            LaggedStart(*[FadeIn(r, shift=UP * 0.08) for r in rows], lag_ratio=0.08),
            run_time=2.0,
        )

        row_lab = txt("10 行", size=24, color=DIM).move_to([2.9, 1.2, 0])
        col_lab = txt("每行多 1 个", size=24, color=DIM).move_to([2.9, 0.55, 0])
        self.play(FadeIn(row_lab), FadeIn(col_lab), run_time=0.5)
        self.finish_section()

        # ================= 2. 复制一份，倒过来 =================
        self.section(2, "复制一份，倒过来盖上去")
        self.play(FadeOut(row_lab), FadeOut(col_lab), run_time=0.3)

        stair = VGroup(*rows)
        ghost = stair.copy().set_color(GOLD)
        ghost.shift(RIGHT * 0.75 + UP * 0.7)
        self.play(FadeIn(ghost), run_time=0.6)

        center = np.array([x0 + 5 * s, y0 + 5 * s, 0])
        target = stair.copy().set_color(GOLD)
        target.rotate(PI, about_point=center)
        target.shift(RIGHT * s)
        self.play(Transform(ghost, target), run_time=1.8)
        self.finish_section()

        # ================= 3. 拼成长方形 =================
        self.section(3, "拼成一个长方形：10 行，11 列")
        outline = Rectangle(
            width=11 * s, height=10 * s,
            color=CHALK, stroke_width=2,
        ).move_to([x0 + 11 * s / 2, y0 + 10 * s / 2, 0])
        self.play(Create(outline), run_time=0.8)

        lab_c = txt("11 个", size=24, color=GOLD).move_to([x0 + 11 * s / 2, y0 - 0.32, 0])
        lab_r = txt("10 行", size=24, color=GOLD).rotate(PI / 2).move_to([x0 - 0.38, y0 + 5 * s, 0])
        self.play(FadeIn(lab_c), FadeIn(lab_r), run_time=0.5)

        mult = txt("10 × 11 = 110", size=36, color=GOLD).move_to([2.9, 1.1, 0])
        self.play(FadeIn(mult, shift=DOWN * 0.1), run_time=0.6)
        self.finish_section()

        # ================= 4. 一半 =================
        self.section(4, "原来那一份，是它的一半")

        note = VGroup(
            txt("两份一共 110 个点", size=26, color=DIM),
            txt("一份就是 55 个", size=36, color=GOLD),
        ).arrange(DOWN, buff=0.25).move_to([2.9, 0.25, 0])
        self.play(FadeIn(note, shift=RIGHT * 0.1), run_time=0.7)

        half = txt("110 ÷ 2 = 55", size=40, color=GREEN).move_to([2.9, -0.85, 0])
        self.play(FadeIn(half, scale=0.9), run_time=0.6)
        self.finish_section()

        # ================= 5. 名字：倒序相加 =================
        self.section(5, "这个方法，叫倒序相加")
        self.play(FadeOut(note), FadeOut(half), FadeOut(mult), run_time=0.5)

        name = txt("倒序相加", size=52, color=GOLD).move_to([2.9, 1.0, 0])
        explain = VGroup(
            txt("正着写一遍", size=26, color=BLUE),
            txt("倒着再写一遍", size=26, color=GOLD),
            txt("两式相加，每一列都相等", size=26, color=CHALK),
        ).arrange(DOWN, buff=0.22).move_to([2.9, -0.15, 0])
        self.play(FadeIn(name, shift=DOWN * 0.1), run_time=0.7)
        self.play(FadeIn(explain, shift=UP * 0.1), run_time=0.7)
        self.finish_section()

        # ================= 6. 公式 =================
        self.section(6, "公式：首项加末项，乘项数，除以 2")
        self.play(FadeOut(name), FadeOut(explain), run_time=0.4)

        formula = txt("S = (首项 + 末项) × 项数 ÷ 2", size=27, color=GOLD).move_to([2.9, 1.15, 0])
        plug = VGroup(
            txt("(1 + 10) × 10 ÷ 2", size=28, color=CHALK),
            txt("= 11 × 10 ÷ 2", size=28, color=CHALK),
            txt("= 55", size=40, color=GREEN),
        ).arrange(DOWN, buff=0.28).move_to([2.9, -0.2, 0])
        self.play(FadeIn(formula, shift=DOWN * 0.1), run_time=0.7)
        self.play(FadeIn(plug[0]), run_time=0.35)
        self.play(FadeIn(plug[1]), run_time=0.35)
        self.play(FadeIn(plug[2], scale=0.9), run_time=0.45)
        self.finish_section()

        self.play(FadeOut(stair), FadeOut(ghost), FadeOut(outline),
                  FadeOut(lab_c), FadeOut(lab_r),
                  FadeOut(formula), FadeOut(plug), run_time=0.8)