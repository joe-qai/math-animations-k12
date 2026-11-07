# -*- coding: utf-8 -*-
"""中考专题 1：数与式。有理数运算、幂与整式、因式分解、二次根式、化简求值。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


def P(x, y):
    return np.array([float(x), float(y), 0.0])


class ZhongkaoShuYuShiScene(NarratedScene):
    lesson = "zhongkao-shu-yu-shi"

    def clear_stage(self, run_time: float = 0.5):
        keep = {id(self._track), id(self._fill)}
        junk = [m for m in self.mobjects if id(m) not in keep]
        if junk:
            self.play(*[FadeOut(m) for m in junk], run_time=run_time)
        self.cur_title = None
        self.cur_sub = None

    # ---------------- 0. 中考怎么考 ---------------- 27.4
    def scene_intro(self):
        self.section(0, "数与式：题不难，坑很多")

        items = [
            (-4.9, "有理数运算", GOLD),
            (-1.65, "科学记数法", GREEN),
            (1.65, "幂与整式", BLUE),
            (4.9, "因式与根式", ORANGE),
        ]
        for cx, name, col in items:
            chip = label_box(name, size=22, color=col)
            chip.move_to([cx, 1.6, 0])
            self.play(FadeIn(chip, shift=UP * 0.04), run_time=0.7)
        self.wait(0.6)

        rows = [
            ("以选择、填空为主，很少出大题", CHALK),
            ("考的是熟练度和细心，不是难度", CHALK),
            ("符号、分母、根号里的条件最容易扣分", RED),
        ]
        y = 0.45
        for s, col in rows:
            t = txt(s, size=24, color=col).move_to([0, y, 0])
            self.play(FadeIn(t, shift=UP * 0.04), run_time=0.85)
            y -= 0.72
        self.wait(0.6)

        box = label_box("今天把这几个坑一次讲清", size=23, color=GOLD)
        box.move_to([0, -2.35, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.0)
        self.wait(16.0)
        self.finish_section()

    # ---------------- 1. 有理数运算 ---------------- 28.0
    def scene_rational(self):
        self.section(1, "有理数运算：三条铁律")

        rows = [
            ("① 先定符号，再算绝对值", GOLD),
            ("② 同级从左到右，先乘方再乘除后加减", GOLD),
            ("③ 减去一个数 = 加上它的相反数", GOLD),
        ]
        y = 2.05
        for s, col in rows:
            t = txt(s, size=23, color=col).move_to([0, y, 0])
            self.play(FadeIn(t, shift=UP * 0.04), run_time=0.8)
            y -= 0.75
        self.wait(0.6)

        cases = [
            ("(−2)² = 4", "负数的偶次方为正", GREEN),
            ("−2² = −4", "负号在乘方外面", RED),
            ("−3 − (−5) = 2", "减负等于加正", BLUE),
            ("|−3| = 3", "绝对值是到原点的距离", ORANGE),
        ]
        y = 0.1
        for a, b, col in cases:
            ta = txt(a, size=25, color=col).move_to([-3.6, y, 0])
            tb = txt(b, size=21, color=DIM).move_to([3.2, y, 0])
            self.play(FadeIn(ta, shift=RIGHT * 0.04), run_time=0.7)
            self.play(FadeIn(tb, shift=RIGHT * 0.04), run_time=0.6)
            y -= 0.72
        self.wait(0.6)

        box = label_box("绝对值永远非负，去绝对值先看正负", size=22, color=RED)
        box.move_to([0, -2.55, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.0)
        self.wait(13.0)
        self.finish_section()

    # ---------------- 2. 幂与整式 ---------------- 28.8
    def scene_power(self):
        self.section(2, "幂的运算与乘法公式")

        rows = [
            ("同底数幂相乘：aᵐ · aⁿ = aᵐ⁺ⁿ", CHALK),
            ("幂的乘方：(aᵐ)ⁿ = aᵐⁿ", CHALK),
            ("积的乘方：(ab)ⁿ = aⁿbⁿ", CHALK),
            ("同底数幂相除：aᵐ ÷ aⁿ = aᵐ⁻ⁿ", CHALK),
        ]
        y = 1.95
        for s, col in rows:
            t = txt(s, size=24, color=col).move_to([0, y, 0])
            self.play(FadeIn(t, shift=UP * 0.04), run_time=0.75)
            y -= 0.7
        self.wait(0.6)

        f1 = txt("平方差：(a + b)(a − b) = a² − b²", size=26, color=GOLD)
        f1.move_to([0, -0.95, 0])
        self.play(FadeIn(f1, shift=UP * 0.04), run_time=0.9)
        f2 = txt("完全平方：(a ± b)² = a² ± 2ab + b²", size=26, color=GOLD)
        f2.move_to([0, -1.6, 0])
        self.play(FadeIn(f2, shift=UP * 0.04), run_time=0.9)
        self.wait(0.6)

        box = label_box("完全平方的中间项 2ab，最容易漏", size=22, color=RED)
        box.move_to([0, -2.5, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.0)
        self.wait(13.0)
        self.finish_section()

    # ---------------- 3. 因式分解 ---------------- 24.4
    def scene_factor(self):
        self.section(3, "因式分解：一提二套三检查")

        steps = [
            (1.9, "一 提：先提公因式", GOLD),
            (1.15, "二 套：平方差、完全平方", GOLD),
            (0.4, "三 查：每个因式能否再分", GOLD),
        ]
        for y, s, col in steps:
            t = txt(s, size=24, color=col).move_to([0, y, 0])
            self.play(FadeIn(t, shift=UP * 0.04), run_time=0.8)
        self.wait(0.5)

        e1 = txt("x³ − 4x = x(x² − 4)", size=27, color=CHALK).move_to([0, -0.55, 0])
        self.play(FadeIn(e1, shift=UP * 0.04), run_time=0.8)
        e2 = txt("= x(x + 2)(x − 2)", size=27, color=GREEN).move_to([0, -1.2, 0])
        self.play(FadeIn(e2, shift=UP * 0.04), run_time=0.8)
        e3 = txt("x² + 5x + 6 = (x + 2)(x + 3)", size=25, color=BLUE)
        e3.move_to([0, -1.9, 0])
        self.play(FadeIn(e3, shift=UP * 0.04), run_time=0.8)
        self.wait(0.5)

        box = label_box("分解到不能再分，才是最后答案", size=22, color=RED)
        box.move_to([0, -2.65, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.0)
        self.wait(9.0)
        self.finish_section()

    # ---------------- 4. 二次根式 ---------------- 24.7
    def scene_sqrt(self):
        self.section(4, "二次根式：两个硬条件")

        rows = [
            ("被开方数必须非负", GOLD),
            ("结果必须是最简形式", GOLD),
            ("能开得尽方的因数要移到根号外", CHALK),
        ]
        y = 2.0
        for s, col in rows:
            t = txt(s, size=24, color=col).move_to([0, y, 0])
            self.play(FadeIn(t, shift=UP * 0.04), run_time=0.8)
            y -= 0.72
        self.wait(0.6)

        cases = [
            ("√8 = 2√2", "化简"),
            ("1 / √2 = √2 / 2", "分母有理化"),
            ("2 < √5 < 3", "夹逼估算"),
        ]
        y = -0.25
        for a, b in cases:
            ta = txt(a, size=28, color=GREEN).move_to([-3.7, y, 0])
            tb = txt(b, size=21, color=DIM).move_to([2.9, y, 0])
            self.play(FadeIn(ta, shift=RIGHT * 0.04), run_time=0.75)
            self.play(FadeIn(tb, shift=RIGHT * 0.04), run_time=0.6)
            y -= 0.78
        self.wait(0.6)

        box = label_box("分母有两项，用平方差有理化", size=22, color=RED)
        box.move_to([0, -2.6, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.0)
        self.wait(9.5)
        self.finish_section()

    # ---------------- 5. 例题：化简求值 ---------------- 20.6
    def scene_example(self):
        self.section(5, "例：先化简，再求值")

        q = txt("化简  (x² − 4)/(x² − 4x + 4) ÷ (x + 2)/(x − 2)", size=25, color=CHALK)
        q.move_to([0, 1.75, 0])
        self.play(FadeIn(q, shift=UP * 0.04), run_time=0.9)
        self.wait(0.5)

        steps = [
            ("= (x − 2)(x + 2)/(x − 2)² · (x − 2)/(x + 2)", CHALK),
            ("= 1", GOLD),
            ("条件：x ≠ 2 且 x ≠ −2", RED),
        ]
        y = 0.65
        for s, col in steps:
            t = txt(s, size=25, color=col).move_to([0, y, 0])
            self.play(FadeIn(t, shift=UP * 0.04), run_time=0.85)
            y -= 0.85
        self.wait(0.6)

        box = label_box("先化到最简，最后才代值", size=23, color=GREEN)
        box.move_to([0, -2.35, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.0)
        self.wait(6.5)
        self.finish_section()

    # ---------------- 6. 易错点 ---------------- 23.3
    def scene_traps(self):
        self.section(6, "四个易错点")

        rows = [
            ("① 负号与乘方", "(−2)² = 4，−2² = −4"),
            ("② 科学记数法", "小数点位置别数错"),
            ("③ 分解不彻底", "提完还要再套公式"),
            ("④ 化简丢条件", "分母不为零、根号非负"),
        ]
        y = 1.85
        for a, b in rows:
            ta = txt(a, size=23, color=RED).move_to([-2.7, y, 0])
            tb = txt(b, size=21, color=DIM).move_to([3.5, y, 0])
            self.play(FadeIn(ta, shift=RIGHT * 0.04), run_time=0.65)
            self.play(FadeIn(tb, shift=RIGHT * 0.04), run_time=0.65)
            y -= 0.86
        self.wait(1.0)

        box = label_box("先定符号，再动笔", size=27, color=GOLD)
        box.move_to([0, -2.45, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.1)
        self.wait(9.0)
        self.finish_section()

    def construct(self):
        self.scene_intro()
        self.clear_stage()
        self.scene_rational()
        self.clear_stage()
        self.scene_power()
        self.clear_stage()
        self.scene_factor()
        self.clear_stage()
        self.scene_sqrt()
        self.clear_stage()
        self.scene_example()
        self.clear_stage()
        self.scene_traps()
        self.clear_stage(0.8)