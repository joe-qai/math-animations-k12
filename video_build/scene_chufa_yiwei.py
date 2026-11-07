# -*- coding: utf-8 -*-
"""除数是一位数的除法：口算、竖式、有余数、验算、商末尾的 0。三年级上册。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403

STEP = 0.6


def digits(s: str, x_right: float, y: float, size: int = 58,
           color: str = CHALK) -> VGroup:
    g = VGroup()
    for i, ch in enumerate(reversed(s)):
        g.add(txt(ch, size=size, color=color).move_to([x_right - i * STEP, y, 0]))
    return g


def bracket(xb: float, y_top: float, x_right: float, color: str = CHALK) -> VGroup:
    v = Line([xb, y_top + 0.5, 0], [xb, y_top - 0.5, 0], color=color, stroke_width=3)
    h = Line([xb, y_top + 0.5, 0], [x_right + 0.45, y_top + 0.5, 0],
             color=color, stroke_width=3)
    return VGroup(v, h)


class ChufaYiweiScene(NarratedScene):
    lesson = "chufa-yiwei"

    def clear_stage(self, run_time: float = 0.5):
        keep = {id(self._track), id(self._fill)}
        junk = [m for m in self.mobjects if id(m) not in keep]
        if junk:
            self.play(*[FadeOut(m) for m in junk], run_time=run_time)
        self.cur_title = None
        self.cur_sub = None

    # ---------------- 0. 分糖 ----------------
    def scene_story(self):
        self.section(0, "48 块糖，平均分给 4 人")

        dots = VGroup()
        for r in range(6):
            for c in range(8):
                dots.add(Dot([-5.6 + c * 0.42, 1.6 - r * 0.55, 0],
                             radius=0.085, color=GOLD))
        self.play(LaggedStart(*[GrowFromCenter(d) for d in dots], lag_ratio=0.02),
                  run_time=1.6)
        self.play(Indicate(dots, color=GOLD, scale_factor=1.0), run_time=0.5)

        total = txt("48 块", size=28, color=GOLD).move_to([-4.1, -1.95, 0])
        self.play(FadeIn(total), run_time=0.4)

        kids = VGroup()
        for i in range(4):
            box = RoundedRectangle(corner_radius=0.12, width=2.1, height=0.72,
                                   stroke_color=BLUE, stroke_width=2,
                                   fill_color=BLUE, fill_opacity=0.08)
            box.move_to([4.2, 1.55 - i * 1.05, 0])
            kids.add(VGroup(box, txt(f"小朋友 {i + 1}", size=24, color=BLUE).move_to(box)))
        self.play(LaggedStart(*[FadeIn(k, shift=LEFT * 0.1) for k in kids], lag_ratio=0.15),
                  run_time=1.2)

        q = txt("平均分给 4 人", size=30, color=CHALK).move_to([0.2, 1.0, 0])
        expr = txt("48 ÷ 4 = ?", size=46, color=GOLD).move_to([0.2, -0.15, 0])
        self.play(FadeIn(q, shift=UP * 0.06), run_time=0.6)
        self.play(Write(expr), run_time=0.9)
        self.finish_section()

    # ---------------- 1. 口算 ----------------
    def scene_split(self):
        self.section(1, "口算：拆成 40 和 8")

        split = VGroup(
            txt("48", size=52, color=CHALK),
            txt("=", size=52, color=DIM),
            txt("40", size=52, color=GOLD),
            txt("+", size=52, color=DIM),
            txt("8", size=52, color=BLUE),
        ).arrange(RIGHT, buff=0.26).move_to([0, 2.05, 0])
        self.play(Write(split), run_time=1.1)

        l1 = txt("40 ÷ 4 = 10", size=50, color=GOLD).move_to([-1.4, 0.85, 0])
        l2 = txt("8 ÷ 4 = 2", size=50, color=BLUE).move_to([-1.4, -0.15, 0])
        self.play(Write(l1), run_time=0.9)
        self.play(Write(l2), run_time=0.8)

        total = txt("10 + 2 = 12", size=52, color=GREEN).move_to([0, -1.25, 0])
        self.play(Write(total), run_time=1.0)

        ans = txt("48 ÷ 4 = 12（块）", size=44, color=GOLD).move_to([0, -2.35, 0])
        self.play(FadeIn(ans, shift=UP * 0.08), run_time=0.8)
        self.finish_section()

    # ---------------- 2. 竖式 48 ÷ 4 ----------------
    def scene_vertical(self):
        self.section(2, "竖式：从最高位除起")

        xb, x_t, x_u = -0.7, 0.45, 1.05
        y_d, y_q = 1.55, 2.55
        br = bracket(xb, y_d, x_u)
        dividend = digits("48", x_u, y_d, size=44)
        divisor = digits("4", xb - 0.55, y_d, size=44)
        self.play(Create(br), run_time=0.7)
        self.play(Write(dividend), Write(divisor), run_time=0.8)

        # 十位：4 ÷ 4
        n1 = txt("十位 4 ÷ 4 = 1", size=26, color=GOLD).move_to([4.4, 2.55, 0])
        self.play(FadeIn(n1, shift=LEFT * 0.06), run_time=0.5)
        q1 = digits("1", x_t, y_q, size=44, color=GOLD)
        self.play(Write(q1), run_time=0.5)

        # 1 × 4 = 4，相减
        s1 = digits("4", x_t, 0.95, size=44)
        l1 = Line([x_t - 0.3, 0.62, 0], [x_u + 0.32, 0.62, 0],
                  color=CHALK, stroke_width=2.4)
        self.play(Write(s1), run_time=0.5)
        self.play(Create(l1), run_time=0.4)

        # 落下 8
        n2 = txt("落下 8，8 ÷ 4 = 2", size=26, color=BLUE).move_to([4.4, 1.5, 0])
        self.play(FadeIn(n2, shift=LEFT * 0.06), run_time=0.5)
        down = digits("8", x_u, 0.05, size=44)
        arr = Arrow([x_u + 0.58, 0.95, 0], [x_u + 0.58, 0.35, 0], color=BLUE,
                    stroke_width=2.4, buff=0, max_tip_length_to_length_ratio=0.4)
        self.play(GrowArrow(arr), Write(down), run_time=0.8)

        q2 = digits("2", x_u, y_q, size=44, color=GOLD)
        self.play(Write(q2), run_time=0.5)

        s2 = digits("8", x_u, -0.6, size=44)
        l2 = Line([x_t - 0.3, -0.92, 0], [x_u + 0.32, -0.92, 0],
                  color=CHALK, stroke_width=2.4)
        self.play(Write(s2), run_time=0.5)
        self.play(Create(l2), run_time=0.4)
        rem = digits("0", x_u, -1.28, size=44, color=GREEN)
        self.play(Write(rem), run_time=0.4)

        ans = txt("48 ÷ 4 = 12", size=40, color=GREEN).move_to([0, -2.25, 0])
        self.play(FadeIn(ans, shift=UP * 0.08), run_time=0.7)
        self.finish_section()

    # ---------------- 3. 有余数 53 ÷ 4 ----------------
    def scene_remainder(self):
        self.section(3, "有余数：53 ÷ 4")

        xb, x_t, x_u = -0.7, 0.45, 1.05
        y_d, y_q = 1.55, 2.55
        br = bracket(xb, y_d, x_u)
        dividend = digits("53", x_u, y_d, size=44)
        divisor = digits("4", xb - 0.55, y_d, size=44)
        self.play(Create(br), Write(dividend), Write(divisor), run_time=1.0)

        n1 = txt("5 ÷ 4 = 1 余 1", size=26, color=GOLD).move_to([4.4, 2.55, 0])
        q1 = digits("1", x_t, y_q, size=44, color=GOLD)
        self.play(FadeIn(n1, shift=LEFT * 0.06), run_time=0.5)
        self.play(Write(q1), run_time=0.5)

        s1 = digits("4", x_t, 0.95, size=44)
        l1 = Line([x_t - 0.3, 0.62, 0], [x_u + 0.32, 0.62, 0],
                  color=CHALK, stroke_width=2.4)
        self.play(Write(s1), Create(l1), run_time=0.7)

        r1 = digits("1", x_t, 0.05, size=44, color=RED)
        self.play(Write(r1), run_time=0.4)

        n2 = txt("落下 3，13 ÷ 4 = 3 余 1", size=26, color=BLUE).move_to([4.35, 1.5, 0])
        self.play(FadeIn(n2, shift=LEFT * 0.06), run_time=0.5)
        down = digits("3", x_u, 0.05, size=44)
        arr = Arrow([x_u + 0.58, 0.95, 0], [x_u + 0.58, 0.35, 0], color=BLUE,
                    stroke_width=2.4, buff=0, max_tip_length_to_length_ratio=0.4)
        self.play(GrowArrow(arr), Write(down), run_time=0.8)

        q2 = digits("3", x_u, y_q, size=44, color=GOLD)
        self.play(Write(q2), run_time=0.5)

        s2 = digits("12", x_u, -0.6, size=44)
        l2 = Line([x_t - 0.3, -0.92, 0], [x_u + 0.32, -0.92, 0],
                  color=CHALK, stroke_width=2.4)
        self.play(Write(s2), Create(l2), run_time=0.7)

        rem = digits("1", x_u, -1.28, size=44, color=RED)
        self.play(Write(rem), run_time=0.4)

        ans = txt("53 ÷ 4 = 13 …… 1", size=40, color=GREEN).move_to([0, -2.25, 0])
        self.play(FadeIn(ans, shift=UP * 0.08), run_time=0.7)
        self.finish_section()

    # ---------------- 4. 验算 ----------------
    def scene_check(self):
        self.section(4, "验算：商 × 除数 + 余数")

        f = txt("商 × 除数 + 余数 = 被除数", size=44, color=GOLD).move_to([0, 2.05, 0])
        self.play(Write(f), run_time=1.2)

        ex = VGroup(
            txt("13", size=56, color=GOLD),
            txt("×", size=44, color=DIM),
            txt("4", size=56, color=BLUE),
            txt("+", size=44, color=DIM),
            txt("1", size=56, color=RED),
            txt("=", size=44, color=DIM),
            txt("53", size=56, color=GREEN),
        ).arrange(RIGHT, buff=0.3).move_to([0, 0.45, 0])
        self.play(Write(ex), run_time=1.4)

        note = txt("13 × 4 = 52，52 + 1 = 53", size=30, color=CHALK).move_to([0, -0.85, 0])
        self.play(FadeIn(note, shift=UP * 0.06), run_time=0.7)

        tick = txt("✓ 和原数一样，算对了", size=34, color=GREEN).move_to([0, -1.85, 0])
        self.play(FadeIn(tick, shift=UP * 0.08), run_time=0.7)
        self.finish_section()

    # ---------------- 5. 商末尾的 0 ----------------
    def scene_zero(self):
        self.section(5, "不够除就商 0：480 ÷ 4")

        xb, x_h, x_t, x_u = -0.5, -0.05, 0.55, 1.15
        y_d, y_q = 1.0, 2.0
        br = bracket(xb, y_d, x_u)
        dividend = digits("480", x_u, y_d)
        divisor = digits("4", xb - 0.55, y_d)
        self.play(Create(br), Write(dividend), Write(divisor), run_time=1.0)

        q1 = digits("1", x_h, y_q, color=GOLD)
        n1 = txt("4 ÷ 4 = 1", size=24, color=GOLD).move_to([4.6, 2.2, 0])
        self.play(Write(q1), FadeIn(n1), run_time=0.6)

        q2 = digits("2", x_t, y_q, color=GOLD)
        n2 = txt("8 ÷ 4 = 2", size=24, color=GOLD).move_to([4.6, 1.35, 0])
        self.play(Write(q2), FadeIn(n2), run_time=0.6)

        n3 = txt("0 ÷ 4 = 0", size=26, color=RED).move_to([4.6, 0.5, 0])
        self.play(FadeIn(n3), run_time=0.4)
        q3 = digits("0", x_u, y_q, color=RED)
        self.play(FadeIn(q3, scale=0.6), run_time=0.5)
        circ = Circle(radius=0.38, color=RED, stroke_width=3).move_to(q3)
        self.play(Create(circ), run_time=0.5)

        warn = txt("这个 0 一定要写，用来占位", size=28, color=GREEN).move_to([0, -0.35, 0])
        self.play(FadeIn(warn, shift=UP * 0.08), run_time=0.7)

        ans = txt("480 ÷ 4 = 120", size=46, color=GREEN).move_to([0, -1.5, 0])
        self.play(Write(ans), run_time=0.9)
        self.finish_section()

    # ---------------- 6. 收束 ----------------
    def scene_summary(self):
        self.section(6, "除法三句话")

        rows = VGroup(
            label_box("① 从高位除起，商写在对齐位", size=28, color=CHALK),
            label_box("② 每次余数都要比除数小", size=28, color=CHALK),
            label_box("③ 商 × 除数 + 余数 = 被除数", size=28, color=GOLD),
        ).arrange(DOWN, buff=0.4).move_to([0, 0.55, 0])
        for r in rows:
            self.play(FadeIn(r, shift=RIGHT * 0.1), run_time=0.6)

        tip = txt("不够除，就商 0 占位", size=30, color=GREEN).move_to([0, -1.85, 0])
        self.play(FadeIn(tip, shift=UP * 0.08), run_time=0.7)
        self.finish_section()

    def construct(self):
        self.scene_story()
        self.clear_stage()
        self.scene_split()
        self.clear_stage()
        self.scene_vertical()
        self.clear_stage()
        self.scene_remainder()
        self.clear_stage()
        self.scene_check()
        self.clear_stage()
        self.scene_zero()
        self.clear_stage()
        self.scene_summary()
        self.clear_stage(0.8)