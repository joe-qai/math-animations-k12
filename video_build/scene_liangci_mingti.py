# -*- coding: utf-8 -*-
"""全称量词与存在量词：全称变存在，结论取反。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


def rtxt(s: str, y: float, size: int = 30, color: str = CHALK,
         width: float = 6.1, x: float = 3.55) -> Text:
    m = txt(s, size=size, color=color)
    if m.width > width:
        m.scale_to_fit_width(width)
    m.move_to([x, y, 0])
    return m


def person(x: float, color: str = CHALK, opacity: float = 1.0) -> VGroup:
    head = Circle(radius=0.19, color=color, stroke_width=2.2,
                  fill_color=color, fill_opacity=0.25 * opacity)
    head.move_to([x, -0.25, 0])
    body = Line([x, -0.45, 0], [x, -1.05, 0], color=color, stroke_width=3)
    arms = Line([x - 0.32, -0.62, 0], [x + 0.32, -0.62, 0],
                color=color, stroke_width=2.4)
    return VGroup(head, body, arms)


class LiangciMingtiScene(NarratedScene):
    lesson = "liangci-mingti"

    def construct(self):
        # ---------- 0. 都到齐了吗 ----------
        self.section(0, "都到齐了吗")
        xs = [-6.1, -5.3, -4.5, -3.7, -2.9]
        people = VGroup(*[person(x) for i, x in enumerate(xs) if i != 2])
        absent = person(xs[2], RED, 0.5)
        self.play(LaggedStart(*[FadeIn(p, shift=UP * 0.1) for p in people],
                              lag_ratio=0.12), run_time=1.0)
        self.play(FadeIn(absent), run_time=0.5)

        qmark = txt("？", size=40, color=RED).move_to([xs[2], 0.55, 0])
        self.play(FadeIn(qmark), run_time=0.5)

        r1 = rtxt("「所有同学都到齐了」", 1.45, 30)
        r2 = rtxt("「有人带了伞」", 0.55, 30)
        r3 = rtxt("一个管全部，一个管至少一个", -0.5, 28, GOLD)
        r4 = rtxt("这就是两种不同的量词", -1.55, 27, DIM)
        for m in (r1, r2, r3, r4):
            self.play(Write(m), run_time=0.5)
        self.finish_section()

        # ---------- 1. 全称量词 ----------
        self.section(1, "全称量词：所有、任意")
        self.play(FadeOut(people), FadeOut(absent), FadeOut(qmark),
                  FadeOut(r1), FadeOut(r2), FadeOut(r3), FadeOut(r4), run_time=0.5)

        fa = txt("∀", size=150, color=GOLD).move_to([-4.2, 0.35, 0])
        self.play(FadeIn(fa, scale=0.8), run_time=0.8)

        l1 = txt("所有", size=30, color=CHALK).move_to([-5.7, -1.5, 0])
        l2 = txt("任意", size=30, color=CHALK).move_to([-4.2, -1.5, 0])
        l3 = txt("每一个", size=30, color=CHALK).move_to([-2.55, -1.5, 0])
        self.play(LaggedStart(FadeIn(l1), FadeIn(l2), FadeIn(l3), lag_ratio=0.2),
                  run_time=0.9)

        r1 = rtxt("全称量词，记作 ∀", 1.45, 32, GOLD)
        r2 = rtxt("∀x ∈ M，p(x)", 0.5, 36, CHALK)
        r3 = rtxt("每一个都成立，才为真", -0.55, 28, GREEN)
        r4 = rtxt("找到一个反例，就能推翻", -1.55, 27, RED)
        for m in (r1, r2, r3, r4):
            self.play(Write(m), run_time=0.5)
        self.finish_section()

        # ---------- 2. 存在量词 ----------
        self.section(2, "存在量词：有一个就行")
        self.play(FadeOut(fa), FadeOut(l1), FadeOut(l2), FadeOut(l3),
                  FadeOut(r1), FadeOut(r2), FadeOut(r3), FadeOut(r4), run_time=0.5)

        ex = txt("∃", size=150, color=GREEN).move_to([-4.2, 0.35, 0])
        self.play(FadeIn(ex, scale=0.8), run_time=0.8)

        l1 = txt("存在", size=30, color=CHALK).move_to([-5.7, -1.5, 0])
        l2 = txt("至少一个", size=30, color=CHALK).move_to([-4.2, -1.5, 0])
        l3 = txt("有些", size=30, color=CHALK).move_to([-2.55, -1.5, 0])
        self.play(LaggedStart(FadeIn(l1), FadeIn(l2), FadeIn(l3), lag_ratio=0.2),
                  run_time=0.9)

        r1 = rtxt("存在量词，记作 ∃", 1.45, 32, GREEN)
        r2 = rtxt("∃x ∈ M，p(x)", 0.5, 36, CHALK)
        r3 = rtxt("找到一个例子，就是真", -0.55, 28, GREEN)
        r4 = rtxt("说它假，要说明一个都没有", -1.55, 27, RED)
        for m in (r1, r2, r3, r4):
            self.play(Write(m), run_time=0.5)
        self.finish_section()

        # ---------- 3. 真假怎么判断 ----------
        self.section(3, "真假怎么判断")
        self.play(FadeOut(ex), FadeOut(l1), FadeOut(l2), FadeOut(l3),
                  FadeOut(r1), FadeOut(r2), FadeOut(r3), FadeOut(r4), run_time=0.5)

        cells = VGroup(*[
            RoundedRectangle(corner_radius=0.1, width=0.9, height=0.9,
                             color=DIM, stroke_width=2,
                             fill_color=DIM, fill_opacity=0.08).move_to([x, 0.55, 0])
            for x in (-5.9, -4.9, -3.9, -2.9, -1.9)
        ])
        self.play(LaggedStart(*[Create(c) for c in cells], lag_ratio=0.15), run_time=1.0)

        bad = cells[2]
        bad.set_stroke(RED, 2.6).set_fill(RED, 0.25)
        cross = VGroup(
            Line(bad.get_corner(UL) + RIGHT * 0.15 + DOWN * 0.15,
                 bad.get_corner(DR) + LEFT * 0.15 + UP * 0.15, color=RED, stroke_width=4),
            Line(bad.get_corner(UR) + LEFT * 0.15 + DOWN * 0.15,
                 bad.get_corner(DL) + RIGHT * 0.15 + UP * 0.15, color=RED, stroke_width=4),
        )
        self.play(Create(cross), run_time=0.7)

        tag = txt("反例", size=26, color=RED).move_to([-3.9, -0.4, 0])
        self.play(FadeIn(tag), run_time=0.4)

        r1 = rtxt("全称命题：举一个反例就假", 1.35, 28, RED)
        r2 = rtxt("存在命题：举一个例子就真", 0.4, 28, GREEN)
        r3 = rtxt("验证几个数，不算证明", -0.6, 27, DIM)
        r4 = rtxt("要证全称，必须讲一般道理", -1.55, 27, GOLD)
        for m in (r1, r2, r3, r4):
            self.play(Write(m), run_time=0.5)
        self.finish_section()

        # ---------- 4. 否定：量词要变 ----------
        self.section(4, "否定：量词要变")
        self.play(FadeOut(cells), FadeOut(cross), FadeOut(tag),
                  FadeOut(r1), FadeOut(r2), FadeOut(r3), FadeOut(r4), run_time=0.5)

        fa2 = txt("∀", size=110, color=GOLD).move_to([-5.0, 0.1, 0])
        ex2 = txt("∃", size=110, color=GREEN).move_to([-2.1, 0.1, 0])
        self.play(FadeIn(fa2), run_time=0.5)
        self.play(FadeIn(ex2), run_time=0.5)

        ar = Arrow([-4.2, 0.1, 0], [-3.0, 0.1, 0], color=CHALK,
                   stroke_width=4, buff=0, max_tip_length_to_length_ratio=0.22)
        self.play(Create(ar), run_time=0.6)

        cap = txt("量词要变", size=26, color=DIM).move_to([-3.6, 0.95, 0])
        self.play(FadeIn(cap), run_time=0.4)

        r1 = rtxt("否定，先改量词", 1.45, 33, GOLD)
        r2 = rtxt("∀ 变成 ∃", 0.5, 34, CHALK)
        r3 = rtxt("∃ 变成 ∀", -0.5, 34, CHALK)
        r4 = rtxt("只改结论、不改量词，是错的", -1.55, 27, RED)
        for m in (r1, r2, r3, r4):
            self.play(Write(m), run_time=0.5)
        self.finish_section()

        # ---------- 5. 结论也要取反 ----------
        self.section(5, "结论也要取反")
        self.play(FadeOut(fa2), FadeOut(ex2), FadeOut(ar), FadeOut(cap),
                  FadeOut(r1), FadeOut(r2), FadeOut(r3), FadeOut(r4), run_time=0.5)

        box1 = RoundedRectangle(corner_radius=0.14, width=2.5, height=1.0,
                                color=BLUE, stroke_width=2.2,
                                fill_color=BLUE, fill_opacity=0.15).move_to([-5.35, 1.0, 0])
        box2 = RoundedRectangle(corner_radius=0.14, width=2.5, height=1.0,
                                color=GREEN, stroke_width=2.2,
                                fill_color=GREEN, fill_opacity=0.15).move_to([-2.0, 1.0, 0])
        self.play(Create(box1), Create(box2), run_time=0.8)

        t1 = txt("所有都及格", size=25, color=CHALK).move_to(box1.get_center())
        t2 = txt("有人没及格", size=25, color=GREEN).move_to(box2.get_center())
        self.play(FadeIn(t1), FadeIn(t2), run_time=0.6)

        ar = Arrow([-4.05, 1.0, 0], [-3.3, 1.0, 0], color=GREEN,
                   stroke_width=4, buff=0, max_tip_length_to_length_ratio=0.3)
        self.play(Create(ar), run_time=0.6)

        wrong = txt("所有人都不及格", size=27, color=RED).move_to([-3.7, -0.55, 0])
        cross = VGroup(
            Line([-5.2, -0.15, 0], [-2.2, -0.95, 0], color=RED, stroke_width=4),
            Line([-5.2, -0.95, 0], [-2.2, -0.15, 0], color=RED, stroke_width=4),
        )
        self.play(FadeIn(wrong), run_time=0.5)
        self.play(Create(cross), run_time=0.6)

        note = txt("这是另一个命题，不是否定", size=24, color=DIM).move_to([-3.7, -1.65, 0])
        self.play(FadeIn(note), run_time=0.4)

        r1 = rtxt("结论也要同时取反", 1.4, 31, GOLD)
        r2 = rtxt("「都及格」的否定", 0.35, 28)
        r3 = rtxt("是「有人没及格」", -0.55, 32, GREEN)
        r4 = rtxt("不是「都不及格」", -1.55, 30, RED)
        for m in (r1, r2, r3, r4):
            self.play(Write(m), run_time=0.5)
        self.finish_section()

        # ---------- 6. 口诀 ----------
        self.section(6, "记一句话")
        self.play(FadeOut(box1), FadeOut(box2), FadeOut(t1), FadeOut(t2),
                  FadeOut(ar), FadeOut(wrong), FadeOut(cross), FadeOut(note),
                  FadeOut(r1), FadeOut(r2), FadeOut(r3), FadeOut(r4), run_time=0.5)

        k1 = txt("全称变存在", size=52, color=GOLD).move_to([0, 1.15, 0])
        k2 = txt("结论取反", size=52, color=GREEN).move_to([0, 0.0, 0])
        self.play(Write(k1), run_time=0.8)
        self.play(Write(k2), run_time=0.8)

        k3 = txt("量词和结论，两件事一起改", size=30, color=DIM)
        k3.move_to([0, -1.2, 0])
        self.play(FadeIn(k3, shift=UP * 0.1), run_time=0.6)
        self.finish_section()

        self.play(FadeOut(k1), FadeOut(k2), FadeOut(k3), run_time=0.6)