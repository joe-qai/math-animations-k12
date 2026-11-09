# -*- coding: utf-8 -*-
"""方差：先求差、再平方、后平均，越小越稳定。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403

A = [78, 79, 80, 81, 82]
B = [70, 75, 80, 85, 90]
A_DEV = [-2, -1, 0, 1, 2]
B_DEV = [-10, -5, 0, 5, 10]
A_SQ = [4, 1, 0, 1, 4]
B_SQ = [100, 25, 0, 25, 100]


def row(values, y: float, color: str, size: int = 26, dx: float = 1.0,
        x0: float = -5.35) -> VGroup:
    g = VGroup()
    for i, v in enumerate(values):
        s = str(v) if not isinstance(v, str) else v
        g.add(txt(s, size=size, color=color).move_to([x0 + i * dx, y, 0]))
    return g


class FangchaScene(NarratedScene):
    lesson = "fangcha"

    def construct(self):
        # ---------- 0. 平均分一样 ----------
        self.section(0, "平均分一样，成绩一样整齐吗")
        la = txt("甲班", size=26, color=GOLD).move_to([-6.55, 1.15, 0])
        lb = txt("乙班", size=26, color=BLUE).move_to([-6.55, 0.0, 0])
        ra = row(A, 1.15, GOLD)
        rb = row(B, 0.0, BLUE)
        self.play(FadeIn(la), FadeIn(lb), run_time=0.5)
        self.play(FadeIn(ra), FadeIn(rb), run_time=0.9)

        mean = txt("平均分都是 80", size=32, color=GREEN).move_to([3.5, 0.9, 0])
        ask = txt("谁的成绩更整齐？", size=34, color=GOLD).move_to([3.5, -0.15, 0])
        self.play(Write(mean), run_time=0.7)
        self.play(Write(ask), run_time=0.6)

        hint = txt("光看平均数看不出来", size=28, color=DIM).move_to([3.5, -1.2, 0])
        self.play(FadeIn(hint), run_time=0.5)
        self.finish_section()

        # ---------- 1. 每个数减平均数 ----------
        self.section(1, "先算每个数离平均数多远")
        self.play(FadeOut(mean), FadeOut(ask), FadeOut(hint), run_time=0.4)

        da = row(A_DEV, 1.15, GOLD)
        db = row(B_DEV, 0.0, BLUE)
        self.play(FadeIn(da), FadeIn(db), run_time=0.9)

        s1 = txt("每个数减 80", size=32, color=CHALK).move_to([3.6, 1.15, 0])
        s2 = txt("得到「离差」", size=32, color=GOLD).move_to([3.6, 0.3, 0])
        s3 = txt("有正有负", size=30, color=DIM).move_to([3.6, -0.6, 0])
        self.play(Write(s1), run_time=0.6)
        self.play(Write(s2), run_time=0.5)
        self.play(FadeIn(s3), run_time=0.5)

        s4 = txt("直接相加会互相抵消", size=30, color=RED).move_to([3.6, -1.6, 0])
        self.play(FadeIn(s4, shift=UP * 0.1), run_time=0.6)
        self.finish_section()

        # ---------- 2. 平方后再平均 ----------
        self.section(2, "平方，就不会抵消了")
        self.play(FadeOut(da), FadeOut(db), FadeOut(s1), FadeOut(s2),
                  FadeOut(s3), FadeOut(s4), run_time=0.5)

        qa = row(A_SQ, 1.15, GOLD)
        qb = row(B_SQ, 0.0, BLUE)
        self.play(FadeIn(qa), FadeIn(qb), run_time=0.9)

        t1 = txt("每个离差平方", size=32, color=CHALK).move_to([3.6, 1.3, 0])
        t2 = txt("再求平均数", size=32, color=GOLD).move_to([3.6, 0.45, 0])
        self.play(Write(t1), run_time=0.6)
        self.play(Write(t2), run_time=0.5)

        t3 = txt("甲班：(4+1+0+1+4)÷5 = 2", size=26, color=GOLD).move_to([0, -1.0, 0])
        t4 = txt("乙班：(100+25+0+25+100)÷5 = 50", size=26, color=BLUE).move_to([0, -1.75, 0])
        self.play(FadeIn(t3), run_time=0.6)
        self.play(FadeIn(t4), run_time=0.6)
        self.finish_section()

        # ---------- 3. 方差 ----------
        self.section(3, "这个平均数，就叫方差")
        self.play(FadeOut(qa), FadeOut(qb), FadeOut(t1), FadeOut(t2),
                  FadeOut(t3), FadeOut(t4), FadeOut(la), FadeOut(lb),
                  FadeOut(ra), FadeOut(rb), run_time=0.5)

        f1 = txt("s² = (x₁−x̄)² + … + (xₙ−x̄)²  ÷ n", size=38, color=GOLD)
        f1.move_to([0, 0.95, 0])
        self.play(Write(f1), run_time=1.2)

        f2 = txt("先求离差，再平方，最后平均", size=32, color=CHALK).move_to([0, -0.3, 0])
        self.play(FadeIn(f2), run_time=0.6)

        f3 = txt("方差衡量的，是数据的波动大小", size=30, color=DIM).move_to([0, -1.35, 0])
        self.play(FadeIn(f3), run_time=0.5)
        self.finish_section()

        # ---------- 4. 越小越稳定 ----------
        self.section(4, "方差越小，数据越稳定")
        self.play(FadeOut(f1), FadeOut(f2), FadeOut(f3), run_time=0.5)

        small = label_box("方差小", size=34, color=GREEN).move_to([-4.2, 1.0, 0])
        small2 = txt("→ 数据集中、整齐", size=32, color=GREEN).move_to([2.4, 1.0, 0])
        big = label_box("方差大", size=34, color=RED).move_to([-4.2, -0.45, 0])
        big2 = txt("→ 数据分散、波动大", size=32, color=RED).move_to([2.4, -0.45, 0])
        self.play(FadeIn(small, shift=UP * 0.1), run_time=0.5)
        self.play(FadeIn(small2), run_time=0.5)
        self.play(FadeIn(big, shift=UP * 0.1), run_time=0.5)
        self.play(FadeIn(big2), run_time=0.5)

        note = txt("所以 2 ＜ 50，甲班更整齐", size=32, color=GOLD).move_to([0, -1.7, 0])
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.6)
        self.finish_section()

        # ---------- 5. 例题 ----------
        self.section(5, "一组数据，算出方差")
        self.play(FadeOut(small), FadeOut(small2), FadeOut(big), FadeOut(big2),
                  FadeOut(note), run_time=0.5)

        g1 = txt("数据：3, 5, 7, 9, 11", size=34, color=CHALK).move_to([0, 1.55, 0])
        g2 = txt("平均数是 7", size=34, color=GOLD).move_to([0, 0.65, 0])
        g3 = txt("离差：−4, −2, 0, 2, 4", size=32, color=BLUE).move_to([0, -0.2, 0])
        g4 = txt("平方和：16+4+0+4+16 = 40", size=32, color=BLUE).move_to([0, -1.05, 0])
        g5 = txt("方差：40 ÷ 5 = 8", size=38, color=GREEN).move_to([0, -1.95, 0])
        for g in (g1, g2, g3, g4, g5):
            self.play(FadeIn(g, shift=UP * 0.08), run_time=0.55)
        self.finish_section()

        # ---------- 6. 口诀 ----------
        self.section(6, "先求差、再平方、后平均")
        self.play(FadeOut(g1), FadeOut(g2), FadeOut(g3), FadeOut(g4), FadeOut(g5),
                  run_time=0.5)

        k1 = txt("求差 → 平方 → 平均", size=48, color=GOLD).move_to([0, 1.2, 0])
        k2 = txt("方差越小越稳定", size=46, color=GREEN).move_to([0, 0.1, 0])
        self.play(Write(k1), run_time=0.9)
        self.play(Write(k2), run_time=0.8)

        fin = txt("比较整齐程度，就看方差", size=28, color=DIM).move_to([0, -1.15, 0])
        self.play(FadeIn(fin), run_time=0.5)
        self.finish_section()

        self.play(FadeOut(k1), FadeOut(k2), FadeOut(fin), run_time=0.6)