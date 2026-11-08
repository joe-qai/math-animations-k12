# -*- coding: utf-8 -*-
"""初升高衔接 1：因式分解强化。一提二套三检查、十字相乘、分组分解、拆项添项。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


def P(x, y):
    return np.array([float(x), float(y), 0.0])


class H0YinshiFenjieScene(NarratedScene):
    lesson = "h0-yinshi-fenjie"

    def clear_stage(self, run_time: float = 0.5):
        keep = {id(self._track), id(self._fill)}
        junk = [m for m in self.mobjects if id(m) not in keep]
        if junk:
            self.play(*[FadeOut(m) for m in junk], run_time=run_time)
        self.cur_title = None
        self.cur_sub = None

    # ---------------- 0. 高中的第一道坎 ---------------- 26.3
    def scene_intro(self):
        self.section(0, "因式分解：高中的第一道坎")

        chips = [(-4.75, "提公因式", GOLD), (-1.58, "公式法", GREEN),
                 (1.58, "十字相乘", BLUE), (4.75, "分组分解", ORANGE)]
        for cx, name, col in chips:
            c = label_box(name, size=20, color=col).move_to([cx, 1.75, 0])
            if c.width > 3.0:
                c.scale_to_fit_width(3.0)
            self.play(FadeIn(c, shift=UP * 0.04), run_time=0.65)
        self.wait(0.5)

        rows = [
            ("初中只会两招，高中式子立刻变复杂", CHALK),
            ("十字相乘是使用频率最高的一招", GOLD),
            ("分解不彻底，后面每一步都会卡住", RED),
        ]
        y = 0.7
        for s, col in rows:
            t = txt(s, size=24, color=col).move_to([0, y, 0])
            self.play(FadeIn(t, shift=UP * 0.04), run_time=0.8)
            y -= 0.78
        self.wait(0.5)

        box = label_box("提、套、查：三步走完", size=23, color=GOLD)
        box.move_to([0, -2.4, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.0)
        self.wait(9.0)
        self.finish_section()

    # ---------------- 1. 一提二套三检查 ---------------- 31.2
    def scene_basic(self):
        self.section(1, "基本功：一提、二套、三检查")

        rows = [
            ("① 提公因式", "3x² − 6x = 3x(x − 2)", GOLD),
            ("② 平方差", "a² − b² = (a + b)(a − b)", GREEN),
            ("③ 完全平方", "a² ± 2ab + b² = (a ± b)²", BLUE),
            ("④ 检查", "每个因式都不能再分解", ORANGE),
        ]
        y = 1.95
        for tag, body, col in rows:
            t1 = txt(tag, size=22, color=col).move_to([-4.35, y, 0])
            self.play(FadeIn(t1, shift=RIGHT * 0.04), run_time=0.55)
            t2 = txt(body, size=24, color=CHALK).move_to([1.55, y, 0])
            if t2.width > 8.2:
                t2.scale_to_fit_width(8.2)
            self.play(FadeIn(t2, shift=RIGHT * 0.04), run_time=0.6)
            y -= 1.0
        self.wait(0.5)

        tip = txt("顺序不能乱：先提公因式，再套公式", size=22, color=RED)
        tip.move_to([0, -2.35, 0])
        self.play(FadeIn(tip, shift=UP * 0.04), run_time=0.9)
        self.wait(12.0)
        self.finish_section()

    # ---------------- 2. 十字相乘（a = 1） ---------------- 28.9
    def scene_cross1(self):
        self.section(2, "十字相乘：二次项系数为 1")

        q = txt("x² − 5x + 6", size=32, color=GOLD).move_to([-4.4, 2.05, 0])
        self.play(FadeIn(q, shift=UP * 0.04), run_time=0.8)

        # 十字图：x、−2 / x、−3
        t_l, t_r = (-5.35, 0.95), (-4.2, 0.95)
        b_l, b_r = (-5.35, -0.35), (-4.2, -0.35)
        self.play(FadeIn(txt("x", size=28, color=CHALK).move_to([t_l[0], t_l[1], 0])),
                  FadeIn(txt("−2", size=28, color=ORANGE).move_to([t_r[0], t_r[1], 0])),
                  run_time=0.6)
        self.play(FadeIn(txt("x", size=28, color=CHALK).move_to([b_l[0], b_l[1], 0])),
                  FadeIn(txt("−3", size=28, color=BLUE).move_to([b_r[0], b_r[1], 0])),
                  run_time=0.6)
        self.play(Create(Line(P(t_l[0], t_l[1] - 0.22), P(b_r[0], b_r[1] + 0.22),
                              color=DIM, stroke_width=1.8)), run_time=0.6)
        self.play(Create(Line(P(t_r[0], t_r[1] - 0.22), P(b_l[0], b_l[1] + 0.22),
                              color=DIM, stroke_width=1.8)), run_time=0.6)

        cross = txt("−3x  +  (−2x)  =  −5x", size=22, color=GREEN)
        cross.move_to([-4.4, -1.35, 0])
        self.play(FadeIn(cross, shift=UP * 0.04), run_time=0.8)
        self.wait(0.4)

        rows = [
            ("和 = −5，积 = 6", GOLD),
            ("从积出发枚举两数", CHALK),
            ("−2 与 −3 满足", GREEN),
            ("符号看一次项", CHALK),
        ]
        y = 2.0
        for s, col in rows:
            t = txt(s, size=22, color=col).move_to([3.2, y, 0])
            self.play(FadeIn(t, shift=RIGHT * 0.04), run_time=0.7)
            y -= 0.82
        self.wait(0.6)

        res = label_box("x² − 5x + 6 = (x − 2)(x − 3)", size=22, color=GOLD)
        res.move_to([3.2, -1.75, 0])
        if res.width > 6.3:
            res.scale_to_fit_width(6.3)
        self.play(FadeIn(res, scale=0.97), run_time=1.0)
        self.wait(9.0)
        self.finish_section()

    # ---------------- 3. 十字相乘（a ≠ 1） ---------------- 32.3
    def scene_cross2(self):
        self.section(3, "十字相乘：二次项系数不为 1")

        q = txt("2x² + 7x + 3", size=32, color=GOLD).move_to([-4.4, 2.05, 0])
        self.play(FadeIn(q, shift=UP * 0.04), run_time=0.8)

        t_l, t_r = (-5.6, 0.95), (-4.1, 0.95)
        b_l, b_r = (-5.6, -0.35), (-4.1, -0.35)
        self.play(FadeIn(txt("2x", size=28, color=CHALK).move_to([t_l[0], t_l[1], 0])),
                  FadeIn(txt("1", size=28, color=GREEN).move_to([t_r[0], t_r[1], 0])),
                  run_time=0.6)
        self.play(FadeIn(txt("x", size=28, color=CHALK).move_to([b_l[0], b_l[1], 0])),
                  FadeIn(txt("3", size=28, color=ORANGE).move_to([b_r[0], b_r[1], 0])),
                  run_time=0.6)
        self.play(Create(Line(P(t_l[0], t_l[1] - 0.22), P(b_r[0], b_r[1] + 0.22),
                              color=DIM, stroke_width=1.8)), run_time=0.6)
        self.play(Create(Line(P(t_r[0], t_r[1] - 0.22), P(b_l[0], b_l[1] + 0.22),
                              color=DIM, stroke_width=1.8)), run_time=0.6)

        cross = txt("2x·3 = 6x      x·1 = x", size=22, color=GREEN)
        cross.move_to([-4.4, -1.35, 0])
        self.play(FadeIn(cross, shift=UP * 0.04), run_time=0.8)
        sm = txt("6x + x = 7x ✓", size=23, color=GOLD).move_to([-4.4, -2.15, 0])
        self.play(FadeIn(sm, shift=UP * 0.04), run_time=0.8)
        self.wait(0.4)

        rows = [
            ("拆两头：2x² 拆成 2x 与 x", CHALK),
            ("常数 3 拆成 1 与 3", CHALK),
            ("交叉相乘之和 = 一次项系数", GREEN),
            ("不相等就换一种拆法", ORANGE),
        ]
        y = 2.0
        for s, col in rows:
            t = txt(s, size=21, color=col).move_to([3.25, y, 0])
            if t.width > 6.2:
                t.scale_to_fit_width(6.2)
            self.play(FadeIn(t, shift=RIGHT * 0.04), run_time=0.7)
            y -= 0.86
        self.wait(0.5)

        res = label_box("2x² + 7x + 3 = (2x + 1)(x + 3)", size=21, color=GOLD)
        res.move_to([3.25, -1.9, 0])
        if res.width > 6.3:
            res.scale_to_fit_width(6.3)
        self.play(FadeIn(res, scale=0.97), run_time=1.0)
        self.wait(9.5)
        self.finish_section()

    # ---------------- 4. 分组分解 ---------------- 24.5
    def scene_group(self):
        self.section(4, "四项式：分组分解")

        head = txt("ax + ay + bx + by", size=30, color=CHALK).move_to([-3.3, 2.05, 0])
        self.play(FadeIn(head, shift=UP * 0.04), run_time=0.8)

        g1 = txt("ax + ay", size=26, color=GOLD).move_to([-5.2, 0.95, 0])
        a1 = txt("= a(x + y)", size=24, color=GOLD).move_to([-2.9, 0.95, 0])
        self.play(FadeIn(g1), run_time=0.6)
        self.play(Create(Line(P(-4.35, 0.95), P(-3.75, 0.95), color=DIM, stroke_width=2.0)),
                  FadeIn(a1), run_time=0.8)

        g2 = txt("bx + by", size=26, color=ORANGE).move_to([-5.2, -0.1, 0])
        a2 = txt("= b(x + y)", size=24, color=ORANGE).move_to([-2.9, -0.1, 0])
        self.play(FadeIn(g2), run_time=0.6)
        self.play(Create(Line(P(-4.35, -0.1), P(-3.75, -0.1), color=DIM, stroke_width=2.0)),
                  FadeIn(a2), run_time=0.8)
        self.wait(0.4)

        fin = label_box("= (a + b)(x + y)", size=26, color=GREEN)
        fin.move_to([-3.3, -1.45, 0])
        self.play(FadeIn(fin, scale=0.97), run_time=1.0)

        rows = [
            ("两项一组，各提公因式", CHALK),
            ("出现公共括号就成功", GOLD),
            ("或把三项凑成完全平方", BLUE),
            ("分不通就换一种分法", ORANGE),
        ]
        y = 1.9
        for s, col in rows:
            t = txt(s, size=21, color=col).move_to([3.55, y, 0])
            if t.width > 6.1:
                t.scale_to_fit_width(6.1)
            self.play(FadeIn(t, shift=RIGHT * 0.04), run_time=0.7)
            y -= 0.86
        self.wait(0.5)

        tip = txt("目标：分完能继续提或用公式", size=21, color=RED).move_to([3.55, -1.95, 0])
        if tip.width > 6.1:
            tip.scale_to_fit_width(6.1)
        self.play(FadeIn(tip, shift=UP * 0.04), run_time=0.9)
        self.wait(5.5)
        self.finish_section()

    # ---------------- 5. 拆项添项与换元 ---------------- 30.7
    def scene_split(self):
        self.section(5, "拆项添项与换元")

        lines = [
            ("x⁴ + 4", CHALK, 26),
            ("= x⁴ + 4x² + 4 − 4x²", GOLD, 24),
            ("= (x² + 2)² − (2x)²", BLUE, 24),
            ("= (x² + 2x + 2)(x² − 2x + 2)", GREEN, 23),
        ]
        y = 2.1
        for s, col, size in lines:
            t = txt(s, size=size, color=col).move_to([-1.7, y, 0])
            self.play(FadeIn(t, shift=UP * 0.04), run_time=0.8)
            y -= 0.82
        self.wait(0.5)

        note1 = txt("先配方，再用平方差", size=21, color=ORANGE).move_to([-1.7, -1.55, 0])
        self.play(FadeIn(note1, shift=UP * 0.04), run_time=0.8)
        note2 = txt("换元：把 x² + x 记作 t，降次后再换回", size=21, color=CHALK)
        note2.move_to([0, -2.35, 0])
        if note2.width > 12.0:
            note2.scale_to_fit_width(12.0)
        self.play(FadeIn(note2, shift=UP * 0.04), run_time=0.9)
        self.wait(15.0)
        self.finish_section()

    # ---------------- 6. 四个易错点 ---------------- 21.7
    def scene_traps(self):
        self.section(6, "四个易错点")

        rows = [
            ("① 分解不彻底", "括号里还能继续分"),
            ("② 符号没提干净", "负号先整体提出"),
            ("③ 只试一种拆法", "交叉和不对就换"),
            ("④ 分解完不检验", "乘回去看是否等于原式"),
        ]
        y = 1.85
        for a, b in rows:
            ta = txt(a, size=22, color=RED).move_to([-2.65, y, 0])
            tb = txt(b, size=20, color=DIM).move_to([3.5, y, 0])
            self.play(FadeIn(ta, shift=RIGHT * 0.04), run_time=0.6)
            self.play(FadeIn(tb, shift=RIGHT * 0.04), run_time=0.6)
            y -= 0.86
        self.wait(0.8)

        box = label_box("分解完，乘回去验一遍", size=24, color=GOLD)
        box.move_to([0, -2.45, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.1)
        self.wait(5.5)
        self.finish_section()

    def construct(self):
        self.scene_intro()
        self.clear_stage()
        self.scene_basic()
        self.clear_stage()
        self.scene_cross1()
        self.clear_stage()
        self.scene_cross2()
        self.clear_stage()
        self.scene_group()
        self.clear_stage()
        self.scene_split()
        self.clear_stage()
        self.scene_traps()
        self.clear_stage(0.8)