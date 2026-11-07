# -*- coding: utf-8 -*-
"""分式：定义、有意义的条件、基本性质、约分与最简分式、乘除、加减。八年级。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


def P(x, y):
    return np.array([float(x), float(y), 0.0])


def frac(num: str, den: str, center, size: int = 40, color: str = CHALK) -> VGroup:
    """竖排分式：分子、分数线、分母。"""
    off = 0.0074 * size
    top = txt(num, size=size, color=color)
    bot = txt(den, size=size, color=color)
    w = max(top.width, bot.width) + 0.3
    line = Line([-w / 2, 0, 0], [w / 2, 0, 0], color=color, stroke_width=3)
    top.move_to([0, off, 0])
    bot.move_to([0, -off, 0])
    return VGroup(top, line, bot).move_to([center[0], center[1], 0])


def cross_out(mob: Mobject, color: str = RED, pad: float = 0.12) -> VGroup:
    """在对象上打一个叉（两条对角线）。"""
    l = mob.get_left()[0] - pad
    r = mob.get_right()[0] + pad
    b = mob.get_bottom()[1] - pad
    t = mob.get_top()[1] + pad
    return VGroup(
        Line([l, b, 0], [r, t, 0], color=color, stroke_width=2.6),
        Line([l, t, 0], [r, b, 0], color=color, stroke_width=2.6),
    )


class FenshiScene(NarratedScene):
    lesson = "fenshi"

    def clear_stage(self, run_time: float = 0.5):
        keep = {id(self._track), id(self._fill)}
        junk = [m for m in self.mobjects if id(m) not in keep]
        if junk:
            self.play(*[FadeOut(m) for m in junk], run_time=run_time)
        self.cur_title = None
        self.cur_sub = None

    # ---------------- 0. 从分数到分式 ---------------- 30.6
    def scene_intro(self):
        self.section(0, "从分数到分式")

        cap = txt("分数：分子分母都是具体的数", size=25, color=DIM)
        cap.move_to([-4.2, 2.55, 0])
        self.play(FadeIn(cap), run_time=0.6)

        f1 = frac("1", "2", [-4.9, 1.75, 0], 46, CHALK)
        f2 = frac("3", "4", [-3.4, 1.75, 0], 46, CHALK)
        self.play(FadeIn(f1, scale=0.94), run_time=0.8)
        self.play(FadeIn(f2, scale=0.94), run_time=0.8)

        a1 = Arrow(P(-2.55, 1.75), P(-1.35, 1.75), color=DIM, stroke_width=2.6,
                   max_tip_length_to_length_ratio=0.3)
        self.play(Create(a1), run_time=0.6)

        g1 = frac("2", "x", [0.1, 1.75, 0], 46, CHALK)
        g1[2].set_color(BLUE)
        self.play(FadeIn(g1, scale=0.94), run_time=0.9)

        g2 = frac("x + 1", "x − 1", [3.5, 1.75, 0], 40, CHALK)
        g2[2].set_color(BLUE)
        self.play(FadeIn(g2, scale=0.94), run_time=1.0)

        nn = txt("分母里含有字母", size=26, color=GOLD)
        nn.move_to([1.9, 0.62, 0])
        self.play(FadeIn(nn, shift=UP * 0.05), run_time=0.8)

        d = label_box("形如 A / B，A、B 是整式，且 B 中含字母", size=29, color=GOLD)
        d.move_to([0, -0.45, 0])
        self.play(FadeIn(d, scale=0.97), run_time=1.1)

        nb = txt("分母必须含字母", size=24, color=DIM)
        nb.move_to([0, -1.25, 0])
        self.play(FadeIn(nb, shift=UP * 0.05), run_time=0.7)

        w1 = frac("x", "2", [-4.5, -2.2, 0], 40, CHALK)
        w1[2].set_color(DIM)
        self.play(FadeIn(w1, scale=0.94), run_time=0.8)
        cross = cross_out(w1)
        self.play(Create(cross), run_time=0.6)
        wn = txt("分母是数，它是整式，不是分式", size=24, color=RED)
        wn.move_to([1.9, -2.2, 0])
        self.play(FadeIn(wn, shift=RIGHT * 0.05), run_time=0.8)

        self.wait(2.2)
        self.finish_section()

    # ---------------- 1. 有意义与值为零 ---------------- 33.6
    def scene_valid(self):
        self.section(1, "什么时候有意义")

        h = txt("先看分母：分母不能等于 0", size=27, color=CHALK)
        h.move_to([0, 2.55, 0])
        self.play(FadeIn(h, shift=UP * 0.05), run_time=0.8)

        r1 = frac("2", "x", [-4.9, 1.75, 0], 40, CHALK)
        self.play(FadeIn(r1, scale=0.94), run_time=0.8)
        a1 = Arrow(P(-4.0, 1.75), P(-2.5, 1.75), color=DIM, stroke_width=2.6,
                   max_tip_length_to_length_ratio=0.3)
        self.play(Create(a1), run_time=0.5)
        t1 = txt("x ≠ 0", size=32, color=GOLD)
        t1.move_to([-1.55, 1.75, 0])
        self.play(FadeIn(t1, shift=RIGHT * 0.05), run_time=0.9)

        r2 = frac("x + 1", "x − 1", [-4.6, 0.55, 0], 36, CHALK)
        self.play(FadeIn(r2, scale=0.94), run_time=0.9)
        a2 = Arrow(P(-3.4, 0.55), P(-2.5, 0.55), color=DIM, stroke_width=2.6,
                   max_tip_length_to_length_ratio=0.3)
        self.play(Create(a2), run_time=0.5)
        t2 = txt("x ≠ 1", size=32, color=GOLD)
        t2.move_to([-1.55, 0.55, 0])
        self.play(FadeIn(t2, shift=RIGHT * 0.05), run_time=0.9)

        tip = txt("让分母等于 0 解出来，那个值就是不能取的", size=24, color=DIM)
        tip.move_to([2.55, 1.15, 0])
        self.play(FadeIn(tip, shift=RIGHT * 0.05), run_time=0.9)

        div = Line(P(-6.3, -0.25), P(6.3, -0.25), color=DIM, stroke_width=2,
                   stroke_opacity=0.5)
        self.play(Create(div), run_time=0.6)

        h2 = label_box("分式的值为 0：分子 = 0，并且分母 ≠ 0", size=28, color=GREEN)
        h2.move_to([0, -1.0, 0])
        self.play(FadeIn(h2, scale=0.97), run_time=1.1)

        r3 = frac("x − 2", "x + 1", [-4.7, -2.2, 0], 36, CHALK)
        self.play(FadeIn(r3, scale=0.94), run_time=0.8)
        a3 = Arrow(P(-3.5, -2.2), P(-2.5, -2.2), color=GREEN, stroke_width=2.6,
                   max_tip_length_to_length_ratio=0.3)
        self.play(Create(a3), run_time=0.5)
        e1 = txt("分子 x − 2 = 0 → x = 2", size=26, color=GREEN)
        e1.move_to([1.1, -2.05, 0])
        self.play(FadeIn(e1, shift=RIGHT * 0.05), run_time=0.8)
        e2 = txt("此时分母 2 + 1 = 3 ≠ 0，可以", size=24, color=DIM)
        e2.move_to([1.3, -2.7, 0])
        self.play(FadeIn(e2, shift=RIGHT * 0.05), run_time=0.8)

        self.wait(2.0)
        self.finish_section()

    # ---------------- 2. 基本性质 ---------------- 30.3
    def scene_prop(self):
        self.section(2, "基本性质：同乘同除，值不变")

        d = label_box("A / B = (A·C) / (B·C)　（C ≠ 0）", size=30, color=GOLD)
        d.move_to([0, 2.55, 0])
        self.play(FadeIn(d, scale=0.97), run_time=1.1)

        f1 = frac("a", "b", [-4.3, 0.95, 0], 44, CHALK)
        self.play(FadeIn(f1, scale=0.94), run_time=0.8)
        a1 = Arrow(P(-3.2, 0.95), P(-1.9, 0.95), color=DIM, stroke_width=2.6,
                   max_tip_length_to_length_ratio=0.28)
        self.play(Create(a1), run_time=0.5)
        mul = txt("× c", size=28, color=ORANGE)
        mul.move_to([-2.55, 1.42, 0])
        self.play(FadeIn(mul, shift=UP * 0.05), run_time=0.6)
        f2 = frac("a·c", "b·c", [0.1, 0.95, 0], 44, CHALK)
        self.play(FadeIn(f2, scale=0.94), run_time=1.0)

        same = txt("值没变", size=26, color=GREEN)
        same.move_to([2.6, 0.95, 0])
        self.play(FadeIn(same, shift=RIGHT * 0.05), run_time=0.7)

        back = Arrow(P(1.5, -0.35), P(-2.0, -0.35), color=GREEN, stroke_width=2.6,
                     max_tip_length_to_length_ratio=0.16)
        self.play(Create(back), run_time=0.7)
        div = txt("÷ c（约分）", size=26, color=GREEN)
        div.move_to([2.1, -0.85, 0])
        self.play(FadeIn(div, shift=UP * 0.05), run_time=0.7)

        n1 = txt("分子分母同乘或同除以一个不等于 0 的整式", size=26, color=CHALK)
        n1.move_to([0, -1.75, 0])
        self.play(FadeIn(n1, shift=UP * 0.05), run_time=0.9)

        n2 = txt("乘 0 就全没了，所以 C 不能等于 0", size=24, color=RED)
        n2.move_to([0, -2.55, 0])
        self.play(FadeIn(n2, shift=UP * 0.05), run_time=0.8)

        self.wait(2.0)
        self.finish_section()

    # ---------------- 3. 约分与最简分式 ---------------- 33.1
    def scene_reduce(self):
        self.section(3, "约分：约到最简")

        f1 = frac("6a²b", "9ab²", [-4.6, 1.65, 0], 44, CHALK)
        self.play(FadeIn(f1, scale=0.94), run_time=0.9)

        a1 = Arrow(P(-3.0, 1.65), P(-1.2, 1.65), color=DIM, stroke_width=2.8,
                   max_tip_length_to_length_ratio=0.22)
        self.play(Create(a1), run_time=0.6)
        lab = txt("÷ 3ab", size=27, color=ORANGE)
        lab.move_to([-2.1, 2.15, 0])
        self.play(FadeIn(lab, shift=UP * 0.05), run_time=0.7)

        f2 = frac("2a", "3b", [1.2, 1.65, 0], 44, GREEN)
        self.play(FadeIn(f2, scale=0.94), run_time=1.0)

        t1 = txt("约分的关键：先把分子分母因式分解，写成乘积", size=26, color=CHALK)
        t1.move_to([0, 0.35, 0])
        self.play(FadeIn(t1, shift=UP * 0.05), run_time=1.0)

        t2 = txt("公因式看清了，才能一次约干净", size=24, color=DIM)
        t2.move_to([0, -0.35, 0])
        self.play(FadeIn(t2, shift=UP * 0.05), run_time=0.8)

        box = label_box("最简分式：分子与分母没有公因式", size=27, color=GOLD)
        box.move_to([0, -1.3, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.0)

        bad = frac("x + 1", "x + 2", [-4.4, -2.5, 0], 34, CHALK)
        self.play(FadeIn(bad, scale=0.94), run_time=0.8)
        cx = cross_out(bad)
        self.play(Create(cx), run_time=0.7)
        warn = txt("只能约因式，不能约项：这里的 x 约不掉", size=24, color=RED)
        warn.move_to([2.2, -2.5, 0])
        self.play(FadeIn(warn, shift=RIGHT * 0.05), run_time=0.9)

        self.wait(2.2)
        self.finish_section()

    # ---------------- 4. 乘除 ---------------- 25.3
    def scene_muldiv(self):
        self.section(4, "乘除：倒数一转")

        h = txt("乘法：分子乘分子，分母乘分母", size=27, color=GOLD)
        h.move_to([0, 2.5, 0])
        self.play(FadeIn(h, shift=UP * 0.05), run_time=0.8)

        row1 = VGroup(
            frac("a", "b", [0, 0, 0], 38, CHALK),
            txt("×", size=32, color=DIM),
            frac("c", "d", [0, 0, 0], 38, CHALK),
            txt("=", size=32, color=DIM),
            frac("a c", "b d", [0, 0, 0], 38, GREEN),
        ).arrange(RIGHT, buff=0.45).move_to([0, 1.25, 0])
        self.play(FadeIn(row1, shift=UP * 0.05), run_time=1.3)

        h2 = txt("除法：除以一个分式，等于乘它的倒数", size=27, color=GOLD)
        h2.move_to([0, 0.1, 0])
        self.play(FadeIn(h2, shift=UP * 0.05), run_time=0.9)

        row2 = VGroup(
            frac("a", "b", [0, 0, 0], 32, CHALK),
            txt("÷", size=28, color=DIM),
            frac("c", "d", [0, 0, 0], 32, CHALK),
            txt("=", size=28, color=DIM),
            frac("a", "b", [0, 0, 0], 32, CHALK),
            txt("×", size=28, color=DIM),
            frac("d", "c", [0, 0, 0], 32, ORANGE),
            txt("=", size=28, color=DIM),
            frac("a d", "b c", [0, 0, 0], 32, GREEN),
        ).arrange(RIGHT, buff=0.3).move_to([0, -1.05, 0])
        self.play(FadeIn(row2, shift=UP * 0.05), run_time=1.6)

        note = txt("乘除之前先因式分解、先约分，算起来最省力", size=25, color=CHALK)
        note.move_to([0, -2.6, 0])
        self.play(FadeIn(note, shift=UP * 0.05), run_time=0.9)

        self.wait(2.2)
        self.finish_section()

    # ---------------- 5. 加减 ---------------- 29.4
    def scene_addsub(self):
        self.section(5, "加减：先通分")

        h = txt("同分母：分母不变，分子相加减", size=27, color=GOLD)
        h.move_to([0, 2.45, 0])
        self.play(FadeIn(h, shift=UP * 0.05), run_time=0.8)

        row1 = VGroup(
            frac("a", "c", [0, 0, 0], 38, CHALK),
            txt("±", size=32, color=DIM),
            frac("b", "c", [0, 0, 0], 38, CHALK),
            txt("=", size=32, color=DIM),
            frac("a ± b", "c", [0, 0, 0], 38, GREEN),
        ).arrange(RIGHT, buff=0.45).move_to([0, 1.2, 0])
        self.play(FadeIn(row1, shift=UP * 0.05), run_time=1.3)

        h2 = txt("异分母：先通分，找最简公分母", size=27, color=GOLD)
        h2.move_to([0, 0.05, 0])
        self.play(FadeIn(h2, shift=UP * 0.05), run_time=0.9)

        t1 = VGroup(
            txt("系数取最小公倍数", size=24, color=CHALK),
            txt("字母取各分母的最高次", size=24, color=CHALK),
        ).arrange(RIGHT, buff=0.6).move_to([0, -0.75, 0])
        for m in t1:
            self.play(FadeIn(m, shift=UP * 0.05), run_time=0.75)

        row2 = VGroup(
            frac("1", "x", [0, 0, 0], 34, CHALK),
            txt("+", size=30, color=DIM),
            frac("1", "y", [0, 0, 0], 34, CHALK),
            txt("=", size=30, color=DIM),
            frac("y + x", "x y", [0, 0, 0], 34, GREEN),
        ).arrange(RIGHT, buff=0.42).move_to([0, -1.95, 0])
        self.play(FadeIn(row2, shift=UP * 0.05), run_time=1.4)

        note = txt("算完看能不能约分，答案要写成最简分式", size=24, color=DIM)
        note.move_to([0, -2.85, 0])
        self.play(FadeIn(note, shift=UP * 0.05), run_time=0.9)

        self.wait(2.0)
        self.finish_section()

    # ---------------- 6. 例题与三个易错点 ---------------- 38.4
    def scene_ex(self):
        self.section(6, "例题与三个易错点")

        q = txt("化简", size=28, color=CHALK)
        q.move_to([-5.5, 2.2, 0])
        s0 = frac("x² − 1", "x² + 2x + 1", [-2.3, 2.2, 0], 32, CHALK)
        self.play(FadeIn(q, shift=RIGHT * 0.05), run_time=0.6)
        self.play(FadeIn(s0, scale=0.94), run_time=0.9)

        a1 = Arrow(P(-0.55, 2.2), P(0.55, 2.2), color=DIM, stroke_width=2.6,
                   max_tip_length_to_length_ratio=0.3)
        self.play(Create(a1), run_time=0.5)
        s1 = frac("(x + 1)(x − 1)", "(x + 1)²", [3.3, 2.2, 0], 30, GOLD)
        self.play(FadeIn(s1, scale=0.94), run_time=1.1)

        a2 = Arrow(P(3.3, 1.62), P(3.3, 0.62), color=GREEN, stroke_width=2.6,
                   max_tip_length_to_length_ratio=0.28)
        self.play(Create(a2), run_time=0.5)
        s2 = VGroup(
            frac("x − 1", "x + 1", [0, 0, 0], 34, GREEN),
            txt("（x ≠ −1）", size=24, color=RED),
        ).arrange(RIGHT, buff=0.5).move_to([3.3, 0.1, 0])
        self.play(FadeIn(s2, shift=UP * 0.05), run_time=1.2)

        step = VGroup(
            txt("分子用平方差，分母用完全平方", size=24, color=DIM),
            txt("约掉公因式 (x + 1)，别忘了写取值范围", size=24, color=DIM),
        ).arrange(DOWN, buff=0.28).move_to([-2.6, 0.15, 0])
        for m in step:
            self.play(FadeIn(m, shift=RIGHT * 0.05), run_time=0.8)

        items = [
            ("以为分母有字母就是分式", "x/2 是整式"),
            ("有意义和值为 0 混了", "值为 0：分子 0 且分母非 0"),
            ("约掉了项，不是因式", "先分解再约"),
        ]
        y = -1.35
        for bad_s, good_s in items:
            bad = txt(bad_s, size=24, color=RED).move_to([-3.1, y, 0])
            good = txt(good_s, size=23, color=GREEN).move_to([3.9, y, 0])
            cross = Line([bad.get_left()[0] - 0.07, y - 0.02, 0],
                         [bad.get_right()[0] + 0.07, y - 0.02, 0],
                         color=RED, stroke_width=2.2)
            self.play(FadeIn(bad, shift=RIGHT * 0.05), run_time=0.6)
            self.play(Create(cross), run_time=0.35)
            self.play(FadeIn(good, shift=RIGHT * 0.05), run_time=0.6)
            y -= 0.8

        self.wait(2.8)
        self.finish_section()

    def construct(self):
        self.scene_intro()
        self.clear_stage()
        self.scene_valid()
        self.clear_stage()
        self.scene_prop()
        self.clear_stage()
        self.scene_reduce()
        self.clear_stage()
        self.scene_muldiv()
        self.clear_stage()
        self.scene_addsub()
        self.clear_stage()
        self.scene_ex()
        self.clear_stage(0.8)