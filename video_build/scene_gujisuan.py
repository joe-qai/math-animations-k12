# -*- coding: utf-8 -*-
"""估算：看成整十整百，先算个大概。三年级下册「估算」。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


def item(x: float, y: float, label: str, price: str, color: str = CHALK) -> VGroup:
    box = RoundedRectangle(corner_radius=0.12, width=0.78, height=0.78,
                           stroke_color=color, stroke_width=1.8,
                           fill_color=color, fill_opacity=0.08)
    box.move_to([x, y, 0])
    t = txt(label, size=34, color=color).move_to([x, y, 0])
    p = txt(price, size=30, color=GOLD).next_to(box, RIGHT, buff=0.28)
    return VGroup(box, t, p)


class GujisuanScene(NarratedScene):
    lesson = "gujisuan"

    def construct(self):
        # ---------- 0. 超市里估一估 ----------
        self.section(0, "买东西，先估一估")
        a = item(-5.6, 1.55, "书", "198 元", BLUE)
        b = item(-5.6, 0.35, "包", "305 元", GREEN)
        c = item(-5.6, -0.85, "笔", "88 元", GOLD)
        for g in (a, b, c):
            self.play(FadeIn(g, shift=RIGHT * 0.1), run_time=0.45)

        q1 = txt("三样东西", size=34, color=CHALK).move_to([3.5, 1.5, 0])
        q2 = txt("大约要花多少钱？", size=38, color=GOLD).move_to([3.5, 0.55, 0])
        q3 = txt("不用算到分，估一估", size=30, color=DIM).move_to([3.5, -0.45, 0])
        self.play(Write(q1), run_time=0.6)
        self.play(Write(q2), run_time=0.7)
        self.play(FadeIn(q3), run_time=0.5)
        self.finish_section()

        # ---------- 1. 看成整十、整百 ----------
        self.section(1, "看成接近的整十、整百")
        self.play(FadeOut(q1), FadeOut(q2), FadeOut(q3), run_time=0.4)
        self.play(FadeOut(a), FadeOut(b), FadeOut(c), run_time=0.4)

        rows = [
            ("198", "200", GOLD, 1.65),
            ("305", "300", BLUE, 0.35),
            ("88", "90", GREEN, -0.95),
        ]
        groups = []
        for src, dst, col, y in rows:
            left = txt(src, size=44, color=CHALK).move_to([-5.6, y, 0])
            arrow = Arrow([-4.9, y, 0], [-3.9, y, 0], buff=0, color=col,
                          stroke_width=3, tip_length=0.16)
            right = txt(dst, size=44, color=col).move_to([-3.3, y, 0])
            g = VGroup(left, arrow, right)
            groups.append(g)
            self.play(GrowArrow(arrow), FadeIn(left), FadeIn(right), run_time=0.5)

        d1 = txt("把不整齐的数", size=34, color=CHALK).move_to([3.4, 1.1, 0])
        d2 = txt("看成整十、整百", size=40, color=GOLD).move_to([3.4, 0.15, 0])
        d3 = txt("算起来就快了", size=34, color=GREEN).move_to([3.4, -0.85, 0])
        self.play(Write(d1), run_time=0.6)
        self.play(Write(d2), run_time=0.7)
        self.play(FadeIn(d3, shift=UP * 0.1), run_time=0.6)
        self.finish_section()

        # ---------- 2. 198 + 305 ----------
        self.section(2, "一百九十八加三百零五")
        self.play(*[FadeOut(g) for g in groups], FadeOut(d1), FadeOut(d2), FadeOut(d3),
                  run_time=0.5)

        e1 = txt("198 + 305", size=54, color=CHALK).move_to([0, 1.55, 0])
        e2 = txt("≈ 200 + 300", size=54, color=GOLD).move_to([0, 0.45, 0])
        e3 = txt("= 500", size=54, color=GREEN).move_to([0, -0.65, 0])
        self.play(Write(e1), run_time=0.8)
        self.play(Write(e2), run_time=0.8)
        self.play(Write(e3), run_time=0.7)

        tip = txt("≈ 读作「约等于」，不是正好相等", size=28, color=DIM).move_to([0, -1.9, 0])
        self.play(FadeIn(tip, shift=UP * 0.1), run_time=0.6)
        self.finish_section()

        # ---------- 3. 乘法也能估 ----------
        self.section(3, "乘法也能估")
        self.play(FadeOut(e1), FadeOut(e2), FadeOut(e3), FadeOut(tip), run_time=0.5)

        m1 = txt("每盒 29 元，买 6 盒", size=36, color=CHALK).move_to([0, 1.6, 0])
        m2 = txt("29 × 6 ≈ 30 × 6", size=48, color=GOLD).move_to([0, 0.5, 0])
        m3 = txt("= 180（元）", size=48, color=GREEN).move_to([0, -0.6, 0])
        self.play(Write(m1), run_time=0.7)
        self.play(Write(m2), run_time=0.8)
        self.play(Write(m3), run_time=0.7)

        m4 = txt("29 估成 30，估大了，所以实际不到 180 元", size=28, color=DIM)
        m4.move_to([0, -1.9, 0])
        self.play(FadeIn(m4, shift=UP * 0.1), run_time=0.6)
        self.finish_section()

        # ---------- 4. 估大还是估小 ----------
        self.section(4, "估大还是估小，看你要干什么")
        self.play(FadeOut(m1), FadeOut(m2), FadeOut(m3), FadeOut(m4), run_time=0.5)

        k1 = label_box("带钱够不够", size=34, color=GOLD).move_to([-3.4, 0.9, 0])
        k2 = txt("→ 往大估，留出余量", size=34, color=GOLD).move_to([2.6, 0.9, 0])
        k3 = label_box("只看结果范围", size=34, color=GREEN).move_to([-3.4, -0.6, 0])
        k4 = txt("→ 估大估小都行", size=34, color=GREEN).move_to([2.6, -0.6, 0])
        self.play(FadeIn(k1, shift=UP * 0.1), run_time=0.5)
        self.play(FadeIn(k2), run_time=0.5)
        self.play(FadeIn(k3, shift=UP * 0.1), run_time=0.5)
        self.play(FadeIn(k4), run_time=0.5)

        note = txt("估的方向，要跟问题对上", size=30, color=DIM).move_to([0, -2.1, 0])
        self.play(FadeIn(note), run_time=0.5)
        self.finish_section()

        # ---------- 5. 给精确计算把关 ----------
        self.section(5, "估算给精确计算把关")
        self.play(FadeOut(k1), FadeOut(k2), FadeOut(k3), FadeOut(k4), FadeOut(note),
                  run_time=0.5)

        g1 = txt("算出：127", size=48, color=CHALK).move_to([-3.6, 0.75, 0])
        g2 = txt("估算：100 左右", size=44, color=GOLD).move_to([3.2, 0.75, 0])
        self.play(Write(g1), run_time=0.7)
        self.play(Write(g2), run_time=0.7)

        ok = txt("✓ 在一个范围里，答案合理", size=40, color=GREEN).move_to([0, -0.7, 0])
        self.play(FadeIn(ok, shift=UP * 0.1), run_time=0.7)

        bad = txt("要是算成 1270，就明显不对了", size=28, color=RED).move_to([0, -1.9, 0])
        self.play(FadeIn(bad), run_time=0.6)
        self.finish_section()

        # ---------- 6. 口诀 ----------
        self.section(6, "看成整十整百，先算个大概")
        self.play(FadeOut(g1), FadeOut(g2), FadeOut(ok), FadeOut(bad), run_time=0.5)

        f1 = txt("看成整十、整百", size=48, color=GOLD).move_to([0, 1.35, 0])
        f2 = txt("先算个大概", size=48, color=CHALK).move_to([0, 0.25, 0])
        f3 = txt("再用范围判断对错", size=48, color=GREEN).move_to([0, -0.85, 0])
        self.play(Write(f1), run_time=0.8)
        self.play(Write(f2), run_time=0.7)
        self.play(Write(f3), run_time=0.8)

        fin = txt("估算，是算得快、看得准的本领", size=28, color=DIM).move_to([0, -2.1, 0])
        self.play(FadeIn(fin, shift=UP * 0.1), run_time=0.6)
        self.finish_section()

        self.play(FadeOut(f1), FadeOut(f2), FadeOut(f3), FadeOut(fin), run_time=0.6)