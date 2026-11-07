# -*- coding: utf-8 -*-
"""轴对称与等腰三角形：对折能重合，三线合一是核心。八年级。"""

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


def P(x, y):
    return np.array([float(x), float(y), 0.0])


def tri(a, b, c, color=CHALK, fill=0.0, width=3.0):
    t = Polygon(P(*a), P(*b), P(*c), color=color, stroke_width=width)
    if fill:
        t.set_fill(color, opacity=fill)
    return t


def right_angle(v, p1, p2, size=0.34, color=CHALK):
    a1 = math.atan2(p1[1] - v[1], p1[0] - v[0])
    a2 = math.atan2(p2[1] - v[1], p2[0] - v[0])
    u1 = np.array([math.cos(a1), math.sin(a1), 0]) * size
    u2 = np.array([math.cos(a2), math.sin(a2), 0]) * size
    o = P(*v)
    return Polygon(o + u1, o + u1 + u2, o + u2,
                   color=color, stroke_width=2.4, fill_color=color, fill_opacity=0.12)


def ang_arc(v, p1, p2, radius=0.55, color=CHALK, width=2.4):
    a1 = math.atan2(p1[1] - v[1], p1[0] - v[0])
    a2 = math.atan2(p2[1] - v[1], p2[0] - v[0])
    d = a2 - a1
    while d > math.pi:
        d -= 2 * math.pi
    while d < -math.pi:
        d += 2 * math.pi
    return Arc(radius=radius, start_angle=a1, angle=d, arc_center=P(*v),
               color=color, stroke_width=width)


def tick(p, q, n=1, color=CHALK, size=0.17, gap=0.22, width=2.6, t=0.5):
    p, q = P(*p), P(*q)
    mid = p + (q - p) * t
    d = q - p
    d = d / np.linalg.norm(d)
    nv = np.array([-d[1], d[0], 0])
    grp = VGroup()
    for k in range(n):
        c = mid + d * ((k - (n - 1) / 2) * gap)
        grp.add(Line(c - nv * size, c + nv * size, color=color, stroke_width=width))
    return grp


def cross_out(mob, color=RED, pad=0.10):
    l = mob.get_left()[0] - pad
    r = mob.get_right()[0] + pad
    b = mob.get_bottom()[1] - pad
    t = mob.get_top()[1] + pad
    return VGroup(
        Line([l, b, 0], [r, t, 0], color=color, stroke_width=2.4),
        Line([l, t, 0], [r, b, 0], color=color, stroke_width=2.4),
    )


