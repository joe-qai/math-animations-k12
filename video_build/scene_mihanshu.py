# -*- coding: utf-8 -*-
"""幂函数：系数为 1，底数是 x，指数是常数。"""

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


def axes_at(cx: float, cy: float, xr, yr, xlen: float = 4.6, ylen: float = 3.0) -> Axes:
    ax = Axes(x_range=xr, y_range=yr, x_length=xlen, y_length=ylen,
              tips=False, color=DIM, axis_config={"stroke_width": 2})
    ax.move_to([cx, cy, 0])
    return ax


class MihanshuScene(NarratedScene):
    lesson = "mihanshu"

    def construct(self):
        # ---------- 0. 面积与体积 ----------
        self.section(0, "从面积和体积说起")
        sq = Rectangle(width=2.0, height=2.0, color=GOLD, stroke_width=3,
                       fill_color=GOLD, fill_opacity=0.12).move_to([-5.0, 0.55, 0])
        self.play(Create(sq), run_time=0.8)
        sx = txt("x", size=28, color=GOLD).move_to([-5.0, -0.62, 0])
        sl = txt("面积 = x²", size=28, color=GOLD).move_to([-5.0, -1.35, 0])
        self.play(FadeIn(sx), FadeIn(sl), run_time=0.5)

        cube = VGroup(
            Polygon([-2.9, -0.05, 0], [-1.9, -0.05, 0], [-1.9, 0.95, 0], [-2.9, 0.95, 0],
                    stroke_color=BLUE, stroke_width=2.6, fill_color=BLUE, fill_opacity=0.12),
            Polygon([-1.9, -0.05, 0], [-1.55, 0.3, 0], [-1.55, 1.3, 0], [-1.9, 0.95, 0],
                    stroke_color=BLUE, stroke_width=2.6, fill_color=BLUE, fill_opacity=0.12),
            Polygon([-2.9, 0.95, 0], [-1.9, 0.95, 0], [-1.55, 1.3, 0], [-2.55, 1.3, 0],
                    stroke_color=BLUE, stroke_width=2.6, fill_color=BLUE, fill_opacity=0.12),
        )
        self.play(Create(cube), run_time=1.0)
        cl = txt("体积 = x³", size=28, color=BLUE).move_to([-2.25, -0.75, 0])
        self.play(FadeIn(cl), run_time=0.5)

        r1 = rtxt("边长是 x，面积就是 x²", 1.45, 30, GOLD)
        r2 = rtxt("棱长是 x，体积就是 x³", 0.5, 30, BLUE)
        r3 = rtxt("它们都是 x 的若干次方", -0.55, 29)
        r4 = rtxt("这类函数，就叫幂函数", -1.6, 32, GREEN)
        for m in (r1, r2, r3, r4):
            self.play(Write(m), run_time=0.5)
        self.finish_section()

        # ---------- 1. 定义 ----------
        self.section(1, "幂函数的定义")
        self.play(FadeOut(sq), FadeOut(sx), FadeOut(sl), FadeOut(cube), FadeOut(cl),
                  FadeOut(r1), FadeOut(r2), FadeOut(r3), FadeOut(r4), run_time=0.5)

        big = txt("y = xᵅ", size=76, color=GOLD).move_to([-4.2, 0.9, 0])
        self.play(Write(big), run_time=0.9)
        note = txt("α 是常数", size=28, color=DIM).move_to([-4.2, -0.1, 0])
        self.play(FadeIn(note), run_time=0.5)

        chips = []
        for i, s in enumerate(["系数是 1", "底数是 x", "指数是常数"]):
            box = RoundedRectangle(corner_radius=0.12, width=1.86, height=0.62,
                                   color=GREEN, stroke_width=2,
                                   fill_color=GREEN, fill_opacity=0.12)
            box.move_to([-5.75 + i * 2.15, -1.15, 0])
            t = txt(s, size=23, color=GREEN).move_to(box.get_center())
            chips.append(VGroup(box, t))
        self.play(LaggedStart(*[FadeIn(c) for c in chips], lag_ratio=0.2), run_time=1.0)

        r1 = rtxt("系数必须是 1", 1.45, 30, GREEN)
        r2 = rtxt("y = 2x² 不是幂函数", 0.5, 29, RED)
        r3 = rtxt("y = x² + 1 也不是", -0.55, 29, RED)
        r4 = rtxt("α 可以是整数，也可以是分数", -1.6, 27, DIM)
        for m in (r1, r2, r3, r4):
            self.play(Write(m), run_time=0.5)
        self.finish_section()

        # ---------- 2. 五个常见图像 ----------
        self.section(2, "五个常见图像")
        self.play(FadeOut(big), FadeOut(note), FadeOut(VGroup(*chips)),
                  FadeOut(r1), FadeOut(r2), FadeOut(r3), FadeOut(r4), run_time=0.5)

        ax = axes_at(-4.0, 0.35, [0, 2.3, 1], [0, 2.5, 1], xlen=4.8, ylen=3.2)
        self.play(Create(ax), run_time=0.8)

        c1 = ax.plot(lambda x: x, x_range=[0, 2.1], color=GREEN, stroke_width=2.8)
        c2 = ax.plot(lambda x: x ** 2, x_range=[0, 1.5], color=GOLD, stroke_width=2.8)
        c3 = ax.plot(lambda x: x ** 3, x_range=[0, 1.3], color=ORANGE, stroke_width=2.8)
        c4 = ax.plot(lambda x: x ** 0.5, x_range=[0, 2.1], color=BLUE, stroke_width=2.8)
        c5 = ax.plot(lambda x: 1 / x, x_range=[0.42, 2.1], color=RED, stroke_width=2.8)
        for c in (c1, c2, c3, c4, c5):
            self.play(Create(c), run_time=0.5)

        legend = VGroup(
            txt("x", size=20, color=GREEN).move_to([-6.0, -1.65, 0]),
            txt("x²", size=20, color=GOLD).move_to([-4.7, -1.65, 0]),
            txt("x³", size=20, color=ORANGE).move_to([-3.4, -1.65, 0]),
            txt("√x", size=20, color=BLUE).move_to([-2.1, -1.65, 0]),
            txt("1/x", size=20, color=RED).move_to([-0.7, -1.65, 0]),
        )
        self.play(FadeIn(legend), run_time=0.6)

        r1 = rtxt("五个最基本的幂函数", 1.45, 30)
        r2 = rtxt("x、x²、x³、√x、1/x", 0.5, 30, GOLD)
        r3 = rtxt("定义域不一样，形状差别很大", -0.55, 27, DIM)
        r4 = rtxt("但它们有一个共同点", -1.6, 27, GREEN)
        for m in (r1, r2, r3, r4):
            self.play(Write(m), run_time=0.5)
        self.finish_section()

        # ---------- 3. α > 0 ----------
        self.section(3, "α > 0：过原点，往上走")
        self.play(FadeOut(VGroup(c1, c4, c5)), FadeOut(legend),
                  FadeOut(r1), FadeOut(r2), FadeOut(r3), FadeOut(r4), run_time=0.5)

        o = Dot(ax.c2p(0, 0), radius=0.1, color=CHALK)
        p1 = Dot(ax.c2p(1, 1), radius=0.1, color=CHALK)
        self.play(FadeIn(o), FadeIn(p1), run_time=0.5)
        lo = txt("原点", size=20, color=CHALK).move_to(ax.c2p(0.35, 0) + DOWN * 0.32)
        lp = txt("(1, 1)", size=20, color=CHALK).move_to(ax.c2p(1, 1) + RIGHT * 0.5 + DOWN * 0.45)
        self.play(FadeIn(lo), FadeIn(lp), run_time=0.4)

        h1 = DashedLine(ax.c2p(1, 0), ax.c2p(1, 1), color=DIM, stroke_width=2)
        self.play(Create(h1), run_time=0.5)

        up = Arrow([-1.55, 0.55, 0], [-1.55, 1.85, 0], color=GREEN, stroke_width=3, buff=0,
                   max_tip_length_to_length_ratio=0.25)
        self.play(Create(up), run_time=0.6)

        r1 = rtxt("α > 0，图像过原点", 1.45, 30, GREEN)
        r2 = rtxt("也一定过 (1, 1)", 0.5, 30, GOLD)
        r3 = rtxt("在 (0, +∞) 上单调递增", -0.55, 28)
        r4 = rtxt("α 越大，x > 1 时涨得越陡", -1.6, 27, DIM)
        for m in (r1, r2, r3, r4):
            self.play(Write(m), run_time=0.5)
        self.finish_section()

        # ---------- 4. α < 0 ----------
        self.section(4, "α < 0：不过原点，往下走")
        self.play(FadeOut(c2), FadeOut(c3), FadeOut(o), FadeOut(p1), FadeOut(lo),
                  FadeOut(lp), FadeOut(h1), FadeOut(up),
                  FadeOut(r1), FadeOut(r2), FadeOut(r3), FadeOut(r4), run_time=0.5)

        c5 = ax.plot(lambda x: 1 / x, x_range=[0.42, 2.1], color=RED, stroke_width=3.2)
        self.play(Create(c5), run_time=1.0)

        down = Arrow([-1.15, 2.05, 0], [-1.15, 0.75, 0], color=BLUE, stroke_width=3, buff=0,
                     max_tip_length_to_length_ratio=0.25)
        self.play(Create(down), run_time=0.6)

        near1 = txt("越来越贴近 y 轴", size=22, color=DIM).move_to([-4.75, 1.78, 0])
        near2 = txt("越来越贴近 x 轴", size=22, color=DIM).move_to([-2.45, 0.95, 0])
        self.play(FadeIn(near1), FadeIn(near2), run_time=0.5)

        r1 = rtxt("α < 0，图像不过原点", 1.45, 30, RED)
        r2 = rtxt("x = 0 没有定义", 0.5, 29)
        r3 = rtxt("在 (0, +∞) 上单调递减", -0.55, 28, BLUE)
        r4 = rtxt("以两条坐标轴为渐近线", -1.6, 27, DIM)
        for m in (r1, r2, r3, r4):
            self.play(Write(m), run_time=0.5)
        self.finish_section()

        # ---------- 5. 都过 (1, 1) ----------
        self.section(5, "都过 (1, 1)，怎么比大小")
        self.play(FadeOut(c5), FadeOut(down), FadeOut(near1), FadeOut(near2),
                  FadeOut(r1), FadeOut(r2), FadeOut(r3), FadeOut(r4), run_time=0.5)

        ax2 = axes_at(-4.0, 0.35, [0, 2.3, 1], [0, 2.5, 1], xlen=4.8, ylen=3.2)
        self.play(FadeOut(ax), run_time=0.3)
        self.play(Create(ax2), run_time=0.5)

        curves = [
            ax2.plot(lambda x: x, x_range=[0, 2.1], color=GREEN, stroke_width=2.6),
            ax2.plot(lambda x: x ** 2, x_range=[0, 1.5], color=GOLD, stroke_width=2.6),
            ax2.plot(lambda x: x ** 3, x_range=[0, 1.3], color=ORANGE, stroke_width=2.6),
            ax2.plot(lambda x: x ** 0.5, x_range=[0, 2.1], color=BLUE, stroke_width=2.6),
            ax2.plot(lambda x: 1 / x, x_range=[0.42, 2.1], color=RED, stroke_width=2.6),
        ]
        self.play(LaggedStart(*[Create(c) for c in curves], lag_ratio=0.15), run_time=1.4)

        dot = Dot(ax2.c2p(1, 1), radius=0.13, color=CHALK)
        self.play(FadeIn(dot), run_time=0.5)
        pl = txt("(1, 1)", size=22, color=CHALK).move_to(ax2.c2p(1, 1) + RIGHT * 0.55 + DOWN * 0.5)
        self.play(FadeIn(pl), run_time=0.4)

        r1 = rtxt("所有幂函数都过 (1, 1)", 1.45, 30, GOLD)
        r2 = rtxt("同指数：用单调性比底数", 0.5, 29, GREEN)
        r3 = rtxt("不同底、不同指数：先找 1", -0.55, 28, BLUE)
        r4 = rtxt("(1, 1) 就是最常用的分界点", -1.6, 26, DIM)
        for m in (r1, r2, r3, r4):
            self.play(Write(m), run_time=0.5)
        self.finish_section()

        # ---------- 6. 口诀 ----------
        self.section(6, "记一句话")
        self.play(FadeOut(ax2), FadeOut(VGroup(*curves)), FadeOut(dot), FadeOut(pl),
                  FadeOut(r1), FadeOut(r2), FadeOut(r3), FadeOut(r4), run_time=0.5)

        k1 = txt("y = xᵅ", size=58, color=GOLD).move_to([0, 1.0, 0])
        k2 = txt("系数是 1，底数是 x，指数是常数", size=30, color=CHALK).move_to([0, -0.1, 0])
        k3 = txt("α 正过原点，α 负不过原点", size=30, color=GREEN).move_to([0, -1.15, 0])
        self.play(Write(k1), run_time=0.9)
        self.play(Write(k2), run_time=0.7)
        self.play(Write(k3), run_time=0.7)
        self.finish_section()

        self.play(FadeOut(k1), FadeOut(k2), FadeOut(k3), run_time=0.6)