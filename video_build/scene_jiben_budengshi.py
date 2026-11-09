# -*- coding: utf-8 -*-
"""基本不等式：和定积最大，积定和最小。"""

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


class JibenBudengshiScene(NarratedScene):
    lesson = "jiben-budengshi"

    def construct(self):
        # ---------- 0. 周长固定的菜地 ----------
        self.section(0, "周长固定的菜地")
        rect = Rectangle(width=4.2, height=2.2, color=ORANGE, stroke_width=3,
                         fill_color=GREEN, fill_opacity=0.08).move_to([-4.2, 0.05, 0])
        self.play(Create(rect), run_time=0.9)

        la = txt("长 a", size=26, color=ORANGE).move_to([-4.2, -1.55, 0])
        lb = txt("宽 b", size=26, color=ORANGE).move_to([-5.9, 1.42, 0])
        self.play(FadeIn(la), FadeIn(lb), run_time=0.5)

        fence = VGroup(*[
            Line([x, -1.1, 0], [x, -1.32, 0], color=DIM, stroke_width=1.5)
            for x in [-5.6, -5.0, -4.4, -3.8, -3.2, -2.6]
        ])
        self.play(LaggedStart(*[Create(f) for f in fence], lag_ratio=0.1), run_time=0.7)

        r1 = rtxt("篱笆长度固定，也就是周长固定", 1.4, 28)
        r2 = rtxt("怎么围，面积最大？", 0.45, 34, GOLD)
        r3 = rtxt("围成正方形时，面积最大", -0.55, 32, GREEN)
        r4 = rtxt("这就是基本不等式要回答的问题", -1.55, 26, DIM)
        for m in (r1, r2, r3, r4):
            self.play(Write(m), run_time=0.5)
        self.finish_section()

        # ---------- 1. 从平方非负推出来 ----------
        self.section(1, "从平方非负推出来")
        self.play(FadeOut(rect), FadeOut(la), FadeOut(lb), FadeOut(fence),
                  FadeOut(r1), FadeOut(r2), FadeOut(r3), FadeOut(r4), run_time=0.5)

        s1 = txt("(√a − √b)² ≥ 0", size=34, color=CHALK).move_to([-3.9, 1.45, 0])
        s2 = txt("a − 2√ab + b ≥ 0", size=30, color=CHALK).move_to([-3.9, 0.45, 0])
        s3 = txt("a + b ≥ 2√ab", size=38, color=GOLD).move_to([-3.9, -0.7, 0])
        s4 = txt("平方一定非负，展开再移项", size=24, color=DIM).move_to([-3.9, -1.65, 0])
        self.play(Write(s1), run_time=0.7)
        self.play(Write(s2), run_time=0.7)
        self.play(Write(s3), run_time=0.7)
        self.play(FadeIn(s4), run_time=0.5)

        r1 = rtxt("对正数 a、b", 1.45, 29)
        r2 = rtxt("(√a − √b)² 一定 ≥ 0", 0.5, 31, CHALK)
        r3 = rtxt("展开、移项", -0.55, 29)
        r4 = rtxt("就得到基本不等式", -1.55, 29, GOLD)
        for m in (r1, r2, r3, r4):
            self.play(Write(m), run_time=0.5)
        self.finish_section()

        # ---------- 2. 基本不等式的样子 ----------
        self.section(2, "基本不等式的样子")
        self.play(FadeOut(s1), FadeOut(s2), FadeOut(s3), FadeOut(s4),
                  FadeOut(r1), FadeOut(r2), FadeOut(r3), FadeOut(r4), run_time=0.5)

        big = txt("a + b ≥ 2√ab", size=50, color=GOLD).move_to([-4.0, 0.65, 0])
        self.play(Write(big), run_time=0.9)

        small = txt("(a + b) / 2 ≥ √ab", size=32, color=CHALK).move_to([-4.0, -0.75, 0])
        self.play(Write(small), run_time=0.7)

        note = txt("两个正数的和，不小于积的平方根的两倍", size=24, color=DIM)
        note.move_to([-4.0, -1.7, 0])
        self.play(FadeIn(note), run_time=0.5)

        r1 = rtxt("a > 0，b > 0", 1.45, 30, GREEN)
        r2 = rtxt("a + b ≥ 2√ab", 0.4, 38, GOLD)
        r3 = rtxt("算术平均数 ≥ 几何平均数", -0.65, 28)
        r4 = rtxt("两边除以 2，就是下面这一行", -1.6, 26, DIM)
        for m in (r1, r2, r3, r4):
            self.play(Write(m), run_time=0.5)
        self.finish_section()

        # ---------- 3. 等号什么时候成立 ----------
        self.section(3, "等号什么时候成立")
        self.play(FadeOut(big), FadeOut(small), FadeOut(note),
                  FadeOut(r1), FadeOut(r2), FadeOut(r3), FadeOut(r4), run_time=0.5)

        sq = Rectangle(width=2.6, height=2.6, color=GREEN, stroke_width=3,
                       fill_color=GREEN, fill_opacity=0.12).move_to([-4.2, 0.05, 0])
        self.play(Create(sq), run_time=0.9)

        e1 = txt("a", size=28, color=GREEN).move_to([-4.2, -1.55, 0])
        e2 = txt("b", size=28, color=GREEN).move_to([-5.75, 0.05, 0])
        self.play(FadeIn(e1), FadeIn(e2), run_time=0.4)

        eq = txt("a = b", size=40, color=GOLD).move_to([-4.2, -2.2, 0])
        self.play(Write(eq), run_time=0.6)

        r1 = rtxt("当且仅当 a = b", 1.4, 32, GOLD)
        r2 = rtxt("等号才成立", 0.45, 34, GREEN)
        r3 = rtxt("根号 a 减根号 b 等于零", -0.55, 28)
        r4 = rtxt("这时和最小、积最大", -1.55, 28, CHALK)
        for m in (r1, r2, r3, r4):
            self.play(Write(m), run_time=0.5)
        self.finish_section()

        # ---------- 4. 一正二定三相等 ----------
        self.section(4, "一正、二定、三相等")
        self.play(FadeOut(sq), FadeOut(e1), FadeOut(e2), FadeOut(eq),
                  FadeOut(r1), FadeOut(r2), FadeOut(r3), FadeOut(r4), run_time=0.5)

        chips = VGroup()
        for i, (s, c) in enumerate([("一正", GREEN), ("二定", GOLD), ("三相等", BLUE)]):
            b = RoundedRectangle(corner_radius=0.14, width=2.5, height=0.9,
                                 color=c, stroke_width=2.2,
                                 fill_color=c, fill_opacity=0.14)
            b.move_to([-4.7, 1.35 - i * 1.35, 0])
            t = txt(s, size=32, color=c).move_to(b.get_center())
            chips.add(VGroup(b, t))
        self.play(LaggedStart(*[FadeIn(c, shift=RIGHT * 0.15) for c in chips],
                              lag_ratio=0.2), run_time=1.2)

        r1 = rtxt("一正：两个数都是正数", 1.35, 29, GREEN)
        r2 = rtxt("二定：和或积能凑出定值", 0.0, 29, GOLD)
        r3 = rtxt("三相等：等号真的能取到", -1.35, 29, BLUE)
        for m in (r1, r2, r3):
            self.play(Write(m), run_time=0.55)
        self.finish_section()

        # ---------- 5. 两个模型 ----------
        self.section(5, "求最值的两个模型")
        self.play(FadeOut(chips), FadeOut(r1), FadeOut(r2), FadeOut(r3), run_time=0.5)

        p1 = RoundedRectangle(corner_radius=0.14, width=5.0, height=1.15,
                              color=GOLD, stroke_width=2.2,
                              fill_color=GOLD, fill_opacity=0.1).move_to([-4.1, 1.15, 0])
        p2 = RoundedRectangle(corner_radius=0.14, width=5.0, height=1.15,
                              color=BLUE, stroke_width=2.2,
                              fill_color=BLUE, fill_opacity=0.1).move_to([-4.1, -0.55, 0])
        self.play(Create(p1), run_time=0.6)
        self.play(Create(p2), run_time=0.6)

        q1 = txt("a + b = 10  ⇒  ab ≤ 25", size=30, color=GOLD).move_to(p1.get_center())
        q2 = txt("ab = 16  ⇒  a + b ≥ 8", size=30, color=BLUE).move_to(p2.get_center())
        self.play(FadeIn(q1), run_time=0.6)
        self.play(FadeIn(q2), run_time=0.6)

        q3 = txt("两个都在 a = b 时取到", size=26, color=GREEN).move_to([-4.1, -1.65, 0])
        self.play(FadeIn(q3), run_time=0.5)

        r1 = rtxt("和一定，积有最大值", 1.3, 32, GOLD)
        r2 = rtxt("积一定，和有最小值", 0.15, 32, BLUE)
        r3 = rtxt("等号都在 a = b 时取到", -0.9, 28, GREEN)
        r4 = rtxt("没凑出定值，算出的不是最值", -1.75, 25, RED)
        for m in (r1, r2, r3, r4):
            self.play(Write(m), run_time=0.5)
        self.finish_section()

        # ---------- 6. 口诀 ----------
        self.section(6, "记一句话")
        self.play(FadeOut(p1), FadeOut(p2), FadeOut(q1), FadeOut(q2), FadeOut(q3),
                  FadeOut(r1), FadeOut(r2), FadeOut(r3), FadeOut(r4), run_time=0.5)

        k1 = txt("和定积最大", size=50, color=GOLD).move_to([0, 1.25, 0])
        k2 = txt("积定和最小", size=50, color=GREEN).move_to([0, 0.2, 0])
        self.play(Write(k1), run_time=0.7)
        self.play(Write(k2), run_time=0.7)

        k3 = txt("一正、二定、三相等", size=32, color=CHALK)
        k3.move_to([0, -1.1, 0])
        self.play(FadeIn(k3, shift=UP * 0.1), run_time=0.6)
        self.finish_section()

        self.play(FadeOut(k1), FadeOut(k2), FadeOut(k3), run_time=0.6)