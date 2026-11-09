# -*- coding: utf-8 -*-
"""充分条件与必要条件：小范围能推出大范围。"""

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


class ChongyaoTiaojianScene(NarratedScene):
    lesson = "chongyao-tiaojian"

    def construct(self):
        # ---------- 0. 下雨了，地会湿吗 ----------
        self.section(0, "下雨了，地会湿吗")
        cloud = VGroup(
            Circle(radius=0.45, color=DIM, stroke_width=2,
                   fill_color=DIM, fill_opacity=0.15).move_to([-4.7, 0.65, 0]),
            Circle(radius=0.58, color=DIM, stroke_width=2,
                   fill_color=DIM, fill_opacity=0.15).move_to([-3.95, 0.82, 0]),
            Circle(radius=0.45, color=DIM, stroke_width=2,
                   fill_color=DIM, fill_opacity=0.15).move_to([-3.2, 0.65, 0]),
            RoundedRectangle(corner_radius=0.2, width=2.4, height=0.7,
                             color=DIM, stroke_width=0,
                             fill_color=DIM, fill_opacity=0.15).move_to([-3.95, 0.45, 0]),
        )
        self.play(FadeIn(cloud), run_time=0.8)

        rain = VGroup(*[
            Line([x, 0.05, 0], [x - 0.12, -0.55, 0], color=BLUE, stroke_width=3)
            for x in (-4.8, -4.2, -3.6, -3.0)
        ])
        self.play(LaggedStart(*[Create(r) for r in rain], lag_ratio=0.15), run_time=0.8)

        puddle = Ellipse(width=3.1, height=0.5, color=BLUE, stroke_width=2,
                         fill_color=BLUE, fill_opacity=0.3).move_to([-3.9, -1.25, 0])
        self.play(Create(puddle), run_time=0.6)

        r1 = rtxt("下雨 ⇒ 地湿", 1.5, 36, GREEN)
        r2 = rtxt("地湿，未必下雨", 0.5, 36, RED)
        r3 = rtxt("洒水，也会把地弄湿", -0.6, 28, DIM)
        r4 = rtxt("这两句话的方向，不一样", -1.55, 27, GOLD)
        for m in (r1, r2, r3, r4):
            self.play(Write(m), run_time=0.5)
        self.finish_section()

        # ---------- 1. p 推出 q ----------
        self.section(1, "p 推出 q 是什么意思")
        self.play(FadeOut(cloud), FadeOut(rain), FadeOut(puddle),
                  FadeOut(r1), FadeOut(r2), FadeOut(r3), FadeOut(r4), run_time=0.5)

        pb = RoundedRectangle(corner_radius=0.16, width=1.7, height=1.15,
                              color=BLUE, stroke_width=2.4,
                              fill_color=BLUE, fill_opacity=0.15).move_to([-5.1, 0.35, 0])
        qb = RoundedRectangle(corner_radius=0.16, width=1.7, height=1.15,
                              color=GOLD, stroke_width=2.4,
                              fill_color=GOLD, fill_opacity=0.15).move_to([-2.1, 0.35, 0])
        self.play(Create(pb), run_time=0.6)
        self.play(Create(qb), run_time=0.6)

        tp = txt("p", size=46, color=BLUE).move_to(pb.get_center())
        tq = txt("q", size=46, color=GOLD).move_to(qb.get_center())
        self.play(FadeIn(tp), FadeIn(tq), run_time=0.5)

        ar = Arrow([-4.15, 0.35, 0], [-3.05, 0.35, 0], color=GREEN,
                   stroke_width=5, buff=0, max_tip_length_to_length_ratio=0.18)
        self.play(Create(ar), run_time=0.7)

        cp = txt("条件", size=24, color=DIM).move_to([-5.1, -0.5, 0])
        cq = txt("结论", size=24, color=DIM).move_to([-2.1, -0.5, 0])
        self.play(FadeIn(cp), FadeIn(cq), run_time=0.4)

        r1 = rtxt("「若 p，则 q」是一个命题", 1.4, 30)
        r2 = rtxt("p ⇒ q", 0.45, 44, GOLD)
        r3 = rtxt("p 成立，q 一定成立", -0.5, 30, GREEN)
        r4 = rtxt("箭头，只有一个方向", -1.55, 27, DIM)
        for m in (r1, r2, r3, r4):
            self.play(Write(m), run_time=0.5)
        self.finish_section()

        # ---------- 2. 充分条件 ----------
        self.section(2, "充分：有它就够")
        self.play(FadeOut(pb), FadeOut(qb), FadeOut(tp), FadeOut(tq),
                  FadeOut(ar), FadeOut(cp), FadeOut(cq),
                  FadeOut(r1), FadeOut(r2), FadeOut(r3), FadeOut(r4), run_time=0.5)

        qc = Circle(radius=2.0, color=GOLD, stroke_width=2.6,
                    fill_color=GOLD, fill_opacity=0.08).move_to([-3.9, -0.1, 0])
        self.play(Create(qc), run_time=0.8)

        pc = Circle(radius=0.8, color=BLUE, stroke_width=2.6,
                    fill_color=BLUE, fill_opacity=0.35).move_to([-4.7, 0.65, 0])
        self.play(Create(pc), run_time=0.6)

        lp = txt("p", size=34, color=CHALK).move_to([-4.7, 0.65, 0])
        lq = txt("q", size=34, color=GOLD).move_to([-2.6, 1.35, 0])
        self.play(FadeIn(lp), FadeIn(lq), run_time=0.4)

        r1 = rtxt("p 是 q 的充分条件", 1.45, 33, GOLD)
        r2 = rtxt("有它就够", 0.55, 40, GREEN)
        r3 = rtxt("只要下雨，就足以保证地湿", -0.55, 27)
        r4 = rtxt("充分条件不唯一，洒水也够", -1.55, 26, DIM)
        for m in (r1, r2, r3, r4):
            self.play(Write(m), run_time=0.5)
        self.finish_section()

        # ---------- 3. 必要条件 ----------
        self.section(3, "必要：没它不行")
        self.play(FadeOut(r1), FadeOut(r2), FadeOut(r3), FadeOut(r4), run_time=0.4)

        ring = Circle(radius=2.0, color=ORANGE, stroke_width=5).move_to([-3.9, -0.1, 0])
        self.play(Create(ring), run_time=0.8)

        r1 = rtxt("q 是 p 的必要条件", 1.45, 33, GOLD)
        r2 = rtxt("没它不行", 0.55, 40, ORANGE)
        r3 = rtxt("地不湿，就一定没下雨", -0.55, 27)
        r4 = rtxt("同一个箭头，反过来读", -1.55, 26, DIM)
        for m in (r1, r2, r3, r4):
            self.play(Write(m), run_time=0.5)
        self.finish_section()

        # ---------- 4. 充要条件 ----------
        self.section(4, "充要：互相推出")
        self.play(FadeOut(qc), FadeOut(pc), FadeOut(lp), FadeOut(lq),
                  FadeOut(ring), FadeOut(r1), FadeOut(r2), FadeOut(r3),
                  FadeOut(r4), run_time=0.5)

        c1 = Circle(radius=1.05, color=BLUE, stroke_width=2.6,
                    fill_color=BLUE, fill_opacity=0.22).move_to([-5.0, -0.1, 0])
        c2 = Circle(radius=1.05, color=GOLD, stroke_width=2.6,
                    fill_color=GOLD, fill_opacity=0.22).move_to([-2.4, -0.1, 0])
        self.play(Create(c1), Create(c2), run_time=0.9)

        t1 = txt("p", size=38, color=BLUE).move_to(c1.get_center())
        t2 = txt("q", size=38, color=GOLD).move_to(c2.get_center())
        self.play(FadeIn(t1), FadeIn(t2), run_time=0.5)

        a1 = Arrow([-3.9, 0.16, 0], [-3.5, 0.16, 0], color=GREEN,
                   stroke_width=4, buff=0, max_tip_length_to_length_ratio=0.3)
        a2 = Arrow([-3.5, -0.36, 0], [-3.9, -0.36, 0], color=GREEN,
                   stroke_width=4, buff=0, max_tip_length_to_length_ratio=0.3)
        self.play(Create(a1), Create(a2), run_time=0.8)

        r1 = rtxt("p ⇔ q", 1.45, 44, GOLD)
        r2 = rtxt("两个方向都成立", 0.5, 32, GREEN)
        r3 = rtxt("互为充要条件，可以互相代替", -0.55, 28)
        r4 = rtxt("只证一个方向，不算充要", -1.55, 27, RED)
        for m in (r1, r2, r3, r4):
            self.play(Write(m), run_time=0.5)
        self.finish_section()

        # ---------- 5. 用范围判断 ----------
        self.section(5, "用范围大小来判断")
        self.play(FadeOut(c1), FadeOut(c2), FadeOut(t1), FadeOut(t2),
                  FadeOut(a1), FadeOut(a2), FadeOut(r1), FadeOut(r2),
                  FadeOut(r3), FadeOut(r4), run_time=0.5)

        bigQ = Circle(radius=2.1, color=GOLD, stroke_width=2.6,
                      fill_color=GOLD, fill_opacity=0.08).move_to([-3.7, -0.1, 0])
        self.play(Create(bigQ), run_time=0.8)

        smallP = Circle(radius=0.9, color=BLUE, stroke_width=2.6,
                        fill_color=BLUE, fill_opacity=0.4).move_to([-4.25, 0.5, 0])
        self.play(Create(smallP), run_time=0.6)

        lp = txt("P", size=30, color=CHALK).move_to([-4.25, 0.5, 0])
        lq = txt("Q", size=30, color=GOLD).move_to([-2.2, -1.15, 0])
        self.play(FadeIn(lp), FadeIn(lq), run_time=0.4)

        r1 = rtxt("把 p、q 看成两个范围", 1.45, 29)
        r2 = rtxt("P ⊆ Q ⇒ p ⇒ q", 0.5, 34, GOLD)
        r3 = rtxt("小范围推大范围", -0.55, 38, GREEN)
        r4 = rtxt("大范围，推不出小范围", -1.6, 28, RED)
        for m in (r1, r2, r3, r4):
            self.play(Write(m), run_time=0.5)
        self.finish_section()

        # ---------- 6. 口诀 ----------
        self.section(6, "记一句话")
        self.play(FadeOut(bigQ), FadeOut(smallP), FadeOut(lp), FadeOut(lq),
                  FadeOut(r1), FadeOut(r2), FadeOut(r3), FadeOut(r4), run_time=0.5)

        k1 = txt("小范围推大范围", size=52, color=GOLD).move_to([0, 1.15, 0])
        k2 = txt("充分看够不够，必要看缺不缺", size=32, color=CHALK)
        k2.move_to([0, -0.05, 0])
        k3 = txt("两个方向都对，才是充要", size=32, color=GREEN)
        k3.move_to([0, -1.15, 0])
        self.play(Write(k1), run_time=0.8)
        self.play(Write(k2), run_time=0.8)
        self.play(Write(k3), run_time=0.8)
        self.finish_section()

        self.play(FadeOut(k1), FadeOut(k2), FadeOut(k3), run_time=0.6)