# -*- coding: utf-8 -*-
"""一元一次不等式（组）：从「最多买几瓶」到解集与数轴。八年级下。"""

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


def P(x, y):
    return np.array([float(x), float(y), 0.0])


def number_line(y: float = 0.0, x0: float = -4.6, x1: float = 4.8,
                color: str = DIM) -> VGroup:
    """一条带箭头的数轴。"""
    axis = Arrow(P(x0, y), P(x1, y), buff=0, color=color, stroke_width=2.2,
                 max_tip_length_to_length_ratio=0.03)
    return VGroup(axis)


def mark_point(x: float, y: float, closed: bool, color: str = GOLD) -> VGroup:
    """数轴上的点：closed=True 画实心，False 画空心。"""
    c = Circle(radius=0.117, color=color, stroke_width=2.6)
    if closed:
        c.set_fill(color, 1.0)
    else:
        c.set_fill(BG, 1.0)
    c.move_to(P(x, y))
    return VGroup(c)


class YiyuanBudengshiScene(NarratedScene):
    lesson = "yiyuan_budengshi"

    def clear_stage(self, run_time: float = 0.5):
        keep = {id(self._track), id(self._fill)}
        junk = [m for m in self.mobjects if id(m) not in keep]
        if junk:
            self.play(*[FadeOut(m) for m in junk], run_time=run_time)
        self.cur_title = None
        self.cur_sub = None

    # ---------------- 0. 最多买几瓶 ---------------- 22.3
    def scene_intro(self):
        self.section(0, "最多买几瓶？")

        q = txt("一瓶 6 元，带 50 元，最多买几瓶？", size=27, color=CHALK)
        q.move_to([0, 2.4, 0])
        self.play(FadeIn(q, shift=UP * 0.05), run_time=0.95)
        self.wait(0.9)

        specs = [
            ("8 瓶", "6 × 8 = 48 元", "48 ≤ 50，够", GREEN, -3.3, True),
            ("9 瓶", "6 × 9 = 54 元", "54 > 50，不够", RED, 3.3, False),
        ]
        for name, calc, verdict, col, cx, ok in specs:
            box = label_box(name, size=30, color=col).move_to([cx, 1.15, 0])
            self.play(FadeIn(box, scale=0.97), run_time=0.9)
            c = txt(calc, size=25, color=CHALK).move_to([cx, 0.25, 0])
            self.play(FadeIn(c, shift=UP * 0.04), run_time=0.8)
            v = txt(verdict, size=25, color=col).move_to([cx, -0.55, 0])
            self.play(FadeIn(v, shift=UP * 0.04), run_time=0.8)
            if ok:
                self.wait(0.8)

        self.wait(1.0)
        n1 = txt("钱够不够，比大小就知道", size=26, color=DIM).move_to([0, -1.5, 0])
        self.play(FadeIn(n1, shift=UP * 0.04), run_time=0.9)

        tip = label_box("「最多」「不超过」用等号写不出来，要用不等号", size=25, color=GOLD)
        tip.move_to([0, -2.45, 0])
        self.play(FadeIn(tip, scale=0.97), run_time=1.1)
        self.wait(3.2)
        self.finish_section()

    # ---------------- 1. 不等式与解集 ---------------- 25.0
    def scene_def(self):
        self.section(1, "不等式、解与解集")

        box = label_box("用不等号连接的式子叫不等式", size=29, color=GOLD)
        box.move_to([0, 2.05, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.0)
        self.wait(0.8)

        syms = VGroup()
        for i, s in enumerate(["<", ">", "≤", "≥", "≠"]):
            t = txt(s, size=34, color=CHALK).move_to([-4.2 + i * 1.55, 1.0, 0])
            syms.add(t)
        self.play(LaggedStart(*[FadeIn(s, shift=UP * 0.08) for s in syms], lag_ratio=0.12),
                  run_time=1.6)
        self.wait(1.0)

        d1 = txt("使不等式成立的未知数的值，叫不等式的解", size=25, color=CHALK)
        d1.move_to([0, -0.05, 0])
        self.play(FadeIn(d1, shift=UP * 0.04), run_time=0.9)

        d2 = txt("所有解合在一起，叫解集", size=25, color=GREEN)
        d2.move_to([0, -0.8, 0])
        self.play(FadeIn(d2, shift=UP * 0.04), run_time=0.9)
        self.wait(1.0)

        ex = txt("x ≤ 8 就是「最多买 8 瓶」", size=27, color=GOLD)
        ex.move_to([0, -1.7, 0])
        self.play(FadeIn(ex, shift=UP * 0.04), run_time=0.9)

        note = txt("解集是一段范围，不是一个数", size=25, color=RED)
        note.move_to([0, -2.55, 0])
        self.play(FadeIn(note, shift=UP * 0.04), run_time=0.9)
        self.wait(3.0)
        self.finish_section()

    # ---------------- 2. 三条基本性质 ---------------- 27.0
    def scene_props(self):
        self.section(2, "不等式的基本性质")

        rows = [
            ("① 两边同加（减）一个数", "方向不变", GREEN),
            ("② 两边同乘（除以）正数", "方向不变", GREEN),
            ("③ 两边同乘（除以）负数", "必须变号", RED),
        ]
        y = 2.0
        for left, right, col in rows:
            a = txt(left, size=25, color=CHALK)
            a.move_to([-2.05, y, 0])
            b = txt("→", size=26, color=DIM).move_to([2.35, y, 0])
            c = txt(right, size=25, color=col).move_to([3.85, y, 0])
            self.play(FadeIn(a, shift=RIGHT * 0.04), run_time=0.6)
            self.play(FadeIn(b), FadeIn(c, shift=RIGHT * 0.04), run_time=0.6)
            y -= 0.82
        self.wait(1.2)

        ex = label_box("−2x > 4", size=30, color=CHALK).move_to([-3.2, -1.05, 0])
        self.play(FadeIn(ex, scale=0.97), run_time=0.9)

        ar = txt("÷(−2)", size=24, color=DIM).move_to([-1.35, -1.05, 0])
        self.play(FadeIn(ar), run_time=0.6)

        res = label_box("x < −2", size=30, color=GOLD).move_to([1.35, -1.05, 0])
        self.play(FadeIn(res, scale=0.97), run_time=0.9)

        flip = txt("方向反了", size=25, color=RED).move_to([3.95, -1.05, 0])
        self.play(FadeIn(flip, shift=UP * 0.04), run_time=0.7)
        self.wait(1.0)

        warn = txt("这一条最容易错：负数一除，不等号立刻掉头", size=24, color=RED)
        warn.move_to([0, -2.25, 0])
        self.play(FadeIn(warn, shift=UP * 0.04), run_time=0.9)
        self.wait(3.2)
        self.finish_section()

    # ---------------- 3. 解法与数轴 ---------------- 23.7
    def scene_solve(self):
        self.section(3, "解不等式的五步")

        steps = ["去分母", "去括号", "移项", "合并同类项", "系数化为一"]
        x = -5.2
        chips = VGroup()
        for i, s in enumerate(steps):
            chip = txt(f"{i + 1}. {s}", size=23, color=CHALK)
            chips.add(chip)
        chips.arrange(RIGHT, buff=0.38)
        chips.move_to([0, 2.3, 0])
        if chips.width > 12.2:
            chips.scale_to_fit_width(12.2)
        self.play(LaggedStart(*[FadeIn(c, shift=UP * 0.08) for c in chips], lag_ratio=0.1),
                  run_time=1.8)
        self.wait(1.0)

        n1 = txt("前三步和解方程完全一样", size=25, color=DIM).move_to([0, 1.35, 0])
        self.play(FadeIn(n1, shift=UP * 0.04), run_time=0.85)

        n2 = txt("区别只在最后：系数是负数，要变号", size=26, color=GOLD)
        n2.move_to([0, 0.6, 0])
        self.play(FadeIn(n2, shift=UP * 0.04), run_time=0.9)
        self.wait(1.2)

        axis = number_line(-0.55)
        self.play(Create(axis), run_time=0.9)
        for xv, lab in [(-3.6, "−3"), (-0.6, "0"), (3.0, "3")]:
            t = txt(lab, size=22, color=DIM).move_to([xv, -0.95, 0])
            self.play(FadeIn(t), run_time=0.35)

        closed = mark_point(1.2, -0.55, True, GREEN)
        cl = txt("实心：取得到（有等号）", size=23, color=GREEN).move_to([2.2, -1.55, 0])
        self.play(FadeIn(closed), run_time=0.6)
        self.play(FadeIn(cl, shift=UP * 0.04), run_time=0.8)
        self.wait(1.0)

        openp = mark_point(-2.0, -0.55, False, GOLD)
        ol = txt("空心：取不到（无等号）", size=23, color=GOLD).move_to([-2.35, -2.1, 0])
        self.play(FadeIn(openp), run_time=0.6)
        self.play(FadeIn(ol, shift=UP * 0.04), run_time=0.8)
        self.wait(2.6)
        self.finish_section()

    # ---------------- 4. 不等式组与口诀 ---------------- 21.7
    def scene_system(self):
        self.section(4, "不等式组：取公共部分")

        d = txt("几个不等式合在一起，叫一元一次不等式组", size=26, color=CHALK)
        d.move_to([0, 2.3, 0])
        self.play(FadeIn(d, shift=UP * 0.05), run_time=0.95)
        self.wait(0.8)

        rules = [
            ("同大取大", "x > 2 且 x > 5  →  x > 5"),
            ("同小取小", "x < 2 且 x < 5  →  x < 2"),
            ("大小小大中间找", "x > 2 且 x < 5  →  2 < x < 5"),
            ("大大小小无解", "x > 5 且 x < 2  →  无解"),
        ]
        y = 1.55
        for name, ex in rules:
            n = label_box(name, size=22, color=GOLD, pad_x=0.2, pad_y=0.12)
            n.move_to([-3.9, y, 0])
            self.play(FadeIn(n, scale=0.97), run_time=0.55)
            t = txt(ex, size=22, color=CHALK)
            t.next_to(n, RIGHT, buff=0.4)
            t.move_to([t.get_center()[0], n.get_center()[1], 0])
            self.play(FadeIn(t, shift=RIGHT * 0.04), run_time=0.6)
            y -= 0.85
        self.wait(1.0)

        axis = number_line(-2.2, -4.4, 4.2)
        self.play(Create(axis), run_time=0.7)
        seg = Line(P(-0.6, -2.2), P(3.0, -2.2), color=GREEN, stroke_width=7)
        self.play(Create(seg), run_time=0.8)
        p1 = mark_point(-0.6, -2.2, False, GREEN)
        p2 = mark_point(3.0, -2.2, False, GREEN)
        self.play(FadeIn(p1), FadeIn(p2), run_time=0.6)

        lab = txt("2 < x < 5：中间那一段", size=24, color=GREEN).move_to([2.0, -1.62, 0])
        self.play(FadeIn(lab, shift=UP * 0.04), run_time=0.8)
        self.wait(2.8)
        self.finish_section()

    # ---------------- 5. 例题 ---------------- 29.3
    def scene_example(self):
        self.section(5, "例题：解 2(x + 1) > 3x − 4")

        q = txt("解不等式：2(x + 1) > 3x − 4", size=28, color=CHALK)
        q.move_to([0, 2.45, 0])
        self.play(FadeIn(q, shift=UP * 0.05), run_time=0.95)
        self.wait(0.9)

        rows = [
            ("去括号", "2x + 2 > 3x − 4", CHALK),
            ("移项", "2x − 3x > −4 − 2", CHALK),
            ("合并", "−x > −6", CHALK),
            ("系数化为一", "x < 6", GOLD),
        ]
        y = 1.45
        for name, expr, col in rows:
            n = txt(name, size=22, color=DIM)
            n.move_to([-4.6, y, 0])
            self.play(FadeIn(n), run_time=0.45)
            t = txt(expr, size=28, color=col)
            t.next_to(n, RIGHT, buff=0.55)
            t.move_to([t.get_center()[0], n.get_center()[1], 0])
            self.play(FadeIn(t, shift=RIGHT * 0.04), run_time=0.65)
            y -= 0.78
        self.wait(1.2)

        axis = number_line(-1.9, -4.6, 4.6)
        self.play(Create(axis), run_time=0.8)
        dot = mark_point(1.6, -1.9, False, GOLD)
        self.play(FadeIn(dot), run_time=0.55)
        arr = Arrow(P(1.6, -1.9), P(4.15, -1.9), buff=0, color=GOLD, stroke_width=5,
                    max_tip_length_to_length_ratio=0.16)
        self.play(Create(arr), run_time=0.8)
        lab = txt("6", size=23, color=GOLD).move_to([1.6, -1.45, 0])
        self.play(FadeIn(lab), run_time=0.4)

        note = txt("除以 −1，不等号变向：从「大于」变「小于」", size=23, color=RED)
        note.move_to([0, -2.95, 0])
        self.play(FadeIn(note, shift=UP * 0.04), run_time=0.9)
        self.wait(3.4)
        self.finish_section()

    # ---------------- 6. 应用题与易错点 ---------------- 24.9
    def scene_apply(self):
        self.section(6, "应用题：把「最多」翻译成不等号")

        pairs = [
            ("至少", "≥"),
            ("最多、不超过", "≤"),
            ("超过", ">"),
        ]
        y = 2.05
        for word, sym in pairs:
            w = txt(word, size=25, color=CHALK).move_to([-3.9, y, 0])
            self.play(FadeIn(w, shift=RIGHT * 0.04), run_time=0.5)
            s = label_box(sym, size=26, color=GREEN).move_to([-1.7, y, 0])
            self.play(FadeIn(s, scale=0.97), run_time=0.55)
            y -= 0.78
        self.wait(1.2)

        eg = txt("例：8 瓶 48 元，9 瓶 54 元 → 6x ≤ 50", size=25, color=DIM)
        eg.move_to([2.2, 1.25, 0])
        self.play(FadeIn(eg, shift=UP * 0.04), run_time=0.9)
        self.wait(1.0)

        warn = txt("易错：乘除负数不变号　·　实心空心画错　·　解集只写一个数",
                   size=23, color=RED)
        warn.move_to([0, -0.7, 0])
        self.play(FadeIn(warn, shift=UP * 0.04), run_time=1.0)
        self.wait(1.0)

        box = label_box("负数乘除要变号", size=30, color=GOLD)
        box.move_to([0, -2.0, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.1)
        self.wait(4.4)
        self.finish_section()

    def construct(self):
        self.scene_intro()
        self.clear_stage()
        self.scene_def()
        self.clear_stage()
        self.scene_props()
        self.clear_stage()
        self.scene_solve()
        self.clear_stage()
        self.scene_system()
        self.clear_stage()
        self.scene_example()
        self.clear_stage()
        self.scene_apply()
        self.clear_stage(0.8)