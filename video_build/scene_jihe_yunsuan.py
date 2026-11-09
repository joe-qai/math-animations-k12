# -*- coding: utf-8 -*-
"""集合：交集取共同，并集取全部，补集是全集里剩下的。"""

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


class JiheYunsuanScene(NarratedScene):
    lesson = "jihe-yunsuan"

    def construct(self):
        # ---------- 0. 把东西装进一个筐 ----------
        self.section(0, "把确定的东西装进一个筐")
        box = RoundedRectangle(corner_radius=0.3, width=4.4, height=3.0,
                               color=GOLD, stroke_width=2.6,
                               fill_color=GOLD, fill_opacity=0.06)
        box.move_to([-3.7, -0.15, 0])
        self.play(Create(box), run_time=0.8)

        b0 = txt("筐", size=34, color=GOLD).move_to([-3.7, 1.02, 0])
        self.play(FadeIn(b0), run_time=0.4)

        items = VGroup(
            txt("铅笔", size=26).move_to([-4.9, 0.0, 0]),
            txt("尺子", size=26).move_to([-3.7, 0.0, 0]),
            txt("橡皮", size=26).move_to([-2.5, 0.0, 0]),
        )
        self.play(LaggedStart(*[FadeIn(m, shift=DOWN * 0.1) for m in items],
                              lag_ratio=0.25), run_time=0.9)

        r1 = rtxt("把确定的对象", 1.45, 32)
        r2 = rtxt("装进一个筐", 0.55, 34, GOLD)
        r3 = rtxt("这个整体，就叫集合", -0.45, 30, GREEN)
        r4 = rtxt("筐里的每个东西，叫元素", -1.4, 27, DIM)
        for m in (r1, r2, r3, r4):
            self.play(Write(m), run_time=0.45)
        self.finish_section()

        # ---------- 1. 元素与集合的写法 ----------
        self.section(1, "元素与集合的写法")
        self.play(FadeOut(b0), FadeOut(items),
                  FadeOut(r1), FadeOut(r2), FadeOut(r3), FadeOut(r4), run_time=0.5)

        nums = VGroup(
            txt("1", size=46, color=CHALK).move_to([-4.9, 0.0, 0]),
            txt("2", size=46, color=CHALK).move_to([-3.7, 0.0, 0]),
            txt("3", size=46, color=CHALK).move_to([-2.5, 0.0, 0]),
        )
        self.play(*[FadeIn(m) for m in nums], run_time=0.6)

        la = txt("A", size=36, color=GOLD).move_to([-5.45, 0.85, 0])
        eq = txt("A = {1, 2, 3}", size=32, color=GOLD).move_to([-3.6, -1.05, 0])
        self.play(Write(la), Write(eq), run_time=0.7)

        r1 = rtxt("1 ∈ A：1 属于 A", 1.45, 32, GREEN)
        r2 = rtxt("4 ∉ A：4 不属于 A", 0.45, 32, RED)
        r3 = rtxt("元素确定、互不相同、不讲顺序", -0.6, 27)
        r4 = rtxt("{1, 2, 3} 与 {3, 1, 2} 是同一个集合", -1.55, 26, DIM)
        for m in (r1, r2, r3, r4):
            self.play(Write(m), run_time=0.5)
        self.finish_section()

        # ---------- 2. 交集 ----------
        self.section(2, "交集：两边都有的")
        self.play(FadeOut(box), FadeOut(nums), FadeOut(la), FadeOut(eq),
                  FadeOut(r1), FadeOut(r2), FadeOut(r3), FadeOut(r4), run_time=0.45)

        cA = Circle(radius=1.35, color=BLUE, stroke_width=2.4,
                    fill_color=BLUE, fill_opacity=0.22).move_to([-4.55, -0.15, 0])
        cB = Circle(radius=1.35, color=ORANGE, stroke_width=2.4,
                    fill_color=ORANGE, fill_opacity=0.22).move_to([-2.75, -0.15, 0])
        self.play(Create(cA), run_time=0.7)
        self.play(Create(cB), run_time=0.7)

        lA = txt("A", size=32, color=BLUE).move_to([-5.3, 0.85, 0])
        lB = txt("B", size=32, color=ORANGE).move_to([-2.0, 0.85, 0])
        self.play(FadeIn(lA), FadeIn(lB), run_time=0.4)

        r1 = rtxt("A ∩ B", 1.5, 44, GOLD)
        r2 = rtxt("两边都有的元素", 0.5, 32, CHALK)
        r3 = rtxt("韦恩图上，是重叠的那一块", -0.5, 27, DIM)
        r4 = rtxt("{1, 2, 3} ∩ {2, 3, 4} = {2, 3}", -1.5, 27, GREEN)
        for m in (r1, r2, r3, r4):
            self.play(Write(m), run_time=0.5)
        self.finish_section()

        # ---------- 3. 并集 ----------
        self.section(3, "并集：有一边就算")
        self.play(FadeOut(r1), FadeOut(r2), FadeOut(r3), FadeOut(r4), run_time=0.4)

        r1 = rtxt("A ∪ B", 1.5, 44, GOLD)
        r2 = rtxt("有一边就算，重复的只写一次", 0.5, 29, CHALK)
        r3 = rtxt("两个圈盖住的全部区域", -0.5, 27, DIM)
        r4 = rtxt("{1, 2, 3} ∪ {2, 3, 4} = {1, 2, 3, 4}", -1.5, 27, GREEN)
        for m in (r1, r2, r3, r4):
            self.play(Write(m), run_time=0.5)
        self.finish_section()

        # ---------- 4. 补集 ----------
        self.section(4, "补集：全集中剩下的")
        self.play(FadeOut(cA), FadeOut(cB), FadeOut(lA), FadeOut(lB),
                  FadeOut(r1), FadeOut(r2), FadeOut(r3), FadeOut(r4), run_time=0.45)

        uni = Rectangle(width=5.0, height=3.0, color=DIM, stroke_width=2)
        uni.move_to([-3.7, -0.15, 0])
        self.play(Create(uni), run_time=0.7)

        cA = Circle(radius=1.0, color=BLUE, stroke_width=2.4,
                    fill_color=BLUE, fill_opacity=0.5).move_to([-4.4, -0.15, 0])
        self.play(Create(cA), run_time=0.7)

        lu = txt("U", size=30, color=DIM).move_to([-5.95, 1.05, 0])
        la2 = txt("A", size=30, color=CHALK).move_to([-4.4, -0.15, 0])
        self.play(FadeIn(lu), FadeIn(la2), run_time=0.4)

        dots = VGroup(
            Dot([-2.3, 0.85, 0], radius=0.1, color=GOLD),
            Dot([-2.2, -0.95, 0], radius=0.1, color=GOLD),
            Dot([-5.5, -1.05, 0], radius=0.1, color=GOLD),
        )
        self.play(LaggedStart(*[GrowFromCenter(d) for d in dots], lag_ratio=0.2), run_time=0.8)
        out = txt("剩下的，就是补集", size=24, color=GOLD).move_to([-3.7, -2.15, 0])
        self.play(FadeIn(out), run_time=0.4)

        r1 = rtxt("先定全集 U", 1.45, 32)
        r2 = rtxt("补集：U 里不属于 A 的元素", 0.4, 30, GOLD)
        r3 = rtxt("全集变了，补集就跟着变", -0.65, 28, RED)
        r4 = rtxt("求补集之前，先看清全集", -1.6, 27, DIM)
        for m in (r1, r2, r3, r4):
            self.play(Write(m), run_time=0.5)
        self.finish_section()

        # ---------- 5. 数轴上看交并补 ----------
        self.section(5, "用数轴看交并补")
        self.play(FadeOut(uni), FadeOut(cA), FadeOut(lu), FadeOut(la2),
                  FadeOut(dots), FadeOut(out), FadeOut(r1), FadeOut(r2),
                  FadeOut(r3), FadeOut(r4), run_time=0.5)

        nl = NumberLine(x_range=[-6, 0, 1], length=6.4, color=DIM)
        nl.move_to([-3.5, -0.4, 0])
        self.play(Create(nl), run_time=1.0)

        ticks = VGroup(*[
            txt(str(i), size=19, color=DIM).move_to(nl.n2p(i) + DOWN * 0.34)
            for i in range(-6, 1)
        ])
        self.play(FadeIn(ticks), run_time=0.6)

        segA = Line(nl.n2p(-5) + UP * 0.55, nl.n2p(-2.5) + UP * 0.55,
                    color=GOLD, stroke_width=7)
        segB = Line(nl.n2p(-3.8) + DOWN * 0.8, nl.n2p(-1.2) + DOWN * 0.8,
                    color=BLUE, stroke_width=7)
        self.play(Create(segA), run_time=0.7)
        self.play(Create(segB), run_time=0.7)

        tA = txt("A", size=28, color=GOLD).move_to(nl.n2p(-5) + UP * 0.95)
        tB = txt("B", size=28, color=BLUE).move_to(nl.n2p(-1.2) + DOWN * 1.2)
        self.play(FadeIn(tA), FadeIn(tB), run_time=0.4)

        inter = Line(nl.n2p(-3.8) + DOWN * 1.55, nl.n2p(-2.5) + DOWN * 1.55,
                     color=GREEN, stroke_width=6)
        ti = txt("A ∩ B", size=24, color=GREEN).move_to(nl.n2p(-3.15) + DOWN * 2.0)
        self.play(Create(inter), run_time=0.6)
        self.play(FadeIn(ti), run_time=0.4)

        r1 = rtxt("交集：两段公共的部分", 1.4, 29, GREEN)
        r2 = rtxt("并集：两段合起来的全部", 0.45, 29, GOLD)
        r3 = rtxt("补集：A 盖住之外剩下的", -0.55, 29, BLUE)
        r4 = rtxt("先画数轴，再找公共与剩余", -1.55, 27, DIM)
        for m in (r1, r2, r3, r4):
            self.play(Write(m), run_time=0.5)
        self.finish_section()

        # ---------- 6. 口诀 ----------
        self.section(6, "记一句话")
        self.play(FadeOut(nl), FadeOut(ticks), FadeOut(segA), FadeOut(segB), FadeOut(tA),
                  FadeOut(tB), FadeOut(inter), FadeOut(ti),
                  FadeOut(r1), FadeOut(r2), FadeOut(r3), FadeOut(r4), run_time=0.5)

        k1 = txt("交集取共同", size=52, color=GOLD).move_to([0, 1.15, 0])
        k2 = txt("并集取全部", size=52, color=GREEN).move_to([0, 0.0, 0])
        self.play(Write(k1), run_time=0.8)
        self.play(Write(k2), run_time=0.8)

        k3 = txt("先看每个集合装了什么，再动符号", size=30, color=DIM)
        k3.move_to([0, -1.2, 0])
        self.play(FadeIn(k3, shift=UP * 0.1), run_time=0.6)
        self.finish_section()

        self.play(FadeOut(k1), FadeOut(k2), FadeOut(k3), run_time=0.6)