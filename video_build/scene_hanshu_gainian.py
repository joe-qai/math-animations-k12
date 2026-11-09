# -*- coding: utf-8 -*-
"""函数的概念与表示：定义域里一个 x，只能配一个 y。"""

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


def car(x: float, y: float) -> VGroup:
    body = RoundedRectangle(corner_radius=0.1, width=0.95, height=0.4,
                            color=GOLD, stroke_width=2,
                            fill_color=GOLD, fill_opacity=0.35)
    body.move_to([x, y, 0])
    roof = Polygon([x - 0.28, y + 0.2, 0], [x + 0.28, y + 0.2, 0],
                   [x + 0.18, y + 0.42, 0], [x - 0.18, y + 0.42, 0],
                   stroke_color=GOLD, stroke_width=2,
                   fill_color=GOLD, fill_opacity=0.35)
    w1 = Circle(radius=0.11, color=CHALK, stroke_width=2,
                fill_color=BG, fill_opacity=1).move_to([x - 0.28, y - 0.22, 0])
    w2 = Circle(radius=0.11, color=CHALK, stroke_width=2,
                fill_color=BG, fill_opacity=1).move_to([x + 0.28, y - 0.22, 0])
    return VGroup(body, roof, w1, w2)


class HanshuGainianScene(NarratedScene):
    lesson = "hanshu-gainian"

    def construct(self):
        # ---------- 0. 匀速行驶 ----------
        self.section(0, "时间定了，路程就定了")
        road = Line([-6.4, -0.85, 0], [-1.0, -0.85, 0], color=DIM, stroke_width=5)
        self.play(Create(road), run_time=0.7)

        c = car(-5.2, -0.55)
        self.play(FadeIn(c), run_time=0.6)

        p1 = txt("2 h  →  120 km", size=25, color=BLUE).move_to([-4.75, -1.45, 0])
        p2 = txt("3 h  →  180 km", size=25, color=BLUE).move_to([-1.65, -1.45, 0])
        self.play(FadeIn(p1), run_time=0.5)
        self.play(FadeIn(p2), run_time=0.5)

        c2 = car(-2.4, -0.55)
        self.play(FadeIn(c2), run_time=0.4)

        r1 = rtxt("速度是每小时 60 km", 1.4, 30)
        r2 = rtxt("时间定了，路程就定了", 0.45, 32, GOLD)
        r3 = rtxt("一个量，跟着另一个量唯一确定", -0.6, 27)
        r4 = rtxt("这种关系，就叫函数", -1.6, 30, GREEN)
        for m in (r1, r2, r3, r4):
            self.play(Write(m), run_time=0.5)
        self.finish_section()

        # ---------- 1. 函数的定义 ----------
        self.section(1, "一个 x，只能配一个 y")
        self.play(FadeOut(road), FadeOut(c), FadeOut(c2), FadeOut(p1),
                  FadeOut(p2),
                  FadeOut(r1), FadeOut(r2), FadeOut(r3), FadeOut(r4), run_time=0.5)

        ax = RoundedRectangle(corner_radius=0.16, width=1.5, height=3.3,
                              color=BLUE, stroke_width=2.4,
                              fill_color=BLUE, fill_opacity=0.08).move_to([-5.9, -0.1, 0])
        bx = RoundedRectangle(corner_radius=0.16, width=1.5, height=3.3,
                              color=GOLD, stroke_width=2.4,
                              fill_color=GOLD, fill_opacity=0.08).move_to([-2.0, -0.1, 0])
        self.play(Create(ax), Create(bx), run_time=0.8)

        ta = txt("A", size=28, color=BLUE).move_to([-5.9, 1.35, 0])
        tb = txt("B", size=28, color=GOLD).move_to([-2.0, 1.35, 0])
        self.play(FadeIn(ta), FadeIn(tb), run_time=0.4)

        left = [txt(s, size=30).move_to([-5.9, 0.55 - i * 0.95, 0]) for i, s in enumerate(["1", "2", "3"])]
        right = [txt(s, size=30, color=GOLD).move_to([-2.0, 0.55 - i * 0.95, 0]) for i, s in enumerate(["2", "4", "6"])]
        self.play(*[FadeIn(m) for m in left], run_time=0.5)
        self.play(*[FadeIn(m) for m in right], run_time=0.5)

        a1 = Arrow([-5.55, 0.55, 0], [-2.35, 0.55, 0], color=GREEN, stroke_width=3,
                   buff=0, max_tip_length_to_length_ratio=0.16)
        a2 = Arrow([-5.55, -0.4, 0], [-2.35, -0.4, 0], color=GREEN, stroke_width=3,
                   buff=0, max_tip_length_to_length_ratio=0.16)
        a3 = Arrow([-5.55, -1.35, 0], [-2.35, -1.35, 0], color=GREEN, stroke_width=3,
                   buff=0, max_tip_length_to_length_ratio=0.16)
        self.play(Create(a1), run_time=0.5)
        self.play(Create(a2), run_time=0.5)
        self.play(Create(a3), run_time=0.5)

        bad = DashedLine([-5.55, 0.55, 0], [-2.35, -0.4, 0], color=RED, stroke_width=3)
        self.play(Create(bad), run_time=0.6)
        cross = VGroup(
            Line([-4.05, 0.2, 0], [-3.75, -0.05, 0], color=RED, stroke_width=4),
            Line([-4.05, -0.05, 0], [-3.75, 0.2, 0], color=RED, stroke_width=4),
        )
        self.play(Create(cross), run_time=0.5)

        r1 = rtxt("A 里的每个 x 都要有", 1.45, 29)
        r2 = rtxt("而且只能有一个 y", 0.5, 32, GOLD)
        r3 = rtxt("一个 x 配两个 y，不是函数", -0.6, 28, RED)
        r4 = rtxt("记作 y = f(x)，x ∈ A", -1.6, 30, GREEN)
        for m in (r1, r2, r3, r4):
            self.play(Write(m), run_time=0.5)
        self.finish_section()

        # ---------- 2. 三要素 ----------
        self.section(2, "三要素：定义域、值域、对应关系")
        self.play(FadeOut(ax), FadeOut(bx), FadeOut(ta), FadeOut(tb),
                  FadeOut(VGroup(*left)), FadeOut(VGroup(*right)),
                  FadeOut(a1), FadeOut(a2), FadeOut(a3), FadeOut(bad), FadeOut(cross),
                  FadeOut(r1), FadeOut(r2), FadeOut(r3), FadeOut(r4), run_time=0.5)

        b1 = RoundedRectangle(corner_radius=0.12, width=1.35, height=0.95,
                              color=BLUE, stroke_width=2.2,
                              fill_color=BLUE, fill_opacity=0.18).move_to([-5.7, 0.3, 0])
        fx = Circle(radius=0.62, color=GOLD, stroke_width=2.4,
                    fill_color=GOLD, fill_opacity=0.18).move_to([-3.9, 0.3, 0])
        b2 = RoundedRectangle(corner_radius=0.12, width=1.35, height=0.95,
                              color=GREEN, stroke_width=2.2,
                              fill_color=GREEN, fill_opacity=0.18).move_to([-2.1, 0.3, 0])
        self.play(Create(b1), Create(fx), Create(b2), run_time=0.8)

        t1 = txt("x", size=38, color=BLUE).move_to(b1.get_center())
        tf = txt("f", size=40, color=GOLD).move_to(fx.get_center())
        t2 = txt("y", size=38, color=GREEN).move_to(b2.get_center())
        self.play(FadeIn(t1), FadeIn(tf), FadeIn(t2), run_time=0.5)

        a1 = Arrow([-4.9, 0.3, 0], [-4.55, 0.3, 0], color=CHALK, stroke_width=3, buff=0,
                   max_tip_length_to_length_ratio=0.3)
        a2 = Arrow([-3.25, 0.3, 0], [-2.8, 0.3, 0], color=CHALK, stroke_width=3, buff=0,
                   max_tip_length_to_length_ratio=0.3)
        self.play(Create(a1), Create(a2), run_time=0.6)

        l1 = txt("定义域", size=22, color=BLUE).move_to([-5.7, -0.55, 0])
        l2 = txt("对应关系", size=22, color=GOLD).move_to([-3.9, -0.55, 0])
        l3 = txt("值域", size=22, color=GREEN).move_to([-2.1, -0.55, 0])
        self.play(FadeIn(l1), FadeIn(l2), FadeIn(l3), run_time=0.5)

        r1 = rtxt("定义域：x 能取的所有值", 1.45, 29, BLUE)
        r2 = rtxt("对应关系：y 怎么由 x 算", 0.5, 29, GOLD)
        r3 = rtxt("值域：算出来的所有 y", -0.55, 29, GREEN)
        r4 = rtxt("前两条定下来，值域就定了", -1.6, 27, DIM)
        for m in (r1, r2, r3, r4):
            self.play(Write(m), run_time=0.5)
        self.finish_section()

        # ---------- 3. 区间 ----------
        self.section(3, "定义域用区间来写")
        self.play(FadeOut(b1), FadeOut(fx), FadeOut(b2), FadeOut(t1), FadeOut(tf),
                  FadeOut(t2), FadeOut(a1), FadeOut(a2), FadeOut(l1), FadeOut(l2),
                  FadeOut(l3), FadeOut(r1), FadeOut(r2), FadeOut(r3),
                  FadeOut(r4), run_time=0.5)

        nl = NumberLine(x_range=[0, 5, 1], length=5.4, color=DIM)
        nl.move_to([-3.9, 0.15, 0])
        self.play(Create(nl), run_time=0.9)
        ticks = VGroup(*[txt(str(i), size=20, color=DIM).move_to(nl.n2p(i) + DOWN * 0.32)
                         for i in range(0, 6)])
        self.play(FadeIn(ticks), run_time=0.5)

        seg = Line(nl.n2p(1) + UP * 0.5, nl.n2p(3) + UP * 0.5, color=GOLD, stroke_width=7)
        d1 = Dot(nl.n2p(1) + UP * 0.5, radius=0.1, color=GOLD)
        d2 = Dot(nl.n2p(3) + UP * 0.5, radius=0.1, color=GOLD)
        self.play(Create(seg), run_time=0.6)
        self.play(FadeIn(d1), FadeIn(d2), run_time=0.4)
        lab = txt("[1, 3]", size=30, color=GOLD).move_to([-3.9, 1.05, 0])
        self.play(Write(lab), run_time=0.6)

        seg2 = Line(nl.n2p(2) + DOWN * 0.75, nl.n2p(5) + DOWN * 0.75, color=BLUE, stroke_width=6)
        ring = Circle(radius=0.1, color=BLUE, stroke_width=3,
                      fill_color=BG, fill_opacity=1).move_to(nl.n2p(2) + DOWN * 0.75)
        self.play(Create(seg2), run_time=0.6)
        self.play(FadeIn(ring), run_time=0.4)
        lab2 = txt("(2, +∞)", size=28, color=BLUE).move_to([-1.0, -1.35, 0])
        self.play(Write(lab2), run_time=0.6)

        r1 = rtxt("都取到：方括号 [a, b]", 1.45, 29, GOLD)
        r2 = rtxt("取不到：圆括号 (a, b)", 0.5, 29, BLUE)
        r3 = rtxt("一端取不到：半开半闭", -0.55, 28)
        r4 = rtxt("写作 (a, +∞) 或 (−∞, b)", -1.6, 27, DIM)
        for m in (r1, r2, r3, r4):
            self.play(Write(m), run_time=0.5)
        self.finish_section()

        # ---------- 4. 三种表示法 ----------
        self.section(4, "三种表示法")
        self.play(FadeOut(nl), FadeOut(ticks), FadeOut(seg), FadeOut(d1), FadeOut(d2),
                  FadeOut(lab), FadeOut(seg2), FadeOut(ring), FadeOut(lab2),
                  FadeOut(r1), FadeOut(r2), FadeOut(r3), FadeOut(r4), run_time=0.5)

        cards = []
        specs = [("解析法", "y = 2x + 1", GOLD, 1.2),
                 ("图像法", "一条直线", BLUE, 0.0),
                 ("列表法", "x: 1 2 3", GREEN, -1.2)]
        for name, ex, col, y in specs:
            box = RoundedRectangle(corner_radius=0.14, width=4.9, height=0.95,
                                   color=col, stroke_width=2,
                                   fill_color=col, fill_opacity=0.1).move_to([-4.5, y, 0])
            nt = txt(name, size=28, color=col).move_to([-6.05, y, 0])
            et = txt(ex, size=26, color=CHALK).move_to([-3.85, y, 0])
            cards.append(VGroup(box, nt, et))
        self.play(LaggedStart(*[FadeIn(c, shift=RIGHT * 0.15) for c in cards],
                              lag_ratio=0.25), run_time=1.2)

        r1 = rtxt("式子便于计算", 1.4, 30, GOLD)
        r2 = rtxt("图像便于看变化趋势", 0.45, 30, BLUE)
        r3 = rtxt("表格适合零散的数据", -0.55, 28, GREEN)
        r4 = rtxt("三种可以互相转换", -1.6, 27, DIM)
        for m in (r1, r2, r3, r4):
            self.play(Write(m), run_time=0.5)
        self.finish_section()

        # ---------- 5. 分段函数 ----------
        self.section(5, "分段函数")
        self.play(FadeOut(VGroup(*cards)), FadeOut(r1), FadeOut(r2), FadeOut(r3),
                  FadeOut(r4), run_time=0.5)

        ox = Line([-6.2, -1.65, 0], [-1.3, -1.65, 0], color=DIM, stroke_width=2.4)
        oy = Line([-6.2, -1.65, 0], [-6.2, 1.65, 0], color=DIM, stroke_width=2.4)
        self.play(Create(ox), Create(oy), run_time=0.7)

        p1 = Line([-6.2, -0.55, 0], [-4.9, -0.55, 0], color=GOLD, stroke_width=5)
        p2 = Line([-4.9, -0.55, 0], [-1.8, 1.25, 0], color=GOLD, stroke_width=5)
        self.play(Create(p1), run_time=0.6)
        self.play(Create(p2), run_time=0.7)

        d1 = Dot([-4.9, -0.55, 0], radius=0.09, color=GOLD)
        self.play(FadeIn(d1), run_time=0.4)

        m1 = txt("起步价", size=24, color=GOLD).move_to([-5.55, 0.0, 0])
        m2 = txt("每公里加钱", size=24, color=GOLD).move_to([-2.6, 1.5, 0])
        self.play(FadeIn(m1), FadeIn(m2), run_time=0.5)

        div = DashedLine([-4.9, -1.65, 0], [-4.9, 1.5, 0], color=RED, stroke_width=2)
        self.play(Create(div), run_time=0.5)

        r1 = rtxt("不同范围，用不同式子", 1.45, 30, GOLD)
        r2 = rtxt("y = 8（0 < x ≤ 2）", 0.5, 28)
        r3 = rtxt("y = 8 + 3(x − 2)（x > 2）", -0.55, 27)
        r4 = rtxt("合起来仍是一个函数", -1.6, 28, GREEN)
        for m in (r1, r2, r3, r4):
            self.play(Write(m), run_time=0.5)
        self.finish_section()

        # ---------- 6. 口诀 ----------
        self.section(6, "记一句话")
        self.play(FadeOut(ox), FadeOut(oy), FadeOut(p1), FadeOut(p2), FadeOut(d1),
                  FadeOut(m1), FadeOut(m2), FadeOut(div),
                  FadeOut(r1), FadeOut(r2), FadeOut(r3), FadeOut(r4), run_time=0.5)

        k1 = txt("一个 x 配一个 y", size=56, color=GOLD).move_to([0, 1.0, 0])
        k2 = txt("先写定义域，再谈对应关系", size=32, color=CHALK).move_to([0, -0.15, 0])
        k3 = txt("分段函数，先看 x 落在哪一段", size=30, color=GREEN).move_to([0, -1.2, 0])
        self.play(Write(k1), run_time=0.9)
        self.play(Write(k2), run_time=0.7)
        self.play(Write(k3), run_time=0.7)
        self.finish_section()

        self.play(FadeOut(k1), FadeOut(k2), FadeOut(k3), run_time=0.6)