"""
勾股定理动画演示 - a^2 + b^2 = c^2
使用经典的几何证明：通过面积重组展示直角三角形三边关系
不使用 LaTeX，全部用 Text 替代
"""

from manim import *
import numpy as np


class PythagoreanTheorem(Scene):
    def construct(self):
        a, b, c = 3, 4, 5

        # 三角形顶点
        right_angle_pos = LEFT * 2.5 + DOWN * 1.5
        A = right_angle_pos + np.array([0, a, 0])
        B = right_angle_pos + np.array([b, 0, 0])
        C = right_angle_pos

        # ============ 第一阶段：标题和三角形 ============
        title = Text("勾股定理", font_size=48, color=WHITE).to_edge(UP)
        self.play(Write(title), run_time=1.5)
        self.wait(0.5)
        self.play(FadeOut(title), run_time=0.5)

        # 绘制三角形
        triangle = Polygon(A, B, C, color=GOLD, fill_opacity=0.1, stroke_width=3)
        self.play(Create(triangle), run_time=1.5)

        # 直角标记
        right_angle_mark = RightAngle(Line(C, A), Line(C, B), length=0.2, color=WHITE)
        self.play(Create(right_angle_mark), run_time=0.5)

        # 标注边长（用 Text）
        label_a = Text("a", color=RED, font_size=36).next_to(C - LEFT * 0.3, LEFT * 1.5)
        label_b = Text("b", color=GREEN, font_size=36).next_to(B + RIGHT * 0.3, DOWN * 2)
        label_c = Text("c", color=BLUE, font_size=36).next_to((A + B) / 2 + RIGHT * 0.5, UP * 0.5)

        self.play(Write(label_a), Write(label_b), Write(label_c), run_time=1.0)
        self.wait(0.5)

        # ============ 第二阶段：构建三个正方形 ============
        # 在边 a 上构建正方形（向左）
        square_a_pts = [
            C,
            A,
            A + np.array([-a, 0, 0]),
            C + np.array([-a, 0, 0]),
        ]
        square_a = Polygon(*square_a_pts, fill_opacity=0.3, stroke_color=RED, stroke_width=3)

        # 在边 b 上构建正方形（向下）
        square_b_pts = [
            C,
            B,
            B + np.array([0, -b, 0]),
            C + np.array([0, -b, 0]),
        ]
        square_b = Polygon(*square_b_pts, fill_opacity=0.3, stroke_color=GREEN, stroke_width=3)

        # 在斜边 c 上构建正方形
        perp_ab = np.array([a, b, 0]) / c
        square_c_pts = [
            A,
            B,
            B + perp_ab * c,
            A + perp_ab * c,
        ]
        square_c = Polygon(*square_c_pts, fill_opacity=0.3, stroke_color=BLUE, stroke_width=3)

        self.play(
            Create(square_a),
            Create(square_b),
            run_time=1.5
        )

        # 面积标注
        area_a = Text("a^2", color=RED, font_size=36).move_to(
            square_a_pts[0] + np.array([-a / 2, a / 2, 0])
        )
        area_b = Text("b^2", color=GREEN, font_size=36).move_to(
            square_b_pts[0] + np.array([b / 2, -b / 2, 0])
        )
        center_c = sum(square_c_pts) / 4
        area_c = Text("c^2", color=BLUE, font_size=36).move_to(center_c)

        self.play(Write(area_a), Write(area_b), run_time=0.8)
        self.play(Create(square_c), run_time=1.0)
        self.play(Write(area_c), run_time=0.8)

        self.wait(0.5)

        # ============ 第三阶段：显示公式 ============
        equation = Text("a^2 + b^2 = c^2", font_size=52, color=WHITE)
        equation.to_edge(DOWN).shift(UP * 0.5)
        equation_highlight = VGroup(
            Text("a^2", color=RED, font_size=52),
            Text(" + ", color=WHITE, font_size=52),
            Text("b^2", color=GREEN, font_size=52),
            Text(" = ", color=WHITE, font_size=52),
            Text("c^2", color=BLUE, font_size=52),
        )
        equation_highlight.arrange(RIGHT, buff=0.05)
        equation_highlight.move_to(equation.get_center())

        self.play(
            FadeIn(equation_highlight[0]),
            run_time=0.5
        )
        self.play(
            FadeIn(equation_highlight[1]),
            FadeIn(equation_highlight[2]),
            run_time=0.5
        )
        self.play(
            FadeIn(equation_highlight[3]),
            FadeIn(equation_highlight[4]),
            run_time=0.5
        )

        self.wait(1)

        # ============ 第四阶段：欧几里得证明 ============
        self.play(
            FadeOut(equation_highlight),
            run_time=0.5
        )

        # 重新显示三角形和标签
        self.play(
            triangle.animate.set_fill_opacity(0.3),
            run_time=0.3
        )
        self.wait(0.2)

        # 从直角顶点向斜边作高
        t = (b * b) / (c * c)
        D = A + t * (B - A)

        altitude = DashedLine(C, D, color=YELLOW, dash_length=0.15, space_between=0.1)
        self.play(Create(altitude), run_time=1.0)

        label_d = Text("D", color=YELLOW, font_size=24).move_to(D + RIGHT * 0.2 + UP * 0.2)
        self.play(Write(label_d), run_time=0.3)

        # 延伸到斜边正方形
        alt_unit = (D - C) / np.linalg.norm(D - C)
        BA = B - A
        rhs = C - A - perp_ab * c
        det = BA[0] * (-alt_unit[1]) - BA[1] * (-alt_unit[0])
        s = (rhs[0] * (-alt_unit[1]) - rhs[1] * (-alt_unit[0])) / det
        E = A + s * (B - A) + perp_ab * c

        extend_line = DashedLine(
            C + alt_unit * (-1),
            E + alt_unit * 0.5,
            color=YELLOW,
            dash_length=0.1,
            space_between=0.08
        )
        self.play(Create(extend_line), run_time=0.8)

        self.wait(0.5)

        # 高亮两个矩形区域
        rect_area_a = Polygon(
            A, D, E, A + perp_ab * c,
            fill_opacity=0.4, stroke_color=RED, stroke_width=2
        )
        rect_area_b = Polygon(
            D, B, B + perp_ab * c, E,
            fill_opacity=0.4, stroke_color=GREEN, stroke_width=2
        )

        self.play(
            Create(rect_area_a),
            Create(rect_area_b),
            run_time=1.5
        )

        self.wait(0.5)

        # ============ 第五阶段：动画重组 ============
        # 淡化中间元素，强调面积相等
        self.play(
            FadeOut(triangle),
            FadeOut(right_angle_mark),
            FadeOut(label_a),
            FadeOut(label_b),
            FadeOut(label_c),
            FadeOut(label_d),
            FadeOut(altitude),
            FadeOut(extend_line),
            run_time=0.8
        )

        # 高亮各区域
        self.play(
            square_a.animate.set_fill_opacity(0.6).set_color(RED),
            rect_area_a.animate.set_fill_opacity(0.6),
            run_time=0.8
        )
        self.wait(0.3)

        self.play(
            square_b.animate.set_fill_opacity(0.6).set_color(GREEN),
            rect_area_b.animate.set_fill_opacity(0.6),
            run_time=0.8
        )
        self.wait(0.5)

        # 淡出证明元素
        self.play(
            FadeOut(square_a),
            FadeOut(square_b),
            FadeOut(square_c),
            FadeOut(area_a),
            FadeOut(area_b),
            FadeOut(area_c),
            FadeOut(rect_area_a),
            FadeOut(rect_area_b),
            run_time=0.8
        )

        # ============ 最终结论 ============
        final_eq = Text("a^2 + b^2 = c^2", font_size=72, color=WHITE)
        final_eq_red = Text("a^2", color=RED, font_size=72)
        final_eq_green = Text("b^2", color=GREEN, font_size=72)
        final_eq_blue = Text("c^2", color=BLUE, font_size=72)
        final_eq_plus = Text(" + ", color=WHITE, font_size=72)
        final_eq_equal = Text(" = ", color=WHITE, font_size=72)

        final_group = VGroup(
            final_eq_red, final_eq_plus, final_eq_green,
            final_eq_equal, final_eq_blue
        )
        final_group.arrange(RIGHT, buff=0.1)
        final_group.to_center()

        self.play(
            FadeIn(final_eq_red),
            run_time=0.5
        )
        self.play(
            FadeIn(final_eq_plus),
            FadeIn(final_eq_green),
            run_time=0.5
        )
        self.play(
            FadeIn(final_eq_equal),
            FadeIn(final_eq_blue),
            run_time=0.5
        )

        # 添加说明文字
        note = Text("直角三角形：两直角边的平方和等于斜边的平方", font_size=28, color=WHITE)
        note.next_to(final_group, DOWN, buff=0.5)
        self.play(Write(note), run_time=1.0)

        self.wait(2)
        self.play(FadeOut(final_group), FadeOut(note), run_time=1.0)


