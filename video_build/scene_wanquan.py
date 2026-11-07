# -*- coding: utf-8 -*-
"""完全平方公式：用面积看懂 (a+b)²。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


class WanquanScene(NarratedScene):
    lesson = "wanquan-pingfang"

    A, B = 2.3, 1.3
    X0, Y0 = -4.3, -1.5          # 大正方形左下角

    def region(self, x0, y0, w, h, color, opacity=0.22) -> Rectangle:
        return Rectangle(
            width=w, height=h, color=color,
            fill_color=color, fill_opacity=opacity, stroke_width=2,
        ).move_to([x0 + w / 2, y0 + h / 2, 0])

    def construct(self):
        a, b = self.A, self.B
        x0, y0 = self.X0, self.Y0
        side = a + b

        # ================= 0. 常见的错误 =================
        self.section(0, "（a + b）² 等于什么？")

        title = txt("(a + b)²", size=72, color=GOLD).move_to([2.9, 1.5, 0])
        right = txt("= a² + b² ？", size=52, color=CHALK).move_to([2.9, 0.55, 0])
        wrong = txt("这样写，少了两块", size=30, color=RED).move_to([2.9, -0.55, 0])
        strike = Line([1.0, 0.55, 0], [4.9, 0.55, 0], color=RED, stroke_width=5)

        self.play(FadeIn(title, shift=DOWN * 0.1), run_time=0.7)
        self.play(FadeIn(right), run_time=0.6)
        self.play(Create(strike), FadeIn(wrong), run_time=0.6)
        self.finish_section()

        # ================= 1. 画一个大正方形 =================
        self.section(1, "画一个边长为 a + b 的大正方形")
        self.play(FadeOut(title), FadeOut(right), FadeOut(strike), FadeOut(wrong), run_time=0.5)

        big = Rectangle(
            width=side, height=side, color=CHALK, stroke_width=3,
            fill_color=WHITE, fill_opacity=0.03,
        ).move_to([x0 + side / 2, y0 + side / 2, 0])
        self.play(Create(big), run_time=1.0)

        lab_bottom = txt("a + b", size=32, color=GOLD).move_to([x0 + side / 2, y0 - 0.3, 0])
        lab_left = txt("a + b", size=32, color=GOLD).rotate(PI / 2).move_to([x0 - 0.35, y0 + side / 2, 0])
        self.play(FadeIn(lab_bottom), FadeIn(lab_left), run_time=0.6)

        area_note = txt("大正方形的面积 = (a + b)²", size=30, color=DIM).move_to([2.9, 1.4, 0])
        self.play(FadeIn(area_note), run_time=0.5)
        self.finish_section()

        # ================= 2. 切出 a² 和 b² =================
        self.section(2, "切出边长 a 和边长 b 的两个正方形")
        self.play(FadeOut(area_note), run_time=0.3)

        sq_a = self.region(x0, y0, a, a, BLUE)
        sq_b = self.region(x0 + a, y0 + a, b, b, GREEN)
        self.play(FadeIn(sq_a), run_time=0.6)
        self.play(FadeIn(sq_b), run_time=0.5)

        lab_a2 = txt("a²", size=40, color=BLUE).move_to(sq_a.get_center())
        lab_b2 = txt("b²", size=36, color=GREEN).move_to(sq_b.get_center())
        self.play(FadeIn(lab_a2, scale=0.85), FadeIn(lab_b2, scale=0.85), run_time=0.6)

        # 边长标注拆成 a、b
        seg_a = txt("a", size=30, color=BLUE).move_to([x0 + a / 2, y0 - 0.3, 0])
        seg_b = txt("b", size=30, color=GREEN).move_to([x0 + a + b / 2, y0 - 0.3, 0])
        seg_a2 = txt("a", size=30, color=BLUE).rotate(PI / 2).move_to([x0 - 0.35, y0 + a / 2, 0])
        seg_b2 = txt("b", size=30, color=GREEN).rotate(PI / 2).move_to([x0 - 0.35, y0 + a + b / 2, 0])
        self.play(
            Transform(lab_bottom, seg_a),
            Transform(lab_left, seg_a2),
            FadeIn(seg_b), FadeIn(seg_b2),
            run_time=0.7,
        )
        self.finish_section()

        # ================= 3. 剩下的两个 ab =================
        self.section(3, "剩下两块，都是 a × b")
        rect1 = self.region(x0 + a, y0, b, a, ORANGE)
        rect2 = self.region(x0, y0 + a, a, b, ORANGE)
        self.play(FadeIn(rect1), run_time=0.5)
        self.play(FadeIn(rect2), run_time=0.5)

        lab_ab1 = txt("ab", size=30, color=ORANGE).move_to(rect1.get_center())
        lab_ab2 = txt("ab", size=30, color=ORANGE).move_to(rect2.get_center())
        self.play(FadeIn(lab_ab1), FadeIn(lab_ab2), run_time=0.5)

        note = txt("两块，一共 2ab", size=30, color=ORANGE).move_to([2.9, 1.4, 0])
        self.play(FadeIn(note), run_time=0.4)
        self.finish_section()

        # ================= 4. 合起来 =================
        self.section(4, "面积相加：a² + 2ab + b²")
        self.play(FadeOut(note), run_time=0.3)

        formula = txt("(a + b)² = a² + 2ab + b²", size=50, color=GOLD).move_to([0, -2.6, 0])
        self.play(FadeIn(formula, shift=UP * 0.1), run_time=0.8)
        self.finish_section()

        # ================= 5. 少算的就是这两块 =================
        self.section(5, "少算的，就是中间这两块")
        self.play(Indicate(rect1, color=WHITE, scale_factor=1.03), run_time=0.7)
        self.play(Indicate(rect2, color=WHITE, scale_factor=1.03), run_time=0.7)
        self.play(Indicate(VGroup(lab_ab1, lab_ab2), color=WHITE, scale_factor=1.2), run_time=0.6)
        self.finish_section()

        # ================= 6. 举个例子 =================
        self.section(6, "举个例子：a = 3，b = 2")

        example = VGroup(
            txt("(3 + 2)² = 5² = 25", size=34, color=CHALK),
            txt("3² + 2 × 3 × 2 + 2² = 9 + 12 + 4 = 25", size=32, color=GREEN),
        ).arrange(DOWN, buff=0.3).move_to([2.9, 0.55, 0])
        self.play(FadeIn(example, shift=RIGHT * 0.1), run_time=0.8)

        self.play(Indicate(formula, color=WHITE, scale_factor=1.04), run_time=0.8)
        self.finish_section()

        self.play(
            FadeOut(example), FadeOut(formula), FadeOut(big), FadeOut(sq_a), FadeOut(sq_b),
            FadeOut(rect1), FadeOut(rect2), FadeOut(lab_a2), FadeOut(lab_b2),
            FadeOut(lab_ab1), FadeOut(lab_ab2), FadeOut(lab_bottom), FadeOut(lab_left),
            FadeOut(seg_b), FadeOut(seg_b2),
            run_time=0.8,
        )