# -*- coding: utf-8 -*-
"""中考专题 5：圆与三角函数。圆的性质、切线、圆中计算、锐角三角函数、应用。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


def P(x, y):
    return np.array([float(x), float(y), 0.0])


def sector_poly(center, r, a0, a1, color=GOLD, stroke=2.2, fill_opacity=0.14, n=48):
    """用采样弧点自建扇形（规避 Sector/AnnularSector 的渲染问题）。"""
    pts = [P(*center)]
    for k in range(n + 1):
        a = (a0 + (a1 - a0) * k / n) * DEGREES
        pts.append(P(center[0] + r * np.cos(a), center[1] + r * np.sin(a)))
    poly = Polygon(*pts, color=color, stroke_width=stroke)
    poly.set_fill(color, opacity=fill_opacity)
    return poly


def label_at(s, pt, dx=0.0, dy=0.0, color=CHALK, size=19):
    return txt(s, size=size, color=color).move_to(P(pt[0] + dx, pt[1] + dy))


class ZhongkaoYuanSanjiaoHanshuScene(NarratedScene):
    lesson = "zhongkao-yuan-sanjiao-hanshu"

    def clear_stage(self, run_time: float = 0.5):
        keep = {id(self._track), id(self._fill)}
        junk = [m for m in self.mobjects if id(m) not in keep]
        if junk:
            self.play(*[FadeOut(m) for m in junk], run_time=run_time)
        self.cur_title = None
        self.cur_sub = None

    # ---------------- 0. 两条固定套路 ---------------- 27.9
    def scene_intro(self):
        self.section(0, "圆与三角函数：两条固定套路")

        chips = [(-4.85, "圆的性质", GOLD), (-1.62, "切线", GREEN),
                 (1.62, "圆中计算", BLUE), (4.85, "解直角三角形", ORANGE)]
        for cx, name, col in chips:
            c = label_box(name, size=21, color=col).move_to([cx, 1.7, 0])
            self.play(FadeIn(c, shift=UP * 0.04), run_time=0.7)
        self.wait(0.5)

        rows = [
            ("圆：年年一道大题，先证切线，再算长度", CHALK),
            ("三角函数：测高、坡度，题型几乎不变", CHALK),
            ("两部分加起来大约 15 分", GOLD),
            ("套路固定，比的是书写和公式准确", CHALK),
        ]
        y = 0.65
        for s, col in rows:
            t = txt(s, size=23, color=col).move_to([0, y, 0])
            self.play(FadeIn(t, shift=UP * 0.04), run_time=0.7)
            y -= 0.68
        self.wait(0.5)

        box = label_box("性质 · 切线 · 计算 · 解三角形", size=23, color=GOLD)
        box.move_to([0, -2.5, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.0)
        self.wait(11.0)
        self.finish_section()

    # ---------------- 1. 圆的基本性质 ---------------- 19.2
    def scene_circle(self):
        self.section(1, "圆的基本性质：四条跳板")

        O = (-4.35, 0.55)
        r = 1.8
        circ = Circle(radius=r, color=CHALK, stroke_width=2.6).move_to(P(*O))
        self.play(Create(circ), run_time=1.0)
        self.play(FadeIn(Dot(P(*O), radius=0.06, color=GOLD)),
                  FadeIn(label_at("O", O, -0.24, 0.14, GOLD)), run_time=0.5)

        A = (-5.6, -0.65)
        B = (-3.1, -0.65)
        M = (O[0], -0.65)
        chord = Line(P(*A), P(*B), color=GOLD, stroke_width=2.8)
        diam = Line(P(O[0], O[1] + r), P(O[0], O[1] - r), color=BLUE, stroke_width=2.4)
        self.play(Create(chord), run_time=0.8)
        self.play(Create(diam), run_time=0.8)
        self.play(FadeIn(Dot(P(*M), radius=0.05, color=RED)),
                  FadeIn(label_at("M", M, -0.36, -0.2, RED)), run_time=0.5)
        self.play(Create(RightAngle(chord, diam, length=0.2, color=RED)), run_time=0.6)
        self.play(FadeIn(label_at("A", A, -0.26, -0.12)),
                  FadeIn(label_at("B", B, 0.26, -0.12)), run_time=0.5)
        self.wait(0.4)

        rows = [
            ("垂径定理：垂直于弦的直径平分弦与弧", GOLD),
            ("同弧所对圆周角 = 圆心角的一半", GREEN),
            ("直径所对的圆周角是 90°", BLUE),
            ("圆内接四边形对角互补", ORANGE),
        ]
        y = 2.15
        for s, col in rows:
            t = txt(s, size=21, color=col).move_to([3.45, y, 0])
            if t.width > 6.4:
                t.scale_to_fit_width(6.4)
            self.play(FadeIn(t, shift=RIGHT * 0.04), run_time=0.75)
            y -= 0.78
        self.wait(0.5)

        box = label_box("这四条是证明题的跳板", size=21, color=RED)
        box.move_to([3.45, -1.85, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.0)
        self.wait(4.0)
        self.finish_section()

    # ---------------- 2. 切线 ---------------- 27.2
    def scene_tangent(self):
        self.section(2, "切线：判定与性质")

        O = (-4.75, -0.25)
        r = 1.5
        circ = Circle(radius=r, color=CHALK, stroke_width=2.6).move_to(P(*O))
        self.play(Create(circ), run_time=0.9)
        self.play(FadeIn(Dot(P(*O), radius=0.06, color=GOLD)),
                  FadeIn(label_at("O", O, -0.26, 0.1, GOLD)), run_time=0.5)

        Q = (-1.35, -0.25)
        self.play(FadeIn(Dot(P(*Q), radius=0.07, color=ORANGE)),
                  FadeIn(label_at("Q", Q, 0.24, -0.14, ORANGE)), run_time=0.5)

        ang = np.arccos(r / 3.4)
        T1 = (O[0] + r * np.cos(ang), O[1] + r * np.sin(ang))
        T2 = (O[0] + r * np.cos(ang), O[1] - r * np.sin(ang))
        l1 = Line(P(*Q), P(*T1), color=GREEN, stroke_width=2.6)
        l2 = Line(P(*Q), P(*T2), color=GREEN, stroke_width=2.6)
        r1 = Line(P(*O), P(*T1), color=BLUE, stroke_width=2.2)
        r2 = Line(P(*O), P(*T2), color=BLUE, stroke_width=2.2)
        self.play(Create(l1), Create(l2), run_time=1.0)
        self.play(Create(r1), Create(r2), run_time=0.9)
        self.play(Create(RightAngle(l1, r1, length=0.2, color=RED)),
                  Create(RightAngle(l2, r2, length=0.2, color=RED)), run_time=0.7)
        self.play(FadeIn(label_at("P", T1, -0.3, 0.24, GREEN)),
                  FadeIn(label_at("E", T2, -0.3, -0.24, GREEN)), run_time=0.5)
        self.wait(0.4)

        rows = [
            ("有公共点：连半径，证垂直", GOLD),
            ("无公共点：作垂线，证 d = r", GOLD),
            ("性质：切线 ⊥ 过切点的半径", BLUE),
            ("外点两切线长相等，连线平分夹角", GREEN),
        ]
        y = 2.2
        for s, col in rows:
            t = txt(s, size=21, color=col).move_to([3.45, y, 0])
            if t.width > 6.4:
                t.scale_to_fit_width(6.4)
            self.play(FadeIn(t, shift=RIGHT * 0.04), run_time=0.8)
            y -= 0.78
        self.wait(0.5)

        box = label_box("判定看条件，性质看结论", size=21, color=RED)
        box.move_to([3.45, -1.85, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.0)
        self.wait(11.5)
        self.finish_section()

    # ---------------- 3. 圆中计算 ---------------- 19.3
    def scene_calc(self):
        self.section(3, "圆中计算：弧长、扇形、圆锥")

        C = (-4.0, -0.2)
        r = 1.9
        circ = Circle(radius=r, color=DIM, stroke_width=2.0).move_to(P(*C))
        self.play(Create(circ), run_time=0.8)
        sec = sector_poly(C, r, 18, 112, color=GOLD, fill_opacity=0.16)
        self.play(FadeIn(sec), run_time=1.0)
        self.play(Create(Line(P(*C), P(C[0] + r * np.cos(18 * DEGREES), C[1] + r * np.sin(18 * DEGREES)),
                              color=GOLD, stroke_width=2.4)),
                  Create(Line(P(*C), P(C[0] + r * np.cos(112 * DEGREES), C[1] + r * np.sin(112 * DEGREES)),
                              color=GOLD, stroke_width=2.4)), run_time=0.8)
        arc = Arc(radius=r, start_angle=18 * DEGREES, angle=94 * DEGREES,
                  arc_center=P(*C), color=RED, stroke_width=4.0)
        self.play(Create(arc), run_time=0.9)
        self.play(FadeIn(txt("n°", size=20, color=RED).move_to(P(C[0] + 0.55, C[1] + 0.5))), run_time=0.5)
        self.wait(0.4)

        rows = [
            ("弧长 ℓ = nπr / 180", GOLD),
            ("扇形 S = nπr² / 360 = ½ℓr", GOLD),
            ("圆锥侧面展开是扇形", BLUE),
            ("扇形弧长 = 底面周长", GREEN),
            ("扇形半径 = 母线长", GREEN),
        ]
        y = 2.3
        for s, col in rows:
            t = txt(s, size=21, color=col).move_to([3.45, y, 0])
            if t.width > 6.4:
                t.scale_to_fit_width(6.4)
            self.play(FadeIn(t, shift=RIGHT * 0.04), run_time=0.7)
            y -= 0.7
        self.wait(0.5)

        box = label_box("把 n、r、母线对应清楚", size=21, color=RED)
        box.move_to([3.45, -1.85, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.0)
        self.wait(3.5)
        self.finish_section()

    # ---------------- 4. 锐角三角函数 ---------------- 24.6
    def scene_trig(self):
        self.section(4, "锐角三角函数：三个比")

        A = (-5.85, 1.05)
        B = (-2.15, -1.45)
        Cc = (-5.85, -1.45)
        tri = Polygon(P(*A), P(*B), P(*Cc), color=CHALK, stroke_width=2.6)
        self.play(Create(tri), run_time=1.0)
        self.play(Create(RightAngle(Line(P(*Cc), P(*B)), Line(P(*Cc), P(*A)),
                                    length=0.24, color=RED)), run_time=0.6)
        self.play(FadeIn(label_at("A", A, -0.12, 0.26)),
                  FadeIn(label_at("B", B, 0.28, -0.14)),
                  FadeIn(label_at("C", Cc, -0.3, -0.16)), run_time=0.6)
        # ∠A = 55.95°，从 −90° 扫到 −34.05°
        self.play(Create(Arc(radius=0.7, start_angle=-90 * DEGREES,
                             angle=55.95 * DEGREES, arc_center=P(*A),
                             color=GOLD, stroke_width=2.4)), run_time=0.7)
        self.wait(0.2)

        self.play(FadeIn(txt("对边", size=20, color=GOLD).move_to([-4.0, -1.8, 0])),
                  run_time=0.5)
        self.play(FadeIn(txt("邻边", size=20, color=GREEN).move_to([-5.35, -0.15, 0])),
                  run_time=0.5)
        self.play(FadeIn(txt("斜边", size=20, color=BLUE).move_to([-3.7, 0.12, 0])),
                  run_time=0.5)
        self.wait(0.4)

        rows = [
            ("sin A = 对边 / 斜边", GOLD),
            ("cos A = 邻边 / 斜边", GREEN),
            ("tan A = 对边 / 邻边", BLUE),
            ("已知两边：勾股 + 三角函数", CHALK),
            ("已知一边一角：直接用三角函数", CHALK),
        ]
        y = 2.3
        for s, col in rows:
            t = txt(s, size=21, color=col).move_to([3.4, y, 0])
            self.play(FadeIn(t, shift=RIGHT * 0.04), run_time=0.7)
            y -= 0.7
        self.wait(0.4)

        spec = txt("sin30° = ½    cos45° = √2/2    tan60° = √3", size=19, color=ORANGE)
        spec.move_to([-1.55, -2.5, 0])
        self.play(FadeIn(spec, shift=UP * 0.04), run_time=0.85)
        self.wait(0.5)

        box = label_box("三个比，对应三个角", size=21, color=RED)
        box.move_to([3.55, -2.1, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.0)
        self.wait(6.0)
        self.finish_section()

    # ---------------- 5. 应用题 ---------------- 20.3
    def scene_apply(self):
        self.section(5, "应用题：仰角、坡度、方位角")

        ground = Line(P(-6.3, -1.85), P(-0.6, -1.85), color=DIM, stroke_width=2.2)
        self.play(Create(ground), run_time=0.7)
        obs = (-5.7, -1.85)
        top = (-2.6, 0.75)
        tower = Line(P(top[0], -1.85), P(*top), color=CHALK, stroke_width=2.6)
        self.play(Create(tower), run_time=0.8)
        sight = Line(P(*obs), P(*top), color=GOLD, stroke_width=2.6)
        self.play(Create(sight), run_time=0.9)
        self.play(Create(Arc(radius=1.35, start_angle=0,
                             angle=40.0 * DEGREES, arc_center=P(*obs),
                             color=RED, stroke_width=2.4)), run_time=0.7)
        self.play(FadeIn(txt("仰角 α", size=20, color=RED).move_to([-3.45, -1.6, 0])),
                  FadeIn(Dot(P(*obs), radius=0.06, color=GOLD)), run_time=0.6)
        self.wait(0.4)

        rows = [
            ("仰角、俯角：都从水平线量起", GOLD),
            ("坡度 i = 竖直高 / 水平宽 = tan 坡角", GREEN),
            ("坡度是比值，不是角度", RED),
            ("方位角：从正北或正南量起", BLUE),
            ("斜三角形：作高拆成两个直角三角形", CHALK),
        ]
        y = 2.25
        for s, col in rows:
            t = txt(s, size=21, color=col).move_to([3.45, y, 0])
            if t.width > 6.4:
                t.scale_to_fit_width(6.4)
            self.play(FadeIn(t, shift=RIGHT * 0.04), run_time=0.7)
            y -= 0.76
        self.wait(0.5)

        box = label_box("先找直角三角形，再找边角关系", size=21, color=RED)
        box.move_to([3.45, -2.15, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.0)
        self.wait(3.5)
        self.finish_section()

    # ---------------- 6. 易错点 ---------------- 18.2
    def scene_traps(self):
        self.section(6, "四个易错点")

        rows = [
            ("① 圆周角与圆心角对错", "先看清是哪条弧"),
            ("② 证切线不连半径", "连半径才有垂直"),
            ("③ 把坡度当坡角", "坡度是正切值"),
            ("④ 特殊角函数值记混", "30、45、60 列表背"),
        ]
        y = 1.85
        for a, b in rows:
            ta = txt(a, size=23, color=RED).move_to([-2.65, y, 0])
            tb = txt(b, size=20, color=DIM).move_to([3.55, y, 0])
            self.play(FadeIn(ta, shift=RIGHT * 0.04), run_time=0.6)
            self.play(FadeIn(tb, shift=RIGHT * 0.04), run_time=0.6)
            y -= 0.86
        self.wait(0.8)

        box = label_box("先画图，再找直角三角形", size=27, color=GOLD)
        box.move_to([0, -2.45, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.1)
        self.wait(5.0)
        self.finish_section()

    def construct(self):
        self.scene_intro()
        self.clear_stage()
        self.scene_circle()
        self.clear_stage()
        self.scene_tangent()
        self.clear_stage()
        self.scene_calc()
        self.clear_stage()
        self.scene_trig()
        self.clear_stage()
        self.scene_apply()
        self.clear_stage()
        self.scene_traps()
        self.clear_stage(0.8)