class SimplePythagorean(Scene):
    def construct(self):
        a, b, c = 3, 4, 5
        C = LEFT * 2 + DOWN * 1
        A = C + UP * a
        B = C + RIGHT * b

        # 标题
        title = Text("勾股定理 Pythagorean Theorem", font_size=40, color=WHITE)
        self.play(Write(title), run_time=1.5)
        self.play(title.animate.to_edge(UP), run_time=0.5)
        self.wait(0.3)
        self.play(FadeOut(title))

        # 三角形
        tri = Polygon(A, B, C, color=GOLD, fill_opacity=0.2, stroke_width=3)
        self.play(Create(tri), run_time=1.2)

        # 三边标注
        la = Text("a=3", color=RED, font_size=24).next_to(Line(C, A), LEFT, buff=0.2)
        lb = Text("b=4", color=GREEN, font_size=24).next_to(Line(C, B), DOWN, buff=0.2)
        lc = Text("c=5", color=BLUE, font_size=24).next_to(Line(A, B), UP + RIGHT, buff=0.2)
        self.play(Write(la), run_time=0.5)
        self.play(Write(lb), run_time=0.5)
        self.play(Write(lc), run_time=0.5)

        # 三个正方形
        sq_a = Polygon(
            C, A, A + np.array([-a, 0, 0]), C + np.array([-a, 0, 0]),
            fill_opacity=0.3, stroke_color=RED, stroke_width=2
        )
        sq_b = Polygon(
            C, B, B + np.array([0, -b, 0]), C + np.array([0, -b, 0]),
            fill_opacity=0.3, stroke_color=GREEN, stroke_width=2
        )
        perp_ab = np.array([a, b, 0]) / c
        sq_c = Polygon(
            A, B, B + perp_ab * c, A + perp_ab * c,
            fill_opacity=0.3, stroke_color=BLUE, stroke_width=2
        )

        self.play(Create(sq_a), Create(sq_b), run_time=1.5)
        self.play(Create(sq_c), run_time=1.0)

        # 面积标注
        ca = sq_a.get_center()
        cb = sq_b.get_center()
        cc = sq_c.get_center()
        ta = Text("a^2=9", color=RED, font_size=30).move_to(ca)
        tb = Text("b^2=16", color=GREEN, font_size=30).move_to(cb)
        tc = Text("c^2=25", color=BLUE, font_size=30).move_to(cc)
        self.play(Write(ta), run_time=0.5)
        self.play(Write(tb), run_time=0.5)
        self.play(Write(tc), run_time=0.5)

        self.wait(1)

        # 最终等式
        eq_red = Text("a^2=9", color=RED, font_size=48)
        eq_green = Text("b^2=16", color=GREEN, font_size=48)
        eq_blue = Text("c^2=25", color=BLUE, font_size=48)
        eq_plus = Text(" + ", color=WHITE, font_size=48)
        eq_equal = Text(" = ", color=WHITE, font_size=48)
        eq = VGroup(eq_red, eq_plus, eq_green, eq_equal, eq_blue)
        eq.arrange(RIGHT, buff=0.15)
        eq.to_edge(DOWN).shift(UP * 0.3)

        self.play(Write(eq), run_time=1.5)
        self.wait(2)
