# -*- coding: utf-8 -*-
"""有理数运算：加减乘除、乘方、混合运算顺序与易错点。七年级上。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


def place(g, x, y):
    """左边缘对齐 x，竖直中心落在 y。"""
    g.move_to([0, 0, 0])
    g.shift(RIGHT * (x - g.get_left()[0]) + UP * (y - g.get_center()[1]))
    return g


def frac(n, d, color=CHALK, size=30):
    """竖排分数（自建，不用 LaTeX）。"""
    t1 = txt(str(n), size=size, color=color)
    t2 = txt(str(d), size=size, color=color)
    line = Line(LEFT, RIGHT, color=color, stroke_width=2)
    line.set_width(max(t1.width, t2.width) + 0.12)
    return VGroup(t1, line, t2).arrange(DOWN, buff=0.08)


def number_line(y=0.0, lo=-3, hi=7, width=10.6):
    nl = NumberLine(x_range=[lo, hi, 1], length=width, include_numbers=False,
                    include_tip=True, color=DIM, stroke_width=2.2)
    nl.move_to([0, y, 0])
    labels = VGroup()
    for i in range(lo + 1, hi):
        labels.add(txt(str(i), size=22, color=DIM).next_to(nl.n2p(i), DOWN, buff=0.16))
    return nl, labels


class YouliYunsuanScene(NarratedScene):
    lesson = "youli-yunsuan"

    def clear_stage(self, run_time: float = 0.5):
        keep = {id(self._track), id(self._fill)}
        junk = [m for m in self.mobjects if id(m) not in keep]
        if junk:
            self.play(*[FadeOut(m) for m in junk], run_time=run_time)
        self.cur_title = None
        self.cur_sub = None

    # ---------------- 0. 从地下二层到五层 ---------------- 19.4
    def scene_story(self):
        self.section(0, "从地下二层到五层")

        e = label_box("电梯：-2 层 → 5 层", size=30, color=GOLD).move_to([-3.2, 2.0, 0])
        t = label_box("温度：-3℃ → 2℃", size=30, color=BLUE).move_to([3.3, 2.0, 0])
        self.play(FadeIn(e, scale=0.97), run_time=0.9)
        self.play(FadeIn(t, scale=0.97), run_time=0.9)

        nl, labels = number_line(y=-0.1)
        self.play(Create(nl), run_time=1.1)
        self.play(FadeIn(labels), run_time=0.8)

        d1 = Dot(nl.n2p(-2), radius=0.12, color=GOLD)
        d2 = Dot(nl.n2p(5), radius=0.12, color=GREEN)
        l1 = txt("-2", size=28, color=GOLD).next_to(d1, UP, buff=0.26)
        l2 = txt("5", size=28, color=GREEN).next_to(d2, UP, buff=0.26)
        self.play(FadeIn(d1, scale=0.7), FadeIn(l1), run_time=0.6)
        self.play(FadeIn(d2, scale=0.7), FadeIn(l2), run_time=0.6)

        arc = Arrow(nl.n2p(-2) + UP * 0.85, nl.n2p(5) + UP * 0.85, color=GOLD,
                    buff=0.04, stroke_width=2.8, max_tip_length_to_length_ratio=0.12)
        up = txt("一共上升 7 层", size=28, color=GOLD).move_to([1.6, 1.05, 0])
        self.play(Create(arc), FadeIn(up), run_time=0.9)

        n1 = txt("升高 5℃，就是把两个温度相减", size=28, color=BLUE).move_to([0, -1.15, 0])
        n2 = txt("负数的加减乘除，都要会算", size=28, color=CHALK).move_to([0, -1.95, 0])
        self.play(FadeIn(n1, shift=UP * 0.05), run_time=0.8)
        self.play(FadeIn(n2, shift=UP * 0.05), run_time=0.8)
        self.wait(3.2)
        self.finish_section()

    # ---------------- 1. 加法：先定符号 ---------------- 18.5
    def scene_add(self):
        self.section(1, "加法：先定符号，再算绝对值")

        rows = [
            ("同号", "符号不变，绝对值相加", "(-3) + (-5) = -8", GOLD),
            ("异号", "取绝对值大的符号，大减小", "(-3) + 5 = 2", BLUE),
            ("相反数", "相加得 0", "3 + (-3) = 0", GREEN),
        ]
        y = 1.9
        for tag, rule, ex, color in rows:
            box = label_box(tag, size=26, color=color).move_to([-5.3, y, 0])
            r = place(txt(rule, size=26, color=CHALK), -3.85, y)
            e = place(txt(ex, size=27, color=color), 1.35, y)
            self.play(FadeIn(box, scale=0.97), run_time=0.55)
            self.play(FadeIn(r, shift=RIGHT * 0.05), run_time=0.6)
            self.play(FadeIn(e, shift=RIGHT * 0.05), run_time=0.6)
            y -= 1.15

        tip = label_box("先定符号，再算绝对值", size=30, color=GOLD).move_to([0, -1.85, 0])
        self.play(FadeIn(tip, scale=0.97), run_time=0.9)
        self.wait(2.6)
        self.finish_section()

    # ---------------- 2. 减法转加法 ---------------- 19.1
    def scene_sub(self):
        self.section(2, "减法：减去一个数 = 加上它的相反数")

        box = label_box("a - b  =  a + (-b)", size=40, color=GOLD).move_to([0, 2.15, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.1)

        f1 = VGroup(
            txt("3 - (-5)", size=31, color=CHALK),
            txt("=", size=29, color=DIM),
            txt("3 + 5", size=31, color=BLUE),
            txt("=", size=29, color=DIM),
            txt("8", size=33, color=GREEN),
        ).arrange(RIGHT, buff=0.34)
        place(f1, -4.0, 0.95)
        self.play(FadeIn(f1, shift=RIGHT * 0.05), run_time=0.9)

        f2 = VGroup(
            txt("-2 - 3", size=31, color=CHALK),
            txt("=", size=29, color=DIM),
            txt("-2 + (-3)", size=31, color=BLUE),
            txt("=", size=29, color=DIM),
            txt("-5", size=33, color=GREEN),
        ).arrange(RIGHT, buff=0.34)
        place(f2, -4.0, 0.0)
        self.play(FadeIn(f2, shift=RIGHT * 0.05), run_time=0.9)

        n1 = place(txt("减号变加号", size=28, color=RED), -3.2, -1.05)
        n2 = place(txt("，减数变相反数", size=28, color=RED), -1.4, -1.05)
        self.play(FadeIn(n1, shift=RIGHT * 0.05), FadeIn(n2, shift=RIGHT * 0.05), run_time=0.9)

        note = txt("减法一律先改成加法，再按加法法则算", size=28, color=CHALK).move_to([0, -1.95, 0])
        self.play(FadeIn(note, shift=UP * 0.05), run_time=0.8)
        self.wait(2.6)
        self.finish_section()

    # ---------------- 3. 乘法：同号得正 ---------------- 18.1
    def scene_mul(self):
        self.section(3, "乘法：同号得正，异号得负")

        exs = [
            ("3 × 4 = 12", GOLD),
            ("(-3) × 4 = -12", BLUE),
            ("(-3) × (-4) = 12", GREEN),
            ("0 × (-5) = 0", DIM),
        ]
        y = 1.65
        for s, c in exs:
            self.play(FadeIn(txt(s, size=31, color=c).move_to([-3.6, y, 0]),
                             shift=RIGHT * 0.05), run_time=0.7)
            y -= 0.78

        box2 = VGroup(
            txt("同号得正", size=28, color=GOLD),
            txt("异号得负", size=28, color=GOLD),
        ).arrange(DOWN, buff=0.3)
        card = VGroup(
            RoundedRectangle(corner_radius=0.12, width=3.6, height=1.6,
                             stroke_color=GOLD, stroke_width=1.6,
                             fill_color=GOLD, fill_opacity=0.1),
            box2,
        ).move_to([3.7, 1.35, 0])
        self.play(FadeIn(card, scale=0.97), run_time=0.95)

        rows = VGroup(
            txt("负号奇数个 → 结果为负", size=26, color=BLUE),
            txt("负号偶数个 → 结果为正", size=26, color=GREEN),
            txt("(-2) × (-3) × (-4) = -24", size=26, color=CHALK),
        ).arrange(DOWN, buff=0.32, aligned_edge=LEFT).move_to([3.7, -0.55, 0])
        for r in rows:
            self.play(FadeIn(r, shift=RIGHT * 0.05), run_time=0.75)

        note = txt("先把符号定下来，再算绝对值相乘", size=27, color=DIM).move_to([0, -2.35, 0])
        self.play(FadeIn(note, shift=UP * 0.05), run_time=0.75)
        self.wait(2.2)
        self.finish_section()

    # ---------------- 4. 除法：乘倒数 ---------------- 18.4
    def scene_div(self):
        self.section(4, "除法：除以一个数 = 乘它的倒数")

        head = VGroup(
            txt("÷ b", size=36, color=CHALK),
            txt("=", size=34, color=DIM),
            txt("×", size=36, color=CHALK),
            frac(1, "b", color=GOLD, size=32),
        ).arrange(RIGHT, buff=0.32)
        card = VGroup(
            RoundedRectangle(corner_radius=0.12, width=5.0, height=1.3,
                             stroke_color=GOLD, stroke_width=1.6,
                             fill_color=GOLD, fill_opacity=0.1),
            head,
        ).move_to([0, 2.15, 0])
        self.play(FadeIn(card, scale=0.97), run_time=1.0)

        rows = [
            ("(-12) ÷ 3 = -4", BLUE),
            ("(-12) ÷ (-3) = 4", GREEN),
            ("12 ÷ (-3) = -4", CHALK),
        ]
        y = 1.0
        for s, c in rows:
            self.play(FadeIn(txt(s, size=32, color=c).move_to([-2.6, y, 0]),
                             shift=RIGHT * 0.05), run_time=0.75)
            y -= 0.75

        warn = label_box("0 不能作除数", size=36, color=RED).move_to([0, -1.45, 0])
        self.play(FadeIn(warn, scale=0.97), run_time=0.9)

        why = txt("找不到一个数和 0 相乘，得到 3 这样的数", size=27, color=DIM).move_to([0, -2.2, 0])
        self.play(FadeIn(why, shift=UP * 0.05), run_time=0.8)
        self.wait(2.2)
        self.finish_section()

    # ---------------- 5. 乘方 ---------------- 18.2
    def scene_power(self):
        self.section(5, "乘方：几个相同因数相乘")

        d = label_box("2³ = 2 × 2 × 2 = 8", size=34, color=GOLD).move_to([0, 2.15, 0])
        self.play(FadeIn(d, scale=0.97), run_time=1.0)

        r = txt("(-2)³ = (-2) × (-2) × (-2) = -8", size=28, color=BLUE).move_to([0, 1.15, 0])
        self.play(FadeIn(r, shift=UP * 0.05), run_time=0.85)

        b1 = label_box("(-2)² = 4", size=36, color=GREEN).move_to([-3.1, 0.0, 0])
        b2 = label_box("-2² = -4", size=36, color=RED).move_to([3.1, 0.0, 0])
        self.play(FadeIn(b1, scale=0.97), run_time=0.85)
        self.play(FadeIn(b2, scale=0.97), run_time=0.85)

        vs = txt("括号里才有负号参与相乘", size=27, color=CHALK).move_to([0, -0.95, 0])
        self.play(FadeIn(vs, shift=UP * 0.05), run_time=0.8)

        rule = txt("负数的偶次幂为正，奇次幂为负", size=29, color=GOLD).move_to([0, -1.75, 0])
        self.play(FadeIn(rule, shift=UP * 0.05), run_time=0.8)

        tip = txt("看完符号，再算数值", size=26, color=DIM).move_to([0, -2.4, 0])
        self.play(FadeIn(tip, shift=UP * 0.05), run_time=0.7)
        self.wait(2.0)
        self.finish_section()

    # ---------------- 6. 运算顺序 + 易错点 ---------------- 21.5
    def scene_order(self):
        self.section(6, "运算顺序和三个易错点")

        flow = VGroup(
            label_box("括号", size=25, color=GREEN),
            txt("→", size=28, color=DIM),
            label_box("乘方", size=25, color=GOLD),
            txt("→", size=28, color=DIM),
            label_box("乘除", size=25, color=BLUE),
            txt("→", size=28, color=DIM),
            label_box("加减", size=25, color=CHALK),
        ).arrange(RIGHT, buff=0.22).move_to([0, 2.2, 0])
        self.play(FadeIn(flow), run_time=1.0)

        e1 = txt("-2² + (-3) × 2", size=31, color=CHALK).move_to([0, 1.15, 0])
        e2 = txt("= -4 - 6 = -10", size=32, color=GREEN).move_to([0, 0.4, 0])
        self.play(FadeIn(e1, shift=UP * 0.05), run_time=0.75)
        self.play(FadeIn(e2, shift=UP * 0.05), run_time=0.75)

        items = [
            ("减法忘记改成加法", "先变加，再算"),
            ("乘方符号判断错", "偶次正，奇次负"),
            ("-2² 和 (-2)² 分不清", "括号管着负号"),
        ]
        y = -0.6
        for bad_s, good_s in items:
            bad = txt(bad_s, size=25, color=RED).move_to([-3.3, y, 0])
            good = txt(good_s, size=24, color=GREEN).move_to([3.5, y, 0])
            cross = Line(bad.get_left() + [-0.1, -0.07, 0],
                         bad.get_right() + [0.1, 0.16, 0],
                         color=RED, stroke_width=2.6)
            self.play(FadeIn(bad, shift=RIGHT * 0.05), run_time=0.55)
            self.play(Create(cross), FadeIn(good, shift=RIGHT * 0.05), run_time=0.65)
            y -= 0.68

        tail = txt("先定符号，再算绝对值", size=28, color=GOLD).move_to([0, -2.45, 0])
        self.play(FadeIn(tail, shift=UP * 0.05), run_time=0.75)
        self.wait(1.8)
        self.finish_section()

    def construct(self):
        self.scene_story()
        self.clear_stage()
        self.scene_add()
        self.clear_stage()
        self.scene_sub()
        self.clear_stage()
        self.scene_mul()
        self.clear_stage()
        self.scene_div()
        self.clear_stage()
        self.scene_power()
        self.clear_stage()
        self.scene_order()
        self.clear_stage(0.8)