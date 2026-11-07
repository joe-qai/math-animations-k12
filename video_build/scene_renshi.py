# -*- coding: utf-8 -*-
"""认识图形：长方形、正方形、三角形、圆。一年级上册「认识图形」。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


def poly(points, color=CHALK, width=4.0):
    return Polygon(*[[x, y, 0] for x, y in points], color=color,
                   stroke_width=width, fill_opacity=0.08)


class RenshiScene(NarratedScene):
    lesson = "renshi-tuxing"

    # ---------------- 0. 身边的图形 ----------------
    def scene_life(self):
        self.section(0, "身边的四种图形")

        clock = Circle(radius=0.8, color=GOLD, stroke_width=4,
                       fill_color=GOLD, fill_opacity=0.08).move_to([-4.5, 0.75, 0])
        hand1 = Line([-4.5, 0.75, 0], [-4.5, 1.35, 0], color=GOLD, stroke_width=4)
        hand2 = Line([-4.5, 0.75, 0], [-4.0, 0.55, 0], color=GOLD, stroke_width=4)

        door = Rectangle(width=1.15, height=1.95, color=BLUE, stroke_width=4,
                         fill_color=BLUE, fill_opacity=0.1).move_to([-1.5, 0.63, 0])
        knob = Dot([-1.1, 0.55, 0], radius=0.06, color=BLUE)

        scarf = poly([(1.55, 0.02), (0.7, 1.62), (2.4, 1.62)], color=RED, width=4)

        window = Square(side_length=1.55, color=GREEN, stroke_width=4,
                        fill_color=GREEN, fill_opacity=0.1).move_to([4.5, 0.7, 0])
        cross1 = Line([3.72, 0.7, 0], [5.28, 0.7, 0], color=GREEN, stroke_width=2)
        cross2 = Line([4.5, -0.08, 0], [4.5, 1.48, 0], color=GREEN, stroke_width=2)

        labels = VGroup(
            txt("钟面 · 圆", size=26, color=GOLD).move_to([-4.5, -0.65, 0]),
            txt("门 · 长方形", size=26, color=BLUE).move_to([-1.5, -0.65, 0]),
            txt("红领巾 · 三角形", size=26, color=RED).move_to([1.55, 0.55, 0]),
            txt("窗 · 正方形", size=26, color=GREEN).move_to([4.5, -0.65, 0]),
        )
        labels[2].move_to([1.55, -0.5, 0])

        self.play(FadeIn(clock), Create(hand1), Create(hand2), run_time=0.8)
        self.play(FadeIn(door), FadeIn(knob), run_time=0.6)
        self.play(FadeIn(scarf), run_time=0.6)
        self.play(FadeIn(window), Create(cross1), Create(cross2), run_time=0.7)
        self.play(LaggedStart(*[FadeIn(l, shift=UP * 0.08) for l in labels], lag_ratio=0.12),
                  run_time=0.9)
        self.finish_section()

    # ---------------- 1. 长方形 ----------------
    def scene_rect(self):
        self.section(1, "长方形：4 条边，4 个角")
        p = [(-4.7, -1.05), (0.7, -1.05), (0.7, 1.85), (-4.7, 1.85)]
        shape = poly(p, color=CHALK, width=4)
        self.play(Create(shape), run_time=0.9)

        sides = [
            Line([-4.7, -1.05, 0], [0.7, -1.05, 0], color=GOLD, stroke_width=5),
            Line([0.7, -1.05, 0], [0.7, 1.85, 0], color=BLUE, stroke_width=5),
            Line([0.7, 1.85, 0], [-4.7, 1.85, 0], color=GOLD, stroke_width=5),
            Line([-4.7, 1.85, 0], [-4.7, -1.05, 0], color=BLUE, stroke_width=5),
        ]
        counter = txt("边：0", size=30, color=GOLD).move_to([3.6, 1.45, 0])
        self.play(FadeIn(counter), run_time=0.3)
        for i, s in enumerate(sides):
            self.play(Create(s), run_time=0.35)
            new = txt(f"边：{i + 1}", size=30, color=GOLD).move_to(counter)
            self.play(Transform(counter, new), run_time=0.12)

        corners = VGroup(*[Dot([x, y, 0], radius=0.1, color=CHALK) for x, y in p])
        self.play(LaggedStart(*[GrowFromCenter(c) for c in corners], lag_ratio=0.15),
                  run_time=0.7)
        ccount = txt("角：4", size=30, color=CHALK).move_to([3.6, 0.75, 0])
        self.play(FadeIn(ccount), run_time=0.4)

        note1 = txt("上下两条边一样长", size=27, color=GOLD).move_to([3.55, -0.35, 0])
        note2 = txt("左右两条边一样长", size=27, color=BLUE).move_to([3.55, -1.0, 0])
        self.play(LaggedStart(FadeIn(note1), FadeIn(note2), lag_ratio=0.3), run_time=0.8)
        self.finish_section()

    # ---------------- 2. 正方形 ----------------
    def scene_square(self):
        self.section(2, "正方形：4 条边一样长")
        s = Square(side_length=2.9, color=CHALK, stroke_width=4,
                   fill_opacity=0.08).move_to([-2.0, 0.4, 0])
        self.play(Create(s), run_time=0.9)

        side_lab = txt("4 条边一样长", size=30, color=GOLD).move_to([3.5, 0.9, 0])
        corner_lab = txt("4 个角", size=30, color=CHALK).move_to([3.5, 0.1, 0])
        same = txt("正方形是特殊的长方形", size=26, color=GREEN).move_to([3.5, -0.9, 0])
        self.play(FadeIn(side_lab), run_time=0.5)
        self.play(FadeIn(corner_lab), run_time=0.4)
        self.play(FadeIn(same, shift=UP * 0.08), run_time=0.5)
        self.finish_section()

    # ---------------- 3. 三角形 ----------------
    def scene_triangle(self):
        self.section(3, "三角形：3 条边，3 个角")
        p = [(-4.4, -1.15), (0.3, -1.15), (-2.05, 1.75)]
        t = poly(p, color=CHALK, width=4)
        self.play(Create(t), run_time=0.9)

        for i in range(3):
            a, b = p[i], p[(i + 1) % 3]
            self.play(Create(Line([a[0], a[1], 0], [b[0], b[1], 0], color=GOLD, stroke_width=5)),
                      run_time=0.3)

        corners = VGroup(*[Dot([x, y, 0], radius=0.1, color=CHALK) for x, y in p])
        self.play(LaggedStart(*[GrowFromCenter(c) for c in corners], lag_ratio=0.15),
                  run_time=0.6)

        n1 = txt("3 条边", size=32, color=GOLD).move_to([3.6, 1.1, 0])
        n2 = txt("3 个角", size=32, color=CHALK).move_to([3.6, 0.35, 0])
        n3 = txt("最稳的形状", size=26, color=GREEN).move_to([3.6, -0.75, 0])
        self.play(FadeIn(n1), run_time=0.4)
        self.play(FadeIn(n2), run_time=0.4)
        self.play(FadeIn(n3, shift=UP * 0.08), run_time=0.5)
        self.finish_section()

    # ---------------- 4. 圆 ----------------
    def scene_circle(self):
        self.section(4, "圆：没有角，边是弯的")
        c = Circle(radius=1.9, color=GOLD, stroke_width=5,
                   fill_color=GOLD, fill_opacity=0.06).move_to([-2.0, 0.35, 0])
        self.play(Create(c), run_time=1.2)

        center_dot = Dot([-2.0, 0.35, 0], radius=0.09, color=CHALK)
        radius = Line([-2.0, 0.35, 0], [-2.0, 2.25, 0], color=BLUE, stroke_width=3)
        self.play(FadeIn(center_dot), Create(radius), run_time=0.5)
        self.play(Rotate(radius, angle=TAU, about_point=[-2.0, 0.35, 0]), run_time=1.4)

        walker = Dot([-0.1, 0.35, 0], radius=0.1, color=RED)
        self.play(MoveAlongPath(walker, c.copy()), run_time=1.2)

        n1 = txt("0 个角", size=34, color=GOLD).move_to([3.6, 1.0, 0])
        n2 = txt("边是弯的", size=28, color=CHALK).move_to([3.6, 0.3, 0])
        n3 = txt("圆心到边上处处一样远", size=24, color=BLUE).move_to([3.6, -0.6, 0])
        self.play(FadeIn(n1), run_time=0.4)
        self.play(FadeIn(n2), run_time=0.4)
        self.play(FadeIn(n3), run_time=0.5)
        self.finish_section()

    # ---------------- 5. 放在一起比一比 ----------------
    def scene_compare(self):
        self.section(5, "比一比：数边、数角")

        head = VGroup(
            txt("图形", size=26, color=DIM),
            txt("边", size=26, color=DIM),
            txt("角", size=26, color=DIM),
        )
        head[0].move_to([-4.2, 1.75, 0])
        head[1].move_to([0.6, 1.75, 0])
        head[2].move_to([3.9, 1.75, 0])
        self.play(FadeIn(head), run_time=0.5)

        rows = [
            ("长方形", "4 条", "4 个", GOLD),
            ("正方形", "4 条", "4 个", GREEN),
            ("三角形", "3 条", "3 个", RED),
            ("圆", "0 条", "0 个", BLUE),
        ]
        y = 0.95
        for name, sides, corners, color in rows:
            row = VGroup(
                txt(name, size=30, color=color),
                txt(sides, size=30, color=CHALK),
                txt(corners, size=30, color=CHALK),
            )
            row[0].move_to([-4.2, y, 0])
            row[1].move_to([0.6, y, 0])
            row[2].move_to([3.9, y, 0])
            self.play(FadeIn(row, shift=RIGHT * 0.06), run_time=0.45)
            y -= 0.82

        tip = txt("数一数：边是直的，还是弯的？", size=27, color=GREEN).move_to([0, -2.6, 0])
        self.play(FadeIn(tip, shift=UP * 0.08), run_time=0.6)
        self.finish_section()

    # ---------------- 6. 收束 ----------------
    def scene_summary(self):
        self.section(6, "先数边，再数角")

        big = txt("先数边，再数角", size=58, color=GOLD).move_to([0, 1.5, 0])
        self.play(Write(big), run_time=0.9)

        left = txt("边是直的 → 多边形", size=32, color=CHALK).move_to([-3.1, 0.35, 0])
        right = txt("边是弯的 → 圆", size=32, color=CHALK).move_to([3.1, 0.35, 0])
        self.play(FadeIn(left, shift=UP * 0.08), FadeIn(right, shift=UP * 0.08), run_time=0.7)

        final = txt("长方形、正方形、三角形，都是多边形", size=28, color=GREEN).move_to([0, -0.9, 0])
        self.play(FadeIn(final, shift=UP * 0.08), run_time=0.6)
        self.finish_section()

    def clear_stage(self, run_time: float = 0.5):
        """清空画面，但保留顶部进度条。"""
        keep = {id(self._track), id(self._fill)}
        junk = [m for m in self.mobjects if id(m) not in keep]
        if junk:
            self.play(*[FadeOut(m) for m in junk], run_time=run_time)
        self.cur_title = None
        self.cur_sub = None

    def construct(self):
        self.scene_life()
        self.clear_stage()
        self.scene_rect()
        self.clear_stage()
        self.scene_square()
        self.clear_stage()
        self.scene_triangle()
        self.clear_stage()
        self.scene_circle()
        self.clear_stage()
        self.scene_compare()
        self.clear_stage()
        self.scene_summary()
        self.clear_stage(0.8)