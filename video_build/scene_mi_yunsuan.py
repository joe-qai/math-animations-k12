# -*- coding: utf-8 -*-
"""幂的运算：同底数幂乘除、幂的乘方、积的乘方、零指数与负整数指数。七年级下。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


def place(g, x, y):
    """左边缘对齐 x，竖直中心落在 y。"""
    g.move_to([0, 0, 0])
    g.shift(RIGHT * (x - g.get_left()[0]) + UP * (y - g.get_center()[1]))
    return g


def pw(base_s: str, exp_s: str, size: int = 30, color: str = CHALK,
       ec: str | None = None) -> VGroup:
    """手写「底数 + 上标指数」，避免依赖 LaTeX。"""
    b = txt(base_s, size=size, color=color)
    e = txt(exp_s, size=max(15, int(size * 0.6)), color=ec or color)
    e.next_to(b, RIGHT, buff=0.03)
    e.shift(UP * b.height * 0.34)
    return VGroup(b, e)


def expr(*parts, size: int = 30, buff: float = 0.16, color: str = CHALK) -> VGroup:
    """把若干文字 / 幂拼成一行，底部对齐。"""
    g = VGroup()
    for p in parts:
        if isinstance(p, str):
            g.add(txt(p, size=size, color=color))
        else:
            g.add(p)
    g.arrange(RIGHT, buff=buff, aligned_edge=DOWN)
    return g


def frac(n: str, d: str, color: str = CHALK, size: int = 28) -> VGroup:
    """竖排分数（自建）。"""
    t1 = txt(str(n), size=size, color=color)
    t2 = txt(str(d), size=size, color=color)
    line = Line(LEFT, RIGHT, color=color, stroke_width=2)
    line.set_width(max(t1.width, t2.width) + 0.14)
    return VGroup(t1, line, t2).arrange(DOWN, buff=0.08)


class MiYunsuanScene(NarratedScene):
    lesson = "mi-yunsuan"

    def clear_stage(self, run_time: float = 0.5):
        keep = {id(self._track), id(self._fill)}
        junk = [m for m in self.mobjects if id(m) not in keep]
        if junk:
            self.play(*[FadeOut(m) for m in junk], run_time=run_time)
        self.cur_title = None
        self.cur_sub = None

    # ---------------- 0. 一张纸对折十次 ---------------- 19.9
    def scene_story(self):
        self.section(0, "对折十次，有多少层")

        paper = Rectangle(width=1.55, height=2.0, color=CHALK, stroke_width=2.2)
        paper.move_to([-5.0, 0.75, 0])
        fold = DashedLine([-5.0, 1.75, 0], [-5.0, -0.25, 0], color=DIM, stroke_width=1.8)
        self.play(Create(paper), run_time=0.9)
        self.play(Create(fold), run_time=0.6)
        self.play(paper.animate.set_fill(CHALK, opacity=0.12), run_time=0.6)
        plab = txt("对折", size=25, color=DIM).move_to([-5.0, -0.75, 0])
        self.play(FadeIn(plab, shift=UP * 0.05), run_time=0.6)

        head = txt("对折以后有几层？", size=28, color=GOLD).move_to([1.3, 2.15, 0])
        self.play(FadeIn(head, shift=UP * 0.05), run_time=0.7)

        rows = [
            ("对折 1 次", "2 层", CHALK),
            ("对折 2 次", "4 层", CHALK),
            ("对折 3 次", "8 层", CHALK),
            ("对折 10 次", "1024 层", GOLD),
        ]
        y = 1.25
        for left_s, right_s, c in rows:
            line = VGroup(
                txt(left_s, size=26, color=c),
                txt(right_s, size=27, color=c),
            ).arrange(RIGHT, buff=0.75, aligned_edge=DOWN)
            place(line, -0.9, y)
            self.play(FadeIn(line, shift=RIGHT * 0.05), run_time=0.62)
            y -= 0.72

        line2 = expr(pw("2", "10", size=28, color=GOLD), " = 1024", size=28, color=GOLD)
        place(line2, -0.9, -1.75)
        self.play(FadeIn(line2, shift=UP * 0.05), run_time=0.8)

        note = txt("每一次都乘 2，重复相乘就写成幂", size=26, color=DIM).move_to([0, -2.5, 0])
        self.play(FadeIn(note, shift=UP * 0.05), run_time=0.7)
        self.wait(3.2)
        self.finish_section()

    # ---------------- 1. 同底数幂相乘 ---------------- 18.5
    def scene_mul(self):
        self.section(1, "同底数幂相乘：指数相加")

        head = expr(pw("2", "3"), " × ", pw("2", "2"), " = ",
                    pw("2", "5"), size=34, buff=0.2)
        head.move_to([0, 2.1, 0])
        self.play(FadeIn(head, shift=UP * 0.05), run_time=1.0)

        b1 = txt("2 × 2 × 2", size=30, color=GOLD).move_to([-3.6, 1.0, 0])
        b2 = txt("×", size=28, color=DIM).move_to([-0.45, 1.0, 0])
        b3 = txt("2 × 2", size=30, color=BLUE).move_to([1.5, 1.0, 0])
        self.play(FadeIn(b1, shift=UP * 0.05), run_time=0.7)
        self.play(FadeIn(b2), FadeIn(b3, shift=UP * 0.05), run_time=0.7)

        cnt = txt("一共 5 个 2 相乘", size=28, color=GREEN).move_to([0, 0.15, 0])
        self.play(FadeIn(cnt, shift=UP * 0.05), run_time=0.75)

        rule = label_box("底数不变，指数相加", size=30, color=GOLD).move_to([0, -0.85, 0])
        self.play(FadeIn(rule, scale=0.97), run_time=0.9)

        form = expr(pw("a", "m", size=32, color=GOLD), "·",
                    pw("a", "n", size=32, color=GOLD), "=",
                    pw("a", "m+n", size=32, color=GOLD), size=32, buff=0.2)
        form.move_to([0, -1.95, 0])
        self.play(FadeIn(form, shift=UP * 0.05), run_time=0.9)

        note = txt("底数必须相同，这条法则才管用", size=25, color=DIM).move_to([0, -2.62, 0])
        self.play(FadeIn(note, shift=UP * 0.05), run_time=0.7)
        self.wait(2.0)
        self.finish_section()

    # ---------------- 2. 幂的乘方 ---------------- 19.1
    def scene_power(self):
        self.section(2, "幂的乘方：指数相乘")

        title = expr(pw("a", "3", size=34), " 的平方", size=32)
        title.move_to([0, 2.15, 0])
        self.play(FadeIn(title, shift=UP * 0.05), run_time=0.8)

        row1 = txt("(a × a × a) × (a × a × a)", size=27, color=CHALK).move_to([0, 1.2, 0])
        self.play(FadeIn(row1, shift=UP * 0.05), run_time=0.85)

        cnt = txt("一共 3 × 2 = 6 个 a 相乘", size=28, color=GREEN).move_to([0, 0.4, 0])
        self.play(FadeIn(cnt, shift=UP * 0.05), run_time=0.8)

        base = txt("(", size=40, color=GOLD)
        inner = pw("a", "m", size=32, color=GOLD)
        rp = txt(")", size=40, color=GOLD)
        left_part = VGroup(base, inner, rp).arrange(RIGHT, buff=0.05, aligned_edge=DOWN)
        expo = txt("n", size=21, color=GOLD)
        expo.next_to(rp, RIGHT, buff=0.09)
        expo.align_to(inner, UP)
        eq = txt("=", size=32, color=DIM)
        eq.next_to(expo, RIGHT, buff=0.24)
        eq.align_to(rp, DOWN)
        right = pw("a", "mn", size=32, color=GOLD)
        right.next_to(eq, RIGHT, buff=0.24)
        right.align_to(eq, DOWN)
        whole = VGroup(left_part, expo, eq, right)
        whole.move_to([0, -0.7, 0])
        self.play(FadeIn(whole, shift=UP * 0.05), run_time=0.95)

        rule = label_box("底数不变，指数相乘", size=30, color=GOLD).move_to([0, -1.85, 0])
        self.play(FadeIn(rule, scale=0.97), run_time=0.9)

        note = txt("和「同底数幂相乘」比一比，一个加、一个乘", size=25, color=DIM).move_to([0, -2.55, 0])
        self.play(FadeIn(note, shift=UP * 0.05), run_time=0.7)
        self.wait(2.0)
        self.finish_section()

    # ---------------- 3. 积的乘方 ---------------- 16.6
    def scene_prod(self):
        self.section(3, "积的乘方：每个因数都要乘方")

        form = VGroup(
            txt("(", size=40, color=GOLD),
            txt("ab", size=32, color=GOLD),
            txt(")", size=40, color=GOLD),
        ).arrange(RIGHT, buff=0.05, aligned_edge=DOWN)
        en = txt("n", size=21, color=GOLD)
        en.next_to(form[2], RIGHT, buff=0.09)
        en.align_to(form[1], UP)
        eq = txt("=", size=32, color=DIM)
        eq.next_to(en, RIGHT, buff=0.26)
        eq.align_to(form[2], DOWN)
        right = VGroup(pw("a", "n", size=32, color=GOLD), pw("b", "n", size=32, color=GOLD)).arrange(RIGHT, buff=0.22)
        right.next_to(eq, RIGHT, buff=0.26)
        right.align_to(eq, DOWN)
        top = VGroup(form, en, eq, right)
        top.move_to([0, 2.0, 0])
        self.play(FadeIn(top, shift=UP * 0.05), run_time=1.0)

        row = VGroup(
            txt("(", size=38, color=CHALK),
            txt("2x", size=32, color=CHALK),
            txt(")", size=38, color=CHALK),
        ).arrange(RIGHT, buff=0.05, aligned_edge=DOWN)
        e3 = txt("3", size=21, color=CHALK)
        e3.next_to(row[2], RIGHT, buff=0.09)
        e3.align_to(row[1], UP)
        eq2 = txt("=", size=30, color=DIM)
        eq2.next_to(e3, RIGHT, buff=0.24)
        eq2.align_to(row[2], DOWN)
        r2 = VGroup(pw("2", "3", size=30, color=GREEN), pw("x", "3", size=30, color=GREEN)).arrange(RIGHT, buff=0.1)
        r2.next_to(eq2, RIGHT, buff=0.24)
        r2.align_to(eq2, DOWN)
        line = VGroup(row, e3, eq2, r2)
        line.move_to([0, 0.9, 0])
        self.play(FadeIn(line, shift=UP * 0.05), run_time=0.9)

        res2 = txt("= 8x³", size=32, color=GREEN).move_to([0, 0.05, 0])
        self.play(FadeIn(res2, shift=UP * 0.05), run_time=0.8)

        warn = label_box("系数 2 也要三次方", size=29, color=RED).move_to([0, -0.95, 0])
        self.play(FadeIn(warn, scale=0.97), run_time=0.9)

        note = txt("括号里每个因数都要乘方，别漏了数字", size=26, color=DIM).move_to([0, -1.95, 0])
        self.play(FadeIn(note, shift=UP * 0.05), run_time=0.8)
        self.wait(2.0)
        self.finish_section()

    # ---------------- 4. 同底数幂相除、零指数 ---------------- 18.7
    def scene_div(self):
        self.section(4, "同底数幂相除：指数相减")

        head = expr(pw("2", "5"), " ÷ ", pw("2", "3"), " = ",
                    pw("2", "2"), size=32, buff=0.18)
        head.move_to([0, 2.15, 0])
        self.play(FadeIn(head, shift=UP * 0.05), run_time=0.9)

        top = expr(pw("a", "m", size=32, color=GOLD), "÷",
                   pw("a", "n", size=32, color=GOLD), "=",
                   pw("a", "m-n", size=32, color=GOLD), size=32, buff=0.2)
        top.move_to([0, 1.15, 0])
        self.play(FadeIn(top, shift=UP * 0.05), run_time=0.9)

        zero = txt("指数相同时：a⁰ = 1（a ≠ 0）", size=30, color=BLUE).move_to([0, 0.1, 0])
        self.play(FadeIn(zero, shift=UP * 0.05), run_time=0.85)

        exs = VGroup(
            txt("3⁵ ÷ 3⁵ = 1", size=28, color=CHALK),
            txt("(-2)⁰ = 1", size=28, color=CHALK),
            txt("7⁰ = 1", size=28, color=CHALK),
        ).arrange(RIGHT, buff=0.9).move_to([0, -0.95, 0])
        for e in exs:
            self.play(FadeIn(e, shift=UP * 0.05), run_time=0.55)

        note = txt("底数不能是 0，0⁰ 没有意义", size=27, color=RED).move_to([0, -1.95, 0])
        self.play(FadeIn(note, shift=UP * 0.05), run_time=0.8)

        tail = txt("任何不等于 0 的数的 0 次幂都等于 1", size=25, color=DIM).move_to([0, -2.6, 0])
        self.play(FadeIn(tail, shift=UP * 0.05), run_time=0.7)
        self.wait(2.2)
        self.finish_section()

    # ---------------- 5. 负整数指数 ---------------- 17.6
    def scene_neg(self):
        self.section(5, "负整数指数：变成倒数")

        form = VGroup(
            pw("a", "-n", size=34, color=GOLD),
            txt("=", size=32, color=DIM),
            frac("1", "aⁿ", color=GOLD, size=28),
        ).arrange(RIGHT, buff=0.28)
        form.move_to([0, 2.0, 0])
        self.play(FadeIn(form, shift=UP * 0.05), run_time=1.0)

        row = VGroup(
            pw("2", "-3", size=32, color=CHALK),
            txt("=", size=30, color=DIM),
            frac("1", "2³", color=GREEN, size=26),
            txt("=", size=30, color=DIM),
            frac("1", "8", color=GREEN, size=26),
        ).arrange(RIGHT, buff=0.26)
        row.move_to([0, 0.85, 0])
        self.play(FadeIn(row, shift=UP * 0.05), run_time=1.0)

        why = txt("同底数幂相除，指数相减，减出负数就是这个结果", size=26, color=DIM)
        why.move_to([0, -0.15, 0])
        self.play(FadeIn(why, shift=UP * 0.05), run_time=0.8)

        sci = VGroup(
            txt("0.001 = ", size=29, color=CHALK),
            pw("10", "-3", size=29, color=BLUE),
        ).arrange(RIGHT, buff=0.14).move_to([0, -1.15, 0])
        self.play(FadeIn(sci, shift=UP * 0.05), run_time=0.8)

        note = label_box("负指数 = 取倒数，不是变负数", size=28, color=RED).move_to([0, -2.15, 0])
        self.play(FadeIn(note, scale=0.97), run_time=0.9)
        self.wait(2.0)
        self.finish_section()

    # ---------------- 6. 例题 + 易错点 ---------------- 23.2
    def scene_ex(self):
        self.section(6, "例题与三个易错点")

        prob = VGroup(
            txt("(", size=38, color=CHALK),
            pw("x", "2", size=32, color=CHALK),
            txt(")", size=38, color=CHALK),
        ).arrange(RIGHT, buff=0.05, aligned_edge=DOWN)
        p3 = txt("3", size=21, color=CHALK)
        p3.next_to(prob[2], RIGHT, buff=0.09)
        p3.align_to(prob[1], UP)
        dot = txt("·", size=34, color=CHALK)
        dot.next_to(p3, RIGHT, buff=0.24)
        dot.align_to(prob[1], DOWN)
        xx = txt("x", size=32, color=CHALK)
        xx.next_to(dot, RIGHT, buff=0.24)
        xx.align_to(dot, DOWN)
        prob_g = VGroup(prob, p3, dot, xx)
        prob_g.move_to([0, 2.15, 0])
        self.play(FadeIn(prob_g, shift=UP * 0.05), run_time=0.9)

        s1 = expr("=", pw("x", "6", size=32, color=BLUE), "·", "x", size=32, buff=0.2)
        s1.move_to([0, 1.25, 0])
        self.play(FadeIn(s1, shift=UP * 0.05), run_time=0.8)

        s2 = expr("=", pw("x", "7", size=34, color=GREEN), size=34, buff=0.12)
        s2.move_to([0, 0.45, 0])
        self.play(FadeIn(s2, shift=UP * 0.05), run_time=0.8)

        note = txt("先算幂的乘方，再把指数相加", size=27, color=GOLD).move_to([0, -0.3, 0])
        self.play(FadeIn(note, shift=UP * 0.05), run_time=0.7)

        items = [
            ("同底数幂相乘写成指数相乘", "应该是相加"),
            ("幂的乘方写成指数相加", "应该是相乘"),
            ("积的乘方漏掉系数", "2x 的三次方 = 8x³"),
        ]
        y = -1.15
        for bad_s, good_s in items:
            bad = txt(bad_s, size=24, color=RED).move_to([-3.4, y, 0])
            good = txt(good_s, size=23, color=GREEN).move_to([3.5, y, 0])
            cross = Line([bad.get_left()[0] - 0.08, y - 0.02, 0],
                         [bad.get_right()[0] + 0.08, y - 0.02, 0],
                         color=RED, stroke_width=2.4)
            self.play(FadeIn(bad, shift=RIGHT * 0.05), run_time=0.55)
            self.play(Create(cross), FadeIn(good, shift=RIGHT * 0.05), run_time=0.65)
            y -= 0.68

        self.wait(2.0)
        self.finish_section()

    def construct(self):
        self.scene_story()
        self.clear_stage()
        self.scene_mul()
        self.clear_stage()
        self.scene_power()
        self.clear_stage()
        self.scene_prod()
        self.clear_stage()
        self.scene_div()
        self.clear_stage()
        self.scene_neg()
        self.clear_stage()
        self.scene_ex()
        self.clear_stage(0.8)