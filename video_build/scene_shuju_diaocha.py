# -*- coding: utf-8 -*-
"""数据收集与整理：调查、正字记录、统计表、条形图。三年级下册「数据的整理和表示」。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403

SPORTS = ["跳绳", "足球", "篮球", "乒乓球"]
COUNTS = [12, 9, 7, 6]
COLORS = [GOLD, BLUE, GREEN, ORANGE]

X0, X1 = -5.9, -1.4
Y0, Y1 = -1.6, 2.1
STEP = (X1 - X0) / 4


def bar_y(v: float) -> float:
    return Y0 + v / 14.0 * (Y1 - Y0)


class ShujuDiaochaScene(NarratedScene):
    lesson = "shuju-diaocha"

    def construct(self):
        # ---------- 0. 想知道最喜欢哪项运动 ----------
        self.section(0, "先要收集数据")
        boxes = VGroup(*[
            label_box(name, size=34, color=c).move_to([-5.0 + i * 2.5, 1.35, 0])
            for i, (name, c) in enumerate(zip(SPORTS, COLORS))
        ])
        self.play(LaggedStart(*[FadeIn(b, shift=UP * 0.12) for b in boxes],
                              lag_ratio=0.15), run_time=1.3)

        q1 = txt("全班同学", size=34, color=CHALK).move_to([0, 0.05, 0])
        q2 = txt("最喜欢哪项运动？", size=40, color=GOLD).move_to([0, -0.95, 0])
        self.play(Write(q1), run_time=0.5)
        self.play(Write(q2), run_time=0.6)

        q3 = txt("先调查，把数据收上来", size=30, color=DIM).move_to([0, -2.0, 0])
        self.play(FadeIn(q3, shift=UP * 0.1), run_time=0.6)
        self.finish_section()

        # ---------- 1. 举手、逐个问 ----------
        self.section(1, "举手调查，一个个记下来")
        self.play(FadeOut(boxes), FadeOut(q1), FadeOut(q2), FadeOut(q3), run_time=0.5)

        # 一排小手
        hands = VGroup()
        for i in range(8):
            x = -5.6 + i * 1.5
            hands.add(VGroup(
                Line([x, -0.4, 0], [x, 0.55, 0], color=CHALK, stroke_width=3),
                Line([x, 0.55, 0], [x - 0.16, 0.95, 0], color=CHALK, stroke_width=3),
                Line([x, 0.55, 0], [x + 0.16, 0.95, 0], color=CHALK, stroke_width=3),
                Line([x, 0.55, 0], [x, 1.1, 0], color=CHALK, stroke_width=3),
            ))
        self.play(LaggedStart(*[Create(h) for h in hands], lag_ratio=0.12), run_time=1.5)

        r1 = txt("可以举手调查", size=34, color=GOLD).move_to([3.6, 0.9, 0])
        r2 = txt("也可以一个一个问", size=34, color=CHALK).move_to([3.6, -0.1, 0])
        r3 = txt("把每个人的选择记下来", size=30, color=DIM).move_to([3.6, -1.1, 0])
        self.play(Write(r1), run_time=0.6)
        self.play(Write(r2), run_time=0.6)
        self.play(FadeIn(r3), run_time=0.5)
        self.finish_section()

        # ---------- 2. 正字记录 ----------
        self.section(2, "画正字，五笔五个人")
        self.play(FadeOut(hands), FadeOut(r1), FadeOut(r2), FadeOut(r3), run_time=0.5)

        big = txt("正", size=120, color=GOLD).move_to([-4.4, 0.35, 0])
        self.play(Write(big), run_time=1.2)

        n1 = txt("一个正字 = 5 笔", size=36, color=CHALK).move_to([2.9, 1.25, 0])
        n2 = txt("正好记 5 个人", size=36, color=GREEN).move_to([2.9, 0.3, 0])
        n3 = txt("数正字，又快又清楚", size=30, color=DIM).move_to([2.9, -0.7, 0])
        self.play(Write(n1), run_time=0.6)
        self.play(Write(n2), run_time=0.6)
        self.play(FadeIn(n3), run_time=0.5)

        # 各种运动的记录
        note = txt("跳绳：正 正 再加 2 笔　足球：正 再加 4 笔", size=26, color=CHALK)
        note.move_to([0, -1.95, 0])
        self.play(FadeIn(note), run_time=0.5)
        self.finish_section()

        # ---------- 3. 整理成统计表 ----------
        self.section(3, "整理成统计表")
        self.play(FadeOut(big), FadeOut(n1), FadeOut(n2), FadeOut(n3), FadeOut(note),
                  run_time=0.5)

        rows = VGroup()
        head = VGroup(
            txt("运动项目", size=28, color=GOLD).move_to([-4.6, 1.55, 0]),
            txt("人数", size=28, color=GOLD).move_to([-1.5, 1.55, 0]),
        )
        rows.add(head)
        for i, (name, cnt, c) in enumerate(zip(SPORTS, COUNTS, COLORS)):
            y = 0.85 - i * 0.72
            rows.add(VGroup(
                txt(name, size=28, color=c).move_to([-4.6, y, 0]),
                txt(str(cnt), size=28, color=CHALK).move_to([-1.5, y, 0]),
            ))
        lines = VGroup(*[
            Line([-5.7, 1.15 - i * 0.72, 0], [-0.6, 1.15 - i * 0.72, 0],
                 color=DIM, stroke_width=1.2)
            for i in range(5)
        ])
        self.play(Create(lines), run_time=0.8)
        self.play(LaggedStart(*[FadeIn(r, shift=RIGHT * 0.08) for r in rows],
                              lag_ratio=0.12), run_time=1.3)

        tb1 = txt("统计表", size=40, color=GOLD).move_to([3.5, 1.2, 0])
        tb2 = txt("每项有多少人", size=34, color=CHALK).move_to([3.5, 0.25, 0])
        tb3 = txt("一眼就能看清", size=34, color=GREEN).move_to([3.5, -0.7, 0])
        self.play(Write(tb1), run_time=0.6)
        self.play(Write(tb2), run_time=0.6)
        self.play(FadeIn(tb3), run_time=0.5)
        self.finish_section()

        # ---------- 4. 画成条形图 ----------
        self.section(4, "画成条形图，比一比")
        self.play(FadeOut(rows), FadeOut(lines), FadeOut(tb1), FadeOut(tb2),
                  FadeOut(tb3), run_time=0.5)

        axes = VGroup(
            Arrow([X0, Y0, 0], [X1 + 0.3, Y0, 0], buff=0, color=DIM,
                  stroke_width=2, tip_length=0.14),
            Arrow([X0, Y0, 0], [X0, Y1 + 0.25, 0], buff=0, color=DIM,
                  stroke_width=2, tip_length=0.14),
        )
        self.play(Create(axes), run_time=0.8)

        bars = VGroup()
        names = VGroup()
        for i, (cnt, c) in enumerate(zip(COUNTS, COLORS)):
            x = X0 + STEP * (i + 0.5)
            y = bar_y(cnt)
            bars.add(Rectangle(width=0.62, height=max(0.05, y - Y0), stroke_width=0,
                               fill_color=c, fill_opacity=0.62
                               ).move_to([x, (Y0 + y) / 2, 0]))
            names.add(txt(SPORTS[i], size=20, color=DIM).move_to([x, Y0 - 0.32, 0]))
        self.play(LaggedStart(*[GrowFromEdge(b, DOWN) for b in bars], lag_ratio=0.14),
                  run_time=1.6)
        self.play(LaggedStart(*[FadeIn(t) for t in names], lag_ratio=0.1), run_time=0.8)

        h1 = txt("直条越高", size=36, color=CHALK).move_to([3.5, 1.1, 0])
        h2 = txt("人数越多", size=36, color=GOLD).move_to([3.5, 0.15, 0])
        h3 = txt("跳绳最受欢迎", size=32, color=GREEN).move_to([3.5, -0.85, 0])
        self.play(Write(h1), run_time=0.6)
        self.play(Write(h2), run_time=0.6)
        self.play(FadeIn(h3, shift=UP * 0.1), run_time=0.6)
        self.finish_section()

        # ---------- 5. 数据要真实 ----------
        self.section(5, "不漏记、不重记")
        self.play(FadeOut(axes), FadeOut(bars), FadeOut(names),
                  FadeOut(h1), FadeOut(h2), FadeOut(h3), run_time=0.6)

        e1 = txt("✗ 漏记一个人", size=36, color=RED).move_to([0, 1.5, 0])
        e2 = txt("✗ 同一个人记两次", size=36, color=RED).move_to([0, 0.5, 0])
        self.play(Write(e1), run_time=0.7)
        self.play(Write(e2), run_time=0.7)

        e3 = txt("✓ 一个人只算一次", size=40, color=GREEN).move_to([0, -0.55, 0])
        self.play(FadeIn(e3, shift=UP * 0.1), run_time=0.7)

        e4 = txt("数据真实，结论才可信", size=30, color=DIM).move_to([0, -1.7, 0])
        self.play(FadeIn(e4), run_time=0.5)
        self.finish_section()

        # ---------- 6. 三步 ----------
        self.section(6, "收集、整理、分析")
        self.play(FadeOut(e1), FadeOut(e2), FadeOut(e3), FadeOut(e4), run_time=0.5)

        k1 = label_box("收集", size=42, color=GOLD).move_to([-4.0, 1.2, 0])
        k2 = label_box("整理", size=42, color=BLUE).move_to([0, 1.2, 0])
        k3 = label_box("分析", size=42, color=GREEN).move_to([4.0, 1.2, 0])
        self.play(LaggedStart(*[FadeIn(k, shift=UP * 0.12) for k in (k1, k2, k3)],
                              lag_ratio=0.25), run_time=1.3)

        big = txt("数据自己会说话", size=46, color=CHALK).move_to([0, -0.2, 0])
        self.play(Write(big), run_time=0.9)

        fin = txt("先调查，再整理，最后看结论", size=28, color=DIM).move_to([0, -1.5, 0])
        self.play(FadeIn(fin, shift=UP * 0.1), run_time=0.6)
        self.finish_section()

        self.play(FadeOut(k1), FadeOut(k2), FadeOut(k3), FadeOut(big), FadeOut(fin),
                  run_time=0.6)