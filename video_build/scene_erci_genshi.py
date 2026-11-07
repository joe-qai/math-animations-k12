# -*- coding: utf-8 -*-
"""二次根式：从开方开不尽，到化简与合并。八年级下。"""

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


def P(x, y):
    return np.array([float(x), float(y), 0.0])


def frac(n, d, color=CHALK, size=30):
    """竖排分数（自建，不用 LaTeX）。"""
    t1 = txt(str(n), size=size, color=color)
    t2 = txt(str(d), size=size, color=color)
    line = Line(LEFT, RIGHT, color=color, stroke_width=2)
    line.set_width(max(t1.width, t2.width) + 0.12)
    return VGroup(t1, line, t2).arrange(DOWN, buff=0.08)


class ErciGenshiScene(NarratedScene):
    lesson = "erci_genshi"

    def clear_stage(self, run_time: float = 0.5):
        keep = {id(self._track), id(self._fill)}
        junk = [m for m in self.mobjects if id(m) not in keep]
        if junk:
            self.play(*[FadeOut(m) for m in junk], run_time=run_time)
        self.cur_title = None
        self.cur_sub = None

    # ---------------- 0. 开方开不尽 ---------------- 20.2
    def scene_intro(self):
        self.section(0, "开方开不尽，就用根号留住")

        specs = [
            ("面积 4", "边长 2", 1.05, -4.3, CHALK),
            ("面积 9", "边长 3", 1.575, -1.55, CHALK),
            ("面积 2", "边长 √2", 0.742, 2.6, GOLD),
        ]
        for label, side, s, cx, col in specs:
            sq = Square(side_length=s, color=col, stroke_width=2.6,
                        fill_color=col, fill_opacity=0.10)
            sq.move_to([cx, 0.6, 0])
            self.play(Create(sq), run_time=0.9)
            tl = txt(label, size=24, color=DIM).move_to([cx, 2.0, 0])
            sl = txt(side, size=26, color=col).move_to([cx, -0.95, 0])
            self.play(FadeIn(tl), run_time=0.55)
            self.play(FadeIn(sl, shift=UP * 0.04), run_time=0.55)
        self.wait(0.8)

        n1 = txt("面积 a 的正方形，边长是 √a", size=27, color=CHALK).move_to([0, -2.15, 0])
        self.play(FadeIn(n1, shift=UP * 0.05), run_time=0.9)
        n2 = txt("√2 ≈ 1.414，是个无限不循环小数", size=24, color=DIM).move_to([0, -2.8, 0])
        self.play(FadeIn(n2, shift=UP * 0.05), run_time=0.9)
        self.wait(3.0)
        self.finish_section()

    # ---------------- 1. 定义与双重非负性 ---------------- 22.8
    def scene_def(self):
        self.section(1, "二次根式：√a")

        box = label_box("形如 √a 的式子叫二次根式", size=30, color=GOLD)
        box.move_to([0, 1.95, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.1)
        self.wait(0.8)

        n1 = txt("a 叫被开方数", size=26, color=CHALK).move_to([-3.4, 0.9, 0])
        self.play(FadeIn(n1, shift=UP * 0.04), run_time=0.8)
        self.wait(0.6)

        c1 = label_box("a ≥ 0", size=30, color=GREEN).move_to([-3.4, -0.15, 0])
        self.play(FadeIn(c1, scale=0.97), run_time=0.9)
        w1 = txt("负数在实数范围内没有平方根", size=23, color=DIM).move_to([-3.4, -0.95, 0])
        self.play(FadeIn(w1, shift=UP * 0.04), run_time=0.85)
        self.wait(1.0)

        n2 = txt("结果也不小于 0", size=26, color=CHALK).move_to([3.2, 0.9, 0])
        self.play(FadeIn(n2, shift=UP * 0.04), run_time=0.8)
        self.wait(0.6)

        c2 = label_box("√a ≥ 0", size=30, color=GREEN).move_to([3.2, -0.15, 0])
        self.play(FadeIn(c2, scale=0.97), run_time=0.9)
        self.wait(1.0)

        key = label_box("双重非负性：被开方数非负，结果也非负", size=27, color=GOLD)
        key.move_to([0, -2.15, 0])
        self.play(FadeIn(key, scale=0.97), run_time=1.1)
        self.wait(3.6)
        self.finish_section()

    # ---------------- 2. 两条性质 ---------------- 27.4
    def scene_prop(self):
        self.section(2, "两条基本性质")

        b1 = label_box("(√a)² = a　（a ≥ 0）", size=31, color=GOLD)
        b1.move_to([0, 2.0, 0])
        self.play(FadeIn(b1, scale=0.97), run_time=1.0)
        self.wait(0.8)

        e1 = txt("例：(√5)² = 5", size=26, color=CHALK).move_to([0, 1.05, 0])
        self.play(FadeIn(e1, shift=UP * 0.04), run_time=0.8)
        self.wait(1.2)

        b2 = label_box("√(a²) = |a|", size=31, color=GREEN)
        b2.move_to([0, -0.05, 0])
        self.play(FadeIn(b2, scale=0.97), run_time=1.0)
        self.wait(0.8)

        n1 = txt("a 是正数：结果就是 a", size=25, color=CHALK).move_to([-3.4, -1.15, 0])
        self.play(FadeIn(n1, shift=UP * 0.04), run_time=0.8)

        n2 = txt("a 是负数：结果是 −a", size=25, color=RED).move_to([3.4, -1.15, 0])
        self.play(FadeIn(n2, shift=UP * 0.04), run_time=0.8)
        self.wait(1.2)

        bad = txt("反例：√((−3)²) = √9 = 3，不是 −3", size=26, color=RED).move_to([0, -2.15, 0])
        self.play(FadeIn(bad, shift=UP * 0.05), run_time=0.9)
        self.wait(1.0)

        why = txt("先算平方，再开方，结果一定非负", size=25, color=DIM).move_to([0, -2.8, 0])
        self.play(FadeIn(why, shift=UP * 0.05), run_time=0.9)
        self.wait(3.0)
        self.finish_section()

    # ---------------- 3. 乘除 ---------------- 23.8
    def scene_muldiv(self):
        self.section(3, "乘除：根号可以合并")

        b1 = label_box("√a · √b = √(ab)", size=31, color=GOLD).move_to([-2.9, 1.85, 0])
        self.play(FadeIn(b1, scale=0.97), run_time=1.0)
        e1 = txt("√2 · √3 = √6", size=26, color=CHALK).move_to([-2.9, 0.9, 0])
        self.play(FadeIn(e1, shift=UP * 0.04), run_time=0.8)
        self.wait(1.0)

        b2 = label_box("√a ÷ √b = √(a/b)", size=31, color=GREEN).move_to([3.0, 1.85, 0])
        self.play(FadeIn(b2, scale=0.97), run_time=1.0)
        e2 = txt("√8 ÷ √2 = √4 = 2", size=26, color=CHALK).move_to([3.0, 0.9, 0])
        self.play(FadeIn(e2, shift=UP * 0.04), run_time=0.8)
        self.wait(1.4)

        n1 = txt("条件：a ≥ 0，b > 0", size=25, color=DIM).move_to([0, -0.35, 0])
        self.play(FadeIn(n1, shift=UP * 0.04), run_time=0.8)
        self.wait(0.8)

        warn = label_box("只有乘除能这样合并，加减不行", size=27, color=RED)
        warn.move_to([0, -1.55, 0])
        self.play(FadeIn(warn, scale=0.97), run_time=1.0)
        self.wait(1.0)

        bad = txt("√2 + √3 ≠ √5", size=27, color=RED).move_to([0, -2.55, 0])
        self.play(FadeIn(bad, shift=UP * 0.04), run_time=0.85)
        self.play(Create(Line([-1.25, -2.55, 0], [1.25, -2.55, 0], color=RED, stroke_width=2.4)),
                  run_time=0.5)
        self.wait(2.4)
        self.finish_section()

    # ---------------- 4. 最简二次根式 ---------------- 26.7
    def scene_simplify(self):
        self.section(4, "化简：化到最简")

        n1 = txt("最简二次根式，两个标准：", size=27, color=GOLD).move_to([0, 2.25, 0])
        self.play(FadeIn(n1, shift=UP * 0.05), run_time=0.9)

        c1 = txt("① 被开方数不含分母", size=26, color=CHALK).move_to([0, 1.5, 0])
        self.play(FadeIn(c1, shift=UP * 0.04), run_time=0.75)
        c2 = txt("② 被开方数不含能开得尽方的因数", size=26, color=CHALK).move_to([0, 0.85, 0])
        self.play(FadeIn(c2, shift=UP * 0.04), run_time=0.8)
        self.wait(1.2)

        s1 = txt("√12 = √(4×3) = 2√3", size=28, color=GREEN).move_to([-3.2, -0.15, 0])
        self.play(FadeIn(s1, shift=UP * 0.04), run_time=0.9)
        self.wait(0.6)

        s2 = txt("√(4/9) = 2/3", size=28, color=GREEN).move_to([3.2, -0.15, 0])
        self.play(FadeIn(s2, shift=UP * 0.04), run_time=0.9)
        self.wait(1.2)

        r1 = txt("12 = 4 × 3，4 能开成 2", size=24, color=DIM).move_to([-2.9, -1.15, 0])
        a1 = txt("3 留在根号里", size=24, color=DIM).move_to([-2.9, -1.8, 0])
        self.play(FadeIn(r1), run_time=0.6)
        self.play(FadeIn(a1, shift=UP * 0.04), run_time=0.8)
        self.wait(1.0)

        rat = txt("分母有理化：1/√2 = √2/2", size=26, color=GOLD).move_to([3.2, -1.65, 0])
        self.play(FadeIn(rat, shift=UP * 0.04), run_time=0.9)
        self.wait(0.6)

        fin = txt("最后检查：分母没有根号，根号里没有平方因数", size=24, color=CHALK)
        fin.move_to([0, -2.85, 0])
        self.play(FadeIn(fin, shift=UP * 0.04), run_time=0.9)
        self.wait(3.0)
        self.finish_section()

    # ---------------- 5. 加减与同类二次根式 ---------------- 26.8
    def scene_add(self):
        self.section(5, "加减：先化简，再合并")

        n1 = txt("化成最简后，被开方数相同的叫同类二次根式", size=26, color=CHALK)
        n1.move_to([0, 2.2, 0])
        self.play(FadeIn(n1, shift=UP * 0.05), run_time=0.9)
        n2 = txt("同类二次根式，像合并同类项一样合并", size=26, color=DIM)
        n2.move_to([0, 1.5, 0])
        self.play(FadeIn(n2, shift=UP * 0.04), run_time=0.9)
        self.wait(1.2)

        l1 = txt("√8 = 2√2", size=29, color=GOLD).move_to([-3.6, 0.35, 0])
        self.play(FadeIn(l1, shift=UP * 0.04), run_time=0.8)
        l2 = txt("√18 = 3√2", size=29, color=GOLD).move_to([-3.6, -0.4, 0])
        self.play(FadeIn(l2, shift=UP * 0.04), run_time=0.8)
        self.wait(0.8)

        r1 = txt("√8 + √18", size=30, color=CHALK).move_to([2.0, 0.35, 0])
        self.play(FadeIn(r1, shift=RIGHT * 0.04), run_time=0.7)
        r2 = txt("= 2√2 + 3√2", size=30, color=CHALK).move_to([2.0, -0.4, 0])
        self.play(FadeIn(r2, shift=RIGHT * 0.04), run_time=0.7)
        r3 = txt("= 5√2", size=32, color=GREEN).move_to([2.0, -1.15, 0])
        self.play(FadeIn(r3, shift=UP * 0.04), run_time=0.8)
        self.wait(1.4)

        n3 = txt("2√2 与 3√2 是同类，系数相加，根号不变", size=24, color=DIM)
        n3.move_to([0, -1.95, 0])
        self.play(FadeIn(n3, shift=UP * 0.04), run_time=0.9)
        self.wait(1.0)

        warn = txt("不同类就不能合并：√2 + √3 只能保留", size=25, color=RED)
        warn.move_to([0, -2.7, 0])
        self.play(FadeIn(warn, shift=UP * 0.04), run_time=0.9)
        self.wait(3.0)
        self.finish_section()

    # ---------------- 6. 例题与易错点 ---------------- 33.3
    def scene_example(self):
        self.section(6, "例题：√((−3)²) 等于几")

        q = txt("计算 √((−3)²)", size=30, color=CHALK).move_to([0, 2.3, 0])
        self.play(FadeIn(q, shift=UP * 0.05), run_time=0.9)
        self.wait(0.8)

        wrong = txt("(−3)² = 9", size=27, color=DIM).move_to([-3.2, 1.15, 0])
        self.play(FadeIn(wrong, shift=UP * 0.04), run_time=0.8)
        w2 = txt("√9 = 3", size=28, color=GREEN).move_to([-3.2, 0.35, 0])
        self.play(FadeIn(w2, shift=UP * 0.04), run_time=0.8)
        self.wait(1.0)

        b1 = txt("也可以写成 |−3| = 3", size=26, color=GOLD).move_to([3.2, 0.75, 0])
        self.play(FadeIn(b1, shift=UP * 0.04), run_time=0.9)
        self.wait(1.2)

        bad = txt("−3", size=30, color=RED).move_to([-3.2, -0.75, 0])
        self.play(FadeIn(bad, shift=UP * 0.04), run_time=0.6)
        self.play(Create(Line([-3.85, -0.75, 0], [-2.55, -0.75, 0], color=RED, stroke_width=2.6)),
                  run_time=0.5)
        bl = txt("开方结果不可能为负", size=23, color=RED).move_to([-3.2, -1.4, 0])
        self.play(FadeIn(bl), run_time=0.7)
        self.wait(1.4)

        warn = txt("易错：√(a²) 当 a 是负数时要变号　·　加减不能直接合并根号　·　结果要最简",
                   size=23, color=RED)
        warn.move_to([0, -1.95, 0])
        self.play(FadeIn(warn, shift=UP * 0.04), run_time=1.0)
        self.wait(1.0)

        box = label_box("先化简，再合并", size=29, color=GOLD)
        box.move_to([0, -2.9, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.1)
        self.wait(3.6)
        self.finish_section()

    def construct(self):
        self.scene_intro()
        self.clear_stage()
        self.scene_def()
        self.clear_stage()
        self.scene_prop()
        self.clear_stage()
        self.scene_muldiv()
        self.clear_stage()
        self.scene_simplify()
        self.clear_stage()
        self.scene_add()
        self.clear_stage()
        self.scene_example()
        self.clear_stage(0.8)