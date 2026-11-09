# -*- coding: utf-8 -*-
"""不等式的性质：同加同减不变号，乘负要变号。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


def rtxt(s: str, y: float, size: int = 30, color: str = CHALK,
         width: float = 6.1, x: float = 3.55) -> Text:
    m = txt(s, size=size, color=color)
    if m.width > width:
        m.scale_to_fit_width(width)
    m.move_to([x, y, 0])
    return m


class BudengshiXingzhiScene(NarratedScene):
    lesson = "budengshi-xingzhi"

    def construct(self):
        # ---------- 0. 跷跷板 ----------
        self.section(0, "跷跷板上的不等式")
        beam = Line([-6.2, 0.2, 0], [-1.5, -0.5, 0], color=CHALK, stroke_width=7)
        fulcrum = Polygon([-4.35, -1.25, 0], [-3.4, -1.25, 0], [-3.88, -0.35, 0],
                          stroke_color=GOLD, stroke_width=2.6,
                          fill_color=GOLD, fill_opacity=0.2)
        self.play(Create(beam), run_time=0.7)
        self.play(Create(fulcrum), run_time=0.6)

        w1 = RoundedRectangle(corner_radius=0.08, width=0.7, height=0.55,
                              color=BLUE, stroke_width=2,
                              fill_color=BLUE, fill_opacity=0.5).move_to([-5.55, 0.35, 0])
        w2 = RoundedRectangle(corner_radius=0.08, width=0.9, height=0.72,
                              color=ORANGE, stroke_width=2,
                              fill_color=ORANGE, fill_opacity=0.5).move_to([-2.1, -0.25, 0])
        self.play(FadeIn(w1, shift=DOWN * 0.2), FadeIn(w2, shift=DOWN * 0.2), run_time=0.7)

        r1 = rtxt("一边重，一边轻", 1.45, 30)
        r2 = rtxt("两边再加一样的重量", 0.5, 31, GOLD)
        r3 = rtxt("谁重谁轻，不会变", -0.55, 34, GREEN)
        r4 = rtxt("不等式，也是这个道理", -1.55, 27, DIM)
        for m in (r1, r2, r3, r4):
            self.play(Write(m), run_time=0.5)
        self.finish_section()

        # ---------- 1. 比大小就是看差 ----------
        self.section(1, "比大小，就是看差")
        self.play(FadeOut(beam), FadeOut(fulcrum), FadeOut(w1), FadeOut(w2),
                  FadeOut(r1), FadeOut(r2), FadeOut(r3), FadeOut(r4), run_time=0.5)

        nl = NumberLine(x_range=[-1, 4, 1], length=6.0, color=DIM)
        nl.move_to([-3.6, -0.25, 0])
        self.play(Create(nl), run_time=1.0)

        ticks = VGroup(*[
            txt(str(i), size=19, color=DIM).move_to(nl.n2p(i) + DOWN * 0.34)
            for i in range(-1, 5)
        ])
        self.play(FadeIn(ticks), run_time=0.5)

        db = Dot(nl.n2p(1) + UP * 0.28, radius=0.12, color=BLUE)
        da = Dot(nl.n2p(3) + UP * 0.28, radius=0.12, color=GOLD)
        self.play(FadeIn(db), FadeIn(da), run_time=0.5)

        lb = txt("b", size=28, color=BLUE).move_to(nl.n2p(1) + UP * 0.75)
        la = txt("a", size=28, color=GOLD).move_to(nl.n2p(3) + UP * 0.75)
        self.play(FadeIn(lb), FadeIn(la), run_time=0.4)

        seg = Line(nl.n2p(1) + DOWN * 0.75, nl.n2p(3) + DOWN * 0.75,
                   color=GREEN, stroke_width=6)
        self.play(Create(seg), run_time=0.7)
        diff = txt("a − b > 0", size=30, color=GREEN).move_to([-3.6, -1.8, 0])
        self.play(FadeIn(diff), run_time=0.5)

        r1 = rtxt("比较两个数，最稳的是看差", 1.4, 29)
        r2 = rtxt("a − b > 0 ⇔ a > b", 0.45, 34, GOLD)
        r3 = rtxt("差等于 0，两个数相等", -0.55, 28)
        r4 = rtxt("差小于 0，大小反过来", -1.55, 28, DIM)
        for m in (r1, r2, r3, r4):
            self.play(Write(m), run_time=0.5)
        self.finish_section()

        # ---------- 2. 两边同加同减 ----------
        self.section(2, "两边同加同减，方向不变")
        self.play(FadeOut(nl), FadeOut(ticks), FadeOut(db), FadeOut(da), FadeOut(lb), FadeOut(la),
                  FadeOut(seg), FadeOut(diff),
                  FadeOut(r1), FadeOut(r2), FadeOut(r3), FadeOut(r4), run_time=0.5)

        s1 = txt("a > b", size=44, color=GOLD).move_to([-4.2, 1.25, 0])
        s2 = txt("两边同加 c", size=28, color=DIM).move_to([-4.2, 0.35, 0])
        s3 = txt("a + c > b + c", size=44, color=GREEN).move_to([-4.2, -0.6, 0])
        s4 = txt("方向不变", size=26, color=DIM).move_to([-4.2, -1.5, 0])
        self.play(Write(s1), run_time=0.7)
        self.play(FadeIn(s2), run_time=0.5)
        self.play(Write(s3), run_time=0.7)
        self.play(FadeIn(s4), run_time=0.4)

        r1 = rtxt("两边同加同减一个数", 1.4, 29)
        r2 = rtxt("不等号方向不变", 0.4, 36, GOLD)
        r3 = rtxt("a ± c > b ± c", -0.6, 30)
        r4 = rtxt("就像天平两边加同样的砝码", -1.55, 26, DIM)
        for m in (r1, r2, r3, r4):
            self.play(Write(m), run_time=0.5)
        self.finish_section()

        # ---------- 3. 乘正数不变号 ----------
        self.section(3, "乘正数，不变号")
        self.play(FadeOut(s1), FadeOut(s2), FadeOut(s3), FadeOut(s4),
                  FadeOut(r1), FadeOut(r2), FadeOut(r3), FadeOut(r4), run_time=0.5)

        t1 = txt("3 > 2", size=46, color=GOLD).move_to([-4.2, 1.25, 0])
        t2 = txt("× 5", size=32, color=BLUE).move_to([-4.2, 0.35, 0])
        t3 = txt("15 > 10", size=46, color=GREEN).move_to([-4.2, -0.6, 0])
        t4 = txt("方向没变", size=26, color=DIM).move_to([-4.2, -1.5, 0])
        self.play(Write(t1), run_time=0.6)
        self.play(FadeIn(t2), run_time=0.5)
        self.play(Write(t3), run_time=0.6)
        self.play(FadeIn(t4), run_time=0.4)

        r1 = rtxt("两边同乘或同除正数", 1.4, 29)
        r2 = rtxt("方向也不变", 0.4, 36, GOLD)
        r3 = rtxt("a > b，c > 0 ⇒ ac > bc", -0.6, 29)
        r4 = rtxt("三大于二，乘五还是大于", -1.55, 26, DIM)
        for m in (r1, r2, r3, r4):
            self.play(Write(m), run_time=0.5)
        self.finish_section()

        # ---------- 4. 乘负数要变号 ----------
        self.section(4, "乘负数，要变号")
        self.play(FadeOut(t1), FadeOut(t2), FadeOut(t3), FadeOut(t4),
                  FadeOut(r1), FadeOut(r2), FadeOut(r3), FadeOut(r4), run_time=0.5)

        u1 = txt("3 > 2", size=46, color=GOLD).move_to([-4.2, 1.25, 0])
        u2 = txt("× (−1)", size=32, color=RED).move_to([-4.2, 0.35, 0])
        u3 = txt("−3 < −2", size=46, color=RED).move_to([-4.2, -0.6, 0])
        u4 = txt("方向反了", size=28, color=RED).move_to([-4.2, -1.55, 0])
        self.play(Write(u1), run_time=0.6)
        self.play(FadeIn(u2), run_time=0.5)
        self.play(Write(u3), run_time=0.6)
        self.play(FadeIn(u4, shift=UP * 0.1), run_time=0.5)

        r1 = rtxt("两边同乘或同除负数", 1.4, 29)
        r2 = rtxt("不等号必须反过来", 0.35, 34, RED)
        r3 = rtxt("a > b，c < 0 ⇒ ac < bc", -0.65, 29)
        r4 = rtxt("这是最容易错的一步", -1.6, 27, DIM)
        for m in (r1, r2, r3, r4):
            self.play(Write(m), run_time=0.5)
        self.finish_section()

        # ---------- 5. 同向可加，正数可乘 ----------
        self.section(5, "同向可加，正数可乘")
        self.play(FadeOut(u1), FadeOut(u2), FadeOut(u3), FadeOut(u4),
                  FadeOut(r1), FadeOut(r2), FadeOut(r3), FadeOut(r4), run_time=0.5)

        v1 = txt("a > b", size=36, color=CHALK).move_to([-4.3, 1.45, 0])
        v2 = txt("c > d", size=36, color=CHALK).move_to([-4.3, 0.7, 0])
        bar = Line([-5.5, 0.15, 0], [-3.1, 0.15, 0], color=DIM, stroke_width=2)
        v3 = txt("a + c > b + d", size=40, color=GOLD).move_to([-4.3, -0.55, 0])
        v4 = txt("同向可加", size=26, color=GREEN).move_to([-4.3, -1.5, 0])
        self.play(Write(v1), Write(v2), run_time=0.7)
        self.play(Create(bar), run_time=0.4)
        self.play(Write(v3), run_time=0.7)
        self.play(FadeIn(v4), run_time=0.4)

        r1 = rtxt("两个同向不等式，可以相加", 1.4, 28)
        r2 = rtxt("而且都是正数，才能相乘", 0.45, 28)
        r3 = rtxt("a > b > 0，c > d > 0 ⇒ ac > bd", -0.6, 25)
        r4 = rtxt("但不能直接相减、随便相除", -1.6, 27, RED)
        for m in (r1, r2, r3, r4):
            self.play(Write(m), run_time=0.5)
        self.finish_section()

        # ---------- 6. 口诀 ----------
        self.section(6, "记一句话")
        self.play(FadeOut(v1), FadeOut(v2), FadeOut(bar), FadeOut(v3), FadeOut(v4),
                  FadeOut(r1), FadeOut(r2), FadeOut(r3), FadeOut(r4), run_time=0.5)

        k1 = txt("乘负要变号", size=54, color=GOLD).move_to([0, 1.15, 0])
        k2 = txt("同加同减、乘正数，都不变号", size=30, color=CHALK)
        k2.move_to([0, 0.0, 0])
        k3 = txt("变形前，先问正还是负", size=30, color=GREEN)
        k3.move_to([0, -1.15, 0])
        self.play(Write(k1), run_time=0.8)
        self.play(Write(k2), run_time=0.8)
        self.play(Write(k3), run_time=0.8)
        self.finish_section()

        self.play(FadeOut(k1), FadeOut(k2), FadeOut(k3), run_time=0.6)