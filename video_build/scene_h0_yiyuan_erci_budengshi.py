# -*- coding: utf-8 -*-
"""初升高衔接 3：一元二次不等式。图像法、口诀、Δ 情形、化正、恒成立。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


def P(x, y):
    return np.array([float(x), float(y), 0.0])


def base_axes(cx=-3.75, cy=-0.15, xr=None, yr=None, xl=4.3, yl=3.2):
    ax = Axes(
        x_range=xr or [0.35, 4.6, 1],
        y_range=yr or [-1.2, 4.0, 1],
        x_length=xl,
        y_length=yl,
        axis_config={"color": DIM, "stroke_width": 2.0,
                     "include_numbers": False, "tip_length": 0.16},
    )
    ax.move_to(P(cx, cy))
    return ax


class H0YiyuanErciBudengshiScene(NarratedScene):
    lesson = "h0-yiyuan-erci-budengshi"

    def clear_stage(self, run_time: float = 0.5):
        keep = {id(self._track), id(self._fill)}
        junk = [m for m in self.mobjects if id(m) not in keep]
        if junk:
            self.play(*[FadeOut(m) for m in junk], run_time=run_time)
        self.cur_title = None
        self.cur_sub = None

    # ---------------- 0. 解集是一段范围 ---------------- 21.7
    def scene_intro(self):
        self.section(0, "一元二次不等式：解集是一段范围")

        chips = [(-4.55, "一元一次：移项即完", DIM), (0.0, "一元二次：看图像", GOLD),
                 (4.4, "解集：一段范围", GREEN)]
        for cx, name, col in chips:
            c = label_box(name, size=19, color=col).move_to([cx, 1.78, 0])
            if c.width > 3.9:
                c.scale_to_fit_width(3.9)
            self.play(FadeIn(c, shift=UP * 0.04), run_time=0.65)
        self.wait(0.4)

        rows = [
            ("x² − 5x + 6 > 0，问的不是一个数", CHALK),
            ("而是 x 的整段取值范围", GOLD),
            ("移项硬算行不通，得看图像", CHALK),
        ]
        y = 0.75
        for s, col in rows:
            t = txt(s, size=24, color=col).move_to([0, y, 0])
            if t.width > 10.4:
                t.scale_to_fit_width(10.4)
            self.play(FadeIn(t, shift=UP * 0.04), run_time=0.8)
            y -= 0.8
        self.wait(0.4)

        box = label_box("先画图，再写解集", size=23, color=GOLD)
        box.move_to([0, -2.3, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.0)
        self.wait(4.0)
        self.finish_section()

    # ---------------- 1. 图像法：看横轴上方 ---------------- 24.6
    def scene_graph(self):
        self.section(1, "图像法：找横轴上方的部分")

        ax = base_axes()
        self.play(Create(ax), run_time=0.9)
        curve = ax.plot(lambda x: x * x - 5 * x + 6, x_range=[0.55, 4.45],
                        color=GOLD, stroke_width=2.8)
        self.play(Create(curve), run_time=1.2)

        for xv, lb, dx in ((1, "x₁ = 1", -0.42), (3, "x₂ = 3", 0.42)):
            self.play(FadeIn(Dot(ax.c2p(xv, 0), radius=0.07, color=GOLD)), run_time=0.4)
            self.play(FadeIn(txt(lb, size=18, color=GOLD).move_to(ax.c2p(xv + dx, -0.42))),
                      run_time=0.45)

        a1 = Arrow(ax.c2p(1, 0), ax.c2p(0.44, 0), color=GREEN, stroke_width=5,
                   buff=0, max_tip_length_to_length_ratio=0.28)
        a2 = Arrow(ax.c2p(3, 0), ax.c2p(4.5, 0), color=GREEN, stroke_width=5,
                   buff=0, max_tip_length_to_length_ratio=0.28)
        self.play(Create(a1), run_time=0.6)
        self.play(Create(a2), run_time=0.6)
        self.play(FadeIn(txt("x < 1", size=18, color=GREEN).move_to(ax.c2p(0.72, 0.34))),
                  FadeIn(txt("x > 3", size=18, color=GREEN).move_to(ax.c2p(3.93, 0.4))),
                  run_time=0.6)
        self.wait(0.3)

        rows = [
            ("f(x) > 0 ⇔ 图像在 x 轴上方", CHALK),
            ("交点：x₁ = 1，x₂ = 3", GOLD),
            ("上方部分对应的 x：两边", GREEN),
        ]
        y = 1.9
        for s, col in rows:
            t = txt(s, size=21, color=col).move_to([2.2, y, 0])
            if t.width > 6.0:
                t.scale_to_fit_width(6.0)
            self.play(FadeIn(t, shift=RIGHT * 0.04), run_time=0.7)
            y -= 0.92
        self.wait(0.4)

        box = label_box("解集：x < 1 或 x > 3", size=21, color=GREEN)
        box.move_to([2.2, -1.85, 0])
        self.play(FadeIn(box, scale=0.97), run_time=0.9)
        self.wait(3.5)
        self.finish_section()

    # ---------------- 2. 口诀：大于取两边 ---------------- 16.7
    def scene_rule(self):
        self.section(2, "口诀：大于取两边，小于取中间")

        head = txt("a > 0，Δ > 0：先求两根", size=23, color=CHALK).move_to([0, 2.05, 0])
        self.play(FadeIn(head, shift=UP * 0.04), run_time=0.8)

        line = Line(P(-5.5, 0.15), P(5.5, 0.15), color=DIM, stroke_width=2.4)
        self.play(Create(line), run_time=0.6)
        for x0, lb in ((-1.6, "1"), (1.6, "3")):
            self.play(FadeIn(Dot(P(x0, 0.15), radius=0.07, color=GOLD)),
                      FadeIn(txt(lb, size=19, color=GOLD).move_to(P(x0, -0.3))), run_time=0.4)
        self.play(Create(Line(P(-5.5, 0.15), P(-1.6, 0.15), color=GREEN, stroke_width=7)),
                  Create(Line(P(1.6, 0.15), P(5.5, 0.15), color=GREEN, stroke_width=7)),
                  run_time=0.7)
        self.play(Create(Line(P(-1.6, 0.15), P(1.6, 0.15), color=RED, stroke_width=7)),
                  run_time=0.6)
        self.play(FadeIn(txt("x < 1 或 x > 3", size=19, color=GREEN).move_to(P(-3.55, -0.62))),
                  FadeIn(txt("1 < x < 3", size=19, color=RED).move_to(P(0, -0.62))),
                  FadeIn(txt("x > 3", size=19, color=GREEN).move_to(P(3.55, -0.62))),
                  run_time=0.7)
        self.wait(0.4)

        rows = [
            ("大于 0：取两边（向外）", GREEN),
            ("小于 0：取中间（夹住）", RED),
        ]
        y = -1.5
        for s, col in rows:
            t = txt(s, size=22, color=col).move_to([0, y, 0])
            self.play(FadeIn(t, shift=UP * 0.04), run_time=0.7)
            y -= 0.72
        self.wait(0.3)
        self.finish_section()

    # ---------------- 3. Δ = 0 与 Δ < 0 ---------------- 28.4
    def scene_delta(self):
        self.section(3, "Δ = 0 与 Δ < 0：只有一个点或没有点")

        rows = [
            ("(x − 1)² > 0", "x ≠ 1", GOLD),
            ("(x − 1)² ≥ 0", "全体实数", GREEN),
            ("x² + 1 > 0", "全体实数", GREEN),
            ("x² + 1 < 0", "空集", RED),
        ]
        y = 1.95
        for a, b, col in rows:
            ta = txt(a, size=24, color=CHALK).move_to([-3.35, y, 0])
            self.play(FadeIn(ta, shift=RIGHT * 0.04), run_time=0.6)
            self.play(FadeIn(txt("→", size=24, color=DIM).move_to([-0.35, y, 0])), run_time=0.35)
            tb = txt(b, size=23, color=col).move_to([2.0, y, 0])
            self.play(FadeIn(tb, shift=RIGHT * 0.04), run_time=0.6)
            y -= 0.9
        self.wait(0.5)

        notes = [
            ("Δ = 0：只有一个点不满足", GOLD),
            ("Δ < 0：图像整体在轴上方，恒正", GREEN),
        ]
        y = -1.85
        for s, col in notes:
            t = txt(s, size=21, color=col).move_to([0, y, 0])
            if t.width > 11.0:
                t.scale_to_fit_width(11.0)
            self.play(FadeIn(t, shift=UP * 0.04), run_time=0.7)
            y -= 0.7
        self.wait(0.3)
        self.finish_section()

    # ---------------- 4. a < 0 先化正 ---------------- 23.6
    def scene_negative(self):
        self.section(4, "二次项系数为负：先化正再处理")

        lines = [
            ("−x² + 4x − 3 > 0", GOLD, 28),
            ("两边乘 −1，不等号变向", DIM, 20),
            ("x² − 4x + 3 < 0", CHALK, 28),
            ("开口向上，小于取中间", DIM, 20),
        ]
        y = 2.2
        for s, col, size in lines:
            t = txt(s, size=size, color=col).move_to([-2.6, y, 0])
            if t.width > 7.4:
                t.scale_to_fit_width(7.4)
            self.play(FadeIn(t, shift=UP * 0.04), run_time=0.8)
            y -= 0.78
        self.wait(0.3)

        line = Line(P(-5.3, -1.35), P(2.2, -1.35), color=DIM, stroke_width=2.4)
        self.play(Create(line), run_time=0.6)
        x1, x2 = -3.0, -0.6
        for x0, lb in ((x1, "1"), (x2, "3")):
            self.play(FadeIn(Dot(P(x0, -1.35), radius=0.07, color=GOLD)),
                      FadeIn(txt(lb, size=19, color=GOLD).move_to(P(x0, -1.8))), run_time=0.4)
        self.play(Create(Line(P(x1, -1.35), P(x2, -1.35), color=GREEN, stroke_width=7)),
                  run_time=0.6)
        self.play(FadeIn(txt("1 < x < 3", size=20, color=GREEN).move_to(P(-1.8, -2.25))),
                  run_time=0.7)
        self.wait(0.4)

        tip = label_box("化正之后再画图", size=21, color=ORANGE)
        tip.move_to([3.75, -0.4, 0])
        if tip.width > 5.4:
            tip.scale_to_fit_width(5.4)
        self.play(FadeIn(tip, scale=0.97), run_time=0.9)
        self.wait(3.5)
        self.finish_section()

    # ---------------- 5. 恒成立求参数 ---------------- 26.8
    def scene_parameter(self):
        self.section(5, "恒成立：把解集反过用来求参数")

        ax = Axes(
            x_range=[-1.5, 1.5, 1],
            y_range=[-0.4, 3.4, 1],
            x_length=3.1,
            y_length=2.5,
            axis_config={"color": DIM, "stroke_width": 2.0,
                         "include_numbers": False, "tip_length": 0.14},
        )
        ax.move_to(P(-4.35, 0.75))
        self.play(Create(ax), run_time=0.8)
        curve = ax.plot(lambda x: x * x + 1, x_range=[-1.45, 1.45],
                        color=GREEN, stroke_width=2.8)
        self.play(Create(curve), run_time=1.1)
        self.play(FadeIn(txt("x² + 1", size=19, color=GREEN).move_to(P(-4.35, 2.45))),
                  run_time=0.5)
        self.play(FadeIn(txt("与轴无交点", size=18, color=DIM).move_to(P(-4.35, -0.55))),
                  run_time=0.5)
        self.wait(0.3)

        head = txt("ax² + bx + c > 0 对任意 x 成立", size=21, color=GOLD)
        head.move_to([2.2, 2.05, 0])
        if head.width > 6.2:
            head.scale_to_fit_width(6.2)
        self.play(FadeIn(head, shift=RIGHT * 0.04), run_time=0.8)

        rows = [
            ("a > 0 且 Δ < 0：图像全在轴上方", GREEN),
            ("a = 0：退化为一次，单独讨论", GOLD),
            ("a < 0：开口向下，不可能恒正", RED),
        ]
        y = 1.05
        for s, col in rows:
            t = txt(s, size=20, color=col).move_to([2.2, y, 0])
            if t.width > 6.2:
                t.scale_to_fit_width(6.2)
            self.play(FadeIn(t, shift=RIGHT * 0.04), run_time=0.75)
            y -= 0.88
        self.wait(0.4)

        box = label_box("a > 0 且 Δ < 0", size=23, color=GOLD)
        box.move_to([2.2, -1.85, 0])
        self.play(FadeIn(box, scale=0.97), run_time=0.9)
        self.wait(4.5)
        self.finish_section()

    # ---------------- 6. 三个易错点 ---------------- 26.4
    def scene_traps(self):
        self.section(6, "三个易错点")

        rows = [
            ("① 不画图直接写", "大于、小于容易写反"),
            ("② a < 0 忘记变号", "先乘 −1，再处理"),
            ("③ 空集与全体实数分不清", "Δ < 0 时看不等号方向"),
        ]
        y = 1.75
        for a, b in rows:
            ta = txt(a, size=22, color=RED).move_to([-2.55, y, 0])
            if ta.width > 5.6:
                ta.scale_to_fit_width(5.6)
            self.play(FadeIn(ta, shift=RIGHT * 0.04), run_time=0.6)
            tb = txt(b, size=20, color=DIM).move_to([3.65, y, 0])
            if tb.width > 5.9:
                tb.scale_to_fit_width(5.9)
            self.play(FadeIn(tb, shift=RIGHT * 0.04), run_time=0.6)
            y -= 1.0
        self.wait(0.8)

        box = label_box("先化正，再画图，后写解集", size=24, color=GOLD)
        box.move_to([0, -2.35, 0])
        if box.width > 11.0:
            box.scale_to_fit_width(11.0)
        self.play(FadeIn(box, scale=0.97), run_time=1.1)
        self.wait(9.0)
        self.finish_section()

    def construct(self):
        self.scene_intro()
        self.clear_stage()
        self.scene_graph()
        self.clear_stage()
        self.scene_rule()
        self.clear_stage()
        self.scene_delta()
        self.clear_stage()
        self.scene_negative()
        self.clear_stage()
        self.scene_parameter()
        self.clear_stage()
        self.scene_traps()
        self.clear_stage(0.8)