# -*- coding: utf-8 -*-
"""小数的初步认识：小数点、十分之几、小数加减。三年级下册。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


def strips(n: int, w: float, h: float, center, color: str = CHALK) -> VGroup:
    """把长方形平均分成 n 条竖格，可单独上色。"""
    cx, cy = center[0], center[1]
    x0 = cx - n * w / 2
    g = VGroup()
    for i in range(n):
        g.add(Rectangle(width=w, height=h, color=color, stroke_width=1.6,
                        fill_color=color, fill_opacity=0.0)
              .move_to([x0 + (i + 0.5) * w, cy, 0]))
    return g


class XiaoshuChubuScene(NarratedScene):
    lesson = "xiaoshu-chubu"

    def clear_stage(self, run_time: float = 0.5):
        keep = {id(self._track), id(self._fill)}
        junk = [m for m in self.mobjects if id(m) not in keep]
        if junk:
            self.play(*[FadeOut(m) for m in junk], run_time=run_time)
        self.cur_title = None
        self.cur_sub = None

    # ---------------- 0. 生活里的两位小数 ----------------
    def scene_story(self):
        self.section(0, "标价 0.5 元，身高 1.3 米")

        # 左：铅笔 + 价签
        body = Rectangle(width=2.5, height=0.34, color=GOLD, stroke_width=2,
                         fill_color=GOLD, fill_opacity=0.35)
        tip = Polygon([-1.25, 0.17, 0], [-1.25, -0.17, 0], [-1.7, 0, 0],
                      color=GOLD, stroke_width=2, fill_color=CHALK, fill_opacity=0.6)
        pencil = VGroup(body, tip).move_to([-3.6, 1.35, 0])
        self.play(FadeIn(pencil, shift=DOWN * 0.08), run_time=0.9)

        tag = RoundedRectangle(corner_radius=0.12, width=2.9, height=1.05,
                               stroke_color=GOLD, stroke_width=2.2,
                               fill_color=GOLD, fill_opacity=0.1).move_to([-3.6, -0.75, 0])
        price = txt("铅笔  0.5 元", size=30, color=GOLD).move_to([-3.6, -0.75, 0])
        self.play(FadeIn(tag, shift=UP * 0.08), run_time=0.7)
        self.play(Write(price), run_time=0.8)

        # 右：身高尺
        axis = Line([1.6, -1.5, 0], [1.6, 2.0, 0], color=CHALK, stroke_width=3)
        ticks = VGroup()
        for i in range(5):
            y = -1.5 + i * 0.875
            ticks.add(Line([1.6, y, 0], [1.85, y, 0], color=CHALK, stroke_width=2))
            ticks.add(txt(f"{round(i * 0.5, 1)}", size=18, color=DIM).move_to([2.15, y, 0]))
        self.play(Create(axis), run_time=0.7)
        self.play(FadeIn(ticks), run_time=0.7)

        mark_y = -1.5 + 2.6 * 0.875
        dash = DashedLine([1.6, mark_y, 0], [4.6, mark_y, 0], color=BLUE, stroke_width=2.4)
        hl = txt("身高 1.3 米", size=30, color=BLUE).move_to([4.4, mark_y + 0.45, 0])
        self.play(Create(dash), run_time=0.7)
        self.play(FadeIn(hl, shift=UP * 0.06), run_time=0.7)
        self.finish_section()

    # ---------------- 1. 小数点 ----------------
    def scene_point(self):
        self.section(1, "小数点：分开整数和小数")

        big = txt("0.5", size=130, color=GOLD).move_to([-1.4, 0.5, 0])
        self.play(Write(big), run_time=1.2)

        dot = Dot(big[1].get_center(), radius=0.11, color=RED)
        circ = Circle(radius=0.42, color=RED, stroke_width=3).move_to(big[1].get_center())
        self.play(FadeIn(dot), Create(circ), run_time=0.7)

        n1 = txt("整数部分", size=26, color=BLUE).move_to([-3.3, 1.75, 0])
        n2 = txt("小数点", size=26, color=RED).move_to([-1.5, -1.15, 0])
        n3 = txt("小数部分", size=26, color=GREEN).move_to([1.0, 1.75, 0])
        arr1 = Arrow([-3.3, 1.45, 0], [-2.75, 0.95, 0], color=BLUE, buff=0,
                     max_tip_length_to_length_ratio=0.2)
        arr3 = Arrow([1.0, 1.45, 0], [0.15, 0.95, 0], color=GREEN, buff=0,
                     max_tip_length_to_length_ratio=0.2)
        self.play(FadeIn(n1), GrowArrow(arr1), run_time=0.6)
        self.play(FadeIn(n2), run_time=0.5)
        self.play(FadeIn(n3), GrowArrow(arr3), run_time=0.6)

        r = txt("读作：零点五", size=38, color=CHALK).move_to([2.9, -1.6, 0])
        self.play(FadeIn(r, shift=UP * 0.08), run_time=0.9)
        self.finish_section()

    # ---------------- 2. 十分之几 ----------------
    def scene_fraction(self):
        self.section(2, "十分之几，就是零点几")

        rows = [
            ("1 角 = 1/10 元", "0.1 元", BLUE),
            ("5 角 = 5/10 元", "0.5 元", GOLD),
            ("10 角", "1 元", GREEN),
        ]
        ys = [1.55, 0.55, -0.45]
        for (left, right, color), y in zip(rows, ys):
            row = VGroup(
                txt(left, size=30, color=CHALK),
                txt("=", size=30, color=DIM),
                txt(right, size=34, color=color),
            ).arrange(RIGHT, buff=0.45).move_to([0, y, 0])
            self.play(FadeIn(row, shift=UP * 0.06), run_time=0.8)

        note = txt("1 元 = 10 角，把 1 元平均分成 10 份", size=26, color=DIM)
        note.move_to([0, -1.55, 0])
        self.play(FadeIn(note, shift=UP * 0.06), run_time=0.7)

        tip = txt("分母是 10，就是一位小数", size=30, color=GOLD)
        tip.move_to([0, -2.4, 0])
        self.play(FadeIn(tip, shift=UP * 0.08), run_time=0.8)
        self.finish_section()

    # ---------------- 3. 正方形成 10 份 ----------------
    def scene_area(self):
        self.section(3, "涂 3 份，就是 0.3")

        center = [-3.4, 0.6, 0]
        s = strips(10, 0.26, 2.6, center, color=CHALK)
        self.play(LaggedStart(*[Create(c) for c in s], lag_ratio=0.05), run_time=1.3)

        lab = txt("平均分成 10 份", size=26, color=DIM).move_to([-3.4, -1.1, 0])
        self.play(FadeIn(lab), run_time=0.5)

        for i in range(3):
            self.play(s[i].animate.set_fill(GOLD, opacity=0.4), run_time=0.4)

        f = VGroup(
            txt("3/10", size=44, color=GOLD),
            txt("=", size=40, color=DIM),
            txt("0.3", size=44, color=GOLD),
        ).arrange(RIGHT, buff=0.3).move_to([2.9, 0.9, 0])
        self.play(FadeIn(f, shift=LEFT * 0.08), run_time=0.9)

        f2 = VGroup(
            txt("10/10", size=40, color=GREEN),
            txt("=", size=36, color=DIM),
            txt("1", size=40, color=GREEN),
        ).arrange(RIGHT, buff=0.3).move_to([2.9, -0.35, 0])
        self.play(FadeIn(f2, shift=LEFT * 0.08), run_time=0.8)

        tip = txt("涂满 10 份就是一", size=26, color=DIM).move_to([2.9, -1.35, 0])
        self.play(FadeIn(tip, shift=UP * 0.06), run_time=0.7)
        self.finish_section()

    # ---------------- 4. 小数加法 ----------------
    def scene_add(self):
        self.section(4, "加法：小数点对齐")

        x_r = 1.9
        a = txt("0.5", size=64, color=CHALK).move_to([x_r, 1.5, 0], aligned_edge=RIGHT)
        b = txt("0.3", size=64, color=BLUE).move_to([x_r, 0.75, 0], aligned_edge=RIGHT)
        plus = txt("+", size=56, color=BLUE).move_to([0.2, 0.75, 0])
        line = Line([x_r - 1.55, 0.35, 0], [x_r + 0.3, 0.35, 0], color=CHALK, stroke_width=3)
        self.play(Write(a), run_time=0.7)
        self.play(Write(b), Write(plus), run_time=0.7)
        self.play(Create(line), run_time=0.5)

        same = txt("小数点对齐", size=28, color=GOLD).move_to([-3.6, 1.15, 0])
        self.play(FadeIn(same, shift=UP * 0.06), run_time=0.7)

        calc = txt("5 + 3 = 8", size=38, color=GREEN).move_to([-3.6, 0.15, 0])
        self.play(Write(calc), run_time=0.8)

        res = txt("0.8", size=64, color=GREEN).move_to([x_r, -0.2, 0], aligned_edge=RIGHT)
        self.play(Write(res), run_time=0.8)

        unit = txt("0.5 元 + 0.3 元 = 0.8 元", size=36, color=GOLD).move_to([0, -1.65, 0])
        self.play(FadeIn(unit, shift=UP * 0.08), run_time=0.9)

        tip = txt("对齐小数点，就是相同单位相加", size=28, color=DIM).move_to([0, -2.55, 0])
        self.play(FadeIn(tip, shift=UP * 0.06), run_time=0.7)
        self.finish_section()

    # ---------------- 5. 小数减法 ----------------
    def scene_sub(self):
        self.section(5, "减法：不够减就借一")

        x_r = 1.9
        a = txt("1.2", size=64, color=CHALK).move_to([x_r, 1.5, 0], aligned_edge=RIGHT)
        b = txt("0.8", size=64, color=BLUE).move_to([x_r, 0.75, 0], aligned_edge=RIGHT)
        minus = txt("−", size=56, color=BLUE).move_to([0.2, 0.75, 0])
        line = Line([x_r - 1.55, 0.35, 0], [x_r + 0.3, 0.35, 0], color=CHALK, stroke_width=3)
        self.play(Write(a), run_time=0.7)
        self.play(Write(b), Write(minus), run_time=0.7)
        self.play(Create(line), run_time=0.5)

        same = txt("小数点还是对齐", size=28, color=GOLD).move_to([-3.6, 1.15, 0])
        self.play(FadeIn(same, shift=UP * 0.06), run_time=0.6)

        s1 = txt("2 减 8 不够减", size=30, color=RED).move_to([-3.6, 0.25, 0])
        s2 = txt("向整数部分借 1 当 10", size=30, color=RED).move_to([-3.6, -0.6, 0])
        self.play(FadeIn(s1, shift=UP * 0.06), run_time=0.6)
        self.play(FadeIn(s2, shift=UP * 0.06), run_time=0.6)

        calc = txt("12 − 8 = 4", size=38, color=GREEN).move_to([-3.6, -1.6, 0])
        self.play(Write(calc), run_time=0.8)

        res = txt("0.4", size=64, color=GREEN).move_to([x_r, -0.2, 0], aligned_edge=RIGHT)
        self.play(Write(res), run_time=0.8)

        unit = txt("1.2 元 − 0.8 元 = 0.4 元", size=36, color=GOLD).move_to([0, -2.5, 0])
        self.play(FadeIn(unit, shift=UP * 0.08), run_time=0.9)
        self.finish_section()

    # ---------------- 6. 收束 ----------------
    def scene_summary(self):
        self.section(6, "小数三句话")

        rows = VGroup(
            label_box("① 小数点分开整数和小数", size=28, color=CHALK),
            label_box("② 十分之几就是零点几", size=28, color=GOLD),
            label_box("③ 加减先对齐小数点", size=28, color=CHALK),
        ).arrange(DOWN, buff=0.45).move_to([0, 0.5, 0])
        for r in rows:
            self.play(FadeIn(r, shift=RIGHT * 0.1), run_time=0.6)

        tip = txt("对齐了小数点，答案就不会错位", size=28, color=GREEN).move_to([0, -1.95, 0])
        self.play(FadeIn(tip, shift=UP * 0.08), run_time=0.8)
        self.finish_section()

    def construct(self):
        self.scene_story()
        self.clear_stage()
        self.scene_point()
        self.clear_stage()
        self.scene_fraction()
        self.clear_stage()
        self.scene_area()
        self.clear_stage()
        self.scene_add()
        self.clear_stage()
        self.scene_sub()
        self.clear_stage()
        self.scene_summary()
        self.clear_stage(0.8)