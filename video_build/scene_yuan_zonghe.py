# -*- coding: utf-8 -*-
"""圆的综合：组合图形面积，外方内圆、外圆内方、弓形，两道例题与易错点。小升初衔接。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403

PI_314 = 3.14


def place(g, x, y):
    """左边缘对齐 x，竖直中心落在 y。"""
    g.move_to([0, 0, 0])
    g.shift(RIGHT * (x - g.get_left()[0]) + UP * (y - g.get_center()[1]))
    return g


def square_circle(side: float, at, color=CHALK):
    """正方形里画最大的圆。"""
    sq = Square(side_length=side, color=color, stroke_width=2.2)
    sq.move_to(at)
    c = Circle(radius=side / 2, color=BLUE, stroke_width=2.2).move_to(at)
    return VGroup(sq, c)


def circle_square(radius: float, at, color=CHALK):
    """圆里画最大的正方形（对角线 = 直径）。"""
    c = Circle(radius=radius, color=BLUE, stroke_width=2.2).move_to(at)
    s = Square(side_length=radius * 2 / (2 ** 0.5), color=color, stroke_width=2.2)
    s.rotate(PI / 4).move_to(at)
    return VGroup(c, s)


class YuanZongheScene(NarratedScene):
    lesson = "yuan-zonghe"

    def clear_stage(self, run_time: float = 0.5):
        keep = {id(self._track), id(self._fill)}
        junk = [m for m in self.mobjects if id(m) not in keep]
        if junk:
            self.play(*[FadeOut(m) for m in junk], run_time=run_time)
        self.cur_title = None
        self.cur_sub = None

    # ---------------- 0. 正方形里的圆 ---------------- 13.6
    def scene_story(self):
        self.section(0, "正方形里画最大的圆")

        g = square_circle(2.9, [-3.4, 0.15, 0])
        self.play(Create(g[0]), run_time=1.0)
        self.play(Create(g[1]), run_time=1.0)

        side = txt("边长 4 厘米", size=28, color=GOLD).move_to([-3.4, -1.75, 0])
        self.play(FadeIn(side, shift=UP * 0.05), run_time=0.7)

        corner = Arrow([-1.35, 1.4, 0], [-2.15, 1.28, 0], color=GOLD, buff=0.08,
                       stroke_width=2.4, max_tip_length_to_length_ratio=0.2)
        lab = txt("四个角是阴影", size=26, color=GOLD).move_to([-0.1, 1.8, 0])
        self.play(Create(corner), FadeIn(lab), run_time=0.8)

        q = txt("阴影面积是多少？", size=34, color=GREEN).move_to([3.2, 0.85, 0])
        self.play(FadeIn(q, shift=UP * 0.05), run_time=0.8)

        note = VGroup(
            txt("不能直接套一个公式", size=27, color=CHALK),
            txt("要用组合图形的办法", size=27, color=DIM),
        ).arrange(DOWN, buff=0.3).move_to([3.2, -0.7, 0])
        self.play(FadeIn(note[0], shift=UP * 0.05), run_time=0.7)
        self.play(FadeIn(note[1], shift=UP * 0.05), run_time=0.7)
        self.wait(1.6)
        self.finish_section()

    # ---------------- 1. 两条路 ---------------- 15.5
    def scene_twoways(self):
        self.section(1, "组合图形有两条路")

        box1 = label_box("整体减空白", size=36, color=GOLD).move_to([-3.3, 2.05, 0])
        self.play(FadeIn(box1, scale=0.97), run_time=0.9)
        d1 = VGroup(
            txt("先算大图形", size=28, color=CHALK),
            txt("再减掉不要的部分", size=28, color=CHALK),
            txt("外方内圆常用", size=26, color=DIM),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT).move_to([-3.3, 0.5, 0])
        for d in d1:
            self.play(FadeIn(d, shift=RIGHT * 0.05), run_time=0.65)

        box2 = label_box("分割求和", size=36, color=BLUE).move_to([3.3, 2.05, 0])
        self.play(FadeIn(box2, scale=0.97), run_time=0.9)
        d2 = VGroup(
            txt("切成几块能算的", size=28, color=CHALK),
            txt("一块一块加起来", size=28, color=CHALK),
            txt("弓形常用", size=26, color=DIM),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT).move_to([3.3, 0.5, 0])
        for d in d2:
            self.play(FadeIn(d, shift=RIGHT * 0.05), run_time=0.65)

        tip = label_box("哪条简单走哪条", size=30, color=GREEN).move_to([0, -1.7, 0])
        self.play(FadeIn(tip, scale=0.97), run_time=0.9)
        self.wait(1.8)
        self.finish_section()

    # ---------------- 2. 两个关键关系 ---------------- 15.7
    def scene_relation(self):
        self.section(2, "圆和正方形的关键关系")

        g1 = square_circle(2.3, [-3.5, 0.75, 0])
        self.play(Create(g1), run_time=1.1)
        t1 = txt("外方内圆：直径 = 边长", size=27, color=GOLD).move_to([-3.5, -0.95, 0])
        self.play(FadeIn(t1, shift=UP * 0.05), run_time=0.8)

        g2 = circle_square(1.15, [3.5, 0.75, 0])
        self.play(Create(g2), run_time=1.1)
        t2 = txt("外圆内方：对角线 = 直径", size=27, color=BLUE).move_to([3.5, -0.95, 0])
        self.play(FadeIn(t2, shift=UP * 0.05), run_time=0.8)

        tip = VGroup(
            txt("抓住这一条，题就破了一半", size=28, color=GREEN),
            txt("圆的半径 = 边长 ÷ 2 = 直径 ÷ 2", size=27, color=DIM),
        ).arrange(DOWN, buff=0.3).move_to([0, -2.15, 0])
        self.play(FadeIn(tip[0], shift=UP * 0.05), run_time=0.7)
        self.play(FadeIn(tip[1], shift=UP * 0.05), run_time=0.7)
        self.wait(1.6)
        self.finish_section()

    # ---------------- 3. 扇形减三角形 ---------------- 13.2
    def scene_sector(self):
        self.section(3, "扇形减三角形，剩下弓形")

        apex = [-3.2, -0.3, 0]
        r = 2.5
        sec = Sector(radius=r, start_angle=0, angle=PI / 2,
                     color=GOLD, fill_color=GOLD, fill_opacity=0.18, stroke_width=2.2)
        sec.shift(apex)
        tri = Polygon([0, 0, 0], [r, 0, 0], [0, r, 0], color=RED,
                      fill_color=RED, fill_opacity=0.16, stroke_width=2.0)
        tri.shift(apex)
        self.play(Create(sec), run_time=1.2)
        self.play(Create(tri), run_time=1.0)

        lab = txt("弓形 = 扇形 - 三角形", size=30, color=GREEN).move_to([3.1, 1.45, 0])
        self.play(FadeIn(lab, shift=UP * 0.05), run_time=0.8)

        rows = VGroup(
            txt("扇形：1/4 × πr²", size=29, color=GOLD),
            txt("三角形：1/2 × r × r", size=29, color=RED),
            txt("相减就是弓形面积", size=28, color=CHALK),
        ).arrange(DOWN, buff=0.34, aligned_edge=LEFT).move_to([3.15, 0.0, 0])
        for rw in rows:
            self.play(FadeIn(rw, shift=RIGHT * 0.05), run_time=0.7)
        self.wait(1.6)
        self.finish_section()

    # ---------------- 4. 例题一：外方内圆 ---------------- 18.1
    def scene_ex1(self):
        self.section(4, "边长 4 厘米，阴影多少")

        g = square_circle(2.1, [-3.7, 0.7, 0])
        self.play(Create(g), run_time=1.1)

        rows = [
            ("正方形：4 × 4 = 16", GOLD),
            ("半径：4 ÷ 2 = 2", BLUE),
            ("圆：3.14 × 2² = 12.56", BLUE),
            ("阴影：16 - 12.56", CHALK),
            ("≈ 3.44（平方厘米）", GREEN),
        ]
        y = 2.3
        for s, c in rows:
            self.play(FadeIn(txt(s, size=29, color=c).move_to([1.2, y, 0]),
                             shift=UP * 0.04), run_time=0.7)
            y -= 0.72

        note = label_box("整体减空白", size=27, color=GOLD).move_to([-3.7, -1.55, 0])
        self.play(FadeIn(note, scale=0.97), run_time=0.8)
        self.wait(2.0)
        self.finish_section()

    # ---------------- 5. 例题二：外圆内方 ---------------- 16.6
    def scene_ex2(self):
        self.section(5, "圆里画正方形，阴影多少")

        g = circle_square(1.25, [-3.7, 0.55, 0])
        self.play(Create(g), run_time=1.1)

        rows = [
            ("直径 4，对角线也是 4", GOLD),
            ("正方形：4 × 4 ÷ 2 = 8", BLUE),
            ("圆：3.14 × 2² = 12.56", BLUE),
            ("阴影：12.56 - 8", CHALK),
            ("≈ 4.56（平方厘米）", GREEN),
        ]
        y = 2.3
        for s, c in rows:
            self.play(FadeIn(txt(s, size=29, color=c).move_to([1.2, y, 0]),
                             shift=UP * 0.04), run_time=0.7)
            y -= 0.72

        note = label_box("圆减正方形", size=27, color=GOLD).move_to([-3.7, -1.55, 0])
        self.play(FadeIn(note, scale=0.97), run_time=0.8)
        self.wait(1.8)
        self.finish_section()

    # ---------------- 6. 易错点 ---------------- 13.3
    def scene_warn(self):
        self.section(6, "三个易错点")

        items = [
            ("半径和直径搞混", "先看清楚给的是哪一个"),
            ("半圆忘记除以 2", "半圆是整圆的一半"),
            ("π 取 3.14 还写等号", "近似值要写约等于"),
        ]
        y = 2.0
        for bad_s, note in items:
            bad = txt(bad_s, size=27, color=RED).move_to([-3.2, y, 0])
            n = txt(note, size=24, color=GREEN).move_to([3.3, y, 0])
            cross = Line(bad.get_left() + [-0.1, -0.08, 0],
                         bad.get_right() + [0.1, 0.18, 0],
                         color=RED, stroke_width=2.8)
            self.play(FadeIn(bad, shift=RIGHT * 0.05), run_time=0.6)
            self.play(Create(cross), FadeIn(n, shift=RIGHT * 0.05), run_time=0.7)
            self.wait(0.4)
            y -= 0.9

        rows = VGroup(
            label_box("① 先看清整体和空白", size=24, color=GOLD),
            label_box("② 半径 = 直径 ÷ 2", size=24, color=CHALK),
            label_box("③ 近似值写约等于", size=24, color=GREEN),
        ).arrange(DOWN, buff=0.18).move_to([0, -1.85, 0])
        for rw in rows:
            self.play(FadeIn(rw, shift=RIGHT * 0.06), run_time=0.6)
            self.wait(0.4)

        self.wait(0.8)
        self.finish_section()

    def construct(self):
        self.scene_story()
        self.clear_stage()
        self.scene_twoways()
        self.clear_stage()
        self.scene_relation()
        self.clear_stage()
        self.scene_sector()
        self.clear_stage()
        self.scene_ex1()
        self.clear_stage()
        self.scene_ex2()
        self.clear_stage()
        self.scene_warn()
        self.clear_stage(0.8)