# -*- coding: utf-8 -*-
"""长方体的展开图：六个面、十二条棱、八个顶点，沿棱剪开摊平。五年级下册「长方体和正方体」。"""

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


def cuboid(w: float, h: float, d: float, cx: float = 0.0, cy: float = 0.0,
           color: str = CHALK, fill_opacity: float = 0.06) -> VGroup:
    """等轴测视角的长方体：正面矩形 + 顶面、右面两个平行四边形。"""
    ox, oy = d * 0.62, d * 0.48
    A = [-w / 2, -h / 2, 0]
    B = [w / 2, -h / 2, 0]
    C = [w / 2, h / 2, 0]
    D = [-w / 2, h / 2, 0]
    off = np.array([ox, oy, 0])
    E = np.array(A) + off
    F = np.array(B) + off
    G = np.array(C) + off
    H = np.array(D) + off

    front = Polygon(A, B, C, D, stroke_width=0, fill_color=color, fill_opacity=fill_opacity)
    top = Polygon(D, C, G, H, stroke_width=0, fill_color=color, fill_opacity=fill_opacity * 1.7)
    right = Polygon(B, C, G, F, stroke_width=0, fill_color=color, fill_opacity=fill_opacity * 1.2)

    edges = VGroup(
        Line(A, B, color=color, stroke_width=2.6),
        Line(B, C, color=color, stroke_width=2.6),
        Line(C, D, color=color, stroke_width=2.6),
        Line(D, A, color=color, stroke_width=2.6),
        Line(D, H, color=color, stroke_width=2.2),
        Line(C, G, color=color, stroke_width=2.2),
        Line(B, F, color=color, stroke_width=2.2),
        Line(H, G, color=color, stroke_width=2.6),
        Line(G, F, color=color, stroke_width=2.6),
    )
    g = VGroup(front, top, right, edges)
    g.shift([cx, cy, 0])
    return g


def cube_vertices(w: float, h: float, d: float, cx: float = 0.0, cy: float = 0.0) -> VGroup:
    ox, oy = d * 0.62, d * 0.48
    pts = [
        [-w / 2, -h / 2], [w / 2, -h / 2], [w / 2, h / 2], [-w / 2, h / 2],
        [-w / 2 + ox, -h / 2 + oy], [w / 2 + ox, -h / 2 + oy],
        [w / 2 + ox, h / 2 + oy], [-w / 2 + ox, h / 2 + oy],
    ]
    visible = [0, 1, 2, 3, 5, 6, 7]  # 背面的左下顶点被挡住，不画
    return VGroup(*[
        Dot([cx + pts[i][0], cy + pts[i][1], 0], radius=0.055, color=GOLD)
        for i in visible
    ])


def net_141(u: float = 0.62, cx: float = 0.0, cy: float = 0.0,
            colors: bool = True) -> VGroup:
    """一四一展开图：中间一排 4 个面，上下各接 1 个面。"""
    faces = []
    band_cols = [BLUE, GREEN, BLUE, GREEN] if colors else [CHALK] * 4
    xs = [-1.5 * u, -0.5 * u, 0.5 * u, 1.5 * u]
    for x, c in zip(xs, band_cols):
        sq = Square(u, stroke_width=2.6, stroke_color=CHALK)
        sq.set_fill(c, 0.38).move_to([cx + x, cy, 0])
        faces.append(sq)
    for x, y in ((-0.5 * u, u), (0.5 * u, -u)):
        sq = Square(u, stroke_width=2.6, stroke_color=CHALK)
        sq.set_fill(GOLD if colors else CHALK, 0.38 if colors else 0.24)
        sq.move_to([cx + x, cy + y, 0])
        faces.append(sq)
    return VGroup(*faces)


def net_231(u: float = 0.52, cx: float = 0.0, cy: float = 0.0) -> VGroup:
    """二三一展开图：上 2、中 3、下 1。"""
    cells = [(-1, 1), (0, 1), (-1, 0), (0, 0), (1, 0), (1, -1)]
    g = VGroup()
    for i, (x, y) in enumerate(cells):
        sq = Square(u, stroke_width=2.2, stroke_color=CHALK)
        sq.set_fill(GOLD if i < 2 else (BLUE if i < 5 else GREEN), 0.12)
        sq.move_to([cx + x * u, cy + y * u, 0])
        g.add(sq)
    return g