class DuichengDengyaoScene(NarratedScene):
    lesson = "duicheng_dengyao"

    def clear_stage(self, run_time: float = 0.5):
        keep = {id(self._track), id(self._fill)}
        junk = [m for m in self.mobjects if id(m) not in keep]
        if junk:
            self.play(*[FadeOut(m) for m in junk], run_time=run_time)
        self.cur_title = None
        self.cur_sub = None

    # ---------------- 0. 对折能重合 ---------------- 30.7
    def scene_intro(self):
        self.section(0, "对折，两边能重合")

        axis = DashedLine([0, -2.7, 0], [0, 2.7, 0], color=DIM, stroke_width=2.2)
        self.play(Create(axis), run_time=1.0)

        half = Polygon(P(0, 1.85), P(-1.75, 0.05), P(0, -1.9),
                       color=GOLD, stroke_width=3, fill_color=GOLD, fill_opacity=0.14)
        self.play(Create(half), run_time=1.2)
        self.wait(1.0)

        right = half.copy()
        right.rotate(math.pi, axis=UP, about_point=ORIGIN)
        self.play(FadeIn(right, shift=RIGHT * 0.12), run_time=1.4)
        self.wait(1.2)

        shape = Polygon(P(0, 1.85), P(-1.75, 0.05), P(0, -1.9),
                        P(1.75, 0.05), color=GREEN, stroke_width=3)
        self.play(Create(shape), run_time=1.3)

        n1 = txt("沿一条直线对折", size=28, color=CHALK).move_to([3.35, 1.95, 0])
        self.play(FadeIn(n1, shift=UP * 0.05), run_time=0.8)

        n2 = txt("两边完全重合", size=30, color=GREEN).move_to([3.35, 1.05, 0])
        self.play(FadeIn(n2, shift=UP * 0.05), run_time=0.9)
        self.wait(1.0)

        n3 = txt("轴对称图形", size=36, color=GOLD).move_to([3.35, 0.0, 0])
        self.play(FadeIn(n3, scale=0.96), run_time=1.0)

        n4 = txt("这条直线叫对称轴", size=27, color=CHALK).move_to([3.35, -1.0, 0])
        self.play(FadeIn(n4, shift=UP * 0.05), run_time=0.8)
        self.wait(1.2)

        n5 = txt("对称轴是直线，不是线段", size=26, color=RED).move_to([0, -2.9, 0])
        self.play(FadeIn(n5, shift=UP * 0.05), run_time=0.9)
        self.wait(2.4)
        self.finish_section()

    # ---------------- 1. 性质：垂直平分 ---------------- 29.6
    def scene_property(self):
        self.section(1, "对称轴垂直平分对应点的连线")

        axis = DashedLine([-3.4, -2.85, 0], [-3.4, 2.85, 0], color=DIM, stroke_width=2.2)
        self.play(Create(axis), run_time=0.9)

        A, A2 = (-5.4, 1.55), (-1.4, 1.55)
        seg = Line(P(*A), P(*A2), color=BLUE, stroke_width=3)
        self.play(Create(seg), run_time=1.0)

        dA = Dot(P(*A), radius=0.09, color=CHALK)
        dB = Dot(P(*A2), radius=0.09, color=CHALK)
        M = Dot([-3.4, 1.55, 0], radius=0.09, color=GOLD)
        self.play(FadeIn(dA), FadeIn(dB), FadeIn(M), run_time=0.7)

        lA = txt("A", size=26, color=CHALK).move_to([-5.65, 1.92, 0])
        lB = txt("A′", size=26, color=CHALK).move_to([-1.15, 1.92, 0])
        lM = txt("M", size=25, color=GOLD).move_to([-3.8, 1.95, 0])
        self.play(FadeIn(lA), FadeIn(lB), FadeIn(lM), run_time=0.8)
        self.wait(0.8)

        ra = right_angle((-3.4, 1.55), (-5.4, 1.55), (-3.4, 0.65), size=0.3, color=GOLD)
        self.play(Create(ra), run_time=0.6)
        self.wait(1.0)

        P2 = (-3.4, -0.85)
        pdot = Dot(P(*P2), radius=0.10, color=GREEN)
        pa = Line(P(*P2), P(*A), color=GREEN, stroke_width=2.6)
        pb = Line(P(*P2), P(*A2), color=GREEN, stroke_width=2.6)
        self.play(FadeIn(pdot), run_time=0.4)
        self.play(Create(pa), Create(pb), run_time=1.2)
        lp = txt("P", size=25, color=GREEN).move_to([-3.9, -0.8, 0])
        self.play(FadeIn(lp), run_time=0.5)
        self.wait(1.2)

        n1 = txt("对称轴垂直平分", size=27, color=GOLD).move_to([3.2, 2.15, 0])
        n2 = txt("对应点的连线", size=27, color=GOLD).move_to([3.2, 1.45, 0])
        self.play(FadeIn(n1, shift=UP * 0.05), run_time=0.8)
        self.play(FadeIn(n2, shift=UP * 0.05), run_time=0.7)
        self.wait(1.2)

        n3 = txt("对应线段相等", size=26, color=CHALK).move_to([3.2, 0.45, 0])
        n4 = txt("对应角相等", size=26, color=CHALK).move_to([3.2, -0.2, 0])
        self.play(FadeIn(n3, shift=UP * 0.05), run_time=0.8)
        self.play(FadeIn(n4, shift=UP * 0.05), run_time=0.8)
        self.wait(1.0)

        n5 = txt("垂直平分线上的点", size=26, color=GREEN).move_to([3.2, -1.3, 0])
        n6 = txt("到两端距离相等：PA = PA′", size=26, color=GREEN).move_to([3.2, -2.05, 0])
        self.play(FadeIn(n5, shift=UP * 0.05), run_time=0.8)
        self.play(FadeIn(n6, shift=UP * 0.05), run_time=0.9)
        self.wait(3.0)
        self.finish_section()

    # ---------------- 2. 画法三步 + 坐标 ---------------- 33.5
    def scene_draw(self):
        self.section(2, "画对称图形：三步")

        items = [
            ("①", "找出图形的关键点", GOLD),
            ("②", "向对称轴作垂线，取等长", CHALK),
            ("③", "把对称点顺次连起来", CHALK),
        ]
        y = 2.05
        for num, s, col in items:
            n = txt(num, size=27, color=GOLD).move_to([-5.6, y, 0])
            t = txt(s, size=26, color=col).move_to([-2.65, y, 0])
            self.play(FadeIn(n, shift=RIGHT * 0.05), run_time=0.55)
            self.play(FadeIn(t, shift=RIGHT * 0.05), run_time=0.7)
            y -= 0.92
        self.wait(1.4)

        ox = Line([1.4, -0.55, 0], [6.4, -0.55, 0], color=DIM, stroke_width=2)
        oy = Line([3.9, -2.35, 0], [3.9, 1.35, 0], color=DIM, stroke_width=2)
        self.play(Create(ox), Create(oy), run_time=1.0)

        P1 = (5.3, 0.55)
        self.play(FadeIn(Dot(P(*P1), radius=0.09, color=GOLD)), run_time=0.4)
        lp = txt("P", size=24, color=GOLD).move_to([5.55, 0.85, 0])
        self.play(FadeIn(lp), run_time=0.4)

        Px = (5.3, -1.5)
        d1 = DashedLine(P(*P1), P(*Px), color=RED, stroke_width=2)
        self.play(Create(d1), run_time=0.7)
        self.play(FadeIn(Dot(P(*Px), radius=0.09, color=RED)), run_time=0.4)
        lx = txt("(x, −y)", size=22, color=RED).move_to([5.95, -1.72, 0])
        self.play(FadeIn(lx), run_time=0.6)
        self.wait(0.8)

        Py = (2.5, 0.55)
        d2 = DashedLine(P(*P1), P(*Py), color=BLUE, stroke_width=2)
        self.play(Create(d2), run_time=0.7)
        self.play(FadeIn(Dot(P(*Py), radius=0.09, color=BLUE)), run_time=0.4)
        ly = txt("(−x, y)", size=22, color=BLUE).move_to([2.15, 0.85, 0])
        self.play(FadeIn(ly), run_time=0.6)
        self.wait(1.4)

        box = label_box("关于 x 轴：(x, y) → (x, −y)　　关于 y 轴：(x, y) → (−x, y)",
                        size=24, color=GOLD)
        box.move_to([0, -2.8, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.1)
        self.wait(4.0)
        self.finish_section()

    # ---------------- 3. 等腰三角形：等边对等角 ---------------- 27.4
    def scene_isosceles(self):
        self.section(3, "等腰三角形：等边对等角")

        A, B, C = (-3.5, 2.05), (-5.35, -1.65), (-1.65, -1.65)
        t = tri(A, B, C, CHALK, 0.09)
        self.play(Create(t), run_time=1.3)

        lA = txt("A", size=27, color=CHALK).move_to([-3.5, 2.4, 0])
        lB = txt("B", size=27, color=CHALK).move_to([-5.62, -1.92, 0])
        lC = txt("C", size=27, color=CHALK).move_to([-1.38, -1.92, 0])
        self.play(FadeIn(lA), FadeIn(lB), FadeIn(lC), run_time=0.8)
        self.wait(0.8)

        tk1 = tick(A, B, 1, GOLD, size=0.19)
        tk2 = tick(A, C, 1, GOLD, size=0.19)
        self.play(Create(tk1), Create(tk2), run_time=0.9)

        w1 = txt("腰", size=25, color=GOLD).move_to([-4.95, 0.15, 0])
        w2 = txt("腰", size=25, color=GOLD).move_to([-2.05, 0.15, 0])
        base = txt("底边", size=25, color=BLUE).move_to([-3.5, -2.18, 0])
        self.play(FadeIn(w1), FadeIn(w2), FadeIn(base), run_time=0.9)
        self.wait(1.2)

        aB = ang_arc(B, A, C, radius=0.62, color=GREEN)
        aC = ang_arc(C, A, B, radius=0.62, color=GREEN)
        self.play(Create(aB), Create(aC), run_time=1.0)
        self.wait(1.0)

        n1 = txt("两条边相等的三角形", size=26, color=CHALK).move_to([2.45, 2.1, 0])
        n2 = txt("叫等腰三角形", size=28, color=GOLD).move_to([2.45, 1.42, 0])
        self.play(FadeIn(n1, shift=UP * 0.05), run_time=0.8)
        self.play(FadeIn(n2, shift=UP * 0.05), run_time=0.8)
        self.wait(1.0)

        n3 = txt("两腰的夹角 → 顶角 ∠A", size=25, color=DIM).move_to([2.45, 0.5, 0])
        n4 = txt("腰与底边的夹角 → 底角", size=25, color=DIM).move_to([2.45, -0.2, 0])
        self.play(FadeIn(n3, shift=UP * 0.05), run_time=0.8)
        self.play(FadeIn(n4, shift=UP * 0.05), run_time=0.8)
        self.wait(1.0)

        box = label_box("等边对等角：AB = AC → ∠B = ∠C", size=27, color=GREEN)
        box.move_to([0, -2.85, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.1)
        self.wait(3.4)
        self.finish_section()

    # ---------------- 4. 三线合一 ---------------- 30.1
    def scene_three_lines(self):
        self.section(4, "三线合一")

        A, B, C = (-2.6, 2.15), (-5.0, -1.9), (-0.2, -1.9)
        D = (-2.6, -1.9)
        t = tri(A, B, C, CHALK, 0.08)
        self.play(Create(t), run_time=1.2)

        lA = txt("A", size=26, color=CHALK).move_to([-2.6, 2.5, 0])
        lB = txt("B", size=26, color=CHALK).move_to([-5.25, -2.15, 0])
        lC = txt("C", size=26, color=CHALK).move_to([0.05, -2.15, 0])
        self.play(FadeIn(lA), FadeIn(lB), FadeIn(lC), run_time=0.8)

        ad = Line(P(*A), P(*D), color=GOLD, stroke_width=4)
        self.play(Create(ad), run_time=1.0)
        lD = txt("D", size=25, color=GOLD).move_to([-2.6, -2.22, 0])
        self.play(FadeIn(lD), run_time=0.5)
        self.wait(0.8)

        bd = tick(B, D, 1, BLUE)
        dc = tick(D, C, 1, BLUE)
        self.play(Create(bd), Create(dc), run_time=0.9)

        ra = right_angle(D, A, C, size=0.3, color=GREEN)
        self.play(Create(ra), run_time=0.7)

        aA1 = ang_arc(A, B, D, radius=0.5, color=ORANGE)
        aA2 = ang_arc(A, D, C, radius=0.5, color=ORANGE)
        self.play(Create(aA1), Create(aA2), run_time=0.9)
        self.wait(1.4)

        items = [
            ("顶角的平分线", ORANGE),
            ("底边上的中线", BLUE),
            ("底边上的高", GREEN),
        ]
        y = 2.0
        for s, col in items:
            d = Dot([2.0, y, 0], radius=0.09, color=col)
            tx = txt(s, size=27, color=col).move_to([3.85, y, 0])
            self.play(FadeIn(d), run_time=0.4)
            self.play(FadeIn(tx, shift=RIGHT * 0.05), run_time=0.65)
            y -= 0.85
        self.wait(1.0)

        same = label_box("三条线互相重合 → 三线合一", size=27, color=GOLD)
        same.move_to([3.6, -0.95, 0])
        self.play(FadeIn(same, scale=0.97), run_time=1.1)
        self.wait(1.2)

        warn = txt("只对顶角和底边成立", size=26, color=RED).move_to([3.6, -2.0, 0])
        self.play(FadeIn(warn, shift=UP * 0.05), run_time=0.9)
        self.wait(0.8)
        warn2 = txt("底角的平分线、腰上的高都不行", size=23, color=DIM).move_to([3.6, -2.65, 0])
        self.play(FadeIn(warn2, shift=UP * 0.05), run_time=0.9)
        self.wait(3.4)
        self.finish_section()

    # ---------------- 5. 判定与等边三角形 ---------------- 30.2
    def scene_equilateral(self):
        self.section(5, "反过来：等角对等边")

        A, B, C = (-3.95, 1.45), (-5.25, -0.85), (-2.65, -0.85)
        t = tri(A, B, C, CHALK, 0.09)
        self.play(Create(t), run_time=1.1)

        aB = ang_arc(B, A, C, radius=0.55, color=GREEN)
        aC = ang_arc(C, A, B, radius=0.55, color=GREEN)
        self.play(Create(aB), Create(aC), run_time=0.9)

        lab = txt("∠B = ∠C", size=25, color=GREEN).move_to([-3.95, -1.35, 0])
        self.play(FadeIn(lab), run_time=0.7)

        tk1 = tick(A, B, 1, GOLD)
        tk2 = tick(A, C, 1, GOLD)
        self.play(Create(tk1), Create(tk2), run_time=0.9)
        self.wait(1.2)

        n1 = txt("等角对等边", size=34, color=GOLD).move_to([2.4, 2.2, 0])
        self.play(FadeIn(n1, scale=0.97), run_time=1.0)

        n2 = txt("∠B = ∠C  →  AB = AC", size=27, color=GREEN).move_to([2.4, 1.3, 0])
        self.play(FadeIn(n2, shift=UP * 0.05), run_time=0.9)
        self.wait(1.2)

        eq = Polygon(P(-3.95, 1.62), P(-5.25, -0.58), P(-2.65, -0.58),
                     color=CHALK, stroke_width=3, fill_color=CHALK, fill_opacity=0.08)
        self.play(Transform(t, eq), FadeOut(aB), FadeOut(aC), FadeOut(lab),
                  FadeOut(tk1), FadeOut(tk2), run_time=1.3)

        tri_arcs = VGroup(
            ang_arc((-3.95, 1.62), (-5.25, -0.58), (-2.65, -0.58), 0.5, GREEN),
            ang_arc((-5.25, -0.58), (-3.95, 1.62), (-2.65, -0.58), 0.5, GREEN),
            ang_arc((-2.65, -0.58), (-3.95, 1.62), (-5.25, -0.58), 0.5, GREEN),
        )
        self.play(Create(tri_arcs), run_time=1.2)

        ticks = VGroup(
            tick((-3.95, 1.62), (-5.25, -0.58), 1, GOLD, t=0.56),
            tick((-5.25, -0.58), (-2.65, -0.58), 1, GOLD, t=0.5),
            tick((-2.65, -0.58), (-3.95, 1.62), 1, GOLD, t=0.56),
        )
        self.play(Create(ticks), run_time=1.0)

        deg1 = txt("60°", size=23, color=GREEN).move_to([-3.95, 0.82, 0])
        deg2 = txt("60°", size=21, color=GREEN).move_to([-4.44, 0.0, 0])
        deg3 = txt("60°", size=21, color=GREEN).move_to([-3.46, 0.0, 0])
        self.play(FadeIn(deg1), FadeIn(deg2), FadeIn(deg3), run_time=1.0)
        self.wait(1.2)

        n3 = txt("等边三角形：三边相等，三个角都是 60°", size=25, color=CHALK)
        n3.move_to([2.4, 0.3, 0])
        self.play(FadeIn(n3, shift=UP * 0.05), run_time=0.9)

        n4 = txt("三个角都相等 → 等边", size=25, color=CHALK).move_to([2.4, -0.5, 0])
        self.play(FadeIn(n4, shift=UP * 0.05), run_time=0.85)

        n5 = txt("有一个角是 60° 的等腰三角形 → 等边", size=24, color=CHALK)
        n5.move_to([2.4, -1.25, 0])
        self.play(FadeIn(n5, shift=UP * 0.05), run_time=0.9)
        self.wait(1.4)

        box = label_box("等腰看两边相等，等边看三个角", size=27, color=GOLD)
        box.move_to([0, -2.8, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.1)
        self.wait(3.2)
        self.finish_section()

    # ---------------- 6. 例题与易错点 ---------------- 37.6
    def scene_example(self):
        self.section(6, "例题：一个角 40°，另外两个角呢")

        q = txt("等腰三角形有一个角是 40°，求另外两个角", size=26, color=CHALK)
        q.move_to([0, 2.35, 0])
        self.play(FadeIn(q, shift=UP * 0.05), run_time=1.0)
        self.wait(1.2)

        # 情形一
        h1 = txt("① 40° 是顶角", size=27, color=GOLD).move_to([-3.5, 1.35, 0])
        self.play(FadeIn(h1, shift=UP * 0.04), run_time=0.8)

        w1 = txt("底角 = (180° − 40°) ÷ 2", size=25, color=CHALK).move_to([-3.5, 0.5, 0])
        self.play(FadeIn(w1, shift=UP * 0.04), run_time=0.85)

        r1 = txt("两个底角都是 70°", size=27, color=GREEN).move_to([-3.5, -0.35, 0])
        self.play(FadeIn(r1, shift=UP * 0.04), run_time=0.85)
        self.wait(1.4)

        # 情形二
        h2 = txt("② 40° 是底角", size=27, color=GOLD).move_to([3.35, 1.35, 0])
        self.play(FadeIn(h2, shift=UP * 0.04), run_time=0.8)

        w2 = txt("另一个底角也是 40°", size=25, color=CHALK).move_to([3.35, 0.5, 0])
        self.play(FadeIn(w2, shift=UP * 0.04), run_time=0.85)

        r2 = txt("顶角 = 180° − 80° = 100°", size=25, color=GREEN).move_to([3.35, -0.35, 0])
        self.play(FadeIn(r2, shift=UP * 0.04), run_time=0.85)
        self.wait(1.6)

        split = Line([0, 1.7, 0], [0, -0.8, 0], color=DIM, stroke_width=1.4)
        split.set_opacity(0.35)
        self.play(Create(split), run_time=0.6)

        ans = label_box("答案有两组：70°、70° 或 40°、100°", size=27, color=GOLD)
        ans.move_to([0, -1.55, 0])
        self.play(FadeIn(ans, scale=0.97), run_time=1.1)
        self.wait(1.4)

        warn = txt("易错：不分类讨论　·　三线合一用到腰上　·　对称轴说成线段",
                   size=23, color=RED)
        warn.move_to([0, -2.5, 0])
        self.play(FadeIn(warn, shift=UP * 0.04), run_time=1.0)
        self.wait(3.4)
        self.finish_section()

    def construct(self):
        self.scene_intro()
        self.clear_stage()
        self.scene_property()
        self.clear_stage()
        self.scene_draw()
        self.clear_stage()
        self.scene_isosceles()
        self.clear_stage()
        self.scene_three_lines()
        self.clear_stage()
        self.scene_equilateral()
        self.clear_stage()
        self.scene_example()
        self.clear_stage(0.8)