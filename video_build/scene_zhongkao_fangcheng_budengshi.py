# -*- coding: utf-8 -*-
"""中考专题 2：方程与不等式。一次方程、方程组、分式方程、一元二次方程、不等式（组）、建模。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


def P(x, y):
    return np.array([float(x), float(y), 0.0])


class ZhongkaoFangchengBudengshiScene(NarratedScene):
    lesson = "zhongkao-fangcheng-budengshi"

    def clear_stage(self, run_time: float = 0.5):
        keep = {id(self._track), id(self._fill)}
        junk = [m for m in self.mobjects if id(m) not in keep]
        if junk:
            self.play(*[FadeOut(m) for m in junk], run_time=run_time)
        self.cur_title = None
        self.cur_sub = None

    def axis(self, cx, cy, half=3.0, color=DIM):
        return Line(P(cx - half, cy), P(cx + half, cy), color=color, stroke_width=2.2)

    # ---------------- 0. 中考怎么考 ---------------- 22.9
    def scene_intro(self):
        self.section(0, "方程与不等式：三条线")

        chips = [
            (-4.9, "一元一次方程", GOLD),
            (-1.65, "二元一次组", GREEN),
            (1.65, "一元二次方程", BLUE),
            (4.9, "不等式（组）", ORANGE),
        ]
        for cx, name, col in chips:
            chip = label_box(name, size=21, color=col)
            chip.move_to([cx, 1.65, 0])
            self.play(FadeIn(chip, shift=UP * 0.04), run_time=0.7)
        self.wait(0.5)

        rows = [
            ("选择填空直接考解法，稳拿基础分", CHALK),
            ("应用题、函数题里当工具，躲不开", CHALK),
            ("分值大约 10 到 15 分", GOLD),
        ]
        y = 0.55
        for s, col in rows:
            t = txt(s, size=24, color=col).move_to([0, y, 0])
            self.play(FadeIn(t, shift=UP * 0.04), run_time=0.85)
            y -= 0.72
        self.wait(0.5)

        box = label_box("怎么解 · 何时不成立 · 怎么建模", size=23, color=GOLD)
        box.move_to([0, -2.4, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.0)
        self.wait(8.0)
        self.finish_section()

    # ---------------- 1. 一次方程与方程组 ---------------- 27.4
    def scene_linear(self):
        self.section(1, "一次方程与方程组：五步与消元")

        steps = txt("① 去分母  ② 去括号  ③ 移项  ④ 合并  ⑤ 系数化为一", size=23, color=GOLD)
        steps.move_to([0, 2.15, 0])
        self.play(FadeIn(steps, shift=UP * 0.04), run_time=0.9)
        self.wait(0.5)

        left = [
            ("3(x − 1) = 2x + 4", CHALK),
            ("3x − 3 = 2x + 4", CHALK),
            ("x = 7", GREEN),
        ]
        y = 0.95
        for s, col in left:
            t = txt(s, size=27, color=col).move_to([-3.3, y, 0])
            self.play(FadeIn(t, shift=UP * 0.04), run_time=0.7)
            y -= 0.8
        self.wait(0.4)

        tag = txt("逐项去括号，别漏乘", size=20, color=DIM).move_to([-3.3, -1.55, 0])
        self.play(FadeIn(tag), run_time=0.6)
        self.wait(0.4)

        right = [
            ("x + y = 5", BLUE),
            ("2x − y = 1", BLUE),
            ("x = 2，y = 3", GREEN),
        ]
        y = 0.95
        for s, col in right:
            t = txt(s, size=27, color=col).move_to([3.3, y, 0])
            self.play(FadeIn(t, shift=UP * 0.04), run_time=0.7)
            y -= 0.8
        self.wait(0.4)

        tag2 = txt("系数相反，两式相加消元", size=20, color=DIM).move_to([3.3, -1.55, 0])
        self.play(FadeIn(tag2), run_time=0.6)
        self.wait(0.5)

        box = label_box("消元：两个未知数，化成一个", size=22, color=RED)
        box.move_to([0, -2.6, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.0)
        self.wait(10.0)
        self.finish_section()

    # ---------------- 2. 分式方程 ---------------- 25.2
    def scene_fraction(self):
        self.section(2, "分式方程：解完必须验根")

        q = txt("1/(x − 2) + 3 = (x − 1)/(x − 2)", size=28, color=CHALK)
        q.move_to([0, 2.0, 0])
        self.play(FadeIn(q, shift=UP * 0.04), run_time=0.9)
        self.wait(0.5)

        rows = [
            ("去分母，两边同乘 x − 2", DIM),
            ("1 + 3(x − 2) = x − 1", CHALK),
            ("3x − 5 = x − 1  →  x = 2", CHALK),
        ]
        y = 1.15
        for s, col in rows:
            t = txt(s, size=25, color=col).move_to([0, y, 0])
            self.play(FadeIn(t, shift=UP * 0.04), run_time=0.75)
            y -= 0.72
        self.wait(0.5)

        bad = txt("把 x = 2 代回最简公分母：x − 2 = 0", size=24, color=RED)
        bad.move_to([0, -1.05, 0])
        self.play(FadeIn(bad, shift=UP * 0.04), run_time=0.85)
        self.wait(0.4)

        res = txt("x = 2 是增根，原方程无解", size=27, color=GOLD).move_to([0, -1.8, 0])
        self.play(FadeIn(res, shift=UP * 0.04), run_time=0.9)
        self.wait(0.5)

        box = label_box("增根要舍去，无解也是答案", size=22, color=RED)
        box.move_to([0, -2.62, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.0)
        self.wait(8.0)
        self.finish_section()

    # ---------------- 3. 一元二次方程 ---------------- 28.8
    def scene_quadratic(self):
        self.section(3, "一元二次方程：解法与判别式")

        f = txt("x = (−b ± √(b² − 4ac)) / 2a", size=30, color=GOLD).move_to([0, 2.05, 0])
        self.play(FadeIn(f, shift=UP * 0.04), run_time=0.9)
        self.wait(0.4)

        cases = [
            ("Δ > 0：两个不等实根", GREEN),
            ("Δ = 0：两个相等实根", ORANGE),
            ("Δ < 0：没有实根", RED),
        ]
        y = 1.1
        for s, col in cases:
            t = txt(s, size=24, color=col).move_to([0, y, 0])
            self.play(FadeIn(t, shift=RIGHT * 0.04), run_time=0.7)
            y -= 0.7
        self.wait(0.4)

        ex = txt("x² − 3x + 2 = 0", size=27, color=CHALK).move_to([0, -1.05, 0])
        self.play(FadeIn(ex, shift=UP * 0.04), run_time=0.7)
        ex2 = txt("(x − 1)(x − 2) = 0  →  x = 1 或 x = 2", size=25, color=GREEN)
        ex2.move_to([0, -1.75, 0])
        self.play(FadeIn(ex2, shift=UP * 0.04), run_time=0.8)
        self.wait(0.4)

        box = label_box("能分解就先分解，最快", size=22, color=GOLD)
        box.move_to([0, -2.65, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.0)
        self.wait(9.0)
        self.finish_section()

    # ---------------- 4. 不等式（组） ---------------- 23.3
    def scene_inequality(self):
        self.section(4, "不等式（组）：变号与取交集")

        rows = [
            ("① 两边乘除负数，不等号变向", GOLD),
            ("② 数轴上：空心不含，实心含", GOLD),
            ("③ 同大取大，同小取小，大小小大中间找", GOLD),
        ]
        y = 2.3
        for s, col in rows:
            t = txt(s, size=22, color=col)
            if t.width > 12.2:
                t.scale_to_fit_width(12.2)
            t.move_to([0, y, 0])
            self.play(FadeIn(t, shift=UP * 0.04), run_time=0.8)
            y -= 0.64
        self.wait(0.4)

        e = txt("−2x + 1 > 5  →  −2x > 4  →  x < −2", size=26, color=GREEN)
        e.move_to([0, 0.3, 0])
        self.play(FadeIn(e, shift=UP * 0.04), run_time=0.8)
        self.wait(0.4)

        # 数轴
        ax = self.axis(-4.0, -1.0, 2.0)
        self.play(Create(ax), run_time=0.7)
        hole = Circle(radius=0.09, color=RED, stroke_width=2.4, fill_opacity=0).move_to([-4.6, -1.0, 0])
        left_ray = Line(P(-4.6, -1.0), P(-5.85, -1.0), color=GOLD, stroke_width=4.0)
        self.play(FadeIn(hole), Create(left_ray), run_time=0.7)
        self.play(FadeIn(txt("−2", size=20, color=RED).move_to([-4.6, -1.5, 0])),
                  run_time=0.5)
        self.wait(0.4)

        e2 = txt("x > 1 且 x ≤ 3  →  1 < x ≤ 3", size=24, color=BLUE)
        e2.move_to([3.6, -0.35, 0])
        self.play(FadeIn(e2, shift=UP * 0.04), run_time=0.8)
        self.wait(0.3)

        ax2 = self.axis(3.6, -1.3, 1.9)
        self.play(Create(ax2), run_time=0.6)
        h1 = Circle(radius=0.08, color=BLUE, stroke_width=2.2, fill_opacity=0).move_to([2.6, -1.3, 0])
        d2 = Dot([4.6, -1.3, 0], radius=0.08, color=BLUE)
        seg = Line(P(2.6, -1.3), P(4.6, -1.3), color=BLUE, stroke_width=4.2)
        self.play(FadeIn(h1), FadeIn(d2), Create(seg), run_time=0.7)
        self.play(FadeIn(txt("1", size=18, color=BLUE).move_to([2.6, -1.8, 0])),
                  FadeIn(txt("3", size=18, color=BLUE).move_to([4.6, -1.8, 0])),
                  run_time=0.5)
        self.wait(0.5)

        box = label_box("乘除负数不变号，是最大的失分点", size=21, color=RED)
        box.move_to([0, -2.65, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.0)
        self.wait(6.5)
        self.finish_section()

    # ---------------- 5. 应用题建模 ---------------- 27.2
    def scene_apply(self):
        self.section(5, "应用题：设、找、列、验")

        four = txt("设未知数 · 找关系 · 列式 · 检验", size=25, color=GOLD)
        four.move_to([0, 2.2, 0])
        self.play(FadeIn(four, shift=UP * 0.04), run_time=0.85)
        self.wait(0.4)

        chips = [(-4.6, "行程", GOLD), (-1.55, "工程", GREEN),
                 (1.55, "销售利润", BLUE), (4.6, "方案选择", ORANGE)]
        for cx, name, col in chips:
            c = label_box(name, size=21, color=col).move_to([cx, 1.2, 0])
            self.play(FadeIn(c, shift=UP * 0.04), run_time=0.55)
        self.wait(0.4)

        q = txt("进价 40 元，标价 60 元，利润率不低于 20%", size=24, color=CHALK)
        q.move_to([0, 0.1, 0])
        self.play(FadeIn(q, shift=UP * 0.04), run_time=0.8)
        self.wait(0.3)

        rows = [
            ("设打 k 折：60k − 40 ≥ 40 × 20%", CHALK),
            ("60k ≥ 48  →  k ≥ 0.8", CHALK),
            ("至少打八折", GREEN),
        ]
        y = -0.55
        for s, col in rows:
            t = txt(s, size=25, color=col).move_to([0, y, 0])
            self.play(FadeIn(t, shift=UP * 0.04), run_time=0.7)
            y -= 0.68
        self.wait(0.5)

        note = txt("设未知数带单位，解完看是否符合实际", size=21, color=DIM)
        note.move_to([0, -2.6, 0])
        self.play(FadeIn(note, shift=UP * 0.04), run_time=0.9)
        self.wait(9.5)
        self.finish_section()

    # ---------------- 6. 易错点 ---------------- 17.5
    def scene_traps(self):
        self.section(6, "四个易错点")

        rows = [
            ("① 去分母漏乘", "不含分母的项也要乘"),
            ("② 移项不变号", "过等号要变相反数"),
            ("③ 乘除负数", "不等号必须变向"),
            ("④ 分式方程不验根", "增根要舍去"),
        ]
        y = 1.85
        for a, b in rows:
            ta = txt(a, size=23, color=RED).move_to([-2.7, y, 0])
            tb = txt(b, size=21, color=DIM).move_to([3.5, y, 0])
            self.play(FadeIn(ta, shift=RIGHT * 0.04), run_time=0.6)
            self.play(FadeIn(tb, shift=RIGHT * 0.04), run_time=0.6)
            y -= 0.86
        self.wait(0.8)

        box = label_box("解完先验，再写答案", size=27, color=GOLD)
        box.move_to([0, -2.45, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.1)
        self.wait(4.0)
        self.finish_section()

    def construct(self):
        self.scene_intro()
        self.clear_stage()
        self.scene_linear()
        self.clear_stage()
        self.scene_fraction()
        self.clear_stage()
        self.scene_quadratic()
        self.clear_stage()
        self.scene_inequality()
        self.clear_stage()
        self.scene_apply()
        self.clear_stage()
        self.scene_traps()
        self.clear_stage(0.8)