# -*- coding: utf-8 -*-
"""三角函数定义与诱导公式：一全正，二正弦。"""

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


def polar(c, r: float, deg: float):
    a = np.deg2rad(deg)
    return c + r * np.array([np.cos(a), np.sin(a), 0])


class SanjiaoDingyiScene(NarratedScene):
    lesson = "sanjiao-dingyi"

    def construct(self):
        # ---------- 0. 从摩天轮说起 ----------
        self.section(0, "从摩天轮说起")
        c = np.array([-4.25, 0.55, 0])
        r = 1.62
        wheel = Circle(radius=r, color=BLUE, stroke_width=2.6).move_to(c)
        bar = Line(c + LEFT * r, c + RIGHT * r, color=DIM, stroke_width=2)
        self.play(Create(wheel), Create(bar), run_time=0.9)

        passengers = VGroup()
        for deg in (140, 205, 265, 320):
            d = Dot(polar(c, r, deg), radius=0.1, color=DIM)
            passengers.add(d)
        self.play(FadeIn(passengers), run_time=0.6)

        p = polar(c, r, 52)
        rad = Line(c, p, color=GOLD, stroke_width=2.6)
        cabin = Dot(p, radius=0.15, color=GOLD)
        self.play(Create(rad), FadeIn(cabin), run_time=0.8)

        drop = DashedLine(p, [p[0], c[1], 0], color=GREEN, stroke_width=2.2)
        self.play(Create(drop), run_time=0.6)

        arc = Arc(radius=0.62, start_angle=0, angle=np.deg2rad(52),
                  arc_center=c, color=GOLD, stroke_width=2.4)
        al = txt("α", size=24, color=GOLD).move_to(polar(c, 0.9, 26))
        self.play(Create(arc), FadeIn(al), run_time=0.5)

        r1 = rtxt("摩天轮上，座舱的高度随角度变化", 1.45, 26)
        r2 = rtxt("角度确定，高度就确定", 0.5, 30, GOLD)
        r3 = rtxt("这就是三角函数要描述的关系", -0.55, 27)
        r4 = rtxt("关键在于：先把角放到圆上", -1.6, 27, GREEN)
        for m in (r1, r2, r3, r4):
            self.play(Write(m), run_time=0.5)
        self.finish_section()

        # ---------- 1. 任意角与弧度制 ----------
        self.section(1, "任意角与弧度制")
        self.play(FadeOut(wheel), FadeOut(bar), FadeOut(passengers), FadeOut(rad),
                  FadeOut(cabin), FadeOut(drop), FadeOut(arc), FadeOut(al),
                  FadeOut(r1), FadeOut(r2), FadeOut(r3), FadeOut(r4), run_time=0.5)

        c = np.array([-4.3, 0.35, 0])
        r = 1.55
        wheel = Circle(radius=r, color=BLUE, stroke_width=2.6).move_to(c)
        xaxis = Line(c + LEFT * (r + 0.35), c + RIGHT * (r + 0.35), color=DIM, stroke_width=2)
        yaxis = Line(c + DOWN * (r + 0.35), c + UP * (r + 0.35), color=DIM, stroke_width=2)
        self.play(Create(wheel), Create(xaxis), Create(yaxis), run_time=0.9)

        p0 = c + RIGHT * r
        p1 = polar(c, r, 120)
        rad0 = Line(c, p0, color=CHALK, stroke_width=2.4)
        rad1 = Line(c, p1, color=GOLD, stroke_width=2.8)
        self.play(Create(rad0), run_time=0.5)
        self.play(Create(rad1), run_time=0.6)

        arc = Arc(radius=0.8, start_angle=0, angle=np.deg2rad(120),
                  arc_center=c, color=GOLD, stroke_width=2.6)
        al = txt("α", size=25, color=GOLD).move_to(polar(c, 1.06, 58))
        self.play(Create(arc), FadeIn(al), run_time=0.6)

        note = txt("360° = 2π 弧度", size=28, color=GREEN).move_to([-4.3, -1.72, 0])
        note2 = txt("π 弧度 = 180°", size=24, color=DIM).move_to([-4.3, -2.2, 0])
        self.play(Write(note), FadeIn(note2), run_time=0.6)

        r1 = rtxt("逆时针为正，顺时针为负", 1.45, 27)
        r2 = rtxt("转一整圈是 360°，也是 2π", 0.5, 27, GOLD)
        r3 = rtxt("π 弧度 = 180°", -0.55, 30, GREEN)
        r4 = rtxt("1 弧度大约是 57.3°", -1.6, 26, DIM)
        for m in (r1, r2, r3, r4):
            self.play(Write(m), run_time=0.5)
        self.finish_section()

        # ---------- 2. 用单位圆定义 ----------
        self.section(2, "用单位圆定义")
        self.play(FadeOut(wheel), FadeOut(xaxis), FadeOut(yaxis), FadeOut(rad0),
                  FadeOut(rad1), FadeOut(arc), FadeOut(al), FadeOut(note), FadeOut(note2),
                  FadeOut(r1), FadeOut(r2), FadeOut(r3), FadeOut(r4), run_time=0.5)

        c = np.array([-4.35, 0.5, 0])
        r = 1.72
        wheel = Circle(radius=r, color=BLUE, stroke_width=2.6).move_to(c)
        xaxis = Line(c + LEFT * (r + 0.35), c + RIGHT * (r + 0.35), color=DIM, stroke_width=2)
        yaxis = Line(c + DOWN * (r + 0.35), c + UP * (r + 0.35), color=DIM, stroke_width=2)
        self.play(Create(wheel), Create(xaxis), Create(yaxis), run_time=0.9)

        p = polar(c, r, 55)
        rad = Line(c, p, color=GOLD, stroke_width=2.6)
        dotp = Dot(p, radius=0.11, color=RED)
        self.play(Create(rad), FadeIn(dotp), run_time=0.7)

        hx = DashedLine(p, [p[0], c[1], 0], color=GREEN, stroke_width=2)
        hy = DashedLine(p, [c[0], p[1], 0], color=BLUE, stroke_width=2)
        self.play(Create(hx), Create(hy), run_time=0.6)

        lx = txt("x", size=25, color=BLUE).move_to([(p[0] + c[0]) / 2, c[1] - 0.3, 0])
        ly = txt("y", size=25, color=GREEN).move_to([c[0] - 0.3, (p[1] + c[1]) / 2, 0])
        lp = txt("P(x, y)", size=24, color=RED).move_to(p + RIGHT * 0.6 + UP * 0.16)
        self.play(FadeIn(lx), FadeIn(ly), FadeIn(lp), run_time=0.6)

        r1 = rtxt("终边与单位圆交于 P(x, y)", 1.45, 27)
        r2 = rtxt("正弦 sinα = y（纵坐标）", 0.5, 27, GREEN)
        r3 = rtxt("余弦 cosα = x（横坐标）", -0.55, 27, BLUE)
        r4 = rtxt("正切 tanα = y / x（x ≠ 0）", -1.6, 26, GOLD)
        for m in (r1, r2, r3, r4):
            self.play(Write(m), run_time=0.5)
        self.finish_section()

        # ---------- 3. 同角关系 ----------
        self.section(3, "同角关系")
        self.play(FadeOut(wheel), FadeOut(xaxis), FadeOut(yaxis), FadeOut(rad),
                  FadeOut(dotp), FadeOut(hx), FadeOut(hy), FadeOut(lx), FadeOut(ly),
                  FadeOut(lp),
                  FadeOut(r1), FadeOut(r2), FadeOut(r3), FadeOut(r4), run_time=0.5)

        c = np.array([-4.35, 0.75, 0])
        r = 1.62
        wheel = Circle(radius=r, color=DIM, stroke_width=2.2).move_to(c)
        self.play(Create(wheel), run_time=0.7)

        p = polar(c, r, 50)
        foot = np.array([p[0], c[1], 0])
        op = Line(c, p, color=GOLD, stroke_width=3)
        ox = Line(c, foot, color=BLUE, stroke_width=3)
        xp = Line(foot, p, color=GREEN, stroke_width=3)
        self.play(Create(op), run_time=0.5)
        self.play(Create(ox), run_time=0.5)
        self.play(Create(xp), run_time=0.5)

        l1 = txt("1", size=24, color=GOLD).move_to((c + p) / 2 + LEFT * 0.32 + UP * 0.2)
        lx = txt("x", size=24, color=BLUE).move_to([(c[0] + foot[0]) / 2, c[1] - 0.28, 0])
        ly = txt("y", size=24, color=GREEN).move_to([foot[0] + 0.28, (foot[1] + p[1]) / 2, 0])
        self.play(FadeIn(l1), FadeIn(lx), FadeIn(ly), run_time=0.5)

        f1 = txt("sin²α + cos²α = 1", size=30, color=GOLD).move_to([-4.35, -1.25, 0])
        f2 = txt("tanα = sinα / cosα", size=26, color=CHALK).move_to([-4.35, -1.95, 0])
        self.play(Write(f1), run_time=0.6)
        self.play(Write(f2), run_time=0.6)

        r1 = rtxt("x² + y² = 1，这是单位圆", 1.45, 28)
        r2 = rtxt("sin²α + cos²α = 1", 0.5, 30, GOLD)
        r3 = rtxt("tanα = sinα / cosα", -0.55, 28, GREEN)
        r4 = rtxt("知一求二，先定象限符号", -1.6, 26, DIM)
        for m in (r1, r2, r3, r4):
            self.play(Write(m), run_time=0.5)
        self.finish_section()

        # ---------- 4. 诱导公式一 ----------
        self.section(4, "诱导公式一")
        self.play(FadeOut(wheel), FadeOut(op), FadeOut(ox), FadeOut(xp), FadeOut(l1),
                  FadeOut(lx), FadeOut(ly), FadeOut(f1), FadeOut(f2),
                  FadeOut(r1), FadeOut(r2), FadeOut(r3), FadeOut(r4), run_time=0.5)

        c = np.array([-4.3, 0.55, 0])
        r = 1.55
        wheel = Circle(radius=r, color=BLUE, stroke_width=2.6).move_to(c)
        turn = DashedVMobject(Circle(radius=r + 0.32, color=DIM, stroke_width=2).move_to(c))
        xaxis = Line(c + LEFT * (r + 0.5), c + RIGHT * (r + 0.5), color=DIM, stroke_width=2)
        self.play(Create(wheel), Create(turn), Create(xaxis), run_time=0.9)

        p = polar(c, r, 30)
        rad = Line(c, p, color=GOLD, stroke_width=3)
        dotp = Dot(p, radius=0.11, color=RED)
        self.play(Create(rad), FadeIn(dotp), run_time=0.7)

        arc = Arc(radius=0.7, start_angle=0, angle=np.deg2rad(30),
                  arc_center=c, color=GOLD, stroke_width=2.4)
        a30 = txt("30°", size=23, color=GOLD).move_to(polar(c, 1.16, 3))
        a390 = txt("390°", size=23, color=RED).move_to(polar(c, 1.18, 62))
        self.play(Create(arc), FadeIn(a30), FadeIn(a390), run_time=0.6)

        same = txt("终边重合，函数值相同", size=25, color=GREEN).move_to([-4.3, -1.72, 0])
        self.play(Write(same), run_time=0.6)

        r1 = rtxt("α + 2kπ 与 α 终边相同", 1.45, 27, GOLD)
        r2 = rtxt("三角函数值完全不变", 0.5, 29, GREEN)
        r3 = rtxt("sin390° = sin30° = 1/2", -0.55, 27)
        r4 = rtxt("大角先减去整数圈", -1.6, 26, DIM)
        for m in (r1, r2, r3, r4):
            self.play(Write(m), run_time=0.5)
        self.finish_section()

        # ---------- 5. 诱导公式二三四 ----------
        self.section(5, "诱导公式二三四")
        self.play(FadeOut(wheel), FadeOut(turn), FadeOut(xaxis), FadeOut(rad),
                  FadeOut(dotp), FadeOut(arc), FadeOut(a30), FadeOut(a390), FadeOut(same),
                  FadeOut(r1), FadeOut(r2), FadeOut(r3), FadeOut(r4), run_time=0.5)

        items = [
            ("sin(−α) = −sinα", 1.6, GREEN),
            ("cos(−α) = cosα", 0.85, BLUE),
            ("sin(π − α) = sinα", 0.1, GREEN),
            ("cos(π − α) = −cosα", -0.65, BLUE),
            ("sin(π + α) = −sinα", -1.4, GREEN),
            ("cos(π + α) = −cosα", -2.05, BLUE),
        ]
        formulas = VGroup()
        for s, y, col in items:
            m = txt(s, size=25, color=col)
            if m.width > 4.8:
                m.scale_to_fit_width(4.8)
            m.move_to([-4.0, y, 0])
            formulas.add(m)
            self.play(Write(m), run_time=0.45)

        r1 = rtxt("负角化正：正弦变号，余弦不变", 1.45, 26)
        r2 = rtxt("π − α：余弦变号，正弦不变", 0.5, 26, BLUE)
        r3 = rtxt("π + α：正弦、余弦都变号", -0.55, 26, GREEN)
        r4 = rtxt("口诀：奇变偶不变，符号看象限", -1.6, 26, GOLD)
        for m in (r1, r2, r3, r4):
            self.play(Write(m), run_time=0.5)
        self.finish_section()

        # ---------- 6. 象限符号 ----------
        self.section(6, "一全正，二正弦")
        self.play(FadeOut(formulas),
                  FadeOut(r1), FadeOut(r2), FadeOut(r3), FadeOut(r4), run_time=0.5)

        k1 = txt("一全正，二正弦", size=54, color=GOLD).move_to([0, 1.25, 0])
        self.play(Write(k1), run_time=0.9)

        cards = VGroup(
            label_box("一　全正", size=25, color=GREEN),
            label_box("二　正弦", size=25, color=BLUE),
            label_box("三　正切", size=25, color=ORANGE),
            label_box("四　余弦", size=25, color=GOLD),
        )
        for card, x in zip(cards, (-4.55, -1.55, 1.45, 4.45)):
            card.move_to([x, 0.0, 0])
        self.play(FadeIn(cards), run_time=0.8)

        k3 = txt("把角化到第一象限，再看原象限的符号", size=28, color=CHALK)
        k3.move_to([0, -1.5, 0])
        self.play(Write(k3), run_time=0.7)
        self.finish_section()

        self.play(FadeOut(k1), FadeOut(cards), FadeOut(k3), run_time=0.6)