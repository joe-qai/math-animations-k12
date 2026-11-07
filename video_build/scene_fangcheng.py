# -*- coding: utf-8 -*-
"""一元一次方程：像天平一样，两边同时做同一件事。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


class FangchengScene(NarratedScene):
    lesson = "yiyuan-yici-fangcheng"

    BEAM_Y = 1.0

    def x_block(self, x: float, y: float = 1.32) -> VGroup:
        box = RoundedRectangle(
            corner_radius=0.08, width=0.62, height=0.62,
            stroke_color=BLUE, stroke_width=2.5,
            fill_color=BLUE, fill_opacity=0.18,
        )
        lab = txt("x", size=32, color=BLUE)
        g = VGroup(box, lab).move_to([x, y, 0])
        return g

    def construct(self):
        # ================= 0. 天平与方程 =================
        self.section(0, "天平平衡：2x + 3 = 11")

        fulcrum = Polygon(
            [-0.85, 0.0, 0], [0.85, 0.0, 0], [0.0, self.BEAM_Y, 0],
            color=DIM, fill_color=DIM, fill_opacity=0.18, stroke_width=2,
        )
        beam = Line([-4.4, self.BEAM_Y, 0], [4.4, self.BEAM_Y, 0],
                    color=CHALK, stroke_width=5)
        pivot = Dot([0, self.BEAM_Y, 0], radius=0.07, color=GOLD)

        left_blocks = VGroup(self.x_block(-3.05), self.x_block(-2.35))
        w3 = VGroup(
            Circle(radius=0.30, color=ORANGE, fill_opacity=0.22, stroke_width=2.5),
            txt("3", size=24, color=ORANGE),
        ).move_to([-1.55, 1.32, 0])

        right_box = RoundedRectangle(
            corner_radius=0.08, width=1.0, height=0.62,
            stroke_color=GREEN, stroke_width=2.5,
            fill_color=GREEN, fill_opacity=0.18,
        )
        right_lab = txt("11", size=30, color=GREEN)
        right_group = VGroup(right_box, right_lab).move_to([2.4, 1.32, 0])

        self.play(Create(fulcrum), run_time=0.6)
        self.play(Create(beam), FadeIn(pivot), run_time=0.7)
        self.play(FadeIn(left_blocks, shift=UP * 0.12), run_time=0.7)
        self.play(FadeIn(w3, shift=UP * 0.12), run_time=0.4)
        self.play(FadeIn(right_group, shift=UP * 0.12), run_time=0.5)

        lab_l = txt("左边", size=24, color=DIM).move_to([-2.35, 2.35, 0])
        lab_r = txt("右边", size=24, color=DIM).move_to([2.4, 2.35, 0])
        self.play(FadeIn(lab_l), FadeIn(lab_r), run_time=0.3)

        eq = txt("2x + 3 = 11", size=56, color=GOLD).move_to([0, -0.75, 0])
        self.play(FadeIn(eq, shift=UP * 0.1), run_time=0.7)
        self.finish_section()

        # ================= 1. 2x 表示什么 =================
        self.section(1, "2x：两个一样的 x")

        tag = txt("2x = x + x", size=34, color=BLUE).move_to([0, -1.85, 0])
        self.play(FadeIn(tag), run_time=0.5)
        self.play(
            Indicate(left_blocks[0], color=WHITE, scale_factor=1.08),
            Indicate(left_blocks[1], color=WHITE, scale_factor=1.08),
            run_time=0.9,
        )
        self.finish_section()

        # ================= 2. 两边同时拿走 3 =================
        self.section(2, "两边同时减 3，天平仍然平衡")
        self.play(FadeOut(tag), run_time=0.3)

        chip_l = txt("− 3", size=30, color=RED).move_to([-1.55, 2.15, 0])
        chip_r = txt("− 3", size=30, color=RED).move_to([2.4, 2.15, 0])
        self.play(
            FadeOut(lab_l), FadeOut(lab_r),
            FadeIn(chip_l, shift=DOWN * 0.1), FadeIn(chip_r, shift=DOWN * 0.1),
            run_time=0.5,
        )

        self.play(FadeOut(w3, shift=UP * 0.4), FadeOut(chip_l, shift=UP * 0.4), run_time=0.7)

        new_right = txt("8", size=30, color=GREEN).move_to(right_lab)
        self.play(Transform(right_lab, new_right), FadeOut(chip_r, shift=UP * 0.4), run_time=0.7)
        self.finish_section()

        # ================= 3. 方程两边同时减 3 =================
        self.section(3, "方程里也一样：两边同时减 3")

        eq2 = txt("2x = 8", size=56, color=GOLD).move_to([0, -0.75, 0])
        self.play(Transform(eq, eq2), run_time=0.8)

        step = txt("2x + 3 − 3 = 11 − 3", size=30, color=DIM).move_to([0, -1.85, 0])
        self.play(FadeIn(step), run_time=0.5)
        self.finish_section()

        # ================= 4. 两边同时除以 2 =================
        self.section(4, "两边同时除以 2，得到 x = 4")
        self.play(FadeOut(step), run_time=0.3)

        # 两个方块上的 x，变成 4
        self.play(
            *[
                Transform(blk[1], txt("4", size=32, color=GOLD).move_to(blk[1]))
                for blk in left_blocks
            ],
            run_time=0.7,
        )

        eq3 = txt("x = 4", size=60, color=GOLD).move_to([0, -0.75, 0])
        self.play(Transform(eq, eq3), run_time=0.8)

        divide = txt("8 ÷ 2 = 4", size=30, color=DIM).move_to([0, -1.85, 0])
        self.play(FadeIn(divide), run_time=0.5)
        self.finish_section()

        # ================= 5. 检验 =================
        self.section(5, "检验：代回去看看")
        self.play(FadeOut(divide), run_time=0.3)

        check = txt("2 × 4 + 3 = 11", size=40, color=CHALK).move_to([0, -1.9, 0])
        tick = txt("成立", size=34, color=GREEN).next_to(check, RIGHT, buff=0.45)
        self.play(FadeIn(check, shift=UP * 0.1), run_time=0.6)
        self.play(FadeIn(tick, scale=0.8), run_time=0.4)
        self.finish_section()

        # ================= 6. 收束 =================
        self.section(6, "解方程 = 保持天平平衡")

        self.play(
            FadeOut(check), FadeOut(tick), FadeOut(divide),
            FadeOut(eq), FadeOut(lab_l), FadeOut(lab_r),
            FadeOut(left_blocks), FadeOut(right_group),
            FadeOut(beam), FadeOut(fulcrum), FadeOut(pivot),
            run_time=0.7,
        )

        big = txt("两边同时做相同的事", size=50, color=GOLD).move_to([0, 0.75, 0])
        explain = txt("等式永远成立", size=34, color=CHALK).next_to(big, DOWN, buff=0.4)
        steps = txt("加、减、乘、除 —— 只要两边一样", size=28, color=GREEN).next_to(explain, DOWN, buff=0.35)

        self.play(FadeIn(big, shift=DOWN * 0.1), run_time=0.8)
        self.play(FadeIn(explain, shift=UP * 0.1), run_time=0.5)
        self.play(FadeIn(steps, shift=UP * 0.1), run_time=0.5)
        self.finish_section()

        self.play(FadeOut(big), FadeOut(explain), FadeOut(steps), run_time=0.8)