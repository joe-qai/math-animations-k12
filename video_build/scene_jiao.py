# -*- coding: utf-8 -*-
"""角的认识：一个顶点两条边，直角、锐角、钝角。二年级下册。"""

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


def ray(vertex, deg, length, color=CHALK, width=4.5) -> Line:
    v = [vertex[0], vertex[1], 0]
    end = [vertex[0] + length * math.cos(math.radians(deg)),
           vertex[1] + length * math.sin(math.radians(deg)), 0]
    return Line(v, end, color=color, stroke_width=width)


def arc(vertex, a1, a2, radius=0.7, color=GOLD, width=3.5) -> Arc:
    return Arc(radius=radius, start_angle=a1 * DEGREES, angle=(a2 - a1) * DEGREES,
               arc_center=[vertex[0], vertex[1], 0], color=color, stroke_width=width)


def right_mark(vertex, length=0.3, color=CHALK) -> Polygon:
    v = [vertex[0], vertex[1], 0]
    p1 = [v[0] + length, v[1], 0]
    p2 = [v[0] + length, v[1] + length, 0]
    p3 = [v[0], v[1] + length, 0]
    return Polygon(v, p1, p2, p3, color=color, stroke_width=2.2, fill_opacity=0)


def ruler(vertex, leg=2.2, color=BLUE) -> VGroup:
    """三角尺：直角在 vertex，一条直角边向右，一条向上。"""
    v = [vertex[0], vertex[1], 0]
    p1 = [v[0] + leg, v[1], 0]
    p2 = [v[0], v[1] + leg, 0]
    tri = Polygon(v, p1, p2, color=color, stroke_width=3,
                  fill_color=color, fill_opacity=0.1)
    mark = right_mark(vertex, 0.34, color=color)
    return VGroup(tri, mark)


def corner_gauge(vertex, leg=2.2, color=BLUE) -> VGroup:
    """直角尺：只画两条互相垂直的边和直角符号，用来判断「里面 / 外面」。"""
    h = ray(vertex, 0, leg, color=color, width=4.5)
    v = ray(vertex, 90, leg, color=color, width=4.5)
    return VGroup(h, v, right_mark(vertex, 0.32, color=color))


