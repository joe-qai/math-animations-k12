# -*- coding: utf-8 -*-
"""三角形的认识：内角和 180°、两边之和大于第三边。四年级下册「三角形」。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


def angle_wedge(v, p1, p2, color: str, radius: float = 0.55,
                opacity: float = 0.35) -> Polygon:
    a1 = np.arctan2(p1[1] - v[1], p1[0] - v[0])
    a2 = np.arctan2(p2[1] - v[1], p2[0] - v[0])
    diff = (a2 - a1) % (2 * PI)
    start = a1
    if diff > PI:
        diff = 2 * PI - diff
        start = a2
    pts = [v] + [
        [v[0] + radius * np.cos(start + diff * t / 24),
         v[1] + radius * np.sin(start + diff * t / 24), 0]
        for t in range(25)
    ]
    return Polygon(*pts, stroke_width=1.2, stroke_color=color,
                   fill_color=color, fill_opacity=opacity)


def sector(radius: float, angle: float, start: float, color: str) -> Polygon:
    pts = [[0, 0, 0]] + [
        [radius * np.cos(start + angle * t / 28),
         radius * np.sin(start + angle * t / 28), 0]
        for t in range(29)
    ]
    return Polygon(*pts, stroke_width=1.2, stroke_color=color,
                   fill_color=color, fill_opacity=0.4)


def tri_angles(A, B, C) -> list[float]:
    import math
    out = []
    for v, p1, p2 in ((A, B, C), (B, C, A), (C, A, B)):
        a = math.dist(v, p1)
        b = math.dist(v, p2)
        c = math.dist(p1, p2)
        out.append(math.degrees(math.acos((a * a + b * b - c * c) / (2 * a * b))))
    return out


class SanjiaoxingNeijiaoheScene(NarratedScene):
    lesson = "sanjiaoxing-neijiaohe"

    def construct(self):
        A = np.array([-2.4, 1.5, 0])
        B = np.array([2.8, 1.5, 0])
        C = np.array([0.3, -1.4, 0])

        # ---------- 0. 三角形有三个角 ----------
        self.section(0, "三个角加起来是多少度？")
        tri = Polygon(A, B, C, stroke_width=4, stroke_color=CHALK, fill_opacity=0)
        self.play(Create(tri), run_time=1.0)

        w1 = angle_wedge(A, B, C, GOLD)
        w2 = angle_wedge(B, C, A, BLUE)
        w3 = angle_wedge(C, A, B, GREEN)
        self.play(FadeIn(w1), run_time=0.5)
        self.play(FadeIn(w2), run_time=0.5)
        self.play(FadeIn(w3), run_time=0.5)

        l1 = txt("∠1", size=30, color=GOLD).move_to(A + np.array([0.62, -0.35, 0]))
        l2 = txt("∠2", size=30, color=BLUE).move_to(B + np.array([-0.62, -0.35, 0]))
        l3 = txt("∠3", size=30, color=GREEN).move_to(C + np.array([0.0, 0.55, 0]))
        self.play(FadeIn(l1), FadeIn(l2), FadeIn(l3), run_time=0.6)

        q = txt("三角形的内角和是多少？", size=38, color=CHALK).move_to([0, -2.25, 0])
        self.play(FadeIn(q, shift=UP * 0.1), run_time=0.6)
        self.finish_section()

        # ---------- 1. 撕角拼成平角 ----------
        self.section(1, "三个角拼起来，正好是平角")
        self.play(FadeOut(q), run_time=0.4)

        ang = tri_angles(A, B, C)
        base = Line([-5.2, -0.2, 0], [5.2, -0.2, 0], color=DIM, stroke_width=2)
        self.play(FadeOut(tri), FadeOut(w1), FadeOut(w2), FadeOut(w3),
                  FadeOut(l1), FadeOut(l2), FadeOut(l3), Create(base), run_time=0.7)

        s1 = sector(1.9, ang[0] * DEGREES, 180 * DEGREES - ang[0] * DEGREES, GOLD)
        s2 = sector(1.9, ang[1] * DEGREES,
                    180 * DEGREES - ang[0] * DEGREES - ang[1] * DEGREES, BLUE)
        s3 = sector(1.9, ang[2] * DEGREES, 0, GREEN)
        for s in (s1, s2, s3):
            s.move_to([0, -0.2, 0])
        self.play(FadeIn(s1), run_time=0.6)
        self.play(FadeIn(s2), run_time=0.6)
        self.play(FadeIn(s3), run_time=0.6)

        e1 = txt("∠1 + ∠2 + ∠3 = 180°", size=46, color=GOLD).move_to([0, 2.2, 0])
        e2 = txt("正好拼成一个平角", size=34, color=GREEN).move_to([0, -2.55, 0])
        self.play(Write(e1), run_time=0.9)
        self.play(FadeIn(e2, shift=UP * 0.1), run_time=0.6)
        self.finish_section()

        # ---------- 2. 直角三角形 ----------
        self.section(2, "直角三角形：两个锐角合起来 90°")
        self.play(FadeOut(base), FadeOut(s1), FadeOut(s2), FadeOut(s3),
                  FadeOut(e1), FadeOut(e2), run_time=0.6)

        P = np.array([-2.6, -1.1, 0])
        Q = np.array([2.2, -1.1, 0])
        R = np.array([-2.6, 1.9, 0])
        rt = Polygon(P, Q, R, stroke_width=4, stroke_color=CHALK, fill_opacity=0)
        self.play(Create(rt), run_time=1.0)

        sq = Square(side_length=0.42, stroke_color=GOLD, stroke_width=2
                    ).move_to([-2.6 + 0.21, -1.1 + 0.21, 0])
        r90 = txt("90°", size=30, color=GOLD).move_to([-1.95, -0.55, 0])
        self.play(Create(sq), FadeIn(r90), run_time=0.6)

        ra = angle_wedge(Q, R, P, BLUE)
        rb = angle_wedge(R, P, Q, GREEN)
        self.play(FadeIn(ra), FadeIn(rb), run_time=0.6)

        c1 = txt("∠A + ∠B = 90°", size=40, color=GREEN).move_to([4.25, 0.6, 0])
        c2 = txt("三个角仍是 180°", size=32, color=DIM).move_to([4.25, -0.3, 0])
        c3 = txt("90° + 90° = 180°", size=34, color=GOLD).move_to([4.25, -1.2, 0])
        self.play(Write(c1), run_time=0.8)
        self.play(FadeIn(c2), run_time=0.5)
        self.play(Write(c3), run_time=0.7)
        self.finish_section()

        # ---------- 3. 三边关系：能围成 ----------
        self.section(3, "三条边：3、4、5 能围成")
        self.play(FadeOut(rt), FadeOut(sq), FadeOut(r90), FadeOut(ra), FadeOut(rb),
                  FadeOut(c1), FadeOut(c2), FadeOut(c3), run_time=0.6)

        k = 0.62
        p0 = np.array([-3.4, -1.4, 0])
        p1 = p0 + np.array([3 * k, 0, 0])
        p2 = p0 + np.array([0, 4 * k, 0])
        t345 = Polygon(p0, p1, p2, stroke_width=6, stroke_color=BLUE, fill_opacity=0)
        t345b = Polygon(p0, p1, p2, stroke_width=6, stroke_color=GOLD, fill_opacity=0)
        self.play(Create(t345), run_time=0.8)

        m3 = txt("3", size=30, color=BLUE).move_to((p0 + p1) / 2 + np.array([0, -0.35, 0]))
        m4 = txt("4", size=30, color=BLUE).move_to((p0 + p2) / 2 + np.array([-0.35, 0, 0]))
        m5 = txt("5", size=30, color=BLUE).move_to((p1 + p2) / 2 + np.array([0.35, 0.2, 0]))
        self.play(FadeIn(m3), FadeIn(m4), FadeIn(m5), run_time=0.6)

        d1 = txt("3 + 4 = 7 > 5", size=38, color=GREEN).move_to([3.4, 1.0, 0])
        d2 = txt("两边之和大于第三边", size=32, color=DIM).move_to([3.4, 0.1, 0])
        d3 = txt("✓ 能围成三角形", size=36, color=GREEN).move_to([3.4, -0.9, 0])
        self.play(Write(d1), run_time=0.7)
        self.play(FadeIn(d2), run_time=0.5)
        self.play(FadeIn(d3, shift=UP * 0.1), run_time=0.6)
        self.finish_section()

        # ---------- 4. 3、4、8 摆不成 ----------
        self.section(4, "3、4、8 摆不成：两根短棒够不到")
        self.play(FadeOut(t345), FadeOut(t345b), FadeOut(m3), FadeOut(m4), FadeOut(m5),
                  FadeOut(d1), FadeOut(d2), FadeOut(d3), run_time=0.6)

        bars = VGroup()
        lens = [("3", 3), ("4", 4), ("8", 8)]
        for i, (name, L) in enumerate(lens):
            y = 1.2 - i * 0.95
            bar = Line([-5.0, y, 0], [-5.0 + L * 0.62, y, 0],
                       color=RED if L == 8 else BLUE, stroke_width=9)
            bars.add(bar)
            bars.add(txt(name, size=30, color=bar.get_color()
                         ).move_to([-5.0 + L * 0.62 + 0.35, y, 0]))
        self.play(LaggedStart(*[Create(b) for b in bars[::2]], lag_ratio=0.2), run_time=1.0)
        self.play(LaggedStart(*[FadeIn(bars[i]) for i in (1, 3, 5)], lag_ratio=0.15),
                  run_time=0.8)

        f1 = txt("3 + 4 = 7", size=40, color=CHALK).move_to([3.6, 1.2, 0])
        f2 = txt("7 < 8", size=46, color=RED).move_to([3.6, 0.25, 0])
        f3 = txt("✗ 摆不成三角形", size=36, color=RED).move_to([3.6, -0.75, 0])
        f4 = txt("两根短棒加起来，还够不到最长的那根", size=26, color=DIM).move_to([0, -2.2, 0])
        self.play(Write(f1), run_time=0.6)
        self.play(Write(f2), run_time=0.6)
        self.play(FadeIn(f3, shift=UP * 0.1), run_time=0.6)
        self.play(FadeIn(f4), run_time=0.6)
        self.finish_section()

        # ---------- 5. 判断方法 ----------
        self.section(5, "只看最短的两条边")
        self.play(FadeOut(bars), FadeOut(f1), FadeOut(f2), FadeOut(f3), FadeOut(f4),
                  run_time=0.6)

        r1 = txt("任意两边之和 > 第三边", size=40, color=GOLD).move_to([0, 1.6, 0])
        r2 = txt("任意两边之差 < 第三边", size=40, color=GOLD).move_to([0, 0.55, 0])
        self.play(Write(r1), run_time=0.9)
        self.play(Write(r2), run_time=0.9)

        g1 = txt("判断时只看最短的两条边：", size=30, color=DIM).move_to([0, -0.6, 0])
        g2 = txt("它们的和大于最长边，就能围成", size=32, color=GREEN).move_to([0, -1.4, 0])
        self.play(FadeIn(g1), run_time=0.5)
        self.play(FadeIn(g2, shift=UP * 0.1), run_time=0.6)
        self.finish_section()

        # ---------- 6. 两句口诀 ----------
        self.section(6, "内角和 180°，两边之和大于第三边")
        self.play(FadeOut(r1), FadeOut(r2), FadeOut(g1), FadeOut(g2), run_time=0.6)

        big1 = txt("内角和 = 180°", size=54, color=GOLD).move_to([0, 1.4, 0])
        big2 = txt("两边之和 > 第三边", size=54, color=GREEN).move_to([0, 0.15, 0])
        self.play(Write(big1), run_time=0.9)
        self.play(Write(big2), run_time=0.9)

        fin = txt("三角形最基本的两个性质", size=32, color=DIM).move_to([0, -1.2, 0])
        self.play(FadeIn(fin, shift=UP * 0.1), run_time=0.6)
        self.finish_section()

        self.play(FadeOut(big1), FadeOut(big2), FadeOut(fin), run_time=0.6)
