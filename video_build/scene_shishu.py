# -*- coding: utf-8 -*-
"""实数：平方根、算术平方根、立方根、无理数与实数分类、数轴与估算。八年级上。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


def P(x, y):
    return np.array([float(x), float(y), 0.0])


class ShishuScene(NarratedScene):
    lesson = "shishu"

    def clear_stage(self, run_time: float = 0.5):
        keep = {id(self._track), id(self._fill)}
        junk = [m for m in self.mobjects if id(m) not in keep]
        if junk:
            self.play(*[FadeOut(m) for m in junk], run_time=run_time)
        self.cur_title = None
        self.cur_sub = None

    # ---------------- 0. 面积是 2 的正方形 ---------------- 24.2
    def scene_story(self):
        self.section(0, "面积是 2，边长是多少")

        sq1 = Square(side_length=2.0, stroke_color=GOLD, stroke_width=3,
                     fill_color=GOLD, fill_opacity=0.1).move_to([-4.4, 0.45, 0])
        self.play(Create(sq1), run_time=1.2)
        s1 = txt("边长 3", size=25, color=CHALK).move_to([-4.4, -1.2, 0])
        a1 = txt("面积 9", size=27, color=GOLD).move_to([-4.4, 1.95, 0])
        self.play(FadeIn(s1), FadeIn(a1), run_time=0.8)

        sq2 = Square(side_length=1.35, stroke_color=BLUE, stroke_width=3,
                     fill_color=BLUE, fill_opacity=0.12).move_to([2.2, 0.5, 0])
        self.play(Create(sq2), run_time=1.2)
        a2 = txt("面积 2", size=27, color=BLUE).move_to([2.2, 1.65, 0])
        self.play(FadeIn(a2), run_time=0.7)

        s2 = txt("边长 = ?", size=27, color=CHALK).move_to([2.2, -1.05, 0])
        self.play(FadeIn(s2, shift=UP * 0.05), run_time=0.7)

        arrow = Arrow(P(-2.6, 0.45), P(1.15, 0.45), color=DIM,
                      stroke_width=3, max_tip_length_to_length_ratio=0.16)
        self.play(Create(arrow), run_time=0.8)

        s3 = VGroup(
            txt("边长 = √2", size=30, color=GREEN),
            txt("≈ 1.414 213 56…", size=27, color=DIM),
        ).arrange(RIGHT, buff=0.35).move_to([1.5, -1.85, 0])
        self.play(FadeIn(s3, shift=UP * 0.05), run_time=1.0)

        note = txt("写不完，也算不尽——这就是无理数", size=27, color=CHALK)
        note.move_to([0, -3.0, 0])
        self.play(FadeIn(note, shift=UP * 0.05), run_time=1.0)
        self.wait(2.8)
        self.finish_section()

    # ---------------- 1. 平方根 ---------------- 28.4
    def scene_sqrt(self):
        self.section(1, "平方根与算术平方根")

        r1 = VGroup(
            txt("3² = 9", size=32, color=CHALK),
            txt("所以 3 是 9 的平方根", size=25, color=DIM),
        ).arrange(RIGHT, buff=0.5).move_to([-2.4, 2.3, 0])
        self.play(FadeIn(r1, shift=UP * 0.05), run_time=0.9)

        r2 = VGroup(
            txt("(−3)² = 9", size=32, color=CHALK),
            txt("所以 −3 也是 9 的平方根", size=25, color=DIM),
        ).arrange(RIGHT, buff=0.5).move_to([-2.0, 1.35, 0])
        self.play(FadeIn(r2, shift=UP * 0.05), run_time=0.9)

        box = label_box("9 的平方根是 ±3", size=34, color=GOLD)
        box.move_to([0.6, 0.1, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.1)

        t1 = txt("一个正数有两个平方根，互为相反数", size=26, color=CHALK)
        t1.move_to([0, -0.85, 0])
        self.play(FadeIn(t1, shift=UP * 0.05), run_time=0.8)

        t2 = VGroup(
            txt("正的那个叫算术平方根", size=26, color=GREEN),
            txt("√9 = 3", size=32, color=GREEN),
        ).arrange(RIGHT, buff=0.5).move_to([-1.4, -1.75, 0])
        self.play(FadeIn(t2, shift=UP * 0.05), run_time=0.9)

        t3 = VGroup(
            txt("0 的平方根是 0", size=24, color=DIM),
            txt("负数没有平方根", size=24, color=RED),
        ).arrange(RIGHT, buff=1.2).move_to([0, -2.75, 0])
        for m in t3:
            self.play(FadeIn(m, shift=UP * 0.05), run_time=0.7)

        self.wait(2.8)
        self.finish_section()

    # ---------------- 2. 立方根 ---------------- 20.3
    def scene_cbrt(self):
        self.section(2, "立方根：任何数都有")

        r1 = VGroup(
            txt("2³ = 8", size=32, color=CHALK),
            txt("→", size=30, color=DIM),
            txt("³√8 = 2", size=32, color=GOLD),
        ).arrange(RIGHT, buff=0.45).move_to([0, 1.85, 0])
        self.play(FadeIn(r1, shift=UP * 0.05), run_time=1.0)

        r2 = VGroup(
            txt("(−2)³ = −8", size=32, color=CHALK),
            txt("→", size=30, color=DIM),
            txt("³√(−8) = −2", size=32, color=GOLD),
        ).arrange(RIGHT, buff=0.45).move_to([0, 0.75, 0])
        self.play(FadeIn(r2, shift=UP * 0.05), run_time=1.0)

        t1 = VGroup(
            txt("平方根：正数有两个，负数没有", size=26, color=BLUE),
            txt("立方根：任何数都有，而且只有一个", size=26, color=GREEN),
        ).arrange(DOWN, buff=0.35).move_to([0, -0.65, 0])
        for m in t1:
            self.play(FadeIn(m, shift=UP * 0.05), run_time=0.8)

        note = txt("负数的立方根是负数，符号直接搬出来", size=25, color=DIM)
        note.move_to([0, -2.5, 0])
        self.play(FadeIn(note, shift=UP * 0.05), run_time=0.9)
        self.wait(2.6)
        self.finish_section()

    # ---------------- 3. 无理数与实数分类 ---------------- 24.5
    def scene_classify(self):
        self.section(3, "无理数与实数")

        root = label_box("实数", size=32, color=GOLD).move_to([-5.2, 2.2, 0])
        self.play(FadeIn(root, scale=0.97), run_time=0.9)

        r1 = label_box("有理数", size=28, color=BLUE).move_to([-1.6, 1.2, 0])
        r2 = label_box("无理数", size=28, color=ORANGE).move_to([3.6, 1.2, 0])
        branch = VGroup(
            Line(P(-5.2, 1.88), P(-5.2, 1.62), color=DIM, stroke_width=2),
            Line(P(-5.2, 1.62), P(3.6, 1.62), color=DIM, stroke_width=2),
            Line(P(-1.6, 1.62), P(-1.6, 1.52), color=DIM, stroke_width=2),
            Line(P(3.6, 1.62), P(3.6, 1.52), color=DIM, stroke_width=2),
        )
        self.play(Create(branch), run_time=0.9)
        self.play(FadeIn(r1, scale=0.97), run_time=0.7)
        self.play(FadeIn(r2, scale=0.97), run_time=0.7)

        c1 = txt("整数、分数都能写成两整数相除", size=23, color=CHALK)
        c1.move_to([-1.6, 0.35, 0])
        c2 = txt("无限不循环小数，如 √2、π", size=23, color=CHALK)
        c2.move_to([3.6, 0.35, 0])
        self.play(FadeIn(c1, shift=UP * 0.05), run_time=0.7)
        self.play(FadeIn(c2, shift=UP * 0.05), run_time=0.7)

        ex1 = txt("如 3、−5、0.25、1/3…", size=22, color=DIM).move_to([-1.6, -0.35, 0])
        ex2 = txt("写不完，也不循环", size=22, color=DIM).move_to([3.6, -0.35, 0])
        self.play(FadeIn(ex1), FadeIn(ex2), run_time=0.7)

        note = VGroup(
            txt("有理数和无理数，统称实数", size=27, color=CHALK),
            txt("√2 不是分数，它的小数位永远不会循环", size=24, color=ORANGE),
        ).arrange(DOWN, buff=0.34).move_to([0, -1.6, 0])
        for m in note:
            self.play(FadeIn(m, shift=UP * 0.05), run_time=0.8)

        tail = txt("π 也是无理数，3.14 只是近似值", size=24, color=DIM)
        tail.move_to([0, -2.7, 0])
        self.play(FadeIn(tail, shift=UP * 0.05), run_time=0.8)
        self.wait(2.6)
        self.finish_section()

    # ---------------- 4. 数轴与估算 ---------------- 20.3
    def scene_line(self):
        self.section(4, "数轴上，一一对应")

        axis = Line(P(-6.4, 0.4), P(6.4, 0.4), color=CHALK, stroke_width=3)
        self.play(Create(axis), run_time=1.0)
        ticks = VGroup()
        for i in range(-3, 4):
            x = i * 1.7
            ticks.add(Line(P(x, 0.22), P(x, 0.58), color=DIM, stroke_width=2))
        self.play(LaggedStart(*[Create(t) for t in ticks], lag_ratio=0.06),
                  run_time=1.0)
        nums = VGroup()
        for i in range(-3, 4):
            nums.add(txt(str(i), size=22, color=DIM).move_to([i * 1.7, -0.05, 0]))
        self.play(FadeIn(nums), run_time=0.7)

        dot = Dot(P(1.7 * 1.414, 0.4), radius=0.09, color=GOLD)
        self.play(FadeIn(dot, scale=0.5), run_time=0.6)
        dl = txt("√2", size=25, color=GOLD).move_to([1.7 * 1.414, 0.95, 0])
        self.play(FadeIn(dl, shift=UP * 0.05), run_time=0.7)

        t1 = txt("每个实数都对应数轴上一个点", size=26, color=CHALK)
        t1.move_to([0, 1.85, 0])
        self.play(FadeIn(t1, shift=UP * 0.05), run_time=0.8)

        t2 = VGroup(
            txt("1.4² = 1.96", size=26, color=BLUE),
            txt("1.5² = 2.25", size=26, color=BLUE),
            txt("所以 1.4 < √2 < 1.5", size=26, color=GREEN),
        ).arrange(RIGHT, buff=0.45).move_to([0, -1.25, 0])
        for m in t2:
            self.play(FadeIn(m, shift=UP * 0.05), run_time=0.65)

        note = txt("估算无理数：找左右两个能开方的数夹住它", size=25, color=DIM)
        note.move_to([0, -2.45, 0])
        self.play(FadeIn(note, shift=UP * 0.05), run_time=0.9)
        self.wait(2.4)
        self.finish_section()

    # ---------------- 5. 两个常用性质 ---------------- 24.5
    def scene_prop(self):
        self.section(5, "两个容易混的式子")

        b1 = label_box("√(a²) = |a|", size=34, color=GOLD).move_to([-3.6, 1.9, 0])
        self.play(FadeIn(b1, scale=0.97), run_time=1.0)
        e1 = VGroup(
            txt("√((−3)²) = √9 = 3", size=26, color=CHALK),
            txt("开出来一定是正数或 0", size=23, color=DIM),
        ).arrange(DOWN, buff=0.26).move_to([-3.6, 0.75, 0])
        for m in e1:
            self.play(FadeIn(m, shift=UP * 0.05), run_time=0.7)

        b2 = label_box("(√a)² = a", size=34, color=GREEN).move_to([3.6, 1.9, 0])
        self.play(FadeIn(b2, scale=0.97), run_time=1.0)
        e2 = VGroup(
            txt("先开方，再平方", size=23, color=DIM),
            txt("要求 a ≥ 0", size=25, color=ORANGE),
        ).arrange(DOWN, buff=0.26).move_to([3.6, 0.75, 0])
        for m in e2:
            self.play(FadeIn(m, shift=UP * 0.05), run_time=0.7)

        note = VGroup(
            txt("顺序不同，结果不同", size=27, color=CHALK),
            txt("一个套绝对值，一个直接还原", size=24, color=DIM),
        ).arrange(DOWN, buff=0.3).move_to([0, -1.0, 0])
        for m in note:
            self.play(FadeIn(m, shift=UP * 0.05), run_time=0.8)

        tail = txt("判断一个数有没有平方根，先看它是不是负数", size=24, color=GOLD)
        tail.move_to([0, -2.2, 0])
        self.play(FadeIn(tail, shift=UP * 0.05), run_time=0.9)
        self.wait(2.4)
        self.finish_section()

    # ---------------- 6. 例题与三个易错点 ---------------- 27.8
    def scene_ex(self):
        self.section(6, "例题与三个易错点")

        q = txt("求下列各式的值", size=27, color=CHALK).move_to([0, 2.45, 0])
        self.play(FadeIn(q, shift=UP * 0.05), run_time=0.8)

        rows = [
            ("√36", "= 6", GOLD),
            ("−√16", "= −4", BLUE),
            ("³√(−27)", "= −3", GREEN),
        ]
        y = 1.6
        for left, right, col in rows:
            lt = txt(left, size=32, color=CHALK)
            lt.move_to([0, y, 0])
            lt.align_to(P(-1.5, 0), RIGHT)
            rt = txt(right, size=32, color=col)
            rt.move_to([0, y, 0])
            rt.align_to(P(-1.15, 0), LEFT)
            self.play(FadeIn(lt, shift=UP * 0.05), run_time=0.55)
            self.play(FadeIn(rt, shift=UP * 0.05), run_time=0.55)
            y -= 0.95

        items = [
            ("9 的平方根只写 3", "两个：±3"),
            ("√(a²) 直接写成 a", "等于 |a|"),
            ("以为负数没有立方根", "负数有立方根"),
        ]
        y2 = -1.25
        for bad_s, good_s in items:
            bad = txt(bad_s, size=24, color=RED).move_to([-3.0, y2, 0])
            good = txt(good_s, size=23, color=GREEN).move_to([3.6, y2, 0])
            cross = Line([bad.get_left()[0] - 0.07, y2 - 0.02, 0],
                         [bad.get_right()[0] + 0.07, y2 - 0.02, 0],
                         color=RED, stroke_width=2.2)
            self.play(FadeIn(bad, shift=RIGHT * 0.05), run_time=0.55)
            self.play(Create(cross), run_time=0.35)
            self.play(FadeIn(good, shift=RIGHT * 0.05), run_time=0.55)
            y2 -= 0.72

        self.wait(2.8)
        self.finish_section()

    def construct(self):
        self.scene_story()
        self.clear_stage()
        self.scene_sqrt()
        self.clear_stage()
        self.scene_cbrt()
        self.clear_stage()
        self.scene_classify()
        self.clear_stage()
        self.scene_line()
        self.clear_stage()
        self.scene_prop()
        self.clear_stage()
        self.scene_ex()
        self.clear_stage(0.8)