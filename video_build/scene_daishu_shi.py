# -*- coding: utf-8 -*-
"""代数式与整式加减：用字母表示数、单项式、多项式、同类项、去括号。七年级上。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


def place(g, x, y):
    """左边缘对齐 x，竖直中心落在 y。"""
    g.move_to([0, 0, 0])
    g.shift(RIGHT * (x - g.get_left()[0]) + UP * (y - g.get_center()[1]))
    return g


class DaishuShiScene(NarratedScene):
    lesson = "daishu-shi"

    def clear_stage(self, run_time: float = 0.5):
        keep = {id(self._track), id(self._fill)}
        junk = [m for m in self.mobjects if id(m) not in keep]
        if junk:
            self.play(*[FadeOut(m) for m in junk], run_time=run_time)
        self.cur_title = None
        self.cur_sub = None

    # ---------------- 0. 笔记本与正方形 ---------------- 16.5
    def scene_story(self):
        self.section(0, "用字母表示数")

        sq = Square(side_length=1.7, color=BLUE, stroke_width=2.2).move_to([-4.6, 0.35, 0])
        side = txt("a", size=30, color=BLUE).next_to(sq, DOWN, buff=0.16)
        self.play(Create(sq), run_time=0.9)
        self.play(FadeIn(side, shift=UP * 0.05), run_time=0.6)

        p = txt("周长 4a，面积 a²", size=29, color=GOLD).move_to([-4.6, -1.35, 0])
        self.play(FadeIn(p, shift=UP * 0.05), run_time=0.75)

        books = VGroup()
        for i in range(3):
            r = RoundedRectangle(corner_radius=0.08, width=0.85, height=1.25,
                                 stroke_color=GREEN, stroke_width=1.8,
                                 fill_color=GREEN, fill_opacity=0.12)
            r.move_to([0.7 + i * 1.05, 0.9, 0])
            books.add(r)
        self.play(LaggedStart(*[Create(b) for b in books], lag_ratio=0.25), run_time=1.1)

        lab = txt("每本 a 元", size=27, color=CHALK).move_to([1.75, -0.1, 0])
        three = txt("3 本就是 3a 元", size=31, color=GOLD).move_to([1.75, -0.95, 0])
        self.play(FadeIn(lab, shift=UP * 0.05), run_time=0.7)
        self.play(FadeIn(three, shift=UP * 0.05), run_time=0.8)

        note = txt("用字母表示数，一句话管一类问题", size=28, color=DIM).move_to([0, -2.25, 0])
        self.play(FadeIn(note, shift=UP * 0.05), run_time=0.8)
        self.wait(3.0)
        self.finish_section()

    # ---------------- 1. 什么是代数式 ---------------- 19.8
    def scene_def(self):
        self.section(1, "什么是代数式")

        head = label_box("用运算符号把数和字母连起来", size=30, color=GOLD).move_to([0, 2.3, 0])
        self.play(FadeIn(head, scale=0.97), run_time=0.95)

        chips = VGroup(
            label_box("3a", size=28, color=CHALK),
            label_box("x + 5", size=28, color=CHALK),
            label_box("a² - 1", size=28, color=CHALK),
            label_box("m", size=28, color=CHALK),
        ).arrange(RIGHT, buff=0.55).move_to([0, 1.25, 0])
        for c in chips:
            self.play(FadeIn(c, shift=UP * 0.06), run_time=0.5)
        self.wait(0.4)

        one = txt("单独一个数或一个字母，也是代数式", size=27, color=GREEN).move_to([0, 0.35, 0])
        self.play(FadeIn(one, shift=UP * 0.05), run_time=0.8)

        head2 = label_box("书写四条规矩", size=27, color=GOLD).move_to([0, -0.5, 0])
        self.play(FadeIn(head2, scale=0.97), run_time=0.75)

        rules = VGroup(
            VGroup(txt("① 数字写在字母前面", size=26, color=CHALK),
                   txt("② 乘号可以省略", size=26, color=CHALK)).arrange(RIGHT, buff=1.7),
            VGroup(txt("③ 除法写成分数线", size=26, color=CHALK),
                   txt("④ 带分数化成假分数", size=26, color=CHALK)).arrange(RIGHT, buff=1.7),
        ).arrange(DOWN, buff=0.38).move_to([0, -1.45, 0])
        for r in rules:
            self.play(FadeIn(r, shift=UP * 0.05), run_time=0.7)

        tip = txt("写成 a ÷ b，不合书写规矩", size=25, color=RED).move_to([0, -2.4, 0])
        self.play(FadeIn(tip, shift=UP * 0.05), run_time=0.7)
        self.wait(2.6)
        self.finish_section()

    # ---------------- 2. 单项式与次数 ---------------- 17.0
    def scene_mono(self):
        self.section(2, "单项式：系数与次数")

        ex = txt("3a²b", size=80, color=GOLD).move_to([-3.5, 0.35, 0])
        self.play(FadeIn(ex, scale=0.95), run_time=1.0)

        coef = label_box("系数：3", size=28, color=GOLD).move_to([-3.5, 1.75, 0])
        self.play(FadeIn(coef, shift=DOWN * 0.05), run_time=0.8)

        deg = label_box("次数：2 + 1 = 3", size=28, color=BLUE).move_to([-3.5, -1.1, 0])
        self.play(FadeIn(deg, shift=UP * 0.05), run_time=0.8)

        a1 = Arrow([-3.5, 1.4, 0], [-3.5, 0.95, 0], color=GOLD, buff=0.04,
                   stroke_width=2.4, max_tip_length_to_length_ratio=0.24)
        a2 = Arrow([-3.5, -0.7, 0], [-3.5, -0.25, 0], color=BLUE, buff=0.04,
                   stroke_width=2.4, max_tip_length_to_length_ratio=0.24)
        self.play(Create(a1), Create(a2), run_time=0.8)

        rows = VGroup(
            txt("数与字母的积，叫单项式", size=27, color=CHALK),
            txt("系数：前面的数字因数", size=27, color=GOLD),
            txt("次数：所有字母指数之和", size=27, color=BLUE),
            txt("2x 的系数是 2，次数是 1", size=26, color=DIM),
        ).arrange(DOWN, buff=0.42, aligned_edge=LEFT).move_to([2.4, 0.35, 0])
        for r in rows:
            self.play(FadeIn(r, shift=RIGHT * 0.05), run_time=0.65)

        note = txt("系数要带符号，别把负号丢了", size=26, color=RED).move_to([0, -2.2, 0])
        self.play(FadeIn(note, shift=UP * 0.05), run_time=0.75)
        self.wait(2.4)
        self.finish_section()

    # ---------------- 3. 多项式 ---------------- 17.5
    def scene_poly(self):
        self.section(3, "多项式：几项、几次")

        ex = txt("2x² - 3x + 1", size=58, color=CHALK).move_to([0, 1.85, 0])
        self.play(FadeIn(ex, shift=UP * 0.05), run_time=0.9)

        terms = VGroup(
            label_box("2x²", size=29, color=GOLD),
            label_box("-3x", size=29, color=BLUE),
            label_box("1", size=29, color=GREEN),
        ).arrange(RIGHT, buff=1.1).move_to([0, 0.6, 0])
        for t in terms:
            self.play(FadeIn(t, scale=0.96), run_time=0.55)

        n1 = txt("每个单项式叫一项，这里有三项", size=27, color=CHALK).move_to([0, -0.4, 0])
        self.play(FadeIn(n1, shift=UP * 0.05), run_time=0.75)

        n2 = txt("次数最高的项是 2x²，次数是 2", size=27, color=GOLD).move_to([0, -1.15, 0])
        self.play(FadeIn(n2, shift=UP * 0.05), run_time=0.75)

        tag = label_box("二次三项式", size=30, color=GREEN).move_to([0, -2.05, 0])
        self.play(FadeIn(tag, scale=0.97), run_time=0.8)
        self.wait(2.6)
        self.finish_section()

    # ---------------- 4. 同类项与合并 ---------------- 20.4
    def scene_like(self):
        self.section(4, "同类项：合并时系数相加减")

        head = label_box("字母相同，相同字母的指数也相同", size=29, color=GOLD)
        head.move_to([0, 2.3, 0])
        self.play(FadeIn(head, scale=0.97), run_time=0.95)

        f1 = VGroup(
            txt("3x + 5x", size=31, color=CHALK),
            txt("=", size=29, color=DIM),
            txt("8x", size=33, color=GREEN),
        ).arrange(RIGHT, buff=0.36).move_to([-3.0, 1.3, 0])
        self.play(FadeIn(f1, shift=RIGHT * 0.05), run_time=0.8)

        f2 = VGroup(
            txt("2a²b - 5a²b", size=31, color=CHALK),
            txt("=", size=29, color=DIM),
            txt("-3a²b", size=33, color=GREEN),
        ).arrange(RIGHT, buff=0.36).move_to([-2.4, 0.45, 0])
        self.play(FadeIn(f2, shift=RIGHT * 0.05), run_time=0.8)

        note = txt("系数相加减，字母和指数都不变", size=28, color=GOLD).move_to([0, -0.55, 0])
        self.play(FadeIn(note, shift=UP * 0.05), run_time=0.8)

        b1 = txt("3x 与 3x²", size=28, color=RED).move_to([-2.4, -1.55, 0])
        cross = Line(b1.get_left() + [-0.12, -0.06, 0], b1.get_right() + [0.12, 0.14, 0],
                     color=RED, stroke_width=2.6)
        b2 = txt("指数不同，不是同类项", size=27, color=GREEN).move_to([2.9, -1.55, 0])
        self.play(FadeIn(b1, shift=RIGHT * 0.05), run_time=0.6)
        self.play(Create(cross), FadeIn(b2, shift=RIGHT * 0.05), run_time=0.8)

        tail = txt("合并前先看清字母和指数", size=26, color=DIM).move_to([0, -2.3, 0])
        self.play(FadeIn(tail, shift=UP * 0.05), run_time=0.7)
        self.wait(2.4)
        self.finish_section()

    # ---------------- 5. 去括号 ---------------- 19.4
    def scene_bracket(self):
        self.section(5, "去括号：看前面的符号")

        p_eq = txt("a + (b - c) = a + b - c", size=32, color=CHALK).move_to([0, 2.0, 0])
        p_tag = label_box("前面是加号：各项都不变号", size=27, color=GREEN).move_to([0, 1.1, 0])
        self.play(FadeIn(p_eq, shift=UP * 0.05), run_time=0.85)
        self.play(FadeIn(p_tag, scale=0.97), run_time=0.8)

        m_eq = txt("a - (b - c) = a - b + c", size=32, color=CHALK).move_to([0, 0.0, 0])
        m_tag = label_box("前面是减号：各项都变号", size=27, color=RED).move_to([0, -0.9, 0])
        self.play(FadeIn(m_eq, shift=UP * 0.05), run_time=0.85)
        self.play(FadeIn(m_tag, scale=0.97), run_time=0.8)

        hl = txt("-c 变成 +c，括号里每一项都要变", size=28, color=GOLD).move_to([0, -1.85, 0])
        self.play(FadeIn(hl, shift=UP * 0.05), run_time=0.8)

        tip = txt("只变第一项，是失分最多的写法", size=26, color=DIM).move_to([0, -2.45, 0])
        self.play(FadeIn(tip, shift=UP * 0.05), run_time=0.7)
        self.wait(2.4)
        self.finish_section()

    # ---------------- 6. 例题 + 易错点 ---------------- 19.9
    def scene_ex(self):
        self.section(6, "化简：先括号，再合并")

        prob = txt("3(x + 2) - 2(x - 1)", size=36, color=CHALK).move_to([0, 2.15, 0])
        self.play(FadeIn(prob, shift=UP * 0.05), run_time=0.85)

        s1 = txt("= 3x + 6 - 2x + 2", size=33, color=BLUE).move_to([0, 1.3, 0])
        self.play(FadeIn(s1, shift=UP * 0.05), run_time=0.8)

        s2 = txt("= x + 8", size=36, color=GREEN).move_to([0, 0.55, 0])
        self.play(FadeIn(s2, shift=UP * 0.05), run_time=0.8)

        note = txt("先去括号，再合并同类项", size=27, color=GOLD).move_to([0, -0.2, 0])
        self.play(FadeIn(note, shift=UP * 0.05), run_time=0.7)

        items = [
            ("系数漏乘括号里每一项", "2 要乘每一个"),
            ("去括号忘记变号", "减号后面全变"),
            ("同类项判断错", "字母指数都要看"),
        ]
        y = -1.0
        for bad_s, good_s in items:
            bad = txt(bad_s, size=25, color=RED).move_to([-3.3, y, 0])
            good = txt(good_s, size=24, color=GREEN).move_to([3.5, y, 0])
            cross = Line(bad.get_left() + [-0.1, -0.07, 0],
                         bad.get_right() + [0.1, 0.16, 0],
                         color=RED, stroke_width=2.6)
            self.play(FadeIn(bad, shift=RIGHT * 0.05), run_time=0.55)
            self.play(Create(cross), FadeIn(good, shift=RIGHT * 0.05), run_time=0.65)
            y -= 0.66

        self.wait(1.6)
        self.finish_section()

    def construct(self):
        self.scene_story()
        self.clear_stage()
        self.scene_def()
        self.clear_stage()
        self.scene_mono()
        self.clear_stage()
        self.scene_poly()
        self.clear_stage()
        self.scene_like()
        self.clear_stage()
        self.scene_bracket()
        self.clear_stage()
        self.scene_ex()
        self.clear_stage(0.8)