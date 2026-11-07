# -*- coding: utf-8 -*-
"""小数乘法：小数乘整数、小数乘小数、补零与去零、估算验算。四年级下册。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


def step_row(n: str, s: str, color: str = CHALK, size: int = 32,
             x: float = -1.2, y: float = 0.0) -> VGroup:
    """带序号的推导行，文字左对齐。"""
    c = Circle(radius=0.22, color=color, stroke_width=1.8).move_to([x - 2.4, y, 0])
    num = txt(n, size=20, color=color).move_to([x - 2.4, y, 0])
    body = txt(s, size=size, color=color)
    body.next_to(c, RIGHT, buff=0.5, aligned_edge=LEFT)
    return VGroup(c, num, body)


class XiaoshuChengScene(NarratedScene):
    lesson = "xiaoshu-cheng"

    def clear_stage(self, run_time: float = 0.5):
        keep = {id(self._track), id(self._fill)}
        junk = [m for m in self.mobjects if id(m) not in keep]
        if junk:
            self.play(*[FadeOut(m) for m in junk], run_time=run_time)
        self.cur_title = None
        self.cur_sub = None

    # ---------------- 0. 买笔、买苹果 ---------------- 14.5
    def scene_story(self):
        self.section(0, "一支笔 2.5 元，买 3 支")

        # 左：三支笔
        pencils = VGroup()
        for i in range(3):
            x = -5.3 + i * 0.85
            body = Rectangle(width=0.28, height=1.9, color=GOLD, stroke_width=1.8,
                             fill_color=GOLD, fill_opacity=0.25).move_to([0, 0.15, 0])
            tip = Triangle(color=GOLD, stroke_width=1.6,
                           fill_color=GOLD, fill_opacity=0.25).scale(0.15)
            tip.rotate(PI).move_to([0, -0.95, 0])
            pencil = VGroup(body, tip).rotate(14 * DEGREES).move_to([x, 0.95, 0])
            pencils.add(pencil)
        self.play(LaggedStart(*[FadeIn(p) for p in pencils], lag_ratio=0.15), run_time=1.4)

        p1 = txt("2.5 元 / 支", size=27, color=GOLD).move_to([-4.5, -1.0, 0])
        q1 = txt("3 支 = ?", size=34, color=CHALK).move_to([-4.5, -1.75, 0])
        self.play(FadeIn(p1, shift=UP * 0.05), run_time=0.6)
        self.play(FadeIn(q1, shift=UP * 0.06), run_time=0.7)

        # 右：一袋苹果
        bag = Circle(radius=1.0, color=RED, stroke_width=2.4,
                     fill_color=RED, fill_opacity=0.18)
        bag.move_to([3.1, 0.95, 0])
        stem = Line([3.1, 1.95, 0], [3.1, 2.15, 0], color=GREEN, stroke_width=3)
        leaf = Ellipse(width=0.5, height=0.24, color=GREEN, stroke_width=1.8,
                       fill_color=GREEN, fill_opacity=0.4).move_to([3.35, 2.05, 0])
        self.play(Create(bag), run_time=0.9)
        self.play(Create(stem), FadeIn(leaf), run_time=0.6)

        p2 = txt("6 元 / 千克", size=27, color=RED).move_to([3.1, -0.55, 0])
        q2 = txt("买 0.8 千克 = ?", size=32, color=CHALK).move_to([3.1, -1.35, 0])
        self.play(FadeIn(p2, shift=UP * 0.05), run_time=0.6)
        self.play(FadeIn(q2, shift=UP * 0.06), run_time=0.7)

        note = txt("价钱里有小数，就要用小数乘法", size=28, color=GREEN)
        note.move_to([0, -2.45, 0])
        self.play(FadeIn(note, shift=UP * 0.08), run_time=0.8)
        self.finish_section()

    # ---------------- 1. 小数乘整数 ---------------- 16.2
    def scene_int(self):
        self.section(1, "先按整数乘，再点小数点")

        big = txt("2.5 × 3", size=52, color=GOLD).move_to([0, 2.35, 0])
        self.play(FadeIn(big, shift=UP * 0.06), run_time=0.8)

        r1 = step_row("1", "2.5 看成 25", CHALK, 30, y=1.25)
        r2 = step_row("2", "25 × 3 = 75", CHALK, 30, y=0.35)
        r3 = step_row("3", "75 ÷ 10 = 7.5", GOLD, 30, y=-0.55)
        self.play(FadeIn(r1, shift=RIGHT * 0.06), run_time=0.7)
        self.play(FadeIn(r2, shift=RIGHT * 0.06), run_time=0.7)
        self.play(FadeIn(r3, shift=RIGHT * 0.06), run_time=0.8)

        rule = txt("因数有 1 位小数 → 积也点 1 位小数", size=27, color=BLUE)
        rule.move_to([0, -1.55, 0])
        ans = txt("2.5 × 3 = 7.5（元）", size=32, color=GREEN).move_to([0, -2.35, 0])
        self.play(FadeIn(rule, shift=UP * 0.06), run_time=0.8)
        self.play(FadeIn(ans, shift=UP * 0.06), run_time=0.7)
        self.finish_section()

    # ---------------- 2. 小数乘小数 ---------------- 13.4
    def scene_dec(self):
        self.section(2, "小数乘小数：两位小数怎么点")

        big = txt("2.4 × 1.3", size=52, color=GOLD).move_to([0, 2.35, 0])
        self.play(FadeIn(big, shift=UP * 0.06), run_time=0.8)

        r1 = step_row("1", "24 × 13 = 312", CHALK, 30, y=1.25)
        r2 = step_row("2", "1 位 + 1 位 = 2 位小数", BLUE, 30, y=0.35)
        r3 = step_row("3", "312 → 3.12", GOLD, 30, y=-0.55)
        self.play(FadeIn(r1, shift=RIGHT * 0.06), run_time=0.7)
        self.play(FadeIn(r2, shift=RIGHT * 0.06), run_time=0.7)
        self.play(FadeIn(r3, shift=RIGHT * 0.06), run_time=0.8)

        # 从右往左数两位
        ans = txt("2.4 × 1.3 = 3.12", size=32, color=GREEN).move_to([0, -1.55, 0])
        tip = txt("两个因数的小数位数相加，就是积的小数位数", size=25, color=DIM)
        tip.move_to([0, -2.3, 0])
        self.play(FadeIn(ans, shift=UP * 0.06), run_time=0.8)
        self.play(FadeIn(tip, shift=UP * 0.05), run_time=0.7)
        self.finish_section()

    # ---------------- 3. 位数不够要补零 ---------------- 13.1
    def scene_zero(self):
        self.section(3, "位数不够，前面补零")

        big = txt("0.02 × 0.3", size=50, color=GOLD).move_to([0, 2.35, 0])
        self.play(FadeIn(big), run_time=0.8)

        r1 = step_row("1", "2 × 3 = 6", CHALK, 30, y=1.3)
        r2 = step_row("2", "2 位 + 1 位 = 3 位小数", BLUE, 30, y=0.4)
        self.play(FadeIn(r1, shift=RIGHT * 0.06), run_time=0.7)
        self.play(FadeIn(r2, shift=RIGHT * 0.06), run_time=0.7)

        zeros = VGroup(
            txt("0.", size=72, color=CHALK),
            txt("00", size=72, color=GOLD),
            txt("6", size=72, color=CHALK),
        ).arrange(RIGHT, buff=0.03).move_to([-0.4, -0.85, 0])
        z1 = txt("这两个 0 是补出来的", size=24, color=GOLD).move_to([2.25, -1.75, 0])
        arrow = Arrow([1.35, -1.6, 0], [-0.1, -1.2, 0], color=GOLD,
                      stroke_width=2.2, buff=0.06,
                      max_tip_length_to_length_ratio=0.22)
        self.play(Write(zeros), run_time=1.1)
        self.play(FadeIn(z1), GrowArrow(arrow), run_time=0.8)

        tip = txt("小数位数不够，就用 0 占位，不能空着", size=26, color=DIM)
        tip.move_to([0, -2.35, 0])
        self.play(FadeIn(tip, shift=UP * 0.06), run_time=0.7)
        self.finish_section()

    # ---------------- 4. 末尾的 0 与中间的 0 ---------------- 11.5
    def scene_tail(self):
        self.section(4, "末尾的 0 能去，中间的不能去")

        a = VGroup(
            txt("0.5 × 0.4 = 0.", size=40, color=CHALK),
            txt("2", size=40, color=GREEN),
            txt("0", size=40, color=CHALK),
        ).arrange(RIGHT, buff=0.02).move_to([-0.8, 1.55, 0])
        self.play(FadeIn(a), run_time=0.8)

        last0 = a[2]
        cross = Line(last0.get_corner(DL) + [-0.04, -0.04, 0],
                     last0.get_corner(UR) + [0.04, 0.1, 0],
                     color=RED, stroke_width=3)
        a2 = txt("= 0.2", size=40, color=GREEN).move_to([1.35, 1.55, 0])
        self.play(Create(cross), run_time=0.6)
        self.play(FadeIn(a2, shift=RIGHT * 0.08), run_time=0.7)

        b = VGroup(
            txt("1.02 × 3 = 3.", size=40, color=CHALK),
            txt("0", size=40, color=GOLD),
            txt("6", size=40, color=CHALK),
        ).arrange(RIGHT, buff=0.02).move_to([-0.6, -0.2, 0])
        self.play(FadeIn(b), run_time=0.8)

        hl = SurroundingRectangle(b[1], color=GOLD, stroke_width=2.4, buff=0.14)
        self.play(Create(hl), run_time=0.7)
        b2 = txt("中间的 0 必须保留", size=26, color=GOLD).move_to([0, -1.1, 0])
        self.play(FadeIn(b2, shift=UP * 0.06), run_time=0.7)

        tip = txt("去掉末尾的 0，小数的大小不变", size=27, color=GREEN)
        tip.move_to([0, -2.1, 0])
        self.play(FadeIn(tip, shift=UP * 0.06), run_time=0.8)
        self.finish_section()

    # ---------------- 5. 估算验算 ---------------- 11.8
    def scene_est(self):
        self.section(5, "先估算，再检查小数点")

        q = txt("2.9 × 4.1", size=46, color=GOLD).move_to([-3.6, 1.6, 0])
        est = txt("≈ 3 × 4 = 12", size=34, color=BLUE).move_to([2.9, 1.6, 0])
        self.play(FadeIn(q), run_time=0.8)
        self.play(FadeIn(est, shift=RIGHT * 0.08), run_time=0.9)

        real = txt("实际算得 11.89", size=38, color=CHALK).move_to([-2.4, 0.35, 0])
        self.play(FadeIn(real, shift=UP * 0.06), run_time=0.9)

        ok = txt("11.89 离 12 很近", size=28, color=GREEN).move_to([0, -0.75, 0])
        self.play(FadeIn(ok, shift=UP * 0.06), run_time=0.8)

        warn = txt("如果算成 118.9 或 1.189，小数点就点错了", size=27, color=RED)
        warn.move_to([0, -1.75, 0])
        self.play(FadeIn(warn, shift=UP * 0.06), run_time=0.8)

        tip = txt("估算能帮你一眼看出答案合不合理", size=26, color=DIM)
        tip.move_to([0, -2.45, 0])
        self.play(FadeIn(tip, shift=UP * 0.05), run_time=0.7)
        self.finish_section()

    # ---------------- 6. 总结 ---------------- 11.4
    def scene_summary(self):
        self.section(6, "小数乘法三句话")

        rows = VGroup(
            label_box("① 先按整数乘", size=30, color=GOLD),
            label_box("② 数一共几位小数", size=30, color=CHALK),
            label_box("③ 从右往左点小数点", size=30, color=GREEN),
        ).arrange(DOWN, buff=0.35).move_to([0, 1.15, 0])
        for r in rows:
            self.play(FadeIn(r, shift=RIGHT * 0.08), run_time=0.6)
            self.wait(0.5)

        n1 = txt("位数不够，用 0 补在前面", size=28, color=BLUE).move_to([0, -1.5, 0])
        n2 = txt("末尾的 0 可以去掉，中间的 0 不能去", size=27, color=DIM)
        n2.move_to([0, -2.2, 0])
        self.play(FadeIn(n1, shift=UP * 0.06), run_time=0.7)
        self.play(FadeIn(n2, shift=UP * 0.06), run_time=0.7)
        self.wait(0.8)
        self.finish_section()

    def construct(self):
        self.scene_story()
        self.clear_stage()
        self.scene_int()
        self.clear_stage()
        self.scene_dec()
        self.clear_stage()
        self.scene_zero()
        self.clear_stage()
        self.scene_tail()
        self.clear_stage()
        self.scene_est()
        self.clear_stage()
        self.scene_summary()
        self.clear_stage(0.8)