class ChangfangtiZhankaituScene(NarratedScene):
    lesson = "changfangti-zhankaitu"

    def construct(self):
        # ---------- 0. 纸盒：6 面 12 棱 8 顶点 ----------
        self.section(0, "六个面、十二条棱、八个顶点")
        box = cuboid(3.0, 2.0, 1.15, cx=-3.6, cy=0.25)
        dots = cube_vertices(3.0, 2.0, 1.15, cx=-3.6, cy=0.25)
        self.play(Create(box), run_time=1.2)
        self.play(LaggedStart(*[FadeIn(d, scale=0.6) for d in dots], lag_ratio=0.06),
                  run_time=0.9)

        f1 = txt("6 个面", size=36, color=GOLD).move_to([3.65, 1.75, 0])
        f2 = txt("12 条棱", size=36, color=BLUE).move_to([3.65, 0.75, 0])
        f3 = txt("8 个顶点", size=36, color=GREEN).move_to([3.65, -0.25, 0])
        self.play(Write(f1), run_time=0.6)
        self.play(Write(f2), run_time=0.6)
        self.play(Write(f3), run_time=0.6)

        q = txt("沿棱剪开摊平，会得到什么？", size=36, color=CHALK).move_to([0, -2.55, 0])
        self.play(FadeIn(q, shift=UP * 0.1), run_time=0.6)
        self.finish_section()

        # ---------- 1. 沿棱剪开 ----------
        self.section(1, "沿棱剪开，连成一整张")
        self.play(FadeOut(f1), FadeOut(f2), FadeOut(f3), FadeOut(q), run_time=0.4)

        # 用红色虚线标出要剪的棱
        ox, oy = 1.15 * 0.62, 1.15 * 0.48
        base = np.array([-3.6, 0.25, 0])
        cuts = VGroup(
            DashedLine(base + np.array([1.5, 1.0, 0]), base + np.array([1.5 + ox, 1.0 + oy, 0]),
                       dash_length=0.12, color=RED, stroke_width=3),
            DashedLine(base + np.array([-1.5, 1.0, 0]), base + np.array([-1.5 + ox, 1.0 + oy, 0]),
                       dash_length=0.12, color=RED, stroke_width=3),
            DashedLine(base + np.array([-1.5, -1.0, 0]), base + np.array([-1.5 + ox, -1.0 + oy, 0]),
                       dash_length=0.12, color=RED, stroke_width=3),
        )
        self.play(LaggedStart(*[Create(c) for c in cuts], lag_ratio=0.25), run_time=1.0)

        net = net_141(u=0.78, cx=-3.6, cy=0.35)
        self.play(FadeOut(box), FadeOut(dots), FadeOut(cuts), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(s, scale=0.85) for s in net], lag_ratio=0.10),
                  run_time=1.2)

        h1 = txt("相对的面不能剪断", size=36, color=GOLD).move_to([3.65, 1.55, 0])
        h2 = txt("否则盒子散成六片", size=30, color=DIM).move_to([3.65, 0.75, 0])
        h3 = txt("最后要连成一整张", size=34, color=GREEN).move_to([3.65, -0.35, 0])
        self.play(Write(h1), run_time=0.7)
        self.play(FadeIn(h2), run_time=0.5)
        self.play(FadeIn(h3, shift=UP * 0.1), run_time=0.6)
        self.finish_section()

        # ---------- 2. 相对的面完全相同 ----------
        self.section(2, "相对的面完全相同")
        self.play(FadeOut(h1), FadeOut(h2), FadeOut(h3), run_time=0.4)

        p1 = txt("上、下两面相同", size=34, color=GOLD).move_to([3.65, 1.65, 0])
        p2 = txt("前、后两面相同", size=34, color=BLUE).move_to([3.65, 0.65, 0])
        p3 = txt("左、右两面相同", size=34, color=GREEN).move_to([3.65, -0.35, 0])
        self.play(Write(p1), run_time=0.7)
        self.play(Write(p2), run_time=0.7)
        self.play(Write(p3), run_time=0.7)

        # 同色的两个面轻轻闪烁，强调一对
        for a, b in ((net[4], net[5]), (net[0], net[2]), (net[1], net[3])):
            self.play(a.animate.set_fill(opacity=0.4), b.animate.set_fill(opacity=0.4),
                      run_time=0.3)
            self.play(a.animate.set_fill(opacity=0.14), b.animate.set_fill(opacity=0.14),
                      run_time=0.3)
        self.finish_section()

        # ---------- 3. 最常见的一四一 ----------
        self.section(3, "最常见的「一四一」")
        self.play(FadeOut(p1), FadeOut(p2), FadeOut(p3), run_time=0.4)

        # 把中间的 4 个面框起来
        band = SurroundingRectangle(VGroup(net[0], net[1], net[2], net[3]),
                                    color=GOLD, stroke_width=2, buff=0.08)
        self.play(Create(band), run_time=0.8)

        r1 = txt("中间一排 4 个面", size=36, color=GOLD).move_to([3.65, 1.55, 0])
        r2 = txt("上下各贴 1 个面", size=36, color=BLUE).move_to([3.65, 0.55, 0])
        r3 = txt("合起来正好 6 个面", size=32, color=GREEN).move_to([3.65, -0.55, 0])
        self.play(Write(r1), run_time=0.8)
        self.play(Write(r2), run_time=0.8)
        self.play(FadeIn(r3, shift=UP * 0.1), run_time=0.6)
        self.finish_section()

        # ---------- 4. 二三一、二二二、三三 ----------
        self.section(4, "展开图不止一种")
        self.play(FadeOut(band), FadeOut(net), FadeOut(r1), FadeOut(r2), FadeOut(r3),
                  run_time=0.5)

        net2 = net_231(u=0.8, cx=-3.8, cy=0.35)
        self.play(LaggedStart(*[FadeIn(s, scale=0.85) for s in net2], lag_ratio=0.10),
                  run_time=1.0)

        t1 = txt("一四一", size=34, color=GOLD).move_to([2.35, 1.75, 0])
        t2 = txt("二三一", size=34, color=BLUE).move_to([2.35, 0.85, 0])
        t3 = txt("二二二", size=34, color=GREEN).move_to([2.35, -0.05, 0])
        t4 = txt("三三", size=34, color=ORANGE).move_to([2.35, -0.95, 0])
        self.play(LaggedStart(*[FadeIn(t, shift=RIGHT * 0.1) for t in (t1, t2, t3, t4)],
                              lag_ratio=0.18), run_time=1.2)

        t5 = txt("不管怎么排", size=32, color=CHALK).move_to([5.15, 0.85, 0])
        t6 = txt("都能折回盒子", size=32, color=CHALK).move_to([5.15, -0.05, 0])
        self.play(FadeIn(t5), FadeIn(t6), run_time=0.6)
        self.finish_section()

        # ---------- 5. 正方体：十一种 ----------
        self.section(5, "正方体：六个面都是正方形")
        self.play(FadeOut(net2), FadeOut(t1), FadeOut(t2), FadeOut(t3), FadeOut(t4),
                  FadeOut(t5), FadeOut(t6), run_time=0.5)

        cb = cuboid(1.5, 1.5, 1.5, cx=-4.55, cy=0.35)
        self.play(Create(cb), run_time=0.9)

        net3 = net_141(u=0.6, cx=-1.45, cy=0.35, colors=False)
        self.play(LaggedStart(*[FadeIn(s, scale=0.85) for s in net3], lag_ratio=0.08),
                  run_time=1.0)

        s1 = txt("正方体是特殊的长方体", size=32, color=GOLD).move_to([4.15, 1.55, 0])
        s2 = txt("六个面都是正方形", size=32, color=CHALK).move_to([4.15, 0.6, 0])
        s3 = txt("展开图共 11 种", size=40, color=GREEN).move_to([4.15, -0.5, 0])
        self.play(Write(s1), run_time=0.7)
        self.play(Write(s2), run_time=0.6)
        self.play(Write(s3), run_time=0.8)
        self.finish_section()

        # ---------- 6. 口诀 ----------
        self.section(6, "六个面、十二条棱、八个顶点")
        self.play(FadeOut(cb), FadeOut(net3), FadeOut(s1), FadeOut(s2), FadeOut(s3),
                  run_time=0.5)

        big1 = txt("6 个面 · 12 条棱 · 8 个顶点", size=46, color=GOLD).move_to([0, 1.45, 0])
        big2 = txt("相对的面完全相同", size=48, color=GREEN).move_to([0, 0.3, 0])
        big3 = txt("相对的棱长度相等", size=48, color=BLUE).move_to([0, -0.85, 0])
        self.play(Write(big1), run_time=0.9)
        self.play(Write(big2), run_time=0.9)
        self.play(Write(big3), run_time=0.9)

        fin = txt("长方体和正方体的基本特征", size=30, color=DIM).move_to([0, -2.15, 0])
        self.play(FadeIn(fin, shift=UP * 0.1), run_time=0.6)
        self.finish_section()

        self.play(FadeOut(big1), FadeOut(big2), FadeOut(big3), FadeOut(fin),
                  run_time=0.6)