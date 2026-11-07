# -*- coding: utf-8 -*-
"""凑十法：9 + 4 怎么算。一年级上册「20 以内进位加法」。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403

EGG = "#f7e6c4"
EGG_EDGE = "#e0c894"


class CoushiScene(NarratedScene):
    lesson = "coushifa"

    # 十格盒：2 行 × 5 列
    COLS, ROWS = 5, 2
    CW, CH = 1.05, 0.95
    PITCH_X, PITCH_Y = 1.12, 1.01
    GX, GY = -1.95, 0.15

    def cell_center(self, i: int, j: int):
        x = self.GX + (i - (self.COLS - 1) / 2) * self.PITCH_X
        y = self.GY + ((self.ROWS - 1) / 2 - j) * self.PITCH_Y
        return [x, y, 0]

    def egg(self, at, scale: float = 1.0) -> Ellipse:
        e = Ellipse(
            width=0.64 * scale, height=0.78 * scale,
            color=EGG_EDGE, stroke_width=1.2,
            fill_color=EGG, fill_opacity=0.92,
        )
        e.move_to(at)
        return e

    def construct(self):
        # ================= 0. 生活问题 =================
        self.section(0, "九个鸡蛋，外面还有四个")

        cells = VGroup()
        for j in range(self.ROWS):
            for i in range(self.COLS):
                cx, cy, _ = self.cell_center(i, j)
                c = self.cell(cx, cy, self.CW, self.CH, DIM,
                              fill_opacity=0.04, stroke_width=1.6)
                cells.add(c)
        self.play(LaggedStart(*[FadeIn(c) for c in cells], lag_ratio=0.04), run_time=1.1)

        inside = VGroup()
        for k in range(9):
            j, i = divmod(k, self.COLS)
            inside.add(self.egg(self.cell_center(i, j)))
        self.play(LaggedStart(*[GrowFromCenter(e) for e in inside], lag_ratio=0.06), run_time=1.3)

        outside = VGroup()
        for k in range(4):
            outside.add(self.egg([1.55 + k * 0.94, self.GY, 0]))
        self.play(LaggedStart(*[FadeIn(e, shift=DOWN * 0.2) for e in outside], lag_ratio=0.15),
                  run_time=1.0)

        box_lab = txt("鸡蛋盒：一格放一个", size=26, color=DIM).move_to([-1.95, 1.55, 0])
        out_lab = txt("外面 4 个", size=26, color=GOLD).move_to([2.95, 1.15, 0])
        question = txt("一共有多少个？", size=40, color=CHALK).move_to([2.95, -1.0, 0])
        self.play(FadeIn(box_lab), FadeIn(out_lab), run_time=0.5)
        self.play(FadeIn(question, shift=UP * 0.1), run_time=0.6)
        self.finish_section()

        # ================= 1. 接着数 =================
        self.section(1, "接着数：10、11、12、13")
        self.play(FadeOut(question), FadeOut(out_lab), run_time=0.35)

        counter = txt("9", size=64, color=GOLD).move_to([2.95, 0.65, 0])
        counter_lab = txt("已经数到", size=24, color=DIM).next_to(counter, UP, buff=0.12)
        self.play(FadeIn(counter), FadeIn(counter_lab), run_time=0.4)

        for k, value in enumerate(["10", "11", "12", "13"]):
            self.play(Indicate(outside[k], color=ORANGE, scale_factor=1.18), run_time=0.55)
            new = txt(value, size=64, color=GOLD).move_to(counter)
            self.play(Transform(counter, new), run_time=0.18)

        slow = txt("一个一个数，有点慢", size=28, color=ORANGE).move_to([2.95, -1.05, 0])
        self.play(FadeIn(slow, shift=UP * 0.1), run_time=0.5)
        self.finish_section()

        # ================= 2. 还空一格 =================
        self.section(2, "十个格子，只差一格")
        self.play(FadeOut(counter), FadeOut(counter_lab), FadeOut(slow), run_time=0.4)

        empty = cells[9]
        ring = SurroundingRectangle(empty, color=GOLD, buff=0.03, stroke_width=4)
        ring.set_fill(GOLD, opacity=0.12)
        self.play(Create(ring), run_time=0.6)
        self.play(Indicate(empty, color=GOLD, scale_factor=1.12), run_time=0.6)

        ten_lab = txt("一格一个，装满正好 10 个", size=24, color=GREEN).move_to([3.15, 1.55, 0])
        gap_lab = txt("现在空了 1 格", size=32, color=GOLD).move_to([2.95, -1.0, 0])
        arrow = Arrow([2.05, -0.55, 0], empty.get_center() + RIGHT * 0.6 + DOWN * 0.15,
                      color=GOLD, stroke_width=3, buff=0.1,
                      max_tip_length_to_length_ratio=0.14)
        self.play(FadeIn(ten_lab), run_time=0.5)
        self.play(FadeIn(gap_lab), GrowArrow(arrow), run_time=0.6)
        self.finish_section()

        # ================= 3. 借一个，装满 =================
        self.section(3, "借 1 个，把盒子装满")
        self.play(FadeOut(gap_lab), FadeOut(arrow), FadeOut(ten_lab), run_time=0.35)

        move_egg = outside[0]
        target = empty.get_center()
        path = ArcBetweenPoints(move_egg.get_center(), target, angle=-PI / 2)
        self.play(MoveAlongPath(move_egg, path), run_time=1.3)
        self.play(Indicate(ring, color=GREEN, scale_factor=1.08), run_time=0.5)

        full = txt("正好 10 个", size=40, color=GREEN).move_to([2.95, 1.35, 0])
        self.play(FadeIn(full, scale=0.9), run_time=0.5)

        left3 = txt("外面还剩 3 个", size=30, color=CHALK).move_to([2.95, -1.0, 0])
        self.play(FadeIn(left3), run_time=0.5)
        self.finish_section()

        # ================= 4. 10 + 3 = 13 =================
        self.section(4, "10 加 3 等于 13")
        self.play(FadeOut(full), FadeOut(left3), FadeOut(ring), run_time=0.4)

        brace_box = Brace(VGroup(*inside, move_egg), DOWN, color=GOLD, buff=0.28)
        lab_box = txt("10 个", size=28, color=GOLD).next_to(brace_box, DOWN, buff=0.16)
        brace_out = Brace(outside[1:], DOWN, color=BLUE, buff=0.28)
        lab_out = txt("3 个", size=28, color=BLUE).next_to(brace_out, DOWN, buff=0.16)
        self.play(GrowFromCenter(brace_box), FadeIn(lab_box), run_time=0.6)
        self.play(GrowFromCenter(brace_out), FadeIn(lab_out), run_time=0.5)

        eq = txt("10 + 3 = 13", size=52, color=GOLD).move_to([2.95, 1.85, 0])
        self.play(Write(eq), run_time=0.9)
        self.finish_section()

        # ================= 5. 拆数：4 = 1 + 3 =================
        self.section(5, "把 4 拆成 1 和 3")
        self.play(
            FadeOut(cells), FadeOut(inside), FadeOut(outside), FadeOut(move_egg),
            FadeOut(brace_box), FadeOut(lab_box), FadeOut(brace_out), FadeOut(lab_out),
            FadeOut(eq), FadeOut(box_lab),
            run_time=0.6,
        )

        top = txt("9 + 4", size=52, color=CHALK).move_to([-3.9, 1.55, 0])
        self.play(FadeIn(top, shift=DOWN * 0.1), run_time=0.5)

        # 4 拆成 1 和 3
        b = txt("4", size=46, color=BLUE).move_to([-1.0, 1.55, 0])
        self.play(FadeIn(b), run_time=0.4)
        l1 = Line(b.get_bottom() + DOWN * 0.1, [-1.8, 0.55, 0], color=DIM, stroke_width=2)
        l2 = Line(b.get_bottom() + DOWN * 0.1, [-0.2, 0.55, 0], color=DIM, stroke_width=2)
        one = txt("1", size=42, color=GOLD).move_to([-1.8, 0.25, 0])
        three = txt("3", size=42, color=BLUE).move_to([-0.2, 0.25, 0])
        self.play(Create(l1), Create(l2), run_time=0.45)
        self.play(FadeIn(one), FadeIn(three), run_time=0.45)

        step1 = txt("9 + 1 = 10", size=44, color=GREEN).move_to([-3.8, -0.95, 0])
        step2 = txt("10 + 3 = 13", size=44, color=GREEN).move_to([1.9, -0.95, 0])
        self.play(Write(step1), run_time=0.7)
        self.play(Write(step2), run_time=0.7)

        chain = txt("9 + 4 = 9 + 1 + 3 = 10 + 3 = 13", size=34, color=GOLD).move_to([0, -2.1, 0])
        self.play(FadeIn(chain, shift=UP * 0.1), run_time=0.6)
        self.finish_section()

        # ================= 6. 收束：凑十口诀 =================
        self.section(6, "见 9 想 1：先凑十")
        self.play(
            FadeOut(top), FadeOut(b), FadeOut(l1), FadeOut(l2),
            FadeOut(one), FadeOut(three), FadeOut(step1), FadeOut(step2), FadeOut(chain),
            run_time=0.55,
        )

        big = txt("9 + 4 = 13", size=78, color=GOLD).move_to([0, 1.35, 0])
        self.play(Write(big), run_time=0.9)

        rules = VGroup(
            txt("见 9 想 1", size=34, color=CHALK),
            txt("见 8 想 2", size=34, color=CHALK),
            txt("见 7 想 3", size=34, color=CHALK),
        ).arrange(RIGHT, buff=0.9).move_to([0, -0.15, 0])
        self.play(LaggedStart(*[FadeIn(r, shift=UP * 0.1) for r in rules], lag_ratio=0.2),
                  run_time=0.9)

        final = txt("先凑成 10，再加剩下的", size=32, color=GREEN).move_to([0, -1.35, 0])
        self.play(FadeIn(final, shift=UP * 0.1), run_time=0.6)
        self.finish_section()

        self.play(FadeOut(big), FadeOut(rules), FadeOut(final), run_time=0.8)