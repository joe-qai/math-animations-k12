# -*- coding: utf-8 -*-
"""二元一次方程组：两个条件，两个未知数。八年级下。"""

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


def P(x, y):
    return np.array([float(x), float(y), 0.0])


def brace(h: float = 0.62, color: str = CHALK):
    """用折线画一个左大括号，标在方程组左边。"""
    m = Brace(Line(P(0, -h / 2), P(0, h / 2)), direction=LEFT, color=color,
              buff=0.06)
    return m


class EryuanYiciScene(NarratedScene):
    lesson = "eryuan_yici"

    def clear_stage(self, run_time: float = 0.5):
        keep = {id(self._track), id(self._fill)}
        junk = [m for m in self.mobjects if id(m) not in keep]
        if junk:
            self.play(*[FadeOut(m) for m in junk], run_time=run_time)
        self.cur_title = None
        self.cur_sub = None

    # ---------------- 0. 两个条件 ---------------- 20.1
    def scene_intro(self):
        self.section(0, "两个未知数，要两个条件")

        q = txt("篮球赛共得 16 分，两分球和罚球各几个？", size=27, color=CHALK)
        q.move_to([0, 2.35, 0])
        self.play(FadeIn(q, shift=UP * 0.05), run_time=0.95)
        self.wait(1.0)

        b1 = label_box("总分 = 16 分", size=27, color=GOLD).move_to([-3.4, 1.05, 0])
        self.play(FadeIn(b1, scale=0.97), run_time=0.9)
        b2 = label_box("球数 = 10 个", size=27, color=GREEN).move_to([3.4, 1.05, 0])
        self.play(FadeIn(b2, scale=0.97), run_time=0.9)
        self.wait(1.0)

        n1 = txt("两分球 x 个，罚球 y 个", size=26, color=DIM).move_to([0, 0.1, 0])
        self.play(FadeIn(n1, shift=UP * 0.04), run_time=0.9)
        self.wait(0.8)

        e1 = txt("x + y = 10", size=30, color=GREEN).move_to([-3.2, -1.05, 0])
        self.play(FadeIn(e1, shift=UP * 0.04), run_time=0.8)
        e2 = txt("2x + y = 16", size=30, color=GOLD).move_to([3.2, -1.05, 0])
        self.play(FadeIn(e2, shift=UP * 0.04), run_time=0.8)
        self.wait(1.0)

        tip = label_box("一个条件定不了两个未知数，两个条件才行", size=26, color=CHALK)
        tip.move_to([0, -2.35, 0])
        self.play(FadeIn(tip, scale=0.97), run_time=1.1)
        self.wait(3.0)
        self.finish_section()

    # ---------------- 1. 定义 ---------------- 24.6
    def scene_def(self):
        self.section(1, "二元一次方程与方程组")

        d1 = txt("含有两个未知数", size=28, color=CHALK).move_to([-3.3, 1.75, 0])
        self.play(FadeIn(d1, shift=UP * 0.04), run_time=0.8)
        d2 = txt("含未知数的项的次数都是一次", size=28, color=CHALK).move_to([2.6, 1.75, 0])
        self.play(FadeIn(d2, shift=UP * 0.04), run_time=0.9)
        self.wait(1.0)

        box = label_box("这样的方程叫二元一次方程", size=28, color=GOLD)
        box.move_to([0, 0.75, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.0)
        self.wait(0.8)

        g1 = txt("x + y = 10", size=27, color=GREEN).move_to([-2.1, 0.15, 0])
        g2 = txt("2x + y = 16", size=27, color=GREEN).move_to([-2.1, -0.55, 0])
        br = Brace(Line(P(-3.85, -0.9), P(-3.85, 0.5)), direction=LEFT, color=GREEN, buff=0.1)
        self.play(FadeIn(g1, shift=UP * 0.04), run_time=0.7)
        self.play(FadeIn(g2, shift=UP * 0.04), run_time=0.7)
        self.play(Create(br), run_time=0.7)
        self.wait(0.8)

        dt = txt("两个方程合在一起，就叫二元一次方程组", size=25, color=DIM)
        dt.move_to([0, -1.55, 0])
        self.play(FadeIn(dt, shift=UP * 0.04), run_time=0.9)
        self.wait(1.2)

        bad = txt("xy = 6", size=30, color=RED).move_to([-3.5, -2.45, 0])
        self.play(FadeIn(bad, shift=UP * 0.04), run_time=0.7)
        bl = txt("次数是二次，不是二元一次", size=24, color=RED).move_to([2.4, -2.45, 0])
        self.play(FadeIn(bl, shift=UP * 0.04), run_time=0.8)
        self.play(Create(Line([-4.55, -2.45, 0], [-2.45, -2.45, 0], color=RED, stroke_width=2.6)),
                  run_time=0.5)
        self.wait(2.8)
        self.finish_section()

    # ---------------- 2. 方程组的解 ---------------- 24.1
    def scene_solution(self):
        self.section(2, "方程组的解，是一对值")

        d = txt("同时满足两个方程的一对未知数的值", size=27, color=CHALK)
        d.move_to([0, 2.25, 0])
        self.play(FadeIn(d, shift=UP * 0.05), run_time=0.9)
        self.wait(0.8)

        sol = label_box("x = 6，y = 4", size=34, color=GOLD).move_to([-3.5, 1.0, 0])
        self.play(FadeIn(sol, scale=0.97), run_time=1.0)
        self.wait(0.8)

        n1 = txt("解要成对写，两个值一起", size=25, color=DIM).move_to([-3.5, 0.0, 0])
        self.play(FadeIn(n1, shift=UP * 0.04), run_time=0.8)
        self.wait(1.0)

        v1 = txt("代入第一个：6 + 4 = 10", size=25, color=GREEN).move_to([3.2, 0.95, 0])
        self.play(FadeIn(v1, shift=UP * 0.04), run_time=0.8)
        v1c = txt("成立", size=24, color=GREEN).move_to([5.55, 0.95, 0])
        self.play(FadeIn(v1c), run_time=0.6)

        v2 = txt("代入第二个：2×6 + 4 = 16", size=25, color=GREEN).move_to([3.2, 0.05, 0])
        self.play(FadeIn(v2, shift=UP * 0.04), run_time=0.8)
        v2c = txt("成立", size=24, color=GREEN).move_to([5.75, 0.05, 0])
        self.play(FadeIn(v2c), run_time=0.6)
        self.wait(1.2)

        warn = txt("只满足一个方程，不算方程组的解", size=25, color=RED).move_to([0, -1.35, 0])
        self.play(FadeIn(warn, shift=UP * 0.05), run_time=0.9)
        self.wait(0.8)

        note = txt("判断一组数是不是解：两个方程都代进去验算", size=24, color=DIM)
        note.move_to([0, -2.2, 0])
        self.play(FadeIn(note, shift=UP * 0.05), run_time=0.9)
        self.wait(3.0)
        self.finish_section()

    # ---------------- 3. 代入消元法 ---------------- 25.8
    def scene_subst(self):
        self.section(3, "代入消元：二元变一元")

        head = label_box("思路：消元，把两个未知数变成一个", size=27, color=GOLD)
        head.move_to([0, 2.15, 0])
        self.play(FadeIn(head, scale=0.97), run_time=1.0)
        self.wait(0.8)

        s1 = txt("① 由 x + y = 10 得 y = 10 − x", size=27, color=CHALK).move_to([0, 1.05, 0])
        self.play(FadeIn(s1, shift=UP * 0.04), run_time=0.9)
        self.wait(0.8)

        s2 = txt("② 代入 2x + y = 16", size=27, color=CHALK).move_to([0, 0.05, 0])
        self.play(FadeIn(s2, shift=UP * 0.04), run_time=0.85)

        s3 = txt("2x + (10 − x) = 16", size=29, color=GREEN).move_to([0, -0.85, 0])
        self.play(FadeIn(s3, shift=UP * 0.04), run_time=0.95)
        self.wait(1.0)

        s4 = txt("③ 解一元一次：x = 6", size=27, color=CHALK).move_to([0, -1.75, 0])
        self.play(FadeIn(s4, shift=UP * 0.04), run_time=0.9)

        s5 = txt("④ 回代：y = 10 − 6 = 4", size=27, color=CHALK).move_to([0, -2.5, 0])
        self.play(FadeIn(s5, shift=UP * 0.04), run_time=0.9)
        self.wait(3.0)
        self.finish_section()

    # ---------------- 4. 加减消元法 ---------------- 22.7
    def scene_addsub(self):
        self.section(4, "加减消元：相加或相减")

        items = [
            ("系数相同", "两式相减", GREEN),
            ("系数互为相反数", "两式相加", GREEN),
            ("系数不同", "先乘倍数，配成相同或相反", GOLD),
        ]
        y = 1.9
        for a, b, col in items:
            ta = txt(a, size=26, color=CHALK).move_to([-3.9, y, 0])
            ar = txt("→", size=26, color=DIM).move_to([-1.15, y, 0])
            tb = txt(b, size=26, color=col).move_to([2.15, y, 0])
            self.play(FadeIn(ta, shift=RIGHT * 0.04), run_time=0.6)
            self.play(FadeIn(ar), FadeIn(tb, shift=RIGHT * 0.04), run_time=0.6)
            y -= 1.0
        self.wait(1.2)

        ex = label_box("例：2x + y = 16 减去 x + y = 10 → x = 6", size=26, color=GREEN)
        ex.move_to([0, -1.35, 0])
        self.play(FadeIn(ex, scale=0.97), run_time=1.1)
        self.wait(1.2)

        warn = txt("相减时，每一项都要减，别漏符号", size=25, color=RED).move_to([0, -2.35, 0])
        self.play(FadeIn(warn, shift=UP * 0.04), run_time=0.9)
        self.wait(3.0)
        self.finish_section()

    # ---------------- 5. 例题 ---------------- 30.7
    def scene_example(self):
        self.section(5, "例题：相减消去 y")

        e1 = txt("x + y = 10", size=29, color=CHALK).move_to([-4.2, 1.55, 0])
        e2 = txt("2x + y = 16", size=29, color=CHALK).move_to([-4.2, 0.85, 0])
        self.play(FadeIn(e1, shift=RIGHT * 0.04), run_time=0.7)
        self.play(FadeIn(e2, shift=RIGHT * 0.04), run_time=0.7)
        self.play(Create(Brace(Line(P(-5.15, 0.6), P(-5.15, 1.8)), direction=LEFT,
                               color=DIM, buff=0.08)), run_time=0.6)
        self.wait(1.0)

        s1 = txt("两式相减（y 的系数相同）：", size=25, color=DIM).move_to([1.0, 1.55, 0])
        self.play(FadeIn(s1, shift=RIGHT * 0.04), run_time=0.8)

        s2 = txt("(2x + y) − (x + y) = 16 − 10", size=26, color=CHALK).move_to([1.0, 0.8, 0])
        self.play(FadeIn(s2, shift=RIGHT * 0.04), run_time=0.9)
        self.wait(0.8)

        s3 = txt("x = 6", size=31, color=GREEN).move_to([1.0, 0.0, 0])
        self.play(FadeIn(s3, shift=UP * 0.04), run_time=0.8)
        self.wait(0.8)

        s4 = txt("回代 x + y = 10：6 + y = 10", size=26, color=CHALK).move_to([0, -0.95, 0])
        self.play(FadeIn(s4, shift=UP * 0.04), run_time=0.9)

        s5 = txt("y = 4", size=30, color=GREEN).move_to([0, -1.7, 0])
        self.play(FadeIn(s5, shift=UP * 0.04), run_time=0.8)
        self.wait(0.8)

        chk = txt("验算：2×6 + 4 = 16，正确", size=25, color=DIM).move_to([0, -2.4, 0])
        self.play(FadeIn(chk, shift=UP * 0.04), run_time=0.9)
        self.wait(3.2)
        self.finish_section()

    # ---------------- 6. 应用题与易错点 ---------------- 32.0
    def scene_apply(self):
        self.section(6, "列方程组解应用题")

        steps = [
            ("①", "设两个未知数"),
            ("②", "找两个等量关系，列两个方程"),
            ("③", "解方程组"),
            ("④", "写答，并检验是否符合实际"),
        ]
        y = 1.95
        for num, s in steps:
            n = txt(num, size=24, color=GOLD).move_to([-6.0, y, 0])
            t = txt(s, size=25, color=CHALK)
            t.next_to(n, RIGHT, buff=0.28)
            t.move_to([t.get_center()[0], n.get_center()[1], 0])
            self.play(FadeIn(n, shift=RIGHT * 0.05), run_time=0.45)
            self.play(FadeIn(t, shift=RIGHT * 0.05), run_time=0.6)
            y -= 0.78
        self.wait(1.2)

        warn = txt("易错：解要成对写　·　相减要每项都减　·　应用题要检验",
                   size=23, color=RED)
        warn.move_to([0, -2.2, 0])
        self.play(FadeIn(warn, shift=UP * 0.04), run_time=1.0)
        self.wait(1.0)

        box = label_box("二元变一元，关键在消元", size=29, color=GOLD)
        box.move_to([0, -2.9, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.1)
        self.wait(4.2)
        self.finish_section()

    def construct(self):
        self.scene_intro()
        self.clear_stage()
        self.scene_def()
        self.clear_stage()
        self.scene_solution()
        self.clear_stage()
        self.scene_subst()
        self.clear_stage()
        self.scene_addsub()
        self.clear_stage()
        self.scene_example()
        self.clear_stage()
        self.scene_apply()
        self.clear_stage(0.8)