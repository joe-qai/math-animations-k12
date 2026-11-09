# -*- coding: utf-8 -*-
"""探索规律：积的变化规律、商不变规律。四年级上册「探索与发现」。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


class TansuoGuilvScene(NarratedScene):
    lesson = "tansuo-guilv"

    def construct(self):
        # ---------- 0. 先算三道题 ----------
        self.section(0, "先算三道题")
        e1 = txt("3 × 2 = 6", size=50, color=CHALK).move_to([-3.3, 1.55, 0])
        e2 = txt("3 × 4 = 12", size=50, color=CHALK).move_to([-3.3, 0.35, 0])
        e3 = txt("3 × 8 = 24", size=50, color=CHALK).move_to([-3.3, -0.85, 0])
        self.play(Write(e1), run_time=0.7)
        self.play(Write(e2), run_time=0.7)
        self.play(Write(e3), run_time=0.7)

        q1 = txt("三个结果", size=36, color=CHALK).move_to([3.9, 1.25, 0])
        q2 = txt("有没有关系？", size=40, color=GOLD).move_to([3.9, 0.3, 0])
        self.play(Write(q1), run_time=0.6)
        self.play(Write(q2), run_time=0.6)

        hint = txt("盯着数字看", size=30, color=DIM).move_to([3.9, -0.9, 0])
        self.play(FadeIn(hint), run_time=0.5)
        self.finish_section()

        # ---------- 1. 三个结果成倍变 ----------
        self.section(1, "六、十二、二十四")
        self.play(FadeOut(e1), FadeOut(e2), FadeOut(e3),
                  FadeOut(q1), FadeOut(q2), FadeOut(hint), run_time=0.4)

        # 结果单独拉出来，做成条
        bars = VGroup()
        for i, (val, w, col) in enumerate(((6, 1.2, GOLD), (12, 2.4, BLUE), (24, 4.8, GREEN))):
            bar = Rectangle(width=w, height=0.34, stroke_width=0,
                            fill_color=col, fill_opacity=0.55)
            bar.move_to([-5.9 + w / 2, 1.5 - i * 0.95, 0])
            bars.add(bar)
        self.play(*(FadeIn(b) for b in bars), run_time=0.9)

        lab = VGroup(
            txt("6", size=30, color=GOLD).next_to(bars[0], RIGHT, buff=0.2),
            txt("12", size=30, color=BLUE).next_to(bars[1], RIGHT, buff=0.2),
            txt("24", size=30, color=GREEN).next_to(bars[2], RIGHT, buff=0.2),
        )
        self.play(FadeIn(lab), run_time=0.5)

        r1 = txt("一个比一个大一倍", size=36, color=CHALK).move_to([4.2, 1.5, 0])
        r2 = txt("6 → 12 → 24", size=40, color=BLUE).move_to([4.2, 0.55, 0])
        r3 = txt("每次都乘 2", size=36, color=GREEN).move_to([4.2, -0.4, 0])
        self.play(Write(r1), run_time=0.6)
        self.play(Write(r2), run_time=0.6)
        self.play(FadeIn(r3, shift=UP * 0.1), run_time=0.6)
        self.finish_section()

        # ---------- 2. 谁在变，谁没变 ----------
        self.section(2, "一个因数没变，另一个在变")
        self.play(FadeOut(bars), FadeOut(lab), FadeOut(r1), FadeOut(r2), FadeOut(r3),
                  FadeOut(e1), FadeOut(e2), FadeOut(e3), run_time=0.5)

        c1 = txt("3 × 2", size=44, color=CHALK).move_to([-4.4, 1.5, 0])
        c2 = txt("3 × 4", size=44, color=CHALK).move_to([-4.4, 0.5, 0])
        c3 = txt("3 × 8", size=44, color=CHALK).move_to([-4.4, -0.5, 0])
        self.play(FadeIn(c1), FadeIn(c2), FadeIn(c3), run_time=0.6)

        ring = VGroup(*[
            Circle(radius=0.26, color=GOLD, stroke_width=2.4).move_to(c[0].get_center())
            for c in (c1, c2, c3)
        ])
        self.play(LaggedStart(*[Create(c) for c in ring], lag_ratio=0.2), run_time=1.0)

        s1 = txt("第一个因数都是 3", size=34, color=GOLD).move_to([2.4, 1.5, 0])
        s2 = txt("第二个：2 → 4 → 8", size=34, color=BLUE).move_to([2.4, 0.45, 0])
        s3 = txt("乘了 2，又乘了 4", size=34, color=BLUE).move_to([2.4, -0.55, 0])
        self.play(Write(s1), run_time=0.6)
        self.play(Write(s2), run_time=0.7)
        self.play(FadeIn(s3), run_time=0.5)

        s4 = txt("结果：6 → 12 → 24", size=34, color=GREEN).move_to([2.4, -1.65, 0])
        self.play(FadeIn(s4, shift=UP * 0.1), run_time=0.6)
        self.finish_section()

        # ---------- 3. 积也跟着乘 ----------
        self.section(3, "因数乘几，积就乘几")
        self.play(FadeOut(c1), FadeOut(c2), FadeOut(c3), FadeOut(ring),
                  FadeOut(s1), FadeOut(s2), FadeOut(s3), FadeOut(s4), run_time=0.5)

        t1 = txt("2 × 2 = 4", size=44, color=BLUE).move_to([-3.2, 1.5, 0])
        t2 = txt("6 × 2 = 12", size=44, color=GREEN).move_to([3.2, 1.5, 0])
        t3 = txt("4 × 2 = 8", size=44, color=BLUE).move_to([-3.2, 0.35, 0])
        t4 = txt("12 × 2 = 24", size=44, color=GREEN).move_to([3.2, 0.35, 0])
        self.play(Write(t1), run_time=0.6)
        self.play(Write(t2), run_time=0.6)
        self.play(Write(t3), run_time=0.6)
        self.play(Write(t4), run_time=0.6)

        same = VGroup(
            Arrow([-0.9, 1.5, 0], [0.9, 1.5, 0], buff=0, color=GOLD,
                  stroke_width=3, tip_length=0.18),
            Arrow([-0.9, 0.35, 0], [0.9, 0.35, 0], buff=0, color=GOLD,
                  stroke_width=3, tip_length=0.18),
        )
        self.play(Create(same), run_time=0.7)

        k = txt("因数 ×2，积也 ×2", size=40, color=GOLD).move_to([0, -1.1, 0])
        self.play(Write(k), run_time=0.7)

        k2 = txt("除以几，积也跟着除以几", size=30, color=DIM).move_to([0, -2.1, 0])
        self.play(FadeIn(k2), run_time=0.5)
        self.finish_section()

        # ---------- 4. 积的变化规律 ----------
        self.section(4, "积的变化规律")
        self.play(FadeOut(t1), FadeOut(t2), FadeOut(t3), FadeOut(t4),
                  FadeOut(same), FadeOut(k), FadeOut(k2), run_time=0.5)

        rule1 = label_box("一个因数不变", size=40, color=GOLD).move_to([0, 1.15, 0])
        rule2 = txt("另一个因数乘几，积就乘几", size=44, color=CHALK).move_to([0, 0.0, 0])
        rule3 = txt("除以几，积也除以几", size=40, color=GREEN).move_to([0, -1.15, 0])
        self.play(FadeIn(rule1, shift=UP * 0.1), run_time=0.7)
        self.play(Write(rule2), run_time=0.8)
        self.play(Write(rule3), run_time=0.7)

        note = txt("这条规律，就是简便计算的依据", size=28, color=DIM).move_to([0, -2.2, 0])
        self.play(FadeIn(note), run_time=0.5)
        self.finish_section()

        # ---------- 5. 商不变的规律 ----------
        self.section(5, "除法里也有规律")
        self.play(FadeOut(rule1), FadeOut(rule2), FadeOut(rule3), FadeOut(note),
                  run_time=0.5)

        d1 = txt("24 ÷ 6 = 4", size=46, color=CHALK).move_to([-3.4, 1.55, 0])
        d2 = txt("48 ÷ 12 = 4", size=46, color=CHALK).move_to([-3.4, 0.5, 0])
        d3 = txt("96 ÷ 24 = 4", size=46, color=CHALK).move_to([-3.4, -0.55, 0])
        self.play(Write(d1), run_time=0.6)
        self.play(Write(d2), run_time=0.6)
        self.play(Write(d3), run_time=0.6)

        h1 = txt("被除数和除数", size=32, color=BLUE).move_to([3.6, 1.35, 0])
        h2 = txt("同时乘 2", size=38, color=BLUE).move_to([3.6, 0.45, 0])
        h3 = txt("商都是 4，没变", size=34, color=GREEN).move_to([3.6, -0.55, 0])
        self.play(Write(h1), run_time=0.6)
        self.play(FadeIn(h2, shift=UP * 0.1), run_time=0.5)
        self.play(Write(h3), run_time=0.6)

        h4 = txt("被除数和除数同时乘或除以相同的数，商不变", size=28, color=GOLD)
        h4.move_to([0, -1.75, 0])
        self.play(FadeIn(h4, shift=UP * 0.1), run_time=0.6)
        self.finish_section()

        # ---------- 6. 口诀 ----------
        self.section(6, "先算，再比，找规律")
        self.play(FadeOut(d1), FadeOut(d2), FadeOut(d3), FadeOut(h1),
                  FadeOut(h2), FadeOut(h3), FadeOut(h4), run_time=0.5)

        big1 = txt("先算一算", size=46, color=CHALK).move_to([-4.1, 1.2, 0])
        big2 = txt("再比一比", size=46, color=CHALK).move_to([0, 1.2, 0])
        big3 = txt("找规律", size=46, color=GOLD).move_to([4.1, 1.2, 0])
        self.play(LaggedStart(*[FadeIn(t, shift=UP * 0.1) for t in (big1, big2, big3)],
                              lag_ratio=0.25), run_time=1.3)

        s1 = txt("看谁在变", size=40, color=GREEN).move_to([-2.6, -0.35, 0])
        s2 = txt("看谁没变", size=40, color=BLUE).move_to([2.6, -0.35, 0])
        self.play(Write(s1), run_time=0.6)
        self.play(Write(s2), run_time=0.6)

        fin = txt("规律，就藏在一组算式的变化里", size=28, color=DIM).move_to([0, -2.0, 0])
        self.play(FadeIn(fin, shift=UP * 0.1), run_time=0.6)
        self.finish_section()

        self.play(FadeOut(big1), FadeOut(big2), FadeOut(big3),
                  FadeOut(s1), FadeOut(s2), FadeOut(fin), run_time=0.6)