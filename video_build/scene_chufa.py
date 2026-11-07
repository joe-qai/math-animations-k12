# -*- coding: utf-8 -*-
"""除法：平均分，还是几个几？"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


class ChufaScene(NarratedScene):
    lesson = "chufa-yiyi"

    TOP_Y = [1.75, 0.85]
    BASKET_X = [-4.35, -1.45, 1.45, 4.35]
    BASKET_Y = -1.05
    BAG_X = [-3.7, 0.0, 3.7]

    def apples_at_top(self) -> VGroup:
        g = VGroup()
        for k in range(12):
            row, col = divmod(k, 6)
            g.add(
                Circle(radius=0.22, color=RED, fill_opacity=0.92, stroke_width=0)
                .move_to([(col - 2.5) * 0.9, self.TOP_Y[row], 0])
            )
        return g

    def construct(self):
        # ================= 0. 12 个苹果，4 个小朋友 =================
        self.section(0, "12 个苹果，平均分给 4 人")

        apples = self.apples_at_top()
        self.play(LaggedStart(*[GrowFromCenter(a) for a in apples], lag_ratio=0.05),
                  run_time=1.3)

        baskets = VGroup()
        for x in self.BASKET_X:
            basket = RoundedRectangle(
                corner_radius=0.16, width=2.35, height=1.15,
                stroke_color=DIM, stroke_width=2,
                fill_color=WHITE, fill_opacity=0.05,
            ).move_to([x, self.BASKET_Y, 0])
            baskets.add(basket)
        self.play(LaggedStart(*[FadeIn(b) for b in baskets], lag_ratio=0.12), run_time=0.9)

        q = txt("每人分几个？", size=40, color=CHALK).move_to([0, 2.62, 0])
        self.play(FadeIn(q, shift=DOWN * 0.1), run_time=0.5)
        self.finish_section()

        # ================= 1. 一个一个地发 =================
        self.section(1, "一个一个地发：每人都一样多")
        self.play(FadeOut(q), run_time=0.3)

        # 轮转发：第 r 轮，每个篮子拿 1 个
        for r in range(3):
            moves = []
            for b, bx in enumerate(self.BASKET_X):
                idx = r * 4 + b
                moves.append(
                    apples[idx].animate.move_to([bx + (r - 1) * 0.62, self.BASKET_Y + 0.08, 0])
                )
            self.play(*moves, run_time=0.75)

        per = VGroup()
        for bx in self.BASKET_X:
            per.add(txt("3 个", size=26, color=GOLD).move_to([bx, self.BASKET_Y - 0.82, 0]))
        self.play(LaggedStart(*[FadeIn(p, shift=UP * 0.08) for p in per], lag_ratio=0.1),
                  run_time=0.7)
        self.finish_section()

        # ================= 2. 12 ÷ 4 = 3 =================
        self.section(2, "平均分：每份同样多")
        eq = txt("12 ÷ 4 = 3", size=64, color=GOLD).move_to([0, -2.55, 0])
        note = txt("4 个小朋友，每人 3 个", size=28, color=DIM).move_to([0, 2.55, 0])
        self.play(FadeIn(eq, shift=UP * 0.1), run_time=0.7)
        self.play(FadeIn(note), run_time=0.5)
        self.finish_section()

        # ================= 3. 第二种意思：每 4 个一袋 =================
        self.section(3, "换一种问法：每 4 个装一袋")
        self.play(FadeOut(per), FadeOut(eq), FadeOut(note), FadeOut(baskets), run_time=0.6)

        back = []
        for k, a in enumerate(apples):
            row, col = divmod(k, 6)
            back.append(a.animate.move_to([(col - 2.5) * 0.9, self.TOP_Y[row], 0]))
        self.play(*back, run_time=1.0)

        bags = VGroup()
        for x in self.BAG_X:
            bags.add(
                RoundedRectangle(
                    corner_radius=0.14, width=2.55, height=1.55,
                    stroke_color=GOLD, stroke_width=2,
                    fill_color=GOLD, fill_opacity=0.05,
                ).move_to([x, self.BASKET_Y, 0])
            )
        bag_lab = txt("每袋 4 个", size=26, color=GOLD).move_to([0, 2.55, 0])
        self.play(FadeIn(bag_lab), run_time=0.4)
        self.play(LaggedStart(*[FadeIn(b) for b in bags], lag_ratio=0.12), run_time=0.8)
        self.finish_section()

        # ================= 4. 装袋 =================
        self.section(4, "装成了 3 袋")
        slots = [(-0.45, 0.35), (0.45, 0.35), (-0.45, -0.42), (0.45, -0.42)]
        for g, bx in enumerate(self.BAG_X):
            moves = []
            for s, (dx, dy) in enumerate(slots):
                a = apples[g * 4 + s]
                moves.append(a.animate.move_to([bx + dx, self.BASKET_Y + dy, 0]))
            self.play(*moves, run_time=0.7)

        self.play(Indicate(bags[0], color=WHITE, scale_factor=1.03), run_time=0.5)
        self.play(Indicate(bags[1], color=WHITE, scale_factor=1.03), run_time=0.5)
        self.play(Indicate(bags[2], color=WHITE, scale_factor=1.03), run_time=0.5)

        eq2 = txt("12 ÷ 4 = 3（袋）", size=48, color=GOLD).move_to([0, 2.5, 0])
        self.play(Transform(bag_lab, eq2), run_time=0.7)
        self.finish_section()

        # ================= 5. 12 里面有几个 4 =================
        self.play(FadeOut(bag_lab), run_time=0.3)
        self.section(5, "除以 4，就是问：12 里面有几个 4")

        sub1 = txt("12 − 4 = 8", size=40, color=CHALK).move_to([0, 2.28, 0])
        sub2 = txt("8 − 4 = 4", size=40, color=CHALK).move_to([0, 1.58, 0])
        sub3 = txt("4 − 4 = 0", size=40, color=CHALK).move_to([0, 0.88, 0])
        times = txt("减了 3 次 → 3 个 4", size=34, color=GREEN).move_to([0, 0.1, 0])

        self.play(FadeIn(sub1, shift=RIGHT * 0.1), run_time=0.45)
        self.play(FadeIn(sub2, shift=RIGHT * 0.1), run_time=0.45)
        self.play(FadeIn(sub3, shift=RIGHT * 0.1), run_time=0.45)
        self.play(FadeIn(times, scale=0.9), run_time=0.5)
        self.finish_section()

        # ================= 6. 两副面孔 =================
        self.section(6, "除法的两副面孔")
        self.play(FadeOut(bags), FadeOut(apples),
                  FadeOut(sub1), FadeOut(sub2), FadeOut(sub3),
                  FadeOut(times), run_time=0.6)

        left = VGroup(
            txt("平均分", size=38, color=BLUE),
            txt("每份分到几个", size=27, color=CHALK),
            txt("12 ÷ 4 = 3（个）", size=30, color=GOLD),
        ).arrange(DOWN, buff=0.32).move_to([-3.3, 0.35, 0])

        right = VGroup(
            txt("包含除", size=38, color=GREEN),
            txt("里面有几个 4", size=27, color=CHALK),
            txt("12 ÷ 4 = 3（份）", size=30, color=GOLD),
        ).arrange(DOWN, buff=0.32).move_to([3.3, 0.35, 0])

        sep = Line([0, 1.9, 0], [0, -1.3, 0], color=WHITE, stroke_width=1.5, stroke_opacity=0.18)
        self.play(FadeIn(left, shift=RIGHT * 0.15), FadeIn(right, shift=LEFT * 0.15),
                  Create(sep), run_time=1.0)

        final = txt("都是把总数，按每份的大小分组", size=30, color=GOLD).move_to([0, -2.15, 0])
        self.play(FadeIn(final, shift=UP * 0.1), run_time=0.6)
        self.finish_section()

        self.play(FadeOut(left), FadeOut(right), FadeOut(sep), FadeOut(final), run_time=0.8)
