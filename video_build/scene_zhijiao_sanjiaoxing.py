# -*- coding: utf-8 -*-
"""直角三角形的性质：两锐角互余、30° 所对直角边是斜边一半、斜边中线是斜边一半。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403

# 直角三角形：直角在 R，∠Q = 30°，斜边 PQ = 4，PR = 2，RQ = 2√3 ≈ 3.46
P = [-5.6, 0.8, 0]
Q = [-2.14, -1.2, 0]
R = [-5.6, -1.2, 0]


def tri(scale: float = 1.0, center: list[float] | None = None) -> Polygon:
    pts = [P, Q, R]
    if center is None:
        center = [-3.9, -0.2, 0]
    out = []
    for p in pts:
        out.append([center[0] + (p[0] - center[0]) * scale,
                    center[1] + (p[1] - center[1]) * scale, 0])
    return Polygon(*out, stroke_color=CHALK, stroke_width=2.6,
                   fill_color=BLUE, fill_opacity=0.08)


def right_mark(v: list[float], a: list[float], b: list[float], s: float = 0.26) -> VGroup:
    def unit(p):
        d = [p[0] - v[0], p[1] - v[1], 0]
        n = (d[0] ** 2 + d[1] ** 2) ** 0.5
        return [d[0] / n * s, d[1] / n * s, 0]
    ua, ub = unit(a), unit(b)
    p1 = [v[0] + ua[0], v[1] + ua[1], 0]
    p2 = [v[0] + ua[0] + ub[0], v[1] + ua[1] + ub[1], 0]
    p3 = [v[0] + ub[0], v[1] + ub[1], 0]
    return VGroup(
        Line(p1, p2, color=GOLD, stroke_width=1.8),
        Line(p2, p3, color=GOLD, stroke_width=1.8),
    )


class ZhijiaoSanjiaoxingScene(NarratedScene):
    lesson = "zhijiao-sanjiaoxing"

    def construct(self):
        # ---------- 0. 只量斜边 ----------
        self.section(0, "直角三角形，斜边最长")
        t = tri()
        self.play(Create(t), run_time=1.1)

        nm_r = txt("直角", size=22, color=GOLD).move_to([-4.55, -1.55, 0])
        rm = right_mark(R, P, Q)
        self.play(Create(rm), FadeIn(nm_r), run_time=0.7)

        hyp = Line(P, Q, color=GOLD, stroke_width=4)
        hlab = txt("斜边", size=26, color=GOLD).move_to([-2.6, 0.05, 0])
        self.play(Create(hyp), FadeIn(hlab), run_time=0.8)

        q1 = txt("只量出斜边", size=34, color=CHALK).move_to([3.5, 1.15, 0])
        q2 = txt("能算出最短的边吗？", size=34, color=GOLD).move_to([3.5, 0.2, 0])
        self.play(Write(q1), run_time=0.6)
        self.play(Write(q2), run_time=0.6)

        q3 = txt("先看直角三角形有哪些性质", size=28, color=DIM).move_to([3.5, -0.9, 0])
        self.play(FadeIn(q3), run_time=0.5)
        self.finish_section()

        # ---------- 1. 两锐角互余 ----------
        self.section(1, "两个锐角加起来是 90°")
        self.play(FadeOut(q1), FadeOut(q2), FadeOut(q3), FadeOut(hlab), run_time=0.4)

        p_ang = txt("∠P + ∠Q = 90°", size=40, color=GREEN).move_to([3.5, 1.0, 0])
        sum1 = txt("三角形内角和 180°", size=30, color=CHALK).move_to([3.5, 0.05, 0])
        sum2 = txt("减去直角 90°", size=30, color=CHALK).move_to([3.5, -0.75, 0])
        sum3 = txt("剩下 90° 给两个锐角", size=30, color=GOLD).move_to([3.5, -1.6, 0])
        self.play(Write(p_ang), run_time=0.7)
        self.play(FadeIn(sum1), run_time=0.5)
        self.play(FadeIn(sum2), run_time=0.5)
        self.play(FadeIn(sum3), run_time=0.6)

        a60 = txt("60°", size=26, color=BLUE).move_to([-5.0, 0.15, 0])
        a30 = txt("30°", size=26, color=ORANGE).move_to([-2.9, -1.5, 0])
        self.play(FadeIn(a60), FadeIn(a30), run_time=0.8)
        self.finish_section()

        # ---------- 2. 30° 对的直角边 ----------
        self.section(2, "30° 对的直角边是斜边一半")
        self.play(FadeOut(p_ang), FadeOut(sum1), FadeOut(sum2), FadeOut(sum3),
                  run_time=0.4)

        leg = Line(P, R, color=ORANGE, stroke_width=5)
        l1 = txt("30° 对的直角边", size=30, color=ORANGE).move_to([3.5, 1.15, 0])
        l2 = txt("= 斜边 × 1/2", size=36, color=ORANGE).move_to([3.5, 0.25, 0])
        self.play(Create(leg), run_time=0.7)
        self.play(Write(l1), run_time=0.6)
        self.play(Write(l2), run_time=0.6)

        eq = txt("斜边 4，这条边就是 2", size=30, color=GREEN).move_to([3.5, -0.85, 0])
        self.play(FadeIn(eq, shift=UP * 0.1), run_time=0.6)

        side_hyp = txt("4", size=22, color=GOLD).move_to([-3.55, 0.05, 0])
        side_leg = txt("2", size=22, color=ORANGE).move_to([-5.9, -0.2, 0])
        self.play(FadeIn(side_hyp), FadeIn(side_leg), run_time=0.6)
        self.finish_section()

        # ---------- 3. 反过来也成立 ----------
        self.section(3, "反过来，也能判断 30°")
        self.play(FadeOut(l1), FadeOut(l2), FadeOut(eq), run_time=0.4)

        c1 = txt("一条直角边 = 斜边的一半", size=32, color=CHALK).move_to([3.5, 1.1, 0])
        c2 = txt("↓", size=30, color=DIM).move_to([3.5, 0.3, 0])
        c3 = txt("它所对的角就是 30°", size=34, color=GOLD).move_to([3.5, -0.55, 0])
        self.play(Write(c1), run_time=0.7)
        self.play(FadeIn(c2), run_time=0.4)
        self.play(Write(c3), run_time=0.7)

        c4 = txt("这是判断 30° 的常用办法", size=28, color=DIM).move_to([3.5, -1.6, 0])
        self.play(FadeIn(c4), run_time=0.5)

        arc = Arc(radius=0.75, start_angle=150 * DEGREES, angle=30 * DEGREES, arc_center=Q,
                  color=ORANGE, stroke_width=2)
        self.play(Create(arc), run_time=0.7)
        self.finish_section()

        # ---------- 4. 斜边中线 ----------
        self.section(4, "斜边中线也是斜边一半")
        self.play(FadeOut(c1), FadeOut(c2), FadeOut(c3), FadeOut(c4),
                  FadeOut(arc), FadeOut(side_hyp), FadeOut(side_leg), run_time=0.5)

        M = [(-5.6 + -2.14) / 2, (0.8 + -1.2) / 2, 0]
        dot = Dot(M, radius=0.07, color=BLUE)
        med = Line(R, M, color=BLUE, stroke_width=4)
        self.play(FadeIn(dot), Create(med), run_time=0.9)

        m1 = txt("取斜边的中点", size=32, color=CHALK).move_to([3.5, 1.2, 0])
        m2 = txt("连到直角顶点", size=32, color=CHALK).move_to([3.5, 0.35, 0])
        m3 = txt("中线 = 斜边 × 1/2", size=34, color=BLUE).move_to([3.5, -0.6, 0])
        self.play(Write(m1), run_time=0.6)
        self.play(Write(m2), run_time=0.5)
        self.play(Write(m3), run_time=0.7)

        m4 = txt("三条线段一样长", size=28, color=DIM).move_to([3.5, -1.65, 0])
        self.play(FadeIn(m4), run_time=0.5)
        self.finish_section()

        # ---------- 5. 用来求线段长 ----------
        self.section(5, "知道了性质，就能算长度")
        self.play(FadeOut(t), FadeOut(hyp), FadeOut(rm), FadeOut(nm_r), FadeOut(leg),
                  FadeOut(dot), FadeOut(med), FadeOut(side_hyp), FadeOut(side_leg),
                  FadeOut(arc), FadeOut(a60), FadeOut(a30),
                  FadeOut(m1), FadeOut(m2), FadeOut(m3), FadeOut(m4), run_time=0.6)

        e1 = txt("斜边 AC = 10，∠A = 30°", size=38, color=CHALK).move_to([0, 1.3, 0])
        e2 = txt("∠A 所对的直角边 BC", size=36, color=ORANGE).move_to([0, 0.35, 0])
        e3 = txt("= 10 × 1/2 = 5", size=42, color=GREEN).move_to([0, -0.55, 0])
        e4 = txt("斜边中线 = 10 × 1/2 = 5", size=34, color=BLUE).move_to([0, -1.55, 0])
        self.play(Write(e1), run_time=0.8)
        self.play(Write(e2), run_time=0.7)
        self.play(Write(e3), run_time=0.7)
        self.play(FadeIn(e4, shift=UP * 0.1), run_time=0.6)
        self.finish_section()

        # ---------- 6. 口诀 ----------
        self.section(6, "两锐角互余，三十度对一半")
        self.play(FadeOut(e1), FadeOut(e2), FadeOut(e3), FadeOut(e4), run_time=0.5)

        k1 = txt("两锐角互余", size=46, color=GREEN).move_to([0, 1.25, 0])
        k2 = txt("30° 对的直角边 = 斜边一半", size=42, color=ORANGE).move_to([0, 0.2, 0])
        k3 = txt("斜边中线 = 斜边一半", size=42, color=BLUE).move_to([0, -0.85, 0])
        self.play(Write(k1), run_time=0.7)
        self.play(Write(k2), run_time=0.8)
        self.play(Write(k3), run_time=0.8)

        fin = txt("三条性质，都指向同一条斜边", size=28, color=DIM).move_to([0, -1.95, 0])
        self.play(FadeIn(fin), run_time=0.5)
        self.finish_section()

        self.play(FadeOut(k1), FadeOut(k2), FadeOut(k3), FadeOut(fin), run_time=0.6)