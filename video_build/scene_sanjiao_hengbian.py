# -*- coding: utf-8 -*-
"""三角恒等变换：余弦相反，正弦相同。"""

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


def ltxt(s: str, y: float, size: int = 30, color: str = CHALK,
         width: float = 5.5, x: float = -4.0) -> Text:
    m = txt(s, size=size, color=color)
    if m.width > width:
        m.scale_to_fit_width(width)
    m.move_to([x, y, 0])
    return m


class SanjiaoHengbianScene(NarratedScene):
    lesson = "sanjiao-hengbian"

    def construct(self):
        # ---------- 0. 从求 cos15° 说起 ----------
        self.section(0, "从求 cos15° 说起")
        c = np.array([-4.85, 0.75, 0])
        r = 1.45
        wheel = Circle(radius=r, color=BLUE, stroke_width=2.4).move_to(c)
        xaxis = Line(c + LEFT * (r + 0.35), c + RIGHT * (r + 0.35), color=DIM, stroke_width=2)
        self.play(Create(wheel), Create(xaxis), run_time=0.8)

        def ray(deg: float):
            a = np.deg2rad(deg)
            return Line(c, c + r * np.array([np.cos(a), np.sin(a), 0]),
                        color=CHALK, stroke_width=2.2)

        r30 = ray(30)
        r45 = ray(45)
        self.play(Create(r30), run_time=0.5)
        self.play(Create(r45), run_time=0.5)

        wedge = Arc(radius=1.0, start_angle=np.deg2rad(30), angle=np.deg2rad(15),
                    arc_center=c, color=GOLD, stroke_width=5)
        self.play(Create(wedge), run_time=0.7)

        l30 = txt("30°", size=22, color=DIM).move_to(c + 1.74 * np.array(
            [np.cos(np.deg2rad(12)), np.sin(np.deg2rad(12)), 0]))
        l45 = txt("45°", size=22, color=DIM).move_to(c + 1.74 * np.array(
            [np.cos(np.deg2rad(58)), np.sin(np.deg2rad(58)), 0]))
        l15 = txt("15°", size=24, color=GOLD).move_to(c + 1.74 * np.array(
            [np.cos(np.deg2rad(35)), np.sin(np.deg2rad(35)), 0]))
        self.play(FadeIn(l30), FadeIn(l45), FadeIn(l15), run_time=0.6)

        f = txt("15° = 45° − 30°", size=36, color=GREEN).move_to([-4.85, -1.35, 0])
        self.play(Write(f), run_time=0.7)

        r1 = rtxt("15° 不是特殊角", 1.45, 30)
        r2 = rtxt("但 15° = 45° − 30°", 0.5, 31, GOLD)
        r3 = rtxt("两个特殊角之差", -0.55, 29, GREEN)
        r4 = rtxt("能不能用公式把它算出来？", -1.6, 26, DIM)
        for m in (r1, r2, r3, r4):
            self.play(Write(m), run_time=0.5)
        self.finish_section()

        # ---------- 1. 两角差的余弦 ----------
        self.section(1, "两角差的余弦")
        self.play(FadeOut(wheel), FadeOut(xaxis), FadeOut(r30), FadeOut(r45),
                  FadeOut(wedge), FadeOut(l30), FadeOut(l45), FadeOut(l15), FadeOut(f),
                  FadeOut(r1), FadeOut(r2), FadeOut(r3), FadeOut(r4), run_time=0.5)

        f1 = ltxt("cos(α − β) = cosα cosβ + sinα sinβ", 1.5, 29, GOLD, width=5.6)
        self.play(Write(f1), run_time=0.9)

        s1 = ltxt("cos(45° − 30°)", 0.55, 31, CHALK)
        s2 = ltxt("= cos45°cos30° + sin45°sin30°", -0.3, 24, CHALK, width=5.4)
        s3 = ltxt("= (√6 + √2) / 4", -1.3, 32, GREEN)
        for m in (s1, s2, s3):
            self.play(Write(m), run_time=0.55)

        r1 = rtxt("cos(α−β) = cosαcosβ + sinαsinβ", 1.45, 25, GOLD)
        r2 = rtxt("注意：中间是加号", 0.5, 31, GREEN)
        r3 = rtxt("例：cos15° = (√6+√2)/4", -0.55, 26)
        r4 = rtxt("这是所有和差角公式的起点", -1.6, 25, DIM)
        for m in (r1, r2, r3, r4):
            self.play(Write(m), run_time=0.5)
        self.finish_section()

        # ---------- 2. 和角与差角的正弦 ----------
        self.section(2, "和角与差角的正弦")
        self.play(FadeOut(f1), FadeOut(s1), FadeOut(s2), FadeOut(s3),
                  FadeOut(r1), FadeOut(r2), FadeOut(r3), FadeOut(r4), run_time=0.5)

        c1 = label_box("sin(α + β) = sinαcosβ + cosαsinβ", size=22, color=GOLD)
        c1.move_to([-4.0, 1.45, 0])
        c2 = label_box("sin(α − β) = sinαcosβ − cosαsinβ", size=22, color=GREEN)
        c2.move_to([-4.0, 0.35, 0])
        self.play(FadeIn(c1), run_time=0.8)
        self.play(FadeIn(c2), run_time=0.8)

        n1 = ltxt("符号和括号里一致", -0.75, 29, GOLD)
        n2 = ltxt("余弦则相反：中间变号", -1.65, 27, BLUE)
        self.play(Write(n1), run_time=0.5)
        self.play(Write(n2), run_time=0.5)

        r1 = rtxt("正弦：中间符号与括号一致", 1.45, 27, GOLD)
        r2 = rtxt("余弦：中间符号与括号相反", 0.5, 27, BLUE)
        r3 = rtxt("cos(α+β) = cosαcosβ − sinαsinβ", -0.55, 25)
        r4 = rtxt("把 β 换成 −β 就能推出来", -1.6, 26, DIM)
        for m in (r1, r2, r3, r4):
            self.play(Write(m), run_time=0.5)
        self.finish_section()

        # ---------- 3. 正切公式与二倍角 ----------
        self.section(3, "正切公式与二倍角")
        self.play(FadeOut(c1), FadeOut(c2), FadeOut(n1), FadeOut(n2),
                  FadeOut(r1), FadeOut(r2), FadeOut(r3), FadeOut(r4), run_time=0.5)

        f1 = ltxt("tan(α ± β) = (tanα ± tanβ) / (1 ∓ tanα·tanβ)",
                  1.45, 24, GOLD, width=5.3)
        self.play(Write(f1), run_time=0.9)
        n1 = ltxt("分母符号与分子相反", 0.55, 27, DIM)
        self.play(Write(n1), run_time=0.5)

        f2 = ltxt("sin2α = 2sinαcosα", -0.4, 32, GREEN)
        f3 = ltxt("cos2α = cos²α − sin²α", -1.25, 28, BLUE)
        f4 = ltxt("= 1 − 2sin²α = 2cos²α − 1", -1.9, 25, CHALK)
        self.play(Write(f2), run_time=0.6)
        self.play(Write(f3), run_time=0.6)
        self.play(Write(f4), run_time=0.6)

        r1 = rtxt("分母符号与分子相反", 1.45, 28, DIM)
        r2 = rtxt("令 β = α，就得到二倍角", 0.5, 27)
        r3 = rtxt("cos2α 有三种等价写法", -0.55, 28, BLUE)
        r4 = rtxt("按已知条件选最方便的那个", -1.6, 26, DIM)
        for m in (r1, r2, r3, r4):
            self.play(Write(m), run_time=0.5)
        self.finish_section()

        # ---------- 4. 辅助角公式 ----------
        self.section(4, "辅助角公式")
        self.play(FadeOut(f1), FadeOut(n1), FadeOut(f2), FadeOut(f3), FadeOut(f4),
                  FadeOut(r1), FadeOut(r2), FadeOut(r3), FadeOut(r4), run_time=0.5)

        A = np.array([-6.05, -0.85, 0])
        B = np.array([-3.55, -0.85, 0])
        C = np.array([-3.55, 1.05, 0])
        tri = VGroup(
            Line(A, B, color=BLUE, stroke_width=3),
            Line(B, C, color=GREEN, stroke_width=3),
            Line(A, C, color=GOLD, stroke_width=3),
        )
        self.play(Create(tri[0]), run_time=0.5)
        self.play(Create(tri[1]), run_time=0.5)
        self.play(Create(tri[2]), run_time=0.6)

        ang = np.arctan2(C[1] - A[1], C[0] - A[0])
        arc = Arc(radius=0.58, start_angle=0, angle=ang, arc_center=A,
                  color=GOLD, stroke_width=2.4)
        phi = txt("φ", size=24, color=GOLD).move_to(
            A + 0.82 * np.array([np.cos(ang / 2), np.sin(ang / 2), 0]))
        self.play(Create(arc), FadeIn(phi), run_time=0.6)

        lb = txt("b", size=24, color=BLUE).move_to([(A[0] + B[0]) / 2, -1.18, 0])
        la = txt("a", size=24, color=GREEN).move_to([-3.22, 0.1, 0])
        lh = txt("√(a²+b²)", size=21, color=GOLD).move_to([-5.1, 0.45, 0])
        self.play(FadeIn(lb), FadeIn(la), FadeIn(lh), run_time=0.6)

        f = ltxt("a sinx + b cosx = √(a²+b²) sin(x+φ)", -1.65, 25, CHALK, width=5.6)
        self.play(Write(f), run_time=0.8)

        r1 = rtxt("a sinx + b cosx", 1.45, 30, CHALK)
        r2 = rtxt("= √(a²+b²) sin(x+φ)", 0.5, 29, GOLD)
        r3 = rtxt("其中 tanφ = b/a", -0.55, 29, GREEN)
        r4 = rtxt("最值 ±√(a²+b²)，周期不变", -1.6, 25, DIM)
        for m in (r1, r2, r3, r4):
            self.play(Write(m), run_time=0.5)
        self.finish_section()

        # ---------- 5. 化简求值套路 ----------
        self.section(5, "化简求值三步")
        self.play(FadeOut(tri), FadeOut(arc), FadeOut(phi), FadeOut(lb), FadeOut(la),
                  FadeOut(lh), FadeOut(f),
                  FadeOut(r1), FadeOut(r2), FadeOut(r3), FadeOut(r4), run_time=0.5)

        c1 = label_box("一看角：化成同角或倍数", size=25, color=GOLD)
        c1.move_to([-4.1, 1.35, 0])
        c2 = label_box("二看名：切化弦，统一函数名", size=24, color=GREEN)
        c2.move_to([-4.1, 0.25, 0])
        c3 = label_box("三看结构：平方差、完全平方", size=23, color=BLUE)
        c3.move_to([-4.1, -0.85, 0])
        self.play(FadeIn(c1), run_time=0.7)
        self.play(FadeIn(c2), run_time=0.7)
        self.play(FadeIn(c3), run_time=0.7)

        goal = txt("目标：项数少、次数低、函数名少", size=24, color=DIM)
        goal.move_to([-4.1, -1.9, 0])
        self.play(Write(goal), run_time=0.6)

        r1 = rtxt("看角：化同角或成倍数", 1.45, 27)
        r2 = rtxt("看名：切化弦，统一函数名", 0.5, 27, GREEN)
        r3 = rtxt("看结构：平方差、完全平方、辅助角", -0.55, 24, BLUE)
        r4 = rtxt("目标：项数少、次数低、函数名少", -1.6, 24, DIM)
        for m in (r1, r2, r3, r4):
            self.play(Write(m), run_time=0.5)
        self.finish_section()

        # ---------- 6. 口诀 ----------
        self.section(6, "记一句话")
        self.play(FadeOut(c1), FadeOut(c2), FadeOut(c3), FadeOut(goal),
                  FadeOut(r1), FadeOut(r2), FadeOut(r3), FadeOut(r4), run_time=0.5)

        k1 = txt("余弦相反，正弦相同", size=54, color=GOLD).move_to([0, 1.0, 0])
        k2 = txt("余弦的差角中间是加号", size=30, color=CHALK).move_to([0, -0.1, 0])
        k3 = txt("正弦的和角中间是加号", size=30, color=GREEN).move_to([0, -1.15, 0])
        self.play(Write(k1), run_time=0.9)
        self.play(Write(k2), run_time=0.7)
        self.play(Write(k3), run_time=0.7)
        self.finish_section()

        self.play(FadeOut(k1), FadeOut(k2), FadeOut(k3), run_time=0.6)