class JiaoScene(NarratedScene):
    lesson = "jiao-renshi"

    def clear_stage(self, run_time: float = 0.5):
        keep = {id(self._track), id(self._fill)}
        junk = [m for m in self.mobjects if id(m) not in keep]
        if junk:
            self.play(*[FadeOut(m) for m in junk], run_time=run_time)
        self.cur_title = None
        self.cur_sub = None

    # ---------------- 0. 生活中的角 ----------------
    def scene_life(self):
        self.section(0, "身边的角")

        # 剪刀
        sv = [-4.2, -1.3]
        sc1 = ray(sv, 20, 2.2, color=CHALK, width=5)
        sc2 = ray(sv, 68, 2.2, color=CHALK, width=5)
        sc_dot = Dot([sv[0], sv[1], 0], radius=0.09, color=GOLD)

        # 钟面指针
        cv = [-0.1, -1.3]
        c1 = ray(cv, 25, 2.0, color=GOLD, width=5)
        c2 = ray(cv, 115, 1.7, color=BLUE, width=5)

        # 扇子
        fv = [3.9, -1.3]
        f1 = ray(fv, 40, 2.1, color=RED, width=5)
        f2 = ray(fv, 125, 2.1, color=RED, width=5)
        f_arc = Arc(radius=1.7, start_angle=40 * DEGREES, angle=85 * DEGREES,
                    arc_center=[fv[0], fv[1], 0], color=RED, stroke_width=2,
                    stroke_opacity=0.7)

        self.play(Create(sc1), Create(sc2), FadeIn(sc_dot), run_time=0.8)
        self.play(Create(c1), Create(c2), run_time=0.8)
        self.play(Create(f1), Create(f2), Create(f_arc), run_time=0.9)

        labs = VGroup(
            txt("剪刀的角", size=28, color=DIM).move_to([-4.2, -2.05, 0]),
            txt("指针的角", size=28, color=DIM).move_to([-0.1, -2.05, 0]),
            txt("扇子的角", size=28, color=DIM).move_to([3.9, -2.05, 0]),
        )
        self.play(FadeIn(labs), run_time=0.7)
        self.finish_section()

    # ---------------- 1. 一个顶点，两条边 ----------------
    def scene_parts(self):
        self.section(1, "角：一个顶点，两条边")

        v = [-4.3, -1.1]
        a = ray(v, 18, 4.4, color=GOLD)
        b = ray(v, 104, 4.4, color=BLUE)
        dot = Dot([v[0], v[1], 0], radius=0.1, color=CHALK)
        self.play(Create(a), run_time=0.7)
        self.play(Create(b), run_time=0.7)
        self.play(FadeIn(dot), run_time=0.3)
        ang = arc(v, 18, 104, radius=0.75, color=CHALK)
        self.play(Create(ang), run_time=0.5)

        l1 = txt("顶点", size=30, color=CHALK).move_to([v[0] - 0.65, v[1] - 0.55, 0])
        l2 = txt("边", size=32, color=GOLD).move_to([v[0] + 2.3, v[1] + 0.25, 0])
        l3 = txt("边", size=32, color=BLUE).move_to([v[0] + 0.45, v[1] + 2.6, 0])
        self.play(FadeIn(l1), FadeIn(l2), FadeIn(l3), run_time=0.7)

        note = VGroup(
            txt("一个顶点", size=34, color=CHALK),
            txt("两条直直的边", size=34, color=CHALK),
            label_box("角的两条边从顶点出发", size=24, color=GREEN),
        ).arrange(DOWN, buff=0.35).move_to([3.6, 0.4, 0])
        self.play(FadeIn(note, shift=UP * 0.08), run_time=0.9)
        self.finish_section()

    # ---------------- 2. 角的大小看张口 ----------------
    def scene_size(self):
        self.section(2, "角的大小，看张口")

        # 左：张口大，角大
        v1 = [-5.0, -0.5]
        s1 = ray(v1, 20, 2.0, color=GOLD)
        s2 = ray(v1, 55, 2.0, color=GOLD)
        self.play(Create(s1), Create(s2), Create(arc(v1, 20, 55, 0.6)), run_time=0.7)
        small_lab = txt("张口小，角小", size=26, color=DIM).move_to([-5.0, -1.55, 0])
        self.play(FadeIn(small_lab), run_time=0.4)

        v2 = [-1.2, -0.5]
        b1 = ray(v2, 20, 2.0, color=BLUE)
        b2 = ray(v2, 100, 2.0, color=BLUE)
        self.play(Create(b1), Create(b2), Create(arc(v2, 20, 100, 0.6, color=BLUE)), run_time=0.7)
        big_lab = txt("张口大，角大", size=26, color=DIM).move_to([-1.2, -1.55, 0])
        self.play(FadeIn(big_lab), run_time=0.4)

        # 右：边变长，角不变
        v3 = [3.5, -0.5]
        c1 = ray(v3, 35, 1.4, color=GREEN)
        c2 = ray(v3, 95, 1.4, color=GREEN)
        ang3 = arc(v3, 35, 95, 0.5, color=GREEN)
        self.play(FadeIn(VGroup(c1, c2, ang3)), run_time=0.6)

        c1e = ray(v3, 35, 3.3, color=GREEN, width=2)
        c2e = ray(v3, 95, 3.3, color=GREEN, width=2)
        self.play(GrowFromPoint(c1e, [v3[0], v3[1], 0]),
                  GrowFromPoint(c2e, [v3[0], v3[1], 0]), run_time=1.0)

        fixed = txt("边变长，角不变", size=28, color=GREEN).move_to([3.6, -2.15, 0])
        self.play(FadeIn(fixed, shift=UP * 0.08), run_time=0.6)
        self.finish_section()

    # ---------------- 3. 直角 ----------------
    def scene_right(self):
        self.section(3, "直角：用三角尺比一比")

        v = [-4.2, -1.4]
        h = ray(v, 0, 3.5, color=GOLD)
        u = ray(v, 90, 3.5, color=BLUE)
        mark = right_mark(v, 0.36, color=CHALK)
        dot = Dot([v[0], v[1], 0], radius=0.09, color=CHALK)
        self.play(Create(h), Create(u), FadeIn(dot), run_time=0.9)
        self.play(Create(mark), run_time=0.5)

        r = ruler(v, leg=2.5)
        r.shift([6.2, 0, 0])
        r_lab = txt("三角尺", size=26, color=BLUE).move_to([5.0, 1.6, 0])
        self.play(FadeIn(r), FadeIn(r_lab), run_time=0.8)
        self.play(r.animate.shift([-6.2, 0, 0]), FadeOut(r_lab), run_time=1.3)

        same = txt("正好重合 → 直角", size=32, color=GREEN).move_to([2.9, 0.7, 0])
        self.play(FadeIn(same, shift=UP * 0.08), run_time=0.7)

        note = txt("书本、桌子、窗户的角，都是直角", size=27, color=DIM).move_to([2.9, -0.2, 0])
        self.play(FadeIn(note), run_time=0.6)
        self.finish_section()

    # ---------------- 4. 锐角与钝角 ----------------
    def scene_kinds(self):
        self.section(4, "锐角、直角、钝角")

        specs = [
            (-4.4, 50, "锐角", "比直角小", GREEN),
            (0.0, 90, "直角", "和三角尺一样", GOLD),
            (4.4, 135, "钝角", "比直角大", RED),
        ]
        for x, deg, name, desc, color in specs:
            v = [x - 1.0, -1.2]
            r1 = ray(v, 0, 2.0, color=CHALK)
            r2 = ray(v, deg, 2.0, color=CHALK)
            ar = arc(v, 0, deg, 0.55, color=color)
            self.play(Create(r1), Create(r2), Create(ar), run_time=0.55)
            lab = txt(name, size=36, color=color).move_to([x - 1.0, 0.95, 0])
            self.play(FadeIn(lab, shift=DOWN * 0.06), run_time=0.35)
            if deg == 90:
                self.play(Create(right_mark(v, 0.3, color=CHALK)), run_time=0.35)
            else:
                self.play(FadeIn(txt(desc, size=23, color=DIM).move_to([x - 1.0, 0.35, 0])),
                          run_time=0.3)

        tip = txt("三角尺上：1 个直角，2 个锐角", size=28, color=GREEN).move_to([0, -2.3, 0])
        self.play(FadeIn(tip, shift=UP * 0.08), run_time=0.7)
        self.finish_section()

    # ---------------- 5. 判断三步 ----------------
    def scene_judge(self):
        self.section(5, "判断三步：对齐、重合、看里面")

        steps = VGroup(
            label_box("① 顶点对齐", size=26, color=CHALK),
            label_box("② 一条边重合", size=26, color=CHALK),
            label_box("③ 看另一边", size=26, color=GOLD),
        ).arrange(RIGHT, buff=0.45).move_to([0, 2.35, 0])
        self.play(LaggedStart(*[FadeIn(s, shift=UP * 0.06) for s in steps], lag_ratio=0.2),
                  run_time=0.9)

        # 左：锐角
        v1 = [-4.3, -1.0]
        a1 = ray(v1, 0, 3.0, color=CHALK)
        a2 = ray(v1, 55, 3.0, color=CHALK)
        self.play(Create(a1), Create(a2), run_time=0.7)
        r1 = corner_gauge(v1, leg=1.9, color=BLUE)
        self.play(FadeIn(r1), run_time=0.5)
        res1 = txt("在直角里面 → 锐角", size=27, color=GREEN).move_to([-4.3, -2.2, 0])
        self.play(FadeIn(res1, shift=UP * 0.08), run_time=0.6)

        # 右：钝角
        v2 = [3.2, -1.0]
        b1 = ray(v2, 0, 3.0, color=CHALK)
        b2 = ray(v2, 128, 3.0, color=CHALK)
        self.play(Create(b1), Create(b2), run_time=0.7)
        r2 = corner_gauge(v2, leg=1.9, color=ORANGE)
        self.play(FadeIn(r2), run_time=0.5)
        res2 = txt("在直角外面 → 钝角", size=27, color=RED).move_to([3.2, -2.2, 0])
        self.play(FadeIn(res2, shift=UP * 0.08), run_time=0.6)
        self.finish_section()

    # ---------------- 6. 收束 ----------------
    def scene_summary(self):
        self.section(6, "记住这三句话")

        big = txt("一个顶点，两条边", size=52, color=GOLD).move_to([0, 1.7, 0])
        self.play(Write(big), run_time=1.0)

        b1 = label_box("角的大小看张口", size=32, color=CHALK).move_to([-3.6, 0.35, 0])
        b2 = label_box("边变长，角不变", size=32, color=CHALK).move_to([3.6, 0.35, 0])
        self.play(FadeIn(b1, shift=UP * 0.08), run_time=0.6)
        self.play(FadeIn(b2, shift=UP * 0.08), run_time=0.6)

        kinds = VGroup(
            txt("锐角", size=34, color=GREEN),
            txt("＜", size=30, color=DIM),
            txt("直角", size=34, color=GOLD),
            txt("＜", size=30, color=DIM),
            txt("钝角", size=34, color=RED),
        ).arrange(RIGHT, buff=0.3).move_to([0, -1.0, 0])
        self.play(FadeIn(kinds, shift=UP * 0.08), run_time=0.8)

        tip = txt("拿不准，就用三角尺的直角去比", size=28, color=DIM).move_to([0, -2.05, 0])
        self.play(FadeIn(tip), run_time=0.6)
        self.finish_section()

    def construct(self):
        self.scene_life()
        self.clear_stage()
        self.scene_parts()
        self.clear_stage()
        self.scene_size()
        self.clear_stage()
        self.scene_right()
        self.clear_stage()
        self.scene_kinds()
        self.clear_stage()
        self.scene_judge()
        self.clear_stage()
        self.scene_summary()
        self.clear_stage(0.8)