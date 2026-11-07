# -*- coding: utf-8 -*-
"""圆的基本性质：弦、弧、垂径定理、圆周角。九年级上。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


def P(x, y):
    return np.array([float(x), float(y), 0.0])


def pt(cx: float, cy: float, r: float, deg: float):
    """圆上一点：角度用度，逆时针为正。"""
    a = deg * np.pi / 180.0
    return P(cx + r * np.cos(a), cy + r * np.sin(a))


def circ(cx: float, cy: float, r: float, color=CHALK, width: float = 2.8) -> Circle:
    return Circle(radius=r, color=color, stroke_width=width).move_to([cx, cy, 0])


def arc(cx: float, cy: float, r: float, a0: float, a1: float,
        color=GOLD, width: float = 5.0) -> Arc:
    """给一段圆弧加粗上色（a0、a1 为角度）。"""
    return Arc(radius=r, start_angle=a0 * DEGREES, angle=(a1 - a0) * DEGREES,
               arc_center=P(cx, cy), color=color, stroke_width=width)


def chord(cx: float, cy: float, r: float, a0: float, a1: float,
          color=BLUE, width: float = 3.2) -> Line:
    return Line(pt(cx, cy, r, a0), pt(cx, cy, r, a1), color=color, stroke_width=width)


def radius(cx: float, cy: float, r: float, deg: float,
           color=GREEN, width: float = 2.6) -> Line:
    return Line(P(cx, cy), pt(cx, cy, r, deg), color=color, stroke_width=width)


def right_mark(vertex, d1, d2, size: float = 0.22, color=CHALK) -> Mobject:
    """在 vertex 处，沿 d1、d2 两个单位方向画直角符号。"""
    return Polygon(vertex + d1 * size, vertex + d1 * size + d2 * size,
                   vertex + d2 * size, color=color, stroke_width=2.0)


def angle_arc(vertex, p1, p2, radius: float = 0.45,
              color=GOLD, width: float = 2.8) -> Arc:
    """以 vertex 为顶点，画从 p1 方向到 p2 方向的小弧。"""
    v1 = p1 - vertex
    v2 = p2 - vertex
    a1 = float(np.arctan2(v1[1], v1[0]))
    a2 = float(np.arctan2(v2[1], v2[0]))
    sweep = (a2 - a1) % (2 * np.pi)
    if sweep > np.pi:
        a1, sweep = a2, 2 * np.pi - sweep
    return Arc(radius=radius, start_angle=a1, angle=sweep,
               arc_center=vertex, color=color, stroke_width=width)


class YuanJibenXingzhiScene(NarratedScene):
    lesson = "yuan-jiben-xingzhi"

    def clear_stage(self, run_time: float = 0.5):
        keep = {id(self._track), id(self._fill)}
        junk = [m for m in self.mobjects if id(m) not in keep]
        if junk:
            self.play(*[FadeOut(m) for m in junk], run_time=run_time)
        self.cur_title = None
        self.cur_sub = None

    # ---------------- 0. 圆里的名字 ---------------- 34.3
    def scene_intro(self):
        self.section(0, "圆里的这些名字")

        cx, cy, r = -3.5, 0.15, 1.75
        c = circ(cx, cy, r)
        self.play(Create(c), run_time=1.5)

        dot = Dot(P(cx, cy), radius=0.07, color=GOLD)
        o = txt("O", size=24, color=GOLD).move_to([cx + 0.22, cy + 0.2, 0])
        self.play(FadeIn(dot), FadeIn(o), run_time=0.6)
        self.wait(0.5)

        # 半径
        rd = radius(cx, cy, r, 52)
        rl = txt("半径 r", size=22, color=GREEN).move_to([cx + 0.75, cy + 1.05, 0])
        self.play(Create(rd), run_time=0.9)
        self.play(FadeIn(rl, shift=UP * 0.04), run_time=0.7)
        self.wait(0.7)

        # 弦
        ch = chord(cx, cy, r, 196, 344, BLUE)
        ca = txt("A", size=22, color=BLUE).move_to(pt(cx, cy, r, 196) + LEFT * 0.28 + DOWN * 0.04)
        cb = txt("B", size=22, color=BLUE).move_to(pt(cx, cy, r, 344) + RIGHT * 0.28 + DOWN * 0.04)
        cl = txt("弦 AB", size=22, color=BLUE).move_to([cx, cy - 0.78, 0])
        self.play(Create(ch), FadeIn(ca), FadeIn(cb), run_time=1.2)
        self.play(FadeIn(cl, shift=UP * 0.04), run_time=0.7)
        self.wait(0.7)

        # 直径
        dm = Line(pt(cx, cy, r, 0), pt(cx, cy, r, 180), color=GOLD, stroke_width=3.4)
        dl = txt("直径（最长的弦）", size=21, color=GOLD).move_to([cx, cy + 2.05, 0])
        self.play(Create(dm), run_time=1.0)
        self.play(FadeIn(dl, shift=UP * 0.04), run_time=0.7)
        self.wait(0.8)

        # 弧
        ar = arc(cx, cy, r, 52, 196, GOLD, 5.2)
        al = txt("弧", size=22, color=GOLD).move_to([cx - 1.75, cy + 0.85, 0])
        self.play(Create(ar), FadeIn(al), run_time=1.1)
        self.wait(1.0)

        rows = [
            ("圆心 O，半径 r", GOLD),
            ("弦 AB：连接圆上两点", BLUE),
            ("直径：过圆心，是 r 的 2 倍", GOLD),
            ("弧：大于半圆叫优弧，小于半圆叫劣弧", GREEN),
        ]
        y = 2.15
        for s, col in rows:
            t = txt(s, size=22, color=col).move_to([3.35, y, 0])
            self.play(FadeIn(t, shift=RIGHT * 0.04), run_time=0.8)
            y -= 0.85
        self.wait(1.2)

        box = label_box("圆的定义：到圆心距离等于半径的所有点", size=22, color=GOLD)
        box.move_to([0, -2.75, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.05)
        self.wait(14.0)
        self.finish_section()

    # ---------------- 1. 对称性与垂径定理 ---------------- 25.9
    def scene_theorem(self):
        self.section(1, "垂径定理")

        cx, cy, r = -2.4, 0.15, 2.0
        c = circ(cx, cy, r)
        self.play(Create(c), run_time=1.3)

        ch = chord(cx, cy, r, 200, 340, BLUE)
        self.play(Create(ch), run_time=1.0)

        dm = Line(pt(cx, cy, r, 90), pt(cx, cy, r, 270), color=GOLD, stroke_width=3.4)
        self.play(Create(dm), run_time=1.0)
        self.wait(0.6)

        # 交点与直角符号
        foot_y = cy + r * np.sin(200 * np.pi / 180)
        foot = P(cx, foot_y)
        rm = right_mark(foot, RIGHT, UP, 0.2, GOLD)
        self.play(Create(rm), run_time=0.8)

        m1 = (foot + pt(cx, cy, r, 200)) / 2
        m2 = (foot + pt(cx, cy, r, 340)) / 2
        t1 = Line(m1 + UP * 0.14, m1 + DOWN * 0.14, color=GOLD, stroke_width=2.6)
        t2 = Line(m2 + UP * 0.14, m2 + DOWN * 0.14, color=GOLD, stroke_width=2.6)
        self.play(Create(t1), Create(t2), run_time=1.0)

        eq = txt("两段相等", size=21, color=GOLD).move_to([cx + 1.15, foot_y - 0.55, 0])
        self.play(FadeIn(eq, shift=UP * 0.04), run_time=0.7)
        self.wait(1.0)

        # 两段弧
        a1 = arc(cx, cy, r, 200, 270, GREEN, 5.0)
        a2 = arc(cx, cy, r, 270, 340, GREEN, 5.0)
        self.play(Create(a1), Create(a2), run_time=1.2)
        self.wait(0.8)

        lines = [
            ("垂直于弦的直径", GOLD),
            ("平分这条弦", BLUE),
            ("并且平分弦所对的两条弧", GREEN),
        ]
        y = 1.55
        for s, col in lines:
            t = txt(s, size=24, color=col).move_to([3.45, y, 0])
            self.play(FadeIn(t, shift=RIGHT * 0.04), run_time=0.85)
            y -= 0.85
        self.wait(1.0)

        note = txt("「直径」与「垂直」两个条件，缺一不可", size=23, color=RED)
        note.move_to([0, -2.55, 0])
        self.play(FadeIn(note, shift=UP * 0.04), run_time=0.95)
        self.wait(8.0)
        self.finish_section()

    # ---------------- 2. 垂径定理的计算 ---------------- 29.3
    def scene_calc(self):
        self.section(2, "见弦作垂径，勾股来算")

        cx, cy, r = -3.1, 0.35, 1.9
        c = circ(cx, cy, r, CHALK, 2.6)
        self.play(Create(c), run_time=1.2)

        ch = chord(cx, cy, r, 210, 330, BLUE)
        self.play(Create(ch), run_time=0.9)

        foot_y = cy + r * np.sin(210 * np.pi / 180)
        foot = P(cx, foot_y)
        dm = Line(P(cx, cy), foot, color=GOLD, stroke_width=3.0)
        rd = Line(P(cx, cy), pt(cx, cy, r, 330), color=GREEN, stroke_width=3.0)
        hc = Line(foot, pt(cx, cy, r, 330), color=BLUE, stroke_width=3.0)
        self.play(Create(dm), Create(rd), Create(hc), run_time=1.5)

        rm = right_mark(foot, RIGHT, UP, 0.18, GOLD)
        self.play(Create(rm), run_time=0.7)

        lr = txt("r", size=24, color=GREEN).move_to([cx + 0.62, cy - 0.05, 0])
        ld = txt("d", size=24, color=GOLD).move_to([cx - 0.28, foot_y + 0.32, 0])
        lh = txt("a/2", size=24, color=BLUE).move_to([cx + 0.95, cy - 1.15, 0])
        self.play(FadeIn(lr), FadeIn(ld), FadeIn(lh), run_time=0.9)
        self.wait(1.0)

        f1 = txt("r² = (a/2)² + d²", size=34, color=GOLD).move_to([3.0, 1.75, 0])
        self.play(FadeIn(f1, scale=0.98), run_time=1.0)
        self.wait(0.7)

        rows = [
            ("例：弦长 a = 8，半径 r = 5", CHALK),
            ("则 a/2 = 4", CHALK),
            ("d² = 5² − 4² = 9", CHALK),
            ("d = 3（弦心距）", GREEN),
        ]
        y = 0.55
        for s, col in rows:
            t = txt(s, size=27, color=col).move_to([3.0, y, 0])
            self.play(FadeIn(t, shift=UP * 0.04), run_time=0.8)
            y -= 0.78
        self.wait(1.0)

        note = txt("半径、半弦、弦心距，正好凑成直角三角形", size=23, color=RED)
        note.move_to([0, -2.55, 0])
        self.play(FadeIn(note, shift=UP * 0.04), run_time=0.95)
        self.wait(11.5)
        self.finish_section()

    # ---------------- 3. 圆心角、弧、弦 ---------------- 22.9
    def scene_central(self):
        self.section(3, "圆心角、弧、弦")

        c = circ(0, 0.05, 1.85)
        self.play(Create(c), run_time=1.2)

        # 左：∠AOB
        oa = Line(P(0, 0.05), pt(0, 0.05, 1.85, 120), color=GOLD, stroke_width=2.8)
        ob = Line(P(0, 0.05), pt(0, 0.05, 1.85, 55), color=GOLD, stroke_width=2.8)
        ab = chord(0, 0.05, 1.85, 55, 120, BLUE)
        self.play(Create(oa), Create(ob), run_time=1.0)
        self.play(Create(ab), run_time=0.8)

        a1 = Arc(radius=0.55, start_angle=55 * DEGREES, angle=65 * DEGREES,
                 arc_center=P(0, 0.05), color=GOLD, stroke_width=3.0)
        self.play(Create(a1), run_time=0.8)

        p1 = txt("∠AOB", size=23, color=GOLD).move_to([0.06, 0.98, 0])
        self.play(FadeIn(p1), run_time=0.7)
        self.wait(0.8)

        l1 = txt("相等的圆心角", size=23, color=GOLD).move_to([0, -2.15, 0])
        l2 = txt("所对的弧相等，所对的弦也相等", size=23, color=BLUE)
        l2.move_to([0, -2.68, 0])
        self.play(FadeIn(l1, shift=UP * 0.04), run_time=0.85)
        self.play(FadeIn(l2, shift=UP * 0.04), run_time=0.85)
        self.wait(0.9)

        box = label_box("同圆或等圆中，圆心角、弧、弦一一对应", size=21, color=GREEN)
        box.move_to([0, 2.65, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.0)
        self.wait(11.0)
        self.finish_section()

    # ---------------- 4. 圆周角定理 ---------------- 28.1
    def scene_inscribed(self):
        self.section(4, "圆周角等于圆心角的一半")

        cx, cy, r = -3.3, 0.2, 1.85
        c = circ(cx, cy, r)
        self.play(Create(c), run_time=1.2)

        pa, pb, pc = pt(cx, cy, r, 205), pt(cx, cy, r, 335), pt(cx, cy, r, 88)
        oa = Line(P(cx, cy), pa, color=GOLD, stroke_width=2.6)
        ob = Line(P(cx, cy), pb, color=GOLD, stroke_width=2.6)
        ca = Line(pc, pa, color=BLUE, stroke_width=2.8)
        cb = Line(pc, pb, color=BLUE, stroke_width=2.8)
        self.play(Create(oa), Create(ob), run_time=1.1)
        self.play(Create(ca), Create(cb), run_time=1.2)

        oang = Arc(radius=0.5, start_angle=205 * DEGREES,
                   angle=(335 - 205) * DEGREES, arc_center=P(cx, cy),
                   color=GOLD, stroke_width=3.0)
        self.play(Create(oang), run_time=0.9)

        pang = angle_arc(pc, pa, pb, radius=0.5, color=BLUE, width=2.8)
        self.play(Create(pang), run_time=0.8)

        lc = txt("C", size=22, color=BLUE).move_to(pc + UP * 0.32)
        la = txt("A", size=22, color=BLUE).move_to(pa + LEFT * 0.3 + DOWN * 0.08)
        lb = txt("B", size=22, color=BLUE).move_to(pb + RIGHT * 0.3 + DOWN * 0.08)
        self.play(FadeIn(lc), FadeIn(la), FadeIn(lb), run_time=0.6)
        self.wait(0.8)

        f = txt("∠ACB = ½ ∠AOB", size=32, color=GOLD).move_to([3.1, 1.85, 0])
        self.play(FadeIn(f, scale=0.98), run_time=1.0)
        self.wait(0.7)

        rows = [
            ("推论①：直径所对的圆周角是直角", GREEN),
            ("推论②：同一条弧所对的圆周角相等", GREEN),
        ]
        y = 0.65
        for s, col in rows:
            t = txt(s, size=24, color=col).move_to([3.05, y, 0])
            self.play(FadeIn(t, shift=RIGHT * 0.04), run_time=0.9)
            y -= 0.95
        self.wait(1.0)

        note = txt("先认清是哪一条弧，再分圆心角和圆周角", size=23, color=RED)
        note.move_to([3.05, -1.3, 0])
        self.play(FadeIn(note, shift=UP * 0.04), run_time=0.95)
        self.wait(11.5)
        self.finish_section()

    # ---------------- 5. 圆内接四边形 ---------------- 22.0
    def scene_quad(self):
        self.section(5, "圆内接四边形：对角互补")

        cx, cy, r = -1.8, 0.2, 2.0
        c = circ(cx, cy, r)
        self.play(Create(c), run_time=1.2)

        angs = [65, 150, 235, 320]
        names = ["A", "B", "C", "D"]
        pts = [pt(cx, cy, r, a) for a in angs]
        poly = Polygon(*pts, color=BLUE, stroke_width=3.0,
                       fill_color=BLUE, fill_opacity=0.05)
        self.play(Create(poly), run_time=1.4)

        for p, n in zip(pts, names):
            d = (p - P(cx, cy))
            d = d / np.linalg.norm(d) * 0.34
            t = txt(n, size=23, color=BLUE).move_to(p + d)
            self.play(FadeIn(t), run_time=0.35)
        self.wait(0.9)

        l1 = txt("∠A + ∠C = 180°", size=30, color=GOLD).move_to([3.4, 1.15, 0])
        l2 = txt("∠B + ∠D = 180°", size=30, color=GOLD).move_to([3.4, 0.35, 0])
        self.play(FadeIn(l1, scale=0.97), run_time=0.9)
        self.play(FadeIn(l2, scale=0.97), run_time=0.9)
        self.wait(1.0)

        why = txt("每组对角所对的弧，合起来是整个圆", size=22, color=CHALK)
        why.move_to([3.4, -0.95, 0])
        self.play(FadeIn(why, shift=UP * 0.04), run_time=0.95)
        self.wait(0.8)

        note = txt("是对角互补，不是对边互补", size=23, color=RED)
        note.move_to([3.4, -1.95, 0])
        self.play(FadeIn(note, shift=UP * 0.04), run_time=0.95)
        self.wait(10.0)
        self.finish_section()

    # ---------------- 6. 四个易错点 ---------------- 26.0
    def scene_traps(self):
        self.section(6, "四个易错点")

        rows = [
            ("① 弦和直径别混", "直径是最长的弦"),
            ("② 垂径定理要「直径垂直弦」", "两个条件缺一不可"),
            ("③ 圆周角与圆心角对同一条弧", "先找弧，再看角"),
            ("④ 圆内接四边形对角互补", "不是对边互补"),
        ]
        y = 1.85
        for a, b in rows:
            ta = txt(a, size=23, color=RED).move_to([-2.65, y, 0])
            tb = txt(b, size=21, color=DIM).move_to([3.7, y, 0])
            self.play(FadeIn(ta, shift=RIGHT * 0.04), run_time=0.65)
            self.play(FadeIn(tb, shift=RIGHT * 0.04), run_time=0.65)
            y -= 0.86
        self.wait(1.0)

        box = label_box("见弦作垂径，见直径想直角", size=26, color=GOLD)
        box.move_to([0, -2.45, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.1)
        self.wait(9.5)
        self.finish_section()

    def construct(self):
        self.scene_intro()
        self.clear_stage()
        self.scene_theorem()
        self.clear_stage()
        self.scene_calc()
        self.clear_stage()
        self.scene_central()
        self.clear_stage()
        self.scene_inscribed()
        self.clear_stage()
        self.scene_quad()
        self.clear_stage()
        self.scene_traps()
        self.clear_stage(0.8)