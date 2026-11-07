# -*- coding: utf-8 -*-
"""尺规作图：五种基本作图与组合应用。九年级下。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


def P(x, y):
    return np.array([float(x), float(y), 0.0])


def right_mark(vertex, d1, d2, size: float = 0.18, color=DIM) -> Mobject:
    return Polygon(vertex + d1 * size, vertex + d1 * size + d2 * size,
                   vertex + d2 * size, color=color, stroke_width=2.0)


def arc_at(center, r, a1, a2, color=CHALK, width=2.2):
    return Arc(radius=r, start_angle=a1 * DEGREES, angle=(a2 - a1) * DEGREES,
               arc_center=center, color=color, stroke_width=width)


class ChiguiZuotuScene(NarratedScene):
    lesson = "chigui-zuotu"

    def clear_stage(self, run_time: float = 0.5):
        keep = {id(self._track), id(self._fill)}
        junk = [m for m in self.mobjects if id(m) not in keep]
        if junk:
            self.play(*[FadeOut(m) for m in junk], run_time=run_time)
        self.cur_title = None
        self.cur_sub = None

    # ---------------- 0. 三个场景 ---------------- 21.5
    def scene_intro(self):
        self.section(0, "两样工具，画出准确图形")

        cards = [(-4.5, "木匠画直角", GOLD), (0.0, "墙上找水平", GREEN), (4.5, "剪纸对折", BLUE)]
        for cx, name, col in cards:
            self.play(FadeIn(txt(name, size=24, color=col).move_to([cx, 2.3, 0])), run_time=0.6)

        # 直角
        cx = -4.5
        self.play(Create(Line(P(cx - 1.0, -0.6), P(cx + 1.2, -0.6), color=CHALK, stroke_width=2.6)),
                  Create(Line(P(cx - 1.0, -0.6), P(cx - 1.0, 1.1), color=CHALK, stroke_width=2.6)),
                  run_time=0.8)
        self.play(Create(right_mark(P(cx - 1.0, -0.6), RIGHT, UP, 0.2, DIM)), run_time=0.5)

        # 水平
        cx = 0.0
        self.play(Create(Line(P(cx - 1.35, -0.15), P(cx + 1.35, -0.15), color=CHALK,
                              stroke_width=2.6)), run_time=0.8)
        self.play(Create(Circle(radius=0.28, color=GREEN, stroke_width=2.2).move_to([cx, 0.42, 0])),
                  run_time=0.6)

        # 折纸
        cx = 4.5
        paper = Polygon(P(cx - 1.2, -0.75), P(cx + 1.2, -0.75), P(cx + 1.2, 0.85),
                        color=CHALK, stroke_width=2.4)
        self.play(Create(paper), run_time=0.8)
        self.play(Create(Line(P(cx - 1.2, -0.75), P(cx + 1.2, 0.85), color=BLUE,
                              stroke_width=2.0)), run_time=0.6)
        self.play(Create(DashedLine(P(cx - 1.0, 0.05), P(cx + 1.0, 0.05), color=DIM,
                                    stroke_width=1.8, dash_length=0.1)), run_time=0.5)
        self.wait(0.6)

        d = txt("直尺没有刻度，圆规只能画弧", size=26, color=CHALK).move_to([0, -1.6, 0])
        self.play(FadeIn(d, shift=UP * 0.04), run_time=0.95)
        box = label_box("只靠这两样，把图形准确画出来", size=23, color=GOLD)
        box.move_to([0, -2.45, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.0)
        self.wait(7.5)
        self.finish_section()

    # ---------------- 1. 工具与规矩 ---------------- 21.8
    def scene_tools(self):
        self.section(1, "能用什么，不能用什么")

        # 直尺
        ruler = Rectangle(width=3.4, height=0.52, color=CHALK, stroke_width=2.4)
        ruler.move_to([-3.6, 1.15, 0])
        self.play(Create(ruler), run_time=0.8)
        ticks = VGroup()
        for i in range(1, 9):
            x = -5.3 + i * 0.36
            h = 0.16 if i % 2 == 0 else 0.1
            ticks.add(Line(P(x, 0.89), P(x, 0.89 + h), color=CHALK, stroke_width=1.6))
        self.play(Create(ticks), run_time=0.7)
        self.play(FadeIn(txt("直尺：只能连线，不能量长度", size=21, color=GOLD)
                         .move_to([-3.6, 0.35, 0])), run_time=0.7)

        # 圆规
        cx = -3.6
        top = P(cx, -0.15)
        foot_l = P(cx - 0.5, -1.5)
        foot_r = P(cx + 0.5, -1.5)
        self.play(Create(Line(top, foot_l, color=CHALK, stroke_width=2.6)),
                  Create(Line(top, foot_r, color=CHALK, stroke_width=2.6)),
                  run_time=0.8)
        self.play(FadeIn(Dot(top, radius=0.09, color=GOLD)), run_time=0.4)
        self.play(Create(arc_at(foot_l, 1.0, 205, 335, GREEN, 2.2)), run_time=0.7)
        self.play(FadeIn(txt("圆规：只能画弧、截取", size=21, color=GREEN)
                         .move_to([-3.6, -2.9, 0])), run_time=0.7)
        self.wait(0.6)

        rows = [
            ("每一步都要留下作图痕迹", GOLD),
            ("弧线不能擦，痕迹就是证明", CHALK),
            ("最后写结论：某线即所求", GREEN),
        ]
        y = 1.7
        for s, col in rows:
            t = txt(s, size=24, color=col).move_to([2.9, y, 0])
            self.play(FadeIn(t, shift=RIGHT * 0.04), run_time=0.85)
            y -= 0.95
        self.wait(0.6)

        box = label_box("尺规作图，图就是理由", size=23, color=RED).move_to([2.9, -1.75, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.0)
        self.wait(6.0)
        self.finish_section()

    # ---------------- 2. 作线段、作角 ---------------- 28.5
    def scene_two_basic(self):
        self.section(2, "作线段，作相等的角")

        h1 = txt("作一条线段等于已知线段", size=23, color=GOLD).move_to([-3.4, 2.45, 0])
        self.play(FadeIn(h1, shift=UP * 0.04), run_time=0.8)

        A = P(-5.5, 1.35)
        B = P(-3.9, 1.35)
        self.play(Create(Line(A, B, color=GOLD, stroke_width=3.0)), run_time=0.7)
        self.play(FadeIn(txt("A", size=19, color=DIM).move_to(A + DOWN * 0.3)),
                  FadeIn(txt("B", size=19, color=DIM).move_to(B + DOWN * 0.3)), run_time=0.5)

        O = P(-5.6, -0.35)
        ray = Line(O, P(-1.5, -0.35), color=CHALK, stroke_width=2.2)
        self.play(Create(ray), run_time=0.7)
        r = (B - A)[0]
        self.play(Create(Arc(radius=r, start_angle=-8 * DEGREES, angle=16 * DEGREES,
                             arc_center=O, color=GREEN, stroke_width=2.4)), run_time=0.7)
        C = P(O[0] + r, O[1])
        self.play(FadeIn(Dot(C, radius=0.06, color=GREEN)), run_time=0.4)
        self.play(FadeIn(txt("C", size=19, color=GREEN).move_to(C + DOWN * 0.52)), run_time=0.4)
        self.wait(0.6)

        h2 = txt("作一个角等于已知角", size=23, color=BLUE).move_to([3.6, 2.45, 0])
        self.play(FadeIn(h2, shift=UP * 0.04), run_time=0.8)

        V = P(1.4, 0.55)
        self.play(Create(Line(V, P(3.6, 0.55), color=CHALK, stroke_width=2.2)),
                  Create(Line(V, P(V[0] + 2.0 * np.cos(42 * DEGREES),
                                   V[1] + 2.0 * np.sin(42 * DEGREES)), color=CHALK, stroke_width=2.2)),
                  run_time=0.8)
        self.play(Create(arc_at(V, 1.15, 0, 42, BLUE, 2.2)), run_time=0.7)

        V2 = P(3.05, -1.15)
        self.play(Create(Line(V2, P(5.8, -1.15), color=CHALK, stroke_width=2.2)), run_time=0.6)
        self.play(Create(arc_at(V2, 1.15, 0, 42, BLUE, 2.2)), run_time=0.7)
        p1 = P(V2[0] + 1.15, V2[1])
        p2 = P(V2[0] + 1.15 * np.cos(42 * DEGREES), V2[1] + 1.15 * np.sin(42 * DEGREES))
        self.play(Create(DashedLine(p1, p2, color=GOLD, stroke_width=1.8, dash_length=0.08)),
                  run_time=0.6)
        self.play(Create(Line(V2, P(V2[0] + 2.0 * np.cos(42 * DEGREES),
                                    V2[1] + 2.0 * np.sin(42 * DEGREES)), color=BLUE,
                              stroke_width=2.4)), run_time=0.8)
        self.wait(0.6)

        tip = txt("量出两交点之间的距离，就能把角搬过去", size=22, color=GOLD)
        tip.move_to([3.6, -2.35, 0])
        self.play(FadeIn(tip, shift=UP * 0.04), run_time=0.9)
        self.wait(8.0)
        self.finish_section()

    # ---------------- 3. 角平分线 ---------------- 25.8
    def scene_bisector(self):
        self.section(3, "作角的平分线")

        V = P(-5.5, -1.75)
        ang = 50.0
        R1 = 1.6
        self.play(Create(Line(V, P(-1.7, -1.75), color=CHALK, stroke_width=2.6)),
                  Create(Line(V, P(V[0] + 3.5 * np.cos(ang * DEGREES),
                                   V[1] + 3.5 * np.sin(ang * DEGREES)), color=CHALK,
                              stroke_width=2.6)), run_time=0.9)
        self.play(Create(arc_at(V, R1, 0, ang, DIM, 2.0)), run_time=0.8)

        p1 = P(V[0] + R1, V[1])
        p2 = P(V[0] + R1 * np.cos(ang * DEGREES), V[1] + R1 * np.sin(ang * DEGREES))
        self.play(FadeIn(Dot(p1, radius=0.06, color=GOLD)),
                  FadeIn(Dot(p2, radius=0.06, color=GOLD)), run_time=0.6)

        r2 = 1.3
        half = R1 * np.sin(ang / 2 * DEGREES)
        proj = R1 * np.cos(ang / 2 * DEGREES)
        t = proj + np.sqrt(max(r2 * r2 - half * half, 0.01))
        R = P(V[0] + t * np.cos(ang / 2 * DEGREES), V[1] + t * np.sin(ang / 2 * DEGREES))

        d1 = np.degrees(np.arctan2(R[1] - p1[1], R[0] - p1[0]))
        d2 = np.degrees(np.arctan2(R[1] - p2[1], R[0] - p2[0]))
        self.play(Create(arc_at(p1, r2, d1 - 24, d1 + 24, GREEN, 2.0)), run_time=0.7)
        self.play(Create(arc_at(p2, r2, d2 - 24, d2 + 24, GREEN, 2.0)), run_time=0.7)
        self.play(FadeIn(Dot(R, radius=0.07, color=GREEN)), run_time=0.5)
        self.play(Create(Line(V, P(V[0] + (t + 1.25) * np.cos(ang / 2 * DEGREES),
                                   V[1] + (t + 1.25) * np.sin(ang / 2 * DEGREES)),
                              color=GOLD, stroke_width=3.0)),
                  run_time=0.9)
        self.play(Create(arc_at(V, 0.8, 0, ang / 2, RED, 2.0)),
                  Create(arc_at(V, 0.8, ang / 2, ang, RED, 2.0)), run_time=0.7)
        self.wait(0.6)

        rows = [
            ("① 顶点为圆心画弧，交两边", CHALK),
            ("② 两交点为圆心，等半径画弧", CHALK),
            ("③ 连顶点和交点，就是角平分线", GOLD),
        ]
        y = 1.85
        for s, col in rows:
            t = txt(s, size=21, color=col).move_to([3.5, y, 0])
            self.play(FadeIn(t, shift=RIGHT * 0.04), run_time=0.8)
            y -= 0.8
        self.wait(0.6)

        box = label_box("三边相等，两三角形全等，所以两角相等", size=20, color=RED)
        box.move_to([3.5, -1.75, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.0)
        self.wait(6.5)
        self.finish_section()

    # ---------------- 4. 垂直平分线 ---------------- 24.5
    def scene_perp_bisector(self):
        self.section(4, "作线段的垂直平分线")

        A = P(-5.7, -0.1)
        B = P(-2.3, -0.1)
        self.play(Create(Line(A, B, color=CHALK, stroke_width=2.8)), run_time=0.8)
        self.play(FadeIn(txt("A", size=19, color=DIM).move_to(A + LEFT * 0.3)),
                  FadeIn(txt("B", size=19, color=DIM).move_to(B + RIGHT * 0.3)), run_time=0.6)

        R = 2.05
        self.play(Create(arc_at(A, R, -55, 55, GREEN, 2.0)), run_time=0.8)
        self.play(Create(arc_at(B, R, 125, 235, GREEN, 2.0)), run_time=0.8)
        top = P(-4.0, -0.1 + np.sqrt(R * R - 1.7 * 1.7))
        bot = P(-4.0, -0.1 - np.sqrt(R * R - 1.7 * 1.7))
        self.play(FadeIn(Dot(top, radius=0.07, color=GOLD)),
                  FadeIn(Dot(bot, radius=0.07, color=GOLD)), run_time=0.6)
        self.play(Create(Line(top, bot, color=GOLD, stroke_width=3.0)), run_time=0.8)
        self.play(Create(right_mark(P(-4.0, -0.1), RIGHT, UP, 0.16, RED)), run_time=0.5)
        self.wait(0.6)

        rows = [
            ("① 两端点为圆心，半径大于一半", CHALK),
            ("② 两弧交于上下两点", CHALK),
            ("③ 连线就是垂直平分线", GOLD),
        ]
        y = 1.85
        for s, col in rows:
            t = txt(s, size=21, color=col).move_to([3.5, y, 0])
            self.play(FadeIn(t, shift=RIGHT * 0.04), run_time=0.8)
            y -= 0.8
        self.wait(0.6)

        note = txt("线上的点到两端距离相等", size=22, color=GREEN).move_to([3.5, -0.9, 0])
        self.play(FadeIn(note, shift=UP * 0.04), run_time=0.85)
        box = label_box("常用来找「到两点一样远」的位置", size=20, color=RED)
        box.move_to([3.5, -1.8, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.0)
        self.wait(7.0)
        self.finish_section()

    # ---------------- 5. 组合 ---------------- 22.5
    def scene_combine(self):
        self.section(5, "组合起来能画什么")

        # 外接圆
        cx, cy, r = -3.9, -0.55, 1.55
        tri = Polygon(P(cx + r * np.cos(100 * DEGREES), cy + r * np.sin(100 * DEGREES)),
                      P(cx + r * np.cos(215 * DEGREES), cy + r * np.sin(215 * DEGREES)),
                      P(cx + r * np.cos(340 * DEGREES), cy + r * np.sin(340 * DEGREES)),
                      color=CHALK, stroke_width=2.4)
        self.play(Create(Circle(radius=r, color=DIM, stroke_width=2.0).move_to([cx, cy, 0])),
                  run_time=0.8)
        self.play(Create(tri), run_time=0.9)
        self.play(FadeIn(Dot([cx, cy, 0], radius=0.07, color=GOLD)), run_time=0.5)
        self.play(FadeIn(txt("外接圆：三边垂直平分线交点", size=19, color=GOLD)
                         .move_to([cx, -2.75, 0])), run_time=0.8)
        self.wait(0.5)

        # 内切圆
        cx2 = 3.4
        tri2 = Polygon(P(cx2 - 1.55, -1.15), P(cx2 + 1.55, -1.15), P(cx2, 1.55),
                       color=CHALK, stroke_width=2.4)
        self.play(Create(tri2), run_time=0.9)
        self.play(Create(Circle(radius=0.9, color=DIM, stroke_width=2.0).move_to([cx2, -0.25, 0])),
                  run_time=0.7)
        self.play(FadeIn(Dot([cx2, -0.25, 0], radius=0.07, color=GREEN)), run_time=0.5)
        self.play(FadeIn(txt("内切圆：三个角平分线交点", size=19, color=GREEN)
                         .move_to([cx2, -2.75, 0])), run_time=0.8)
        self.wait(0.5)

        tip = txt("作完图，还要说明理由", size=25, color=CHALK).move_to([0, 2.85, 0])
        self.play(FadeIn(tip, shift=UP * 0.04), run_time=0.9)
        box = label_box("中考常考：作图 + 说理", size=22, color=RED).move_to([0, 2.0, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.0)
        self.wait(7.5)
        self.finish_section()

    # ---------------- 6. 易错点 ---------------- 25.9
    def scene_traps(self):
        self.section(6, "四个易错点")

        rows = [
            ("① 不留作图痕迹", "弧线就是证明，别擦"),
            ("② 半径取得太小", "两弧交不上，画不出点"),
            ("③ 用刻度尺量长度", "那就不是尺规作图"),
            ("④ 只画图不写结论", "结论要写清对象"),
        ]
        y = 1.85
        for a, b in rows:
            ta = txt(a, size=23, color=RED).move_to([-2.6, y, 0])
            tb = txt(b, size=21, color=DIM).move_to([3.6, y, 0])
            self.play(FadeIn(ta, shift=RIGHT * 0.04), run_time=0.65)
            self.play(FadeIn(tb, shift=RIGHT * 0.04), run_time=0.65)
            y -= 0.86
        self.wait(1.0)

        box = label_box("留痕迹，写结论，说理由", size=26, color=GOLD)
        box.move_to([0, -2.45, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.1)
        self.wait(10.5)
        self.finish_section()

    def construct(self):
        self.scene_intro()
        self.clear_stage()
        self.scene_tools()
        self.clear_stage()
        self.scene_two_basic()
        self.clear_stage()
        self.scene_bisector()
        self.clear_stage()
        self.scene_perp_bisector()
        self.clear_stage()
        self.scene_combine()
        self.clear_stage()
        self.scene_traps()
        self.clear_stage(0.8)