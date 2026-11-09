# -*- coding: utf-8 -*-
"""图形的位似：形状不变、对应点连线过同一点、坐标同乘一个比。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403

OX, OY, U = -6.0, -1.85, 1.15
TRI = [(1, 1), (2, 1), (1, 2)]


def P(u: float, v: float) -> list[float]:
    return [OX + u * U, OY + v * U, 0]


def poly(scale: float = 1.0, color: str = CHALK, fill: str = BLUE,
         opacity: float = 0.12, width: float = 2.4) -> Polygon:
    pts = [P(u * scale, v * scale) for (u, v) in TRI]
    return Polygon(*pts, stroke_color=color, stroke_width=width,
                   fill_color=fill, fill_opacity=opacity)


class WeisiScene(NarratedScene):
    lesson = "weisi"

    def construct(self):
        # ---------- 0. 放大镜 ----------
        self.section(0, "形状不变，只是按比例放大")
        base = poly(1.0)
        self.play(Create(base), run_time=0.9)

        bl = txt("原图", size=24, color=CHALK).move_to([-4.3, -1.15, 0])
        self.play(FadeIn(bl), run_time=0.4)

        q1 = txt("用放大镜看它", size=34, color=CHALK).move_to([3.5, 1.2, 0])
        q2 = txt("形状变了吗？", size=36, color=GOLD).move_to([3.5, 0.25, 0])
        self.play(Write(q1), run_time=0.6)
        self.play(Write(q2), run_time=0.6)

        q3 = txt("没有，只是每个地方都按同样的比例变大", size=26, color=DIM)
        q3.move_to([3.5, -0.85, 0])
        self.play(FadeIn(q3), run_time=0.6)
        self.finish_section()

        # ---------- 1. 对应点连线过同一点 ----------
        self.section(1, "对应点连线，都过同一个点")
        self.play(FadeOut(q1), FadeOut(q2), FadeOut(q3), run_time=0.4)

        big = poly(2.0, color=GOLD, fill=GOLD, opacity=0.08)
        self.play(Create(big), run_time=1.0)

        O = Dot([OX, OY, 0], radius=0.09, color=RED)
        olab = txt("O", size=24, color=RED).move_to([OX - 0.25, OY - 0.25, 0])
        self.play(FadeIn(O), FadeIn(olab), run_time=0.5)

        rays = VGroup(*[
            Line([OX, OY, 0], P(u * 2, v * 2), color=RED, stroke_width=1.4)
            for (u, v) in TRI
        ])
        self.play(LaggedStart(*[Create(r) for r in rays], lag_ratio=0.2), run_time=1.2)

        t1 = txt("三个顶点都在同一点出发的射线上", size=28, color=RED)
        t1.move_to([3.4, 0.9, 0])
        self.play(Write(t1), run_time=0.7)

        t2 = txt("这样的两个图形叫「位似图形」", size=30, color=GOLD)
        t2.move_to([3.4, -0.15, 0])
        self.play(FadeIn(t2, shift=UP * 0.1), run_time=0.6)
        self.finish_section()

        # ---------- 2. 位似中心和位似比 ----------
        self.section(2, "那个点是位似中心")
        self.play(FadeOut(t1), FadeOut(t2), run_time=0.4)

        c1 = txt("点 O 叫位似中心", size=36, color=RED).move_to([3.5, 1.2, 0])
        c2 = txt("对应边之比叫位似比", size=34, color=GOLD).move_to([3.5, 0.25, 0])
        self.play(Write(c1), run_time=0.6)
        self.play(Write(c2), run_time=0.6)

        c3 = txt("位似比就是相似比", size=34, color=GREEN).move_to([3.5, -0.8, 0])
        self.play(Write(c3), run_time=0.6)

        c4 = txt("这里是 2 : 1", size=32, color=BLUE).move_to([3.5, -1.75, 0])
        self.play(FadeIn(c4, shift=UP * 0.1), run_time=0.6)
        self.finish_section()

        # ---------- 3. 位似与相似 ----------
        self.section(3, "位似一定相似，相似不一定位似")
        self.play(FadeOut(c1), FadeOut(c2), FadeOut(c3), FadeOut(c4),
                  FadeOut(rays), FadeOut(O), FadeOut(olab), FadeOut(big),
                  FadeOut(base), FadeOut(bl), run_time=0.5)

        a1 = label_box("位似", size=32, color=GOLD).move_to([-3.2, 0.85, 0])
        a2 = txt("→ 一定相似", size=32, color=GREEN).move_to([2.6, 0.85, 0])
        self.play(FadeIn(a1), FadeIn(a2), run_time=0.6)

        b1 = label_box("相似", size=32, color=BLUE).move_to([-3.2, -0.35, 0])
        b2 = txt("→ 不一定位似", size=32, color=RED).move_to([2.6, -0.35, 0])
        self.play(FadeIn(b1), FadeIn(b2), run_time=0.6)

        note = txt("还要看对应点的连线是否过同一点", size=28, color=DIM)
        note.move_to([0, -1.45, 0])
        self.play(FadeIn(note), run_time=0.6)
        self.finish_section()

        # ---------- 4. 怎么画位似图形 ----------
        self.section(4, "画法：先连线，再按比取点")
        self.play(FadeOut(a1), FadeOut(a2), FadeOut(b1), FadeOut(b2), FadeOut(note),
                  run_time=0.5)

        d1 = txt("① 把各顶点与位似中心连起来", size=30, color=CHALK).move_to([0, 1.25, 0])
        d2 = txt("② 在射线上按位似比取点", size=30, color=CHALK).move_to([0, 0.35, 0])
        d3 = txt("③ 依次连接新顶点", size=30, color=CHALK).move_to([0, -0.55, 0])
        self.play(FadeIn(d1, shift=RIGHT * 0.1), run_time=0.6)
        self.play(FadeIn(d2, shift=RIGHT * 0.1), run_time=0.6)
        self.play(FadeIn(d3, shift=RIGHT * 0.1), run_time=0.6)

        d4 = txt("顺序固定，画出来才不歪", size=28, color=GOLD).move_to([0, -1.55, 0])
        self.play(FadeIn(d4), run_time=0.5)
        self.finish_section()

        # ---------- 5. 坐标规律 ----------
        self.section(5, "以原点为中心，坐标同乘 k")
        self.play(FadeOut(d1), FadeOut(d2), FadeOut(d3), FadeOut(d4), run_time=0.5)

        e1 = txt("原点为位似中心，位似比 k", size=30, color=CHALK).move_to([0, 1.4, 0])
        e2 = txt("(x, y)  →  (kx, ky)", size=46, color=GOLD).move_to([0, 0.35, 0])
        self.play(Write(e1), run_time=0.6)
        self.play(Write(e2), run_time=0.9)

        e3 = txt("A(1, 2) 配 k = 3  →  A′(3, 6)", size=32, color=GREEN).move_to([0, -0.8, 0])
        self.play(FadeIn(e3, shift=UP * 0.1), run_time=0.6)

        e4 = txt("k 是负数时，图形跑到中心另一侧", size=28, color=DIM).move_to([0, -1.8, 0])
        self.play(FadeIn(e4), run_time=0.5)
        self.finish_section()

        # ---------- 6. 口诀 ----------
        self.section(6, "形状不变，比例相同")
        self.play(FadeOut(e1), FadeOut(e2), FadeOut(e3), FadeOut(e4), run_time=0.5)

        k1 = txt("形状不变，比例相同", size=46, color=GOLD).move_to([0, 1.15, 0])
        k2 = txt("对应点连线过同一点", size=42, color=CHALK).move_to([0, 0.15, 0])
        k3 = txt("坐标同乘一个比", size=42, color=GREEN).move_to([0, -0.9, 0])
        self.play(Write(k1), run_time=0.8)
        self.play(Write(k2), run_time=0.8)
        self.play(Write(k3), run_time=0.7)

        fin = txt("位似，是用一个点控制整体放大缩小", size=28, color=DIM)
        fin.move_to([0, -1.95, 0])
        self.play(FadeIn(fin), run_time=0.5)
        self.finish_section()

        self.play(FadeOut(k1), FadeOut(k2), FadeOut(k3), FadeOut(fin), run_time=0.6)