# -*- coding: utf-8 -*-
"""函数性质：单调性看区间，奇偶性看对称，周期性看重复。"""

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


def rtxt(s: str, y: float, size: int = 30, color: str = CHALK,
         width: float = 6.1, x: float = 3.55) -> Text:
    m = txt(s, size=size, color=color)
    if m.width > width:
        m.scale_to_fit_width(width)
    m.move_to([x, y, 0])
    return m


def mini_axes(cx: float, cy: float, xr, yr, xlen: float = 2.6, ylen: float = 2.2) -> Axes:
    ax = Axes(x_range=xr, y_range=yr, x_length=xlen, y_length=ylen,
              tips=False, color=DIM,
              axis_config={"stroke_width": 2})
    ax.move_to([cx, cy, 0])
    return ax


class HanshuXingzhiScene(NarratedScene):
    lesson = "hanshu-xingzhi"

    def construct(self):
        # ---------- 0. 上升还是下降 ----------
        self.section(0, "上升还是下降")
        a1 = mini_axes(-5.2, 0.15, [-1.5, 1.5, 1], [-1.5, 1.5, 1])
        c1 = a1.plot(lambda x: x ** 3, x_range=[-1.02, 1.02], color=GREEN, stroke_width=3)
        l1 = txt("越走越高", size=22, color=GREEN).move_to([-5.2, -1.45, 0])
        self.play(Create(a1), run_time=0.6)
        self.play(Create(c1), run_time=0.8)
        self.play(FadeIn(l1), run_time=0.4)

        a2 = mini_axes(-2.5, 0.15, [0, 3, 1], [0, 3, 1])
        c2 = a2.plot(lambda x: 1 / x, x_range=[0.45, 2.7], color=ORANGE, stroke_width=3)
        l2 = txt("越走越低", size=22, color=ORANGE).move_to([-2.5, -1.45, 0])
        self.play(Create(a2), run_time=0.6)
        self.play(Create(c2), run_time=0.8)
        self.play(FadeIn(l2), run_time=0.4)

        r1 = rtxt("看图像，先看往哪走", 1.45, 30)
        r2 = rtxt("从左往右，上升还是下降", 0.5, 31, GOLD)
        r3 = rtxt("这就是单调性", -0.55, 34, GREEN)
        r4 = rtxt("还要看它是否左右对称", -1.6, 27, DIM)
        for m in (r1, r2, r3, r4):
            self.play(Write(m), run_time=0.5)
        self.finish_section()

        # ---------- 1. 单调性的定义 ----------
        self.section(1, "单调性的定义")
        self.play(FadeOut(a1), FadeOut(c1), FadeOut(l1), FadeOut(a2), FadeOut(c2),
                  FadeOut(l2), FadeOut(r1), FadeOut(r2), FadeOut(r3),
                  FadeOut(r4), run_time=0.5)

        ax = mini_axes(-4.0, 0.0, [-1, 3, 1], [-1, 4, 1], xlen=4.2, ylen=3.0)
        curve = ax.plot(lambda x: x ** 2, x_range=[-0.4, 1.9], color=GOLD, stroke_width=3.4)
        self.play(Create(ax), run_time=0.7)
        self.play(Create(curve), run_time=1.0)

        x1, x2 = 0.5, 1.5
        p1 = Dot(ax.c2p(x1, x1 ** 2), radius=0.1, color=BLUE)
        p2 = Dot(ax.c2p(x2, x2 ** 2), radius=0.1, color=RED)
        self.play(FadeIn(p1), FadeIn(p2), run_time=0.5)

        d1 = DashedLine(ax.c2p(x1, 0), ax.c2p(x1, x1 ** 2), color=BLUE, stroke_width=2)
        d2 = DashedLine(ax.c2p(x2, 0), ax.c2p(x2, x2 ** 2), color=RED, stroke_width=2)
        self.play(Create(d1), Create(d2), run_time=0.5)

        t1 = txt("x₁", size=26, color=BLUE).move_to(ax.c2p(x1, 0) + DOWN * 0.3)
        t2 = txt("x₂", size=26, color=RED).move_to(ax.c2p(x2, 0) + DOWN * 0.3)
        self.play(FadeIn(t1), FadeIn(t2), run_time=0.4)

        r1 = rtxt("区间上任取 x₁ < x₂", 1.45, 30)
        r2 = rtxt("f(x₁) < f(x₂) 就是递增", 0.5, 30, GREEN)
        r3 = rtxt("f(x₁) > f(x₂) 就是递减", -0.55, 30, ORANGE)
        r4 = rtxt("单调性一定是对某个区间说的", -1.6, 27, DIM)
        for m in (r1, r2, r3, r4):
            self.play(Write(m), run_time=0.5)
        self.finish_section()

        # ---------- 2. 证明单调性 ----------
        self.section(2, "怎么证明单调性")
        self.play(FadeOut(ax), FadeOut(curve), FadeOut(p1), FadeOut(p2), FadeOut(d1),
                  FadeOut(d2), FadeOut(t1), FadeOut(t2),
                  FadeOut(r1), FadeOut(r2), FadeOut(r3), FadeOut(r4), run_time=0.5)

        steps = []
        for i, (name, col) in enumerate([("取值", BLUE), ("作差", GOLD), ("定号", GREEN)]):
            box = RoundedRectangle(corner_radius=0.16, width=1.6, height=0.9,
                                   color=col, stroke_width=2.2,
                                   fill_color=col, fill_opacity=0.14)
            box.move_to([-5.6 + i * 1.75, 0.6, 0])
            t = txt(name, size=28, color=col).move_to(box.get_center())
            steps.append(VGroup(box, t))
        self.play(LaggedStart(*[FadeIn(s, shift=RIGHT * 0.1) for s in steps],
                              lag_ratio=0.25), run_time=1.2)

        ar = Arrow([-4.9, 0.6, 0], [-4.5, 0.6, 0], color=DIM, stroke_width=3, buff=0,
                   max_tip_length_to_length_ratio=0.3)
        ar2 = Arrow([-3.15, 0.6, 0], [-2.75, 0.6, 0], color=DIM, stroke_width=3, buff=0,
                    max_tip_length_to_length_ratio=0.3)
        self.play(Create(ar), Create(ar2), run_time=0.5)

        ex1 = txt("设 x₁ < x₂", size=26).move_to([-4.0, -0.55, 0])
        ex2 = txt("算 f(x₁) − f(x₂)", size=26).move_to([-4.0, -1.25, 0])
        ex3 = txt("看符号：同正则增", size=26, color=GREEN).move_to([-4.0, -1.95, 0])
        self.play(FadeIn(ex1), run_time=0.4)
        self.play(FadeIn(ex2), run_time=0.4)
        self.play(FadeIn(ex3), run_time=0.4)

        r1 = rtxt("证明用定义法，一步步来", 1.45, 29)
        r2 = rtxt("复合函数：同增异减", 0.45, 33, GOLD)
        r3 = rtxt("内外两层同向，整体递增", -0.6, 27)
        r4 = rtxt("一增一减，整体递减", -1.6, 27, DIM)
        for m in (r1, r2, r3, r4):
            self.play(Write(m), run_time=0.5)
        self.finish_section()

        # ---------- 3. 奇函数：关于原点 ----------
        self.section(3, "奇函数：关于原点对称")
        self.play(FadeOut(VGroup(*steps)), FadeOut(ar), FadeOut(ar2), FadeOut(ex1),
                  FadeOut(ex2), FadeOut(ex3), FadeOut(r1), FadeOut(r2), FadeOut(r3),
                  FadeOut(r4), run_time=0.5)

        ax = mini_axes(-4.1, 0.0, [-1.4, 1.4, 1], [-1.6, 1.6, 1], xlen=3.6, ylen=3.0)
        odd = ax.plot(lambda x: x ** 3, x_range=[-1.15, 1.15], color=GOLD, stroke_width=3.2)
        self.play(Create(ax), run_time=0.7)
        self.play(Create(odd), run_time=1.0)

        o = Dot(ax.c2p(0, 0), radius=0.1, color=RED)
        self.play(FadeIn(o), run_time=0.4)
        ang = Arc(radius=0.75, start_angle=0.2, angle=-2.2, color=RED, stroke_width=2.4,
                  arc_center=ax.c2p(0, 0))
        self.play(Create(ang), run_time=0.8)

        lab = txt("转 180° 重合", size=24, color=RED).move_to([-4.1, -1.6, 0])
        self.play(FadeIn(lab), run_time=0.5)

        r1 = rtxt("f(−x) = −f(x)", 1.45, 36, GOLD)
        r2 = rtxt("图像绕原点转 180° 不变", 0.5, 29, RED)
        r3 = rtxt("零点处有定义，则 f(0) = 0", -0.55, 27)
        r4 = rtxt("例：y = x³，y = 1/x", -1.6, 26, DIM)
        for m in (r1, r2, r3, r4):
            self.play(Write(m), run_time=0.5)
        self.finish_section()

        # ---------- 4. 偶函数：关于 y 轴 ----------
        self.section(4, "偶函数：关于 y 轴对称")
        self.play(FadeOut(ax), FadeOut(odd), FadeOut(o), FadeOut(ang), FadeOut(lab),
                  FadeOut(r1), FadeOut(r2), FadeOut(r3), FadeOut(r4), run_time=0.5)

        ax = mini_axes(-4.1, 0.0, [-1.6, 1.6, 1], [-0.4, 2.4, 1], xlen=3.6, ylen=3.0)
        even = ax.plot(lambda x: x ** 2, x_range=[-1.4, 1.4], color=GREEN, stroke_width=3.2)
        self.play(Create(ax), run_time=0.7)
        self.play(Create(even), run_time=1.0)

        axis = DashedLine(ax.c2p(0, -0.4), ax.c2p(0, 2.2), color=BLUE, stroke_width=2.2)
        self.play(Create(axis), run_time=0.6)
        m1 = Dot(ax.c2p(-1, 1), radius=0.1, color=RED)
        m2 = Dot(ax.c2p(1, 1), radius=0.1, color=RED)
        self.play(FadeIn(m1), FadeIn(m2), run_time=0.5)
        mirror = DoubleArrow(ax.c2p(-1, 1.22), ax.c2p(1, 1.22), color=RED,
                             stroke_width=2, buff=0,
                             max_tip_length_to_length_ratio=0.12)
        self.play(Create(mirror), run_time=0.6)

        r1 = rtxt("f(−x) = f(x)", 1.45, 36, GOLD)
        r2 = rtxt("图像关于 y 轴左右对称", 0.5, 29, GREEN)
        r3 = rtxt("先看定义域是否关于原点对称", -0.55, 27)
        r4 = rtxt("不对称，就直接非奇非偶", -1.6, 27, RED)
        for m in (r1, r2, r3, r4):
            self.play(Write(m), run_time=0.5)
        self.finish_section()

        # ---------- 5. 周期性 ----------
        self.section(5, "周期性：隔一段就重复")
        self.play(FadeOut(ax), FadeOut(even), FadeOut(axis), FadeOut(m1), FadeOut(m2),
                  FadeOut(mirror), FadeOut(r1), FadeOut(r2), FadeOut(r3),
                  FadeOut(r4), run_time=0.5)

        wave = VMobject(color=GOLD, stroke_width=3.2)
        xs = np.linspace(-6.3, -1.1, 260)
        pts = [np.array([x, 0.35 + 0.62 * np.sin(2 * np.pi * (x + 6.3) / 1.9), 0]) for x in xs]
        wave.set_points_smoothly(pts)
        self.play(Create(wave), run_time=1.4)

        base = Line([-6.3, -0.55, 0], [-1.1, -0.55, 0], color=DIM, stroke_width=2)
        self.play(Create(base), run_time=0.5)

        marks = VGroup()
        for k in range(3):
            x = -6.3 + k * 1.9
            ln = DashedLine([x, -0.55, 0], [x, 1.2, 0], color=BLUE, stroke_width=2)
            marks.add(ln)
            self.play(Create(ln), run_time=0.4)
        tlab = txt("每 T 重复一次", size=26, color=BLUE).move_to([-3.7, -1.35, 0])
        self.play(FadeIn(tlab), run_time=0.5)

        r1 = rtxt("f(x + T) = f(x)", 1.45, 34, GOLD)
        r2 = rtxt("T 是非零常数，叫周期", 0.5, 29)
        r3 = rtxt("最小的正周期，叫最小正周期", -0.55, 27)
        r4 = rtxt("常函数有周期，但没有最小正周期", -1.6, 26, DIM)
        for m in (r1, r2, r3, r4):
            self.play(Write(m), run_time=0.5)
        self.finish_section()

        # ---------- 6. 口诀 ----------
        self.section(6, "记一句话")
        self.play(FadeOut(wave), FadeOut(base), FadeOut(tlab), FadeOut(marks),
                  FadeOut(r1), FadeOut(r2), FadeOut(r3), FadeOut(r4), run_time=0.5)

        k1 = txt("奇原点，偶 y 轴", size=54, color=GOLD).move_to([0, 1.05, 0])
        k2 = txt("单调性，说清在哪个区间", size=32, color=CHALK).move_to([0, -0.1, 0])
        k3 = txt("周期性，找到重复的间隔", size=32, color=GREEN).move_to([0, -1.15, 0])
        self.play(Write(k1), run_time=0.9)
        self.play(Write(k2), run_time=0.7)
        self.play(Write(k3), run_time=0.7)
        self.finish_section()

        self.play(FadeOut(k1), FadeOut(k2), FadeOut(k3), run_time=0.6)