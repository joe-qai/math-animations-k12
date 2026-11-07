# -*- coding: utf-8 -*-
"""一元二次方程：一般形式与四种解法。九年级上。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


def P(x, y):
    return np.array([float(x), float(y), 0.0])


def rect(x0, y0, w, h, color=CHALK, width=2.8, fill=0.06) -> Rectangle:
    return Rectangle(width=w, height=h, color=color, stroke_width=width,
                     fill_color=color, fill_opacity=fill).move_to([x0 + w / 2, y0 + h / 2, 0])


def frac(num: Mobject, den: Mobject, color=CHALK, lw: float = 2.4,
         gap: float = 0.10, pad: float = 0.08) -> VGroup:
    """竖排分数：分子在横线上，分母在横线下。"""
    w = max(num.width, den.width) + pad * 2
    line = Line(P(-w / 2, 0), P(w / 2, 0), color=color, stroke_width=lw)
    num.next_to(line, UP, buff=gap)
    den.next_to(line, DOWN, buff=gap)
    return VGroup(num, line, den)


class YiyuanErciFangchengScene(NarratedScene):
    lesson = "yiyuan-erci-fangcheng"

    def clear_stage(self, run_time: float = 0.5):
        keep = {id(self._track), id(self._fill)}
        junk = [m for m in self.mobjects if id(m) not in keep]
        if junk:
            self.play(*[FadeOut(m) for m in junk], run_time=run_time)
        self.cur_title = None
        self.cur_sub = None

    # ---------------- 0. 两个实际问题 ---------------- 30.3
    def scene_intro(self):
        self.section(0, "从两个实际问题说起")

        # 左：正方形花坛
        sq = rect(-5.9, 0.55, 1.7, 1.7, GOLD)
        xl = txt("x", size=24, color=GOLD).move_to([-5.05, 0.22, 0])
        area = txt("面积 36", size=22, color=DIM).move_to([-5.05, 2.62, 0])
        self.play(Create(sq), FadeIn(area), run_time=1.0)
        self.play(FadeIn(xl, scale=0.9), run_time=0.6)
        e1 = txt("x² = 36", size=30, color=GOLD).move_to([-5.05, -0.95, 0])
        self.play(FadeIn(e1, shift=UP * 0.04), run_time=0.9)
        self.wait(0.9)

        # 右：长方形菜地
        rc = rect(1.9, 0.85, 2.1, 1.4, GREEN)
        wl = txt("x", size=22, color=GREEN).move_to([2.95, 0.52, 0])
        ll = txt("x + 2", size=22, color=GREEN).move_to([2.95, 2.55, 0])
        ar2 = txt("面积 24", size=22, color=DIM).move_to([4.6, 1.55, 0])
        self.play(Create(rc), FadeIn(ar2), run_time=1.0)
        self.play(FadeIn(wl, scale=0.9), FadeIn(ll, scale=0.9), run_time=0.8)
        e2 = txt("x (x + 2) = 24", size=30, color=GREEN).move_to([2.95, -0.35, 0])
        self.play(FadeIn(e2, shift=UP * 0.04), run_time=0.9)
        self.wait(1.1)

        e3 = txt("x² + 2x − 24 = 0", size=26, color=GREEN).move_to([2.95, -1.15, 0])
        self.play(FadeIn(e3, shift=UP * 0.04), run_time=0.85)
        self.wait(1.0)

        d1 = txt("只含一个未知数，未知数的最高次数是 2", size=25, color=CHALK)
        d1.move_to([0, -2.0, 0])
        self.play(FadeIn(d1, shift=UP * 0.04), run_time=0.95)
        box = label_box("这样的方程，叫一元二次方程", size=25, color=GOLD)
        box.move_to([0, -2.75, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.05)
        self.wait(11.0)
        self.finish_section()

    # ---------------- 1. 一般形式 ---------------- 26.7
    def scene_general(self):
        self.section(1, "一般形式：ax² + bx + c = 0")

        f = txt("ax² + bx + c = 0", size=54, color=GOLD).move_to([-0.7, 1.75, 0])
        cond = txt("(a ≠ 0)", size=32, color=RED).next_to(f, RIGHT, buff=0.28)
        cond.align_to(f, DOWN)
        self.play(FadeIn(f, scale=0.98), run_time=1.0)
        self.play(FadeIn(cond, shift=LEFT * 0.05), run_time=0.8)
        self.wait(0.8)

        boxes = [
            ("a　二次项系数", "a ≠ 0", -4.1, GOLD),
            ("b　一次项系数", "可以为 0", -0.2, GREEN),
            ("c　常数项", "可以为 0", 3.7, BLUE),
        ]
        for s1, s2, cx, col in boxes:
            b = label_box(s1, size=23, color=col).move_to([cx, 0.55, 0])
            n = txt(s2, size=20, color=DIM).move_to([cx, 0.02, 0])
            self.play(FadeIn(b, scale=0.97), run_time=0.75)
            self.play(FadeIn(n, shift=UP * 0.04), run_time=0.6)
        self.wait(0.9)

        ex1 = txt("例：3x² − 5x + 2 = 0", size=27, color=CHALK).move_to([0, -0.9, 0])
        self.play(FadeIn(ex1, shift=UP * 0.04), run_time=0.85)
        ex2 = txt("a = 3，b = −5，c = 2", size=29, color=GOLD).move_to([0, -1.7, 0])
        self.play(FadeIn(ex2, shift=UP * 0.04), run_time=0.9)
        self.wait(0.8)

        tip = txt("系数要带符号，负号不能丢", size=24, color=RED).move_to([0, -2.6, 0])
        self.play(FadeIn(tip, shift=UP * 0.04), run_time=0.9)
        self.wait(8.5)
        self.finish_section()

    # ---------------- 2. 直接开平方与因式分解 ---------------- 27.4
    def scene_factor(self):
        self.section(2, "解法一：开平方与因式分解")

        l1 = txt("x² = 36", size=36, color=CHALK).move_to([-3.6, 1.55, 0])
        a1 = Arrow(P(-1.5, 1.55), P(-0.2, 1.55), color=GOLD, stroke_width=3,
                   buff=0, max_tip_length_to_length_ratio=0.18)
        r1 = txt("x = ±6", size=40, color=GOLD).move_to([1.7, 1.55, 0])
        self.play(FadeIn(l1, shift=UP * 0.04), run_time=0.8)
        self.play(GrowArrow(a1), run_time=0.6)
        self.play(FadeIn(r1, scale=0.97), run_time=0.85)
        self.wait(0.9)

        l2 = txt("x² − 5x = 0", size=36, color=CHALK).move_to([-4.4, 0.1, 0])
        a2 = Arrow(P(-2.5, 0.1), P(-1.3, 0.1), color=GOLD, stroke_width=3,
                   buff=0, max_tip_length_to_length_ratio=0.18)
        r2 = txt("x (x − 5) = 0", size=34, color=GOLD).move_to([0.2, 0.1, 0])
        a3 = Arrow(P(1.9, 0.1), P(3.1, 0.1), color=GOLD, stroke_width=3,
                   buff=0, max_tip_length_to_length_ratio=0.18)
        r3 = txt("x = 0 或 5", size=34, color=GREEN).move_to([4.9, 0.1, 0])
        self.play(FadeIn(l2, shift=UP * 0.04), run_time=0.8)
        self.play(GrowArrow(a2), run_time=0.55)
        self.play(FadeIn(r2, shift=UP * 0.04), run_time=0.8)
        self.play(GrowArrow(a3), run_time=0.55)
        self.play(FadeIn(r3, shift=UP * 0.04), run_time=0.8)
        self.wait(1.0)

        note = txt("关键：把方程变成两个因式相乘等于零", size=26, color=CHALK)
        note.move_to([0, -1.25, 0])
        self.play(FadeIn(note, shift=UP * 0.04), run_time=0.95)
        self.wait(0.8)

        box = label_box("先看能不能分解，再考虑其它解法", size=24, color=GOLD)
        box.move_to([0, -2.35, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.0)
        self.wait(7.5)
        self.finish_section()

    # ---------------- 3. 配方法 ---------------- 26.8
    def scene_square(self):
        self.section(3, "解法二：配方法")

        head = txt("x² + 6x − 7 = 0", size=36, color=CHALK).move_to([0, 2.4, 0])
        self.play(FadeIn(head, shift=UP * 0.04), run_time=0.9)
        self.wait(0.7)

        rows = [
            ("①", "x² + 6x = 7", CHALK),
            ("②", "x² + 6x + 9 = 16", CHALK),
            ("③", "(x + 3)² = 16", GOLD),
            ("④", "x + 3 = ±4　→　x = 1 或 −7", GREEN),
        ]
        y = 1.5
        for num, s, col in rows:
            n = txt(num, size=24, color=GOLD).move_to([-5.9, y, 0])
            t = txt(s, size=30, color=col)
            t.next_to(n, RIGHT, buff=0.36)
            t.move_to([t.get_center()[0], y, 0])
            self.play(FadeIn(n, shift=RIGHT * 0.05), run_time=0.35)
            self.play(FadeIn(t, shift=RIGHT * 0.04), run_time=0.75)
            y -= 0.88
        self.wait(0.9)

        tip = txt("加的是「一次项系数一半的平方」：(6 ÷ 2)² = 9", size=23, color=RED)
        tip.move_to([0, -1.95, 0])
        self.play(FadeIn(tip, shift=UP * 0.04), run_time=0.95)
        self.wait(0.8)

        note = txt("左边凑成完全平方，右边算成一个数", size=23, color=DIM)
        note.move_to([0, -2.62, 0])
        self.play(FadeIn(note, shift=UP * 0.04), run_time=0.9)
        self.wait(7.0)
        self.finish_section()

    # ---------------- 4. 公式法与判别式 ---------------- 33.3
    def scene_formula(self):
        self.section(4, "解法三：公式法")

        num = txt("−b ± √(b² − 4ac)", size=30, color=CHALK)
        den = txt("2a", size=30, color=CHALK)
        fr = frac(num, den, color=GOLD)
        f = VGroup(txt("x =", size=36, color=GOLD), fr).arrange(RIGHT, buff=0.18)
        f.move_to([0, 2.05, 0])
        self.play(FadeIn(f, scale=0.98), run_time=1.2)
        self.wait(0.9)

        dis = txt("判别式　Δ = b² − 4ac", size=29, color=GOLD).move_to([0, 0.75, 0])
        self.play(FadeIn(dis, shift=UP * 0.04), run_time=0.9)
        self.wait(0.6)

        cases = [
            ("Δ > 0", "两个不相等的实根", GREEN),
            ("Δ = 0", "两个相等的实根", CHALK),
            ("Δ < 0", "没有实根", RED),
        ]
        y = 0.0
        for a, b, col in cases:
            ta = txt(a, size=25, color=col)
            ta.move_to([-1.9, y, 0])
            tb = txt(b, size=24, color=col)
            tb.move_to([2.15, y, 0])
            self.play(FadeIn(ta, shift=RIGHT * 0.04), FadeIn(tb, shift=RIGHT * 0.04),
                      run_time=0.85)
            y -= 0.72
        self.wait(1.0)

        ex1 = txt("例：x² − 2x − 3 = 0", size=26, color=CHALK).move_to([0, -1.95, 0])
        self.play(FadeIn(ex1, shift=UP * 0.04), run_time=0.85)
        ex2 = txt("Δ = 4 + 12 = 16　→　x = 3 或 −1", size=27, color=GOLD)
        ex2.move_to([0, -2.7, 0])
        self.play(FadeIn(ex2, shift=UP * 0.04), run_time=0.95)
        self.wait(12.0)
        self.finish_section()

    # ---------------- 5. 根与系数的关系 ---------------- 23.9
    def scene_vieta(self):
        self.section(5, "根与系数的关系")

        num1 = txt("−b", size=28, color=CHALK)
        den1 = txt("a", size=28, color=CHALK)
        f1 = VGroup(txt("x₁ + x₂ =", size=30, color=GOLD), frac(num1, den1)).arrange(RIGHT, buff=0.16)
        f1.move_to([-2.9, 1.6, 0])

        num2 = txt("c", size=28, color=CHALK)
        den2 = txt("a", size=28, color=CHALK)
        f2 = VGroup(txt("x₁ · x₂ =", size=30, color=GOLD), frac(num2, den2)).arrange(RIGHT, buff=0.16)
        f2.move_to([2.9, 1.6, 0])

        self.play(FadeIn(f1, scale=0.97), run_time=1.0)
        self.play(FadeIn(f2, scale=0.97), run_time=1.0)
        self.wait(1.0)

        ex1 = txt("例：x² − 5x + 6 = 0", size=28, color=CHALK).move_to([0, 0.05, 0])
        self.play(FadeIn(ex1, shift=UP * 0.04), run_time=0.85)
        ex2 = txt("两根是 2 和 3：和 = 5，积 = 6", size=27, color=GOLD)
        ex2.move_to([0, -0.85, 0])
        self.play(FadeIn(ex2, shift=UP * 0.04), run_time=0.9)
        self.wait(0.9)

        note = txt("用之前：先化成一般形式，并确认 a ≠ 0", size=24, color=RED)
        note.move_to([0, -1.95, 0])
        self.play(FadeIn(note, shift=UP * 0.04), run_time=0.95)
        self.wait(9.5)
        self.finish_section()

    # ---------------- 6. 三个易错点 ---------------- 27.2
    def scene_traps(self):
        self.section(6, "三个易错点")

        rows = [
            ("① a 不能等于 0", "二次项系数是字母，先讨论"),
            ("② 公式法前先化一般式", "否则 a、b、c 全错"),
            ("③ 实际问题要检验根", "长度、人数不能为负"),
        ]
        y = 1.7
        for a, b in rows:
            ta = txt(a, size=24, color=RED).move_to([-3.0, y, 0])
            self.play(FadeIn(ta, shift=RIGHT * 0.04), run_time=0.7)
            tb = txt(b, size=22, color=DIM).move_to([3.55, y, 0])
            self.play(FadeIn(tb, shift=RIGHT * 0.04), run_time=0.7)
            y -= 0.95
        self.wait(1.0)

        note = txt("一根算出来是负数，别急着写答案，先看它合不合题意", size=23, color=CHALK)
        note.move_to([0, -1.45, 0])
        self.play(FadeIn(note, shift=UP * 0.04), run_time=1.0)
        self.wait(0.8)

        box = label_box("先化一般式，再挑解法", size=28, color=GOLD)
        box.move_to([0, -2.5, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.1)
        self.wait(9.5)
        self.finish_section()

    def construct(self):
        self.scene_intro()
        self.clear_stage()
        self.scene_general()
        self.clear_stage()
        self.scene_factor()
        self.clear_stage()
        self.scene_square()
        self.clear_stage()
        self.scene_formula()
        self.clear_stage()
        self.scene_vieta()
        self.clear_stage()
        self.scene_traps()
        self.clear_stage(0.8)