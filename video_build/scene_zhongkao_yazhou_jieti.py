# -*- coding: utf-8 -*-
"""中考专题 7：压轴题拆解（几何综合）。标图、模型、动点、最值与存在性、答题策略。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


def P(x, y):
    return np.array([float(x), float(y), 0.0])


def label_at(s, pt, dx=0.0, dy=0.0, color=CHALK, size=19):
    return txt(s, size=size, color=color).move_to(P(pt[0] + dx, pt[1] + dy))


def angle_mark(cx, cy, r, a0, sweep, color=GOLD):
    return Arc(radius=r, start_angle=a0 * DEGREES, angle=sweep * DEGREES,
               arc_center=P(cx, cy), color=color, stroke_width=2.2)


class ZhongkaoYazhouJietiScene(NarratedScene):
    lesson = "zhongkao-yazhou-jieti"

    def clear_stage(self, run_time: float = 0.5):
        keep = {id(self._track), id(self._fill)}
        junk = [m for m in self.mobjects if id(m) not in keep]
        if junk:
            self.play(*[FadeOut(m) for m in junk], run_time=run_time)
        self.cur_title = None
        self.cur_sub = None

    # ---------------- 0. 压轴题的分值结构 ---------------- 21.3
    def scene_intro(self):
        self.section(0, "压轴题：先把必得的分拿到")

        chips = [(-4.6, "第 (1) 问 · 基础", GOLD, 3.6),
                 (0.0, "第 (2) 问 · 中等", GREEN, 3.4),
                 (4.3, "第 (3) 问 · 拉分", RED, 3.4)]
        for cx, name, col, w in chips:
            c = label_box(name, size=21, color=col).move_to([cx, 1.75, 0])
            if c.width > w:
                c.scale_to_fit_width(w)
            self.play(FadeIn(c, shift=UP * 0.04), run_time=0.7)
        self.wait(0.5)

        rows = [
            ("前两问是送分题，写清步骤就能拿", CHALK),
            ("整题空着，等于白丢六到八分", RED),
            ("最后一问只考几个固定模型", GOLD),
        ]
        y = 0.75
        for s, col in rows:
            t = txt(s, size=24, color=col).move_to([0, y, 0])
            self.play(FadeIn(t, shift=UP * 0.04), run_time=0.8)
            y -= 0.76
        self.wait(0.5)

        box = label_box("先拿稳的，再冲难的", size=24, color=GOLD)
        box.move_to([0, -2.35, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.0)
        self.wait(6.5)
        self.finish_section()

    # ---------------- 1. 读题先标图 ---------------- 26.5
    def scene_mark(self):
        self.section(1, "读题第一件事：把条件标到图上")

        A = (-5.15, 2.05)
        B = (-6.05, -1.35)
        Cc = (-3.15, -1.55)
        tri = Polygon(P(*A), P(*B), P(*Cc), color=CHALK, stroke_width=2.6)
        self.play(Create(tri), run_time=1.0)

        # 中点 D 在 BC 上
        D = ((Cc[0] + B[0]) / 2, (Cc[1] + B[1]) / 2)
        self.play(FadeIn(Dot(P(*D), radius=0.06, color=GOLD)),
                  FadeIn(label_at("中点", D, -0.05, -0.42, GOLD, 19)), run_time=0.6)
        self.play(Create(Line(P(*A), P(*D), color=GOLD, stroke_width=2.2)), run_time=0.7)

        # 角平分线，终点落在 BC 上
        bis = Line(P(*A), P(-4.45, -1.46), color=GREEN, stroke_width=2.0)
        self.play(Create(bis), run_time=0.7)
        self.play(Create(angle_mark(A[0], A[1], 0.62, -74, 20, GREEN)),
                  FadeIn(label_at("角平分", A, 0.85, -0.6, GREEN, 19)), run_time=0.6)

        # 平行：截线两端落在三角形两边上
        par = Line(P(-5.6, 0.35), P(-4.21, 0.35), color=BLUE, stroke_width=2.0)
        self.play(Create(par), run_time=0.6)
        self.play(FadeIn(label_at("平行", (-3.92, 0.35), 0.0, 0.0, BLUE, 19)), run_time=0.6)
        self.wait(0.4)

        # 两条分支
        b1 = label_box("图形固定", size=21, color=GOLD).move_to([2.9, 1.9, 0])
        self.play(FadeIn(b1, shift=RIGHT * 0.04), run_time=0.7)
        t1 = txt("全等 · 相似 · 特殊四边形", size=20, color=CHALK).move_to([2.9, 1.25, 0])
        self.play(FadeIn(t1), run_time=0.6)

        b2 = label_box("有点在动", size=21, color=ORANGE).move_to([2.9, 0.2, 0])
        self.play(FadeIn(b2, shift=RIGHT * 0.04), run_time=0.7)
        t2 = txt("设元 · 建函数 · 写定义域", size=20, color=CHALK).move_to([2.9, -0.45, 0])
        self.play(FadeIn(t2), run_time=0.6)
        self.wait(0.5)

        box = label_box("标完图，再决定用哪条路", size=21, color=RED)
        box.move_to([2.9, -1.85, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.0)
        self.wait(12.0)
        self.finish_section()

    # ---------------- 2. 一线三等角与手拉手 ---------------- 26.2
    def scene_models(self):
        self.section(2, "模型一：一线三等角与手拉手")

        # 一线三等角：B、C、D 在直线上，A、E 在同侧
        line = Line(P(-6.35, 1.6), P(-1.35, 1.6), color=DIM, stroke_width=2.2)
        self.play(Create(line), run_time=0.7)
        Bp = (-5.9, 1.6)
        Cp = (-3.9, 1.6)
        Dp = (-1.9, 1.6)
        Ap = (-5.2, 2.62)
        Ep = (-2.65, 2.62)
        tri1 = Polygon(P(*Bp), P(*Cp), P(*Ap), color=GOLD, stroke_width=2.4)
        tri2 = Polygon(P(*Cp), P(*Dp), P(*Ep), color=GREEN, stroke_width=2.4)
        self.play(Create(tri1), run_time=0.8)
        self.play(Create(tri2), run_time=0.8)
        # ∠ABC、∠ACE、∠CDE 三处等角
        self.play(Create(angle_mark(Bp[0], Bp[1], 0.45, 0, 56.3, GOLD)), run_time=0.4)
        self.play(Create(angle_mark(Cp[0], Cp[1], 0.5, 40.0, 101.1, GREEN)), run_time=0.4)
        self.play(Create(angle_mark(Dp[0], Dp[1], 0.45, 125.5, 54.5, GREEN)), run_time=0.4)
        self.wait(0.4)

        # 手拉手：两个等腰三角形共顶点 O，顶角相等
        O = (-4.35, -0.55)
        A = (-5.15, 0.84)
        B = (-5.74, -1.35)
        C = (-2.96, 0.25)
        D = (-3.55, -1.94)
        t_a = Polygon(P(*O), P(*A), P(*B), color=BLUE, stroke_width=2.2)
        t_b = Polygon(P(*O), P(*C), P(*D), color=ORANGE, stroke_width=2.2)
        self.play(Create(t_a), run_time=0.7)
        self.play(Create(t_b), run_time=0.7)
        ac = Line(P(*A), P(*C), color=GREEN, stroke_width=2.8)
        bd = Line(P(*B), P(*D), color=GREEN, stroke_width=2.8)
        self.play(Create(ac), Create(bd), run_time=0.9)
        self.play(Create(angle_mark(O[0], O[1], 0.5, 120, 90, GOLD)),
                  Create(angle_mark(O[0], O[1], 0.5, -60, 90, GOLD)), run_time=0.6)
        self.play(FadeIn(txt("AC = BD", size=20, color=GREEN).move_to([-4.35, -2.5, 0])),
                  run_time=0.6)
        self.wait(0.4)

        rows = [
            ("一线三等角 → 两个三角形相似", GOLD),
            ("共顶点 + 两边相等 → 想旋转", BLUE),
            ("手拉手：连出来两条线段相等", GREEN),
            ("夹角等于两个顶角之和或差", CHALK),
        ]
        y = 2.15
        for s, col in rows:
            t = txt(s, size=21, color=col).move_to([3.4, y, 0])
            if t.width > 6.4:
                t.scale_to_fit_width(6.4)
            self.play(FadeIn(t, shift=RIGHT * 0.04), run_time=0.75)
            y -= 0.88
        self.wait(0.5)

        box = label_box("看到共顶点，先想旋转", size=21, color=RED)
        box.move_to([3.4, -1.95, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.0)
        self.wait(11.0)
        self.finish_section()

    # ---------------- 3. 半角模型 ---------------- 25.8
    def scene_half(self):
        self.section(3, "模型二：半角模型，旋转造全等")

        A = (-4.55, 2.05)
        B = (-1.05, 2.05)
        C = (-1.05, -1.45)
        D = (-4.55, -1.45)
        sq = Polygon(P(*A), P(*B), P(*C), P(*D), color=CHALK, stroke_width=2.6)
        self.play(Create(sq), run_time=1.0)
        for pt, nm, dx, dy in [(A, "A", -0.3, 0.24), (B, "B", 0.3, 0.24),
                               (C, "C", 0.3, -0.22), (D, "D", -0.3, -0.22)]:
            self.play(FadeIn(label_at(nm, pt, dx, dy)), run_time=0.25)

        # 从 A 出发的 45°：E 在 BC 上，F 在 CD 上，∠EAF = 45°
        E = (-1.05, 0.42)
        F = (-3.28, -1.45)
        Ep = (-6.18, -1.45)
        self.play(Create(Line(P(*A), P(*E), color=GOLD, stroke_width=2.4)), run_time=0.7)
        self.play(Create(Line(P(*A), P(*F), color=GOLD, stroke_width=2.4)), run_time=0.7)
        self.play(Create(angle_mark(A[0], A[1], 1.05, -70.1, 45.1, RED)), run_time=0.6)
        self.play(FadeIn(txt("45°", size=20, color=RED).move_to([-3.42, 1.3, 0])), run_time=0.5)
        self.play(FadeIn(label_at("E", E, 0.28, 0.0)), FadeIn(label_at("F", F, 0.0, -0.34)),
                  run_time=0.4)

        # 旋转：把 △ABE 绕 A 顺时针转 90°，B → D，E → E′
        lower = Polygon(P(*A), P(*B), P(*E), color=BLUE, stroke_width=2.0)
        lower.set_fill(BLUE, opacity=0.16)
        self.play(FadeIn(lower), run_time=0.7)
        rotated = Polygon(P(*A), P(*D), P(*Ep), color=ORANGE, stroke_width=2.0)
        rotated.set_fill(ORANGE, opacity=0.14)
        self.play(FadeIn(rotated), run_time=1.0)
        self.play(FadeIn(txt("旋转 90°", size=19, color=ORANGE).move_to([-5.9, 1.55, 0])),
                  run_time=0.8)
        self.play(FadeIn(label_at("E′", Ep, -0.05, -0.36, ORANGE)), run_time=0.4)
        self.play(FadeIn(txt("E′、F、C 三点共线", size=19, color=ORANGE).move_to([-3.4, -2.3, 0])),
                  run_time=0.6)
        self.wait(0.4)

        rows = [
            ("45° 是 90° 的一半，30° 是 60° 的一半", GOLD),
            ("把一个小三角形绕顶点旋转", BLUE),
            ("让两条相等的边重合", BLUE),
            ("旋转后说明三点共线，才能连成一条", CHALK),
        ]
        y = 2.05
        for s, col in rows:
            t = txt(s, size=20, color=col).move_to([3.45, y, 0])
            if t.width > 6.3:
                t.scale_to_fit_width(6.3)
            self.play(FadeIn(t, shift=RIGHT * 0.04), run_time=0.75)
            y -= 0.86
        self.wait(0.5)

        box = label_box("半角模型：旋转是关键一步", size=20, color=RED)
        box.move_to([3.45, -1.95, 0])
        if box.width > 6.3:
            box.scale_to_fit_width(6.3)
        self.play(FadeIn(box, scale=0.97), run_time=1.0)
        self.wait(10.0)
        self.finish_section()

    # ---------------- 4. 动点三步 ---------------- 25.8
    def scene_moving(self):
        self.section(4, "动点问题：设元、建式、写定义域")

        cards = [
            ("① 设元", "设时间 t 或线段长 x", GOLD, -4.55),
            ("② 建式", "勾股、相似、面积列函数", GREEN, -1.5),
            ("③ 定义域", "起点到终点，x 有范围", ORANGE, 1.55),
        ]
        for name, desc, col, cx in cards:
            b = label_box(name, size=21, color=col).move_to([cx, 1.75, 0])
            self.play(FadeIn(b, shift=UP * 0.04), run_time=0.6)
            d = txt(desc, size=18, color=CHALK).move_to([cx, 1.05, 0])
            if d.width > 2.9:
                d.scale_to_fit_width(2.9)
            self.play(FadeIn(d), run_time=0.55)
        self.wait(0.4)

        # 线段上动点
        seg = Line(P(-5.9, -0.45), P(-0.1, -0.45), color=DIM, stroke_width=2.4)
        self.play(Create(seg), run_time=0.7)
        self.play(FadeIn(Dot(P(-5.9, -0.45), radius=0.07, color=GOLD)),
                  FadeIn(txt("P", size=19, color=GOLD).move_to([-5.9, -0.85, 0])), run_time=0.5)
        self.play(FadeIn(Dot(P(-0.1, -0.45), radius=0.07, color=GREEN)),
                  FadeIn(txt("Q", size=19, color=GREEN).move_to([-0.1, -0.85, 0])), run_time=0.5)
        moving = Dot(P(-2.9, -0.45), radius=0.09, color=RED)
        lab = txt("M", size=19, color=RED).move_to([-2.9, -0.85, 0])
        self.play(FadeIn(moving), FadeIn(lab), run_time=0.5)
        self.play(moving.animate.move_to(P(-1.5, -0.45)),
                  lab.animate.move_to([-1.5, -0.85, 0]), run_time=1.6)
        self.wait(0.3)

        note = txt("0 ≤ x ≤ 6：起点和终点都要写", size=21, color=ORANGE)
        note.move_to([0, -1.75, 0])
        self.play(FadeIn(note, shift=UP * 0.04), run_time=0.8)
        self.wait(0.5)

        box = label_box("漏写定义域，要扣分", size=22, color=RED)
        box.move_to([0, -2.55, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.0)
        self.wait(8.5)
        self.finish_section()

    # ---------------- 5. 最值与存在性 ---------------- 25.8
    def scene_extremum(self):
        self.section(5, "最后一问：最值与存在性")

        ax = Axes(
            x_range=[0, 4.6, 1],
            y_range=[0, 4.6, 1],
            x_length=4.4,
            y_length=3.2,
            axis_config={"color": DIM, "stroke_width": 2.0,
                         "include_numbers": False, "tip_length": 0.15},
        )
        ax.move_to(P(-3.6, -0.15))
        self.play(Create(ax), run_time=0.9)

        curve = ax.plot(lambda x: -(x - 2) ** 2 + 4, x_range=[0, 4],
                        color=GOLD, stroke_width=2.8)
        self.play(Create(curve), run_time=1.2)
        self.play(FadeIn(Dot(ax.c2p(2, 4), radius=0.07, color=RED)), run_time=0.5)
        self.play(Create(DashedLine(ax.c2p(2, 0), ax.c2p(2, 4), color=RED,
                                    stroke_width=1.6, dash_length=0.08)), run_time=0.6)
        self.play(FadeIn(txt("顶点 (2, 4)", size=19, color=RED).move_to([-2.45, 1.0, 0])),
                  run_time=0.5)
        self.play(FadeIn(txt("0 ≤ x ≤ 4", size=19, color=GREEN).move_to([-4.3, -2.2, 0])),
                  run_time=0.5)
        self.wait(0.4)

        rows = [
            ("配方求顶点，先看顶点在不在范围内", GOLD),
            ("在范围内取顶点，不在就取端点", GREEN),
            ("存在性：等腰按三边两两相等分三类", BLUE),
            ("直角按三个顶点分三类，逐一验证", ORANGE),
        ]
        y = 2.2
        for s, col in rows:
            t = txt(s, size=20, color=col).move_to([3.55, y, 0])
            if t.width > 6.2:
                t.scale_to_fit_width(6.2)
            self.play(FadeIn(t, shift=RIGHT * 0.04), run_time=0.75)
            y -= 0.92
        self.wait(0.5)

        box = label_box("分类讨论，一类都不能漏", size=21, color=RED)
        box.move_to([3.55, -2.05, 0])
        if box.width > 6.2:
            box.scale_to_fit_width(6.2)
        self.play(FadeIn(box, scale=0.97), run_time=1.0)
        self.wait(9.5)
        self.finish_section()

    # ---------------- 6. 策略与易错 ---------------- 22.3
    def scene_strategy(self):
        self.section(6, "答题策略与四个易错点")

        rows = [
            ("① 整题空着", "前两问就有六到八分"),
            ("② 辅助线不写依据", "旋转要写对应关系"),
            ("③ 分类讨论漏情况", "等腰、直角各分三类"),
            ("④ 算完不回到题目", "问什么答什么"),
        ]
        y = 1.85
        for a, b in rows:
            ta = txt(a, size=22, color=RED).move_to([-2.7, y, 0])
            tb = txt(b, size=20, color=DIM).move_to([3.55, y, 0])
            self.play(FadeIn(ta, shift=RIGHT * 0.04), run_time=0.6)
            self.play(FadeIn(tb, shift=RIGHT * 0.04), run_time=0.6)
            y -= 0.86
        self.wait(0.8)

        box = label_box("按步给分，先拿稳的，再冲难的", size=24, color=GOLD)
        box.move_to([0, -2.45, 0])
        if box.width > 10.5:
            box.scale_to_fit_width(10.5)
        self.play(FadeIn(box, scale=0.97), run_time=1.1)
        self.wait(6.0)
        self.finish_section()

    def construct(self):
        self.scene_intro()
        self.clear_stage()
        self.scene_mark()
        self.clear_stage()
        self.scene_models()
        self.clear_stage()
        self.scene_half()
        self.clear_stage()
        self.scene_moving()
        self.clear_stage()
        self.scene_extremum()
        self.clear_stage()
        self.scene_strategy()
        self.clear_stage(0.8)