# -*- coding: utf-8 -*-
"""退位减法：13 − 9 怎么算。一年级「20 以内退位减法」。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403

CANDY = "#e8875a"


class TuiweiJianfaScene(NarratedScene):
    lesson = "tuiwei-jianfa"

    # ---------- 小零件 ----------
    def candy(self, at, r: float = 0.2) -> Circle:
        c = Circle(
            radius=r, stroke_color=CHALK, stroke_width=1.2,
            fill_color=CANDY, fill_opacity=0.9,
        )
        c.move_to(at)
        return c

    def stick(self, at, h: float = 1.7, color: str = BLUE) -> Rectangle:
        s = Rectangle(
            width=0.13, height=h, stroke_width=0,
            fill_color=color, fill_opacity=0.92,
        )
        s.move_to(at)
        return s

    def construct(self):
        # ================= 0. 生活问题：13 颗糖，送出 9 颗 =================
        self.section(0, "十三颗糖，送给同学九颗")

        candies = VGroup()
        for k in range(10):
            j, i = divmod(k, 5)
            candies.add(self.candy([-3.6 + i * 1.1, 1.45 - j * 1.05, 0]))
        box = RoundedRectangle(
            corner_radius=0.18, width=5.9, height=2.35,
            stroke_color=GOLD, stroke_width=2.4,
            fill_color=GOLD, fill_opacity=0.05,
        ).move_to([-1.4, 0.925, 0])
        self.play(Create(box), run_time=0.7)
        self.play(LaggedStart(*[GrowFromCenter(c) for c in candies], lag_ratio=0.06),
                  run_time=1.5)

        outside = VGroup()
        for k in range(3):
            outside.add(self.candy([2.6 + k * 0.7, 0.95, 0]))
        self.play(LaggedStart(*[FadeIn(c, shift=DOWN * 0.15) for c in outside], lag_ratio=0.14),
                  run_time=0.9)

        lab_box = txt("一盒 10 颗", size=26, color=GOLD).move_to([-1.4, 2.55, 0])
        lab_out = txt("外面 3 颗", size=26, color=BLUE).move_to([3.3, 2.55, 0])
        self.play(FadeIn(lab_box), FadeIn(lab_out), run_time=0.5)

        question = txt("还剩几颗？", size=40, color=CHALK).move_to([2.9, -1.35, 0])
        self.play(FadeIn(question, shift=UP * 0.12), run_time=0.7)
        self.finish_section()

        # ================= 1. 倒着数 =================
        self.section(1, "倒着数：13、12、11……")
        self.play(
            FadeOut(candies), FadeOut(outside), FadeOut(box),
            FadeOut(lab_box), FadeOut(lab_out), FadeOut(question),
            run_time=0.6,
        )

        axis = Line([-6.4, 0.6, 0], [6.4, 0.6, 0], color=DIM, stroke_width=2)
        self.play(Create(axis), run_time=0.6)

        def tick_x(v: int) -> float:
            return -6.3 + (v - 4) * 1.4

        ticks = VGroup()
        for v in range(4, 14):
            x = tick_x(v)
            ticks.add(Line([x, 0.45, 0], [x, 0.75, 0], color=DIM, stroke_width=2))
            ticks.add(txt(str(v), size=24, color=DIM).move_to([x, 0.08, 0]))
        self.play(LaggedStart(*[FadeIn(t) for t in ticks], lag_ratio=0.05), run_time=1.2)

        marker = Dot([tick_x(13), 0.6, 0], radius=0.15, color=GOLD)
        counter = txt("13", size=56, color=GOLD).move_to([0, 2.15, 0])
        self.play(FadeIn(marker, scale=0.8), FadeIn(counter), run_time=0.5)

        for v in range(12, 3, -1):
            self.play(
                marker.animate.move_to([tick_x(v), 0.6, 0]),
                Transform(counter, txt(str(v), size=56, color=GOLD).move_to([0, 2.15, 0])),
                run_time=0.62,
            )

        used = txt("倒着数了 9 下", size=28, color=DIM).move_to([0, -1.25, 0])
        slow = txt("一个一个数，有点慢", size=32, color=ORANGE).move_to([0, -2.05, 0])
        self.play(FadeIn(used), run_time=0.5)
        self.play(FadeIn(slow, shift=UP * 0.1), run_time=0.5)
        self.finish_section()

        # ================= 2. 把 13 拆成 10 和 3 =================
        self.section(2, "十三，拆成十和三")
        self.play(FadeOut(axis), FadeOut(ticks), FadeOut(marker),
                  FadeOut(counter), FadeOut(used), FadeOut(slow), run_time=0.6)

        bundle = VGroup()
        for k in range(10):
            bundle.add(self.stick([-3.0 + k * 0.15, 0.35, 0], color=BLUE))
        loose = VGroup()
        for k in range(3):
            loose.add(self.stick([1.85 + k * 0.55, 0.35, 0], color=BLUE))

        self.play(LaggedStart(*[FadeIn(s, shift=UP * 0.15) for s in bundle], lag_ratio=0.05),
                  run_time=1.2)
        self.play(LaggedStart(*[FadeIn(s, shift=UP * 0.15) for s in loose], lag_ratio=0.14),
                  run_time=0.8)

        band = Rectangle(width=1.9, height=0.30, stroke_color=GOLD, stroke_width=2.5,
                         fill_color=GOLD, fill_opacity=0.28).move_to([-2.33, 0.35, 0])
        self.play(Create(band), run_time=0.6)

        lab_b = txt("10 根，捆成一捆", size=26, color=GOLD).move_to([-2.33, -0.95, 0])
        lab_l = txt("3 根", size=26, color=BLUE).move_to([2.4, -0.95, 0])
        self.play(FadeIn(lab_b), FadeIn(lab_l), run_time=0.6)

        split = txt("13 = 10 + 3", size=46, color=GOLD).move_to([0, -2.15, 0])
        self.play(Write(split), run_time=0.8)
        self.finish_section()

        # ================= 3. 十减九，还剩一根 =================
        self.section(3, "从十根里拿走九根")
        self.play(FadeOut(band), FadeOut(lab_b), FadeOut(lab_l), FadeOut(split),
                  run_time=0.5)

        spread_x = [-4.9 + k * 0.62 for k in range(10)]
        self.play(*[bundle[k].animate.move_to([spread_x[k], 0.35, 0]) for k in range(10)],
                  run_time=1.1)

        brace10 = Brace(bundle, UP, color=GOLD, buff=0.18)
        lab10 = txt("10 根", size=26, color=GOLD).next_to(brace10, UP, buff=0.10)
        self.play(GrowFromCenter(brace10), FadeIn(lab10), run_time=0.6)

        self.play(LaggedStart(*[FadeOut(bundle[k], shift=UP * 0.9) for k in range(9)],
                             lag_ratio=0.07), run_time=2.4)

        rest = bundle[9]
        self.play(rest.animate.set_fill(GREEN, opacity=0.95),
                  FadeOut(brace10), FadeOut(lab10), run_time=0.6)

        got = txt("十减九，还剩一根", size=32, color=GREEN).move_to([1.6, -0.75, 0])
        eq3 = txt("10 − 9 = 1", size=52, color=GOLD).move_to([1.6, -1.9, 0])
        self.play(FadeIn(got, shift=UP * 0.1), run_time=0.6)
        self.play(Write(eq3), run_time=0.9)
        self.finish_section()

        # ================= 4. 一加三等于四 =================
        self.section(4, "再加上零头的三根")
        self.play(FadeOut(got), FadeOut(eq3), run_time=0.45)

        target_x = [-0.80, -0.25, 0.30, 0.85]
        self.play(
            *[m.animate.move_to([target_x[i], 1.05, 0])
              for i, m in enumerate([rest, *loose])],
            run_time=1.1,
        )
        group4 = VGroup(rest, *loose)
        brace4 = Brace(group4, DOWN, color=GREEN, buff=0.18)
        lab4 = txt("4 根", size=28, color=GREEN).next_to(brace4, DOWN, buff=0.10)
        self.play(GrowFromCenter(brace4), FadeIn(lab4), run_time=0.6)

        step1 = txt("10 − 9 = 1", size=36, color=CHALK).move_to([-3.2, -0.95, 0])
        arrow = Arrow([-1.25, -0.95, 0], [-0.25, -0.95, 0], color=DIM,
                      stroke_width=2.4, buff=0, max_tip_length_to_length_ratio=0.3)
        step2 = txt("1 + 3 = 4", size=36, color=GREEN).move_to([1.5, -0.95, 0])
        self.play(FadeIn(step1), run_time=0.5)
        self.play(GrowArrow(arrow), FadeIn(step2), run_time=0.6)

        final4 = txt("13 − 9 = 4", size=60, color=GOLD).move_to([0, -2.35, 0])
        self.play(Write(final4), run_time=0.9)
        self.finish_section()

        # ================= 5. 平十法 / 想加算减 =================
        self.section(5, "还有两种办法")
        self.play(*[FadeOut(m) for m in [*bundle, *loose, brace4, lab4,
                                         step1, arrow, step2, final4]],
                  run_time=0.65)

        div = Line([0, -2.55, 0], [0, 2.55, 0], color=DIM, stroke_width=1.4)
        self.play(Create(div), run_time=0.5)

        t_left = txt("平十法（先减到十）", size=28, color=GOLD).move_to([-3.4, 2.2, 0])
        l1 = txt("13 − 3 = 10", size=40, color=CHALK).move_to([-3.4, 0.85, 0])
        l_arrow = Arrow([-3.4, 0.35, 0], [-3.4, -0.25, 0], color=DIM,
                        stroke_width=2.4, buff=0, max_tip_length_to_length_ratio=0.28)
        l2 = txt("10 − 6 = 4", size=40, color=GREEN).move_to([-3.4, -0.95, 0])
        l3 = txt("把 9 拆成 3 和 6", size=24, color=DIM).move_to([-3.4, -2.05, 0])

        self.play(FadeIn(t_left), run_time=0.5)
        self.play(Write(l1), run_time=0.7)
        self.play(GrowArrow(l_arrow), run_time=0.4)
        self.play(Write(l2), run_time=0.7)
        self.play(FadeIn(l3), run_time=0.5)

        t_right = txt("想加算减", size=28, color=BLUE).move_to([3.3, 2.2, 0])
        r1 = txt("9 + 4 = 13", size=40, color=CHALK).move_to([3.3, 0.85, 0])
        r_arrow = Arrow([3.3, 0.35, 0], [3.3, -0.25, 0], color=DIM,
                        stroke_width=2.4, buff=0, max_tip_length_to_length_ratio=0.28)
        r2 = txt("13 − 9 = 4", size=40, color=GREEN).move_to([3.3, -0.95, 0])
        r3 = txt("加减互逆，想到加就想到了减", size=24, color=DIM).move_to([3.3, -2.05, 0])

        self.play(FadeIn(t_right), run_time=0.5)
        self.play(Write(r1), run_time=0.7)
        self.play(GrowArrow(r_arrow), run_time=0.4)
        self.play(Write(r2), run_time=0.7)
        self.play(FadeIn(r3), run_time=0.5)
        self.finish_section()

        # ================= 6. 收束：破十法口诀 =================
        self.section(6, "破十法口诀")
        self.play(FadeOut(div), FadeOut(t_left), FadeOut(l1), FadeOut(l_arrow),
                  FadeOut(l2), FadeOut(l3), FadeOut(t_right), FadeOut(r1),
                  FadeOut(r_arrow), FadeOut(r2), FadeOut(r3), run_time=0.6)

        head = txt("十几减 9，先破十", size=50, color=GOLD).move_to([0, 2.15, 0])
        self.play(Write(head), run_time=0.9)

        s1 = txt("① 10 − 9 = 1", size=40, color=CHALK).move_to([-2.6, 0.6, 0])
        s2 = txt("② 1 + 3 = 4", size=40, color=GREEN).move_to([2.6, 0.6, 0])
        mid = Arrow([-0.75, 0.6, 0], [0.75, 0.6, 0], color=DIM,
                    stroke_width=2.4, buff=0, max_tip_length_to_length_ratio=0.25)
        self.play(FadeIn(s1), run_time=0.5)
        self.play(GrowArrow(mid), FadeIn(s2), run_time=0.6)

        big = txt("13 − 9 = 4", size=68, color=GOLD).move_to([0, -0.9, 0])
        self.play(Write(big), run_time=0.9)

        tags = txt("破十法 · 平十法 · 想加算减", size=28, color=DIM).move_to([0, -2.15, 0])
        self.play(FadeIn(tags, shift=UP * 0.1), run_time=0.6)
        self.finish_section()

        self.play(FadeOut(head), FadeOut(s1), FadeOut(s2), FadeOut(mid),
                  FadeOut(big), FadeOut(tags), run_time=0.8)