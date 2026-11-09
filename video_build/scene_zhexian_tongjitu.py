# -*- coding: utf-8 -*-
"""折线统计图：点看数量，线看变化。五年级下册「折线统计图」。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403

DAYS = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
DATA = [18, 20, 22, 19, 21, 23, 24]
LO, HI = 16.0, 26.0
X0, X1 = -5.9, -0.6
Y0, Y1 = -1.9, 2.3
STEP = (X1 - X0) / 7
XS = [X0 + STEP * (i + 0.5) for i in range(7)]


def ypos(v: float, y0: float = Y0, y1: float = Y1,
         lo: float = LO, hi: float = HI) -> float:
    return y0 + (v - lo) / (hi - lo) * (y1 - y0)


def axis_pair(x0: float, y0: float, x1: float, y1: float) -> VGroup:
    return VGroup(
        Arrow([x0, y0, 0], [x1, y0, 0], buff=0, color=DIM,
              stroke_width=2, tip_length=0.13),
        Arrow([x0, y0, 0], [x0, y1, 0], buff=0, color=DIM,
              stroke_width=2, tip_length=0.13),
    )


def bar_chart(xs: list[float], ys: list[float], base: float,
              width: float = 0.42, color: str = BLUE) -> VGroup:
    bars = VGroup()
    for x, y in zip(xs, ys):
        bars.add(Rectangle(width=width, height=max(0.02, y - base),
                           stroke_width=1.2, stroke_color=color,
                           fill_color=color, fill_opacity=0.35
                           ).move_to([x, (base + y) / 2, 0]))
    return bars


def dots(xs: list[float], ys: list[float], color: str = GOLD) -> VGroup:
    return VGroup(*[Dot([x, y, 0], radius=0.06, color=color)
                    for x, y in zip(xs, ys)])


def polyline(xs: list[float], ys: list[float],
             color: str = GOLD, width: float = 3) -> VGroup:
    return VGroup(*[
        Line([xs[i], ys[i], 0], [xs[i + 1], ys[i + 1], 0],
             color=color, stroke_width=width)
        for i in range(len(xs) - 1)
    ])


class ZhexianTongjituScene(NarratedScene):
    lesson = "zhexian-tongjitu"

    def construct(self):
        ys = [ypos(v) for v in DATA]
        axes = axis_pair(X0, Y0, X1, Y0 + 4.2)
        ylab = txt("气温 / ℃", size=22, color=DIM).move_to([X0 - 0.02, Y1 + 0.25, 0])

        def xlabels(y: float = Y0 - 0.28, size: int = 18) -> VGroup:
            return VGroup(*[
                txt(d, size=size, color=DIM).move_to([xs_i, y, 0])
                for d, xs_i in zip(DAYS, XS)
            ])

        # ---------- 0. 条形图看不出趋势 ----------
        self.section(0, "条形图能比多少，看不出趋势")
        self.play(Create(axes), FadeIn(ylab), run_time=0.9)
        bars = bar_chart(XS, ys, Y0)
        self.play(LaggedStart(*[GrowFromEdge(b, DOWN) for b in bars], lag_ratio=0.10),
                  run_time=1.4)
        xlab = xlabels()
        self.play(LaggedStart(*[FadeIn(t) for t in xlab], lag_ratio=0.05),
                  run_time=0.7)

        h1 = txt("条形图：每天多少度", size=34, color=BLUE).move_to([3.6, 1.55, 0])
        h2 = txt("变化趋势呢？", size=36, color=GOLD).move_to([3.6, 0.5, 0])
        h3 = txt("这时候用折线统计图", size=32, color=GREEN).move_to([3.6, -0.55, 0])
        self.play(Write(h1), run_time=0.7)
        self.play(FadeIn(h2, shift=UP * 0.1), run_time=0.6)
        self.play(FadeIn(h3), run_time=0.6)
        self.finish_section()

        # ---------- 1. 点表示数量，线连接 ----------
        self.section(1, "点表示数量，线段连起来")
        self.play(FadeOut(h1), FadeOut(h2), FadeOut(h3), run_time=0.4)

        ds = dots(XS, ys)
        self.play(LaggedStart(*[FadeIn(d, scale=0.6) for d in ds], lag_ratio=0.10),
                  run_time=1.2)
        pl = polyline(XS, ys)
        self.play(LaggedStart(*[Create(s) for s in pl], lag_ratio=0.15), run_time=1.2)

        a1 = txt("点的高低 = 数量多少", size=34, color=GOLD).move_to([3.6, 1.55, 0])
        a2 = txt("线的陡缓 = 变化快慢", size=34, color=GREEN).move_to([3.6, 0.5, 0])
        a3 = txt("连起来，趋势就出来了", size=30, color=DIM).move_to([3.6, -0.55, 0])
        self.play(Write(a1), run_time=0.7)
        self.play(Write(a2), run_time=0.7)
        self.play(FadeIn(a3), run_time=0.6)
        self.finish_section()

        # ---------- 2. 画法：描点、连线 ----------
        self.section(2, "先描点，再按顺序连线")
        self.play(FadeOut(a1), FadeOut(a2), FadeOut(a3), run_time=0.4)

        # 重新演示一遍：清掉线，只留坐标轴
        self.play(FadeOut(bars), FadeOut(ds), FadeOut(pl),
                  FadeOut(axes), FadeOut(ylab), FadeOut(xlab), run_time=0.6)

        s1 = txt("① 画横轴、纵轴", size=34, color=CHALK).move_to([3.6, 1.9, 0])
        s2 = txt("② 标好日期和温度", size=34, color=CHALK).move_to([3.6, 1.0, 0])
        s3 = txt("③ 根据数据描点", size=34, color=GOLD).move_to([3.6, 0.1, 0])
        s4 = txt("④ 按顺序连起来", size=34, color=GREEN).move_to([3.6, -0.8, 0])
        self.play(FadeIn(s1), run_time=0.5)

        axes2 = axis_pair(X0, Y0, X1, Y0 + 4.2)
        ylab2 = txt("气温 / ℃", size=22, color=DIM).move_to([X0 - 0.02, Y1 + 0.25, 0])
        self.play(Create(axes2), FadeIn(ylab2), run_time=0.8)
        self.play(FadeIn(s2), run_time=0.4)
        xlab2 = xlabels()
        self.play(LaggedStart(*[FadeIn(t) for t in xlab2], lag_ratio=0.05),
                  run_time=0.6)

        ds2 = dots(XS, ys)
        self.play(FadeIn(s3), run_time=0.4)
        self.play(LaggedStart(*[FadeIn(d, scale=0.6) for d in ds2], lag_ratio=0.12),
                  run_time=1.2)
        self.play(FadeIn(s4), run_time=0.4)
        pl2 = polyline(XS, ys)
        self.play(LaggedStart(*[Create(s) for s in pl2], lag_ratio=0.12), run_time=1.2)
        self.finish_section()

        # ---------- 3. 上升、下降、平稳 ----------
        self.section(3, "线往上、往下、平着，各说明什么")
        self.play(FadeOut(s1), FadeOut(s2), FadeOut(s3), FadeOut(s4),
                  FadeOut(axes2), FadeOut(ylab2), FadeOut(xlab2),
                  FadeOut(ds2), FadeOut(pl2), run_time=0.6)

        up = VGroup(
            Line([-5.4, 0.7, 0], [-4.2, 1.5, 0], color=GREEN, stroke_width=4),
            Arrow([-4.4, 1.36, 0], [-4.2, 1.5, 0], buff=0, color=GREEN,
                  stroke_width=4, tip_length=0.18),
        )
        flat = VGroup(
            Line([-5.4, 0.0, 0], [-4.2, 0.0, 0], color=GOLD, stroke_width=4),
            Arrow([-4.4, 0.0, 0], [-4.2, 0.0, 0], buff=0, color=GOLD,
                  stroke_width=4, tip_length=0.18),
        )
        down = VGroup(
            Line([-5.4, -0.7, 0], [-4.2, -1.5, 0], color=RED, stroke_width=4),
            Arrow([-4.4, -1.36, 0], [-4.2, -1.5, 0], buff=0, color=RED,
                  stroke_width=4, tip_length=0.18),
        )
        self.play(Create(up), run_time=0.6)
        self.play(Create(flat), run_time=0.6)
        self.play(Create(down), run_time=0.6)

        u1 = txt("线往上：数量在增加", size=34, color=GREEN).move_to([0.55, 1.15, 0])
        u2 = txt("线平着：变化不大", size=34, color=GOLD).move_to([0.55, 0.0, 0])
        u3 = txt("线往下：数量在减少", size=34, color=RED).move_to([0.55, -1.15, 0])
        self.play(Write(u1), run_time=0.6)
        self.play(Write(u2), run_time=0.6)
        self.play(Write(u3), run_time=0.6)

        tip = txt("陡一点变化快，缓一点变化慢", size=28, color=DIM).move_to([0, -2.35, 0])
        self.play(FadeIn(tip), run_time=0.5)
        self.finish_section()

        # ---------- 4. 一周气温实例 ----------
        self.section(4, "看一周气温的走势")
        self.play(FadeOut(up), FadeOut(flat), FadeOut(down),
                  FadeOut(u1), FadeOut(u2), FadeOut(u3), FadeOut(tip), run_time=0.5)

        # 重新画出完整折线，并标出升、降
        axes4 = axis_pair(X0, Y0, X1, Y0 + 4.2)
        ylab4 = txt("气温 / ℃", size=22, color=DIM).move_to([X0 - 0.02, Y1 + 0.25, 0])
        xlab4 = xlabels()
        ds4 = dots(XS, ys)
        pl4 = polyline(XS, ys)
        self.play(Create(axes4), FadeIn(ylab4), run_time=0.6)
        self.play(LaggedStart(*[FadeIn(t) for t in xlab4], lag_ratio=0.05),
                  run_time=0.5)
        self.play(LaggedStart(*[FadeIn(d, scale=0.6) for d in ds4], lag_ratio=0.10),
                  run_time=0.8)
        self.play(LaggedStart(*[Create(s) for s in pl4], lag_ratio=0.10), run_time=0.9)

        w1 = txt("周一到周三：缓慢上升", size=32, color=GREEN).move_to([3.5, 1.6, 0])
        w2 = txt("周四：明显下降", size=32, color=RED).move_to([3.5, 0.6, 0])
        w3 = txt("周五以后：继续回升", size=32, color=GREEN).move_to([3.5, -0.4, 0])
        self.play(Write(w1), run_time=0.7)
        self.play(Write(w2), run_time=0.7)
        self.play(Write(w3), run_time=0.7)
        self.finish_section()

        # ---------- 5. 条形图比多少，折线图看变化 ----------
        self.section(5, "条形图比多少，折线图看变化")
        self.play(FadeOut(axes4), FadeOut(ylab4), FadeOut(xlab4),
                  FadeOut(ds4), FadeOut(pl4),
                  FadeOut(w1), FadeOut(w2), FadeOut(w3), run_time=0.6)

        # 小坐标轴 + 条形
        bx0, bx1 = -5.7, -2.6
        by0, by1 = -1.6, 1.3
        bstep = (bx1 - bx0) / 7
        bxs = [bx0 + bstep * (i + 0.5) for i in range(7)]
        bys = [by0 + (v - LO) / (HI - LO) * (by1 - by0) for v in DATA]
        ba = axis_pair(bx0, by0, bx1, by0 + 2.9)
        bb = bar_chart(bxs, bys, by0, width=0.24)
        cap1 = txt("条形图：比多少", size=28, color=BLUE).move_to([-4.15, -2.15, 0])
        self.play(Create(ba), run_time=0.6)
        self.play(LaggedStart(*[GrowFromEdge(b, DOWN) for b in bb], lag_ratio=0.08),
                  run_time=1.0)
        self.play(FadeIn(cap1), run_time=0.5)

        # 小坐标轴 + 折线
        lx0, lx1 = 0.2, 3.3
        lstep = (lx1 - lx0) / 7
        lxs = [lx0 + lstep * (i + 0.5) for i in range(7)]
        lys = [by0 + (v - LO) / (HI - LO) * (by1 - by0) for v in DATA]
        la = axis_pair(lx0, by0, lx1, by0 + 2.9)
        lp = polyline(lxs, lys, color=GREEN, width=2.6)
        ld = dots(lxs, lys, color=GREEN)
        cap2 = txt("折线图：看变化", size=28, color=GREEN).move_to([1.75, -2.15, 0])
        self.play(Create(la), run_time=0.6)
        self.play(LaggedStart(*[FadeIn(d, scale=0.6) for d in ld], lag_ratio=0.08),
                  run_time=0.8)
        self.play(LaggedStart(*[Create(s) for s in lp], lag_ratio=0.10), run_time=0.9)
        self.play(FadeIn(cap2), run_time=0.5)

        t1 = txt("同一组数据", size=30, color=DIM).move_to([5.5, -0.4, 0])
        self.play(FadeIn(t1), run_time=0.5)
        self.finish_section()

        # ---------- 6. 三步口诀 ----------
        self.section(6, "描点、连线、读趋势")
        self.play(FadeOut(ba), FadeOut(bb), FadeOut(cap1), FadeOut(la), FadeOut(lp),
                  FadeOut(ld), FadeOut(cap2), FadeOut(t1), run_time=0.6)

        k1 = label_box("描点", size=36, color=GOLD).move_to([-3.9, 1.3, 0])
        k2 = label_box("连线", size=36, color=BLUE).move_to([0, 1.3, 0])
        k3 = label_box("读趋势", size=36, color=GREEN).move_to([3.9, 1.3, 0])
        self.play(LaggedStart(*[FadeIn(m, shift=UP * 0.1) for m in (k1, k2, k3)],
                              lag_ratio=0.2), run_time=1.2)

        big1 = txt("点看数量，线看变化", size=44, color=CHALK).move_to([0, -0.1, 0])
        big2 = txt("比大小用条形图，看趋势用折线图", size=36, color=GOLD).move_to([0, -1.2, 0])
        self.play(Write(big1), run_time=0.9)
        self.play(Write(big2), run_time=0.9)

        fin = txt("折线统计图，看的是变化", size=28, color=DIM).move_to([0, -2.3, 0])
        self.play(FadeIn(fin, shift=UP * 0.1), run_time=0.6)
        self.finish_section()

        self.play(FadeOut(k1), FadeOut(k2), FadeOut(k3),
                  FadeOut(big1), FadeOut(big2), FadeOut(fin), run_time=0.6)