# -*- coding: utf-8 -*-
"""函数与方程、不等式的图像：交点即解，图像上下即大小。九年级下。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


def P(x, y):
    return np.array([float(x), float(y), 0.0])


def mk_axes(xr, yr, xl=5.4, yl=3.2, pos=(-3.2, -0.15)):
    ax = Axes(
        x_range=xr,
        y_range=yr,
        x_length=xl,
        y_length=yl,
        axis_config={"color": DIM, "stroke_width": 2.0,
                     "include_numbers": False, "tip_length": 0.16},
    )
    ax.move_to(np.array([float(pos[0]), float(pos[1]), 0.0]))
    return ax


class HanshuFangchengTuxiangScene(NarratedScene):
    lesson = "hanshu-fangcheng-tuxiang"

    def clear_stage(self, run_time: float = 0.5):
        keep = {id(self._track), id(self._fill)}
        junk = [m for m in self.mobjects if id(m) not in keep]
        if junk:
            self.play(*[FadeOut(m) for m in junk], run_time=run_time)
        self.cur_title = None
        self.cur_sub = None

    # ---------------- 0. 两家快递 ---------------- 26.7
    def scene_intro(self):
        self.section(0, "两家快递，哪家便宜")

        ax = mk_axes([0, 10, 2], [0, 30, 10], 5.2, 3.3, (-3.1, -0.2))
        self.play(Create(ax), run_time=1.0)

        la = ax.plot(lambda x: 10 + 2 * x, x_range=[0, 9.2], color=GOLD, stroke_width=3.0)
        lb = ax.plot(lambda x: 6 + 3 * x, x_range=[0, 7.6], color=BLUE, stroke_width=3.0)
        self.play(Create(la), run_time=1.2)
        self.play(Create(lb), run_time=1.2)
        self.wait(0.5)

        dot = Dot(ax.c2p(4, 18), radius=0.08, color=RED)
        self.play(FadeIn(dot, scale=0.8), run_time=0.6)
        self.wait(0.4)

        rows = [
            ("甲：10 + 2x", GOLD),
            ("乙：6 + 3x", BLUE),
            ("交点：两家收费相同", RED),
            ("交点左边：乙更便宜", BLUE),
            ("交点右边：甲更便宜", GOLD),
        ]
        y = 1.95
        for s, col in rows:
            t = txt(s, size=22, color=col).move_to([3.4, y, 0])
            self.play(FadeIn(t, shift=RIGHT * 0.04), run_time=0.8)
            y -= 0.68
        self.wait(0.6)

        box = label_box("两条直线的交点，就是收费相同的时刻", size=21, color=RED)
        box.move_to([3.4, -1.75, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.0)
        self.wait(9.0)
        self.finish_section()

    # ---------------- 1. 一次函数与方程 ---------------- 22.9
    def scene_linear_eq(self):
        self.section(1, "交点的横坐标就是解")

        ax = mk_axes([-3, 3, 1], [-3, 5, 2], 4.9, 3.1, (-3.5, -0.2))
        self.play(Create(ax), run_time=1.0)

        line = ax.plot(lambda x: x + 1, x_range=[-2.9, 2.4], color=GOLD, stroke_width=3.0)
        self.play(Create(line), run_time=1.2)
        self.play(FadeIn(txt("y = kx + b", size=21, color=GOLD).move_to([-1.55, 2.4, 0])),
                  run_time=0.6)

        dot = Dot(ax.c2p(-1, 0), radius=0.08, color=RED)
        dash = DashedLine(ax.c2p(-1, 0), ax.c2p(-1, -1.9), color=RED, stroke_width=1.7,
                          dash_length=0.09)
        self.play(FadeIn(dot), Create(dash), run_time=0.8)
        self.play(FadeIn(txt("x = −1", size=21, color=RED).move_to([-1.87, -1.6, 0])),
                  run_time=0.6)
        self.wait(0.6)

        rows = [
            ("令 y = 0，解 kx + b = 0", CHALK),
            ("解就是与 x 轴交点的横坐标", GOLD),
            ("令 y = m，解就是与直线 y = m 的交点", BLUE),
        ]
        y = 1.55
        for s, col in rows:
            t = txt(s, size=22, color=col).move_to([3.2, y, 0])
            self.play(FadeIn(t, shift=RIGHT * 0.04), run_time=0.9)
            y -= 0.9
        self.wait(0.6)

        note = txt("解方程，就是在图像上找交点", size=23, color=RED).move_to([3.2, -1.35, 0])
        self.play(FadeIn(note, shift=UP * 0.04), run_time=0.9)
        self.wait(7.0)
        self.finish_section()

    # ---------------- 2. 一次函数与不等式 ---------------- 22.9
    def scene_linear_ineq(self):
        self.section(2, "看上方还是下方")

        ax = mk_axes([-2, 4, 1], [-3, 4, 2], 5.0, 3.0, (-3.4, -0.15))
        self.play(Create(ax), run_time=1.0)

        up = ax.plot(lambda x: x - 1, x_range=[1, 3.8], color=GOLD, stroke_width=7.0)
        dn = ax.plot(lambda x: x - 1, x_range=[-1.9, 1], color=DIM, stroke_width=3.0)
        self.play(Create(dn), run_time=0.8)
        self.play(Create(up), run_time=0.9)
        dot = Dot(ax.c2p(1, 0), radius=0.07, color=RED)
        self.play(FadeIn(dot), run_time=0.5)
        self.play(FadeIn(txt("1", size=19, color=RED).move_to([1.1, -0.82, 0])), run_time=0.4)
        self.wait(0.6)

        rows = [
            ("x 轴上方：函数值大于 0", GOLD),
            ("x 轴下方：函数值小于 0", DIM),
            ("kx + b > 0 的解集看上方那一段", CHALK),
        ]
        y = 1.5
        for s, col in rows:
            t = txt(s, size=22, color=col).move_to([3.3, y, 0])
            self.play(FadeIn(t, shift=RIGHT * 0.04), run_time=0.9)
            y -= 0.85
        self.wait(0.6)

        cmp1 = txt("两个函数比大小：看谁在上、谁在下", size=22, color=BLUE)
        cmp1.move_to([3.3, -1.2, 0])
        self.play(FadeIn(cmp1, shift=UP * 0.04), run_time=0.9)
        box = label_box("上方函数值大，下方函数值小", size=21, color=RED)
        box.move_to([3.3, -2.05, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.0)
        self.wait(7.5)
        self.finish_section()

    # ---------------- 3. 二次函数与判别式 ---------------- 28.1
    def scene_quad_eq(self):
        self.section(3, "抛物线与 x 轴的交点个数")

        cases = [
            (-4.15, lambda x: x * x - 2, "Δ > 0", "两个交点", "两个根", GOLD),
            (0.0, lambda x: x * x, "Δ = 0", "一个交点", "两个相等根", GREEN),
            (4.15, lambda x: x * x + 1, "Δ < 0", "没有交点", "没有实数根", RED),
        ]
        for cx, fn, dtag, cnt, root, col in cases:
            ax = Axes(x_range=[-2.2, 2.2, 2], y_range=[-2.5, 4, 2], x_length=2.9, y_length=1.9,
                      axis_config={"color": DIM, "stroke_width": 1.6,
                                   "include_numbers": False, "tip_length": 0.12})
            ax.move_to([cx, 0.95, 0])
            self.play(Create(ax), run_time=0.7)
            curve = ax.plot(fn, x_range=[-1.95, 1.95], color=col, stroke_width=3.0)
            self.play(Create(curve), run_time=1.0)
            self.play(FadeIn(txt(dtag, size=22, color=col).move_to([cx, -0.85, 0])),
                      run_time=0.5)
            self.play(FadeIn(txt(cnt, size=21, color=CHALK).move_to([cx, -1.35, 0])),
                      run_time=0.5)
            self.play(FadeIn(txt(root, size=19, color=DIM).move_to([cx, -1.8, 0])),
                      run_time=0.5)
        self.wait(0.8)

        d = txt("ax² + bx + c = 0 的根，就是交点的横坐标", size=26, color=CHALK)
        d.move_to([0, 2.85, 0])
        self.play(FadeIn(d, shift=UP * 0.04), run_time=1.0)
        box = label_box("交点个数 = 实数根的个数", size=23, color=GOLD)
        box.move_to([0, -2.6, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.0)
        self.wait(12.0)
        self.finish_section()

    # ---------------- 4. 二次不等式 ---------------- 23.5
    def scene_quad_ineq(self):
        self.section(4, "大于取两边，小于取中间")

        ax = Axes(x_range=[-2, 4, 1], y_range=[-4, 4, 2], x_length=5.0, y_length=2.9,
                  axis_config={"color": DIM, "stroke_width": 2.0,
                               "include_numbers": False, "tip_length": 0.15})
        ax.move_to([-3.3, -0.25, 0])
        self.play(Create(ax), run_time=0.9)

        curve = ax.plot(lambda x: (x - 1) ** 2 - 2.25, x_range=[-1.7, 3.7],
                        color=CHALK, stroke_width=3.0)
        self.play(Create(curve), run_time=1.2)

        left = ax.plot(lambda x: (x - 1) ** 2 - 2.25, x_range=[-1.7, -0.5],
                       color=GOLD, stroke_width=7.0)
        right = ax.plot(lambda x: (x - 1) ** 2 - 2.25, x_range=[2.5, 3.7],
                        color=GOLD, stroke_width=7.0)
        mid = ax.plot(lambda x: (x - 1) ** 2 - 2.25, x_range=[-0.5, 2.5],
                      color=GREEN, stroke_width=7.0)
        self.play(Create(left), Create(right), run_time=1.0)
        self.play(Create(mid), run_time=0.8)
        for xv in (-0.5, 2.5):
            self.add(Dot(ax.c2p(xv, 0), radius=0.06, color=RED))
        self.wait(0.6)

        t1 = txt("开口向上：大于 0 取两边", size=24, color=GOLD).move_to([3.2, 1.5, 0])
        self.play(FadeIn(t1, shift=RIGHT * 0.04), run_time=0.9)
        t2 = txt("小于 0 取中间", size=24, color=GREEN).move_to([3.2, 0.65, 0])
        self.play(FadeIn(t2, shift=RIGHT * 0.04), run_time=0.9)
        t3 = txt("开口向下正好相反", size=22, color=BLUE).move_to([3.2, -0.3, 0])
        self.play(FadeIn(t3, shift=RIGHT * 0.04), run_time=0.9)
        self.wait(0.7)

        box = label_box("先看开口方向，再读范围", size=22, color=RED)
        box.move_to([3.2, -1.7, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.0)
        self.wait(8.0)
        self.finish_section()

    # ---------------- 5. 例题 ---------------- 27.9
    def scene_example(self):
        self.section(5, "例：y = x² − 2x − 3")

        ax = Axes(x_range=[-2.5, 4.5, 1], y_range=[-5, 6, 2], x_length=5.2, y_length=3.3,
                  axis_config={"color": DIM, "stroke_width": 2.0,
                               "include_numbers": False, "tip_length": 0.15})
        ax.move_to([-3.15, -0.1, 0])
        self.play(Create(ax), run_time=1.0)
        curve = ax.plot(lambda x: x * x - 2 * x - 3, x_range=[-1.75, 3.75],
                        color=CHALK, stroke_width=3.0)
        self.play(Create(curve), run_time=1.3)

        for xv, lab in ((-1, "−1"), (3, "3")):
            self.add(Dot(ax.c2p(xv, 0), radius=0.07, color=RED))
            self.play(FadeIn(txt(lab, size=19, color=RED).move_to(ax.c2p(xv, 0) + DOWN * 0.42)),
                      run_time=0.4)
        self.wait(0.4)

        left = ax.plot(lambda x: x * x - 2 * x - 3, x_range=[-1.75, -1],
                       color=GOLD, stroke_width=7.0)
        right = ax.plot(lambda x: x * x - 2 * x - 3, x_range=[3, 3.75],
                        color=GOLD, stroke_width=7.0)
        mid = ax.plot(lambda x: x * x - 2 * x - 3, x_range=[-1, 3],
                      color=GREEN, stroke_width=7.0)
        self.play(Create(left), Create(right), run_time=0.9)
        self.play(Create(mid), run_time=0.8)
        self.wait(0.5)

        steps = [
            ("令 y = 0：(x − 3)(x + 1) = 0", CHALK),
            ("交点是 −1 和 3", CHALK),
            ("x² − 2x − 3 > 0：x < −1 或 x > 3", GOLD),
            ("x² − 2x − 3 < 0：−1 < x < 3", GREEN),
        ]
        y = 1.75
        for s, col in steps:
            t = txt(s, size=21, color=col).move_to([3.35, y, 0])
            self.play(FadeIn(t, shift=RIGHT * 0.04), run_time=0.9)
            y -= 0.88
        self.wait(0.7)

        box = label_box("端点不含等号，画空心", size=21, color=RED).move_to([3.35, -1.95, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.0)
        self.wait(9.0)
        self.finish_section()

    # ---------------- 6. 易错点 ---------------- 24.7
    def scene_traps(self):
        self.section(6, "四个易错点")

        rows = [
            ("① 横纵坐标搞混", "方程的解是横坐标"),
            ("② 不看开口方向", "开口向下，口诀要反"),
            ("③ 端点取不取", "大于 0 不含等号"),
            ("④ 算完不核对", "回到图像上看一眼"),
        ]
        y = 1.85
        for a, b in rows:
            ta = txt(a, size=23, color=RED).move_to([-2.6, y, 0])
            tb = txt(b, size=21, color=DIM).move_to([3.6, y, 0])
            self.play(FadeIn(ta, shift=RIGHT * 0.04), run_time=0.65)
            self.play(FadeIn(tb, shift=RIGHT * 0.04), run_time=0.65)
            y -= 0.86
        self.wait(1.0)

        box = label_box("先画图，再找交点，最后读范围", size=23, color=GOLD)
        box.move_to([0, -2.45, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.1)
        self.wait(10.0)
        self.finish_section()

    def construct(self):
        self.scene_intro()
        self.clear_stage()
        self.scene_linear_eq()
        self.clear_stage()
        self.scene_linear_ineq()
        self.clear_stage()
        self.scene_quad_eq()
        self.clear_stage()
        self.scene_quad_ineq()
        self.clear_stage()
        self.scene_example()
        self.clear_stage()
        self.scene_traps()
        self.clear_stage(0.8)