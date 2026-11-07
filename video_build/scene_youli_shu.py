# -*- coding: utf-8 -*-
"""有理数：正负数、数轴、相反数、绝对值、比较大小与易错点。七年级上。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


def place(g, x, y):
    """左边缘对齐 x，竖直中心落在 y。"""
    g.move_to([0, 0, 0])
    g.shift(RIGHT * (x - g.get_left()[0]) + UP * (y - g.get_center()[1]))
    return g


def number_line(y=0.0, lo=-6, hi=6, width=11.6):
    nl = NumberLine(x_range=[lo, hi, 1], length=width, include_numbers=False,
                    include_tip=True, color=DIM, stroke_width=2.2)
    nl.move_to([0, y, 0])
    labels = VGroup()
    for i in range(lo + 1, hi):
        labels.add(txt(str(i), size=22, color=DIM).next_to(nl.n2p(i), DOWN, buff=0.16))
    zero = txt("O", size=22, color=DIM).next_to(nl.n2p(0), DOWN, buff=0.16)
    return nl, labels, zero


class YouliShuScene(NarratedScene):
    lesson = "youli-shu"

    def clear_stage(self, run_time: float = 0.5):
        keep = {id(self._track), id(self._fill)}
        junk = [m for m in self.mobjects if id(m) not in keep]
        if junk:
            self.play(*[FadeOut(m) for m in junk], run_time=run_time)
        self.cur_title = None
        self.cur_sub = None

    # ---------------- 0. 零下二十五度 ---------------- 14.4
    def scene_story(self):
        self.section(0, "零下二十五度")

        t1 = label_box("哈尔滨 零下 25℃", size=32, color=BLUE).move_to([-3.1, 1.6, 0])
        t2 = txt("记作 -25℃", size=36, color=GOLD).move_to([-3.1, 0.55, 0])
        self.play(FadeIn(t1, scale=0.97), run_time=0.9)
        self.play(FadeIn(t2, shift=UP * 0.05), run_time=0.8)

        h1 = label_box("吐鲁番 低于海平面 155 米", size=29, color=GREEN).move_to([2.9, 1.6, 0])
        h2 = txt("记作 -155 米", size=36, color=GOLD).move_to([2.9, 0.55, 0])
        self.play(FadeIn(h1, scale=0.97), run_time=0.9)
        self.play(FadeIn(h2, shift=UP * 0.05), run_time=0.8)

        note = VGroup(
            txt("零上 25 度和零下 25 度", size=28, color=CHALK),
            txt("是一对相反意义的量", size=28, color=DIM),
        ).arrange(DOWN, buff=0.3).move_to([0, -1.35, 0])
        self.play(FadeIn(note[0], shift=UP * 0.05), run_time=0.8)
        self.play(FadeIn(note[1], shift=UP * 0.05), run_time=0.8)
        self.wait(2.6)
        self.finish_section()

    # ---------------- 1. 正数、负数、零 ---------------- 14.1
    def scene_sign(self):
        self.section(1, "正数、负数和零")

        pos = label_box("正数：大于 0 的数", size=30, color=GOLD).move_to([0, 2.0, 0])
        self.play(FadeIn(pos, scale=0.97), run_time=0.8)
        pe = txt("5、+2.5、三分之一", size=30, color=CHALK).move_to([0, 1.15, 0])
        self.play(FadeIn(pe, shift=UP * 0.05), run_time=0.7)

        neg = label_box("负数：小于 0 的数", size=30, color=BLUE).move_to([0, 0.1, 0])
        self.play(FadeIn(neg, scale=0.97), run_time=0.8)
        ne = txt("-3、-0.5、负四分之一", size=30, color=CHALK).move_to([0, -0.75, 0])
        self.play(FadeIn(ne, shift=UP * 0.05), run_time=0.7)

        zero = label_box("0：既不是正数，也不是负数", size=29, color=GREEN)
        zero.move_to([0, -1.75, 0])
        self.play(FadeIn(zero, scale=0.97), run_time=0.9)

        tip = txt("正号可以省略，负号不能省", size=26, color=DIM).move_to([0, -2.5, 0])
        self.play(FadeIn(tip, shift=UP * 0.05), run_time=0.7)
        self.wait(2.0)
        self.finish_section()

    # ---------------- 2. 数轴 ---------------- 16.6
    def scene_axis(self):
        self.section(2, "数轴：原点、正方向、单位长度")

        nl, labels, zero = number_line(y=0.15)
        self.play(Create(nl), run_time=1.2)
        self.play(FadeIn(labels), FadeIn(zero), run_time=0.9)

        o_lab = txt("原点", size=24, color=GOLD).move_to([0, -0.85, 0])
        d_lab = txt("正方向 →", size=24, color=GOLD).move_to([5.1, 0.75, 0])
        u_lab = txt("单位长度 1", size=24, color=GOLD).move_to([-4.5, 0.75, 0])
        self.play(FadeIn(o_lab, shift=UP * 0.05), run_time=0.7)
        self.play(FadeIn(d_lab, shift=UP * 0.05), run_time=0.7)
        self.play(FadeIn(u_lab, shift=UP * 0.05), run_time=0.7)

        note = VGroup(
            txt("每一个有理数", size=28, color=CHALK),
            txt("都能在数轴上找到唯一一个点", size=28, color=GREEN),
        ).arrange(DOWN, buff=0.3).move_to([0, -2.15, 0])
        self.play(FadeIn(note[0], shift=UP * 0.05), run_time=0.7)
        self.play(FadeIn(note[1], shift=UP * 0.05), run_time=0.7)
        self.wait(2.0)
        self.finish_section()

    # ---------------- 3. 相反数 ---------------- 18.0
    def scene_opposite(self):
        self.section(3, "只有符号不同的两个数")

        nl, labels, zero = number_line(y=0.55)
        self.play(Create(nl), FadeIn(labels), FadeIn(zero), run_time=1.1)

        d1 = Dot(nl.n2p(3), radius=0.11, color=GOLD)
        d2 = Dot(nl.n2p(-3), radius=0.11, color=GOLD)
        l1 = txt("3", size=30, color=GOLD).next_to(d1, UP, buff=0.28)
        l2 = txt("-3", size=30, color=GOLD).next_to(d2, UP, buff=0.28)
        self.play(FadeIn(d1, scale=0.7), FadeIn(l1), run_time=0.7)
        self.play(FadeIn(d2, scale=0.7), FadeIn(l2), run_time=0.7)

        seg = DashedLine(nl.n2p(-3), nl.n2p(3), color=GOLD, stroke_width=2.2, dash_length=0.14)
        seg.shift(DOWN * 0.42)
        sym = txt("关于原点对称", size=26, color=GREEN).move_to([0, -0.05, 0])
        self.play(Create(seg), FadeIn(sym, shift=UP * 0.05), run_time=0.9)

        rows = VGroup(
            txt("3 和 -3 互为相反数", size=29, color=CHALK),
            txt("零的相反数还是零", size=29, color=CHALK),
            txt("-(-3) = 3", size=31, color=BLUE),
        ).arrange(DOWN, buff=0.32, aligned_edge=LEFT).move_to([-0.4, -1.55, 0])
        for r in rows:
            self.play(FadeIn(r, shift=RIGHT * 0.05), run_time=0.7)
        self.wait(1.6)
        self.finish_section()

    # ---------------- 4. 绝对值 ---------------- 16.6
    def scene_abs(self):
        self.section(4, "绝对值：到原点的距离")

        nl, labels, zero = number_line(y=0.5)
        self.play(Create(nl), FadeIn(labels), FadeIn(zero), run_time=1.1)

        d = Dot(nl.n2p(-3), radius=0.11, color=BLUE)
        lab = txt("-3", size=30, color=BLUE).next_to(d, UP, buff=0.28)
        self.play(FadeIn(d, scale=0.7), FadeIn(lab), run_time=0.7)

        seg = Arrow(nl.n2p(0) + DOWN * 0.62, nl.n2p(-3) + DOWN * 0.62,
                    color=GOLD, buff=0.02, stroke_width=2.6,
                    max_tip_length_to_length_ratio=0.14)
        dist = txt("距离 3", size=27, color=GOLD).move_to([-1.5, -0.55, 0])
        self.play(Create(seg), FadeIn(dist, shift=UP * 0.05), run_time=0.9)

        box = label_box("|-3| = 3", size=38, color=GOLD).move_to([3.6, 1.65, 0])
        self.play(FadeIn(box, scale=0.97), run_time=0.9)

        rows = VGroup(
            txt("正数的绝对值是它本身", size=28, color=CHALK),
            txt("负数的绝对值是它的相反数", size=28, color=CHALK),
            txt("0 的绝对值是 0，绝对值不小于 0", size=27, color=GREEN),
        ).arrange(DOWN, buff=0.32, aligned_edge=LEFT).move_to([2.3, -1.35, 0])
        for r in rows:
            self.play(FadeIn(r, shift=RIGHT * 0.05), run_time=0.72)
        self.wait(1.6)
        self.finish_section()

    # ---------------- 5. 例题：比大小 ---------------- 18.0
    def scene_example(self):
        self.section(5, "比较 -3 和 -5")

        nl, labels, zero = number_line(y=1.35, lo=-6, hi=2, width=8.4)
        self.play(Create(nl), FadeIn(labels), FadeIn(zero), run_time=1.0)

        d3 = Dot(nl.n2p(-3), radius=0.11, color=GOLD)
        d5 = Dot(nl.n2p(-5), radius=0.11, color=BLUE)
        l3 = txt("-3", size=26, color=GOLD).next_to(d3, UP, buff=0.24)
        l5 = txt("-5", size=26, color=BLUE).next_to(d5, UP, buff=0.24)
        self.play(FadeIn(d3, scale=0.7), FadeIn(l3), run_time=0.6)
        self.play(FadeIn(d5, scale=0.7), FadeIn(l5), run_time=0.6)

        rows = [
            ("-5 在 -3 的左边", BLUE),
            ("所以 -5 < -3", GOLD),
            ("|-5| = 5", CHALK),
            ("-(-3) = 3", GREEN),
            ("数轴上右边的数总比左边的大", DIM),
        ]
        y = 0.25
        for s, c in rows:
            self.play(FadeIn(txt(s, size=29, color=c).move_to([2.4, y, 0]),
                             shift=UP * 0.04), run_time=0.7)
            y -= 0.62

        self.wait(1.4)
        self.finish_section()

    # ---------------- 6. 易错点 ---------------- 15.6
    def scene_warn(self):
        self.section(6, "三个易错点")

        items = [
            ("0 是正数", "0 既不是正数，也不是负数"),
            ("绝对值等于 3 的数只有 3", "还有一个 -3"),
            ("-5 比 -3 大", "越往左越小"),
        ]
        y = 2.0
        for bad_s, note in items:
            bad = txt(bad_s, size=27, color=RED).move_to([-2.9, y, 0])
            n = txt(note, size=24, color=GREEN).move_to([3.5, y, 0])
            cross = Line(bad.get_left() + [-0.1, -0.08, 0],
                         bad.get_right() + [0.1, 0.18, 0],
                         color=RED, stroke_width=2.8)
            self.play(FadeIn(bad, shift=RIGHT * 0.05), run_time=0.6)
            self.play(Create(cross), FadeIn(n, shift=RIGHT * 0.05), run_time=0.7)
            self.wait(0.4)
            y -= 0.9

        rows = VGroup(
            label_box("① 0 既不是正数也不是负数", size=23, color=GOLD),
            label_box("② 绝对值是距离，一定不小于 0", size=23, color=CHALK),
            label_box("③ 数轴上右边的大", size=23, color=GREEN),
        ).arrange(DOWN, buff=0.18).move_to([0, -1.9, 0])
        for r in rows:
            self.play(FadeIn(r, shift=RIGHT * 0.06), run_time=0.6)
            self.wait(0.4)

        self.wait(0.8)
        self.finish_section()

    def construct(self):
        self.scene_story()
        self.clear_stage()
        self.scene_sign()
        self.clear_stage()
        self.scene_axis()
        self.clear_stage()
        self.scene_opposite()
        self.clear_stage()
        self.scene_abs()
        self.clear_stage()
        self.scene_example()
        self.clear_stage()
        self.scene_warn()
        self.clear_stage(0.8)