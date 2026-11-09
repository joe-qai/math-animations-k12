# -*- coding: utf-8 -*-
"""三角函数图像与性质：五点作图，周期 2π。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403

PI = np.pi


def rtxt(s: str, y: float, size: int = 30, color: str = CHALK,
         width: float = 6.1, x: float = 3.55) -> Text:
    m = txt(s, size=size, color=color)
    if m.width > width:
        m.scale_to_fit_width(width)
    m.move_to([x, y, 0])
    return m


def axes_at(cx: float, cy: float, xr, yr, xlen: float = 4.9, ylen: float = 2.9) -> Axes:
    ax = Axes(x_range=xr, y_range=yr, x_length=xlen, y_length=ylen,
              tips=False, color=DIM, axis_config={"stroke_width": 2})
    ax.move_to([cx, cy, 0])
    return ax


def legend(entries, y: float = -1.95, x0: float = -6.2) -> VGroup:
    g = VGroup()
    x = x0
    for color, s in entries:
        d = Dot([x, y, 0], radius=0.07, color=color)
        t = txt(s, size=21, color=color).next_to(d, RIGHT, buff=0.12)
        g.add(d, t)
        x = t.get_right()[0] + 0.5
    return g


class SanjiaoTuxiangScene(NarratedScene):
    lesson = "sanjiao-tuxiang"

    def construct(self):
        # ---------- 0. 从单位圆到波浪线 ----------
        self.section(0, "从单位圆到波浪线")
        c = np.array([-5.45, 0.75, 0])
        r = 0.95
        wheel = Circle(radius=r, color=BLUE, stroke_width=2.4).move_to(c)
        bar = Line(c + LEFT * r, c + RIGHT * r, color=DIM, stroke_width=2)
        self.play(Create(wheel), Create(bar), run_time=0.8)

        ang = np.deg2rad(55)
        p = c + r * np.array([np.cos(ang), np.sin(ang), 0])
        rad = Line(c, p, color=GOLD, stroke_width=2.2)
        dotp = Dot(p, radius=0.1, color=RED)
        drop = DashedLine(p, [p[0], c[1], 0], color=GREEN, stroke_width=2)
        self.play(Create(rad), FadeIn(dotp), Create(drop), run_time=0.8)

        ax = axes_at(-2.45, 0.15, [0, 6.4, 1], [-1.3, 1.3, 1], xlen=3.2, ylen=1.9)
        self.play(Create(ax), run_time=0.7)
        wave = ax.plot(lambda x: np.sin(x), x_range=[0, 6.28], color=GOLD, stroke_width=2.8)
        self.play(Create(wave), run_time=1.4)

        arrow = Arrow([-4.35, 0.35, 0], [-3.75, 0.35, 0], color=DIM, stroke_width=2.4,
                      buff=0, max_tip_length_to_length_ratio=0.3)
        self.play(Create(arrow), run_time=0.5)

        r1 = rtxt("点在圆上匀速转动", 1.45, 28)
        r2 = rtxt("纵坐标随时间上下起伏", 0.5, 28, GREEN)
        r3 = rtxt("把纵坐标画出来，就是波浪线", -0.55, 26, GOLD)
        r4 = rtxt("这条线叫正弦曲线", -1.6, 29, BLUE)
        for m in (r1, r2, r3, r4):
            self.play(Write(m), run_time=0.5)
        self.finish_section()

        # ---------- 1. 正弦曲线 ----------
        self.section(1, "正弦曲线")
        self.play(FadeOut(wheel), FadeOut(bar), FadeOut(rad), FadeOut(dotp), FadeOut(drop),
                  FadeOut(ax), FadeOut(wave), FadeOut(arrow),
                  FadeOut(r1), FadeOut(r2), FadeOut(r3), FadeOut(r4), run_time=0.5)

        ax = axes_at(-4.1, 0.15, [-0.5, 6.8, 1], [-1.45, 1.45, 1], xlen=4.9, ylen=2.9)
        self.play(Create(ax), run_time=0.8)
        wave = ax.plot(lambda x: np.sin(x), x_range=[-0.45, 6.6], color=GOLD, stroke_width=3)
        self.play(Create(wave), run_time=1.6)

        top = DashedLine(ax.c2p(-0.35, 1), ax.c2p(6.6, 1), color=GREEN, stroke_width=1.8)
        bot = DashedLine(ax.c2p(-0.35, -1), ax.c2p(6.6, -1), color=GREEN, stroke_width=1.8)
        self.play(Create(top), Create(bot), run_time=0.6)
        t1 = txt("1", size=22, color=GREEN).move_to([-0.5, 1.15, 0])
        t2 = txt("−1", size=22, color=GREEN).move_to([-0.56, -0.85, 0])
        self.play(FadeIn(t1), FadeIn(t2), run_time=0.4)

        r1 = rtxt("y = sinx，定义域 R", 1.45, 29, GOLD)
        r2 = rtxt("值域 [−1, 1]", 0.5, 31)
        r3 = rtxt("最小正周期 2π", -0.55, 31, GREEN)
        r4 = rtxt("奇函数，关于原点对称", -1.6, 26, DIM)
        for m in (r1, r2, r3, r4):
            self.play(Write(m), run_time=0.5)
        self.finish_section()

        # ---------- 2. 余弦曲线 ----------
        self.section(2, "余弦曲线")
        self.play(FadeOut(ax), FadeOut(wave), FadeOut(top), FadeOut(bot), FadeOut(t1),
                  FadeOut(t2),
                  FadeOut(r1), FadeOut(r2), FadeOut(r3), FadeOut(r4), run_time=0.5)

        ax = axes_at(-4.1, 0.15, [-0.5, 6.8, 1], [-1.45, 1.45, 1], xlen=4.9, ylen=2.9)
        self.play(Create(ax), run_time=0.8)
        sw = ax.plot(lambda x: np.sin(x), x_range=[-0.45, 6.6], color=DIM, stroke_width=2.4)
        cw = ax.plot(lambda x: np.cos(x), x_range=[-0.45, 6.6], color=GOLD, stroke_width=3)
        self.play(Create(sw), run_time=0.7)
        self.play(Create(cw), run_time=1.2)

        ar = Arrow(ax.c2p(PI / 2, 1.32), ax.c2p(0.0, 1.32), color=GREEN, stroke_width=2.6,
                   buff=0, max_tip_length_to_length_ratio=0.25)
        at = txt("左移 π/2", size=22, color=GREEN).move_to(ax.c2p(PI / 4, 1.64))
        self.play(Create(ar), FadeIn(at), run_time=0.6)

        lg = legend([(GOLD, "y = cosx"), (DIM, "y = sinx")], y=-1.95, x0=-5.6)
        self.play(FadeIn(lg), run_time=0.5)

        r1 = rtxt("y = cosx，值域 [−1, 1]", 1.45, 28, GOLD)
        r2 = rtxt("最小正周期也是 2π", 0.5, 29)
        r3 = rtxt("偶函数，关于 y 轴对称", -0.55, 28, GREEN)
        r4 = rtxt("cosx = sin(x + π/2)", -1.6, 27, DIM)
        for m in (r1, r2, r3, r4):
            self.play(Write(m), run_time=0.5)
        self.finish_section()

        # ---------- 3. 五点作图法 ----------
        self.section(3, "五点作图法")
        self.play(FadeOut(ax), FadeOut(sw), FadeOut(cw), FadeOut(ar), FadeOut(at),
                  FadeOut(lg),
                  FadeOut(r1), FadeOut(r2), FadeOut(r3), FadeOut(r4), run_time=0.5)

        ax = axes_at(-4.1, 0.2, [-0.5, 6.8, 1], [-1.45, 1.45, 1], xlen=4.9, ylen=2.8)
        self.play(Create(ax), run_time=0.8)
        wave = ax.plot(lambda x: np.sin(x), x_range=[0, 6.283], color=GOLD, stroke_width=3)
        self.play(Create(wave), run_time=1.2)

        pts = [(0, 0), (PI / 2, 1), (PI, 0), (3 * PI / 2, -1), (2 * PI, 0)]
        labels = ["0", "π/2", "π", "3π/2", "2π"]
        dots = VGroup()
        labs = VGroup()
        for (x, y), s in zip(pts, labels):
            d = Dot(ax.c2p(x, y), radius=0.1, color=RED)
            dots.add(d)
            lb = txt(s, size=20, color=BLUE).move_to(ax.c2p(x, 0) + DOWN * 0.42)
            labs.add(lb)
        self.play(FadeIn(dots), run_time=0.9)
        self.play(FadeIn(labs), run_time=0.8)

        r1 = rtxt("一个周期取五个关键点", 1.45, 28)
        r2 = rtxt("零点 → 最高点 → 零点", 0.5, 27, GOLD)
        r3 = rtxt("再 → 最低点 → 零点", -0.55, 27, GREEN)
        r4 = rtxt("用光滑曲线连接，不要画折线", -1.6, 26, DIM)
        for m in (r1, r2, r3, r4):
            self.play(Write(m), run_time=0.5)
        self.finish_section()

        # ---------- 4. 周期与最值 ----------
        self.section(4, "周期与最值")
        self.play(FadeOut(ax), FadeOut(wave), FadeOut(dots), FadeOut(labs),
                  FadeOut(r1), FadeOut(r2), FadeOut(r3), FadeOut(r4), run_time=0.5)

        ax = axes_at(-4.1, 0.35, [-0.5, 6.8, 1], [-2.4, 2.4, 1], xlen=4.9, ylen=3.0)
        self.play(Create(ax), run_time=0.8)
        w1 = ax.plot(lambda x: np.sin(x), x_range=[-0.45, 6.6], color=GOLD, stroke_width=3)
        w2 = ax.plot(lambda x: 2 * np.sin(x), x_range=[-0.45, 6.6], color=BLUE, stroke_width=3)
        self.play(Create(w1), run_time=0.8)
        self.play(Create(w2), run_time=0.9)

        lg = legend([(BLUE, "y = 2sinx"), (GOLD, "y = sinx")], y=-2.0, x0=-5.7)
        self.play(FadeIn(lg), run_time=0.5)

        r1 = rtxt("最大值 1，最小值 −1", 1.45, 28)
        r2 = rtxt("A 决定振幅，值域 [−|A|, |A|]", 0.5, 26, BLUE)
        r3 = rtxt("T = 2π / |ω|", -0.55, 31, GREEN)
        r4 = rtxt("ω 越大，曲线越密", -1.6, 27, DIM)
        for m in (r1, r2, r3, r4):
            self.play(Write(m), run_time=0.5)
        self.finish_section()

        # ---------- 5. 单调区间与对称轴 ----------
        self.section(5, "单调区间与对称轴")
        self.play(FadeOut(ax), FadeOut(w1), FadeOut(w2), FadeOut(lg),
                  FadeOut(r1), FadeOut(r2), FadeOut(r3), FadeOut(r4), run_time=0.5)

        ax = axes_at(-4.1, 0.2, [-2.2, 8.0, 1], [-1.45, 1.45, 1], xlen=5.1, ylen=2.8)
        self.play(Create(ax), run_time=0.8)
        full = ax.plot(lambda x: np.sin(x), x_range=[-2.0, 7.8], color=DIM, stroke_width=2.4)
        inc = ax.plot(lambda x: np.sin(x), x_range=[-PI / 2, PI / 2], color=GREEN, stroke_width=6)
        dec = ax.plot(lambda x: np.sin(x), x_range=[PI / 2, 3 * PI / 2], color=RED, stroke_width=6)
        self.play(Create(full), run_time=1.0)
        self.play(Create(inc), run_time=0.8)
        self.play(Create(dec), run_time=0.8)

        sym = DashedLine(ax.c2p(PI / 2, -1.4), ax.c2p(PI / 2, 1.4), color=BLUE, stroke_width=2)
        sl = txt("对称轴", size=21, color=BLUE).move_to(ax.c2p(PI / 2, 1.25) + RIGHT * 0.55)
        self.play(Create(sym), FadeIn(sl), run_time=0.6)

        r1 = rtxt("增区间 [−π/2+2kπ, π/2+2kπ]", 1.45, 24, GREEN)
        r2 = rtxt("减区间 [π/2+2kπ, 3π/2+2kπ]", 0.5, 24, RED)
        r3 = rtxt("对称轴 x = π/2 + kπ", -0.55, 27, BLUE)
        r4 = rtxt("对称中心是 (kπ, 0)", -1.6, 26, DIM)
        for m in (r1, r2, r3, r4):
            self.play(Write(m), run_time=0.5)
        self.finish_section()

        # ---------- 6. 口诀 ----------
        self.section(6, "记一句话")
        self.play(FadeOut(ax), FadeOut(full), FadeOut(inc), FadeOut(dec), FadeOut(sym),
                  FadeOut(sl),
                  FadeOut(r1), FadeOut(r2), FadeOut(r3), FadeOut(r4), run_time=0.5)

        k1 = txt("五点作图，周期 2π", size=52, color=GOLD).move_to([0, 1.0, 0])
        k2 = txt("正弦是奇函数，余弦是偶函数", size=30, color=CHALK).move_to([0, -0.1, 0])
        k3 = txt("振幅看 A，周期看 ω", size=30, color=GREEN).move_to([0, -1.15, 0])
        self.play(Write(k1), run_time=0.9)
        self.play(Write(k2), run_time=0.7)
        self.play(Write(k3), run_time=0.7)
        self.finish_section()

        self.play(FadeOut(k1), FadeOut(k2), FadeOut(k3), run_time=0.6)