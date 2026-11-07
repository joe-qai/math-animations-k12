# -*- coding: utf-8 -*-
"""三角形的面积：为什么要除以 2。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


class SanjiaoxingScene(NarratedScene):
    lesson = "sanjiaoxing-mianji"

    BL = (-4.6, -1.3, 0)
    BR = (-0.1, -1.3, 0)
    TR = (-0.1, 1.7, 0)
    TL = (-4.6, 1.7, 0)

    def construct(self):
        # ================= 0. 一块三角形的地 =================
        self.section(0, "一块三角形的地，面积是多少？")

        tri = Polygon(self.BL, self.BR, self.TL, color=GOLD,
                      fill_color=GOLD, fill_opacity=0.30, stroke_width=4)
        right_angle = RightAngle(
            Line(self.BL, self.TL), Line(self.BL, self.BR), length=0.28, color=WHITE
        )

        base_lab = txt("底 = 6 米", size=30, color=GREEN).move_to([-2.35, -1.75, 0])
        height_lab = txt("高 = 4 米", size=30, color=RED).rotate(PI / 2).move_to([-5.05, 0.2, 0])

        self.play(Create(tri), run_time=1.0)
        self.play(Create(right_angle), run_time=0.5)
        self.play(FadeIn(base_lab), FadeIn(height_lab), run_time=0.7)

        q = txt("怎么算？", size=38, color=CHALK).move_to([3.2, 0.3, 0])
        self.play(FadeIn(q, shift=LEFT * 0.1), run_time=0.5)
        self.finish_section()

        # ================= 1. 放进长方形 =================
        self.section(1, "先放进一个长方形里")
        self.play(FadeOut(q), run_time=0.3)

        rect = Polygon(self.BL, self.BR, self.TR, self.TL,
                       color=DIM, stroke_width=3)
        self.play(Create(rect), run_time=1.2)

        side = VGroup(
            txt("长方形", size=30, color=DIM),
            txt("长 6 米，宽 4 米", size=30, color=CHALK),
        ).arrange(DOWN, buff=0.25).move_to([3.3, 1.2, 0])
        self.play(FadeIn(side, shift=RIGHT * 0.1), run_time=0.6)
        self.finish_section()

        # ================= 2. 对角线剪开 =================
        self.section(2, "沿对角线剪开，得到两个一样的三角形")
        self.play(FadeOut(side), run_time=0.3)

        diag = Line(self.BR, self.TL, color=ORANGE, stroke_width=4)
        self.play(Create(diag), run_time=0.8)

        tri2 = tri.copy().set_fill(BLUE, 0.30).set_stroke(BLUE, 3)
        tri2.shift(RIGHT * 0.5 + UP * 0.5)
        self.play(FadeIn(tri2), run_time=0.5)

        center = np.array([-2.35, 0.2, 0])
        target = tri.copy().set_fill(BLUE, 0.30).set_stroke(BLUE, 3)
        target.rotate(PI, about_point=center)
        self.play(Transform(tri2, target), run_time=1.8)

        same = VGroup(
            txt("剪开的两块", size=30, color=BLUE),
            txt("能完全重合", size=30, color=BLUE),
        ).arrange(DOWN, buff=0.2).move_to([3.3, 1.1, 0])
        self.play(FadeIn(same, shift=RIGHT * 0.1), run_time=0.6)
        self.finish_section()

        # ================= 3. 长方形面积 =================
        self.section(3, "先算长方形，再取一半")
        self.play(FadeOut(same), run_time=0.3)

        rect_fill = Polygon(self.BL, self.BR, self.TR, self.TL,
                            fill_color=WHITE, fill_opacity=0.06, stroke_width=0)
        rect_fill.set_z_index(-3)
        self.add(rect_fill)

        calc = VGroup(
            txt("长方形面积", size=30, color=DIM),
            txt("6 × 4 = 24", size=44, color=GOLD),
            txt("平方米", size=26, color=DIM),
        ).arrange(DOWN, buff=0.22).move_to([3.3, 1.0, 0])
        self.play(FadeIn(calc, shift=RIGHT * 0.1), run_time=0.8)
        self.finish_section()

        # ================= 4. 一个三角形 = 一半 =================
        self.section(4, "一个三角形，就是它的一半")
        self.play(FadeOut(calc), run_time=0.3)

        half = VGroup(
            txt("24 ÷ 2 = 12", size=50, color=GOLD),
            txt("三角形的面积 = 12 平方米", size=30, color=CHALK),
        ).arrange(DOWN, buff=0.3).move_to([3.2, 0.95, 0])
        self.play(FadeIn(half, shift=RIGHT * 0.1), run_time=0.8)
        self.play(Indicate(tri, color=WHITE, scale_factor=1.03), run_time=0.8)
        self.finish_section()

        # ================= 5. 公式 =================
        self.section(5, "所以：底 × 高 ÷ 2")
        self.play(FadeOut(half), run_time=0.3)

        formula = txt("S = 底 × 高 ÷ 2", size=52, color=GOLD).move_to([0, -2.5, 0])
        self.play(FadeIn(formula, shift=UP * 0.1), run_time=0.7)

        plug = txt("S = 6 × 4 ÷ 2 = 12", size=30, color=CHALK).move_to([3.2, 0.95, 0])
        self.play(FadeIn(plug), run_time=0.5)
        self.finish_section()

        # ================= 6. 为什么除以 2 =================
        self.section(6, "为什么一定要除以 2？")
        self.play(FadeOut(plug), run_time=0.3)

        # 两个三角形交替高亮，强调"拼成长方形"
        self.play(Indicate(tri, color=GOLD, scale_factor=1.04), run_time=0.9)
        self.play(Indicate(tri2, color=BLUE, scale_factor=1.04), run_time=0.9)

        why = VGroup(
            txt("两个一样的三角形", size=30, color=CHALK),
            txt("正好拼成一个长方形", size=30, color=CHALK),
            txt("所以要 ÷ 2", size=38, color=GOLD),
        ).arrange(DOWN, buff=0.28).move_to([3.2, 0.95, 0])
        self.play(FadeIn(why, shift=RIGHT * 0.1), run_time=0.8)
        self.finish_section()

        self.play(FadeOut(why), FadeOut(formula), FadeOut(tri2), FadeOut(tri),
                  FadeOut(rect), FadeOut(diag), FadeOut(base_lab), FadeOut(height_lab),
                  FadeOut(right_angle), FadeOut(rect_fill), run_time=0.8)