# -*- coding: utf-8 -*-
"""因式分解：提公因式、公式法、分解要彻底、与整式乘法的互逆关系。八年级。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


def P(x, y):
    return np.array([float(x), float(y), 0.0])


class YinshiScene(NarratedScene):
    lesson = "yinshi"

    def clear_stage(self, run_time: float = 0.5):
        keep = {id(self._track), id(self._fill)}
        junk = [m for m in self.mobjects if id(m) not in keep]
        if junk:
            self.play(*[FadeOut(m) for m in junk], run_time=run_time)
        self.cur_title = None
        self.cur_sub = None

    # ---------------- 0. 从 12 = 3 × 4 说起 ---------------- 19.5
    def scene_story(self):
        self.section(0, "把和差写成乘积")

        l1 = txt("12", size=54, color=CHALK)
        l1.move_to([0, 1.65, 0])
        l1.align_to(P(-2.35, 0), RIGHT)
        r1 = txt("3 × 4", size=44, color=GOLD)
        r1.move_to([0, 1.65, 0])
        r1.align_to(P(-1.45, 0), LEFT)
        self.play(FadeIn(l1, shift=UP * 0.05), run_time=0.8)
        self.play(FadeIn(r1, shift=UP * 0.05), run_time=0.9)
        a1 = Arrow(P(-2.28, 1.65), P(-1.5, 1.65), color=DIM, stroke_width=2.6,
                   max_tip_length_to_length_ratio=0.3)
        self.play(Create(a1), run_time=0.5)
        n1 = txt("因数分解", size=24, color=DIM).next_to(r1, RIGHT, buff=0.5)
        self.play(FadeIn(n1, shift=RIGHT * 0.05), run_time=0.7)

        l2 = txt("a² − b²", size=42, color=CHALK)
        l2.move_to([0, 0.3, 0])
        l2.align_to(P(-2.35, 0), RIGHT)
        r2 = txt("(a + b)(a − b)", size=40, color=GREEN)
        r2.move_to([0, 0.3, 0])
        r2.align_to(P(-1.45, 0), LEFT)
        self.play(FadeIn(l2, shift=UP * 0.05), run_time=0.9)
        self.play(FadeIn(r2, shift=UP * 0.05), run_time=1.1)
        a2 = Arrow(P(-2.28, 0.3), P(-1.5, 0.3), color=DIM, stroke_width=2.6,
                   max_tip_length_to_length_ratio=0.3)
        self.play(Create(a2), run_time=0.5)
        n2 = txt("因式分解", size=24, color=DIM).next_to(r2, RIGHT, buff=0.5)
        self.play(FadeIn(n2, shift=RIGHT * 0.05), run_time=0.7)

        t1 = VGroup(
            txt("加减的式子 → 几个式子相乘", size=30, color=GOLD),
            txt("乘法比加减好算，很多题拆开就一眼看出答案", size=25, color=CHALK),
        ).arrange(DOWN, buff=0.36).move_to([0, -1.35, 0])
        for m in t1:
            self.play(FadeIn(m, shift=UP * 0.05), run_time=0.9)

        self.wait(2.6)
        self.finish_section()

    # ---------------- 1. 提公因式 ---------------- 22.6
    def scene_common(self):
        self.section(1, "方法一：提公因式")

        src = txt("6a²b + 9ab²", size=44, color=CHALK).move_to([0, 2.15, 0])
        self.play(FadeIn(src, shift=UP * 0.05), run_time=1.0)

        fac = label_box("公因式：3ab", size=30, color=GOLD).move_to([0, 1.1, 0])
        self.play(FadeIn(fac, scale=0.97), run_time=1.0)

        res = VGroup(
            txt("3ab", size=42, color=GOLD),
            txt("(2a + 3b)", size=42, color=GREEN),
        ).arrange(RIGHT, buff=0.22).move_to([0, -0.15, 0])
        self.play(FadeIn(res, shift=UP * 0.05), run_time=1.2)

        chk = VGroup(
            txt("乘开检验：3ab·2a = 6a²b", size=25, color=CHALK),
            txt("3ab·3b = 9ab²，能还原", size=25, color=CHALK),
        ).arrange(DOWN, buff=0.3).move_to([0, -1.35, 0])
        for m in chk:
            self.play(FadeIn(m, shift=UP * 0.05), run_time=0.8)

        note = txt("找公因式：系数取最大公约数，字母取最低次", size=24, color=DIM)
        note.move_to([0, -2.6, 0])
        self.play(FadeIn(note, shift=UP * 0.05), run_time=0.9)
        self.wait(2.4)
        self.finish_section()

    # ---------------- 2. 公式法 ---------------- 24.0
    def scene_formula(self):
        self.section(2, "方法二：套公式")

        b1 = label_box("平方差：a² − b² = (a + b)(a − b)", size=28, color=GOLD)
        b1.move_to([0, 2.15, 0])
        self.play(FadeIn(b1, scale=0.97), run_time=1.1)

        b2 = label_box("完全平方：a² + 2ab + b² = (a + b)²", size=28, color=BLUE)
        b2.move_to([0, 1.05, 0])
        self.play(FadeIn(b2, scale=0.97), run_time=1.1)

        b3 = label_box("a² − 2ab + b² = (a − b)²", size=28, color=BLUE)
        b3.move_to([0, 0.1, 0])
        self.play(FadeIn(b3, scale=0.97), run_time=1.0)

        t1 = txt("用之前先看形状：两项还是三项？", size=27, color=CHALK)
        t1.move_to([0, -0.95, 0])
        self.play(FadeIn(t1, shift=UP * 0.05), run_time=0.9)

        t2 = VGroup(
            txt("两项、都是平方、中间是减号 → 平方差", size=24, color=GOLD),
            txt("三项、首尾是平方、中间是加减 2ab → 完全平方", size=24, color=BLUE),
        ).arrange(DOWN, buff=0.32).move_to([0, -1.9, 0])
        for m in t2:
            self.play(FadeIn(m, shift=UP * 0.05), run_time=0.8)

        self.wait(2.6)
        self.finish_section()

    # ---------------- 3. 分解要彻底 ---------------- 26.7
    def scene_thorough(self):
        self.section(3, "分解要彻底")

        s0 = txt("x⁴ − 1", size=40, color=CHALK).move_to([0, 2.15, 0])
        self.play(FadeIn(s0), run_time=0.9)

        a1 = txt("↓", size=32, color=DIM).move_to([0, 1.5, 0])
        self.play(FadeIn(a1), run_time=0.5)
        s1 = txt("(x² + 1)(x² − 1)", size=38, color=GOLD).move_to([0, 0.85, 0])
        self.play(FadeIn(s1, shift=UP * 0.05), run_time=1.0)

        a2 = txt("↓", size=32, color=DIM).move_to([0, 0.2, 0])
        self.play(FadeIn(a2), run_time=0.5)
        s2 = VGroup(
            txt("(x² + 1)", size=38, color=GOLD),
            txt("(x + 1)(x − 1)", size=38, color=GREEN),
        ).arrange(RIGHT, buff=0.25).move_to([0, -0.45, 0])
        self.play(FadeIn(s2, shift=UP * 0.05), run_time=1.2)

        note = VGroup(
            txt("x² − 1 还能再拆，必须拆到不能再拆", size=26, color=CHALK),
            txt("x² + 1 在实数范围内拆不动，就停在这里", size=25, color=DIM),
        ).arrange(DOWN, buff=0.34).move_to([0, -1.65, 0])
        for m in note:
            self.play(FadeIn(m, shift=UP * 0.05), run_time=0.85)

        tail = txt("最后写成三个式子相乘，才算完成", size=25, color=GOLD)
        tail.move_to([0, -2.65, 0])
        self.play(FadeIn(tail, shift=UP * 0.05), run_time=0.85)
        self.wait(2.4)
        self.finish_section()

    # ---------------- 4. 与整式乘法互逆 ---------------- 19.0
    def scene_reverse(self):
        self.section(4, "它和整式乘法正好相反")

        left = VGroup(
            txt("整式乘法", size=30, color=GOLD),
            txt("(a + b)(a − b) → a² − b²", size=27, color=CHALK),
            txt("乘开", size=23, color=DIM),
        ).arrange(DOWN, buff=0.3).move_to([-3.9, 0.75, 0])
        right = VGroup(
            txt("因式分解", size=30, color=GREEN),
            txt("a² − b² → (a + b)(a − b)", size=27, color=CHALK),
            txt("写成乘积", size=23, color=DIM),
        ).arrange(DOWN, buff=0.3).move_to([3.9, 0.75, 0])
        self.play(FadeIn(left, shift=UP * 0.05), run_time=1.0)
        self.play(FadeIn(right, shift=UP * 0.05), run_time=1.0)

        ar1 = Arrow(P(-1.15, 0.95), P(1.15, 0.95), color=GOLD, stroke_width=3,
                    max_tip_length_to_length_ratio=0.18)
        ar2 = Arrow(P(1.15, 0.4), P(-1.15, 0.4), color=GREEN, stroke_width=3,
                    max_tip_length_to_length_ratio=0.18)
        self.play(Create(ar1), run_time=0.7)
        self.play(Create(ar2), run_time=0.7)

        t1 = VGroup(
            txt("检验方法：把结果乘开，看能不能回到原式", size=27, color=CHALK),
            txt("乘不回去，就是分解错了", size=25, color=RED),
        ).arrange(DOWN, buff=0.34).move_to([0, -1.45, 0])
        for m in t1:
            self.play(FadeIn(m, shift=UP * 0.05), run_time=0.9)

        self.wait(2.4)
        self.finish_section()

    # ---------------- 5. 用它把计算变简单 ---------------- 18.8
    def scene_apply(self):
        self.section(5, "拆开之后，一步算出")

        q = txt("计算：101 × 99", size=32, color=CHALK).move_to([0, 2.3, 0])
        self.play(FadeIn(q, shift=UP * 0.05), run_time=0.9)

        l1 = VGroup(
            txt("101 × 99", size=34, color=CHALK),
            txt("=", size=32, color=DIM),
            txt("(100 + 1)(100 − 1)", size=34, color=GOLD),
        ).arrange(RIGHT, buff=0.3).move_to([0, 1.15, 0])
        self.play(FadeIn(l1, shift=UP * 0.05), run_time=1.0)

        l2 = VGroup(
            txt("=", size=32, color=DIM),
            txt("100² − 1²", size=34, color=GREEN),
            txt("=", size=32, color=DIM),
            txt("9999", size=38, color=GREEN),
        ).arrange(RIGHT, buff=0.3).move_to([0, 0.05, 0])
        self.play(FadeIn(l2, shift=UP * 0.05), run_time=1.0)

        note = VGroup(
            txt("把接近整百的两个数，凑成和与差", size=26, color=CHALK),
            txt("平方差一拆，竖式都省了", size=24, color=DIM),
        ).arrange(DOWN, buff=0.34).move_to([0, -1.35, 0])
        for m in note:
            self.play(FadeIn(m, shift=UP * 0.05), run_time=0.85)

        self.wait(2.4)
        self.finish_section()

    # ---------------- 6. 例题与三个易错点 ---------------- 25.9
    def scene_ex(self):
        self.section(6, "例题与三个易错点")

        q = txt("分解因式：2x² − 8", size=29, color=CHALK).move_to([0, 2.35, 0])
        self.play(FadeIn(q, shift=UP * 0.05), run_time=0.9)

        s1 = VGroup(
            txt("2x² − 8", size=34, color=CHALK),
            txt("=", size=30, color=DIM),
            txt("2(x² − 4)", size=34, color=GOLD),
        ).arrange(RIGHT, buff=0.28).move_to([-0.6, 1.4, 0])
        self.play(FadeIn(s1, shift=UP * 0.05), run_time=0.9)

        s2 = VGroup(
            txt("=", size=30, color=DIM),
            txt("2(x + 2)(x − 2)", size=34, color=GREEN),
        ).arrange(RIGHT, buff=0.28).move_to([-0.6, 0.6, 0])
        self.play(FadeIn(s2, shift=UP * 0.05), run_time=1.0)

        tip = txt("先提公因式，再用公式，顺序不能反", size=24, color=CHALK)
        tip.move_to([0, -0.2, 0])
        self.play(FadeIn(tip, shift=UP * 0.05), run_time=0.8)

        items = [
            ("公因式提不干净", "系数和字母都提全"),
            ("平方差的符号丢三落四", "先写 (a+b)(a−b)"),
            ("分解到一半就停手", "拆到不能再拆"),
        ]
        y = -1.2
        for bad_s, good_s in items:
            bad = txt(bad_s, size=24, color=RED).move_to([-3.0, y, 0])
            good = txt(good_s, size=23, color=GREEN).move_to([3.7, y, 0])
            cross = Line([bad.get_left()[0] - 0.07, y - 0.02, 0],
                         [bad.get_right()[0] + 0.07, y - 0.02, 0],
                         color=RED, stroke_width=2.2)
            self.play(FadeIn(bad, shift=RIGHT * 0.05), run_time=0.55)
            self.play(Create(cross), run_time=0.35)
            self.play(FadeIn(good, shift=RIGHT * 0.05), run_time=0.55)
            y -= 0.72

        self.wait(2.6)
        self.finish_section()

    def construct(self):
        self.scene_story()
        self.clear_stage()
        self.scene_common()
        self.clear_stage()
        self.scene_formula()
        self.clear_stage()
        self.scene_thorough()
        self.clear_stage()
        self.scene_reverse()
        self.clear_stage()
        self.scene_apply()
        self.clear_stage()
        self.scene_ex()
        self.clear_stage(0.8)