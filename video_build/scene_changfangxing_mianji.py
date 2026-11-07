# -*- coding: utf-8 -*-
"""长方形和正方形的面积：面积单位、长 × 宽、边长 × 边长、单位换算、周长对比。三年级下册。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


def grid(cols: int, rows: int, unit: float, center, color: str = CHALK,
         fill_opacity: float = 0.12, stroke_width: float = 1.6) -> VGroup:
    """cols × rows 的方格阵，返回 VGroup（含每格矩形）。"""
    cx, cy = center[0], center[1]
    w, h = cols * unit, rows * unit
    x0, y0 = cx - w / 2, cy - h / 2
    g = VGroup()
    for c in range(cols):
        for r in range(rows):
            g.add(Rectangle(width=unit, height=unit, color=color,
                            stroke_width=stroke_width,
                            fill_color=color, fill_opacity=fill_opacity)
                  .move_to([x0 + (c + 0.5) * unit, y0 + (r + 0.5) * unit, 0]))
    return g


def outline(cols: int, rows: int, unit: float, center, color: str = GOLD,
            stroke_width: float = 3) -> Rectangle:
    return Rectangle(width=cols * unit, height=rows * unit, color=color,
                     stroke_width=stroke_width).move_to([center[0], center[1], 0])


class ChangfangxingMianjiScene(NarratedScene):
    lesson = "changfangxing-mianji"

    def clear_stage(self, run_time: float = 0.5):
        keep = {id(self._track), id(self._fill)}
        junk = [m for m in self.mobjects if id(m) not in keep]
        if junk:
            self.play(*[FadeOut(m) for m in junk], run_time=run_time)
        self.cur_title = None
        self.cur_sub = None

    # ---------------- 0. 铺地砖 ---------------- 7x5
    def scene_story(self):
        self.section(0, "铺地砖：到底要多少块")

        tiles = grid(8, 6, 0.4, [-3.6, 0.35], color=GOLD, fill_opacity=0.075)
        frame = outline(8, 6, 0.4, [-3.6, 0.35], color=CHALK, stroke_width=3)
        self.play(LaggedStart(*[FadeIn(t) for t in tiles], lag_ratio=0.015), run_time=1.6)
        self.play(Create(frame), run_time=0.8)

        l_len = txt("长 8 米", size=24, color=GOLD).move_to([-3.6, -1.15, 0])
        l_wid = txt("宽 6 米", size=24, color=BLUE).move_to([-3.6, 1.95, 0])
        self.play(FadeIn(l_len), FadeIn(l_wid), run_time=0.7)

        head = txt("面积 = 表面的大小", size=34, color=GOLD).move_to([3.3, 1.5, 0])
        q1 = txt("铺满地面", size=32, color=CHALK).move_to([3.3, 0.35, 0])
        q2 = txt("要多少块？", size=32, color=CHALK).move_to([3.3, -0.35, 0])
        no = txt("不是围一圈的长度", size=24, color=DIM).move_to([3.3, -1.45, 0])
        self.play(FadeIn(head, shift=UP * 0.08), run_time=0.7)
        self.play(FadeIn(q1, shift=UP * 0.06), run_time=0.5)
        self.play(FadeIn(q2, shift=UP * 0.06), run_time=0.5)
        self.play(FadeIn(no), run_time=0.6)
        self.finish_section()

    # ---------------- 1. 1 平方厘米 ----------------
    def scene_unit(self):
        self.section(1, "1 平方厘米有多大")

        unit = grid(1, 1, 2.0, [-3.6, 0.45], color=GOLD, fill_opacity=0.16, stroke_width=3)
        frame = outline(1, 1, 2.0, [-3.6, 0.45], color=GOLD, stroke_width=3)
        lab = txt("1 平方厘米", size=24, color=GOLD).move_to([-3.6, 0.45, 0])
        self.play(FadeIn(unit), run_time=0.8)
        self.play(Create(frame), FadeIn(lab), run_time=0.8)

        # 两条边各标 1 厘米
        top = DoubleArrow([-3.6 - 1.0, 1.62, 0], [-3.6 + 1.0, 1.62, 0],
                          color=CHALK, stroke_width=2, buff=0,
                          max_tip_length_to_length_ratio=0.2)
        tl = txt("1 厘米", size=22, color=CHALK).move_to([-3.6, 1.95, 0])
        left = DoubleArrow([-4.75, 0.45 - 1.0, 0], [-4.75, 0.45 + 1.0, 0],
                           color=CHALK, stroke_width=2, buff=0,
                           max_tip_length_to_length_ratio=0.2)
        ll = txt("1 厘米", size=22, color=CHALK).move_to([-5.35, 0.45, 0])
        self.play(GrowArrow(top), FadeIn(tl), run_time=0.6)
        self.play(GrowArrow(left), FadeIn(ll), run_time=0.6)

        h1 = txt("边长 1 厘米的正方形", size=28, color=CHALK).move_to([3.1, 1.55, 0])
        h2 = txt("面积就是 1 平方厘米", size=28, color=GOLD).move_to([3.1, 0.75, 0])
        self.play(FadeIn(h1, shift=UP * 0.06), run_time=0.6)
        self.play(FadeIn(h2, shift=UP * 0.06), run_time=0.6)

        # 一排 3 个：3 平方厘米
        strip = grid(3, 1, 0.5, [3.1, -0.55], color=GREEN, fill_opacity=0.18)
        sframe = outline(3, 1, 0.5, [3.1, -0.55], color=GREEN, stroke_width=2.4)
        sl = txt("3 个 → 3 平方厘米", size=24, color=GREEN).move_to([3.1, -1.35, 0])
        self.play(LaggedStart(*[FadeIn(s) for s in strip], lag_ratio=0.2), run_time=0.9)
        self.play(Create(sframe), FadeIn(sl), run_time=0.7)
        self.finish_section()

    # ---------------- 2. 5 × 3 数格子 ----------------
    def scene_count(self):
        self.section(2, "5 × 3：数格子得面积")

        center = [-3.5, 0.6, 0]
        u = 0.62
        g = grid(5, 3, u, center, color=CHALK, fill_opacity=0.1)
        fr = outline(5, 3, u, center, color=GOLD, stroke_width=3)
        self.play(Create(fr), run_time=0.7)

        # 第一行 5 个
        self.play(LaggedStart(*[FadeIn(s) for s in g[:5]], lag_ratio=0.18), run_time=1.0)
        r1 = txt("每行摆 5 个", size=28, color=GOLD).move_to([3.2, 1.35, 0])
        self.play(FadeIn(r1, shift=UP * 0.06), run_time=0.6)

        # 其余两行
        self.play(LaggedStart(*[FadeIn(s) for s in g[5:]], lag_ratio=0.06), run_time=1.0)
        r2 = txt("一共摆 3 行", size=28, color=BLUE).move_to([3.2, 0.55, 0])
        self.play(FadeIn(r2, shift=UP * 0.06), run_time=0.6)

        # 长宽标注
        l_len = txt("长 5 厘米", size=24, color=GOLD).move_to([-3.5, -0.95, 0])
        l_wid = txt("宽 3 厘米", size=22, color=BLUE).move_to([-5.9, 0.6, 0])
        self.play(FadeIn(l_len), FadeIn(l_wid), run_time=0.6)

        calc = txt("5 × 3 = 15", size=44, color=GREEN).move_to([3.2, -0.65, 0])
        ans = txt("面积 15 平方厘米", size=26, color=GREEN).move_to([3.2, -1.5, 0])
        self.play(Write(calc), run_time=0.9)
        self.play(FadeIn(ans, shift=UP * 0.06), run_time=0.6)
        self.finish_section()

    # ---------------- 3. 公式 ----------------
    def scene_formula(self):
        self.section(3, "每行几个，摆几行")

        f = txt("长方形面积 = 长 × 宽", size=52, color=GOLD).move_to([0, 2.15, 0])
        self.play(Write(f), run_time=1.2)

        # 通用长方形 + 长宽标注
        rect = Rectangle(width=4.6, height=2.4, color=CHALK, stroke_width=3,
                         fill_color=CHALK, fill_opacity=0.06).move_to([0, 0.15, 0])
        self.play(Create(rect), run_time=0.8)

        da = DoubleArrow([-2.3, -1.32, 0], [2.3, -1.32, 0], color=GOLD,
                         stroke_width=2.6, buff=0,
                         max_tip_length_to_length_ratio=0.14)
        dl = txt("长", size=26, color=GOLD).move_to([0, -1.72, 0])
        self.play(GrowArrow(da), FadeIn(dl), run_time=0.7)

        db = DoubleArrow([-2.75, -1.05, 0], [-2.75, 1.35, 0], color=BLUE,
                         stroke_width=2.6, buff=0,
                         max_tip_length_to_length_ratio=0.14)
        bl = txt("宽", size=26, color=BLUE).move_to([-3.2, 0.15, 0])
        self.play(GrowArrow(db), FadeIn(bl), run_time=0.7)

        tip1 = txt("每行摆「长」个，一共摆「宽」行", size=26, color=DIM).move_to([0, -2.3, 0])
        self.play(FadeIn(tip1, shift=UP * 0.06), run_time=0.7)

        tip2 = txt("长和宽的单位要统一", size=26, color=GREEN).move_to([0, -2.9, 0])
        self.play(FadeIn(tip2, shift=UP * 0.06), run_time=0.7)
        self.finish_section()

    # ---------------- 4. 正方形 ----------------
    def scene_square(self):
        self.section(4, "正方形面积 = 边长 × 边长")

        center = [-3.7, 0.55, 0]
        u = 0.56
        g = grid(4, 4, u, center, color=GOLD, fill_opacity=0.12)
        fr = outline(4, 4, u, center, color=GOLD, stroke_width=3)
        self.play(Create(fr), run_time=0.6)
        self.play(LaggedStart(*[FadeIn(s) for s in g], lag_ratio=0.03), run_time=1.2)

        l1 = txt("边长 4 厘米", size=24, color=CHALK).move_to([-3.7, -0.82, 0])
        l2 = txt("边长 4 厘米", size=22, color=CHALK).move_to([-5.75, 0.55, 0])
        self.play(FadeIn(l1), FadeIn(l2), run_time=0.6)

        h = txt("正方形：长 = 宽", size=28, color=DIM).move_to([3.0, 1.45, 0])
        f = txt("面积 = 边长 × 边长", size=32, color=GOLD).move_to([3.0, 0.6, 0])
        c = txt("4 × 4 = 16", size=44, color=GREEN).move_to([3.0, -0.45, 0])
        a = txt("16 平方厘米", size=26, color=GREEN).move_to([3.0, -1.25, 0])
        self.play(FadeIn(h, shift=UP * 0.06), run_time=0.6)
        self.play(FadeIn(f, shift=UP * 0.06), run_time=0.7)
        self.play(Write(c), run_time=0.9)
        self.play(FadeIn(a, shift=UP * 0.06), run_time=0.6)
        self.finish_section()

    # ---------------- 5. 单位换算 ----------------
    def scene_convert(self):
        self.section(5, "1 平方分米 = 100 平方厘米")

        center = [-3.7, 0.45, 0]
        u = 0.25
        g = grid(10, 10, u, center, color=CHALK, fill_opacity=0.06, stroke_width=0.8)
        fr = outline(10, 10, u, center, color=GOLD, stroke_width=3)
        self.play(Create(fr), run_time=0.7)
        self.play(LaggedStart(*[FadeIn(s) for s in g], lag_ratio=0.006), run_time=1.8)

        # 10 厘米标注
        da = DoubleArrow([-3.7 - 1.25, 1.95, 0], [-3.7 + 1.25, 1.95, 0],
                         color=BLUE, stroke_width=2.2, buff=0,
                         max_tip_length_to_length_ratio=0.2)
        dt = txt("10 厘米", size=22, color=BLUE).move_to([-3.7, 2.28, 0])
        self.play(GrowArrow(da), FadeIn(dt), run_time=0.7)

        inner = txt("10 × 10 = 100 个小方块", size=22, color=DIM).move_to([-3.7, -1.35, 0])
        self.play(FadeIn(inner), run_time=0.6)

        f1 = txt("1 平方分米", size=34, color=GOLD).move_to([3.0, 1.35, 0])
        f2 = txt("= 100 平方厘米", size=34, color=GOLD).move_to([3.0, 0.6, 0])
        f3 = txt("1 平方米", size=30, color=BLUE).move_to([3.0, -0.55, 0])
        f4 = txt("= 100 平方分米", size=30, color=BLUE).move_to([3.0, -1.3, 0])
        self.play(FadeIn(f1, shift=UP * 0.06), run_time=0.6)
        self.play(FadeIn(f2, shift=UP * 0.06), run_time=0.6)
        self.play(FadeIn(f3, shift=UP * 0.06), run_time=0.6)
        self.play(FadeIn(f4, shift=UP * 0.06), run_time=0.6)
        self.finish_section()

    # ---------------- 6. 周长 vs 面积 ----------------
    def scene_compare(self):
        self.section(6, "周长走一圈，面积铺里面")

        head_l = txt("周长", size=32, color=BLUE).move_to([-3.4, 2.2, 0])
        head_r = txt("面积", size=32, color=GOLD).move_to([3.4, 2.2, 0])
        self.play(FadeIn(head_l, shift=UP * 0.08), FadeIn(head_r, shift=UP * 0.08),
                  run_time=0.7)

        u = 0.6
        # 左：只画边框，强调走一圈
        left = Rectangle(width=4 * u, height=3 * u, color=BLUE, stroke_width=4)
        left.move_to([-3.4, 0.5, 0])
        self.play(Create(left), run_time=1.0)
        walk = Dot(left.get_corner(UP + LEFT), radius=0.09, color=BLUE)
        self.play(FadeIn(walk), run_time=0.3)
        self.play(MoveAlongPath(walk, left.copy().set_fill(None)), run_time=1.8)
        self.play(FadeOut(walk), run_time=0.3)

        pc = txt("(4 + 3) × 2 = 14", size=32, color=BLUE).move_to([-3.4, -1.1, 0])
        pu = txt("周长 14 厘米", size=24, color=DIM).move_to([-3.4, -1.75, 0])
        self.play(Write(pc), run_time=0.9)
        self.play(FadeIn(pu), run_time=0.5)

        # 右：铺满
        g = grid(4, 3, u, [3.4, 0.5], color=GOLD, fill_opacity=0.2)
        self.play(LaggedStart(*[FadeIn(s) for s in g], lag_ratio=0.05), run_time=1.4)
        ac = txt("4 × 3 = 12", size=32, color=GOLD).move_to([3.4, -1.1, 0])
        au = txt("面积 12 平方厘米", size=24, color=DIM).move_to([3.4, -1.75, 0])
        self.play(Write(ac), run_time=0.9)
        self.play(FadeIn(au), run_time=0.5)

        tip = txt("周长用长度单位，面积用平方单位", size=27, color=GREEN).move_to([0, -2.7, 0])
        self.play(FadeIn(tip, shift=UP * 0.08), run_time=0.8)
        self.finish_section()

    def construct(self):
        self.scene_story()
        self.clear_stage()
        self.scene_unit()
        self.clear_stage()
        self.scene_count()
        self.clear_stage()
        self.scene_formula()
        self.clear_stage()
        self.scene_square()
        self.clear_stage()
        self.scene_convert()
        self.clear_stage()
        self.scene_compare()
        self.clear_stage(0.8)