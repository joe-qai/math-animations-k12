# -*- coding: utf-8 -*-
"""代数式求值：代入、按顺序算、能整体代入就别拆开。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


class DaishushiQiuzhiScene(NarratedScene):
    lesson = "daishushi-qiuzhi"

    def construct(self):
        # ---------- 0. 已知字母的值 ----------
        self.section(0, "知道字母的值，就能算出结果")
        g1 = txt("已知 a = 3，b = −2", size=42, color=GOLD).move_to([0, 1.35, 0])
        self.play(Write(g1), run_time=0.9)

        g2 = txt("求 2a + b 的值", size=46, color=CHALK).move_to([0, 0.2, 0])
        self.play(Write(g2), run_time=0.9)

        g3 = txt("把字母换成数，就叫「求值」", size=30, color=DIM).move_to([0, -1.05, 0])
        self.play(FadeIn(g3, shift=UP * 0.1), run_time=0.6)
        self.finish_section()

        # ---------- 1. 代入 ----------
        self.section(1, "第一步：把字母换成数")
        self.play(FadeOut(g1), FadeOut(g2), FadeOut(g3), run_time=0.4)

        s1 = txt("2a + b", size=54, color=CHALK).move_to([-3.4, 1.35, 0])
        self.play(Write(s1), run_time=0.7)

        arr = Arrow([-3.4, 0.85, 0], [-3.4, 0.2, 0], buff=0, color=DIM,
                    stroke_width=2.4, tip_length=0.16)
        self.play(GrowArrow(arr), run_time=0.5)

        s2 = txt("2 × 3 + (−2)", size=50, color=GOLD).move_to([-3.4, -0.5, 0])
        self.play(Write(s2), run_time=0.9)

        n1 = txt("a 换成 3", size=30, color=GOLD).move_to([3.5, 1.15, 0])
        n2 = txt("b 换成 −2", size=30, color=ORANGE).move_to([3.5, 0.3, 0])
        self.play(Write(n1), run_time=0.5)
        self.play(Write(n2), run_time=0.5)
        self.finish_section()

        # ---------- 2. 两个注意 ----------
        self.section(2, "代入时的两个注意")
        self.play(FadeOut(s1), FadeOut(arr), FadeOut(s2), FadeOut(n1), FadeOut(n2),
                  run_time=0.4)

        w1 = label_box("负数要加括号", size=34, color=ORANGE).move_to([-3.5, 1.25, 0])
        w1b = txt("写成 (−2)，不写 −2 单独放", size=26, color=DIM).move_to([0, 0.35, 0])
        self.play(FadeIn(w1, shift=UP * 0.1), run_time=0.6)
        self.play(FadeIn(w1b), run_time=0.5)

        w2 = label_box("乘号不能省", size=34, color=GOLD).move_to([-3.7, -0.65, 0])
        w2b = txt("2a 要写成 2 × a，不能写 2a 直接代", size=26, color=DIM)
        w2b.move_to([0, -1.55, 0])
        self.play(FadeIn(w2, shift=UP * 0.1), run_time=0.6)
        self.play(FadeIn(w2b), run_time=0.5)
        self.finish_section()

        # ---------- 3. 按顺序算 ----------
        self.section(3, "第二步：按运算顺序算")
        self.play(FadeOut(w1), FadeOut(w1b), FadeOut(w2), FadeOut(w2b), run_time=0.5)

        c1 = txt("2 × 3 + (−2)", size=46, color=CHALK).move_to([0, 1.5, 0])
        c2 = txt("= 6 + (−2)", size=46, color=CHALK).move_to([0, 0.55, 0])
        c3 = txt("= 6 − 2", size=46, color=BLUE).move_to([0, -0.4, 0])
        c4 = txt("= 4", size=56, color=GREEN).move_to([0, -1.5, 0])
        self.play(Write(c1), run_time=0.7)
        self.play(Write(c2), run_time=0.7)
        self.play(Write(c3), run_time=0.6)
        self.play(Write(c4), run_time=0.7)
        self.finish_section()

        # ---------- 4. 整体代入 ----------
        self.section(4, "能整体代入，就别拆开")
        self.play(FadeOut(c1), FadeOut(c2), FadeOut(c3), FadeOut(c4), run_time=0.5)

        h1 = txt("已知 x + y = 5", size=42, color=GOLD).move_to([0, 1.45, 0])
        h2 = txt("求 2x + 2y", size=42, color=CHALK).move_to([0, 0.5, 0])
        self.play(Write(h1), run_time=0.7)
        self.play(Write(h2), run_time=0.6)

        h3 = txt("2x + 2y = 2(x + y)", size=44, color=BLUE).move_to([0, -0.6, 0])
        h4 = txt("= 2 × 5 = 10", size=44, color=GREEN).move_to([0, -1.6, 0])
        self.play(Write(h3), run_time=0.8)
        self.play(Write(h4), run_time=0.7)
        self.finish_section()

        # ---------- 5. 易错对比 ----------
        self.section(5, "a² 和 2a 不是一回事")
        self.play(FadeOut(h1), FadeOut(h2), FadeOut(h3), FadeOut(h4), run_time=0.5)

        e1 = txt("a = 3 时", size=34, color=DIM).move_to([0, 1.5, 0])
        self.play(FadeIn(e1), run_time=0.5)

        e2 = txt("a² = 3 × 3 = 9", size=44, color=GOLD).move_to([-3.5, 0.45, 0])
        e3 = txt("2a = 2 × 3 = 6", size=44, color=BLUE).move_to([3.5, 0.45, 0])
        self.play(Write(e2), run_time=0.7)
        self.play(Write(e3), run_time=0.7)

        e4 = txt("a² 是 a 乘 a，2a 是 2 乘 a", size=30, color=CHALK).move_to([0, -0.75, 0])
        self.play(FadeIn(e4), run_time=0.6)

        e5 = txt("把 a² 算成 2a，是最常见的错", size=28, color=RED).move_to([0, -1.7, 0])
        self.play(FadeIn(e5), run_time=0.5)
        self.finish_section()

        # ---------- 6. 口诀 ----------
        self.section(6, "先代入，再计算")
        self.play(FadeOut(e1), FadeOut(e2), FadeOut(e3), FadeOut(e4), FadeOut(e5),
                  run_time=0.5)

        k1 = txt("先代入 → 再计算", size=48, color=GOLD).move_to([0, 1.15, 0])
        k2 = txt("负数加括号，乘号不省", size=40, color=CHALK).move_to([0, 0.1, 0])
        k3 = txt("能整体代入，就别拆开", size=40, color=GREEN).move_to([0, -0.95, 0])
        self.play(Write(k1), run_time=0.8)
        self.play(Write(k2), run_time=0.8)
        self.play(Write(k3), run_time=0.8)

        fin = txt("代入法，是代数式的第一课", size=28, color=DIM).move_to([0, -2.0, 0])
        self.play(FadeIn(fin), run_time=0.5)
        self.finish_section()

        self.play(FadeOut(k1), FadeOut(k2), FadeOut(k3), FadeOut(fin), run_time=0.6)