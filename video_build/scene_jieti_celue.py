# -*- coding: utf-8 -*-
"""解决问题的策略：鸡兔同笼 + 植树问题。四年级下册「解决问题的策略」。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


def head(x: float, y: float, color: str) -> VGroup:
    return VGroup(
        Circle(radius=0.30, stroke_width=2, stroke_color=color,
               fill_color=color, fill_opacity=0.14).move_to([x, y, 0]),
        txt("?", size=24, color=color).move_to([x, y, 0]),
    )


def legs(x: float, y: float, count: int, color: str) -> VGroup:
    g = VGroup()
    xs = [-0.17, -0.06, 0.06, 0.17] if count == 4 else [-0.09, 0.09]
    for dx in xs:
        g.add(Line([x + dx, y - 0.30, 0], [x + dx, y - 0.55, 0],
                   color=color, stroke_width=3))
    return g


def tree(x: float, y: float, color: str = GREEN) -> VGroup:
    return VGroup(
        Triangle(stroke_width=0, fill_color=color, fill_opacity=0.9)
        .scale(0.2).move_to([x, y + 0.2, 0]),
        Line([x, y, 0], [x, y + 0.1, 0], color=GOLD, stroke_width=4),
    )


def road(y: float, planted: tuple[bool, ...], half: float = 3.6,
         cx: float = -1.8) -> VGroup:
    g = VGroup(Line([cx - half, y, 0], [cx + half, y, 0], color=DIM, stroke_width=2))
    for k, on in enumerate(planted):
        x = cx - half + k * half / 2
        if on:
            g.add(tree(x, y))
        else:
            g.add(Circle(radius=0.09, color=DIM, stroke_width=1.6).move_to([x, y, 0]))
    return g


class JietiCelueScene(NarratedScene):
    lesson = "jieti-celue"

    def construct(self):
        # ---------- 0. 生活问题 ----------
        self.section(0, "8 个头，26 只脚")

        heads = VGroup(*[head(-5.9 + i * 0.96, 1.5, CHALK) for i in range(8)])
        self.play(LaggedStart(*[FadeIn(h, scale=0.7) for h in heads],
                              lag_ratio=0.08), run_time=1.2)
        lab1 = txt("8 个头", size=32, color=GOLD).move_to([3.75, 2.15, 0])
        lab2 = txt("26 只脚", size=32, color=BLUE).move_to([3.75, 1.5, 0])
        self.play(FadeIn(lab1), run_time=0.4)
        self.play(FadeIn(lab2), run_time=0.4)

        q = txt("鸡和兔各有多少只？", size=40, color=CHALK).move_to([0, -0.4, 0])
        eq = txt("鸡 + 兔 = 8", size=34, color=DIM).move_to([0, -1.5, 0])
        self.play(FadeIn(q, shift=UP * 0.1), run_time=0.7)
        self.play(FadeIn(eq), run_time=0.5)
        self.finish_section()

        # ---------- 1. 假设全是鸡 ----------
        self.section(1, "假设全是鸡：只有 16 只脚")
        self.play(FadeOut(q), FadeOut(eq), FadeOut(lab1), FadeOut(lab2), run_time=0.5)
        self.play(*[h.animate.set_color(GOLD) for h in heads], run_time=0.8)

        leg_groups = VGroup(*[legs(-5.9 + i * 0.96, 1.5, 2, GOLD) for i in range(8)])
        self.play(LaggedStart(*[FadeIn(lg, shift=DOWN * 0.05) for lg in leg_groups],
                              lag_ratio=0.06), run_time=1.0)

        a1 = txt("8 × 2 = 16 只脚", size=40, color=GOLD).move_to([3.75, 2.15, 0])
        a2 = txt("26 − 16 = 10", size=40, color=RED).move_to([3.75, 1.2, 0])
        a3 = txt("少了 10 只脚", size=34, color=RED).move_to([3.75, 0.3, 0])
        self.play(Write(a1), run_time=0.7)
        self.play(Write(a2), run_time=0.6)
        self.play(FadeIn(a3, shift=UP * 0.1), run_time=0.5)
        self.finish_section()

        # ---------- 2. 换兔 ----------
        self.section(2, "每换 1 只兔，多 2 只脚")
        self.play(FadeOut(a1), FadeOut(a2), FadeOut(a3), run_time=0.4)

        self.play(FadeOut(leg_groups[3:8]), run_time=0.3)
        rabbit_legs = VGroup()
        for i in range(3, 8):
            lg = legs(-5.9 + i * 0.96, 1.5, 4, BLUE)
            rabbit_legs.add(lg)
            self.play(heads[i].animate.set_color(BLUE), FadeIn(lg), run_time=0.28)

        b1 = txt("10 ÷ 2 = 5 只兔", size=42, color=BLUE).move_to([3.75, 2.15, 0])
        b2 = txt("8 − 5 = 3 只鸡", size=42, color=GOLD).move_to([3.75, 1.2, 0])
        b3 = txt("换 5 次，正好补上 10 只脚", size=28, color=GREEN).move_to([3.75, 0.3, 0])
        self.play(Write(b1), run_time=0.8)
        self.play(Write(b2), run_time=0.8)
        self.play(FadeIn(b3), run_time=0.5)
        self.finish_section()

        # ---------- 3. 验算 ----------
        self.section(3, "验算：20 + 6 = 26")
        self.play(FadeOut(b1), FadeOut(b2), FadeOut(b3), run_time=0.4)

        c1 = txt("兔：5 × 4 = 20 只脚", size=38, color=BLUE).move_to([3.75, 2.1, 0])
        c2 = txt("鸡：3 × 2 = 6 只脚", size=38, color=GOLD).move_to([3.75, 1.1, 0])
        c3 = txt("20 + 6 = 26 ✓", size=44, color=GREEN).move_to([3.75, 0.0, 0])
        self.play(Write(c1), run_time=0.7)
        self.play(Write(c2), run_time=0.7)
        self.play(Write(c3), run_time=0.8)

        d1 = txt("脚数对上了，答案就对了", size=28, color=DIM).move_to([3.75, -1.0, 0])
        self.play(FadeIn(d1), run_time=0.5)
        self.finish_section()

        # ---------- 4. 植树问题 ----------
        self.section(4, "植树：先算间隔数")
        self.play(FadeOut(heads), FadeOut(leg_groups), FadeOut(rabbit_legs),
                  FadeOut(c1), FadeOut(c2), FadeOut(c3), FadeOut(d1), run_time=0.6)

        r0 = road(0.5, (True, True, True, True, True), half=5.8, cx=0)
        self.play(Create(r0[0]), run_time=0.6)
        self.play(LaggedStart(*[FadeIn(t, scale=0.7) for t in r0[1:]],
                              lag_ratio=0.15), run_time=1.0)

        segs = VGroup()
        for k in range(4):
            x = -5.8 + k * 2.9 + 1.45
            segs.add(txt("5 米", size=24, color=DIM).move_to([x, 1.05, 0]))
        self.play(LaggedStart(*[FadeIn(s) for s in segs], lag_ratio=0.1), run_time=0.8)

        e1 = txt("20 ÷ 5 = 4 个间隔", size=42, color=GOLD).move_to([0, -1.05, 0])
        e2 = txt("两端都种：4 + 1 = 5 棵", size=36, color=GREEN).move_to([0, -2.05, 0])
        self.play(Write(e1), run_time=0.8)
        self.play(FadeIn(e2, shift=UP * 0.1), run_time=0.6)
        self.finish_section()

        # ---------- 5. 三种情况 ----------
        self.section(5, "两端都种、只种一端、两端都不种")
        self.play(FadeOut(r0), FadeOut(segs), FadeOut(e1), FadeOut(e2), run_time=0.6)

        rows = [
            (1.9, (True, True, True, True, True), "4 + 1 = 5 棵", "两端都种", GREEN),
            (0.05, (True, True, True, True, False), "就是 4 棵", "只种一端", GOLD),
            (-1.8, (False, True, True, True, False), "4 − 1 = 3 棵", "两端都不种", ORANGE),
        ]
        sec5 = VGroup()
        for y, planted, res, name, col in rows:
            rd = road(y, planted)
            tag = txt(name, size=26, color=col).move_to([-1.8, y + 0.62, 0])
            val = txt(res, size=32, color=col).move_to([5.35, y, 0])
            sec5.add(rd, tag, val)
            self.play(Create(rd[0]), FadeIn(tag), run_time=0.5)
            self.play(LaggedStart(*[FadeIn(t, scale=0.7) for t in rd[1:]],
                                  lag_ratio=0.12), run_time=0.7)
            self.play(FadeIn(val, shift=LEFT * 0.1), run_time=0.5)
        self.finish_section()

        # ---------- 6. 口诀 ----------
        self.section(6, "假设法，先算间隔，再看条件")
        self.play(FadeOut(sec5), run_time=0.6)

        k1 = label_box("假设全是鸡", size=30, color=CHALK).move_to([-3.6, 1.1, 0])
        k2 = label_box("先算间隔数", size=30, color=CHALK).move_to([0, 1.1, 0])
        k3 = label_box("看清条件", size=30, color=GOLD).move_to([3.6, 1.1, 0])
        self.play(LaggedStart(*[FadeIn(m, shift=UP * 0.1) for m in (k1, k2, k3)],
                              lag_ratio=0.2), run_time=1.2)

        big = txt("鸡兔同笼：脚数差 ÷ 2", size=42, color=GREEN).move_to([0, -0.3, 0])
        big2 = txt("植树：棵数 = 间隔数 ± 1", size=42, color=GREEN).move_to([0, -1.3, 0])
        self.play(Write(big), run_time=0.9)
        self.play(Write(big2), run_time=0.9)

        end = txt("两种题型，同一个思路", size=30, color=DIM).move_to([0, -2.4, 0])
        self.play(FadeIn(end, shift=UP * 0.1), run_time=0.6)
        self.finish_section()

        self.play(FadeOut(k1), FadeOut(k2), FadeOut(k3),
                  FadeOut(big), FadeOut(big2), FadeOut(end), run_time=0.6)
