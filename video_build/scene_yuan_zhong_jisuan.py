# -*- coding: utf-8 -*-
"""圆中的计算：弧长、扇形面积、圆锥的侧面积。九年级上。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


def P(x, y):
    return np.array([float(x), float(y), 0.0])


def pt(cx: float, cy: float, r: float, deg: float):
    a = deg * np.pi / 180.0
    return P(cx + r * np.cos(a), cy + r * np.sin(a))


def circ(cx: float, cy: float, r: float, color=CHALK, width: float = 2.8) -> Circle:
    return Circle(radius=r, color=color, stroke_width=width).move_to([cx, cy, 0])


def sector(cx: float, cy: float, r: float, a0: float, a1: float,
           color=GOLD, fill_opacity: float = 0.10, width: float = 2.4) -> VGroup:
    """扇形：两条半径 + 一段弧（带淡填充）。"""
    a = Arc(radius=r, start_angle=a0 * DEGREES, angle=(a1 - a0) * DEGREES,
            arc_center=P(cx, cy), color=color, stroke_width=3.2)
    l1 = Line(P(cx, cy), pt(cx, cy, r, a0), color=color, stroke_width=width)
    l2 = Line(P(cx, cy), pt(cx, cy, r, a1), color=color, stroke_width=width)
    fan = Sector(radius=r, start_angle=a0 * DEGREES, angle=(a1 - a0) * DEGREES,
                 arc_center=P(cx, cy), color=color, stroke_width=0,
                 fill_color=color, fill_opacity=fill_opacity)
    return VGroup(fan, a, l1, l2)


class YuanZhongJisuanScene(NarratedScene):
    lesson = "yuan-zhong-jisuan"

    def clear_stage(self, run_time: float = 0.5):
        keep = {id(self._track), id(self._fill)}
        junk = [m for m in self.mobjects if id(m) not in keep]
        if junk:
            self.play(*[FadeOut(m) for m in junk], run_time=run_time)
        self.cur_title = None
        self.cur_sub = None

    # ---------------- 0. 弧与扇形 ---------------- 29.6
    def scene_intro(self):
        self.section(0, "一段弧，一块扇形")

        c = circ(-3.6, 0.55, 1.75, CHALK, 2.6)
        self.play(Create(c), run_time=1.1)
        ar = Arc(radius=1.75, start_angle=20 * DEGREES, angle=110 * DEGREES,
                 arc_center=P(-3.6, 0.55), color=GOLD, stroke_width=6.0)
        l1 = Line(P(-3.6, 0.55), pt(-3.6, 0.55, 1.75, 20), color=GOLD, stroke_width=2.4)
        l2 = Line(P(-3.6, 0.55), pt(-3.6, 0.55, 1.75, 130), color=GOLD, stroke_width=2.4)
        self.play(Create(ar), run_time=1.0)
        self.play(Create(l1), Create(l2), run_time=0.8)

        ang_arc = Arc(radius=0.5, start_angle=20 * DEGREES, angle=110 * DEGREES,
                      arc_center=P(-3.6, 0.55), color=BLUE, stroke_width=2.6)
        rad_line = Line(P(-3.6, 0.55), pt(-3.6, 0.55, 1.75, 270),
                        color=GREEN, stroke_width=2.4)
        self.play(Create(ang_arc), Create(rad_line), run_time=0.9)

        ln = txt("弧长 ℓ", size=23, color=GOLD).move_to([-3.6, 2.68, 0])
        rad = txt("半径 r", size=23, color=GREEN).move_to([-3.12, -0.72, 0])
        ang = txt("n°", size=22, color=BLUE).move_to([-3.36, 1.3, 0])
        self.play(FadeIn(ln), FadeIn(rad), FadeIn(ang), run_time=0.9)
        self.wait(1.0)

        rows = [
            ("跑道弯道：一段圆弧", GOLD),
            ("折扇扇面：一个扇形", BLUE),
            ("圆心角占 360° 的几分之几", GREEN),
            ("弧长、面积就占整个圆的几分之几", GREEN),
        ]
        y = 2.35
        for s, col in rows:
            t = txt(s, size=23, color=col).move_to([3.2, y, 0])
            self.play(FadeIn(t, shift=RIGHT * 0.04), run_time=0.8)
            y -= 0.8
        self.wait(1.0)

        box = label_box("只和两个量有关：圆心角 n 与半径 r", size=23, color=GOLD)
        box.move_to([0, -2.65, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.05)
        self.wait(15.0)
        self.finish_section()

    # ---------------- 1. 弧长公式 ---------------- 25.2
    def scene_arc(self):
        self.section(1, "弧长：ℓ = nπr / 180")

        c = circ(-3.5, 0.6, 1.6, CHALK, 2.5)
        self.play(Create(c), run_time=1.0)
        rd = Line(P(-3.5, 0.6), pt(-3.5, 0.6, 1.6, 30), color=GREEN, stroke_width=2.6)
        self.play(Create(rd), run_time=0.8)
        rl = txt("r", size=24, color=GREEN).move_to([-2.55, 0.95, 0])
        self.play(FadeIn(rl), run_time=0.5)
        self.wait(0.6)

        rows = [
            ("圆的周长 = 2πr", CHALK),
            ("整个圆 = 360°", CHALK),
            ("圆心角 n° 占 n/360", GOLD),
            ("ℓ = (n/360) · 2πr", GOLD),
        ]
        y = 2.0
        for s, col in rows:
            t = txt(s, size=27, color=col).move_to([3.0, y, 0])
            self.play(FadeIn(t, shift=UP * 0.04), run_time=0.85)
            y -= 0.78
        self.wait(0.8)

        res = txt("ℓ = nπr / 180", size=40, color=GOLD).move_to([3.0, -1.25, 0])
        self.play(FadeIn(res, scale=0.98), run_time=1.0)
        self.wait(0.7)

        note = txt("分母是 180：分子里的 2 和 360 约掉了一个 2", size=22, color=RED)
        note.move_to([0, -2.62, 0])
        self.play(FadeIn(note, shift=UP * 0.04), run_time=0.95)
        self.wait(10.5)
        self.finish_section()

    # ---------------- 2. 扇形面积 ---------------- 25.1
    def scene_area(self):
        self.section(2, "扇形面积：两个公式")

        fan = sector(-3.2, 0.4, 1.9, 25, 145, GOLD, 0.10)
        self.play(Create(fan), run_time=1.4)
        rl = txt("r", size=23, color=GREEN).move_to([-1.35, 1.28, 0])
        self.play(FadeIn(rl), run_time=0.5)
        self.wait(0.7)

        f1 = txt("S = (n/360) · πr²", size=32, color=GOLD).move_to([3.1, 1.8, 0])
        self.play(FadeIn(f1, scale=0.98), run_time=1.0)
        self.wait(0.6)

        f2 = txt("S = ½ ℓ r", size=38, color=GREEN).move_to([3.1, 0.55, 0])
        self.play(FadeIn(f2, scale=0.98), run_time=1.0)
        self.wait(0.7)

        note = txt("已知弧长时，用 ½ ℓ r 更快", size=24, color=CHALK)
        note.move_to([3.1, -0.65, 0])
        self.play(FadeIn(note, shift=UP * 0.04), run_time=0.9)
        self.wait(0.7)

        expl = txt("把扇形看成一个三角形：底是弧 ℓ，高是 r", size=22, color=DIM)
        expl.move_to([0, -2.2, 0])
        self.play(FadeIn(expl, shift=UP * 0.04), run_time=0.95)
        self.wait(8.5)
        self.finish_section()

    # ---------------- 3. 圆锥侧面展开 ---------------- 21.1
    def scene_cone(self):
        self.section(3, "圆锥侧面展开是扇形")

        apex = P(-4.6, 1.6)
        base_l = P(-5.6, -0.9)
        base_r = P(-3.6, -0.9)
        side1 = Line(apex, base_l, color=CHALK, stroke_width=2.6)
        side2 = Line(apex, base_r, color=CHALK, stroke_width=2.6)
        base = Ellipse(width=2.0, height=0.55, color=CHALK, stroke_width=2.4)
        base.move_to([-4.6, -0.9, 0])
        self.play(Create(side1), Create(side2), run_time=1.0)
        self.play(Create(base), run_time=0.9)

        ll = txt("母线 ℓ", size=22, color=GREEN).move_to([-5.75, 0.95, 0])
        rl = txt("半径 r", size=22, color=BLUE).move_to([-4.6, -1.45, 0])
        self.play(FadeIn(ll), FadeIn(rl), run_time=0.8)
        self.wait(0.8)

        # 展开后的扇形
        fan = sector(3.0, -0.5, 1.75, 55, 155, GOLD, 0.10)
        self.play(Create(fan), run_time=1.4)

        a1 = txt("扇形半径 = 母线 ℓ", size=23, color=GREEN).move_to([3.0, 2.15, 0])
        a2 = txt("扇形弧长 = 底面周长 2πr", size=23, color=BLUE).move_to([3.0, 1.55, 0])
        self.play(FadeIn(a1, shift=UP * 0.04), run_time=0.85)
        self.play(FadeIn(a2, shift=UP * 0.04), run_time=0.85)
        self.wait(0.8)

        arr = Arrow(P(-3.2, -0.1), P(1.0, -0.1), color=DIM, stroke_width=2.2,
                    buff=0, max_tip_length_to_length_ratio=0.15)
        self.play(GrowArrow(arr), run_time=0.8)
        self.wait(0.8)

        note = txt("这两个对应关系，是圆锥计算的关键", size=23, color=RED)
        note.move_to([0, -2.35, 0])
        self.play(FadeIn(note, shift=UP * 0.04), run_time=0.95)
        self.wait(7.0)
        self.finish_section()

    # ---------------- 4. 侧面积与全面积 ---------------- 23.6
    def scene_surface(self):
        self.section(4, "侧面积与全面积")

        f1 = txt("S侧 = ½ · (2πr) · ℓ", size=32, color=CHALK).move_to([0, 2.05, 0])
        self.play(FadeIn(f1, shift=UP * 0.04), run_time=0.95)
        self.wait(0.8)

        f2 = txt("S侧 = πrℓ", size=44, color=GOLD).move_to([0, 0.95, 0])
        self.play(FadeIn(f2, scale=0.98), run_time=1.0)
        self.wait(0.9)

        f3 = txt("S全 = πrℓ + πr²", size=38, color=GREEN).move_to([0, -0.25, 0])
        self.play(FadeIn(f3, scale=0.98), run_time=1.0)
        self.wait(0.8)

        note1 = txt("底面圆：πr²，求全面积别忘加", size=23, color=DIM)
        note1.move_to([0, -1.45, 0])
        self.play(FadeIn(note1, shift=UP * 0.04), run_time=0.9)
        self.wait(0.7)

        box = label_box("母线 ℓ 是直角三角形的斜边，一定比 r 长", size=22, color=RED)
        box.move_to([0, -2.55, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.05)
        self.wait(9.5)
        self.finish_section()

    # ---------------- 5. 例题 ---------------- 26.3
    def scene_example(self):
        self.section(5, "例：半径 6，圆心角 120°")

        head = txt("半径 r = 6，圆心角 n = 120°", size=26, color=CHALK).move_to([0, 2.15, 0])
        self.play(FadeIn(head, shift=UP * 0.04), run_time=0.9)
        self.wait(0.7)

        rows = [
            ("弧长 ℓ = (120/180) · π · 6 = 4π", GOLD),
            ("面积 S = (120/360) · π · 36 = 12π", GREEN),
            ("验证：½ ℓ r = ½ · 4π · 6 = 12π", BLUE),
        ]
        y = 1.05
        for s, col in rows:
            t = txt(s, size=28, color=col).move_to([0, y, 0])
            self.play(FadeIn(t, shift=UP * 0.04), run_time=0.9)
            y -= 0.95
        self.wait(1.0)

        note = txt("两个公式算出来一样，说明公式没记错", size=23, color=DIM)
        note.move_to([0, -1.95, 0])
        self.play(FadeIn(note, shift=UP * 0.04), run_time=0.95)
        self.wait(0.8)

        box = label_box("先算弧长，再用 ½ ℓ r 验证", size=24, color=GOLD)
        box.move_to([0, -2.9, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.0)
        self.wait(11.0)
        self.finish_section()

    # ---------------- 6. 四个易错点 ---------------- 27.8
    def scene_traps(self):
        self.section(6, "四个易错点")

        rows = [
            ("① 弧长分母写成 360", "应该是 180"),
            ("② ½ ℓ r 里的 ℓ 是弧长", "不是半径，也不是母线"),
            ("③ 圆锥展开后扇形半径是母线", "不是底面半径 r"),
            ("④ 求全面积忘加底面圆", "侧面积 + πr²"),
        ]
        y = 1.85
        for a, b in rows:
            ta = txt(a, size=23, color=RED).move_to([-2.6, y, 0])
            tb = txt(b, size=21, color=DIM).move_to([3.6, y, 0])
            self.play(FadeIn(ta, shift=RIGHT * 0.04), run_time=0.65)
            self.play(FadeIn(tb, shift=RIGHT * 0.04), run_time=0.65)
            y -= 0.86
        self.wait(1.0)

        box = label_box("先看圆心角占几分之几，再套公式", size=24, color=GOLD)
        box.move_to([0, -2.45, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.1)
        self.wait(11.5)
        self.finish_section()

    def construct(self):
        self.scene_intro()
        self.clear_stage()
        self.scene_arc()
        self.clear_stage()
        self.scene_area()
        self.clear_stage()
        self.scene_cone()
        self.clear_stage()
        self.scene_surface()
        self.clear_stage()
        self.scene_example()
        self.clear_stage()
        self.scene_traps()
        self.clear_stage(0.8)