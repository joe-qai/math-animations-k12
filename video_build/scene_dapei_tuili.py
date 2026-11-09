# -*- coding: utf-8 -*-
"""数学广角：搭配与推理。三年级上册「数学广角——搭配」。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


def shirt(x: float, y: float, label: str, color: str) -> VGroup:
    body = RoundedRectangle(corner_radius=0.1, width=0.9, height=0.8,
                            stroke_width=2, stroke_color=color,
                            fill_color=color, fill_opacity=0.14).move_to([x, y, 0])
    t = txt(label, size=22, color=color).move_to([x, y, 0])
    return VGroup(body, t)


def pants(x: float, y: float, label: str, color: str) -> VGroup:
    body = RoundedRectangle(corner_radius=0.1, width=0.72, height=0.9,
                            stroke_width=2, stroke_color=color,
                            fill_color=color, fill_opacity=0.14).move_to([x, y, 0])
    t = txt(label, size=20, color=color).move_to([x, y, 0])
    return VGroup(body, t)


def kid(x: float, y: float, name: str, color: str) -> VGroup:
    head = Circle(radius=0.3, stroke_width=2, stroke_color=color,
                  fill_color=color, fill_opacity=0.16).move_to([x, y, 0])
    t = txt(name, size=22, color=color).move_to([x, y, 0])
    return VGroup(head, t)


class DapeiTuiliScene(NarratedScene):
    lesson = "dapei-tuili"

    def construct(self):
        # ---------- 0. 两件上衣、三条裤子 ----------
        self.section(0, "两件上衣，三条裤子")
        s1 = shirt(-5.4, 1.45, "上衣 1", GOLD)
        s2 = shirt(-3.9, 1.45, "上衣 2", BLUE)
        p1 = pants(-6.0, -1.1, "裤 1", GREEN)
        p2 = pants(-4.6, -1.1, "裤 2", GREEN)
        p3 = pants(-3.2, -1.1, "裤 3", GREEN)
        self.play(FadeIn(s1, shift=DOWN * 0.1), FadeIn(s2, shift=DOWN * 0.1),
                  run_time=0.8)
        self.play(LaggedStart(*[FadeIn(p, shift=UP * 0.1) for p in (p1, p2, p3)],
                              lag_ratio=0.15), run_time=1.0)

        q1 = txt("一共有多少种穿法？", size=38, color=GOLD).move_to([3.5, 1.0, 0])
        q2 = txt("一件上衣配一条裤子", size=28, color=DIM).move_to([3.5, -0.05, 0])
        self.play(Write(q1), run_time=0.7)
        self.play(FadeIn(q2), run_time=0.5)
        self.finish_section()

        # ---------- 1. 第一件上衣配三条 ----------
        self.section(1, "第一件上衣，有三种配法")
        self.play(FadeOut(q1), FadeOut(q2), run_time=0.4)

        links1 = VGroup(*[
            Line(s1.get_bottom() + DOWN * 0.04, p.get_top() + UP * 0.04,
                 color=GOLD, stroke_width=2.2)
            for p in (p1, p2, p3)
        ])
        self.play(LaggedStart(*[Create(l) for l in links1], lag_ratio=0.18), run_time=1.2)

        one = txt("1 种", size=26, color=GOLD).move_to([-6.0, 0.15, 0])
        two = txt("1 种", size=26, color=GOLD).move_to([-4.6, 0.15, 0])
        three = txt("1 种", size=26, color=GOLD).move_to([-3.2, 0.15, 0])
        self.play(LaggedStart(*[FadeIn(t, scale=0.8) for t in (one, two, three)],
                              lag_ratio=0.15), run_time=0.9)

        a1 = txt("上衣 1 配裤 1", size=32, color=GOLD).move_to([3.5, 1.0, 0])
        a2 = txt("配裤 2、配裤 3", size=32, color=GOLD).move_to([3.5, 0.05, 0])
        a3 = txt("一共 3 种", size=36, color=GREEN).move_to([3.5, -0.95, 0])
        self.play(Write(a1), run_time=0.5)
        self.play(Write(a2), run_time=0.5)
        self.play(FadeIn(a3, shift=UP * 0.1), run_time=0.6)
        self.finish_section()

        # ---------- 2. 第二件上衣再配三条 ----------
        self.section(2, "第二件上衣，又有三种")
        self.play(FadeOut(a1), FadeOut(a2), FadeOut(a3), run_time=0.4)

        links2 = VGroup(*[
            Line(s2.get_bottom() + DOWN * 0.04, p.get_top() + UP * 0.04,
                 color=BLUE, stroke_width=2.2)
            for p in (p1, p2, p3)
        ])
        self.play(LaggedStart(*[Create(l) for l in links2], lag_ratio=0.18), run_time=1.2)

        b1 = txt("上衣 2 也能配这三条", size=32, color=BLUE).move_to([3.5, 0.9, 0])
        b2 = txt("又是 3 种", size=36, color=BLUE).move_to([3.5, -0.05, 0])
        b3 = txt("3 + 3 = 6 种", size=40, color=GOLD).move_to([3.5, -1.1, 0])
        self.play(Write(b1), run_time=0.6)
        self.play(Write(b2), run_time=0.5)
        self.play(FadeIn(b3, shift=UP * 0.1), run_time=0.6)
        self.finish_section()

        # ---------- 3. 用乘法算 ----------
        self.section(3, "二乘三等于六")
        self.play(FadeOut(links1), FadeOut(links2), FadeOut(one), FadeOut(two),
                  FadeOut(three), FadeOut(b1), FadeOut(b2), FadeOut(b3),
                  FadeOut(s1), FadeOut(s2), FadeOut(p1), FadeOut(p2), FadeOut(p3),
                  run_time=0.6)

        e1 = txt("2 × 3 = 6", size=62, color=GOLD).move_to([0, 1.15, 0])
        self.play(Write(e1), run_time=0.9)

        c1 = txt("2 件上衣", size=34, color=BLUE).move_to([-2.6, -0.15, 0])
        c2 = txt("×", size=34, color=DIM).move_to([0, -0.15, 0])
        c3 = txt("3 条裤子", size=34, color=GREEN).move_to([2.6, -0.15, 0])
        self.play(FadeIn(c1), FadeIn(c2), FadeIn(c3), run_time=0.7)

        c4 = txt("= 6 种穿法", size=40, color=CHALK).move_to([0, -1.25, 0])
        self.play(FadeIn(c4, shift=UP * 0.1), run_time=0.6)

        c5 = txt("搭配问题，用乘法算最快", size=30, color=DIM).move_to([0, -2.25, 0])
        self.play(FadeIn(c5), run_time=0.5)
        self.finish_section()

        # ---------- 4. 有顺序地搭配 ----------
        self.section(4, "有顺序，才不重不漏")
        self.play(FadeOut(e1), FadeOut(c1), FadeOut(c2), FadeOut(c3), FadeOut(c4),
                  FadeOut(c5), run_time=0.5)

        step1 = label_box("① 固定上衣 1", size=34, color=GOLD).move_to([-2.9, 1.3, 0])
        step2 = label_box("② 配完三条裤子", size=34, color=GOLD).move_to([-2.9, 0.2, 0])
        step3 = label_box("③ 再换上衣 2", size=34, color=BLUE).move_to([-2.9, -0.9, 0])
        self.play(FadeIn(step1, shift=RIGHT * 0.1), run_time=0.6)
        self.play(FadeIn(step2, shift=RIGHT * 0.1), run_time=0.6)
        self.play(FadeIn(step3, shift=RIGHT * 0.1), run_time=0.6)

        tip1 = txt("乱着配", size=34, color=RED).move_to([3.7, 1.05, 0])
        tip2 = txt("容易重复、容易漏", size=30, color=RED).move_to([3.7, 0.15, 0])
        tip3 = txt("按顺序，一个不漏", size=34, color=GREEN).move_to([3.7, -0.9, 0])
        self.play(Write(tip1), run_time=0.5)
        self.play(Write(tip2), run_time=0.5)
        self.play(FadeIn(tip3, shift=UP * 0.1), run_time=0.6)
        self.finish_section()

        # ---------- 5. 推理：排除法 ----------
        self.section(5, "推理题，用排除法")
        self.play(FadeOut(step1), FadeOut(step2), FadeOut(step3),
                  FadeOut(tip1), FadeOut(tip2), FadeOut(tip3), run_time=0.5)

        k1 = kid(-4.9, 1.1, "小明", GOLD)
        k2 = kid(-3.2, 1.1, "小红", BLUE)
        k3 = kid(-1.5, 1.1, "小刚", GREEN)
        self.play(LaggedStart(*[FadeIn(k, scale=0.85) for k in (k1, k2, k3)],
                              lag_ratio=0.18), run_time=1.0)

        clue = txt("每人拿一种：苹果、梨、香蕉", size=28, color=DIM).move_to([0, 0.05, 0])
        self.play(FadeIn(clue), run_time=0.5)

        r1 = txt("小明：不是苹果，也不是梨", size=30, color=GOLD).move_to([0, -0.85, 0])
        self.play(Write(r1), run_time=0.6)

        r2 = txt("→ 小明拿香蕉", size=36, color=GOLD).move_to([0, -1.75, 0])
        self.play(FadeIn(r2, shift=UP * 0.1), run_time=0.6)

        self.wait(0.2)
        self.play(FadeOut(clue), FadeOut(r1), FadeOut(r2), run_time=0.4)

        s1 = txt("剩下苹果和梨", size=32, color=CHALK).move_to([0, 0.05, 0])
        s2 = txt("小红：不是苹果", size=30, color=BLUE).move_to([0, -0.8, 0])
        s3 = txt("→ 小红拿梨，小刚拿苹果", size=34, color=GREEN).move_to([0, -1.7, 0])
        self.play(Write(s1), run_time=0.5)
        self.play(Write(s2), run_time=0.5)
        self.play(FadeIn(s3, shift=UP * 0.1), run_time=0.6)
        self.finish_section()

        # ---------- 6. 口诀 ----------
        self.section(6, "搭配用乘法，推理用排除")
        self.play(FadeOut(k1), FadeOut(k2), FadeOut(k3),
                  FadeOut(s1), FadeOut(s2), FadeOut(s3), run_time=0.5)

        j1 = txt("搭配 → 用乘法", size=48, color=GOLD).move_to([0, 1.3, 0])
        j2 = txt("推理 → 用排除", size=48, color=BLUE).move_to([0, 0.15, 0])
        j3 = txt("先找能确定的那个", size=42, color=GREEN).move_to([0, -1.05, 0])
        self.play(Write(j1), run_time=0.8)
        self.play(Write(j2), run_time=0.8)
        self.play(FadeIn(j3, shift=UP * 0.1), run_time=0.7)

        fin = txt("有序思考，是数学的好习惯", size=28, color=DIM).move_to([0, -2.15, 0])
        self.play(FadeIn(fin), run_time=0.6)
        self.finish_section()

        self.play(FadeOut(j1), FadeOut(j2), FadeOut(j3), FadeOut(fin), run_time=0.6)