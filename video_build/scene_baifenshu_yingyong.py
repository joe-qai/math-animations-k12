# -*- coding: utf-8 -*-
"""百分数应用：折扣、利率、浓度，两道例题与易错点。小升初衔接。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


def place(g, x, y):
    """左边缘对齐 x，竖直中心落在 y。"""
    g.move_to([0, 0, 0])
    g.shift(RIGHT * (x - g.get_left()[0]) + UP * (y - g.get_center()[1]))
    return g


class BaifenshuYingyongScene(NarratedScene):
    lesson = "baifenshu-yingyong"

    def clear_stage(self, run_time: float = 0.5):
        keep = {id(self._track), id(self._fill)}
        junk = [m for m in self.mobjects if id(m) not in keep]
        if junk:
            self.play(*[FadeOut(m) for m in junk], run_time=run_time)
        self.cur_title = None
        self.cur_sub = None

    # ---------------- 0. 商场打折 ---------------- 16.5
    def scene_story(self):
        self.section(0, "商场里的八折")

        tag = label_box("标价 200 元", size=38, color=GOLD).move_to([-3.3, 1.55, 0])
        self.play(FadeIn(tag, scale=0.96), run_time=0.9)

        badge = label_box("全场 8 折", size=44, color=BLUE).move_to([3.4, 1.55, 0])
        self.play(FadeIn(badge, scale=0.94), run_time=1.0)

        q = txt("现价多少？省了多少？", size=33, color=GREEN).move_to([0, 0.2, 0])
        self.play(FadeIn(q, shift=UP * 0.05), run_time=0.9)

        arrow = Arrow([0, -0.35, 0], [0, -0.8, 0], color=DIM, buff=0.06, stroke_width=3,
                      max_tip_length_to_length_ratio=0.3)
        self.play(Create(arrow), run_time=0.6)

        note = VGroup(
            txt("百分数不只是算一算", size=29, color=CHALK),
            txt("买东西、存钱、配糖水都用它", size=29, color=DIM),
        ).arrange(DOWN, buff=0.3).move_to([0, -1.9, 0])
        self.play(FadeIn(note[0], shift=UP * 0.05), run_time=0.8)
        self.play(FadeIn(note[1], shift=UP * 0.05), run_time=0.8)
        self.wait(2.4)
        self.finish_section()

    # ---------------- 1. 几折就是百分之几十 ---------------- 16.0
    def scene_meaning(self):
        self.section(1, "几折就是百分之几十")

        head = txt("几折 = 十分之几 = 百分之几十", size=33, color=GOLD).move_to([0, 2.25, 0])
        self.play(FadeIn(head, shift=UP * 0.05), run_time=0.9)

        rows = [
            ("九折", "9/10", "90%", CHALK),
            ("八折", "8/10", "80%", GREEN),
            ("七五折", "7.5/10", "75%", BLUE),
            ("五折", "5/10", "50%", CHALK),
        ]
        y = 1.15
        for name, frac_s, pct, color in rows:
            g = VGroup(
                txt(name, size=32, color=color),
                txt("=", size=30, color=DIM),
                txt(frac_s, size=30, color=color),
                txt("=", size=30, color=DIM),
                txt(pct, size=32, color=color),
            ).arrange(RIGHT, buff=0.3)
            place(g, -2.6, y)
            self.play(FadeIn(g, shift=RIGHT * 0.05), run_time=0.65)
            y -= 0.72

        tip = label_box("折数越小，价格越便宜", size=29, color=GOLD).move_to([0, -2.05, 0])
        self.play(FadeIn(tip, scale=0.97), run_time=0.9)
        self.wait(2.0)
        self.finish_section()

    # ---------------- 2. 现价怎么算 ---------------- 14.8
    def scene_price(self):
        self.section(2, "打完折要付多少钱")

        box = label_box("现价 = 原价 × 折扣", size=40, color=GOLD).move_to([0, 1.95, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.0)

        r1 = txt("现价：200 × 80% = 160（元）", size=33, color=GREEN).move_to([0, 0.85, 0])
        self.play(FadeIn(r1, shift=UP * 0.05), run_time=0.9)

        r2 = txt("省下：200 - 160 = 40（元）", size=33, color=BLUE).move_to([0, -0.05, 0])
        self.play(FadeIn(r2, shift=UP * 0.05), run_time=0.9)

        r3 = txt("也可以：200 ×（1 - 80%）= 40（元）", size=30, color=DIM).move_to([0, -1.0, 0])
        self.play(FadeIn(r3, shift=UP * 0.05), run_time=0.85)

        note = txt("八折就是按原价的 80% 付钱", size=28, color=CHALK).move_to([0, -1.95, 0])
        self.play(FadeIn(note, shift=UP * 0.05), run_time=0.8)
        self.wait(2.0)
        self.finish_section()

    # ---------------- 3. 利息怎么算 ---------------- 16.9
    def scene_interest(self):
        self.section(3, "存钱怎么算利息")

        box = label_box("利息 = 本金 × 利率 × 时间", size=38, color=GOLD).move_to([0, 2.15, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.1)

        rows = VGroup(
            txt("本金：存进去的钱", size=30, color=CHALK),
            txt("利率：每年百分之几", size=30, color=CHALK),
            txt("时间：存了几年", size=30, color=CHALK),
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT).move_to([-1.7, 0.35, 0])
        for r in rows:
            self.play(FadeIn(r, shift=RIGHT * 0.05), run_time=0.8)
            self.wait(0.15)

        add = label_box("本息和 = 本金 + 利息", size=30, color=GREEN).move_to([0, -1.35, 0])
        self.play(FadeIn(add, scale=0.97), run_time=0.9)

        warn = txt("年利率按一年算，存两年就要乘 2", size=27, color=RED).move_to([0, -2.15, 0])
        self.play(FadeIn(warn, shift=UP * 0.05), run_time=0.8)
        self.wait(2.2)
        self.finish_section()

    # ---------------- 4. 浓度 ---------------- 16.8
    def scene_concentration(self):
        self.section(4, "糖水有多甜")

        sugar = label_box("糖 50 克", size=30, color=GOLD).move_to([-4.4, 1.7, 0])
        water = label_box("水 200 克", size=30, color=BLUE).move_to([-1.7, 1.7, 0])
        plus = txt("+", size=36, color=DIM).move_to([-3.05, 1.7, 0])
        self.play(FadeIn(sugar, scale=0.97), FadeIn(plus), FadeIn(water, scale=0.97), run_time=1.0)

        eq = txt("=", size=36, color=DIM).move_to([0.35, 1.7, 0])
        cup = label_box("糖水 250 克", size=30, color=GREEN).move_to([2.4, 1.7, 0])
        self.play(FadeIn(eq), FadeIn(cup, scale=0.97), run_time=0.9)

        box = label_box("浓度 = 溶质 ÷ 溶液", size=38, color=GOLD).move_to([0, 0.55, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.0)

        rows = VGroup(
            txt("溶质：糖、盐这些被溶解的", size=27, color=CHALK),
            txt("溶剂：水这样的液体", size=27, color=CHALK),
            txt("溶液 = 溶质 + 溶剂", size=27, color=GREEN),
        ).arrange(DOWN, buff=0.34, aligned_edge=LEFT).move_to([-1.4, -1.05, 0])
        for r in rows:
            self.play(FadeIn(r, shift=RIGHT * 0.05), run_time=0.75)

        warn = txt("分母是溶液，不是水的质量", size=27, color=RED).move_to([0, -2.42, 0])
        self.play(FadeIn(warn, shift=UP * 0.05), run_time=0.8)
        self.wait(1.8)
        self.finish_section()

    # ---------------- 5. 例题：折扣 + 利息 ---------------- 15.6
    def scene_ex1(self):
        self.section(5, "打折和存钱两道题")

        left = txt("原价 200 元，打八折", size=30, color=GOLD).move_to([-3.3, 2.35, 0])
        self.play(FadeIn(left, shift=UP * 0.05), run_time=0.7)

        ls = [
            ("现价 200 × 80%", CHALK),
            ("= 160（元）", GREEN),
            ("省下 200 - 160", CHALK),
            ("= 40（元）", GREEN),
        ]
        y = 1.5
        for s, c in ls:
            self.play(FadeIn(txt(s, size=29, color=c).move_to([-3.3, y, 0]),
                             shift=UP * 0.04), run_time=0.6)
            y -= 0.62

        right = txt("存 2000 元，年利率 2.5%，两年", size=28, color=GOLD).move_to([3.3, 2.35, 0])
        self.play(FadeIn(right, shift=UP * 0.05), run_time=0.7)

        rs = [
            ("利息 2000 × 2.5%", CHALK),
            ("× 2 = 100（元）", GREEN),
            ("本息和 2000 + 100", CHALK),
            ("= 2100（元）", GREEN),
        ]
        y = 1.5
        for s, c in rs:
            self.play(FadeIn(txt(s, size=27, color=c).move_to([3.3, y, 0]),
                             shift=UP * 0.04), run_time=0.6)
            y -= 0.62

        note = txt("折数乘原价，利息乘时间，两条线别串", size=27, color=CHALK)
        note.move_to([0, -2.1, 0])
        self.play(FadeIn(note, shift=UP * 0.05), run_time=0.8)
        self.wait(2.2)
        self.finish_section()

    # ---------------- 6. 例题：浓度 + 易错点 ---------------- 17.2
    def scene_ex2(self):
        self.section(6, "配糖水与三个易错点")

        prob = txt("50 克糖放进 200 克水里", size=30, color=CHALK).move_to([0, 2.3, 0])
        self.play(FadeIn(prob, shift=UP * 0.05), run_time=0.8)

        rows = [
            ("糖水 50 + 200 = 250（克）", GOLD),
            ("浓度 50 ÷ 250 = 20%", GREEN),
            ("答：这杯糖水的浓度是 20%", BLUE),
        ]
        y = 1.35
        for s, c in rows:
            self.play(FadeIn(txt(s, size=32, color=c).move_to([-1.0, y, 0]),
                             shift=UP * 0.04), run_time=0.8)
            y -= 0.72

        items = [
            ("打八折不是减 8 元", "是乘 80%"),
            ("利息别忘乘时间", "存几年乘几"),
            ("浓度分母是溶液", "糖加水一起算"),
        ]
        y = -1.15
        for bad_s, good_s in items:
            bad = txt(bad_s, size=25, color=RED).move_to([-3.2, y, 0])
            good = txt(good_s, size=24, color=GREEN).move_to([3.3, y, 0])
            cross = Line(bad.get_left() + [-0.1, -0.06, 0],
                         bad.get_right() + [0.1, 0.14, 0],
                         color=RED, stroke_width=2.6)
            self.play(FadeIn(bad, shift=RIGHT * 0.05), run_time=0.55)
            self.play(Create(cross), FadeIn(good, shift=RIGHT * 0.05), run_time=0.6)
            y -= 0.62

        self.wait(1.4)
        self.finish_section()

    def construct(self):
        self.scene_story()
        self.clear_stage()
        self.scene_meaning()
        self.clear_stage()
        self.scene_price()
        self.clear_stage()
        self.scene_interest()
        self.clear_stage()
        self.scene_concentration()
        self.clear_stage()
        self.scene_ex1()
        self.clear_stage()
        self.scene_ex2()
        self.clear_stage(0.8)