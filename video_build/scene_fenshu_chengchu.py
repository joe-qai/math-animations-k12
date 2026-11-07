# -*- coding: utf-8 -*-
"""分数乘除法：分数乘整数、分数乘分数、倒数、除法转乘法、实际应用。五年级下册。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


def frac(num: str, den: str, center, size: int = 44, color: str = CHALK) -> VGroup:
    off = 0.0074 * size
    top = txt(num, size=size, color=color)
    bot = txt(den, size=size, color=color)
    w = max(top.width, bot.width) + 0.28
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


def mixed(whole: str, n: str, d: str, center, size: int = 40, color: str = CHALK) -> VGroup:
    w = txt(whole, size=size, color=color)
    f = frac(n, d, [0, 0, 0], size * 0.74, color)
    return VGroup(w, f).arrange(RIGHT, buff=0.1).move_to([center[0], center[1], 0])


class FenshuChengchuScene(NarratedScene):
    lesson = "fenshu-chengchu"

    def clear_stage(self, run_time: float = 0.5):
        keep = {id(self._track), id(self._fill)}
        junk = [m for m in self.mobjects if id(m) not in keep]
        if junk:
            self.play(*[FadeOut(m) for m in junk], run_time=run_time)
        self.cur_title = None
        self.cur_sub = None

    # ---------------- 0. 三分之一的一半 ---------------- 14.4
    def scene_story(self):
        self.section(0, "三分之一的二分之一，是多少")

        x0, y0, y1 = -4.9, 0.55, 2.35
        cell = 0.85
        base = Rectangle(width=3 * cell, height=y1 - y0, color=CHALK, stroke_width=2.5)
        base.move_to([x0 + 1.5 * cell, (y0 + y1) / 2, 0])
        self.play(Create(base), run_time=1.0)

        vlines = VGroup(*[Line([x0 + i * cell, y0, 0], [x0 + i * cell, y1, 0],
                               color=CHALK, stroke_width=1.8) for i in (1, 2)])
        self.play(Create(vlines), run_time=0.7)

        third = Rectangle(width=cell, height=y1 - y0, stroke_width=0,
                          fill_color=GOLD, fill_opacity=0.45)
        third.move_to([x0 + 0.5 * cell, (y0 + y1) / 2, 0])
        self.play(FadeIn(third), run_time=0.8)
        l3 = frac("1", "3", [x0 + 0.5 * cell, -0.1, 0], 38, GOLD)
        self.play(FadeIn(l3, shift=UP * 0.05), run_time=0.6)

        half = Line([x0, (y0 + y1) / 2, 0], [x0 + cell, (y0 + y1) / 2, 0],
                    color=CHALK, stroke_width=1.8)
        self.play(Create(half), run_time=0.6)

        sixth = Rectangle(width=cell, height=(y1 - y0) / 2, stroke_width=0,
                          fill_color=GREEN, fill_opacity=0.85)
        sixth.move_to([x0 + 0.5 * cell, (y0 + y1) / 2 + (y1 - y0) / 4, 0])
        self.play(FadeIn(sixth), run_time=0.8)

        l6 = frac("1", "6", [1.4, 1.85, 0], 44, GREEN)
        arr = Arrow([0.0, 1.85, 0], [-1.65, 1.85, 0], color=GREEN, stroke_width=2.2,
                    buff=0.05, max_tip_length_to_length_ratio=0.3)
        self.play(GrowArrow(arr), FadeIn(l6, shift=RIGHT * 0.05), run_time=0.9)

        note = txt("求一个数的几分之几，用乘法", size=28, color=GOLD)
        note.move_to([1.2, 0.35, 0])
        self.play(FadeIn(note, shift=UP * 0.05), run_time=0.8)

        eq = VGroup(
            frac("1", "3", [0, 0, 0], 36, GOLD),
            txt("×", size=30, color=DIM),
            frac("1", "2", [0, 0, 0], 36, GREEN),
            txt("=", size=30, color=DIM),
            frac("1", "6", [0, 0, 0], 36, GREEN),
        ).arrange(RIGHT, buff=0.26).move_to([1.4, -1.25, 0])
        self.play(FadeIn(eq, shift=UP * 0.05), run_time=1.0)
        self.wait(2.6)
        self.finish_section()

    # ---------------- 1. 分数乘整数 ---------------- 13.2
    def scene_int(self):
        self.section(1, "五分之二乘三")

        bars = VGroup()
        for i in range(3):
            g = cells(5, 0.5, [-4.6 + i * 2.55, 1.85, 0])
            for j in range(2):
                g[j].set_fill(GOLD, opacity=0.6)
            bars.add(g)
        self.play(LaggedStart(*[FadeIn(b) for b in bars], lag_ratio=0.2), run_time=1.5)

        labs = VGroup(*[frac("2", "5", [-4.6 + i * 2.55, 0.75, 0], 34, GOLD) for i in range(3)])
        self.play(FadeIn(labs), run_time=0.9)

        row = VGroup(
            frac("2", "5", [0, 0, 0], 46, GOLD),
            txt("×", size=38, color=DIM),
            txt("3", size=46, color=CHALK),
            txt("=", size=38, color=DIM),
            frac("6", "5", [0, 0, 0], 46, GREEN),
            txt("=", size=38, color=DIM),
            mixed("1", "1", "5", [0, 0, 0], 36, GREEN),
        ).arrange(RIGHT, buff=0.3).move_to([0, -1.1, 0])
        self.play(FadeIn(row, shift=UP * 0.05), run_time=1.3)

        rule = txt("分子乘整数，分母不变", size=27, color=BLUE).move_to([0, -2.45, 0])
        self.play(FadeIn(rule, shift=UP * 0.05), run_time=0.8)

        side = txt("就是 3 个五分之二相加", size=25, color=DIM).move_to([0, 2.85, 0])
        self.play(FadeIn(side, shift=DOWN * 0.05), run_time=0.7)
        self.wait(2.6)
        self.finish_section()

    # ---------------- 2. 分数乘分数 ---------------- 18.4
    def scene_frac(self):
        self.section(2, "分子乘分子，分母乘分母")

        g = VGroup()
        for c in range(4):
            for r in range(3):
                g.add(Rectangle(width=0.62, height=0.62, color=CHALK, stroke_width=1.6,
                                fill_color=CHALK, fill_opacity=0.0)
                      .move_to([-4.5 + c * 0.62, 1.55 - r * 0.62, 0]))
        self.play(LaggedStart(*[FadeIn(c) for c in g], lag_ratio=0.04), run_time=1.4)

        # 3 列 × 2 行 = 6 格
        k = 0
        for c in range(3):
            for r in range(2):
                idx = c * 3 + r
                self.play(g[idx].animate.set_fill(GOLD, opacity=0.6), run_time=0.12)
        cnt = txt("12 格中的 6 格", size=24, color=GOLD).move_to([-3.3, -0.75, 0])
        self.play(FadeIn(cnt, shift=UP * 0.05), run_time=0.7)

        row = VGroup(
            frac("2", "3", [0, 0, 0], 42, GOLD),
            txt("×", size=34, color=DIM),
            frac("3", "4", [0, 0, 0], 42, GOLD),
            txt("=", size=34, color=DIM),
            frac("2×3", "3×4", [0, 0, 0], 38, CHALK),
            txt("=", size=34, color=DIM),
            frac("6", "12", [0, 0, 0], 42, GREEN),
        ).arrange(RIGHT, buff=0.26).move_to([1.7, 1.75, 0])
        self.play(FadeIn(row, shift=RIGHT * 0.05), run_time=1.5)

        res = VGroup(
            txt("6 ÷ 6 = 1，12 ÷ 6 = 2", size=25, color=CHALK),
            frac("6", "12", [0, 0, 0], 36, GREEN),
            txt("=", size=32, color=DIM),
            frac("1", "2", [0, 0, 0], 42, GREEN),
        ).arrange(RIGHT, buff=0.28).move_to([1.9, 0.35, 0])
        self.play(FadeIn(res, shift=UP * 0.05), run_time=1.1)

        rule = VGroup(
            txt("分子乘分子，分母乘分母", size=26, color=BLUE),
            txt("能约分的先约分，算起来更简单", size=26, color=DIM),
        ).arrange(DOWN, buff=0.24).move_to([0, -1.85, 0])
        self.play(FadeIn(rule[0], shift=UP * 0.05), run_time=0.8)
        self.play(FadeIn(rule[1], shift=UP * 0.05), run_time=0.8)
        self.wait(3.2)
        self.finish_section()

    # ---------------- 3. 除以一个数 = 乘倒数 ---------------- 13.4
    def scene_recip(self):
        self.section(3, "除以三分之一，就是乘 3")

        row = VGroup(
            frac("1", "2", [0, 0, 0], 46, GOLD),
            txt("÷", size=40, color=DIM),
            frac("1", "3", [0, 0, 0], 46, BLUE),
            txt("=", size=40, color=DIM),
            frac("1", "2", [0, 0, 0], 46, GOLD),
            txt("×", size=40, color=DIM),
            frac("3", "1", [0, 0, 0], 46, BLUE),
            txt("=", size=40, color=DIM),
            frac("3", "2", [0, 0, 0], 46, GREEN),
        ).arrange(RIGHT, buff=0.24).move_to([0, 1.55, 0])
        self.play(FadeIn(row), run_time=1.6)

        flip = VGroup(
            txt("分子分母交换位置，就是倒数", size=27, color=BLUE),
            txt("三分之一的倒数是 3", size=27, color=CHALK),
        ).arrange(DOWN, buff=0.26).move_to([0, -0.35, 0])
        self.play(FadeIn(flip[0], shift=UP * 0.05), run_time=0.8)
        self.play(FadeIn(flip[1], shift=UP * 0.05), run_time=0.8)

        rule = label_box("除以一个分数，等于乘它的倒数", size=26, color=GOLD)
        rule.move_to([0, -1.75, 0])
        self.play(FadeIn(rule, scale=0.97), run_time=0.9)

        tip = txt("除号变乘号，除数变倒数，两件事一起做", size=26, color=DIM)
        tip.move_to([0, -2.55, 0])
        self.play(FadeIn(tip, shift=UP * 0.05), run_time=0.8)
        self.wait(2.4)
        self.finish_section()

    # ---------------- 4. 三分之二 ÷ 五分之四 ---------------- 15.0
    def scene_divide(self):
        self.section(4, "三分之二除以五分之四")

        top = VGroup(
            frac("2", "3", [0, 0, 0], 46, GOLD),
            txt("÷", size=40, color=DIM),
            frac("4", "5", [0, 0, 0], 46, BLUE),
        ).arrange(RIGHT, buff=0.3).move_to([0, 2.25, 0])
        self.play(FadeIn(top), run_time=1.1)

        bottom = VGroup(
            frac("2", "3", [0, 0, 0], 44, GOLD),
            txt("×", size=38, color=DIM),
            frac("5", "4", [0, 0, 0], 44, BLUE),
            txt("=", size=38, color=DIM),
            frac("2×5", "3×4", [0, 0, 0], 34, CHALK),
            txt("=", size=38, color=DIM),
            frac("10", "12", [0, 0, 0], 44, GREEN),
            txt("=", size=38, color=DIM),
            frac("5", "6", [0, 0, 0], 44, GREEN),
        ).arrange(RIGHT, buff=0.22).move_to([0, 0.65, 0])
        self.play(FadeIn(bottom, shift=UP * 0.05), run_time=1.7)

        steps = VGroup(
            txt("① 除号变乘号", size=26, color=CHALK),
            txt("② 五分之四变四分之五", size=26, color=CHALK),
            txt("③ 算出十二分之十，约成六分之五", size=26, color=GREEN),
        ).arrange(DOWN, buff=0.24, aligned_edge=LEFT).move_to([-1.2, -1.05, 0])
        for s in steps:
            self.play(FadeIn(s, shift=RIGHT * 0.05), run_time=0.6)
            self.wait(0.4)

        tip = txt("被除数不动，只把除数变倒数", size=27, color=GOLD)
        tip.move_to([0, -2.55, 0])
        self.play(FadeIn(tip, shift=UP * 0.05), run_time=0.8)
        self.wait(1.6)
        self.finish_section()

    # ---------------- 5. 应用题 ---------------- 15.4
    def scene_apply(self):
        self.section(5, "四分之三米，用去三分之二")

        rope = Line([-5.2, 1.85, 0], [-2.5, 1.85, 0], color=CHALK, stroke_width=7)
        self.play(Create(rope), run_time=1.0)

        marks = VGroup()
        for i in range(1, 3):
            x = -5.2 + i * 0.9
            marks.add(Line([x, 1.62, 0], [x, 2.08, 0], color=CHALK, stroke_width=2))
        self.play(LaggedStart(*[Create(m) for m in marks], lag_ratio=0.15), run_time=0.9)

        used = Line([-5.2, 1.85, 0], [-3.4, 1.85, 0], color=GOLD, stroke_width=7)
        self.play(Create(used), run_time=0.9)

        lab = VGroup(
            txt("全长 四分之三 米", size=27, color=CHALK),
            txt("用去 三分之二", size=27, color=GOLD),
        ).arrange(DOWN, buff=0.24).move_to([2.6, 1.95, 0])
        self.play(FadeIn(lab[0], shift=RIGHT * 0.05), run_time=0.7)
        self.play(FadeIn(lab[1], shift=RIGHT * 0.05), run_time=0.7)

        eq = VGroup(
            frac("3", "4", [0, 0, 0], 46, GOLD),
            txt("×", size=40, color=DIM),
            frac("2", "3", [0, 0, 0], 46, GOLD),
            txt("=", size=40, color=DIM),
            frac("6", "12", [0, 0, 0], 46, CHALK),
            txt("=", size=40, color=DIM),
            frac("1", "2", [0, 0, 0], 46, GREEN),
        ).arrange(RIGHT, buff=0.26).move_to([0, 0.05, 0])
        self.play(FadeIn(eq, shift=UP * 0.05), run_time=1.4)

        ans = txt("用去 二分之一 米", size=32, color=GREEN).move_to([0, -1.35, 0])
        self.play(FadeIn(ans, shift=UP * 0.06), run_time=0.9)

        why = VGroup(
            txt("求四分之三的三分之二，就是四分之三乘三分之二", size=25, color=CHALK),
            txt("「的」字后面是几分之几，就用乘法", size=25, color=GOLD),
        ).arrange(DOWN, buff=0.22).move_to([0, -2.4, 0])
        self.play(FadeIn(why[0], shift=UP * 0.05), run_time=0.7)
        self.play(FadeIn(why[1], shift=UP * 0.05), run_time=0.7)
        self.wait(2.4)
        self.finish_section()

    # ---------------- 6. 易错点 + 三句话 ---------------- 19.1
    def scene_warn(self):
        self.section(6, "三个易错点")

        items = [
            ("乘法先通分", "乘法直接分子乘分子"),
            ("被除数和除数都变倒数", "只把除数变倒数"),
            ("算出十二分之十就停", "要约成最简分数"),
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
            label_box("① 分数乘法：分子乘分子，分母乘分母", size=24, color=GOLD),
            label_box("② 除法：除号变乘号，除数变倒数", size=24, color=CHALK),
            label_box("③ 结果都要约成最简分数", size=24, color=GREEN),
        ).arrange(DOWN, buff=0.2).move_to([0, -1.65, 0])
        for r in rows:
            self.play(FadeIn(r, shift=RIGHT * 0.06), run_time=0.6)
            self.wait(0.55)

        self.wait(1.0)
        self.finish_section()

    def construct(self):
        self.scene_story()
        self.clear_stage()
        self.scene_int()
        self.clear_stage()
        self.scene_frac()
        self.clear_stage()
        self.scene_recip()
        self.clear_stage()
        self.scene_divide()
        self.clear_stage()
        self.scene_apply()
        self.clear_stage()
        self.scene_warn()
        self.clear_stage(0.8)