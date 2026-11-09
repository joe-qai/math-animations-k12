# -*- coding: utf-8 -*-
"""梯形：只有一组对边平行，等腰梯形两底角相等，中位线是上下底和的一半。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


def trap(cx: float = -3.9, cy: float = -0.25, bottom: float = 4.0,
         top: float = 1.9, h: float = 2.1, offset: float = 0.0,
         color: str = CHALK, width: float = 2.6, opacity: float = 0.09) -> Polygon:
    bl = [cx - bottom / 2, cy - h / 2, 0]
    br = [cx + bottom / 2, cy - h / 2, 0]
    tr = [cx + top / 2 + offset, cy + h / 2, 0]
    tl = [cx - top / 2 + offset, cy + h / 2, 0]
    return Polygon(bl, br, tr, tl, stroke_color=color, stroke_width=width,
                   fill_color=BLUE, fill_opacity=opacity)


class TixingTuxingScene(NarratedScene):
    lesson = "tixing-tuxing"

    def construct(self):
        # ---------- 0. 堤坝和梯子 ----------
        self.section(0, "只有一组对边平行的四边形")
        t = trap(offset=0.45)
        self.play(Create(t), run_time=1.0)

        q1 = txt("堤坝的横截面", size=34, color=CHALK).move_to([3.5, 1.25, 0])
        q2 = txt("梯子的侧面", size=34, color=CHALK).move_to([3.5, 0.35, 0])
        self.play(Write(q1), run_time=0.5)
        self.play(Write(q2), run_time=0.5)

        q3 = txt("都是只有一组对边平行", size=32, color=GOLD).move_to([3.5, -0.7, 0])
        self.play(Write(q3), run_time=0.6)

        q4 = txt("这样的四边形，叫梯形", size=30, color=GREEN).move_to([3.5, -1.65, 0])
        self.play(FadeIn(q4, shift=UP * 0.1), run_time=0.6)
        self.finish_section()

        # ---------- 1. 上底、下底、腰 ----------
        self.section(1, "上底、下底和两条腰")
        self.play(FadeOut(q1), FadeOut(q2), FadeOut(q3), FadeOut(q4), run_time=0.4)

        top_line = Line([-4.85, 0.8, 0], [-2.95, 0.8, 0], color=GOLD, stroke_width=5)
        bot_line = Line([-5.9, -1.3, 0], [-1.9, -1.3, 0], color=BLUE, stroke_width=5)
        self.play(Create(top_line), run_time=0.6)
        self.play(Create(bot_line), run_time=0.6)

        l1 = txt("上底", size=26, color=GOLD).move_to([-6.5, 0.85, 0])
        l2 = txt("下底", size=26, color=BLUE).move_to([-6.6, -1.3, 0])
        l3 = txt("腰", size=26, color=ORANGE).move_to([-6.2, -0.1, 0])
        self.play(FadeIn(l1), FadeIn(l2), FadeIn(l3), run_time=0.7)

        t1 = txt("平行的两条边", size=32, color=GOLD).move_to([3.5, 1.05, 0])
        t2 = txt("叫上底和下底", size=32, color=GOLD).move_to([3.5, 0.15, 0])
        self.play(Write(t1), run_time=0.5)
        self.play(Write(t2), run_time=0.5)

        t3 = txt("另两条不平行的边叫腰", size=30, color=ORANGE).move_to([3.5, -0.85, 0])
        self.play(FadeIn(t3), run_time=0.6)

        t4 = txt("上底短、下底长，是一般情况", size=26, color=DIM).move_to([3.5, -1.8, 0])
        self.play(FadeIn(t4), run_time=0.5)
        self.finish_section()

        # ---------- 2. 等腰梯形 ----------
        self.section(2, "两腰相等，就是等腰梯形")
        self.play(FadeOut(t), FadeOut(top_line), FadeOut(bot_line), FadeOut(l1),
                  FadeOut(l2), FadeOut(l3), FadeOut(t1), FadeOut(t2), FadeOut(t3),
                  FadeOut(t4), run_time=0.5)

        iso = trap(offset=0.0)
        self.play(Create(iso), run_time=0.9)

        legL = Line([-5.9, -1.3, 0], [-4.85, 0.8, 0], color=ORANGE, stroke_width=4.5)
        legR = Line([-1.9, -1.3, 0], [-2.95, 0.8, 0], color=ORANGE, stroke_width=4.5)
        self.play(Create(legL), run_time=0.5)
        self.play(Create(legR), run_time=0.5)

        a1 = txt("两腰相等", size=36, color=ORANGE).move_to([3.5, 1.25, 0])
        a2 = txt("同一底上的两个角也相等", size=30, color=GOLD).move_to([3.5, 0.3, 0])
        self.play(Write(a1), run_time=0.6)
        self.play(Write(a2), run_time=0.6)

        ang_bl = txt("∠1", size=24, color=GREEN).move_to([-5.5, -0.95, 0])
        ang_br = txt("∠1", size=24, color=GREEN).move_to([-2.3, -0.95, 0])
        self.play(FadeIn(ang_bl), FadeIn(ang_br), run_time=0.6)

        a3 = txt("上底两个角也相等，各是它的补角", size=26, color=DIM)
        a3.move_to([3.5, -0.85, 0])
        self.play(FadeIn(a3), run_time=0.5)
        self.finish_section()

        # ---------- 3. 对角线相等 ----------
        self.section(3, "等腰梯形的对角线相等")
        self.play(FadeOut(a1), FadeOut(a2), FadeOut(a3), FadeOut(ang_bl),
                  FadeOut(ang_br), FadeOut(legL), FadeOut(legR), run_time=0.5)

        d1 = Line([-5.9, -1.3, 0], [-2.95, 0.8, 0], color=BLUE, stroke_width=3)
        d2 = Line([-1.9, -1.3, 0], [-4.85, 0.8, 0], color=BLUE, stroke_width=3)
        self.play(Create(d1), run_time=0.7)
        self.play(Create(d2), run_time=0.7)

        b1 = txt("两条对角线一样长", size=34, color=BLUE).move_to([3.5, 1.1, 0])
        b2 = txt("这也是等腰梯形常用的性质", size=28, color=CHALK).move_to([3.5, 0.1, 0])
        self.play(Write(b1), run_time=0.6)
        self.play(FadeIn(b2), run_time=0.5)

        b3 = txt("普通梯形没有这个性质", size=28, color=RED).move_to([3.5, -1.0, 0])
        self.play(FadeIn(b3), run_time=0.5)
        self.finish_section()

        # ---------- 4. 直角梯形 ----------
        self.section(4, "有一个角是直角，就是直角梯形")
        self.play(FadeOut(iso), FadeOut(d1), FadeOut(d2), FadeOut(b1), FadeOut(b2),
                  FadeOut(b3), run_time=0.5)

        rt = Polygon([-5.9, -1.3, 0], [-1.9, -1.3, 0], [-2.95, 0.8, 0], [-5.9, 0.8, 0],
                     stroke_color=CHALK, stroke_width=2.6, fill_color=GREEN,
                     fill_opacity=0.09)
        self.play(Create(rt), run_time=0.9)

        c1 = txt("两个直角", size=34, color=GREEN).move_to([3.5, 1.2, 0])
        c2 = txt("垂直的那条腰，就是高", size=32, color=GOLD).move_to([3.5, 0.25, 0])
        self.play(Write(c1), run_time=0.6)
        self.play(Write(c2), run_time=0.6)

        c3 = txt("直角梯形在求面积时最好用", size=28, color=DIM).move_to([3.5, -0.85, 0])
        self.play(FadeIn(c3), run_time=0.5)

        sq1 = VGroup(
            Line([-5.9, -1.05, 0], [-5.65, -1.05, 0], color=GOLD, stroke_width=1.8),
            Line([-5.65, -1.05, 0], [-5.65, -1.3, 0], color=GOLD, stroke_width=1.8),
        )
        self.play(Create(sq1), run_time=0.5)
        self.finish_section()

        # ---------- 5. 中位线与面积 ----------
        self.section(5, "中位线是上下底和的一半")
        self.play(FadeOut(rt), FadeOut(c1), FadeOut(c2), FadeOut(c3), FadeOut(sq1),
                  run_time=0.5)

        iso2 = trap(cx=-4.95, cy=0.55, bottom=2.9, top=1.5, h=1.7, offset=0.0)
        self.play(Create(iso2), run_time=0.8)

        mid = Line([-6.075, 0.55, 0], [-3.825, 0.55, 0], color=ORANGE, stroke_width=4.5)
        self.play(Create(mid), run_time=0.8)

        d1 = txt("中位线 = (上底 + 下底) ÷ 2", size=28, color=ORANGE).move_to([3.55, 1.45, 0])
        d2 = txt("= (2.4 + 4) ÷ 2 = 3.2", size=28, color=ORANGE).move_to([3.55, 0.7, 0])
        self.play(Write(d1), run_time=0.7)
        self.play(Write(d2), run_time=0.6)

        d3 = txt("面积 = (上底 + 下底) × 高 ÷ 2", size=28, color=GOLD).move_to([3.55, -0.2, 0])
        d4 = txt("也可以写成：中位线 × 高", size=28, color=GREEN).move_to([3.55, -1.05, 0])
        self.play(Write(d3), run_time=0.7)
        self.play(FadeIn(d4, shift=UP * 0.1), run_time=0.6)
        self.finish_section()

        # ---------- 6. 口诀 ----------
        self.section(6, "一组对边平行，等腰梯形两底角相等")
        self.play(FadeOut(iso2), FadeOut(mid), FadeOut(d1), FadeOut(d2),
                  FadeOut(d3), FadeOut(d4), run_time=0.5)

        k1 = txt("只有一组对边平行", size=44, color=GOLD).move_to([0, 1.2, 0])
        k2 = txt("等腰梯形：两腰相等、两底角相等", size=36, color=CHALK)
        k2.move_to([0, 0.25, 0])
        k3 = txt("中位线 = 上下底和的一半", size=36, color=GREEN).move_to([0, -0.75, 0])
        self.play(Write(k1), run_time=0.8)
        self.play(Write(k2), run_time=0.8)
        self.play(Write(k3), run_time=0.8)

        fin = txt("梯形，是平行四边形被截去一半的样子", size=28, color=DIM)
        fin.move_to([0, -1.85, 0])
        self.play(FadeIn(fin), run_time=0.5)
        self.finish_section()

        self.play(FadeOut(k1), FadeOut(k2), FadeOut(k3), FadeOut(fin), run_time=0.6)