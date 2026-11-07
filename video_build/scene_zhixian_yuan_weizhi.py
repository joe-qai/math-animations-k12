# -*- coding: utf-8 -*-
"""直线与圆的位置关系：相离、相切、相交，切线判定与性质，切线长定理，内切圆。九年级上。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


def P(x, y):
    return np.array([float(x), float(y), 0.0])


def pt(cx: float, cy: float, r: float, deg: float):
    a = deg * np.pi / 180.0
    return P(cx + r * np.cos(a), cy + r * np.sin(a))


def circ(cx: float, cy: float, r: float, color=CHALK, width: float = 2.8) -> Circle:
    return Circle(radius=r, color=color, stroke_width=width).move_to([cx, cy, 0])


def right_mark(vertex, d1, d2, size: float = 0.2, color=CHALK) -> Mobject:
    return Polygon(vertex + d1 * size, vertex + d1 * size + d2 * size,
                   vertex + d2 * size, color=color, stroke_width=2.0)


def tick(mid, d, size: float = 0.13, color=GOLD) -> Line:
    """在线段中点处画等长刻度（d 为线段方向的单位向量）。"""
    n = np.array([-d[1], d[0], 0.0])
    return Line(mid + n * size, mid - n * size, color=color, stroke_width=2.6)


class ZhixianYuanWeizhiScene(NarratedScene):
    lesson = "zhixian-yuan-weizhi"

    def clear_stage(self, run_time: float = 0.5):
        keep = {id(self._track), id(self._fill)}
        junk = [m for m in self.mobjects if id(m) not in keep]
        if junk:
            self.play(*[FadeOut(m) for m in junk], run_time=run_time)
        self.cur_title = None
        self.cur_sub = None

    # ---------------- 0. 三种位置关系 ---------------- 27.1
    def scene_intro(self):
        self.section(0, "一条直线和一个圆")

        cols = [
            ("相离", "没有公共点", 1.55, DIM, -4.7),
            ("相切", "只有一个公共点", 1.0, GOLD, 0.0),
            ("相交", "两个公共点", 0.45, GREEN, 4.7),
        ]
        for name, note, dist, col, cx in cols:
            c = circ(cx, 0.95, 1.0, CHALK, 2.4)
            ln = Line(P(cx - 2.15, 0.95 - dist), P(cx + 2.15, 0.95 - dist),
                      color=col, stroke_width=3.0)
            self.play(Create(c), run_time=0.7)
            self.play(Create(ln), run_time=0.6)
            t = txt(name, size=28, color=col).move_to([cx, -1.05, 0])
            n = txt(note, size=21, color=DIM).move_to([cx, -1.62, 0])
            self.play(FadeIn(t, shift=UP * 0.04), run_time=0.6)
            self.play(FadeIn(n, shift=UP * 0.04), run_time=0.5)
            self.wait(0.4)

        box = label_box("判断只看圆心到直线的距离 d 与半径 r", size=23, color=GOLD)
        box.move_to([0, -2.6, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.0)
        self.wait(12.5)
        self.finish_section()

    # ---------------- 1. d 与 r 比较 ---------------- 25.1
    def scene_compare(self):
        self.section(1, "比较 d 与 r")

        cx, cy, r = -3.4, 0.55, 1.65
        c = circ(cx, cy, r, CHALK, 2.6)
        tang = Line(P(cx - 2.6, cy + r), P(cx + 2.6, cy + r), color=GOLD, stroke_width=3.0)
        self.play(Create(c), run_time=1.0)
        self.play(Create(tang), run_time=0.8)

        dline = DashedLine(P(cx, cy), P(cx, cy + r), color=GREEN, stroke_width=2.2, dash_length=0.12)
        rline = DashedLine(P(cx, cy), pt(cx, cy, r, 32), color=BLUE, stroke_width=2.2, dash_length=0.12)
        self.play(Create(dline), run_time=0.8)
        self.play(Create(rline), run_time=0.8)

        ld = txt("d", size=24, color=GREEN).move_to([cx + 0.3, cy + 0.95, 0])
        lr = txt("r", size=24, color=BLUE).move_to([cx + 1.05, cy + 0.72, 0])
        rm = right_mark(P(cx, cy + r), DOWN, RIGHT, 0.18, CHALK)
        self.play(FadeIn(ld), FadeIn(lr), Create(rm), run_time=0.9)
        self.wait(0.8)

        rows = [
            ("d > r", "相离：没有公共点", DIM),
            ("d = r", "相切：只有一个公共点", GOLD),
            ("d < r", "相交：两个公共点", GREEN),
        ]
        y = 1.85
        for a, b, col in rows:
            ta = txt(a, size=30, color=col).move_to([1.55, y, 0])
            tb = txt(b, size=24, color=CHALK).move_to([4.5, y, 0])
            self.play(FadeIn(ta, shift=RIGHT * 0.04), run_time=0.7)
            self.play(FadeIn(tb, shift=RIGHT * 0.04), run_time=0.6)
            y -= 1.05
        self.wait(0.9)

        note = txt("反过来，位置关系也能推出 d 与 r 的大小关系", size=23, color=RED)
        note.move_to([2.9, -1.55, 0])
        self.play(FadeIn(note, shift=UP * 0.04), run_time=0.95)
        self.wait(9.5)
        self.finish_section()

    # ---------------- 2. 切线的判定 ---------------- 28.6
    def scene_judge(self):
        self.section(2, "切线的判定")

        cx, cy, r = -3.2, 0.5, 1.7
        c = circ(cx, cy, r, CHALK, 2.6)
        a = pt(cx, cy, r, 90)
        oa = Line(P(cx, cy), a, color=GREEN, stroke_width=2.8)
        tang = Line(P(cx - 1.9, a[1]), P(cx + 1.9, a[1]), color=GOLD, stroke_width=3.2)
        self.play(Create(c), run_time=1.0)
        self.play(Create(oa), run_time=0.8)
        self.play(Create(tang), run_time=1.0)

        rm = right_mark(a, DOWN, RIGHT, 0.2, GOLD)
        dot = Dot(a, radius=0.065, color=GOLD)
        la = txt("A", size=22, color=GOLD).move_to(a + RIGHT * 0.36 + UP * 0.32)
        self.play(Create(rm), FadeIn(dot), FadeIn(la), run_time=0.8)
        self.wait(0.7)

        th1 = txt("经过半径外端", size=25, color=GOLD).move_to([2.75, 2.35, 0])
        th2 = txt("且垂直于半径的直线，是切线", size=23, color=GOLD).move_to([2.75, 1.72, 0])
        self.play(FadeIn(th1, shift=UP * 0.04), run_time=0.85)
        self.play(FadeIn(th2, shift=UP * 0.04), run_time=0.85)
        self.wait(0.6)

        rows = [
            ("已经有公共点：连半径，证垂直", GREEN),
            ("没有公共点：作垂线，证 d = r", BLUE),
        ]
        y = 0.62
        for s, col in rows:
            t = txt(s, size=24, color=col).move_to([2.9, y, 0])
            self.play(FadeIn(t, shift=RIGHT * 0.04), run_time=0.9)
            y -= 0.9
        self.wait(0.9)

        note = txt("两个条件缺一不可：点在圆上，且垂直", size=23, color=RED)
        note.move_to([2.9, -1.6, 0])
        self.play(FadeIn(note, shift=UP * 0.04), run_time=0.95)
        self.wait(11.0)
        self.finish_section()

    # ---------------- 3. 切线的性质 ---------------- 20.4
    def scene_property(self):
        self.section(3, "切线的性质")

        cx, cy, r = -2.9, 0.35, 1.75
        c = circ(cx, cy, r, CHALK, 2.6)
        a = pt(cx, cy, r, 62)
        oa = Line(P(cx, cy), a, color=GREEN, stroke_width=2.9)
        u = (a - P(cx, cy))
        u = u / np.linalg.norm(u)
        n = np.array([-u[1], u[0], 0.0])
        tang = Line(a - n * 2.2, a + n * 2.2, color=GOLD, stroke_width=3.2)
        self.play(Create(c), run_time=1.0)
        self.play(Create(oa), run_time=0.8)
        self.play(Create(tang), run_time=1.0)

        rm = right_mark(a, -u, n, 0.22, GOLD)
        la = txt("A", size=22, color=GOLD).move_to(a + u * 0.28)
        self.play(Create(rm), FadeIn(la), run_time=0.8)
        self.wait(0.8)

        f = txt("切线 ⊥ 过切点的半径", size=32, color=GOLD).move_to([3.0, 1.5, 0])
        self.play(FadeIn(f, scale=0.98), run_time=1.0)
        self.wait(0.6)

        note = txt("题目里出现切线，先连切点与圆心", size=24, color=CHALK)
        note.move_to([3.0, 0.5, 0])
        self.play(FadeIn(note, shift=UP * 0.04), run_time=0.9)
        self.wait(0.7)

        box = label_box("见切线，连半径，得直角", size=26, color=GREEN)
        box.move_to([3.0, -1.35, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.0)
        self.wait(7.0)
        self.finish_section()

    # ---------------- 4. 切线长定理 ---------------- 23.0
    def scene_lengths(self):
        self.section(4, "切线长定理")

        cx, cy, r = -2.6, 0.25, 1.5
        c = circ(cx, cy, r, CHALK, 2.6)
        self.play(Create(c), run_time=1.0)

        ox, oy = cx - 3.2, cy
        pa_ = pt(cx, cy, r, 145)
        pb_ = pt(cx, cy, r, 215)
        self.play(FadeIn(Dot(P(ox, oy), radius=0.07, color=GOLD)), run_time=0.5)

        la = Line(P(ox, oy), pa_, color=GOLD, stroke_width=2.8)
        lb = Line(P(ox, oy), pb_, color=GOLD, stroke_width=2.8)
        oa = Line(P(cx, cy), pa_, color=GREEN, stroke_width=2.4)
        ob = Line(P(cx, cy), pb_, color=GREEN, stroke_width=2.4)
        self.play(Create(la), Create(lb), run_time=1.2)
        self.play(Create(oa), Create(ob), run_time=1.0)

        ta = txt("A", size=22, color=GOLD).move_to(pa_ + UP * 0.26)
        tb = txt("B", size=22, color=GOLD).move_to(pb_ + DOWN * 0.26)
        tp = txt("P", size=22, color=GOLD).move_to(P(ox, oy) + LEFT * 0.26)
        self.play(FadeIn(ta), FadeIn(tb), FadeIn(tp), run_time=0.7)

        mid_a = (P(ox, oy) + pa_) / 2
        mid_b = (P(ox, oy) + pb_) / 2
        ua = (pa_ - P(ox, oy))
        ua = ua / np.linalg.norm(ua)
        ub = (pb_ - P(ox, oy))
        ub = ub / np.linalg.norm(ub)
        self.play(Create(tick(mid_a, ua)), Create(tick(mid_b, ub)), run_time=0.8)
        self.wait(0.8)

        l1 = txt("PA = PB：切线长相等", size=26, color=GOLD).move_to([3.1, 1.45, 0])
        l2 = txt("OP 平分 ∠APB", size=26, color=GREEN).move_to([3.1, 0.6, 0])
        self.play(FadeIn(l1, shift=UP * 0.04), run_time=0.85)
        self.play(FadeIn(l2, shift=UP * 0.04), run_time=0.85)
        self.wait(0.8)

        note = txt("连两条半径，得到两个全等直角三角形", size=23, color=CHALK)
        note.move_to([3.1, -0.85, 0])
        self.play(FadeIn(note, shift=UP * 0.04), run_time=0.9)

        box = label_box("从圆外一点引两条切线，长度相等", size=22, color=GOLD)
        box.move_to([3.1, -1.95, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.0)
        self.wait(8.5)
        self.finish_section()

    # ---------------- 5. 三角形内切圆 ---------------- 22.3
    def scene_incircle(self):
        self.section(5, "三角形的内切圆")

        B = P(-5.5, -1.25)
        C = P(-1.7, -1.25)
        A = P(-5.5, 1.6)
        tri = Polygon(A, B, C, color=CHALK, stroke_width=2.8)
        self.play(Create(tri), run_time=1.2)
        self.play(Create(right_mark(B, UP, RIGHT, 0.2, DIM)), run_time=0.6)

        # 直角三角形：两直角边 3 : 4，斜边 5，整体缩放 m
        m = 0.95
        rr = m
        ix, iy = B[0] + rr, B[1] + rr
        inc = circ(ix, iy, rr, GOLD, 2.6)
        self.play(Create(inc), run_time=1.1)
        self.play(FadeIn(Dot(P(ix, iy), radius=0.06, color=GOLD)), run_time=0.5)

        ti = txt("I", size=22, color=GOLD).move_to([ix - 0.26, iy + 0.2, 0])
        self.play(FadeIn(ti), run_time=0.5)

        # 到三边的垂线
        f1 = P(ix, B[1])
        f2 = P(B[0], iy)
        f3 = _foot(A, C, P(ix, iy))
        d1 = Line(P(ix, iy), f1, color=GREEN, stroke_width=2.2)
        d2 = Line(P(ix, iy), f2, color=GREEN, stroke_width=2.2)
        d3 = Line(P(ix, iy), f3, color=GREEN, stroke_width=2.2)
        self.play(Create(d1), Create(d2), Create(d3), run_time=1.2)

        u_ac = (C - A)
        u_ac = u_ac / np.linalg.norm(u_ac)
        v_r = (f3 - P(ix, iy))
        v_r = v_r / np.linalg.norm(v_r)
        self.play(Create(right_mark(f1, UP, RIGHT, 0.16, GREEN)),
                  Create(right_mark(f2, RIGHT, UP, 0.16, GREEN)),
                  Create(right_mark(f3, u_ac, v_r, 0.16, GREEN)), run_time=0.9)

        lr = txt("r", size=22, color=GREEN).move_to([ix + 0.26, iy - 0.42, 0])
        self.play(FadeIn(lr), run_time=0.5)
        self.wait(0.8)

        rows = [
            ("内心 I：三条角平分线的交点", GOLD),
            ("到三边距离相等，都等于 r", GREEN),
            ("直角三角形：r = (a + b − c) / 2", BLUE),
        ]
        y = 1.75
        for s, col in rows:
            t = txt(s, size=24, color=col).move_to([2.85, y, 0])
            self.play(FadeIn(t, shift=RIGHT * 0.04), run_time=0.9)
            y -= 0.95
        self.wait(0.9)

        note = txt("内心在内，外心可能在外", size=23, color=RED)
        note.move_to([2.85, -1.75, 0])
        self.play(FadeIn(note, shift=UP * 0.04), run_time=0.95)
        self.wait(8.0)
        self.finish_section()

    # ---------------- 6. 四个易错点 ---------------- 30.4
    def scene_traps(self):
        self.section(6, "四个易错点")

        rows = [
            ("① 判定切线只证垂直", "忘了说明点在圆上"),
            ("② 用切线性质没连半径", "直角找不出来"),
            ("③ 切线长定理和切割线定理混", "一个是长度相等，一个是乘积"),
            ("④ 内心和外心搞反", "内心角平分线，外心垂直平分线"),
        ]
        y = 1.85
        for a, b in rows:
            ta = txt(a, size=23, color=RED).move_to([-2.6, y, 0])
            tb = txt(b, size=21, color=DIM).move_to([3.65, y, 0])
            self.play(FadeIn(ta, shift=RIGHT * 0.04), run_time=0.65)
            self.play(FadeIn(tb, shift=RIGHT * 0.04), run_time=0.65)
            y -= 0.86
        self.wait(1.0)

        box = label_box("比 d 和 r，连切点半径，看切线长相等", size=23, color=GOLD)
        box.move_to([0, -2.45, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.1)
        self.wait(13.0)
        self.finish_section()

    def construct(self):
        self.scene_intro()
        self.clear_stage()
        self.scene_compare()
        self.clear_stage()
        self.scene_judge()
        self.clear_stage()
        self.scene_property()
        self.clear_stage()
        self.scene_lengths()
        self.clear_stage()
        self.scene_incircle()
        self.clear_stage()
        self.scene_traps()
        self.clear_stage(0.8)


def _foot(a, b, p):
    """点 p 到直线 ab 的垂足。"""
    ab = b - a
    t = np.dot(p - a, ab) / np.dot(ab, ab)
    return a + ab * t