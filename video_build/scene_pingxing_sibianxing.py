# -*- coding: utf-8 -*-
"""平行四边形：两组对边分别平行。八年级下。"""

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


def P(x, y):
    return np.array([float(x), float(y), 0.0])


def para(A, B, C, D, color=CHALK, width=3.0, fill=0.06):
    """按顺序 A→B→C→D 画平行四边形。"""
    poly = Polygon(P(*A), P(*B), P(*C), P(*D),
                   color=color, stroke_width=width,
                   fill_color=color, fill_opacity=fill)
    return poly


def vlabel(ch, pos, color=CHALK, size=27):
    t = txt(ch, size=size, color=color)
    t.move_to(P(*pos))
    return t


def mid(a, b):
    return ((a[0] + b[0]) / 2, (a[1] + b[1]) / 2)


class PingxingSibianxingScene(NarratedScene):
    lesson = "pingxing_sibianxing"

    def clear_stage(self, run_time: float = 0.5):
        keep = {id(self._track), id(self._fill)}
        junk = [m for m in self.mobjects if id(m) not in keep]
        if junk:
            self.play(*[FadeOut(m) for m in junk], run_time=run_time)
        self.cur_title = None
        self.cur_sub = None

    # ---------------- 0. 生活中的平行四边形 ---------------- 23.5
    def scene_intro(self):
        self.section(0, "两组对边分别平行")

        A, B, C, D = (-4.4, -1.5), (2.4, -1.5), (4.0, 1.5), (-2.8, 1.5)
        shape = para(A, B, C, D, GOLD)
        self.play(Create(shape), run_time=1.2)
        self.wait(0.6)

        ab = Line(P(*A), P(*B), color=GREEN, stroke_width=6)
        cd = Line(P(*D), P(*C), color=GREEN, stroke_width=6)
        self.play(Create(ab), run_time=0.7)
        self.play(Create(cd), run_time=0.7)

        ad = Line(P(*A), P(*D), color=BLUE, stroke_width=6)
        bc = Line(P(*B), P(*C), color=BLUE, stroke_width=6)
        self.play(Create(ad), run_time=0.7)
        self.play(Create(bc), run_time=0.7)
        self.wait(1.0)

        l1 = txt("绿：上下一组对边平行", size=24, color=GREEN).move_to([-2.6, 2.55, 0])
        l2 = txt("蓝：左右一组对边平行", size=24, color=BLUE).move_to([2.9, 2.55, 0])
        self.play(FadeIn(l1, shift=UP * 0.04), FadeIn(l2, shift=UP * 0.04), run_time=0.95)
        self.wait(1.2)

        names = [vlabel("A", (-5.05, -1.75)), vlabel("B", (2.7, -1.75)),
                 vlabel("C", (4.45, 1.7)), vlabel("D", (-3.15, 1.7))]
        self.play(LaggedStart(*[FadeIn(n, scale=0.9) for n in names], lag_ratio=0.15),
                  run_time=1.6)
        self.wait(0.8)

        box = label_box("两组对边分别平行的四边形，叫平行四边形", size=26, color=GOLD)
        box.move_to([0, -2.6, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.1)
        self.wait(3.4)
        self.finish_section()

    # ---------------- 1. 四条性质 ---------------- 24.6
    def scene_props(self):
        self.section(1, "平行四边形的四条性质")

        A, B, C, D = (-5.2, -1.3), (-1.6, -1.3), (-0.4, 1.3), (-4.0, 1.3)
        shape = para(A, B, C, D, CHALK, width=2.8)
        self.play(Create(shape), run_time=1.0)

        O = mid(A, C)
        diag1 = Line(P(*A), P(*C), color=GOLD, stroke_width=2.4)
        diag2 = Line(P(*B), P(*D), color=GOLD, stroke_width=2.4)
        dot = Dot(P(*O), radius=0.07, color=GOLD)
        self.play(Create(diag1), Create(diag2), FadeIn(dot), run_time=1.4)
        lab = txt("O", size=22, color=GOLD).move_to(P(O[0] + 0.3, O[1] - 0.42))
        self.play(FadeIn(lab), run_time=0.5)
        self.wait(1.0)

        rows = [
            ("① 对边平行且相等", CHALK),
            ("② 对角相等", CHALK),
            ("③ 邻角互补：和 180°", CHALK),
            ("④ 对角线互相平分", GOLD),
        ]
        y = 2.05
        for s, col in rows:
            t = txt(s, size=24, color=col).move_to([3.35, y, 0])
            self.play(FadeIn(t, shift=RIGHT * 0.04), run_time=0.7)
            y -= 0.85
        self.wait(1.0)

        note = txt("前三条看边和角，最后一条看对角线", size=23, color=DIM)
        note.move_to([0, -2.25, 0])
        self.play(FadeIn(note, shift=UP * 0.04), run_time=0.9)
        self.wait(3.4)
        self.finish_section()

    # ---------------- 2. 四种判定 ---------------- 27.7
    def scene_rules(self):
        self.section(2, "怎么判断它是平行四边形")

        head = txt("常用判定方法", size=26, color=GOLD).move_to([0, 2.4, 0])
        self.play(FadeIn(head, shift=UP * 0.05), run_time=0.85)
        self.wait(0.6)

        rows = [
            ("①", "两组对边分别平行"),
            ("②", "两组对边分别相等"),
            ("③", "一组对边平行且相等"),
            ("④", "对角线互相平分"),
            ("⑤", "两组对角分别相等"),
        ]
        y = 1.65
        for num, s in rows:
            n = txt(num, size=23, color=GOLD).move_to([-5.7, y, 0])
            t = txt(s, size=25, color=CHALK)
            t.next_to(n, RIGHT, buff=0.3)
            t.move_to([t.get_center()[0], n.get_center()[1], 0])
            self.play(FadeIn(n, shift=RIGHT * 0.05), run_time=0.4)
            self.play(FadeIn(t, shift=RIGHT * 0.04), run_time=0.55)
            y -= 0.78
        self.wait(1.2)

        warn = label_box("「一组对边平行、另一组对边相等」不够", size=25, color=RED)
        warn.move_to([0, -2.05, 0])
        self.play(FadeIn(warn, scale=0.97), run_time=1.0)

        eg = txt("等腰梯形就满足，却不是平行四边形", size=23, color=RED)
        eg.move_to([0, -2.75, 0])
        self.play(FadeIn(eg, shift=UP * 0.04), run_time=0.9)
        self.wait(3.6)
        self.finish_section()

    # ---------------- 3. 面积 ---------------- 19.4
    def scene_area(self):
        self.section(3, "面积：底乘高")

        A, B, C, D = (-3.6, -1.5), (2.4, -1.5), (3.6, 1.3), (-2.4, 1.3)
        shape = para(A, B, C, D, CHALK)
        self.play(Create(shape), run_time=1.0)
        self.wait(0.5)

        base = Line(P(*A), P(*B), color=GREEN, stroke_width=6)
        self.play(Create(base), run_time=0.7)
        bl = txt("底", size=23, color=GREEN).move_to([-0.6, -1.95, 0])
        self.play(FadeIn(bl), run_time=0.5)

        hx = -2.4
        h = DashedLine(P(hx, -1.5), P(hx, 1.3), color=GOLD, stroke_width=2.6)
        self.play(Create(h), run_time=0.9)
        hl = txt("高", size=23, color=GOLD).move_to([hx - 0.5, -0.1, 0])
        self.play(FadeIn(hl), run_time=0.5)
        right = RightAngle(Line(P(hx, -1.5), P(hx, 0.0)),
                           Line(P(hx, -1.5), P(hx - 1.0, -1.5)),
                           length=0.22, color=GOLD)
        self.play(Create(right), run_time=0.6)
        self.wait(1.0)

        f = txt("S = 底 × 高", size=34, color=GOLD).move_to([3.6, 1.4, 0])
        self.play(FadeIn(f, scale=0.97), run_time=0.95)
        w = txt("高是对边的垂直距离", size=24, color=RED).move_to([3.6, 0.4, 0])
        self.play(FadeIn(w, shift=UP * 0.04), run_time=0.85)
        w2 = txt("不是斜边", size=24, color=RED).move_to([3.6, -0.3, 0])
        self.play(FadeIn(w2, shift=UP * 0.04), run_time=0.7)
        self.wait(1.0)

        note = txt("换一条底，对应的高也换，底乘高不变", size=23, color=DIM)
        note.move_to([0, -2.85, 0])
        self.play(FadeIn(note, shift=UP * 0.04), run_time=0.9)
        self.wait(2.8)
        self.finish_section()

    # ---------------- 4. 例题：求角 ---------------- 19.0
    def scene_angles(self):
        self.section(4, "例题：一个角是 60°")

        A = (-4.6, -2.0)
        B = (-0.6, -2.0)
        C = (0.965, 0.71)
        D = (-3.035, 0.71)
        shape = para(A, B, C, D, CHALK)
        self.play(Create(shape), run_time=1.0)

        names = [vlabel("A", (-5.05, -2.25)), vlabel("B", (-0.25, -2.25)),
                 vlabel("C", (1.2, 0.95)), vlabel("D", (-3.35, 0.95))]
        self.play(LaggedStart(*[FadeIn(n, scale=0.9) for n in names], lag_ratio=0.12),
                  run_time=1.3)

        a60 = txt("60°", size=25, color=GOLD).move_to([-3.85, -1.55, 0])
        self.play(FadeIn(a60, scale=0.9), run_time=0.7)
        self.wait(1.0)

        q = txt("∠A = 60°，求 ∠B、∠C、∠D", size=26, color=CHALK)
        q.move_to([3.5, 2.2, 0])
        self.play(FadeIn(q, shift=UP * 0.05), run_time=0.9)
        self.wait(0.6)

        r1 = txt("∠C = ∠A = 60°（对角相等）", size=24, color=GREEN).move_to([3.5, 1.35, 0])
        self.play(FadeIn(r1, shift=UP * 0.04), run_time=0.85)
        r2 = txt("∠B = 180° − 60° = 120°", size=24, color=GREEN).move_to([3.5, 0.5, 0])
        self.play(FadeIn(r2, shift=UP * 0.04), run_time=0.9)
        r3 = txt("∠D = ∠B = 120°", size=24, color=GREEN).move_to([3.5, -0.35, 0])
        self.play(FadeIn(r3, shift=UP * 0.04), run_time=0.85)
        self.wait(1.0)

        b120 = txt("120°", size=23, color=BLUE).move_to([-0.85, -1.5, 0])
        d120 = txt("120°", size=23, color=BLUE).move_to([-2.5, 0.2, 0])
        self.play(FadeIn(b120), FadeIn(d120), run_time=0.8)

        note = txt("四个角的和：60 + 120 + 60 + 120 = 360°", size=23, color=DIM)
        note.move_to([0, -2.75, 0])
        self.play(FadeIn(note, shift=UP * 0.04), run_time=0.9)
        self.wait(2.6)
        self.finish_section()

    # ---------------- 5. 例题：周长与对角线 ---------------- 22.1
    def scene_sides(self):
        self.section(5, "例题：周长与对角线")

        q = txt("AB = 5，BC = 8，求周长", size=27, color=CHALK).move_to([0, 2.35, 0])
        self.play(FadeIn(q, shift=UP * 0.05), run_time=0.95)
        self.wait(0.7)

        s1 = txt("CD = AB = 5", size=26, color=GREEN).move_to([-3.2, 1.35, 0])
        self.play(FadeIn(s1, shift=UP * 0.04), run_time=0.8)
        s2 = txt("AD = BC = 8", size=26, color=GREEN).move_to([3.2, 1.35, 0])
        self.play(FadeIn(s2, shift=UP * 0.04), run_time=0.8)
        self.wait(0.8)

        s3 = txt("周长 = 2×5 + 2×8 = 26", size=30, color=GOLD).move_to([0, 0.3, 0])
        self.play(FadeIn(s3, shift=UP * 0.04), run_time=0.95)
        self.wait(1.2)

        sep = Line([-4.6, -0.35, 0], [4.6, -0.35, 0], color=DIM, stroke_width=1.2)
        sep.set_opacity(0.35)
        self.play(Create(sep), run_time=0.6)

        q2 = txt("若对角线 AC = 10，求 OA", size=26, color=CHALK).move_to([0, -1.05, 0])
        self.play(FadeIn(q2, shift=UP * 0.04), run_time=0.9)
        r2 = txt("O 是 AC 中点 → OA = 10 ÷ 2 = 5", size=27, color=GREEN).move_to([0, -1.85, 0])
        self.play(FadeIn(r2, shift=UP * 0.04), run_time=0.95)
        self.wait(0.8)

        note = txt("对角线互相平分：OA = OC，OB = OD", size=24, color=DIM)
        note.move_to([0, -2.65, 0])
        self.play(FadeIn(note, shift=UP * 0.04), run_time=0.9)
        self.wait(2.8)
        self.finish_section()

    # ---------------- 6. 易错点 ---------------- 24.7
    def scene_traps(self):
        self.section(6, "三个易错点")

        rows = [
            ("① 面积用底乘高", "斜边不是高"),
            ("② 一组对边平行 + 另一组相等", "等腰梯形是反例"),
            ("③ 对角线相等不是判定", "那是矩形的性质"),
        ]
        y = 1.95
        for a, b in rows:
            ta = txt(a, size=25, color=RED).move_to([-3.0, y, 0])
            self.play(FadeIn(ta, shift=RIGHT * 0.04), run_time=0.7)
            tb = txt(b, size=23, color=DIM).move_to([3.9, y, 0])
            self.play(FadeIn(tb, shift=RIGHT * 0.04), run_time=0.7)
            y -= 0.95
        self.wait(1.2)

        note = txt("四边形 → 先找平行，再用判定", size=25, color=CHALK)
        note.move_to([0, -1.2, 0])
        self.play(FadeIn(note, shift=UP * 0.04), run_time=0.9)
        self.wait(0.8)

        box = label_box("对角线互相平分", size=30, color=GOLD)
        box.move_to([0, -2.35, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.1)
        self.wait(4.4)
        self.finish_section()

    def construct(self):
        self.scene_intro()
        self.clear_stage()
        self.scene_props()
        self.clear_stage()
        self.scene_rules()
        self.clear_stage()
        self.scene_area()
        self.clear_stage()
        self.scene_angles()
        self.clear_stage()
        self.scene_sides()
        self.clear_stage()
        self.scene_traps()
        self.clear_stage(0.8)