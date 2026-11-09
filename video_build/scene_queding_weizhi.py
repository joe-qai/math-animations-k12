# -*- coding: utf-8 -*-
"""确定位置：用数对表示位置（先列后行），用方向和距离确定位置。五年级下册「确定位置」。"""

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403

COLS, ROWS = 6, 4
CX, CY = -5.9, 1.65
DX, DY = 0.98, 1.0


def seat_xy(col: int, row: int) -> list[float]:
    return [CX + (col - 1) * DX, CY - (row - 1) * DY, 0]


class QuedingWeizhiScene(NarratedScene):
    lesson = "queding-weizhi"

    def construct(self):
        # ---------- 0. 教室里的座位 ----------
        self.section(0, "一句话说清坐在哪里")
        seats = VGroup()
        for r in range(1, ROWS + 1):
            for c in range(1, COLS + 1):
                seats.add(RoundedRectangle(corner_radius=0.06, width=0.7, height=0.62,
                                           stroke_color=DIM, stroke_width=1.2,
                                           fill_color=CHALK, fill_opacity=0.05
                                           ).move_to(seat_xy(c, r)))
        self.play(LaggedStart(*[FadeIn(s, scale=0.9) for s in seats], lag_ratio=0.03),
                  run_time=1.6)

        podium = txt("讲　台", size=22, color=GOLD).move_to([-3.5, 2.62, 0])
        self.play(FadeIn(podium), run_time=0.4)

        # 目标座位
        target = seat_xy(4, 3)
        mark = Circle(radius=0.5, color=GOLD, stroke_width=2.6).move_to(target)
        qmark = txt("?", size=30, color=GOLD).move_to(target)
        self.play(Create(mark), FadeIn(qmark), run_time=0.7)

        q1 = txt("教室里这么多座位", size=34, color=CHALK).move_to([3.9, 1.1, 0])
        q2 = txt("怎样说清谁坐在哪？", size=36, color=GOLD).move_to([3.9, 0.15, 0])
        self.play(Write(q1), run_time=0.6)
        self.play(Write(q2), run_time=0.6)

        q3 = txt("先要定一个标准", size=30, color=DIM).move_to([3.9, -1.0, 0])
        self.play(FadeIn(q3), run_time=0.5)
        self.finish_section()

        # ---------- 1. 先数列，再数行 ----------
        self.section(1, "竖排是列，横排是行")
        self.play(FadeOut(q1), FadeOut(q2), FadeOut(q3), FadeOut(mark), FadeOut(qmark),
                  run_time=0.4)

        cols_num = VGroup(*[
            txt(str(c), size=24, color=GOLD).move_to(seat_xy(c, ROWS)[:2] + [0])
            .shift(DOWN * 0.55)
            for c in range(1, COLS + 1)
        ])
        rows_num = VGroup(*[
            txt(str(r), size=24, color=BLUE).move_to(seat_xy(1, r)).shift(LEFT * 0.62)
            for r in range(1, ROWS + 1)
        ])
        self.play(LaggedStart(*[FadeIn(t, shift=UP * 0.08) for t in cols_num],
                              lag_ratio=0.12), run_time=1.2)
        self.play(LaggedStart(*[FadeIn(t, shift=RIGHT * 0.08) for t in rows_num],
                              lag_ratio=0.12), run_time=1.2)

        a1 = txt("竖排叫「列」", size=34, color=GOLD).move_to([3.9, 1.1, 0])
        a2 = txt("从前往后数「行」", size=34, color=BLUE).move_to([3.9, 0.15, 0])
        self.play(Write(a1), run_time=0.6)
        self.play(Write(a2), run_time=0.6)

        a3 = txt("列和行交叉的地方", size=30, color=CHALK).move_to([3.9, -0.9, 0])
        a4 = txt("就是一个座位", size=32, color=GREEN).move_to([3.9, -1.8, 0])
        self.play(FadeIn(a3), run_time=0.5)
        self.play(FadeIn(a4, shift=UP * 0.1), run_time=0.6)
        self.finish_section()

        # ---------- 2. 数对的写法 ----------
        self.section(2, "先写列，再写行")
        self.play(FadeOut(a1), FadeOut(a2), FadeOut(a3), FadeOut(a4), run_time=0.4)

        w1 = txt("第 3 列", size=40, color=GOLD).move_to([3.2, 1.45, 0])
        w2 = txt("第 2 行", size=40, color=BLUE).move_to([3.2, 0.65, 0])
        self.play(Write(w1), run_time=0.6)
        self.play(Write(w2), run_time=0.6)

        w3 = txt("写成", size=30, color=DIM).move_to([2.0, -0.25, 0])
        w4 = txt("(3, 2)", size=52, color=GREEN).move_to([4.4, -0.25, 0])
        self.play(FadeIn(w3), run_time=0.4)
        self.play(Write(w4), run_time=0.8)

        n1 = txt("先列后行，中间用逗号", size=28, color=CHALK).move_to([3.3, -1.2, 0])
        n2 = txt("外面加上括号", size=28, color=CHALK).move_to([3.3, -2.0, 0])
        self.play(FadeIn(n1), run_time=0.5)
        self.play(FadeIn(n2), run_time=0.5)
        self.finish_section()

        # ---------- 3. 在图上找到它 ----------
        self.section(3, "三逗号二，就是这个座位")
        self.play(FadeOut(w1), FadeOut(w2), FadeOut(w3), FadeOut(w4),
                  FadeOut(n1), FadeOut(n2), run_time=0.4)

        tgt = seat_xy(3, 2)
        ring = Circle(radius=0.52, color=GREEN, stroke_width=2.8).move_to(tgt)
        self.play(Create(ring), run_time=0.7)

        lab = txt("(3, 2)", size=30, color=GREEN).move_to([1.35, 0.65, 0])
        arr = Arrow(lab.get_left() + LEFT * 0.05, tgt + RIGHT * 0.5,
                    buff=0, color=GREEN, stroke_width=2.2, tip_length=0.14)
        self.play(FadeIn(lab), GrowArrow(arr), run_time=0.8)

        s1 = txt("第 3 列 第 2 行", size=36, color=CHALK).move_to([3.7, 1.1, 0])
        s2 = txt("列在前，行在后", size=34, color=GOLD).move_to([3.7, 0.15, 0])
        s3 = txt("一个数对，一个位置", size=30, color=GREEN).move_to([3.7, -0.9, 0])
        self.play(Write(s1), run_time=0.6)
        self.play(Write(s2), run_time=0.6)
        self.play(FadeIn(s3, shift=UP * 0.1), run_time=0.6)
        self.finish_section()

        # ---------- 4. 顺序不能反 ----------
        self.section(4, "顺序一反，位置就变了")
        self.play(FadeOut(lab), FadeOut(arr), FadeOut(s1), FadeOut(s2), FadeOut(s3),
                  run_time=0.5)

        tgt2 = seat_xy(2, 3)
        ring2 = Circle(radius=0.52, color=BLUE, stroke_width=2.8).move_to(tgt2)
        self.play(Create(ring2), run_time=0.7)

        l1 = txt("(3, 2)", size=30, color=GREEN).move_to([0.6, 1.4, 0])
        l2 = txt("(2, 3)", size=30, color=BLUE).move_to([0.6, 0.55, 0])
        self.play(FadeIn(l1), FadeIn(l2), run_time=0.6)

        p1 = txt("(3, 2)：第 3 列第 2 行", size=26, color=GREEN).move_to([3.5, -0.55, 0])
        p2 = txt("(2, 3)：第 2 列第 3 行", size=26, color=BLUE).move_to([3.5, -1.35, 0])
        self.play(FadeIn(p1), run_time=0.5)
        self.play(FadeIn(p2), run_time=0.5)

        warn = txt("两个位置完全不同", size=32, color=RED).move_to([0, -2.45, 0])
        self.play(FadeIn(warn), run_time=0.6)
        self.finish_section()

        # ---------- 5. 方向 + 距离 ----------
        self.section(5, "也可以用方向和距离")
        self.play(FadeOut(seats), FadeOut(cols_num), FadeOut(rows_num),
                  FadeOut(podium), FadeOut(ring), FadeOut(ring2),
                  FadeOut(l1), FadeOut(l2), FadeOut(p1), FadeOut(p2),
                  FadeOut(warn), run_time=0.6)

        origin = [-4.9, -1.1, 0]
        east = Arrow(origin, [-0.5, -1.1, 0], buff=0, color=DIM,
                     stroke_width=2.4, tip_length=0.16)
        north = Arrow(origin, [-4.9, 1.55, 0], buff=0, color=DIM,
                      stroke_width=2.4, tip_length=0.16)
        elab = txt("东", size=26, color=DIM).move_to([-0.15, -1.1, 0])
        nlab = txt("北", size=26, color=DIM).move_to([-4.9, 1.9, 0])
        self.play(Create(east), Create(north), run_time=0.8)
        self.play(FadeIn(elab), FadeIn(nlab), run_time=0.4)

        ang = np.radians(30)
        length = 3.4
        tip = [origin[0] + length * np.cos(ang), origin[1] + length * np.sin(ang), 0]
        path = Arrow(origin, tip, buff=0, color=GOLD, stroke_width=3.2, tip_length=0.2)
        self.play(GrowArrow(path), run_time=0.9)

        arc = Arc(radius=1.1, start_angle=0, angle=ang, arc_center=origin,
                  color=GOLD, stroke_width=2)
        ang_lab = txt("30°", size=24, color=GOLD).move_to([-3.55, -0.72, 0])
        self.play(Create(arc), FadeIn(ang_lab), run_time=0.7)

        dist = txt("200 米", size=26, color=GOLD)
        dist.move_to([(origin[0] + tip[0]) / 2 - 0.1, (origin[1] + tip[1]) / 2 + 0.6, 0])
        self.play(FadeIn(dist), run_time=0.5)

        d1 = txt("从起点出发", size=32, color=CHALK).move_to([3.5, 1.0, 0])
        d2 = txt("东偏北 30°", size=36, color=GOLD).move_to([3.5, 0.1, 0])
        d3 = txt("走 200 米", size=36, color=GREEN).move_to([3.5, -0.8, 0])
        self.play(Write(d1), run_time=0.5)
        self.play(Write(d2), run_time=0.6)
        self.play(Write(d3), run_time=0.6)
        self.finish_section()

        # ---------- 6. 口诀 ----------
        self.section(6, "数对先列后行")
        self.play(FadeOut(east), FadeOut(north), FadeOut(elab), FadeOut(nlab),
                  FadeOut(path), FadeOut(arc), FadeOut(ang_lab), FadeOut(dist),
                  FadeOut(d1), FadeOut(d2), FadeOut(d3), run_time=0.6)

        k1 = txt("数对", size=44, color=GOLD).move_to([-4.2, 1.25, 0])
        k2 = txt("先列后行", size=44, color=CHALK).move_to([0, 1.25, 0])
        k3 = txt("括号逗号", size=44, color=GREEN).move_to([4.2, 1.25, 0])
        self.play(LaggedStart(*[FadeIn(t, shift=UP * 0.12) for t in (k1, k2, k3)],
                              lag_ratio=0.25), run_time=1.3)

        big1 = txt("(3, 2)", size=54, color=GOLD).move_to([-2.4, -0.1, 0])
        big2 = txt("≠", size=44, color=RED).move_to([0, -0.1, 0])
        big3 = txt("(2, 3)", size=54, color=BLUE).move_to([2.4, -0.1, 0])
        self.play(Write(big1), Write(big2), Write(big3), run_time=1.0)

        fin = txt("数对定位置，先列后行不能反", size=28, color=DIM).move_to([0, -1.5, 0])
        self.play(FadeIn(fin, shift=UP * 0.1), run_time=0.6)
        self.finish_section()

        self.play(FadeOut(k1), FadeOut(k2), FadeOut(k3),
                  FadeOut(big1), FadeOut(big2), FadeOut(big3), FadeOut(fin),
                  run_time=0.6)