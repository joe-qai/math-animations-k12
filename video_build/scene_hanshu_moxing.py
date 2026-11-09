# -*- coding: utf-8 -*-
"""函数模型：先建模，再求解，最后回到实际检验。"""

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


class HanshuMoxingScene(NarratedScene):
    lesson = "hanshu-moxing"

    def construct(self):
        # ---------- 0. 围菜地 ----------
        self.section(0, "周长固定的菜地")
        fence = Rectangle(width=4.4, height=2.6, color=ORANGE, stroke_width=3.4,
                          fill_color=GREEN, fill_opacity=0.1).move_to([-4.0, 0.3, 0])
        self.play(Create(fence), run_time=0.9)

        lx = txt("x", size=30, color=GOLD).move_to([-4.0, -1.35, 0])
        ly = txt("宽：10 − x", size=24, color=GOLD).move_to([-5.35, 1.88, 0])
        self.play(FadeIn(lx), FadeIn(ly), run_time=0.5)

        per = txt("篱笆总长 20", size=26, color=DIM).move_to([-4.0, 2.6, 0])
        self.play(FadeIn(per), run_time=0.5)

        r1 = rtxt("用 20 长的篱笆围矩形", 1.45, 29)
        r2 = rtxt("怎么围，面积最大？", 0.5, 33, GOLD)
        r3 = rtxt("先别急着算", -0.55, 28, DIM)
        r4 = rtxt("先把题目翻译成函数", -1.6, 30, GREEN)
        for m in (r1, r2, r3, r4):
            self.play(Write(m), run_time=0.5)
        self.finish_section()

        # ---------- 1. 列二次函数 ----------
        self.section(1, "设一边为 x，面积就是二次函数")
        self.play(FadeOut(fence), FadeOut(lx), FadeOut(ly), FadeOut(per),
                  FadeOut(r1), FadeOut(r2), FadeOut(r3), FadeOut(r4), run_time=0.5)

        s1 = txt("长：x", size=30, color=GOLD).move_to([-4.4, 1.55, 0])
        s2 = txt("宽：10 − x", size=30, color=GOLD).move_to([-4.4, 0.8, 0])
        s3 = txt("面积 S = x(10 − x)", size=34, color=GREEN).move_to([-4.4, -0.1, 0])
        s4 = txt("= −x² + 10x", size=30, color=CHALK).move_to([-4.4, -0.9, 0])
        s5 = txt("0 < x < 10", size=26, color=RED).move_to([-4.4, -1.7, 0])
        for m in (s1, s2, s3, s4, s5):
            self.play(Write(m), run_time=0.6)

        r1 = rtxt("设一边为 x", 1.45, 30, GOLD)
        r2 = rtxt("另一边就是 10 − x", 0.5, 30)
        r3 = rtxt("相乘得到二次函数", -0.55, 29, GREEN)
        r4 = rtxt("别忘了写范围 0 < x < 10", -1.6, 27, RED)
        for m in (r1, r2, r3, r4):
            self.play(Write(m), run_time=0.5)
        self.finish_section()

        # ---------- 2. 四个步骤 ----------
        self.section(2, "建模四步")
        self.play(FadeOut(s1), FadeOut(s2), FadeOut(s3), FadeOut(s4), FadeOut(s5),
                  FadeOut(r1), FadeOut(r2), FadeOut(r3), FadeOut(r4), run_time=0.5)

        steps = []
        for i, (name, col) in enumerate([("设变量", BLUE), ("列关系", GOLD),
                                         ("定范围", ORANGE), ("求最值", GREEN)]):
            box = RoundedRectangle(corner_radius=0.14, width=1.3, height=0.9,
                                   color=col, stroke_width=2.2,
                                   fill_color=col, fill_opacity=0.14)
            box.move_to([-5.75 + i * 1.42, 0.0, 0])
            t = txt(name, size=24, color=col).move_to(box.get_center())
            steps.append(VGroup(box, t))
        self.play(LaggedStart(*[FadeIn(s, shift=RIGHT * 0.12) for s in steps],
                              lag_ratio=0.22), run_time=1.3)

        r1 = rtxt("第一步：设变量，写清单位", 1.45, 28, BLUE)
        r2 = rtxt("第二步：用条件列关系", 0.5, 28, GOLD)
        r3 = rtxt("第三步：写实际范围", -0.55, 28, ORANGE)
        r4 = rtxt("第四步：在范围内求最值", -1.6, 28, GREEN)
        for m in (r1, r2, r3, r4):
            self.play(Write(m), run_time=0.5)

        warn = txt("少了第三步，最容易错", size=26, color=RED).move_to([-4.1, -2.35, 0])
        self.play(FadeIn(warn), run_time=0.5)
        self.finish_section()

        # ---------- 3. 顶点就是正方形 ----------
        self.section(3, "顶点在 x = 5，正好是正方形")
        self.play(FadeOut(VGroup(*steps)), FadeOut(warn),
                  FadeOut(r1), FadeOut(r2), FadeOut(r3), FadeOut(r4), run_time=0.5)

        ax = axes_at(-4.2, 0.25, [0, 10, 1], [0, 28, 5], xlen=4.6, ylen=3.0)
        self.play(Create(ax), run_time=0.8)
        para = ax.plot(lambda x: -x * x + 10 * x, x_range=[0.2, 9.8],
                       color=GOLD, stroke_width=3.4)
        self.play(Create(para), run_time=1.4)

        v = Dot(ax.c2p(5, 25), radius=0.11, color=RED)
        self.play(FadeIn(v), run_time=0.5)
        vl = txt("(5, 25)", size=22, color=RED).move_to(ax.c2p(5, 25) + UP * 0.45)
        self.play(FadeIn(vl), run_time=0.4)

        d = DashedLine(ax.c2p(5, 0), ax.c2p(5, 25), color=DIM, stroke_width=2)
        self.play(Create(d), run_time=0.5)

        sq = Rectangle(width=1.5, height=1.5, color=GREEN, stroke_width=3,
                       fill_color=GREEN, fill_opacity=0.15).move_to([-1.5, 1.0, 0])
        self.play(Create(sq), run_time=0.7)
        sqt = txt("5 × 5 = 25", size=24, color=GREEN).move_to([-1.5, 0.0, 0])
        self.play(FadeIn(sqt), run_time=0.5)

        r1 = rtxt("开口向下，最值在顶点", 1.45, 29)
        r2 = rtxt("x = 5 时，面积最大 25", 0.5, 31, GOLD)
        r3 = rtxt("长和宽相等，围成正方形", -0.55, 29, GREEN)
        r4 = rtxt("这是周长固定时的一般结论", -1.6, 26, DIM)
        for m in (r1, r2, r3, r4):
            self.play(Write(m), run_time=0.5)
        self.finish_section()

        # ---------- 4. 指数模型 ----------
        self.section(4, "增长率问题：指数模型")
        self.play(FadeOut(ax), FadeOut(para), FadeOut(v), FadeOut(vl), FadeOut(d),
                  FadeOut(sq), FadeOut(sqt),
                  FadeOut(r1), FadeOut(r2), FadeOut(r3), FadeOut(r4), run_time=0.5)

        ax = axes_at(-4.2, 0.15, [0, 5, 1], [0, 6, 1], xlen=4.6, ylen=3.2)
        self.play(Create(ax), run_time=0.8)
        line = ax.plot(lambda x: 1 + 0.9 * x, x_range=[0, 4.6], color=DIM, stroke_width=2.6)
        expo = ax.plot(lambda x: 1.0 * 1.45 ** x, x_range=[0, 4.4], color=GOLD, stroke_width=3.4)
        self.play(Create(line), run_time=0.8)
        self.play(Create(expo), run_time=1.2)

        ll = txt("线性增长", size=21, color=DIM).move_to(ax.c2p(3.4, 4.6))
        le = txt("指数增长", size=21, color=GOLD).move_to(ax.c2p(3.1, 5.6))
        self.play(FadeIn(ll), FadeIn(le), run_time=0.5)

        r1 = rtxt("每期乘同一个倍数", 1.45, 30, GOLD)
        r2 = rtxt("y = a(1 + r)ˣ", 0.5, 34, CHALK)
        r3 = rtxt("增长用加号，衰减用减号", -0.55, 28)
        r4 = rtxt("它的变化越来越快", -1.6, 27, DIM)
        for m in (r1, r2, r3, r4):
            self.play(Write(m), run_time=0.5)
        self.finish_section()

        # ---------- 5. 两年各涨 10% ----------
        self.section(5, "两期各涨 10%，不是涨 20%")
        self.play(FadeOut(ax), FadeOut(line), FadeOut(expo), FadeOut(ll), FadeOut(le),
                  FadeOut(r1), FadeOut(r2), FadeOut(r3), FadeOut(r4), run_time=0.5)

        c1 = txt("第一年：× 1.1", size=32, color=CHALK).move_to([-4.2, 1.45, 0])
        c2 = txt("第二年：再 × 1.1", size=32, color=CHALK).move_to([-4.2, 0.6, 0])
        c3 = txt("1.1 × 1.1 = 1.21", size=40, color=GOLD).move_to([-4.2, -0.45, 0])
        c4 = txt("一共涨了 21%", size=32, color=GREEN).move_to([-4.2, -1.4, 0])
        for m in (c1, c2, c3, c4):
            self.play(Write(m), run_time=0.6)

        wrong = txt("100 × (1 + 10% × 2) = 120", size=24, color=RED).move_to([-4.2, -1.95, 0])
        self.play(FadeIn(wrong), run_time=0.5)
        cross = VGroup(
            Line([-6.3, -1.8, 0], [-2.1, -2.12, 0], color=RED, stroke_width=3),
            Line([-6.3, -2.12, 0], [-2.1, -1.8, 0], color=RED, stroke_width=3),
        )
        self.play(Create(cross), run_time=0.6)

        r1 = rtxt("增长率不能线性相加", 1.45, 30, RED)
        r2 = rtxt("100 × 1.21 = 121 元", 0.5, 30, GOLD)
        r3 = rtxt("求平均增长率要用开方", -0.55, 28)
        r4 = rtxt("n 期就是 (1 + r)ⁿ", -1.6, 27, DIM)
        for m in (r1, r2, r3, r4):
            self.play(Write(m), run_time=0.5)
        self.finish_section()

        # ---------- 6. 口诀 ----------
        self.section(6, "记一句话")
        self.play(FadeOut(c1), FadeOut(c2), FadeOut(c3), FadeOut(c4), FadeOut(wrong),
                  FadeOut(cross),
                  FadeOut(r1), FadeOut(r2), FadeOut(r3), FadeOut(r4), run_time=0.5)

        k1 = txt("先建模，再求解", size=54, color=GOLD).move_to([0, 1.0, 0])
        k2 = txt("设变量、列关系、定范围、求最值", size=30, color=CHALK).move_to([0, -0.1, 0])
        k3 = txt("算完回到题目，检验是否符合实际", size=29, color=GREEN).move_to([0, -1.15, 0])
        self.play(Write(k1), run_time=0.9)
        self.play(Write(k2), run_time=0.7)
        self.play(Write(k3), run_time=0.7)
        self.finish_section()

        self.play(FadeOut(k1), FadeOut(k2), FadeOut(k3), run_time=0.6)