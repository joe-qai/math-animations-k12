# -*- coding: utf-8 -*-
"""初升高衔接 2：二次函数图像与根的分布。判别式、两根与 k 的关系、区间根。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


def P(x, y):
    return np.array([float(x), float(y), 0.0])


def base_axes(cx=-3.7, cy=-0.1, xr=None, yr=None, xl=4.3, yl=3.4):
    ax = Axes(
        x_range=xr or [0, 4.4, 1],
        y_range=yr or [-1.8, 3.4, 1],
        x_length=xl,
        y_length=yl,
        axis_config={"color": DIM, "stroke_width": 2.0,
                     "include_numbers": False, "tip_length": 0.16},
    )
    ax.move_to(P(cx, cy))
    return ax


class H0ErciHanshuGenScene(NarratedScene):
    lesson = "h0-erci-hanshu-gen"

    def clear_stage(self, run_time: float = 0.5):
        keep = {id(self._track), id(self._fill)}
        junk = [m for m in self.mobjects if id(m) not in keep]
        if junk:
            self.play(*[FadeOut(m) for m in junk], run_time=run_time)
        self.cur_title = None
        self.cur_sub = None

    # ---------------- 0. 高中要问的是「根在哪」 ---------------- 25.2
    def scene_intro(self):
        self.section(0, "根的分布：从图像看根的位置")

        chips = [(-4.7, "初中：画图求最值", DIM), (-1.55, "高中：根的位置", GOLD),
                 (1.6, "工具：二次函数图像", GREEN), (4.75, "先 Δ，再轴，后端点", BLUE)]
        for cx, name, col in chips:
            c = label_box(name, size=19, color=col).move_to([cx, 1.78, 0])
            if c.width > 3.2:
                c.scale_to_fit_width(3.2)
            self.play(FadeIn(c, shift=UP * 0.04), run_time=0.6)
        self.wait(0.4)

        rows = [
            ("题目不再问「图长什么样」", CHALK),
            ("而是问：两根落在哪里", GOLD),
            ("都在 k 右边？分居两边？在区间内？", CHALK),
        ]
        y = 0.75
        for s, col in rows:
            t = txt(s, size=24, color=col).move_to([0, y, 0])
            if t.width > 10.6:
                t.scale_to_fit_width(10.6)
            self.play(FadeIn(t, shift=UP * 0.04), run_time=0.8)
            y -= 0.8
        self.wait(0.5)

        box = label_box("图像不动，条件在变", size=23, color=GOLD)
        box.move_to([0, -2.3, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.0)
        self.wait(6.0)
        self.finish_section()

    # ---------------- 1. 图像三要素 ---------------- 23.0
    def scene_basic(self):
        self.section(1, "图像三要素：开口、对称轴、顶点")

        ax = base_axes()
        self.play(Create(ax), run_time=0.9)
        curve = ax.plot(lambda x: x * x - 4 * x + 3, x_range=[0.12, 3.9],
                        color=GOLD, stroke_width=2.8)
        self.play(Create(curve), run_time=1.2)

        axis_line = DashedLine(ax.c2p(2, -1), ax.c2p(2, 3.0), color=RED,
                              stroke_width=1.8, dash_length=0.09)
        self.play(Create(axis_line), run_time=0.7)
        self.play(FadeIn(Dot(ax.c2p(2, -1), radius=0.07, color=RED)), run_time=0.45)
        self.play(FadeIn(txt("顶点 (2, −1)", size=18, color=RED).move_to(P(-1.05, -1.23))),
                  run_time=0.55)
        self.play(FadeIn(txt("x = 2", size=18, color=RED).move_to(P(-3.78, 1.85))),
                  run_time=0.5)
        for xv in (1, 3):
            self.play(FadeIn(Dot(ax.c2p(xv, 0), radius=0.06, color=GREEN)), run_time=0.4)
        self.play(FadeIn(txt("x₁ = 1", size=18, color=GREEN).move_to(ax.c2p(0.75, -0.42))),
                  FadeIn(txt("x₂ = 3", size=18, color=GREEN).move_to(ax.c2p(3.25, -0.42))),
                  run_time=0.6)
        self.wait(0.4)

        rows = [
            ("开口：a > 0 向上，a < 0 向下", GOLD),
            ("对称轴：x = −b / (2a)", GREEN),
            ("顶点：把对称轴代回函数", BLUE),
            ("三样定了，图就定了大半", ORANGE),
        ]
        y = 1.95
        for s, col in rows:
            t = txt(s, size=20, color=col).move_to([2.15, y, 0])
            if t.width > 6.0:
                t.scale_to_fit_width(6.0)
            self.play(FadeIn(t, shift=RIGHT * 0.04), run_time=0.65)
            y -= 0.82
        self.wait(0.4)
        self.finish_section()

    # ---------------- 2. 判别式决定交点个数 ---------------- 21.1
    def scene_delta(self):
        self.section(2, "交点个数：判别式说了算")

        ax = base_axes(cx=-3.6, cy=-0.1, xr=[-1.6, 3.8], yr=[-2.6, 3.2],
                       xl=4.4, yl=3.4)
        self.play(Create(ax), run_time=0.9)

        c1 = ax.plot(lambda x: x * x - 2 * x - 1, x_range=[-0.72, 2.72],
                     color=GOLD, stroke_width=2.6)
        self.play(Create(c1), run_time=1.0)
        c2 = ax.plot(lambda x: x * x - 2 * x + 1, x_range=[-0.62, 2.62],
                     color=GREEN, stroke_width=2.6)
        self.play(Create(c2), run_time=1.0)
        c3 = ax.plot(lambda x: x * x - 2 * x + 3, x_range=[-0.05, 2.05],
                     color=RED, stroke_width=2.6)
        self.play(Create(c3), run_time=1.0)
        self.wait(0.4)

        rows = [
            ("Δ = b² − 4ac", CHALK),
            ("Δ > 0：两个交点", GOLD),
            ("Δ = 0：一个交点（重根）", GREEN),
            ("Δ < 0：没有交点", RED),
        ]
        y = 1.95
        for s, col in rows:
            t = txt(s, size=21, color=col).move_to([2.15, y, 0])
            if t.width > 6.0:
                t.scale_to_fit_width(6.0)
            self.play(FadeIn(t, shift=RIGHT * 0.04), run_time=0.65)
            y -= 0.86
        self.wait(0.4)

        box = label_box("先算 Δ，再谈根在哪", size=21, color=GOLD)
        box.move_to([2.15, -2.05, 0])
        self.play(FadeIn(box, scale=0.97), run_time=0.9)
        self.wait(3.5)
        self.finish_section()

    # ---------------- 3. 模型一：两根都大于 k ---------------- 24.7
    def scene_both_right(self):
        self.section(3, "模型一：两根都大于 k")

        ax = base_axes()
        self.play(Create(ax), run_time=0.9)
        curve = ax.plot(lambda x: x * x - 4 * x + 3, x_range=[0.12, 3.9],
                        color=GOLD, stroke_width=2.8)
        self.play(Create(curve), run_time=1.1)

        k = 0.6
        kline = DashedLine(ax.c2p(k, -1.7), ax.c2p(k, 3.2), color=BLUE,
                           stroke_width=1.8, dash_length=0.09)
        self.play(Create(kline), run_time=0.6)
        self.play(FadeIn(txt("k", size=20, color=BLUE).move_to(ax.c2p(k, -2.0))), run_time=0.4)
        self.play(FadeIn(Dot(ax.c2p(k, k * k - 4 * k + 3), radius=0.07, color=BLUE)),
                  run_time=0.45)
        self.play(FadeIn(txt("f(k) > 0", size=18, color=BLUE).move_to(P(-1.15, -0.5))),
                  run_time=0.5)
        for xv in (1, 3):
            self.play(FadeIn(Dot(ax.c2p(xv, 0), radius=0.06, color=GREEN)), run_time=0.35)
        self.wait(0.4)

        rows = [
            ("① Δ > 0：有两个根", GOLD),
            ("② 对称轴在 k 右边", GREEN),
            ("③ f(k) > 0：k 在两根之外", BLUE),
        ]
        y = 1.9
        for s, col in rows:
            t = txt(s, size=21, color=col).move_to([2.2, y, 0])
            if t.width > 6.0:
                t.scale_to_fit_width(6.0)
            self.play(FadeIn(t, shift=RIGHT * 0.04), run_time=0.7)
            y -= 1.0
        self.wait(0.4)

        box = label_box("三条同时成立，缺一不可", size=21, color=RED)
        box.move_to([2.2, -2.0, 0])
        if box.width > 6.0:
            box.scale_to_fit_width(6.0)
        self.play(FadeIn(box, scale=0.97), run_time=0.9)
        self.wait(4.0)
        self.finish_section()

    # ---------------- 4. 模型二：k 在两根之间 ---------------- 24.0
    def scene_between(self):
        self.section(4, "模型二：两根在 k 的两侧")

        ax = base_axes()
        self.play(Create(ax), run_time=0.9)
        curve = ax.plot(lambda x: x * x - 4 * x + 3, x_range=[0.12, 3.9],
                        color=GOLD, stroke_width=2.8)
        self.play(Create(curve), run_time=1.1)

        kline = DashedLine(ax.c2p(2, -1), ax.c2p(2, 3.2), color=BLUE,
                           stroke_width=1.8, dash_length=0.09)
        self.play(Create(kline), run_time=0.6)
        self.play(FadeIn(Dot(ax.c2p(2, -1), radius=0.08, color=RED)), run_time=0.45)
        self.play(FadeIn(txt("f(k) < 0", size=19, color=RED).move_to(P(-1.05, -1.6))),
                  run_time=0.5)
        for xv, dx in ((1, -0.42), (3, 0.42)):
            self.play(FadeIn(Dot(ax.c2p(xv, 0), radius=0.06, color=GREEN)), run_time=0.35)
        self.wait(0.4)

        rows = [
            ("k 夹在两根之间 ⇔ f(k) < 0", CHALK),
            ("不用再看 Δ：一定有交点", GOLD),
            ("一根在 k 左，一根在 k 右", GREEN),
        ]
        y = 1.9
        for s, col in rows:
            t = txt(s, size=21, color=col).move_to([2.2, y, 0])
            if t.width > 6.0:
                t.scale_to_fit_width(6.0)
            self.play(FadeIn(t, shift=RIGHT * 0.04), run_time=0.75)
            y -= 1.0
        self.wait(0.4)

        box = label_box("一个符号，判断完毕", size=22, color=GOLD)
        box.move_to([2.2, -1.95, 0])
        self.play(FadeIn(box, scale=0.97), run_time=0.9)
        self.wait(5.0)
        self.finish_section()

    # ---------------- 5. 模型三：根落在区间里 ---------------- 25.7
    def scene_interval(self):
        self.section(5, "模型三：根落在区间里")

        ax = base_axes()
        self.play(Create(ax), run_time=0.9)
        curve = ax.plot(lambda x: x * x - 4 * x + 3, x_range=[0.12, 3.9],
                        color=GOLD, stroke_width=2.8)
        self.play(Create(curve), run_time=1.1)

        m, n = 0.55, 3.45
        x1 = ax.c2p(m, 0)[0]
        x2 = ax.c2p(n, 0)[0]
        cy = ax.c2p(0, 0.4)[1]
        band = Rectangle(width=x2 - x1, height=3.2, stroke_width=0,
                         fill_color=GREEN, fill_opacity=0.10)
        band.move_to([(x1 + x2) / 2, cy, 0])
        self.play(FadeIn(band), run_time=0.7)
        self.play(Create(DashedLine(ax.c2p(m, -1.7), ax.c2p(m, 3.2), color=GREEN,
                                    stroke_width=1.6, dash_length=0.08)),
                  Create(DashedLine(ax.c2p(n, -1.7), ax.c2p(n, 3.2), color=GREEN,
                                    stroke_width=1.6, dash_length=0.08)), run_time=0.7)
        self.play(FadeIn(txt("m", size=19, color=GREEN).move_to(ax.c2p(m, -2.0))),
                  FadeIn(txt("n", size=19, color=GREEN).move_to(ax.c2p(n, -2.0))),
                  run_time=0.5)
        for xv in (1, 3):
            self.play(FadeIn(Dot(ax.c2p(xv, 0), radius=0.06, color=GOLD)), run_time=0.35)
        self.wait(0.4)

        rows = [
            ("① Δ ≥ 0：有实根", GOLD),
            ("② m < 对称轴 < n", GREEN),
            ("③ f(m) > 0 且 f(n) > 0", BLUE),
            ("只有一根在区间：f(m)·f(n) < 0", ORANGE),
        ]
        y = 1.95
        for s, col in rows:
            t = txt(s, size=20, color=col).move_to([2.25, y, 0])
            if t.width > 6.0:
                t.scale_to_fit_width(6.0)
            self.play(FadeIn(t, shift=RIGHT * 0.04), run_time=0.7)
            y -= 0.9
        self.wait(0.4)
        self.finish_section()

    # ---------------- 6. 三个提醒 ---------------- 24.2
    def scene_traps(self):
        self.section(6, "三个提醒")

        rows = [
            ("① 条件靠画图验证，不靠背", "图像一画，条件就出来了"),
            ("② 端点能否取到单独算", "大于与大于等于差一个点"),
            ("③ 别忘判别式", "没有交点时，后面条件全是空的"),
        ]
        y = 1.75
        for a, b in rows:
            ta = txt(a, size=22, color=RED).move_to([-2.35, y, 0])
            if ta.width > 5.6:
                ta.scale_to_fit_width(5.6)
            self.play(FadeIn(ta, shift=RIGHT * 0.04), run_time=0.6)
            tb = txt(b, size=19, color=DIM).move_to([3.75, y, 0])
            if tb.width > 5.9:
                tb.scale_to_fit_width(5.9)
            self.play(FadeIn(tb, shift=RIGHT * 0.04), run_time=0.6)
            y -= 1.05
        self.wait(0.8)

        box = label_box("先看 Δ，再看轴，最后看端点", size=24, color=GOLD)
        box.move_to([0, -2.35, 0])
        if box.width > 11.0:
            box.scale_to_fit_width(11.0)
        self.play(FadeIn(box, scale=0.97), run_time=1.1)
        self.wait(8.0)
        self.finish_section()

    def construct(self):
        self.scene_intro()
        self.clear_stage()
        self.scene_basic()
        self.clear_stage()
        self.scene_delta()
        self.clear_stage()
        self.scene_both_right()
        self.clear_stage()
        self.scene_between()
        self.clear_stage()
        self.scene_interval()
        self.clear_stage()
        self.scene_traps()
        self.clear_stage(0.8)