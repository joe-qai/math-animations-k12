# -*- coding: utf-8 -*-
"""对数与对数函数：对数就是问指数。"""

import math
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


def ltxt(s: str, y: float, size: int = 30, color: str = CHALK,
         width: float = 5.5, x: float = -4.0) -> Text:
    m = txt(s, size=size, color=color)
    if m.width > width:
        m.scale_to_fit_width(width)
    m.move_to([x, y, 0])
    return m


def legend(entries, y: float = -1.9, x0: float = -6.2) -> VGroup:
    g = VGroup()
    x = x0
    for color, s in entries:
        d = Dot([x, y, 0], radius=0.07, color=color)
        t = txt(s, size=21, color=color).next_to(d, RIGHT, buff=0.12)
        g.add(d, t)
        x = t.get_right()[0] + 0.5
    return g


def axes_at(cx: float, cy: float, xr, yr, xlen: float = 4.6, ylen: float = 3.0) -> Axes:
    ax = Axes(x_range=xr, y_range=yr, x_length=xlen, y_length=ylen,
              tips=False, color=DIM, axis_config={"stroke_width": 2})
    ax.move_to([cx, cy, 0])
    return ax


class DuishuHanshuScene(NarratedScene):
    lesson = "duishu-hanshu"

    def construct(self):
        # ---------- 0. 把指数问题反过来问 ----------
        self.section(0, "把指数问题反过来问")
        eq = txt("2³ = 8", size=58, color=GOLD).move_to([-4.3, 1.55, 0])
        self.play(Write(eq), run_time=0.8)

        ar = Arrow([-4.3, 0.85, 0], [-4.3, 0.25, 0], color=DIM,
                   stroke_width=3, buff=0, max_tip_length_to_length_ratio=0.3)
        self.play(Create(ar), run_time=0.5)

        q = txt("2 的几次方等于 8？", size=31, color=CHALK).move_to([-4.3, -0.2, 0])
        self.play(Write(q), run_time=0.8)

        ans = txt("3", size=70, color=GREEN).move_to([-5.55, -1.35, 0])
        lab = txt("这个 3，就是对数", size=27, color=GREEN).move_to([-2.55, -1.35, 0])
        self.play(FadeIn(ans, scale=0.7), FadeIn(lab), run_time=0.7)

        r1 = rtxt("2 的 3 次方等于 8", 1.45, 29)
        r2 = rtxt("反过来问：2 要乘几次才等于 8", 0.5, 27)
        r3 = rtxt("答案 3，就是对数", -0.55, 32, GREEN)
        r4 = rtxt("记作 log₂8 = 3", -1.6, 30, GOLD)
        for m in (r1, r2, r3, r4):
            self.play(Write(m), run_time=0.5)
        self.finish_section()

        # ---------- 1. 对数的定义 ----------
        self.section(1, "对数的定义")
        self.play(FadeOut(eq), FadeOut(ar), FadeOut(q), FadeOut(ans), FadeOut(lab),
                  FadeOut(r1), FadeOut(r2), FadeOut(r3), FadeOut(r4), run_time=0.5)

        f = txt("aᵇ = N  ⇔  b = logₐN", size=40, color=GOLD)
        if f.width > 5.6:
            f.scale_to_fit_width(5.6)
        f.move_to([-4.0, 1.35, 0])
        self.play(Write(f), run_time=1.0)

        base = txt("a：底数", size=27, color=BLUE).move_to([-5.45, 0.35, 0])
        true = txt("N：真数", size=27, color=GREEN).move_to([-3.05, 0.35, 0])
        self.play(FadeIn(base), FadeIn(true), run_time=0.6)

        n1 = ltxt("真数 N 必须大于 0", -0.65, 28, RED)
        n2 = ltxt("a^(logₐN) = N", -1.55, 30, CHALK)
        n3 = ltxt("logₐaᵇ = b", -2.1, 26, DIM)
        for m in (n1, n2, n3):
            self.play(Write(m), run_time=0.5)

        r1 = rtxt("aᵇ = N  ⇔  b = logₐN", 1.45, 27, GOLD)
        r2 = rtxt("a 是底数，N 是真数", 0.5, 28, BLUE)
        r3 = rtxt("真数必须大于 0", -0.55, 31, RED)
        r4 = rtxt("两个恒等式，互为反运算", -1.6, 26, DIM)
        for m in (r1, r2, r3, r4):
            self.play(Write(m), run_time=0.5)
        self.finish_section()

        # ---------- 2. 三条运算律 ----------
        self.section(2, "三条运算律")
        self.play(FadeOut(f), FadeOut(base), FadeOut(true), FadeOut(n1), FadeOut(n2),
                  FadeOut(n3),
                  FadeOut(r1), FadeOut(r2), FadeOut(r3), FadeOut(r4), run_time=0.5)

        c1 = label_box("logₐ(MN) = logₐM + logₐN", size=24, color=GOLD)
        c1.move_to([-4.0, 1.5, 0])
        c2 = label_box("logₐ(M/N) = logₐM − logₐN", size=24, color=GREEN)
        c2.move_to([-4.0, 0.5, 0])
        c3 = label_box("logₐMⁿ = n · logₐM", size=27, color=BLUE)
        c3.move_to([-4.15, -0.5, 0])
        self.play(FadeIn(c1), run_time=0.7)
        self.play(FadeIn(c2), run_time=0.7)
        self.play(FadeIn(c3), run_time=0.7)

        ex = txt("log₂(4 × 8) = 2 + 3 = 5", size=26, color=CHALK).move_to([-4.15, -1.65, 0])
        self.play(Write(ex), run_time=0.7)

        r1 = rtxt("积的对数 = 对数的和", 1.45, 28, GOLD)
        r2 = rtxt("商的对数 = 对数的差", 0.5, 28, GREEN)
        r3 = rtxt("幂的对数 = 指数乘对数", -0.55, 28, BLUE)
        r4 = rtxt("把乘除降成加减，乘方降成乘法", -1.6, 25, DIM)
        for m in (r1, r2, r3, r4):
            self.play(Write(m), run_time=0.5)
        self.finish_section()

        # ---------- 3. 换底公式 ----------
        self.section(3, "换底公式")
        self.play(FadeOut(c1), FadeOut(c2), FadeOut(c3), FadeOut(ex),
                  FadeOut(r1), FadeOut(r2), FadeOut(r3), FadeOut(r4), run_time=0.5)

        f = txt("logₐb = log_c b / log_c a", size=40, color=GOLD)
        if f.width > 5.7:
            f.scale_to_fit_width(5.7)
        f.move_to([-4.0, 1.25, 0])
        self.play(Write(f), run_time=1.0)

        up = ltxt("分子：真数 b 的对数", 0.25, 27, BLUE)
        dn = ltxt("分母：原底 a 的对数", -0.6, 27, GREEN)
        self.play(Write(up), run_time=0.5)
        self.play(Write(dn), run_time=0.5)

        ex = ltxt("例：log₂3 = lg3 / lg2", -1.6, 28, CHALK)
        self.play(Write(ex), run_time=0.6)

        r1 = rtxt("logₐb = log_c b / log_c a", 1.45, 26, GOLD)
        r2 = rtxt("分子是真数的对数", 0.5, 29, BLUE)
        r3 = rtxt("分母是原底数的对数", -0.55, 29, GREEN)
        r4 = rtxt("推论：logₐb · log_b a = 1", -1.6, 26, DIM)
        for m in (r1, r2, r3, r4):
            self.play(Write(m), run_time=0.5)
        self.finish_section()

        # ---------- 4. 对数函数的图像 ----------
        self.section(4, "对数函数的图像")
        self.play(FadeOut(f), FadeOut(up), FadeOut(dn), FadeOut(ex),
                  FadeOut(r1), FadeOut(r2), FadeOut(r3), FadeOut(r4), run_time=0.5)

        ax = axes_at(-4.15, 0.15, [-0.5, 4.5, 1], [-2.4, 2.4, 1], xlen=4.7, ylen=3.2)
        self.play(Create(ax), run_time=0.8)

        up = ax.plot(lambda x: math.log(x, 2), x_range=[0.2, 4.3], color=GOLD, stroke_width=3.2)
        down = ax.plot(lambda x: math.log(x, 0.5), x_range=[0.2, 4.3], color=BLUE, stroke_width=3.2)
        self.play(Create(up), run_time=1.1)
        self.play(Create(down), run_time=1.1)

        p0 = Dot(ax.c2p(1, 0), radius=0.1, color=RED)
        l0 = txt("(1, 0)", size=22, color=RED).move_to(ax.c2p(1, 0) + RIGHT * 0.72 + DOWN * 0.4)
        self.play(FadeIn(p0), FadeIn(l0), run_time=0.5)

        lg = legend([(GOLD, "y = log₂x"), (BLUE, "y = log₀.₅x")], y=-1.92, x0=-5.9)
        self.play(FadeIn(lg), run_time=0.5)

        r1 = rtxt("y = logₐx，定义域 (0, +∞)", 1.45, 28, GOLD)
        r2 = rtxt("值域 R，恒过 (1, 0)", 0.5, 28)
        r3 = rtxt("y 轴是竖直渐近线", -0.55, 28, GREEN)
        r4 = rtxt("与 y = aˣ 关于 y = x 对称", -1.6, 26, DIM)
        for m in (r1, r2, r3, r4):
            self.play(Write(m), run_time=0.5)
        self.finish_section()

        # ---------- 5. 底数与单调性 ----------
        self.section(5, "底数决定增减")
        self.play(FadeOut(ax), FadeOut(up), FadeOut(down), FadeOut(p0), FadeOut(l0),
                  FadeOut(lg),
                  FadeOut(r1), FadeOut(r2), FadeOut(r3), FadeOut(r4), run_time=0.5)

        ax = axes_at(-4.15, 0.15, [-0.5, 4.5, 1], [-2.2, 2.2, 1], xlen=4.7, ylen=3.0)
        self.play(Create(ax), run_time=0.8)
        up = ax.plot(lambda x: math.log(x, 2), x_range=[0.22, 4.3], color=GOLD, stroke_width=3.2)
        down = ax.plot(lambda x: math.log(x, 0.5), x_range=[0.22, 4.3], color=BLUE, stroke_width=3.2)
        self.play(Create(up), run_time=1.0)
        self.play(Create(down), run_time=1.0)

        a1 = Arrow(ax.c2p(2.4, 0.55), ax.c2p(3.7, 1.3), color=GOLD, stroke_width=3,
                   buff=0, max_tip_length_to_length_ratio=0.24)
        t1 = txt("a > 1 递增", size=23, color=GOLD).move_to([-1.35, 1.9, 0])
        self.play(Create(a1), FadeIn(t1), run_time=0.6)

        a2 = Arrow(ax.c2p(2.4, -0.55), ax.c2p(3.7, -1.3), color=BLUE, stroke_width=3,
                   buff=0, max_tip_length_to_length_ratio=0.24)
        t2 = txt("0 < a < 1 递减", size=23, color=BLUE).move_to([-1.3, 1.35, 0])
        self.play(Create(a2), FadeIn(t2), run_time=0.6)

        r1 = rtxt("a > 1：在 (0, +∞) 上递增", 1.45, 28, GOLD)
        r2 = rtxt("0 < a < 1：在 (0, +∞) 上递减", 0.5, 27, BLUE)
        r3 = rtxt("a > 1 时，底数越大曲线越平缓", -0.55, 25)
        r4 = rtxt("比较大小，先看底数是大于 1 还是小于 1", -1.6, 24, DIM)
        for m in (r1, r2, r3, r4):
            self.play(Write(m), run_time=0.5)
        self.finish_section()

        # ---------- 6. 口诀 ----------
        self.section(6, "记一句话")
        self.play(FadeOut(ax), FadeOut(up), FadeOut(down), FadeOut(a1), FadeOut(t1),
                  FadeOut(a2), FadeOut(t2),
                  FadeOut(r1), FadeOut(r2), FadeOut(r3), FadeOut(r4), run_time=0.5)

        k1 = txt("对数就是问指数", size=54, color=GOLD).move_to([0, 1.0, 0])
        k2 = txt("真数必须大于 0，底数大于 0 且不等于 1", size=29, color=CHALK).move_to([0, -0.1, 0])
        k3 = txt("乘除能拆成加减，加减不能拆", size=30, color=GREEN).move_to([0, -1.15, 0])
        self.play(Write(k1), run_time=0.9)
        self.play(Write(k2), run_time=0.7)
        self.play(Write(k3), run_time=0.7)
        self.finish_section()

        self.play(FadeOut(k1), FadeOut(k2), FadeOut(k3), run_time=0.6)