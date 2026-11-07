# -*- coding: utf-8 -*-
"""平行四边形的面积：数方格、剪拼成长方形、底×高、例题与易错点。五年级上册。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


def para(A, B, D, color: str = CHALK, fill: float = 0.0) -> Polygon:
    """由底边两端点 A、B 与左上顶点 D 确定平行四边形。"""
    C = [B[0] + (D[0] - A[0]), B[1] + (D[1] - A[1]), 0]
    return Polygon(A, B, C, D, color=color, stroke_width=3,
                   fill_color=color, fill_opacity=fill)


class PingxingMianjiScene(NarratedScene):
    lesson = "pingxing-mianji"

    def clear_stage(self, run_time: float = 0.5):
        keep = {id(self._track), id(self._fill)}
        junk = [m for m in self.mobjects if id(m) not in keep]
        if junk:
            self.play(*[FadeOut(m) for m in junk], run_time=run_time)
        self.cur_title = None
        self.cur_sub = None

    # ---------------- 0. 一块平行四边形菜地 ---------------- 18.7
    def scene_story(self):
        self.section(0, "一块平行四边形菜地")

        A, B = [-4.6, -1.4, 0], [-0.4, -1.4, 0]
        D, C = [-2.5, 1.4, 0], [1.7, 1.4, 0]
        shape = para(A, B, D, GOLD, 0.22)
        self.play(Create(shape), run_time=1.6)

        base_br = Brace(Line(A, B, color=GOLD), DOWN, buff=0.16, color=GOLD)
        base_l = txt("底 6 米", size=26, color=GOLD).next_to(base_br, DOWN, buff=0.1)
        self.play(Create(base_br), FadeIn(base_l), run_time=1.0)

        E = [-2.5, -1.4, 0]
        h_line = DashedLine(D, E, color=BLUE, stroke_width=2.6, dash_length=0.14)
        right = Square(side_length=0.26, color=BLUE, stroke_width=2)
        right.move_to([E[0] + 0.13, E[1] + 0.13, 0])
        h_l = txt("高 4 米", size=24, color=BLUE).move_to([-1.62, 0.05, 0])
        self.play(Create(h_line), run_time=0.8)
        self.play(Create(right), FadeIn(h_l, shift=RIGHT * 0.05), run_time=0.8)

        slant_l = txt("斜边 5 米", size=24, color=DIM).move_to([-4.05, 0.5, 0])
        self.play(FadeIn(slant_l, shift=RIGHT * 0.05), run_time=0.8)

        q = VGroup(
            txt("肥料按面积买", size=27, color=CHALK),
            txt("它的面积是多少？", size=30, color=GOLD),
        ).arrange(DOWN, buff=0.24).move_to([4.2, 1.2, 0])
        self.play(FadeIn(q[0], shift=UP * 0.05), run_time=0.7)
        self.play(FadeIn(q[1], shift=UP * 0.05), run_time=0.7)

        note = VGroup(
            txt("不像长方形，", size=25, color=DIM),
            txt("不能直接量长乘宽", size=25, color=DIM),
            txt("先把它变成学过的图形", size=26, color=GREEN),
        ).arrange(DOWN, buff=0.2).move_to([4.2, -1.1, 0])
        for n in note:
            self.play(FadeIn(n, shift=UP * 0.05), run_time=0.65)
        self.wait(2.0)
        self.finish_section()

    # ---------------- 1. 数方格 ---------------- 18.0
    def scene_count(self):
        self.section(1, "先数方格试试")

        cell = 0.5
        x0, y0 = -4.6, -1.1
        grid = VGroup()
        for c in range(9):
            for r in range(4):
                grid.add(Rectangle(width=cell, height=cell, stroke_width=1.4,
                                   color=DIM, fill_opacity=0.0)
                          .move_to([x0 + (c + 0.5) * cell, y0 + (r + 0.5) * cell, 0]))
        self.play(LaggedStart(*[FadeIn(g) for g in grid], lag_ratio=0.02), run_time=1.6)

        A = [x0, y0, 0]
        B = [x0 + 6 * cell, y0, 0]
        D = [x0 + 3 * cell, y0 + 4 * cell, 0]
        shape = para(A, B, D, GOLD, 0.0)
        self.play(Create(shape), run_time=1.4)

        rows = [
            ("整格：16 个", GOLD),
            ("不满格：拼成 8 个", BLUE),
            ("一共：24 个格", GREEN),
        ]
        y = 1.15
        for s, c in rows:
            self.play(FadeIn(txt(s, size=27, color=c).move_to([4.0, y, 0]), shift=RIGHT * 0.05),
                      run_time=0.7)
            y -= 0.85

        res = txt("面积 = 24 平方厘米", size=29, color=GREEN).move_to([3.9, -1.35, 0])
        self.play(FadeIn(res, shift=UP * 0.05), run_time=0.9)

        tip = txt("数格子太麻烦，得找公式", size=26, color=GOLD).move_to([0, -2.45, 0])
        self.play(FadeIn(tip, shift=UP * 0.05), run_time=0.8)
        self.wait(2.0)
        self.finish_section()

    # ---------------- 2. 剪拼成长方形 ---------------- 12.7
    def scene_cut(self):
        self.section(2, "沿高剪开，平移到右边")

        A, B = [-4.6, -1.4, 0], [-0.4, -1.4, 0]
        D, C = [-2.5, 1.4, 0], [1.7, 1.4, 0]
        E = [-2.5, -1.4, 0]
        shape = para(A, B, D, CHALK, 0.10)
        self.play(Create(shape), run_time=1.2)

        h_line = DashedLine(D, E, color=BLUE, stroke_width=2.6, dash_length=0.14)
        self.play(Create(h_line), run_time=0.7)

        tri = Polygon(A, D, E, color=BLUE, stroke_width=2.5,
                      fill_color=BLUE, fill_opacity=0.35)
        self.play(FadeIn(tri), run_time=0.8)

        self.play(tri.animate.shift(RIGHT * 4.2), run_time=2.0, rate_func=smooth)

        self.play(FadeOut(shape), run_time=0.5)

        rect = Rectangle(width=4.2, height=2.8, color=GREEN, stroke_width=3)
        rect.move_to([-0.4, 0, 0])
        self.play(Create(rect), run_time=0.9)

        lab = txt("拼成长方形，面积一点没变", size=28, color=GREEN).move_to([0, -2.4, 0])
        self.play(FadeIn(lab, shift=UP * 0.06), run_time=0.9)
        self.wait(2.6)
        self.finish_section()

    # ---------------- 3. 对应关系 ---------------- 15.5
    def scene_map(self):
        self.section(3, "长就是底，宽就是高")

        rect = Rectangle(width=3.6, height=2.4, color=GOLD, stroke_width=3,
                         fill_color=GOLD, fill_opacity=0.15)
        rect.move_to([-2.7, 0.35, 0])
        self.play(Create(rect), run_time=1.1)

        left_br = Brace(rect, LEFT, buff=0.16, color=GOLD)
        left_l = txt("宽 = 高", size=25, color=GOLD).next_to(left_br, LEFT, buff=0.1)
        bot_br = Brace(rect, DOWN, buff=0.16, color=BLUE)
        bot_l = txt("长 = 底", size=25, color=BLUE).next_to(bot_br, DOWN, buff=0.1)
        self.play(Create(bot_br), FadeIn(bot_l), run_time=0.9)
        self.play(Create(left_br), FadeIn(left_l), run_time=0.9)

        eqs = VGroup(
            txt("长方形的长 = 平行四边形的底", size=27, color=BLUE),
            txt("长方形的宽 = 平行四边形的高", size=27, color=GOLD),
            txt("长 × 宽 = 底 × 高", size=29, color=CHALK),
            txt("所以两个图形的面积相等", size=27, color=GREEN),
        ).arrange(DOWN, buff=0.26, aligned_edge=LEFT).move_to([2.9, 0.55, 0])
        for e in eqs:
            self.play(FadeIn(e, shift=RIGHT * 0.05), run_time=0.6)
            self.wait(0.3)
        self.wait(1.8)
        self.finish_section()

    # ---------------- 4. 公式 ---------------- 13.5
    def scene_formula(self):
        self.section(4, "平行四边形的面积公式")

        f1 = txt("平行四边形的面积 = 底 × 高", size=40, color=CHALK).move_to([0, 1.85, 0])
        self.play(FadeIn(f1, shift=UP * 0.05), run_time=1.0)

        box = label_box("S = a × h", size=48, color=GOLD)
        box.move_to([0, 0.15, 0])
        self.play(FadeIn(box, scale=0.96), run_time=1.0)

        leg = VGroup(
            txt("S 表示面积", size=25, color=DIM),
            txt("a 表示底", size=25, color=BLUE),
            txt("h 表示高", size=25, color=GOLD),
        ).arrange(RIGHT, buff=0.9).move_to([0, -1.1, 0])
        self.play(FadeIn(leg, shift=UP * 0.05), run_time=1.0)

        note = VGroup(
            txt("底和高必须互相对应", size=27, color=CHALK),
            txt("高是这条底边上的高，不是斜边", size=26, color=GREEN),
        ).arrange(DOWN, buff=0.22).move_to([0, -2.3, 0])
        self.play(FadeIn(note[0], shift=UP * 0.05), run_time=0.7)
        self.play(FadeIn(note[1], shift=UP * 0.05), run_time=0.8)
        self.wait(2.2)
        self.finish_section()

    # ---------------- 5. 例题 ---------------- 15.5
    def scene_example(self):
        self.section(5, "底 6 米，高 4 米，面积多少")

        prob = txt("底 6 米，高 4 米，斜边 5 米", size=30, color=CHALK).move_to([0, 2.2, 0])
        self.play(FadeIn(prob, shift=UP * 0.05), run_time=0.9)

        eq = VGroup(
            txt("S = 6 × 4", size=42, color=GOLD),
            txt("= 24（平方米）", size=40, color=GREEN),
        ).arrange(DOWN, buff=0.3).move_to([0, 0.6, 0])
        self.play(FadeIn(eq[0], shift=UP * 0.05), run_time=0.9)
        self.play(FadeIn(eq[1], shift=UP * 0.05), run_time=0.9)

        warn = txt("斜边 5 米是干扰条件，用不上", size=27, color=RED).move_to([0, -0.9, 0])
        self.play(FadeIn(warn, shift=UP * 0.05), run_time=0.9)

        rev = VGroup(
            label_box("求底：a = S ÷ h", size=25, color=BLUE),
            label_box("求高：h = S ÷ a", size=25, color=GOLD),
        ).arrange(RIGHT, buff=0.7).move_to([0, -2.0, 0])
        self.play(FadeIn(rev[0], shift=UP * 0.05), run_time=0.7)
        self.play(FadeIn(rev[1], shift=UP * 0.05), run_time=0.7)
        self.wait(2.2)
        self.finish_section()

    # ---------------- 6. 易错点 + 三句话 ---------------- 15.1
    def scene_warn(self):
        self.section(6, "三个易错点")

        items = [
            ("把斜边当成高", "高要垂直于底"),
            ("底和高不配对", "高必须是这条底上的"),
            ("面积单位写成米", "面积用平方米"),
        ]
        y = 2.05
        for bad_s, note in items:
            bad = txt(bad_s, size=28, color=RED).move_to([-3.2, y, 0])
            n = txt(note, size=25, color=GREEN).move_to([3.2, y, 0])
            cross = Line(bad.get_left() + [-0.1, -0.08, 0],
                         bad.get_right() + [0.1, 0.18, 0],
                         color=RED, stroke_width=2.8)
            self.play(FadeIn(bad, shift=RIGHT * 0.05), run_time=0.6)
            self.play(Create(cross), FadeIn(n, shift=RIGHT * 0.05), run_time=0.7)
            self.wait(0.7)
            y -= 0.92

        rows = VGroup(
            label_box("① 剪拼成长方形，面积不变", size=24, color=GOLD),
            label_box("② 面积 = 底 × 高", size=24, color=CHALK),
            label_box("③ 高要对准底，单位用平方", size=24, color=GREEN),
        ).arrange(DOWN, buff=0.2).move_to([0, -1.65, 0])
        for r in rows:
            self.play(FadeIn(r, shift=RIGHT * 0.06), run_time=0.6)
            self.wait(0.55)

        self.wait(1.0)
        self.finish_section()

    def construct(self):
        self.scene_story()
        self.clear_stage()
        self.scene_count()
        self.clear_stage()
        self.scene_cut()
        self.clear_stage()
        self.scene_map()
        self.clear_stage()
        self.scene_formula()
        self.clear_stage()
        self.scene_example()
        self.clear_stage()
        self.scene_warn()
        self.clear_stage(0.8)