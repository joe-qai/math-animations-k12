# -*- coding: utf-8 -*-
"""科学记数法：一位整数乘十的幂，指数就是小数点移动的位数。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


def sci(a_str: str, exp_str: str, y: float = 0.0, x: float = 0.0,
        size: int = 46, color: str = GOLD) -> VGroup:
    a = txt(a_str, size=size, color=color)
    ten = txt("×10", size=size, color=color)
    e = txt(exp_str, size=int(size * 0.55), color=color)
    g = VGroup(a, ten, e).arrange(RIGHT, buff=0.14)
    e.shift(UP * 0.32 * size / 46 + LEFT * 0.05)
    g.move_to([x, y, 0])
    return g


class KexueJishufaScene(NarratedScene):
    lesson = "kexue-jishufa"

    def construct(self):
        # ---------- 0. 大数太长 ----------
        self.section(0, "这么大的数，写起来太长")
        big = txt("150000000 千米", size=48, color=CHALK).move_to([0, 1.35, 0])
        self.play(Write(big), run_time=1.2)

        r1 = txt("地球到太阳的距离", size=30, color=DIM).move_to([0, 0.45, 0])
        self.play(FadeIn(r1), run_time=0.5)

        diff = txt("一共 9 位，数零都要数半天", size=32, color=RED).move_to([0, -0.6, 0])
        self.play(FadeIn(diff, shift=UP * 0.1), run_time=0.6)

        q = txt("有没有更简短的写法？", size=34, color=GOLD).move_to([0, -1.6, 0])
        self.play(Write(q), run_time=0.6)
        self.finish_section()

        # ---------- 1. 科学记数法的形式 ----------
        self.section(1, "写成「一位整数 × 10 的幂」")
        self.play(FadeOut(big), FadeOut(r1), FadeOut(diff), FadeOut(q), run_time=0.5)

        form = sci("a", "n", y=1.4, size=56)
        self.play(FadeIn(form), run_time=0.8)

        c1 = txt("1 ≤ a ＜ 10", size=36, color=GOLD).move_to([0, 0.3, 0])
        c2 = txt("a 只有一位整数", size=32, color=CHALK).move_to([0, -0.6, 0])
        c3 = txt("n 是整数，可以是负数", size=30, color=DIM).move_to([0, -1.55, 0])
        self.play(Write(c1), run_time=0.6)
        self.play(FadeIn(c2), run_time=0.5)
        self.play(FadeIn(c3), run_time=0.5)
        self.finish_section()

        # ---------- 2. 例：一亿五千万 ----------
        self.section(2, "一亿五千万怎么写")
        self.play(FadeOut(form), FadeOut(c1), FadeOut(c2), FadeOut(c3), run_time=0.5)

        s1 = txt("150000000", size=44, color=CHALK).move_to([-3.6, 1.45, 0])
        s2 = sci("1.5", "8", y=0.35, x=-3.4, size=46)
        self.play(Write(s1), run_time=0.8)
        self.play(FadeIn(s2, shift=DOWN * 0.1), run_time=0.8)

        d1 = txt("整数部分写成 1.5", size=30, color=GOLD).move_to([3.4, 1.35, 0])
        d2 = txt("小数点从末尾往左移 8 位", size=28, color=CHALK).move_to([3.4, 0.4, 0])
        self.play(Write(d1), run_time=0.6)
        self.play(FadeIn(d2), run_time=0.6)

        d3 = txt("所以 = 1.5 × 10⁸", size=34, color=GREEN).move_to([0, -0.75, 0])
        self.play(FadeIn(d3, shift=UP * 0.1), run_time=0.7)
        self.finish_section()

        # ---------- 3. 指数怎么定 ----------
        self.section(3, "指数 = 整数位数 − 1")
        self.play(FadeOut(s1), FadeOut(s2), FadeOut(d1), FadeOut(d2), FadeOut(d3),
                  run_time=0.5)

        k1 = txt("150000000 有 9 位整数", size=34, color=CHALK).move_to([0, 1.3, 0])
        k2 = txt("9 − 1 = 8", size=44, color=GOLD).move_to([0, 0.25, 0])
        k3 = txt("所以指数是 8", size=36, color=GREEN).move_to([0, -0.8, 0])
        self.play(Write(k1), run_time=0.6)
        self.play(Write(k2), run_time=0.7)
        self.play(FadeIn(k3, shift=UP * 0.1), run_time=0.6)

        k4 = txt("小数用负指数，比如 0.001 = 10⁻³", size=28, color=DIM)
        k4.move_to([0, -1.9, 0])
        self.play(FadeIn(k4), run_time=0.5)
        self.finish_section()

        # ---------- 4. 小数也能写 ----------
        self.section(4, "很小的数，用负指数")
        self.play(FadeOut(k1), FadeOut(k2), FadeOut(k3), FadeOut(k4), run_time=0.5)

        v1 = txt("0.00032", size=44, color=CHALK).move_to([-3.4, 1.15, 0])
        v2 = sci("3.2", "-4", y=0.1, x=-3.3, size=44)
        self.play(Write(v1), run_time=0.7)
        self.play(FadeIn(v2, shift=DOWN * 0.1), run_time=0.7)

        w1 = txt("小数点往右移 4 位", size=30, color=BLUE).move_to([3.4, 1.05, 0])
        w2 = txt("指数就是 −4", size=30, color=BLUE).move_to([3.4, 0.15, 0])
        self.play(Write(w1), run_time=0.6)
        self.play(FadeIn(w2), run_time=0.5)

        w3 = txt("小数用负指数，大数用正指数", size=28, color=DIM).move_to([0, -1.1, 0])
        self.play(FadeIn(w3), run_time=0.6)
        self.finish_section()

        # ---------- 5. 还原回去 ----------
        self.section(5, "看指数，就能还原")
        self.play(FadeOut(v1), FadeOut(v2), FadeOut(w1), FadeOut(w2), FadeOut(w3),
                  run_time=0.5)

        h1 = txt("指数是正数 → 小数点往右移", size=32, color=GOLD).move_to([0, 1.15, 0])
        h2 = txt("指数是负数 → 小数点往左移", size=32, color=BLUE).move_to([0, 0.2, 0])
        self.play(Write(h1), run_time=0.6)
        self.play(Write(h2), run_time=0.6)

        h3 = txt("2.5 × 10³ = 2500", size=40, color=GREEN).move_to([0, -0.9, 0])
        h4 = txt("2.5 × 10⁻² = 0.025", size=40, color=GREEN).move_to([0, -1.85, 0])
        self.play(FadeIn(h3, shift=UP * 0.1), run_time=0.6)
        self.play(FadeIn(h4, shift=UP * 0.1), run_time=0.6)
        self.finish_section()

        # ---------- 6. 口诀 ----------
        self.section(6, "一位整数，指数看小数点")
        self.play(FadeOut(h1), FadeOut(h2), FadeOut(h3), FadeOut(h4), run_time=0.5)

        z1 = txt("a × 10ⁿ，1 ≤ a ＜ 10", size=46, color=GOLD).move_to([0, 1.2, 0])
        z2 = txt("n = 小数点移动的位数", size=42, color=CHALK).move_to([0, 0.1, 0])
        self.play(Write(z1), run_time=0.9)
        self.play(Write(z2), run_time=0.8)

        fin = txt("往左移是正，往右移是负", size=30, color=DIM).move_to([0, -1.1, 0])
        self.play(FadeIn(fin), run_time=0.5)
        self.finish_section()

        self.play(FadeOut(z1), FadeOut(z2), FadeOut(fin), run_time=0.6)