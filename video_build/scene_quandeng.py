# -*- coding: utf-8 -*-
"""全等三角形：定义与对应关系、SSS、SAS（含 SSA 反例）、ASA/AAS、HL、证明书写、例题。八年级。"""

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


def P(x, y):
    return np.array([float(x), float(y), 0.0])


def tri(a, b, c, color=CHALK, fill=0.0, width=3.0):
    t = Polygon(P(*a), P(*b), P(*c), color=color, stroke_width=width)
    if fill:
        t.set_fill(color, opacity=fill)
    return t


def tick_marks(a, b, n=1, color=GOLD, size=0.22, width=2.6):
    """在线段 ab 上画 n 道垂直短线，表示「相等」。"""
    ax, ay = a
    bx, by = b
    dx, dy = bx - ax, by - ay
    L = math.hypot(dx, dy)
    ux, uy = dx / L, dy / L
    nx, ny = -uy, ux
    marks = VGroup()
    if n == 1:
        spots = [0.5]
    elif n == 2:
        spots = [0.42, 0.58]
    else:
        spots = [0.37, 0.5, 0.63]
    for t in spots:
        cx, cy = ax + dx * t, ay + dy * t
        marks.add(Line(
            [cx - nx * size / 2, cy - ny * size / 2, 0],
            [cx + nx * size / 2, cy + ny * size / 2, 0],
            color=color, stroke_width=width,
        ))
    return marks


def ang_arc(v, p1, p2, r=0.62, color=BLUE, width=3.0):
    """在顶点 v 处画 p1、p2 之间的小弧。"""
    a1 = math.atan2(p1[1] - v[1], p1[0] - v[0])
    a2 = math.atan2(p2[1] - v[1], p2[0] - v[0])
    d = (a2 - a1) % (2 * math.pi)
    if d > math.pi:
        a1, a2 = a2, a1
        d = 2 * math.pi - d
    return Arc(radius=r, start_angle=a1, angle=d, arc_center=P(*v),
               color=color, stroke_width=width)


def right_angle(v, p1, p2, size=0.34, color=CHALK):
    """直角小方块。"""
    a1 = math.atan2(p1[1] - v[1], p1[0] - v[0])
    a2 = math.atan2(p2[1] - v[1], p2[0] - v[0])
    u1 = np.array([math.cos(a1), math.sin(a1), 0]) * size
    u2 = np.array([math.cos(a2), math.sin(a2), 0]) * size
    o = P(*v)
    return Polygon(o + u1, o + u1 + u2, o + u2,
                   color=color, stroke_width=2.4, fill_color=color, fill_opacity=0.12)


