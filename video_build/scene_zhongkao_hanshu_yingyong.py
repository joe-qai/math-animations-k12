# -*- coding: utf-8 -*-
"""中考专题 3：函数及其应用。一次函数、反比例函数、二次函数、最值区间、建模。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


def P(x, y):
    return np.array([float(x), float(y), 0.0])


def mk_axes(xr, yr, xl=4.6, yl=3.0, pos=(-3.7, -0.25)):
    ax = Axes(
        x_range=xr,
        y_range=yr,
        x_length=xl,
        y_length=yl,
        axis_config={"color": DIM, "stroke_width": 2.0,
                     "include_numbers": False, "tip_length": 0.15},
    )
    ax.move_to(np.array([float(pos[0]), float(pos[1]), 0.0]))
    return ax


class ZhongkaoHanshuYingyongScene(NarratedScene):
    lesson = "zhongkao-hanshu-yingyong"

    def clear_stage(self, run_time: float = 0.5):
        keep = {id(self._track), id(self._fill)}
        junk = [m for m in self.mobjects if id(m) not in keep]
        if junk:
            self.play(*[FadeOut(m) for m in junk], run_time=run_time)
        self.cur_title = None
        self.cur_sub = None

    # ---------------- 0. 函数是最大的块 ---------------- 25.5
    def scene_intro(self):
        self.section(0, "函数：分值最高的一块")

        chips = [(-4.35, "一次函数 y = kx + b", GOLD),
                 (0.0, "反比例 y = k/x", GREEN),
                 (4.35, "二次函数 y = ax² + bx + c", BLUE)]
        for cx, name, col in chips:
            c = label_box(name, size=20, color=col).move_to([cx, 1.8, 0])
            c.scale_to_fit_width(min(c.width, 4.0))
            self.play(FadeIn(c, shift=UP * 0.04), run_time=0.8)
        self.wait(0.5)

        rows = [
            ("图像与性质：看 k、b、a 的符号", CHALK),
            ("求解析式：待定系数法", CHALK),
            ("实际应用：利润、拱桥、面积", CHALK),
            ("压轴题：函数与几何结合", RED),
        ]
        y = 0.75
        for s, col in rows:
            t = txt(s, size=23, color=col).move_to([0, y, 0])
            self.play(FadeIn(t, shift=UP * 0.04), run_time=0.7)
            y -= 0.66
        self.wait(0.5)

        box = label_box("图像 · 解析式 · 最值 · 建模", size=23, color=GOLD)
        box.move_to([0, -2.5, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.0)
        self.wait(9.5)
        self.finish_section()

    # ---------------- 1. 一次函数 ---------------- 24.6
    def scene_linear(self):
        self.section(1, "一次函数：k 管增减，b 管截距")

        ax = mk_axes([-2, 4, 1], [-3, 4, 1], 4.4, 3.4, (-3.9, -0.35))
        self.play(Create(ax), run_time=0.9)
        line = ax.plot(lambda x: 2 * x - 1, x_range=[-1.2, 2.4], color=GOLD, stroke_width=3.2)
        self.play(Create(line), run_time=1.0)
        p1 = Dot(ax.c2p(0, -1), radius=0.06, color=RED)
        p2 = Dot(ax.c2p(2, 3), radius=0.06, color=RED)
        self.play(FadeIn(p1), FadeIn(p2), run_time=0.6)
        self.play(FadeIn(txt("(0, −1)", size=18, color=RED).move_to([-3.0, -1.9, 0])),
                  FadeIn(txt("(2, 3)", size=18, color=RED).move_to([-1.0, 1.6, 0])),
                  run_time=0.6)
        self.wait(0.5)

        rows = [
            ("k > 0：y 随 x 增大而增大", GOLD),
            ("b：与 y 轴交点的纵坐标", GOLD),
            ("待定系数法：两点定一条直线", CHALK),
            ("与 x 轴交点 = 方程 kx + b = 0", CHALK),
        ]
        y = 2.15
        for s, col in rows:
            t = txt(s, size=22, color=col).move_to([3.4, y, 0])
            self.play(FadeIn(t, shift=RIGHT * 0.04), run_time=0.75)
            y -= 0.72
        self.wait(0.5)

        box = label_box("k 定方向，b 定位置", size=22, color=GREEN)
        box.move_to([3.4, -1.9, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.0)
        self.wait(9.0)
        self.finish_section()

    # ---------------- 2. 反比例函数 ---------------- 23.5
    def scene_reciprocal(self):
        self.section(2, "反比例函数：两支与矩形面积")

        ax = mk_axes([-4, 4, 1], [-4, 4, 1], 4.2, 3.6, (-3.9, -0.2))
        self.play(Create(ax), run_time=0.9)
        b1 = ax.plot(lambda x: 4 / x, x_range=[0.85, 4.2], color=GREEN, stroke_width=3.0)
        b2 = ax.plot(lambda x: 4 / x, x_range=[-4.2, -0.85], color=GREEN, stroke_width=3.0)
        self.play(Create(b1), Create(b2), run_time=1.3)
        self.wait(0.4)

        rect = Rectangle(width=ax.c2p(2, 0)[0] - ax.c2p(0, 0)[0],
                         height=ax.c2p(0, 2)[1] - ax.c2p(0, 0)[1],
                         color=GOLD, stroke_width=2.0, fill_color=GOLD, fill_opacity=0.12)
        rect.move_to(P(ax.c2p(1, 1)[0], ax.c2p(1, 1)[1]))
        dot = Dot(ax.c2p(2, 2), radius=0.06, color=GOLD)
        self.play(FadeIn(dot), Create(rect), run_time=0.9)
        self.play(FadeIn(txt("S = |k| = 4", size=20, color=GOLD).move_to([-2.6, 1.7, 0])),
                  run_time=0.6)
        self.wait(0.5)

        rows = [
            ("k > 0：一、三象限；k < 0：二、四象限", GREEN),
            ("图像是两支，各自单调", GREEN),
            ("矩形面积 = |k|", GOLD),
            ("与一次函数交点：联立解方程", CHALK),
        ]
        y = 2.15
        for s, col in rows:
            t = txt(s, size=21, color=col).move_to([3.35, y, 0])
            if t.width > 6.4:
                t.scale_to_fit_width(6.4)
            self.play(FadeIn(t, shift=RIGHT * 0.04), run_time=0.75)
            y -= 0.72
        self.wait(0.5)

        box = label_box("只画一支，是常见扣分点", size=21, color=RED)
        box.move_to([3.35, -1.75, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.0)
        self.wait(7.5)
        self.finish_section()

    # ---------------- 3. 二次函数三种形式 ---------------- 25.7
    def scene_quadratic(self):
        self.section(3, "二次函数：三种写法")

        ax = mk_axes([-1, 5, 1], [-2, 4, 1], 3.6, 3.2, (3.7, -0.3))
        self.play(Create(ax), run_time=0.8)
        para = ax.plot(lambda x: x * x - 4 * x + 3, x_range=[0.2, 3.8], color=BLUE, stroke_width=3.0)
        self.play(Create(para), run_time=1.2)
        vline = DashedLine(ax.c2p(2, -1), ax.c2p(2, 4), color=GOLD, stroke_width=1.8,
                           dash_length=0.08)
        vdot = Dot(ax.c2p(2, -1), radius=0.06, color=GOLD)
        self.play(Create(vline), FadeIn(vdot), run_time=0.8)
        self.wait(0.4)

        rows = [
            ("一般式：y = ax² + bx + c", CHALK),
            ("顶点式：y = a(x − h)² + k", GOLD),
            ("交点式：y = a(x − x₁)(x − x₂)", GREEN),
            ("对称轴：x = −b / 2a", BLUE),
            ("开口：a > 0 向上，a < 0 向下", BLUE),
        ]
        y = 2.3
        for s, col in rows:
            t = txt(s, size=21, color=col).move_to([-2.85, y, 0])
            if t.width > 6.6:
                t.scale_to_fit_width(6.6)
            self.play(FadeIn(t, shift=RIGHT * 0.04), run_time=0.7)
            y -= 0.66
        self.wait(0.5)

        box = label_box("给顶点用顶点式，给交点用交点式", size=20, color=GOLD)
        box.move_to([-2.85, -2.2, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.0)
        self.wait(8.5)
        self.finish_section()

    # ---------------- 4. 最值与区间 ---------------- 21.4
    def scene_maxmin(self):
        self.section(4, "最值：先看区间，再看顶点")

        ax = mk_axes([-1, 6, 1], [-2, 5, 1], 5.2, 3.1, (-2.6, -0.3))
        self.play(Create(ax), run_time=0.9)
        para = ax.plot(lambda x: -1 * (x - 1) ** 2 + 4, x_range=[-0.4, 2.6],
                       color=DIM, stroke_width=2.4)
        self.play(Create(para), run_time=1.1)
        part = ax.plot(lambda x: -1 * (x - 1) ** 2 + 4, x_range=[2, 5.2],
                       color=GOLD, stroke_width=3.4)
        self.play(Create(part), run_time=1.0)
        vdot = Dot(ax.c2p(1, 4), radius=0.07, color=BLUE)
        vline = DashedLine(ax.c2p(1, 0), ax.c2p(1, 4), color=BLUE, stroke_width=1.6,
                           dash_length=0.08)
        self.play(FadeIn(vdot), Create(vline), run_time=0.8)
        self.play(FadeIn(txt("顶点 x = 1", size=19, color=BLUE).move_to([-3.9, 1.55, 0])),
                  run_time=0.5)
        self.wait(0.4)

        rows = [
            ("配方：y = −(x − 1)² + 4", CHALK),
            ("题目给的区间：[2, 5]", GOLD),
            ("顶点 x = 1 不在区间内", RED),
            ("所以最大值在端点 x = 2 处", GREEN),
            ("y(2) = 3", GREEN),
        ]
        y = 2.15
        for s, col in rows:
            t = txt(s, size=21, color=col).move_to([3.5, y, 0])
            self.play(FadeIn(t, shift=RIGHT * 0.04), run_time=0.65)
            y -= 0.64
        self.wait(0.5)

        box = label_box("顶点不在区间内，最值在端点", size=21, color=RED)
        box.move_to([3.5, -1.4, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.0)
        self.wait(6.0)
        self.finish_section()

    # ---------------- 5. 应用：利润最大 ---------------- 23.8
    def scene_apply(self):
        self.section(5, "应用：设、列、求最值")

        q = txt("每件利润 x 元，每天卖 40 − 2x 件", size=24, color=CHALK)
        q.move_to([0, 2.1, 0])
        self.play(FadeIn(q, shift=UP * 0.04), run_time=0.85)
        self.wait(0.4)

        f1 = txt("总利润 W = x(40 − 2x)", size=27, color=GOLD).move_to([0, 1.25, 0])
        f2 = txt("= −2(x − 10)² + 200", size=27, color=GREEN).move_to([0, 0.5, 0])
        self.play(FadeIn(f1, shift=UP * 0.04), run_time=0.85)
        self.play(FadeIn(f2, shift=UP * 0.04), run_time=0.85)
        self.wait(0.4)

        note = txt("0 < x < 20，x = 10 时 W 最大，为 200 元", size=24, color=BLUE)
        note.move_to([0, -0.45, 0])
        self.play(FadeIn(note, shift=UP * 0.04), run_time=0.85)
        self.wait(0.4)

        steps = txt("① 设自变量与范围  ② 列关系式  ③ 求顶点  ④ 作答带单位",
                    size=21, color=CHALK)
        steps.move_to([0, -1.2, 0])
        self.play(FadeIn(steps, shift=UP * 0.04), run_time=0.8)
        self.wait(0.5)

        box = label_box("算完要回答题目问的那句话", size=21, color=RED)
        box.move_to([0, -2.4, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.0)
        self.wait(6.0)
        self.finish_section()

    # ---------------- 6. 易错点 ---------------- 20.2
    def scene_traps(self):
        self.section(6, "四个易错点")

        rows = [
            ("① k 的符号说反", "增减性由 k 决定"),
            ("② 反比例只画一支", "两支都要画"),
            ("③ 求最值不看范围", "顶点可能不在区间内"),
            ("④ 忘检验与写单位", "点要代回解析式"),
        ]
        y = 1.85
        for a, b in rows:
            ta = txt(a, size=23, color=RED).move_to([-2.7, y, 0])
            tb = txt(b, size=21, color=DIM).move_to([3.5, y, 0])
            self.play(FadeIn(ta, shift=RIGHT * 0.04), run_time=0.6)
            self.play(FadeIn(tb, shift=RIGHT * 0.04), run_time=0.6)
            y -= 0.86
        self.wait(0.8)

        box = label_box("先看范围，再求最值", size=27, color=GOLD)
        box.move_to([0, -2.45, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.1)
        self.wait(8.0)
        self.finish_section()

    def construct(self):
        self.scene_intro()
        self.clear_stage()
        self.scene_linear()
        self.clear_stage()
        self.scene_reciprocal()
        self.clear_stage()
        self.scene_quadratic()
        self.clear_stage()
        self.scene_maxmin()
        self.clear_stage()
        self.scene_apply()
        self.clear_stage()
        self.scene_traps()
        self.clear_stage(0.8)