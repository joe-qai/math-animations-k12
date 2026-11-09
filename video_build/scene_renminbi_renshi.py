# -*- coding: utf-8 -*-
"""认识人民币：元、角、分，一元十角、一角十分。一年级下册「购物」。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


def coin(x: float, y: float, label: str, color: str = GOLD,
         r: float = 0.42, size: int = 24) -> VGroup:
    c = Circle(radius=r, stroke_width=2, stroke_color=color,
               fill_color=color, fill_opacity=0.14).move_to([x, y, 0])
    t = txt(label, size=size, color=color).move_to([x, y, 0])
    return VGroup(c, t)


def note(x: float, y: float, label: str, color: str = GREEN) -> VGroup:
    b = RoundedRectangle(corner_radius=0.08, width=1.7, height=0.9,
                         stroke_width=2, stroke_color=color,
                         fill_color=color, fill_opacity=0.1).move_to([x, y, 0])
    t = txt(label, size=34, color=color).move_to([x, y, 0])
    return VGroup(b, t)


class RenminbiRenshiScene(NarratedScene):
    lesson = "renminbi-renshi"

    def construct(self):
        # ---------- 0. 商店里要用钱 ----------
        self.section(0, "买东西，要用人民币")
        shop = RoundedRectangle(corner_radius=0.16, width=4.2, height=2.6,
                                stroke_color=DIM, stroke_width=2,
                                fill_color=BLUE, fill_opacity=0.06).move_to([-3.7, 0.35, 0])
        roof = Polygon([-6.2, 1.65, 0], [-3.7, 2.55, 0], [-1.2, 1.65, 0],
                       stroke_width=2, stroke_color=GOLD, fill_color=GOLD,
                       fill_opacity=0.12)
        q = txt("商 店", size=34, color=GOLD).move_to([-3.7, 1.05, 0])
        self.play(Create(shop), Create(roof), run_time=1.0)
        self.play(Write(q), run_time=0.6)

        pen = txt("铅笔  8 角", size=30, color=CHALK).move_to([-3.7, 0.2, 0])
        self.play(FadeIn(pen), run_time=0.5)

        money = note(3.5, 1.2, "人民币", GREEN)
        self.play(FadeIn(money, shift=UP * 0.1), run_time=0.7)

        w1 = txt("我们国家的钱", size=34, color=CHALK).move_to([3.5, 0.15, 0])
        w2 = txt("叫人民币", size=40, color=GOLD).move_to([3.5, -0.8, 0])
        self.play(Write(w1), run_time=0.5)
        self.play(Write(w2), run_time=0.6)
        self.finish_section()

        # ---------- 1. 三个单位 ----------
        self.section(1, "元、角、分")
        self.play(FadeOut(shop), FadeOut(roof), FadeOut(q), FadeOut(pen),
                  FadeOut(money), FadeOut(w1), FadeOut(w2), run_time=0.5)

        u1 = label_box("元", size=44, color=GOLD).move_to([-3.9, 1.35, 0])
        u2 = label_box("角", size=44, color=BLUE).move_to([0, 1.35, 0])
        u3 = label_box("分", size=44, color=GREEN).move_to([3.9, 1.35, 0])
        self.play(LaggedStart(*[FadeIn(u, shift=UP * 0.12) for u in (u1, u2, u3)],
                              lag_ratio=0.25), run_time=1.2)

        c1 = VGroup(coin(-3.9, -0.15, "1 元", GOLD, r=0.62, size=30),
                    coin(-3.9, -1.35, "5 角", BLUE, r=0.52, size=24))
        c2 = VGroup(coin(0, -0.15, "1 角", BLUE, r=0.52, size=26),
                    coin(0, -1.35, "5 角", GOLD, r=0.52, size=24))
        c3 = VGroup(coin(3.9, -0.15, "1 分", GREEN, r=0.5, size=24),
                    coin(3.9, -1.35, "5 分", GOLD, r=0.5, size=24))
        self.play(FadeIn(c1), run_time=0.6)
        self.play(FadeIn(c2), run_time=0.6)
        self.play(FadeIn(c3), run_time=0.6)

        t = txt("人民币有纸币，也有硬币", size=28, color=DIM).move_to([0, -2.35, 0])
        self.play(FadeIn(t), run_time=0.5)
        self.finish_section()

        # ---------- 2. 1 元 = 10 角 ----------
        self.section(2, "一元可以换十个一角")
        self.play(FadeOut(u1), FadeOut(u2), FadeOut(u3),
                  FadeOut(c1), FadeOut(c2), FadeOut(c3), FadeOut(t), run_time=0.5)

        one = coin(-5.4, 0.55, "1 元", GOLD, r=0.72, size=32)
        self.play(FadeIn(one, scale=0.85), run_time=0.6)

        eq = txt("=", size=48, color=CHALK).move_to([-3.85, 0.55, 0])
        self.play(Write(eq), run_time=0.4)

        tens = VGroup()
        for i in range(10):
            col = i % 5
            row = i // 5
            tens.add(coin(-2.55 + col * 0.86, 1.05 - row * 0.92, "1 角",
                          BLUE, r=0.38, size=20))
        self.play(LaggedStart(*[FadeIn(c, scale=0.7) for c in tens], lag_ratio=0.06),
                  run_time=1.2)

        r1 = txt("十个 1 角", size=36, color=BLUE).move_to([3.6, 1.15, 0])
        r2 = txt("= 1 元", size=40, color=GOLD).move_to([3.6, 0.2, 0])
        r3 = txt("1 元 = 10 角", size=44, color=GREEN).move_to([3.6, -0.85, 0])
        self.play(Write(r1), run_time=0.5)
        self.play(Write(r2), run_time=0.5)
        self.play(FadeIn(r3, shift=UP * 0.1), run_time=0.6)
        self.finish_section()

        # ---------- 3. 1 角 = 10 分 ----------
        self.section(3, "一角可以换十个一分")
        self.play(FadeOut(one), FadeOut(eq), FadeOut(tens),
                  FadeOut(r1), FadeOut(r2), FadeOut(r3), run_time=0.5)

        one2 = coin(-5.4, 0.55, "1 角", BLUE, r=0.62, size=28)
        eq2 = txt("=", size=44, color=CHALK).move_to([-3.95, 0.55, 0])
        self.play(FadeIn(one2, scale=0.85), Write(eq2), run_time=0.7)

        fen = VGroup()
        for i in range(10):
            col = i % 5
            row = i // 5
            fen.add(coin(-2.75 + col * 0.78, 1.0 - row * 0.85, "1 分",
                         GREEN, r=0.34, size=18))
        self.play(LaggedStart(*[FadeIn(c, scale=0.7) for c in fen], lag_ratio=0.06),
                  run_time=1.2)

        g1 = txt("十个 1 分", size=36, color=GREEN).move_to([3.6, 1.15, 0])
        g2 = txt("= 1 角", size=40, color=BLUE).move_to([3.6, 0.2, 0])
        g3 = txt("1 角 = 10 分", size=44, color=GOLD).move_to([3.6, -0.85, 0])
        self.play(Write(g1), run_time=0.5)
        self.play(Write(g2), run_time=0.5)
        self.play(FadeIn(g3, shift=UP * 0.1), run_time=0.6)
        self.finish_section()

        # ---------- 4. 买一支笔 ----------
        self.section(4, "八角一支笔，给一元找两角")
        self.play(FadeOut(one2), FadeOut(eq2), FadeOut(fen),
                  FadeOut(g1), FadeOut(g2), FadeOut(g3), run_time=0.5)

        pbox = RoundedRectangle(corner_radius=0.1, width=1.5, height=0.5,
                                stroke_color=CHALK, stroke_width=2,
                                fill_color=CHALK, fill_opacity=0.08).move_to([-4.7, 1.2, 0])
        pbody = Line([-5.2, 1.2, 0], [-4.3, 1.2, 0], color=GOLD, stroke_width=6)
        plank = txt("8 角", size=28, color=GOLD).move_to([-4.7, 0.62, 0])
        self.play(Create(pbox), Create(pbody), FadeIn(plank), run_time=0.8)

        pay = coin(1.0, 1.2, "1 元", GOLD, r=0.62, size=30)
        self.play(FadeIn(pay, scale=0.85), run_time=0.6)

        ar = Arrow([-2.1, 0.55, 0], [-0.9, 1.0, 0], buff=0, color=DIM,
                   stroke_width=2.4, tip_length=0.16)
        self.play(GrowArrow(ar), run_time=0.5)

        back = coin(3.6, 1.2, "2 角", GREEN, r=0.52, size=26)
        self.play(FadeIn(back, scale=0.85), run_time=0.6)

        b1 = txt("1 元 = 10 角", size=38, color=GOLD).move_to([-2.6, -0.15, 0])
        b2 = txt("10 角 − 8 角 = 2 角", size=40, color=GREEN).move_to([-1.4, -1.05, 0])
        b3 = txt("应找回 2 角", size=38, color=CHALK).move_to([-1.4, -1.95, 0])
        self.play(Write(b1), run_time=0.6)
        self.play(Write(b2), run_time=0.7)
        self.play(FadeIn(b3, shift=UP * 0.1), run_time=0.6)
        self.finish_section()

        # ---------- 5. 付钱的组合 ----------
        self.section(5, "五角加两角加一角，正好八角")
        self.play(FadeOut(pbox), FadeOut(pbody), FadeOut(plank), FadeOut(pay),
                  FadeOut(ar), FadeOut(back), FadeOut(b1), FadeOut(b2), FadeOut(b3),
                  run_time=0.5)

        c5 = coin(-4.6, 0.9, "5 角", GOLD, r=0.56, size=26)
        plus1 = txt("+", size=38, color=DIM).move_to([-3.5, 0.9, 0])
        c2 = coin(-2.4, 0.9, "2 角", BLUE, r=0.46, size=24)
        plus2 = txt("+", size=38, color=DIM).move_to([-1.5, 0.9, 0])
        c1 = coin(-0.5, 0.9, "1 角", GREEN, r=0.42, size=22)
        self.play(FadeIn(c5, scale=0.85), run_time=0.6)
        self.play(FadeIn(plus1), FadeIn(c2, scale=0.85), run_time=0.6)
        self.play(FadeIn(plus2), FadeIn(c1, scale=0.85), run_time=0.6)

        s1 = txt("5 角 + 2 角 + 1 角 = 8 角", size=44, color=CHALK).move_to([0, -0.85, 0])
        self.play(Write(s1), run_time=0.8)

        s2 = txt("付钱可以几张几枚一起凑", size=32, color=GREEN).move_to([0, -1.95, 0])
        self.play(FadeIn(s2, shift=UP * 0.1), run_time=0.6)
        self.finish_section()

        # ---------- 6. 两句口诀 ----------
        self.section(6, "一元十角，一角十分")
        self.play(FadeOut(c5), FadeOut(plus1), FadeOut(c2), FadeOut(plus2),
                  FadeOut(c1), FadeOut(s1), FadeOut(s2), run_time=0.5)

        k1 = txt("1 元 = 10 角", size=56, color=GOLD).move_to([0, 1.3, 0])
        k2 = txt("1 角 = 10 分", size=56, color=BLUE).move_to([0, 0.1, 0])
        self.play(Write(k1), run_time=0.9)
        self.play(Write(k2), run_time=0.9)

        k3 = txt("都是满十进一", size=38, color=GREEN).move_to([0, -1.15, 0])
        self.play(FadeIn(k3, shift=UP * 0.1), run_time=0.7)

        fin = txt("认识人民币，买东西心不慌", size=28, color=DIM).move_to([0, -2.2, 0])
        self.play(FadeIn(fin), run_time=0.6)
        self.finish_section()

        self.play(FadeOut(k1), FadeOut(k2), FadeOut(k3), FadeOut(fin), run_time=0.6)