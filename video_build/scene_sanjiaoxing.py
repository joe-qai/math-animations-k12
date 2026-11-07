# -*- coding: utf-8 -*-
"""三角形内角和与三边关系：内角和 180°、外角定理、三边关系与等腰分类。七年级下。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


def P(x, y):
    return np.array([float(x), float(y), 0.0])


def ang_arc(O, dA, dB, color=GOLD, radius=0.8, lab=None, lab_r=1.22,
            size=23, lab_color=None, width=2.6):
    """以 O 为顶点、沿 dA、dB 两个方向的劣角弧（手动画，避免优角）。"""
    o = P(*O)
    ua = P(*dA)
    ua = ua / np.linalg.norm(ua)
    ub = P(*dB)
    ub = ub / np.linalg.norm(ub)
    a1 = float(np.arctan2(ua[1], ua[0]))
    a2 = float(np.arctan2(ub[1], ub[0]))
    d = (a2 - a1) % TAU
    if d > PI:
        start = a2
        d = TAU - d
    else:
        start = a1
    arc = Arc(radius=radius, start_angle=start, angle=d, arc_center=o,
              color=color, stroke_width=width)
    grp = VGroup(arc)
    if lab:
        mid = start + d / 2
        pos = o + np.array([np.cos(mid), np.sin(mid), 0.0]) * lab_r
        grp.add(txt(lab, size=size, color=lab_color or color)
                .move_to([pos[0], pos[1], 0]))
    return grp


def right_angle(vertex, u, v, size=0.3, color=GOLD):
    o = P(*vertex)
    uu = P(*u)
    uu = uu / np.linalg.norm(uu) * size
    vv = P(*v)
    vv = vv / np.linalg.norm(vv) * size
    pts = [o + uu, o + uu + vv, o + vv]
    return VGroup(*[Line(pts[0], pts[1], color=color, stroke_width=2.2),
                    Line(pts[1], pts[2], color=color, stroke_width=2.2)])


class SanjiaoxingScene(NarratedScene):
    lesson = "sanjiaoxing"

    def clear_stage(self, run_time: float = 0.5):
        keep = {id(self._track), id(self._fill)}
        junk = [m for m in self.mobjects if id(m) not in keep]
        if junk:
            self.play(*[FadeOut(m) for m in junk], run_time=run_time)
        self.cur_title = None
        self.cur_sub = None

    # ---------------- 0. 为什么到处都是三角形 ---------------- 27.2
    def scene_story(self):
        self.section(0, "为什么到处都是三角形")

        tri = Polygon(P(-6.0, -1.3), P(-1.8, -1.3), P(-3.9, 1.2),
                      color=GOLD, stroke_width=3, fill_color=GOLD, fill_opacity=0.1)
        self.play(Create(tri), run_time=1.2)
        struts = VGroup(
            Line(P(-3.9, 1.2), P(-3.9, -1.3), color=DIM, stroke_width=1.8),
            Line(P(-3.9, -1.3), P(-4.95, -0.05), color=DIM, stroke_width=1.8),
            Line(P(-3.9, -1.3), P(-2.85, -0.05), color=DIM, stroke_width=1.8),
        )
        self.play(Create(struts), run_time=1.2)
        t1 = txt("三角形：推不动", size=26, color=GOLD).move_to([-3.9, -2.25, 0])
        self.play(FadeIn(t1, shift=UP * 0.05), run_time=0.8)

        quad = Polygon(P(-0.4, -1.0), P(1.5, -1.0), P(1.5, 0.9), P(-0.4, 0.9),
                       color=BLUE, stroke_width=3, fill_color=BLUE, fill_opacity=0.1)
        self.play(Create(quad), run_time=1.2)
        t2 = txt("四边形：一推就歪", size=26, color=BLUE).move_to([3.55, -2.25, 0])
        self.play(FadeIn(t2, shift=UP * 0.05), run_time=0.8)

        leaned = Polygon(P(0.6, -1.0), P(2.5, -1.0), P(2.0, 0.9), P(0.1, 0.9),
                         color=BLUE, stroke_width=3, fill_color=BLUE, fill_opacity=0.1)
        self.play(Transform(quad, leaned), run_time=1.6)
        self.play(Indicate(quad, color=BLUE, scale_factor=1.03), run_time=0.9)

        note = txt("三边一定，形状就定了；这是三角形的稳定性", size=26, color=CHALK)
        note.move_to([0, -2.85, 0])
        self.play(FadeIn(note, shift=UP * 0.05), run_time=1.0)
        self.wait(3.2)
        self.finish_section()

    # ---------------- 1. 内角和 180° ---------------- 24.1
    def scene_sum(self):
        self.section(1, "内角和为什么是 180°")

        A, B, C = (-5.2, -1.7), (-1.4, -1.7), (-3.3, 1.3)
        tri = Polygon(P(*A), P(*B), P(*C), color=CHALK, stroke_width=3,
                      fill_color=CHALK, fill_opacity=0.05)
        self.play(Create(tri), run_time=1.2)
        labs = VGroup(
            txt("A", size=24, color=DIM).move_to([A[0] - 0.22, A[1] - 0.32, 0]),
            txt("B", size=24, color=DIM).move_to([B[0] + 0.25, B[1] - 0.32, 0]),
            txt("C", size=24, color=DIM).move_to([C[0], C[1] + 0.3, 0]),
        )
        self.play(FadeIn(labs), run_time=0.6)

        alpha = ang_arc(A, (1, 0), (C[0] - A[0], C[1] - A[1]),
                        color=GOLD, radius=0.62, lab="α", lab_r=0.95)
        beta = ang_arc(B, (-1, 0), (C[0] - B[0], C[1] - B[1]),
                       color=BLUE, radius=0.62, lab="β", lab_r=0.95, lab_color=BLUE)
        gamma = ang_arc(C, (A[0] - C[0], A[1] - C[1]), (B[0] - C[0], B[1] - C[1]),
                        color=GREEN, radius=0.62, lab="γ", lab_r=0.95, lab_color=GREEN)
        for g in (alpha, beta, gamma):
            self.play(FadeIn(g, scale=0.9), run_time=0.7)

        para = Line(P(-6.6, C[1]), P(-0.1, C[1]), color=ORANGE, stroke_width=2.4)
        self.play(Create(para), run_time=1.1)
        pnote = txt("过 C 作 AB 的平行线", size=24, color=ORANGE)
        pnote.move_to([-0.55, C[1] + 0.42, 0])
        self.play(FadeIn(pnote, shift=UP * 0.05), run_time=0.8)

        a2 = ang_arc(C, (-1, 0), (A[0] - C[0], A[1] - C[1]),
                     color=GOLD, radius=0.86, lab="α", lab_r=1.15)
        b2 = ang_arc(C, (1, 0), (B[0] - C[0], B[1] - C[1]),
                     color=BLUE, radius=0.86, lab="β", lab_r=1.15, lab_color=BLUE)
        self.play(FadeIn(a2, scale=0.9), run_time=0.8)
        self.play(FadeIn(b2, scale=0.9), run_time=0.8)

        res = VGroup(
            txt("α + β + γ", size=30, color=CHALK),
            txt("=", size=28, color=DIM),
            txt("180°", size=32, color=GREEN),
        ).arrange(RIGHT, buff=0.22).move_to([4.3, 0.9, 0])
        self.play(FadeIn(res, shift=UP * 0.05), run_time=1.0)

        why = VGroup(
            txt("α、β 被平行线搬到了 C 点", size=24, color=CHALK),
            txt("三个角拼成一个平角", size=24, color=GREEN),
        ).arrange(DOWN, buff=0.32).move_to([4.3, -0.35, 0])
        for m in why:
            self.play(FadeIn(m, shift=UP * 0.05), run_time=0.8)

        note = txt("三角形内角和 = 180°，与形状大小无关", size=26, color=GOLD)
        note.move_to([0, -2.75, 0])
        self.play(FadeIn(note, shift=UP * 0.05), run_time=0.9)
        self.wait(2.4)
        self.finish_section()

    # ---------------- 2. 两个推论 ---------------- 25.3
    def scene_corollary(self):
        self.section(2, "直角互余与外角定理")

        A, B, C = (-6.4, -1.0), (-3.6, -1.0), (-6.4, 1.0)
        tri = Polygon(P(*A), P(*B), P(*C), color=CHALK, stroke_width=3,
                      fill_color=CHALK, fill_opacity=0.05)
        self.play(Create(tri), run_time=1.1)
        ra = right_angle(A, (1, 0), (0, 1), size=0.32, color=GREEN)
        self.play(Create(ra), run_time=0.6)
        ar1 = ang_arc(B, (-1, 0), (C[0] - B[0], C[1] - B[1]),
                      color=GOLD, radius=0.5)
        ar2 = ang_arc(C, (0, -1), (B[0] - C[0], B[1] - C[1]),
                      color=BLUE, radius=0.5)
        self.play(FadeIn(ar1), FadeIn(ar2), run_time=0.8)

        t1 = VGroup(
            txt("直角三角形，两锐角互余", size=26, color=CHALK),
            txt("∠B + ∠C = 90°", size=30, color=GOLD),
        ).arrange(DOWN, buff=0.34).move_to([-4.9, -2.15, 0])
        for m in t1:
            self.play(FadeIn(m, shift=UP * 0.05), run_time=0.8)

        A2, B2, C2 = (1.3, -1.1), (3.9, -1.1), (2.6, 0.9)
        D2 = (5.3, -1.1)
        tri2 = Polygon(P(*A2), P(*B2), P(*C2), color=CHALK, stroke_width=3,
                       fill_color=CHALK, fill_opacity=0.05)
        self.play(Create(tri2), run_time=1.0)
        ext = Line(P(*B2), P(*D2), color=ORANGE, stroke_width=2.6)
        self.play(Create(ext), run_time=0.8)

        ar3 = ang_arc(B2, (1, 0), (C2[0] - B2[0], C2[1] - B2[1]),
                      color=ORANGE, radius=0.62, lab="外角", lab_r=1.35,
                      size=22, lab_color=ORANGE)
        self.play(FadeIn(ar3, scale=0.9), run_time=0.8)

        t2 = VGroup(
            txt("外角 = 不相邻两内角之和", size=26, color=ORANGE),
            txt("外角 > 任何一个不相邻内角", size=23, color=DIM),
        ).arrange(DOWN, buff=0.3).move_to([4.2, 2.0, 0])
        for m in t2:
            self.play(FadeIn(m, shift=UP * 0.05), run_time=0.8)

        t3 = txt("外角与相邻内角互补", size=25, color=DIM).move_to([4.2, -2.15, 0])
        self.play(FadeIn(t3, shift=UP * 0.05), run_time=0.8)
        self.wait(2.8)
        self.finish_section()

    # ---------------- 3. 三边关系 ---------------- 23.0
    def scene_sides(self):
        self.section(3, "三边关系：两点之间线段最短")

        A, B = (-6.0, -1.2), (-1.6, -1.2)
        M = (-3.8, 1.4)
        straight = Line(P(*A), P(*B), color=GOLD, stroke_width=4)
        self.play(Create(straight), run_time=1.0)
        dA = Dot(P(*A), radius=0.08, color=CHALK)
        dB = Dot(P(*B), radius=0.08, color=CHALK)
        self.play(FadeIn(dA), FadeIn(dB), run_time=0.6)

        broken = VGroup(Line(P(*A), P(*M), color=BLUE, stroke_width=2.6),
                        Line(P(*M), P(*B), color=BLUE, stroke_width=2.6))
        self.play(Create(broken), run_time=1.3)
        self.play(Indicate(straight, color=GOLD, scale_factor=1.02), run_time=0.9)

        t1 = VGroup(
            txt("走直线最短", size=27, color=GOLD),
            txt("所以 a + b > c", size=28, color=GREEN),
        ).arrange(DOWN, buff=0.34).move_to([4.0, 1.0, 0])
        for m in t1:
            self.play(FadeIn(m, shift=UP * 0.05), run_time=0.85)

        t2 = VGroup(
            txt("任意两边之和 > 第三边", size=26, color=CHALK),
            txt("任意两边之差 < 第三边", size=26, color=CHALK),
        ).arrange(DOWN, buff=0.34).move_to([4.0, -0.55, 0])
        for m in t2:
            self.play(FadeIn(m, shift=UP * 0.05), run_time=0.8)

        note = txt("三条线段要围成三角形，这两条必须同时满足", size=25, color=DIM)
        note.move_to([0, -2.75, 0])
        self.play(FadeIn(note, shift=UP * 0.05), run_time=0.9)
        self.wait(2.4)
        self.finish_section()

    # ---------------- 4. 能不能组成三角形 ---------------- 29.3
    def scene_judge(self):
        self.section(4, "先看最短的两条")

        head = txt("检查：两条较短的边之和 > 最长边", size=27, color=GOLD)
        head.move_to([0, 2.4, 0])
        self.play(FadeIn(head, shift=UP * 0.05), run_time=0.9)

        rows = [
            ("3、4、5", "3 + 4 = 7 > 5", "√ 能组成", GREEN),
            ("1、2、4", "1 + 2 = 3 < 4", "× 不能组成", RED),
            ("2、3、6", "2 + 3 = 5 < 6", "× 不能组成", RED),
        ]
        y = 1.35
        for data, calc, res, col in rows:
            g1 = txt(data, size=28, color=CHALK).move_to([-4.2, y, 0])
            g2 = txt(calc, size=26, color=DIM).move_to([-0.6, y, 0])
            g3 = txt(res, size=27, color=col).move_to([4.1, y, 0])
            self.play(FadeIn(g1, shift=RIGHT * 0.05), run_time=0.6)
            self.play(FadeIn(g2, shift=RIGHT * 0.05), run_time=0.6)
            self.play(FadeIn(g3, shift=RIGHT * 0.05), run_time=0.65)
            y -= 1.05

        b1 = label_box("等腰三角形要分两种情况", size=28, color=GOLD)
        b1.move_to([0, -2.05, 0])
        self.play(FadeIn(b1, scale=0.97), run_time=1.0)

        note = txt("两种情况都要回头检验三边关系", size=25, color=DIM).move_to([0, -2.75, 0])
        self.play(FadeIn(note, shift=UP * 0.05), run_time=0.8)
        self.wait(3.0)
        self.finish_section()

    # ---------------- 5. 求第三边的范围 ---------------- 26.1
    def scene_range(self):
        self.section(5, "已知两边，求第三边")

        q = txt("三角形两边长 3 和 5", size=29, color=CHALK).move_to([0, 2.35, 0])
        self.play(FadeIn(q, shift=UP * 0.05), run_time=0.9)

        up = VGroup(txt("3 + 5", size=30, color=GOLD), txt("= 8", size=30, color=DIM),
                    txt("→ x < 8", size=30, color=GREEN)).arrange(RIGHT, buff=0.25)
        up.move_to([0, 1.3, 0])
        self.play(FadeIn(up, shift=UP * 0.05), run_time=0.9)

        dn = VGroup(txt("5 − 3", size=30, color=GOLD), txt("= 2", size=30, color=DIM),
                    txt("→ x > 2", size=30, color=GREEN)).arrange(RIGHT, buff=0.25)
        dn.move_to([0, 0.35, 0])
        self.play(FadeIn(dn, shift=UP * 0.05), run_time=0.9)

        box = label_box("2 < x < 8", size=38, color=GOLD).move_to([0, -0.95, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.1)

        note = VGroup(
            txt("第三边大于两边之差，小于两边之和", size=25, color=CHALK),
            txt("两端都取不到，因为要「大于」和「小于」", size=24, color=DIM),
        ).arrange(DOWN, buff=0.3).move_to([0, -2.15, 0])
        for m in note:
            self.play(FadeIn(m, shift=UP * 0.05), run_time=0.8)

        self.wait(2.8)
        self.finish_section()

    # ---------------- 6. 例题与三个易错点 ---------------- 32.3
    def scene_ex(self):
        self.section(6, "例题与三个易错点")

        q = txt("等腰三角形两边长 3 和 7，求周长", size=27, color=CHALK).move_to([0, 2.4, 0])
        self.play(FadeIn(q, shift=UP * 0.05), run_time=0.9)

        c1 = VGroup(
            txt("若腰 = 3：", size=26, color=DIM),
            txt("3 + 3 = 6 < 7", size=26, color=RED),
            txt("围不成，舍去", size=26, color=RED),
        ).arrange(RIGHT, buff=0.22).move_to([0, 1.55, 0])
        self.play(FadeIn(c1, shift=RIGHT * 0.05), run_time=0.8)

        c2 = VGroup(
            txt("若腰 = 7：", size=26, color=DIM),
            txt("7 + 7 > 3", size=26, color=GREEN),
            txt("周长 = 17", size=26, color=GREEN),
        ).arrange(RIGHT, buff=0.22).move_to([0, 0.8, 0])
        self.play(FadeIn(c2, shift=RIGHT * 0.05), run_time=0.9)

        items = [
            ("内角和记成 360°", "三角形是 180°"),
            ("不算就答，忘了检验", "先看三边关系"),
            ("等腰只算一种情况", "腰和底都要试"),
        ]
        y = -0.35
        for bad_s, good_s in items:
            bad = txt(bad_s, size=24, color=RED).move_to([-2.9, y, 0])
            good = txt(good_s, size=23, color=GREEN).move_to([3.7, y, 0])
            cross = Line([bad.get_left()[0] - 0.07, y - 0.07, 0],
                         [bad.get_right()[0] + 0.07, y - 0.07, 0],
                         color=RED, stroke_width=2.2)
            self.play(FadeIn(bad, shift=RIGHT * 0.05), run_time=0.55)
            self.play(Create(cross), run_time=0.35)
            self.play(FadeIn(good, shift=RIGHT * 0.05), run_time=0.55)
            y -= 0.75

        self.wait(2.8)
        self.finish_section()

    def construct(self):
        self.scene_story()
        self.clear_stage()
        self.scene_sum()
        self.clear_stage()
        self.scene_corollary()
        self.clear_stage()
        self.scene_sides()
        self.clear_stage()
        self.scene_judge()
        self.clear_stage()
        self.scene_range()
        self.clear_stage()
        self.scene_ex()
        self.clear_stage(0.8)