class QuandengScene(NarratedScene):
    lesson = "quandeng"

    def clear_stage(self, run_time: float = 0.5):
        keep = {id(self._track), id(self._fill)}
        junk = [m for m in self.mobjects if id(m) not in keep]
        if junk:
            self.play(*[FadeOut(m) for m in junk], run_time=run_time)
        self.cur_title = None
        self.cur_sub = None

    # ---------------- 0. 两块玻璃，完全重合 ---------------- 37.1
    def scene_intro(self):
        self.section(0, "完全重合，就叫全等")

        A, B, C = (-5.9, 0.5), (-3.7, 0.5), (-4.85, 2.4)
        D, E, F = (-5.9 + 6.4, 0.5), (-3.7 + 6.4, 0.5), (-4.85 + 6.4, 2.4)

        t1 = tri(A, B, C, CHALK, 0.10)
        self.play(Create(t1), run_time=1.2)
        la = txt("A", size=26, color=DIM).next_to(P(*A), LEFT, buff=0.12)
        lb = txt("B", size=26, color=DIM).next_to(P(*B), RIGHT, buff=0.12)
        lc = txt("C", size=26, color=DIM).next_to(P(*C), UP, buff=0.12)
        self.play(FadeIn(la), FadeIn(lb), FadeIn(lc), run_time=0.9)

        t2shape = tri(D, E, F, CHALK, 0.10)
        ld = txt("D", size=26, color=DIM).next_to(P(*D), LEFT, buff=0.12)
        le = txt("E", size=26, color=DIM).next_to(P(*E), RIGHT, buff=0.12)
        lf = txt("F", size=26, color=DIM).next_to(P(*F), UP, buff=0.12)
        self.play(FadeIn(t2shape, shift=LEFT * 0.1), run_time=1.3)
        self.play(FadeIn(ld), FadeIn(le), FadeIn(lf), run_time=0.8)
        self.wait(2.2)

        hint = txt("形状一样、大小一样，拿起来能完全重合", size=25, color=DIM)
        hint.move_to([0, -0.5, 0])
        self.play(FadeIn(hint, shift=UP * 0.05), run_time=1.0)
        self.play(FadeOut(ld), FadeOut(le), FadeOut(lf), run_time=0.4)
        self.play(t2shape.animate.shift(LEFT * 6.4), run_time=1.8)
        self.wait(2.0)
        self.play(t2shape.animate.shift(RIGHT * 6.4), run_time=1.2)
        self.play(FadeIn(ld), FadeIn(le), FadeIn(lf), run_time=0.7)
        self.wait(1.2)

        self.play(FadeOut(hint), run_time=0.5)

        note = txt("△ABC ≌ △DEF", size=46, color=GOLD)
        note.move_to([0, -1.25, 0])
        self.play(FadeIn(note, shift=UP * 0.05), run_time=1.2)

        read = txt("读作：三角形 ABC 全等于三角形 DEF", size=26, color=CHALK)
        read.move_to([0, -1.95, 0])
        self.play(FadeIn(read, shift=UP * 0.05), run_time=1.0)
        self.wait(2.2)

        corr = txt("A 对 D　　B 对 E　　C 对 F：顶点要按对应顺序写", size=25, color=GOLD)
        corr.move_to([0, -2.6, 0])
        self.play(FadeIn(corr, shift=UP * 0.05), run_time=1.2)
        self.wait(2.6)

        prop = txt("全等的性质：对应边相等，对应角相等", size=25, color=GREEN)
        prop.move_to([0, -3.22, 0])
        self.play(FadeIn(prop, shift=UP * 0.05), run_time=1.2)
        self.wait(2.4)
        self.finish_section()

    # ---------------- 1. SSS ---------------- 28.9
    def scene_sss(self):
        self.section(1, "判定一：边边边 SSS")

        h = label_box("SSS：三条边分别对应相等 → 两个三角形全等", size=28, color=GOLD)
        h.move_to([0, 2.62, 0])
        self.play(FadeIn(h, scale=0.97), run_time=1.1)
        self.wait(1.4)

        a1, b1, c1 = (-5.6, -0.15), (-2.9, -0.15), (-4.6, 1.75)
        a2, b2, c2 = (2.0, -0.15), (4.7, -0.15), (3.0, 1.75)
        t1 = tri(a1, b1, c1, CHALK, 0.10)
        t2 = tri(a2, b2, c2, CHALK, 0.10)
        self.play(Create(t1), run_time=1.1)
        self.play(Create(t2), run_time=1.1)
        self.wait(1.2)

        m1 = VGroup(
            tick_marks(a1, b1, 1), tick_marks(b1, c1, 2), tick_marks(c1, a1, 3),
        )
        m2 = VGroup(
            tick_marks(a2, b2, 1), tick_marks(b2, c2, 2), tick_marks(c2, a2, 3),
        )
        for g in m1:
            self.play(Create(g), run_time=0.6)
        for g in m2:
            self.play(Create(g), run_time=0.6)
        self.wait(1.8)

        eq = txt("三条边都对上了，三角形就唯一确定了", size=25, color=DIM)
        eq.move_to([0, -1.15, 0])
        self.play(FadeIn(eq, shift=UP * 0.05), run_time=1.0)

        st = label_box("三条边一旦定了，形状就定了 —— 三角形的稳定性", size=27, color=GREEN)
        st.move_to([0, -2.1, 0])
        self.play(FadeIn(st, scale=0.97), run_time=1.2)

        ex = txt("自行车的三角架、屋顶的桁架，用的都是这一条", size=24, color=CHALK)
        ex.move_to([0, -2.95, 0])
        self.play(FadeIn(ex, shift=UP * 0.05), run_time=1.0)
        self.wait(2.8)
        self.finish_section()

    # ---------------- 2. SAS 与 SSA 反例 ---------------- 31.3
    def scene_sas(self):
        self.section(2, "判定二：边角边 SAS")

        h = txt("SAS：两边和它们的夹角分别相等", size=27, color=GOLD)
        h.move_to([0, 2.72, 0])
        self.play(FadeIn(h, shift=UP * 0.05), run_time=0.9)
        self.wait(1.2)

        # 右上角：夹角示意
        sa, sb, sc = (4.0, 0.35), (6.4, 0.35), (4.7, 1.85)
        st = tri(sa, sb, sc, CHALK, 0.08)
        self.play(Create(st), run_time=0.9)
        arc = ang_arc(sa, sb, sc, r=0.62, color=BLUE)
        self.play(Create(arc), run_time=0.7)
        lab = txt("夹角", size=24, color=BLUE).move_to([3.35, 0.62, 0])
        self.play(FadeIn(lab), run_time=0.7)
        self.wait(1.8)

        # 下半区：SSA 反例
        A, B = (-4.4, -1.75), (0.0, -1.75)
        P1, P2 = (-1.23, -0.52), (-3.17, 1.42)

        base = Line(P(*A), P(*B), color=CHALK, stroke_width=3)
        self.play(Create(base), run_time=0.9)
        ray = DashedLine(P(*B), P(-3.85, 1.95), color=DIM, stroke_width=2, dash_length=0.16)
        self.play(Create(ray), run_time=1.0)
        circle = Arc(radius=3.4, start_angle=0.32, angle=0.92, arc_center=P(*A),
                     color=DIM, stroke_width=2)
        self.play(Create(circle), run_time=1.0)

        tA = tri(A, B, P1, BLUE, 0.10)
        tB = tri(A, B, P2, ORANGE, 0.10)
        self.play(Create(tA), run_time=1.1)
        self.play(Create(tB), run_time=1.1)
        self.play(FadeIn(txt("P₁", size=24, color=BLUE).move_to(P(-0.95, -0.30))),
                  run_time=0.6)
        self.play(FadeIn(txt("P₂", size=24, color=ORANGE).move_to(P(-3.30, 1.52))),
                  run_time=0.6)
        self.play(Create(ang_arc(B, A, P1, r=0.7, color=GOLD)), run_time=0.7)
        self.wait(1.6)

        data = txt("AB = 4.4　AC = 3.4　∠B = 45°：两组边一样，却画出两个三角形", size=23, color=CHALK)
        data.move_to([0, -2.62, 0])
        self.play(FadeIn(data, shift=UP * 0.05), run_time=1.1)

        warn = txt("边边角（SSA）不能判定全等", size=26, color=RED)
        warn.move_to([3.45, -1.72, 0])
        self.play(FadeIn(warn, shift=UP * 0.05), run_time=1.0)
        self.wait(2.6)
        self.finish_section()

    # ---------------- 3. ASA / AAS ---------------- 33.2
    def scene_asa(self):
        self.section(3, "判定三：角边角 ASA、角角边 AAS")

        h = txt("两个角加上一条边，也能定住一个三角形", size=26, color=CHALK)
        h.move_to([0, 2.72, 0])
        self.play(FadeIn(h, shift=UP * 0.05), run_time=1.0)
        self.wait(1.0)

        a1, b1, c1 = (-5.8, -0.35), (-3.0, -0.35), (-5.0, 1.7)
        a2, b2, c2 = (1.6, -0.35), (4.4, -0.35), (2.4, 1.7)
        t1 = tri(a1, b1, c1, CHALK, 0.08)
        t2 = tri(a2, b2, c2, CHALK, 0.08)
        self.play(Create(t1), run_time=1.0)
        self.play(Create(t2), run_time=1.0)
        self.wait(1.0)

        # 左：两角 + 夹边
        self.play(Create(ang_arc(a1, b1, c1, r=0.55, color=BLUE)), run_time=0.6)
        self.play(Create(ang_arc(b1, a1, c1, r=0.55, color=BLUE)), run_time=0.6)
        side1 = Line(P(*a1), P(*b1), color=GOLD, stroke_width=5)
        self.play(Create(side1), run_time=0.8)
        l1 = txt("ASA：两角 + 夹边", size=26, color=GOLD)
        l1.move_to([-4.4, -1.35, 0])
        self.play(FadeIn(l1, shift=UP * 0.05), run_time=0.9)
        self.wait(1.6)

        # 右：两角 + 一角的对边
        self.play(Create(ang_arc(a2, b2, c2, r=0.55, color=BLUE)), run_time=0.6)
        self.play(Create(ang_arc(b2, a2, c2, r=0.55, color=BLUE)), run_time=0.6)
        side2 = Line(P(*b2), P(*c2), color=GOLD, stroke_width=5)
        self.play(Create(side2), run_time=0.8)
        l2 = txt("AAS：两角 + 一角的对边", size=26, color=GOLD)
        l2.move_to([3.0, -1.35, 0])
        self.play(FadeIn(l2, shift=UP * 0.05), run_time=0.9)
        self.wait(1.8)

        why = label_box("三角形内角和 = 180°，两个角定了，第三个角也定了", size=26, color=CHALK)
        why.move_to([0, -2.2, 0])
        self.play(FadeIn(why, scale=0.97), run_time=1.2)

        concl = txt("所以 AAS 本质还是 ASA，不必纠结那条边是不是夹边", size=25, color=GREEN)
        concl.move_to([0, -2.95, 0])
        self.play(FadeIn(concl, shift=UP * 0.05), run_time=1.1)
        self.wait(2.6)
        self.finish_section()

    # ---------------- 4. 直角三角形 HL ---------------- 23.5
    def scene_hl(self):
        self.section(4, "直角三角形：斜边、直角边 HL")

        h = txt("斜边和一条直角边分别对应相等 → 两个直角三角形全等", size=26, color=GOLD)
        h.move_to([0, 2.72, 0])
        self.play(FadeIn(h, shift=UP * 0.05), run_time=1.0)
        self.wait(1.2)

        A, B, C = (-5.4, -1.1), (0.4, -1.1), (0.4, 1.85)
        t = tri(A, B, C, CHALK, 0.08)
        self.play(Create(t), run_time=1.2)
        self.play(Create(right_angle(B, A, C, size=0.36, color=DIM)), run_time=0.8)

        la = txt("A", size=24, color=DIM).next_to(P(*A), LEFT, buff=0.14)
        lb = txt("B", size=24, color=DIM).next_to(P(*B), DOWN, buff=0.14)
        lc = txt("C", size=24, color=DIM).next_to(P(*C), UP, buff=0.14)
        self.play(FadeIn(la), FadeIn(lb), FadeIn(lc), run_time=0.8)

        hyp = Line(P(*A), P(*C), color=GOLD, stroke_width=6)
        self.play(Create(hyp), run_time=1.0)
        hl = txt("斜边：直角所对，最长", size=24, color=GOLD).move_to([-3.6, 1.35, 0])
        self.play(FadeIn(hl, shift=RIGHT * 0.05), run_time=0.9)
        self.wait(1.4)

        leg = Line(P(*A), P(*B), color=BLUE, stroke_width=6)
        self.play(Create(leg), run_time=1.0)
        ll = txt("一条直角边", size=24, color=BLUE).move_to([-3.3, -1.75, 0])
        self.play(FadeIn(ll, shift=UP * 0.05), run_time=0.9)
        self.wait(1.6)

        box = txt("两条直角边相等是 SAS，不是 HL", size=25, color=CHALK)
        box.move_to([3.3, 0.9, 0])
        self.play(FadeIn(box, shift=RIGHT * 0.05), run_time=1.0)

        warn = txt("HL 只对直角三角形有效", size=26, color=RED)
        warn.move_to([0, -2.35, 0])
        self.play(FadeIn(warn, shift=UP * 0.05), run_time=1.0)
        self.wait(2.4)
        self.finish_section()

    # ---------------- 5. 证明怎么写 ---------------- 33.8
    def scene_proof(self):
        self.section(5, "证明：先找条件，再下结论")

        h = txt("找三组相等条件，常见的来源有这些", size=26, color=CHALK)
        h.move_to([0, 2.72, 0])
        self.play(FadeIn(h, shift=UP * 0.05), run_time=1.0)
        self.wait(0.8)

        items = [
            ("公共边、公共角", "天然相等"),
            ("对顶角", "相交就相等"),
            ("中点、角平分线", "分出一半"),
            ("两直线平行", "内错角相等"),
            ("垂直", "得到直角"),
        ]
        y = 2.25
        rows = VGroup()
        for name, why in items:
            a = txt(name, size=25, color=GOLD).move_to([-3.5, y, 0])
            b = txt(why, size=24, color=DIM).move_to([2.45, y, 0])
            self.play(FadeIn(a, shift=RIGHT * 0.05), run_time=0.5)
            self.play(FadeIn(b, shift=RIGHT * 0.05), run_time=0.5)
            rows.add(a, b)
            y -= 0.62
        self.wait(1.4)
        self.play(FadeOut(rows), FadeOut(h), run_time=0.6)

        tpl = VGroup(
            txt("在 △ABC 和 △DEF 中：", size=26, color=CHALK),
            txt("AB = DE（已知）　∠B = ∠E（已知）　BC = EF（已知）", size=24, color=CHALK),
            txt("所以 △ABC ≌ △DEF（SAS）", size=27, color=GREEN),
            txt("所以 AB = DE，∠A = ∠D", size=26, color=GOLD),
            txt("（全等三角形的对应边、对应角相等）", size=23, color=DIM),
        ).arrange(DOWN, buff=0.34).move_to([0, -0.5, 0])
        for m in tpl:
            self.play(FadeIn(m, shift=UP * 0.04), run_time=0.8)
        self.wait(2.8)
        self.finish_section()

    # ---------------- 6. 例题与三个易错点 ---------------- 37.5
    def scene_ex(self):
        self.section(6, "例题与三个易错点")

        q = txt("已知 AB = AD，BC = DC，求证 ∠B = ∠D", size=26, color=CHALK)
        q.move_to([0, 2.9, 0])
        self.play(FadeIn(q, shift=UP * 0.05), run_time=1.0)
        self.wait(1.0)

        A, B, C, D = (-4.7, 2.05), (-6.15, 0.55), (-4.7, -0.95), (-3.25, 0.55)
        kite = VGroup(
            Line(P(*A), P(*B), color=CHALK, stroke_width=3),
            Line(P(*B), P(*C), color=CHALK, stroke_width=3),
            Line(P(*C), P(*D), color=CHALK, stroke_width=3),
            Line(P(*D), P(*A), color=CHALK, stroke_width=3),
        )
        for ln in kite:
            self.play(Create(ln), run_time=0.45)
        la = txt("A", size=24, color=DIM).next_to(P(*A), UP, buff=0.10)
        lb = txt("B", size=24, color=DIM).next_to(P(*B), LEFT, buff=0.10)
        lc = txt("C", size=24, color=DIM).next_to(P(*C), DOWN, buff=0.10)
        ld = txt("D", size=24, color=DIM).next_to(P(*D), RIGHT, buff=0.10)
        self.play(FadeIn(la), FadeIn(lb), FadeIn(lc), FadeIn(ld), run_time=0.8)
        self.wait(1.2)

        diag = Line(P(*A), P(*C), color=BLUE, stroke_width=4)
        self.play(Create(diag), run_time=0.9)
        dn = txt("连接 AC：公共边 AC = AC", size=23, color=BLUE)
        dn.move_to([2.6, 2.4, 0])
        self.play(FadeIn(dn, shift=RIGHT * 0.05), run_time=0.9)

        m1 = VGroup(tick_marks(A, B, 1), tick_marks(A, D, 1))
        m2 = VGroup(tick_marks(B, C, 2), tick_marks(C, D, 2))
        self.play(Create(m1), run_time=0.7)
        self.play(Create(m2), run_time=0.7)
        self.wait(1.4)

        steps = VGroup(
            txt("AB = AD，BC = DC（已知）", size=23, color=CHALK),
            txt("AC = AC（公共边）", size=23, color=CHALK),
            txt("所以 △ABC ≌ △ADC（SSS）", size=23, color=GREEN),
            txt("所以 ∠B = ∠D（对应角相等）", size=23, color=GOLD),
        ).arrange(DOWN, buff=0.30).move_to([2.6, 0.72, 0])
        for m in steps:
            self.play(FadeIn(m, shift=UP * 0.04), run_time=0.75)
        self.wait(2.4)

        items = [
            ("把边边角当成边角边", "SSA 不成立"),
            ("顶点顺序不对应", "按 A-D、B-E、C-F 写"),
            ("只写结论，不写理由", "公共边、已知都要注明"),
        ]
        y = -1.75
        for bad_s, good_s in items:
            bad = txt(bad_s, size=23, color=RED).move_to([-3.25, y, 0])
            good = txt(good_s, size=23, color=GREEN).move_to([2.5, y, 0])
            cross = Line([bad.get_left()[0] - 0.06, y - 0.02, 0],
                         [bad.get_right()[0] + 0.06, y - 0.02, 0],
                         color=RED, stroke_width=2.2)
            self.play(FadeIn(bad, shift=RIGHT * 0.05), run_time=0.55)
            self.play(Create(cross), run_time=0.3)
            self.play(FadeIn(good, shift=RIGHT * 0.05), run_time=0.55)
            y -= 0.60

        self.wait(3.0)
        self.finish_section()

    def construct(self):
        self.scene_intro()
        self.clear_stage()
        self.scene_sss()
        self.clear_stage()
        self.scene_sas()
        self.clear_stage()
        self.scene_asa()
        self.clear_stage()
        self.scene_hl()
        self.clear_stage()
        self.scene_proof()
        self.clear_stage()
        self.scene_ex()
        self.clear_stage(0.8)