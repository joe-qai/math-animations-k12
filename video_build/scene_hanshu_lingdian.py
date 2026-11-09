# -*- coding: utf-8 -*-
"""函数的零点：连续且异号，就必有一个零点。"""

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


class HanshuLingdianScene(NarratedScene):
    lesson = "hanshu-lingdian"

    def construct(self):
        # ---------- 0. 穿过 x 轴的地方 ----------
        self.section(0, "图像穿过 x 轴的地方")
        ax = axes_at(-4.0, 0.1, [-1, 4, 1], [-1.4, 3, 1], xlen=5.0, ylen=3.2)
        self.play(Create(ax), run_time=0.8)

        curve = ax.plot(lambda x: (x - 0.7) * (x - 2.9), x_range=[0.14, 3.6],
                        color=GOLD, stroke_width=3.2)
        self.play(Create(curve), run_time=1.4)

        z1 = Dot(ax.c2p(0.7, 0), radius=0.11, color=RED)
        z2 = Dot(ax.c2p(2.9, 0), radius=0.11, color=RED)
        self.play(FadeIn(z1), FadeIn(z2), run_time=0.6)

        l1 = txt("零点", size=24, color=RED).move_to(ax.c2p(0.7, 0) + DOWN * 0.45)
        l2 = txt("零点", size=24, color=RED).move_to(ax.c2p(2.9, 0) + DOWN * 0.45)
        self.play(FadeIn(l1), FadeIn(l2), run_time=0.5)

        r1 = rtxt("曲线从 x 轴下方穿到上方", 1.45, 28)
        r2 = rtxt("穿过去的位置，就是零点", 0.5, 31, GOLD)
        r3 = rtxt("它其实是方程 f(x) = 0 的根", -0.55, 28, GREEN)
        r4 = rtxt("也是图像与 x 轴交点的横坐标", -1.6, 26, DIM)
        for m in (r1, r2, r3, r4):
            self.play(Write(m), run_time=0.5)
        self.finish_section()

        # ---------- 1. 零点是数，不是点 ----------
        self.section(1, "零点是数，不是点")
        self.play(FadeOut(ax), FadeOut(curve), FadeOut(z1), FadeOut(z2),
                  FadeOut(l1), FadeOut(l2),
                  FadeOut(r1), FadeOut(r2), FadeOut(r3), FadeOut(r4), run_time=0.5)

        f = txt("f(x) = x − 3", size=44, color=CHALK).move_to([-4.2, 1.35, 0])
        self.play(Write(f), run_time=0.7)
        eq = txt("x − 3 = 0  ⇒  x = 3", size=38, color=GOLD).move_to([-4.2, 0.35, 0])
        self.play(Write(eq), run_time=0.8)

        good = txt("零点：x = 3", size=34, color=GREEN).move_to([-4.6, -0.85, 0])
        bad = txt("(3, 0)", size=32, color=RED).move_to([-2.7, -0.85, 0])
        self.play(FadeIn(good), FadeIn(bad), run_time=0.5)
        cross = VGroup(
            Line([-3.15, -0.55, 0], [-2.25, -1.15, 0], color=RED, stroke_width=4),
            Line([-3.15, -1.15, 0], [-2.25, -0.55, 0], color=RED, stroke_width=4),
        )
        self.play(Create(cross), run_time=0.6)

        note = txt("(3, 0) 是图像上的点，不是零点", size=24, color=DIM)
        note.move_to([-4.0, -1.75, 0])
        self.play(FadeIn(note), run_time=0.5)

        r1 = rtxt("零点的定义：使 f(x) = 0 的 x", 1.45, 28)
        r2 = rtxt("它是一个数", 0.5, 34, GREEN)
        r3 = rtxt("不是坐标点", -0.55, 32, RED)
        r4 = rtxt("方程有几个实根，就有几个零点", -1.6, 26, DIM)
        for m in (r1, r2, r3, r4):
            self.play(Write(m), run_time=0.5)
        self.finish_section()

        # ---------- 2. 零点存在定理 ----------
        self.section(2, "连续 + 异号，就必有零点")
        self.play(FadeOut(f), FadeOut(eq), FadeOut(good), FadeOut(bad), FadeOut(cross),
                  FadeOut(note), FadeOut(r1), FadeOut(r2), FadeOut(r3),
                  FadeOut(r4), run_time=0.5)

        ax = axes_at(-4.0, 0.1, [0, 4, 1], [-1.6, 2.4, 1], xlen=4.8, ylen=3.2)
        self.play(Create(ax), run_time=0.8)
        curve = ax.plot(lambda x: 0.9 * (x - 1.9), x_range=[0.35, 3.4],
                        color=GOLD, stroke_width=3.2)
        self.play(Create(curve), run_time=1.0)

        pa = Dot(ax.c2p(1, -0.81), radius=0.1, color=BLUE)
        pb = Dot(ax.c2p(3, 0.99), radius=0.1, color=RED)
        self.play(FadeIn(pa), FadeIn(pb), run_time=0.5)

        la = txt("a", size=24, color=BLUE).move_to(ax.c2p(1, 0) + DOWN * 0.42)
        lb = txt("b", size=24, color=RED).move_to(ax.c2p(3, 0) + DOWN * 0.3)
        fa = txt("f(a) < 0", size=22, color=BLUE).move_to(ax.c2p(1, -0.81) + UP * 0.95)
        fb = txt("f(b) > 0", size=22, color=RED).move_to(ax.c2p(3, 0.99) + RIGHT * 0.55 + UP * 0.55)
        self.play(FadeIn(la), FadeIn(lb), run_time=0.4)
        self.play(FadeIn(fa), FadeIn(fb), run_time=0.5)

        ga = DashedLine(ax.c2p(1, 0), ax.c2p(1, -0.81), color=BLUE, stroke_width=2)
        gb = DashedLine(ax.c2p(3, 0), ax.c2p(3, 0.99), color=RED, stroke_width=2)
        self.play(Create(ga), Create(gb), run_time=0.5)

        zp = Dot(ax.c2p(1.9, 0), radius=0.11, color=GREEN)
        self.play(FadeIn(zp), run_time=0.5)
        zl = txt("零点", size=22, color=GREEN).move_to(ax.c2p(1.9, 0) + RIGHT * 0.6 + DOWN * 0.5)
        self.play(FadeIn(zl), run_time=0.4)

        r1 = rtxt("在 [a, b] 上连续不断", 1.45, 29)
        r2 = rtxt("f(a) · f(b) < 0", 0.5, 34, GOLD)
        r3 = rtxt("(a, b) 内至少有一个零点", -0.55, 29, GREEN)
        r4 = rtxt("两个条件，缺一不可", -1.6, 27, DIM)
        for m in (r1, r2, r3, r4):
            self.play(Write(m), run_time=0.5)
        self.finish_section()

        # ---------- 3. 存在不等于唯一 ----------
        self.section(3, "存在，不等于唯一")
        self.play(FadeOut(ax), FadeOut(curve), FadeOut(pa), FadeOut(pb), FadeOut(la),
                  FadeOut(lb), FadeOut(fa), FadeOut(fb), FadeOut(ga), FadeOut(gb),
                  FadeOut(zp), FadeOut(zl),
                  FadeOut(r1), FadeOut(r2), FadeOut(r3), FadeOut(r4), run_time=0.5)

        ax = axes_at(-4.0, 0.1, [0, 4, 1], [-1.2, 1.6, 1], xlen=4.8, ylen=3.0)
        self.play(Create(ax), run_time=0.7)
        w = ax.plot(lambda x: 0.5 * (x - 1.2) * (x - 2.6) * (x - 3.6) / 1.6,
                    x_range=[0.4, 3.9], color=ORANGE, stroke_width=3)
        self.play(Create(w), run_time=1.2)
        dots3 = VGroup()
        for xx in (1.2, 2.6, 3.6):
            d = Dot(ax.c2p(xx, 0), radius=0.09, color=RED)
            dots3.add(d)
            self.play(FadeIn(d), run_time=0.3)

        p1 = txt("两端同号", size=24, color=BLUE).move_to([-5.3, -1.15, 0])
        p2 = txt("也可能有零点", size=24, color=RED).move_to([-2.6, -1.5, 0])
        self.play(FadeIn(p1), FadeIn(p2), run_time=0.5)

        r1 = rtxt("定理只保证「至少有一个」", 1.45, 29)
        r2 = rtxt("不能直接说「有且只有一个」", 0.5, 29, RED)
        r3 = rtxt("再加上单调性，才能保证唯一", -0.55, 28, GREEN)
        r4 = rtxt("同号时也可能有偶数个零点", -1.6, 26, DIM)
        for m in (r1, r2, r3, r4):
            self.play(Write(m), run_time=0.5)
        self.finish_section()

        # ---------- 4. 变成两个图像的交点 ----------
        self.section(4, "零点个数 = 交点个数")
        self.play(FadeOut(ax), FadeOut(w), FadeOut(dots3), FadeOut(p1), FadeOut(p2),
                  FadeOut(r1), FadeOut(r2), FadeOut(r3), FadeOut(r4), run_time=0.5)

        ax = axes_at(-4.0, 0.1, [-1, 4, 1], [-1, 4, 1], xlen=4.8, ylen=3.2)
        self.play(Create(ax), run_time=0.7)
        g = ax.plot(lambda x: x ** 2 / 2 + 0.2, x_range=[-0.8, 3.4], color=GOLD, stroke_width=3)
        h = ax.plot(lambda x: x + 1, x_range=[-0.5, 3.0], color=BLUE, stroke_width=3)
        self.play(Create(g), run_time=0.8)
        self.play(Create(h), run_time=0.8)

        xa = 1 - (1 + 1.6) ** 0.5
        xb = 1 + (1 + 1.6) ** 0.5
        i1 = Dot(ax.c2p(xa, xa + 1), radius=0.11, color=GREEN)
        i2 = Dot(ax.c2p(xb, xb + 1), radius=0.11, color=GREEN)
        self.play(FadeIn(i1), FadeIn(i2), run_time=0.6)

        lg = txt("y = g(x)", size=20, color=GOLD).move_to([-5.6, -1.95, 0])
        lh = txt("y = h(x)", size=20, color=BLUE).move_to([-3.7, -1.95, 0])
        self.play(FadeIn(lg), FadeIn(lh), run_time=0.5)

        r1 = rtxt("f(x) = 0 可以变形成", 1.45, 29)
        r2 = rtxt("g(x) = h(x)", 0.5, 34, GOLD)
        r3 = rtxt("交点有几个，零点就有几个", -0.55, 29, GREEN)
        r4 = rtxt("比硬解方程直观得多", -1.6, 27, DIM)
        for m in (r1, r2, r3, r4):
            self.play(Write(m), run_time=0.5)
        self.finish_section()

        # ---------- 5. 二分法 ----------
        self.section(5, "二分法：一步步逼近")
        self.play(FadeOut(ax), FadeOut(g), FadeOut(h), FadeOut(i1), FadeOut(i2),
                  FadeOut(lg), FadeOut(lh),
                  FadeOut(r1), FadeOut(r2), FadeOut(r3), FadeOut(r4), run_time=0.5)

        base = Line([-6.2, -1.5, 0], [-1.3, -1.5, 0], color=DIM, stroke_width=3)
        self.play(Create(base), run_time=0.6)

        seg = Line([-5.8, -1.0, 0], [-1.9, -1.0, 0], color=GOLD, stroke_width=9)
        va = DashedLine([-5.8, -1.5, 0], [-5.8, -1.0, 0], color=GOLD, stroke_width=2)
        vb = DashedLine([-1.9, -1.5, 0], [-1.9, -1.0, 0], color=GOLD, stroke_width=2)
        self.play(Create(seg), Create(va), Create(vb), run_time=0.8)

        mid1 = DashedLine([-3.85, -1.0, 0], [-3.85, -0.2, 0], color=BLUE, stroke_width=2.4)
        self.play(Create(mid1), run_time=0.5)
        m1 = txt("取中点", size=22, color=BLUE).move_to([-3.3, -0.25, 0])
        self.play(FadeIn(m1), run_time=0.4)

        seg2 = Line([-3.85, -0.55, 0], [-1.9, -0.55, 0], color=GREEN, stroke_width=7)
        self.play(Create(seg2), run_time=0.6)
        mid2 = DashedLine([-2.87, -0.55, 0], [-2.87, 0.25, 0], color=BLUE, stroke_width=2.4)
        self.play(Create(mid2), run_time=0.5)
        m2 = txt("再取中点", size=22, color=BLUE).move_to([-2.1, 0.35, 0])
        self.play(FadeIn(m2), run_time=0.4)

        seg3 = Line([-3.85, 0.25, 0], [-2.87, 0.25, 0], color=RED, stroke_width=6)
        self.play(Create(seg3), run_time=0.5)

        r1 = rtxt("每次把范围缩小一半", 1.45, 30, GOLD)
        r2 = rtxt("看中点函数值的符号", 0.5, 29)
        r3 = rtxt("重复到精度满足为止", -0.55, 28, GREEN)
        r4 = rtxt("二分法求的是近似值", -1.6, 26, DIM)
        for m in (r1, r2, r3, r4):
            self.play(Write(m), run_time=0.5)
        self.finish_section()

        # ---------- 6. 口诀 ----------
        self.section(6, "记一句话")
        self.play(FadeOut(base), FadeOut(seg), FadeOut(va), FadeOut(vb), FadeOut(mid1),
                  FadeOut(m1), FadeOut(seg2),
                  FadeOut(mid2), FadeOut(m2), FadeOut(seg3),
                  FadeOut(r1), FadeOut(r2), FadeOut(r3), FadeOut(r4), run_time=0.5)

        k1 = txt("异号就必有零点", size=54, color=GOLD).move_to([0, 1.0, 0])
        k2 = txt("连续 + 端点异号，只能保证「有」", size=30, color=CHALK).move_to([0, -0.1, 0])
        k3 = txt("零点是一个数，不是坐标点", size=30, color=GREEN).move_to([0, -1.15, 0])
        self.play(Write(k1), run_time=0.9)
        self.play(Write(k2), run_time=0.7)
        self.play(Write(k3), run_time=0.7)
        self.finish_section()

        self.play(FadeOut(k1), FadeOut(k2), FadeOut(k3), run_time=0.6)