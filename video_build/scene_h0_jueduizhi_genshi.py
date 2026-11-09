# -*- coding: utf-8 -*-
"""初升高衔接 4：绝对值与根式运算。绝对值看距离，根式先看符号。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


def P(x, y):
    return np.array([float(x), float(y), 0.0])


class H0JueduizhiGenshiScene(NarratedScene):
    lesson = "h0-jueduizhi-genshi"

    def clear_stage(self, run_time: float = 0.5):
        keep = {id(self._track), id(self._fill)}
        junk = [m for m in self.mobjects if id(m) not in keep]
        if junk:
            self.play(*[FadeOut(m) for m in junk], run_time=run_time)
        self.cur_title = None
        self.cur_sub = None

    # ---------------- 0. 两条主线 ---------------- 22.1
    def scene_intro(self):
        self.section(0, "绝对值与根式：两条主线")

        chips = [(-4.6, "绝对值 → 距离", GOLD), (-1.5, "根式 → 符号", GREEN),
                 (1.6, "先看符号，再动根号", BLUE), (4.75, "高中高频", RED)]
        for cx, name, col in chips:
            c = label_box(name, size=19, color=col).move_to([cx, 1.72, 0])
            if c.width > 3.2:
                c.scale_to_fit_width(3.2)
            self.play(FadeIn(c, shift=UP * 0.04), run_time=0.6)
        self.wait(0.4)

        rows = [
            ("初中只学定义，高中把它们和方程、不等式放一起", CHALK),
            ("绝对值：点到点的距离", GOLD),
            ("根式：开方结果必须非负", GREEN),
        ]
        y = 0.7
        for s, col in rows:
            t = txt(s, size=23, color=col).move_to([0, y, 0])
            if t.width > 11.4:
                t.scale_to_fit_width(11.4)
            self.play(FadeIn(t, shift=UP * 0.04), run_time=0.8)
            y -= 0.8
        self.wait(0.4)

        box = label_box("距离与符号：两个判断工具", size=23, color=GOLD)
        box.move_to([0, -2.3, 0])
        if box.width > 10.6:
            box.scale_to_fit_width(10.6)
        self.play(FadeIn(box, scale=0.97), run_time=1.0)
        self.wait(5.0)
        self.finish_section()

    # ---------------- 1. 绝对值的几何意义 ---------------- 19.9
    def scene_distance(self):
        self.section(1, "绝对值的几何意义：一段距离")

        line = Line(P(-5.9, 0.1), P(5.9, 0.1), color=DIM, stroke_width=2.4)
        self.play(Create(line), run_time=0.7)
        self.play(FadeIn(Dot(P(0, 0.1), radius=0.07, color=GOLD)),
                  FadeIn(txt("0", size=19, color=GOLD).move_to(P(0, -0.32))), run_time=0.45)
        self.play(FadeIn(Dot(P(2.4, 0.1), radius=0.07, color=CHALK)),
                  FadeIn(txt("x", size=19, color=CHALK).move_to(P(2.4, -0.32))), run_time=0.45)
        self.play(Create(DoubleArrow(P(0, 0.55), P(2.4, 0.55), color=GREEN,
                                     buff=0, stroke_width=3.0, tip_length=0.16)),
                  run_time=0.7)
        self.play(FadeIn(txt("|x|", size=21, color=GREEN).move_to(P(1.25, 0.95))), run_time=0.5)
        self.wait(0.3)

        self.play(FadeIn(Dot(P(-1.6, 0.1), radius=0.07, color=ORANGE)),
                  FadeIn(txt("a", size=19, color=ORANGE).move_to(P(-1.6, -0.32))), run_time=0.5)
        self.play(Create(DoubleArrow(P(-1.6, -0.6), P(2.4, -0.6), color=ORANGE,
                                     buff=0, stroke_width=3.0, tip_length=0.16)),
                  run_time=0.7)
        self.play(FadeIn(txt("|x − a|", size=21, color=ORANGE).move_to(P(0.45, -1.02))),
                  run_time=0.5)
        self.wait(0.3)

        rows = [
            ("|x|：到原点的距离", GOLD),
            ("|x − a|：到点 a 的距离", ORANGE),
            ("绝对值一定是非负数", GREEN),
        ]
        y = 1.85
        for s, col in rows:
            t = txt(s, size=22, color=col).move_to([3.3, y, 0])
            if t.width > 5.3:
                t.scale_to_fit_width(5.3)
            self.play(FadeIn(t, shift=RIGHT * 0.04), run_time=0.7)
            y -= 0.86
        self.wait(0.4)

        tip = txt("把 |x − a| 读成「到 a 的距离」", size=21, color=CHALK)
        tip.move_to([0, -2.15, 0])
        if tip.width > 11.0:
            tip.scale_to_fit_width(11.0)
        self.play(FadeIn(tip, shift=UP * 0.04), run_time=0.8)
        self.wait(3.0)
        self.finish_section()

    # ---------------- 2. 两条基本结论 ---------------- 27.3
    def scene_rules(self):
        self.section(2, "两条基本结论：小于夹、大于取")

        head = txt("a > 0", size=23, color=CHALK).move_to([-4.6, 2.05, 0])
        self.play(FadeIn(head), run_time=0.5)

        # 上：|x| < a
        l1 = Line(P(-5.4, 1.15), P(2.0, 1.15), color=DIM, stroke_width=2.2)
        self.play(Create(l1), run_time=0.6)
        self.play(Create(Line(P(-1.85, 1.15), P(-0.15, 1.15), color=GREEN, stroke_width=7)),
                  run_time=0.6)
        for x0, lb in ((-1.85, "−a"), (-0.15, "a")):
            self.play(FadeIn(Dot(P(x0, 1.15), radius=0.06, color=GOLD)),
                      FadeIn(txt(lb, size=18, color=GOLD).move_to(P(x0, 0.76))), run_time=0.35)
        self.play(FadeIn(txt("|x| < a  ⇔  −a < x < a", size=22, color=GREEN)
                         .move_to([4.05, 1.15, 0])), run_time=0.7)
        self.play(FadeIn(txt("小于：夹在中间", size=19, color=GREEN).move_to(P(-1.0, 1.68))),
                  run_time=0.5)
        self.wait(0.3)

        # 下：|x| > a
        l2 = Line(P(-5.4, -0.55), P(2.0, -0.55), color=DIM, stroke_width=2.2)
        self.play(Create(l2), run_time=0.6)
        self.play(Create(Line(P(-5.4, -0.55), P(-1.85, -0.55), color=ORANGE, stroke_width=7)),
                  Create(Line(P(-0.15, -0.55), P(2.0, -0.55), color=ORANGE, stroke_width=7)),
                  run_time=0.6)
        for x0, lb in ((-1.85, "−a"), (-0.15, "a")):
            self.play(FadeIn(Dot(P(x0, -0.55), radius=0.06, color=GOLD)),
                      FadeIn(txt(lb, size=18, color=GOLD).move_to(P(x0, -0.94))), run_time=0.35)
        self.play(FadeIn(txt("|x| > a  ⇔  x < −a 或 x > a", size=22, color=ORANGE)
                         .move_to([3.6, -0.55, 0])), run_time=0.7)
        self.play(FadeIn(txt("大于：取两边", size=19, color=ORANGE).move_to(P(-3.7, -0.1))),
                  run_time=0.5)
        self.wait(0.3)

        tip = label_box("口诀与二次不等式一致", size=21, color=GOLD)
        tip.move_to([0, -2.25, 0])
        self.play(FadeIn(tip, scale=0.97), run_time=0.9)
        self.wait(9.0)
        self.finish_section()

    # ---------------- 3. 带平移：先找中心再看半径 ---------------- 19.3
    def scene_shift(self):
        self.section(3, "带平移：先找中心，再看半径")

        f = txt("|x − 2| < 3", size=31, color=GOLD).move_to([-3.0, 2.15, 0])
        self.play(FadeIn(f, shift=UP * 0.04), run_time=0.8)
        note = txt("到 2 的距离小于 3：中心 2，半径 3", size=21, color=CHALK)
        note.move_to([0.2, 1.55, 0])
        self.play(FadeIn(note, shift=UP * 0.04), run_time=0.8)

        line = Line(P(-5.4, 0.3), P(5.4, 0.3), color=DIM, stroke_width=2.4)
        self.play(Create(line), run_time=0.7)
        self.play(Create(Line(P(-2.6, 0.3), P(3.4, 0.3), color=GREEN, stroke_width=7)),
                  run_time=0.7)
        for x0, lb in ((-2.6, "−1"), (0.4, "2"), (3.4, "5")):
            self.play(FadeIn(Dot(P(x0, 0.3), radius=0.06, color=GOLD)),
                      FadeIn(txt(lb, size=19, color=GOLD).move_to(P(x0, -0.12))), run_time=0.4)
        self.play(FadeIn(txt("−1 < x < 5", size=23, color=GREEN).move_to([0.4, -0.95, 0])),
                  run_time=0.7)
        self.wait(0.3)

        rows = [
            ("① 找中心点 a", GOLD),
            ("② 左右各展开 a 的半径", GREEN),
            ("③ 直接写区间，不去绝对值", BLUE),
        ]
        y = -1.35
        for s, col in rows:
            t = txt(s, size=21, color=col).move_to([0, y, 0])
            self.play(FadeIn(t, shift=UP * 0.04), run_time=0.6)
            y -= 0.58
        self.wait(2.5)
        self.finish_section()

    # ---------------- 4. 两个绝对值相加：距离和 ---------------- 22.5
    def scene_sum(self):
        self.section(4, "两个绝对值相加：看距离和")

        f = txt("|x − 1| + |x + 2|", size=29, color=GOLD).move_to([0, 2.15, 0])
        self.play(FadeIn(f, shift=UP * 0.04), run_time=0.8)

        line = Line(P(-5.6, 0.35), P(5.6, 0.35), color=DIM, stroke_width=2.4)
        self.play(Create(line), run_time=0.7)
        p1, p2 = -2.9, 1.3
        self.play(Create(Line(P(p1, 0.35), P(p2, 0.35), color=GREEN, stroke_width=7)),
                  run_time=0.6)
        for x0, lb in ((p1, "−2"), (p2, "1")):
            self.play(FadeIn(Dot(P(x0, 0.35), radius=0.07, color=GOLD)),
                      FadeIn(txt(lb, size=19, color=GOLD).move_to(P(x0, -0.08))), run_time=0.4)
        self.play(FadeIn(txt("距离和最小 = 3", size=22, color=GREEN).move_to([0, -0.72, 0])),
                  run_time=0.7)
        self.wait(0.3)

        rows = [
            ("x 在两点之间时，距离和最小", CHALK),
            ("最小值就是两点之间的距离", GOLD),
            ("x 在两点之外，距离和变大", ORANGE),
        ]
        y = -1.45
        for s, col in rows:
            t = txt(s, size=21, color=col).move_to([0, y, 0])
            if t.width > 11.0:
                t.scale_to_fit_width(11.0)
            self.play(FadeIn(t, shift=UP * 0.04), run_time=0.6)
            y -= 0.6
        self.wait(3.0)
        self.finish_section()

    # ---------------- 5. 根式：开方要带绝对值 ---------------- 23.8
    def scene_sqrt(self):
        self.section(5, "根式：开方结果必须非负")

        f1 = txt("√(a²) = |a|", size=34, color=GOLD).move_to([0, 2.0, 0])
        self.play(FadeIn(f1, shift=UP * 0.04), run_time=0.9)
        c1 = txt("√((−3)²) = |−3| = 3，不是 −3", size=22, color=CHALK).move_to([0, 1.25, 0])
        self.play(FadeIn(c1, shift=UP * 0.04), run_time=0.8)
        self.wait(0.4)

        sep = Line(P(-6.0, 0.75), P(6.0, 0.75), color=DIM, stroke_width=1.4)
        self.play(Create(sep), run_time=0.5)

        f2 = txt("√(x² − 2x + 1) = √((x − 1)²) = |x − 1|", size=25, color=CHALK)
        f2.move_to([0, 0.1, 0])
        if f2.width > 12.2:
            f2.scale_to_fit_width(12.2)
        self.play(FadeIn(f2, shift=UP * 0.04), run_time=0.9)
        note = txt("先配方，再开方，最后按 x 的范围去绝对值", size=21, color=ORANGE)
        note.move_to([0, -0.62, 0])
        if note.width > 11.6:
            note.scale_to_fit_width(11.6)
        self.play(FadeIn(note, shift=UP * 0.04), run_time=0.7)
        self.wait(0.4)

        f3 = txt("1 / (√a + √b) = (√a − √b) / (a − b)", size=24, color=GREEN)
        f3.move_to([0, -1.6, 0])
        if f3.width > 12.2:
            f3.scale_to_fit_width(12.2)
        self.play(FadeIn(f3, shift=UP * 0.04), run_time=0.9)
        tip = txt("上下同乘 √a − √b：分母有理化", size=20, color=DIM)
        tip.move_to([0, -2.35, 0])
        self.play(FadeIn(tip), run_time=0.7)
        self.wait(8.5)
        self.finish_section()

    # ---------------- 6. 三个易错点 ---------------- 25.1
    def scene_traps(self):
        self.section(6, "三个易错点")

        rows = [
            ("① 开方忘记绝对值", "√(a²) 是 |a|，不是 a"),
            ("② 去绝对值不判断符号", "先定 x 的范围再脱符号"),
            ("③ 有理化漏乘分子", "分母乘什么，分子也乘什么"),
        ]
        y = 1.75
        for a, b in rows:
            ta = txt(a, size=22, color=RED).move_to([-2.5, y, 0])
            if ta.width > 5.7:
                ta.scale_to_fit_width(5.7)
            self.play(FadeIn(ta, shift=RIGHT * 0.04), run_time=0.6)
            tb = txt(b, size=20, color=DIM).move_to([3.7, y, 0])
            if tb.width > 5.9:
                tb.scale_to_fit_width(5.9)
            self.play(FadeIn(tb, shift=RIGHT * 0.04), run_time=0.6)
            y -= 1.0
        self.wait(0.8)

        box = label_box("先看符号，再动根号", size=24, color=GOLD)
        box.move_to([0, -2.35, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.1)
        self.wait(8.5)
        self.finish_section()

    def construct(self):
        self.scene_intro()
        self.clear_stage()
        self.scene_distance()
        self.clear_stage()
        self.scene_rules()
        self.clear_stage()
        self.scene_shift()
        self.clear_stage()
        self.scene_sum()
        self.clear_stage()
        self.scene_sqrt()
        self.clear_stage()
        self.scene_traps()
        self.clear_stage(0.8)