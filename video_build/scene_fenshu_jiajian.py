# -*- coding: utf-8 -*-
"""分数加减法：同分母、约分、异分母通分、1 减分数、带分数。五年级下册。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


def frac(num: str, den: str, center, size: int = 46, color: str = CHALK) -> VGroup:
    """竖排分数：分子、分数线、分母。"""
    off = 0.0074 * size
    top = txt(num, size=size, color=color)
    bot = txt(den, size=size, color=color)
    w = max(top.width, bot.width) + 0.3
    line = Line([-w / 2, 0, 0], [w / 2, 0, 0], color=color, stroke_width=3)
    top.move_to([0, off, 0])
    bot.move_to([0, -off, 0])
    return VGroup(top, line, bot).move_to([center[0], center[1], 0])


def cells(n: int, cell: float, center, color: str = CHALK) -> VGroup:
    x0 = center[0] - n * cell / 2
    g = VGroup()
    for i in range(n):
        g.add(Rectangle(width=cell, height=cell * 1.2, color=color, stroke_width=2,
                        fill_color=color, fill_opacity=0.0)
              .move_to([x0 + (i + 0.5) * cell, center[1], 0]))
    return g


def mixed(whole: str, n: str, d: str, center, size: int = 42, color: str = CHALK) -> VGroup:
    """带分数：整数 + 竖排分数。"""
    w = txt(whole, size=size, color=color)
    f = frac(n, d, [0, 0, 0], size * 0.74, color)
    g = VGroup(w, f).arrange(RIGHT, buff=0.1)
    return g.move_to([center[0], center[1], 0])


class FenshuJiajianScene(NarratedScene):
    lesson = "fenshu-jiajian"

    def clear_stage(self, run_time: float = 0.5):
        keep = {id(self._track), id(self._fill)}
        junk = [m for m in self.mobjects if id(m) not in keep]
        if junk:
            self.play(*[FadeOut(m) for m in junk], run_time=run_time)
        self.cur_title = None
        self.cur_sub = None

    # ---------------- 0. 吃饼 ---------------- 15.4
    def scene_story(self):
        self.section(0, "先吃 3 份，又吃 2 份")

        g = cells(8, 0.68, [-3.2, 1.35, 0])
        self.play(LaggedStart(*[FadeIn(c) for c in g], lag_ratio=0.08), run_time=1.4)

        first = txt("先吃 3 份", size=26, color=GOLD).move_to([-3.2, 2.5, 0])
        self.play(FadeIn(first, shift=UP * 0.05), run_time=0.6)
        for i in range(3):
            self.play(g[i].animate.set_fill(GOLD, opacity=0.6), run_time=0.22)

        f1 = frac("3", "8", [2.9, 2.05, 0], 42, GOLD)
        self.play(FadeIn(f1, shift=RIGHT * 0.06), run_time=0.6)

        second = txt("又吃 2 份", size=26, color=GREEN).move_to([-3.2, 0.35, 0])
        self.play(FadeIn(second, shift=UP * 0.05), run_time=0.6)
        for i in (3, 4):
            self.play(g[i].animate.set_fill(GREEN, opacity=0.65), run_time=0.25)

        f2 = frac("2", "8", [2.9, 0.75, 0], 42, GREEN)
        self.play(FadeIn(f2, shift=RIGHT * 0.06), run_time=0.6)

        total = txt("一共 5 份", size=27, color=CHALK).move_to([-3.2, -0.55, 0])
        self.play(FadeIn(total, shift=UP * 0.05), run_time=0.6)
        f3 = frac("5", "8", [2.9, -0.55, 0], 42, CHALK)
        self.play(FadeIn(f3, shift=RIGHT * 0.06), run_time=0.6)

        note = txt("分数加减，就是数「一共有几份」", size=27, color=GOLD)
        note.move_to([0, -2.35, 0])
        self.play(FadeIn(note, shift=UP * 0.06), run_time=0.9)
        self.wait(1.8)
        self.finish_section()

    # ---------------- 1. 同分母 ---------------- 15.6
    def scene_same(self):
        self.section(1, "分母不变，分子相加减")

        f1 = frac("3", "8", [0, 0, 0], 48, GOLD)
        plus = txt("+", size=44, color=DIM)
        f2 = frac("2", "8", [0, 0, 0], 48, GREEN)
        eq = txt("=", size=44, color=DIM)
        f3 = frac("5", "8", [0, 0, 0], 48, CHALK)
        row = VGroup(f1, plus, f2, eq, f3).arrange(RIGHT, buff=0.36).move_to([0, 1.55, 0])
        self.play(FadeIn(row), run_time=1.3)

        br_num = Brace(VGroup(f1[0], f2[0]), UP, buff=0.16, color=GOLD)
        lab_num = txt("分子相加", size=25, color=GOLD).next_to(br_num, UP, buff=0.1)
        self.play(Create(br_num), FadeIn(lab_num), run_time=0.9)

        br_den = Brace(VGroup(f1[2], f2[2]), DOWN, buff=0.16, color=BLUE)
        lab_den = txt("分母不变", size=25, color=BLUE).next_to(br_den, DOWN, buff=0.1)
        self.play(Create(br_den), FadeIn(lab_den), run_time=0.9)

        f4 = frac("5", "8", [0, 0, 0], 44, CHALK)
        minus = txt("−", size=44, color=DIM)
        f5 = frac("2", "8", [0, 0, 0], 44, GREEN)
        eq2 = txt("=", size=44, color=DIM)
        f6 = frac("3", "8", [0, 0, 0], 44, GOLD)
        row2 = VGroup(f4, minus, f5, eq2, f6).arrange(RIGHT, buff=0.34).move_to([0, -1.5, 0])
        self.play(FadeIn(row2, shift=UP * 0.05), run_time=1.2)

        note = txt("分母是「分成几份」，加减时份数不变", size=26, color=DIM)
        note.move_to([0, -2.65, 0])
        self.play(FadeIn(note, shift=UP * 0.05), run_time=0.8)
        self.wait(2.2)
        self.finish_section()

    # ---------------- 2. 结果要约分 ---------------- 13.2
    def scene_reduce(self):
        self.section(2, "算完记得约分")

        a = VGroup(
            frac("2", "6", [0, 0, 0], 46, CHALK),
            txt("+", size=42, color=DIM),
            frac("1", "6", [0, 0, 0], 46, CHALK),
            txt("=", size=42, color=DIM),
            frac("3", "6", [0, 0, 0], 46, GOLD),
        ).arrange(RIGHT, buff=0.32).move_to([0, 1.75, 0])
        self.play(FadeIn(a), run_time=1.2)

        arrow = Arrow([1.55, 1.15, 0], [1.55, 0.35, 0], color=BLUE, stroke_width=2.4,
                      buff=0.02, max_tip_length_to_length_ratio=0.3)
        op = txt("同时除以 3", size=25, color=BLUE).move_to([3.8, 0.75, 0])
        self.play(GrowArrow(arrow), FadeIn(op, shift=RIGHT * 0.05), run_time=0.9)

        b = frac("1", "2", [1.55, -0.75, 0], 48, GREEN)
        self.play(FadeIn(b, shift=DOWN * 0.06), run_time=0.9)

        r1 = VGroup(
            txt("3 ÷ 3 = 1，6 ÷ 3 = 2", size=27, color=CHALK),
            txt("六分之三就是二分之一", size=27, color=GREEN),
        ).arrange(DOWN, buff=0.24).move_to([-2.9, -0.9, 0])
        self.play(FadeIn(r1[0], shift=UP * 0.05), run_time=0.7)
        self.play(FadeIn(r1[1], shift=UP * 0.05), run_time=0.7)

        tip = txt("结果一般都要写成最简分数", size=27, color=GOLD)
        tip.move_to([0, -2.4, 0])
        self.play(FadeIn(tip, shift=UP * 0.06), run_time=0.8)
        self.wait(2.4)
        self.finish_section()

    # ---------------- 3. 异分母 ---------------- 15.7
    def scene_diff(self):
        self.section(3, "分母不同，先通分")

        f1 = frac("1", "2", [-3.9, 2.3, 0], 44, GOLD)
        plus = txt("+", size=40, color=DIM).move_to([-2.3, 2.3, 0])
        f2 = frac("1", "3", [-0.8, 2.3, 0], 44, BLUE)
        self.play(FadeIn(f1, scale=0.96), FadeIn(f2, scale=0.96), FadeIn(plus), run_time=1.1)

        a1 = Arrow([-3.9, 1.82, 0], [-3.9, 1.12, 0], color=GOLD, stroke_width=2.2,
                   buff=0.02, max_tip_length_to_length_ratio=0.3)
        a2 = Arrow([-0.8, 1.82, 0], [-0.8, 1.12, 0], color=BLUE, stroke_width=2.2,
                   buff=0.02, max_tip_length_to_length_ratio=0.3)
        m1 = txt("×3", size=23, color=GOLD).move_to([-3.0, 1.45, 0])
        m2 = txt("×2", size=23, color=BLUE).move_to([0.1, 1.45, 0])
        self.play(GrowArrow(a1), GrowArrow(a2), run_time=0.9)
        self.play(FadeIn(m1), FadeIn(m2), run_time=0.5)

        g1 = frac("3", "6", [-3.9, 0.5, 0], 44, GOLD)
        plus2 = txt("+", size=40, color=DIM).move_to([-2.3, 0.5, 0])
        g2 = frac("2", "6", [-0.8, 0.5, 0], 44, BLUE)
        eq = txt("=", size=40, color=DIM).move_to([0.85, 0.5, 0])
        g3 = frac("5", "6", [2.5, 0.5, 0], 46, GREEN)
        self.play(FadeIn(g1, shift=DOWN * 0.05), run_time=0.6)
        self.play(FadeIn(g2, shift=DOWN * 0.05), run_time=0.6)
        self.play(FadeIn(plus2), FadeIn(eq), run_time=0.5)
        self.play(FadeIn(g3, shift=RIGHT * 0.06), run_time=0.8)

        note = VGroup(
            txt("六分之三加六分之二，等于六分之五", size=26, color=CHALK),
            txt("分母相同了，才能直接加分子", size=26, color=GOLD),
        ).arrange(DOWN, buff=0.22).move_to([0, -1.35, 0])
        self.play(FadeIn(note[0], shift=UP * 0.05), run_time=0.7)
        self.play(FadeIn(note[1], shift=UP * 0.05), run_time=0.7)
        self.wait(2.2)
        self.finish_section()

    # ---------------- 4. 1 减分数 ---------------- 15.0
    def scene_one(self):
        self.section(4, "1 减八分之三，怎么减")

        one = txt("1", size=52, color=CHALK).move_to([-4.4, 1.85, 0])
        self.play(FadeIn(one), run_time=0.7)

        a1 = Arrow([-3.7, 1.85, 0], [-2.1, 1.85, 0], color=GOLD, stroke_width=2.4,
                   buff=0.02, max_tip_length_to_length_ratio=0.26)
        lab = txt("看成 8 个八分之一", size=25, color=GOLD).move_to([-1.0, 2.55, 0])
        self.play(GrowArrow(a1), run_time=0.7)
        self.play(FadeIn(lab, shift=DOWN * 0.05), run_time=0.7)

        e1 = frac("8", "8", [-1.55, 1.75, 0], 48, GOLD)
        self.play(FadeIn(e1, shift=RIGHT * 0.06), run_time=0.8)

        row = VGroup(
            frac("8", "8", [0, 0, 0], 46, GOLD),
            txt("−", size=40, color=DIM),
            frac("3", "8", [0, 0, 0], 46, BLUE),
            txt("=", size=40, color=DIM),
            frac("5", "8", [0, 0, 0], 46, GREEN),
        ).arrange(RIGHT, buff=0.34).move_to([0, -0.65, 0])
        self.play(FadeIn(row, shift=UP * 0.05), run_time=1.3)

        note = VGroup(
            txt("整数 1 可以化成任何分母的分数", size=26, color=CHALK),
            txt("分母是几，就写成几分之几", size=25, color=DIM),
        ).arrange(DOWN, buff=0.22).move_to([0, -2.15, 0])
        self.play(FadeIn(note[0], shift=UP * 0.05), run_time=0.7)
        self.play(FadeIn(note[1], shift=UP * 0.05), run_time=0.7)
        self.wait(2.6)
        self.finish_section()

    # ---------------- 5. 带分数 ---------------- 17.7
    def scene_mixed(self):
        self.section(5, "带分数：整数和分数分开算")

        m1 = mixed("2", "1", "4", [0, 0, 0], 40, GOLD)
        plus = txt("+", size=40, color=DIM)
        m2 = mixed("1", "1", "4", [0, 0, 0], 40, BLUE)
        eq = txt("=", size=40, color=DIM)
        m3 = mixed("3", "2", "4", [0, 0, 0], 40, CHALK)
        row = VGroup(m1, plus, m2, eq, m3).arrange(RIGHT, buff=0.36).move_to([0, 2.2, 0])
        self.play(FadeIn(row), run_time=1.4)

        s1 = VGroup(
            txt("整数部分：2 + 1 = 3", size=26, color=GOLD),
            txt("分数部分：四分之一 + 四分之一 = 四分之二 = 二分之一", size=26, color=CHALK),
        ).arrange(DOWN, buff=0.26).move_to([0, 0.75, 0])
        self.play(FadeIn(s1[0], shift=UP * 0.05), run_time=0.8)
        self.play(FadeIn(s1[1], shift=UP * 0.05), run_time=0.9)

        res = mixed("3", "1", "2", [0, -1.35, 0], 54, GREEN)
        self.play(FadeIn(res, shift=UP * 0.06), run_time=1.0)

        note = txt("最后别忘了把分数部分约成最简", size=26, color=GOLD)
        note.move_to([0, -2.55, 0])
        self.play(FadeIn(note, shift=UP * 0.06), run_time=0.8)
        self.wait(2.4)
        self.finish_section()

    # ---------------- 6. 易错点 + 三句话 ---------------- 20.5
    def scene_warn(self):
        self.section(6, "三个易错点")

        items = [
            ("分母也一起相加", "分母不变，只加分子"),
            ("分母相加、分子相加", "先通分，再加分子"),
            ("算出结果不约分", "结果要约成最简"),
        ]
        y = 2.05
        for bad_s, note in items:
            bad = txt(bad_s, size=27, color=RED).move_to([-3.2, y, 0])
            n = txt(note, size=25, color=GREEN).move_to([3.2, y, 0])
            cross = Line(bad.get_left() + [-0.1, -0.08, 0],
                         bad.get_right() + [0.1, 0.18, 0],
                         color=RED, stroke_width=2.8)
            self.play(FadeIn(bad, shift=RIGHT * 0.05), run_time=0.6)
            self.play(Create(cross), FadeIn(n, shift=RIGHT * 0.05), run_time=0.7)
            self.wait(0.7)
            y -= 0.92

        rows = VGroup(
            label_box("① 同分母：分母不变，分子加减", size=24, color=GOLD),
            label_box("② 异分母：先通分，再加分子", size=24, color=CHALK),
            label_box("③ 算完检查，约成最简分数", size=24, color=GREEN),
        ).arrange(DOWN, buff=0.2).move_to([0, -1.65, 0])
        for r in rows:
            self.play(FadeIn(r, shift=RIGHT * 0.06), run_time=0.6)
            self.wait(0.55)

        self.wait(1.0)
        self.finish_section()

    def construct(self):
        self.scene_story()
        self.clear_stage()
        self.scene_same()
        self.clear_stage()
        self.scene_reduce()
        self.clear_stage()
        self.scene_diff()
        self.clear_stage()
        self.scene_one()
        self.clear_stage()
        self.scene_mixed()
        self.clear_stage()
        self.scene_warn()
        self.clear_stage(0.8)