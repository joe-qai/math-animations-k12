# -*- coding: utf-8 -*-
"""视图与投影：影子怎么来，三张图怎么画。八年级下。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


def P(x, y):
    return np.array([float(x), float(y), 0.0])


def rect(x0, y0, w, h, color=CHALK, width=2.6, fill=0.06) -> Rectangle:
    return Rectangle(width=w, height=h, color=color, stroke_width=width,
                     fill_color=color, fill_opacity=fill).move_to([x0 + w / 2, y0 + h / 2, 0])


def circ(cx, cy, r, color=CHALK, width=2.6, fill=0.06) -> Circle:
    return Circle(radius=r, color=color, stroke_width=width,
                  fill_color=color, fill_opacity=fill).move_to([cx, cy, 0])


def iso_tri(cx, base_y, w, h, color=CHALK, width=2.6) -> Polygon:
    return Polygon(P(cx - w / 2, base_y), P(cx + w / 2, base_y), P(cx, base_y + h),
                   color=color, stroke_width=width,
                   fill_color=color, fill_opacity=0.06)


def cube3(cx, cy, s, dx, dy, color=CHALK, width=2.4) -> VGroup:
    """简易立体正方体：正面正方形 + 背面平移 + 连线。"""
    front = Rectangle(width=s, height=s, color=color, stroke_width=width,
                      fill_color=color, fill_opacity=0.06)
    front.move_to([cx, cy, 0])
    back = front.copy().shift([dx, dy, 0])
    lines = VGroup(*[
        Line(front.get_corner(c), back.get_corner(c), color=color, stroke_width=width)
        for c in (UL, UR, DL, DR)
    ])
    return VGroup(back, lines, front)


class ShituTouyingScene(NarratedScene):
    lesson = "shitu-touying"

    def clear_stage(self, run_time: float = 0.5):
        keep = {id(self._track), id(self._fill)}
        junk = [m for m in self.mobjects if id(m) not in keep]
        if junk:
            self.play(*[FadeOut(m) for m in junk], run_time=run_time)
        self.cur_title = None
        self.cur_sub = None

    # ---------------- 0. 影子和图纸 ---------------- 23.6
    def scene_intro(self):
        self.section(0, "影子是投影，图纸是三视图")

        chips = [
            ("太阳下的影子", "光被挡住", -4.2, GOLD),
            ("台灯的手影", "光从一个点散开", 0.0, GREEN),
            ("三张设计图", "正面、左面、上面", 4.2, BLUE),
        ]
        for name, note, cx, col in chips:
            t = label_box(name, size=23, color=col).move_to([cx, 2.25, 0])
            self.play(FadeIn(t, scale=0.97), run_time=0.75)
            n = txt(note, size=21, color=DIM).move_to([cx, 1.55, 0])
            self.play(FadeIn(n, shift=UP * 0.04), run_time=0.7)
        self.wait(1.1)

        l1 = txt("投影：物体挡住光线，在平面上留下影子", size=27, color=CHALK)
        l1.move_to([0, 0.45, 0])
        self.play(FadeIn(l1, shift=UP * 0.05), run_time=0.95)
        l2 = txt("三视图：从三个方向看，画出三张图", size=27, color=CHALK)
        l2.move_to([0, -0.5, 0])
        self.play(FadeIn(l2, shift=UP * 0.04), run_time=0.95)
        self.wait(1.1)

        box = label_box("影子是投影，图纸是三视图", size=26, color=GOLD)
        box.move_to([0, -2.35, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.1)
        self.wait(9.5)
        self.finish_section()

    # ---------------- 1. 平行投影与中心投影 ---------------- 31.3
    def scene_types(self):
        self.section(1, "投影分两类")

        # 左：平行投影
        t1 = txt("平行投影", size=26, color=GOLD).move_to([-3.7, 2.65, 0])
        c1 = txt("光线互相平行", size=21, color=DIM).move_to([-3.7, 2.1, 0])
        self.play(FadeIn(t1, shift=UP * 0.04), FadeIn(c1, shift=UP * 0.04), run_time=0.95)

        ground1 = Line(P(-6.9, -1.9), P(-0.55, -1.9), color=DIM, stroke_width=2.2)
        self.play(Create(ground1), run_time=0.8)

        obj1 = Line(P(-4.85, -1.9), P(-4.85, 0.05), color=BLUE, stroke_width=7)
        self.play(Create(obj1), run_time=0.8)

        shadow1 = Line(P(-4.85, -1.9), P(-2.95, -1.9), color=GOLD, stroke_width=9)
        self.play(Create(shadow1), run_time=0.9)

        rays = VGroup(*[
            Arrow(P(x, 1.85), P(x + 1.32, 0.53), color=GOLD, stroke_width=2.2,
                  buff=0, max_tip_length_to_length_ratio=0.16)
            for x in (-6.4, -5.9, -5.4)
        ])
        self.play(LaggedStart(*[GrowArrow(a) for a in rays], lag_ratio=0.15), run_time=1.5)

        dash1 = DashedLine(P(-4.85, 0.05), P(-2.95, -1.9), color=GOLD,
                           stroke_width=2.0, dash_length=0.12)
        self.play(Create(dash1), run_time=1.0)
        self.wait(1.0)

        # 右：中心投影
        t2 = txt("中心投影", size=26, color=GREEN).move_to([3.3, 2.65, 0])
        c2 = txt("光线交于一点", size=21, color=DIM).move_to([3.3, 2.1, 0])
        self.play(FadeIn(t2, shift=UP * 0.04), FadeIn(c2, shift=UP * 0.04), run_time=0.95)

        ground2 = Line(P(0.55, -1.9), P(6.9, -1.9), color=DIM, stroke_width=2.2)
        self.play(Create(ground2), run_time=0.8)

        bulb = Dot(P(3.9, 1.6), radius=0.13, color=GOLD)
        halo = Circle(radius=0.28, color=GOLD, stroke_width=1.6).move_to(P(3.9, 1.6))
        self.play(FadeIn(bulb), Create(halo), run_time=0.9)

        obj2 = Line(P(2.2, -1.9), P(2.2, -0.1), color=BLUE, stroke_width=7)
        self.play(Create(obj2), run_time=0.8)

        shadow2 = Line(P(0.4, -1.9), P(2.2, -1.9), color=GOLD, stroke_width=9)
        self.play(Create(shadow2), run_time=0.9)

        r1 = Line(P(3.9, 1.6), P(2.2, -0.1), color=GOLD, stroke_width=2.0)
        r2 = Line(P(3.9, 1.6), P(2.2, -1.9), color=GOLD, stroke_width=2.0)
        r3 = DashedLine(P(2.2, -0.1), P(0.4, -1.9), color=GOLD,
                        stroke_width=2.0, dash_length=0.12)
        self.play(Create(r1), Create(r2), run_time=1.2)
        self.play(Create(r3), run_time=0.9)
        self.wait(1.0)

        box = label_box("正投影：光线垂直射到投影面上", size=25, color=BLUE)
        box.move_to([0, -2.6, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.1)
        self.wait(12.5)
        self.finish_section()

    # ---------------- 2. 三个方向与三条关系 ---------------- 29.4
    def scene_views(self):
        self.section(2, "三个方向，三张图")

        # 三个视图框
        main = rect(-4.6, 0.75, 2.4, 1.4, CHALK)
        left = rect(0.2, 0.75, 2.4, 1.4, CHALK)
        top = rect(-4.6, -2.05, 2.4, 1.0, CHALK)
        self.play(Create(main), run_time=0.9)
        self.play(Create(left), run_time=0.9)
        self.play(Create(top), run_time=0.9)

        lm = txt("主视图", size=23, color=GOLD).move_to([-3.4, 2.5, 0])
        ll = txt("左视图", size=23, color=GREEN).move_to([1.4, 2.5, 0])
        lt = txt("俯视图", size=23, color=BLUE).move_to([-1.35, -1.55, 0])
        self.play(FadeIn(lm, shift=UP * 0.04), run_time=0.6)
        self.play(FadeIn(ll, shift=UP * 0.04), run_time=0.6)
        self.play(FadeIn(lt, shift=UP * 0.04), run_time=0.6)
        self.wait(1.0)

        # 三条对应关系
        v1 = DashedLine(P(-4.6, 0.62), P(-4.6, -1.02), color=GOLD, stroke_width=1.6, dash_length=0.1)
        v2 = DashedLine(P(-2.2, 0.62), P(-2.2, -1.02), color=GOLD, stroke_width=1.6, dash_length=0.1)
        h1 = DashedLine(P(-2.08, 2.15), P(0.08, 2.15), color=GREEN, stroke_width=1.6, dash_length=0.1)
        h2 = DashedLine(P(-2.08, 0.75), P(0.08, 0.75), color=GREEN, stroke_width=1.6, dash_length=0.1)
        self.play(LaggedStart(*[Create(x) for x in (v1, v2, h1, h2)], lag_ratio=0.15), run_time=1.8)

        w1 = txt("长对正", size=21, color=GOLD).move_to([-3.4, -0.25, 0])
        w2 = txt("高平齐", size=21, color=GREEN).move_to([-1.0, 1.52, 0])
        w3 = txt("宽相等", size=21, color=BLUE).move_to([2.55, 0.15, 0])
        self.play(FadeIn(w1, scale=0.9), run_time=0.7)
        self.play(FadeIn(w2, scale=0.9), run_time=0.7)
        self.play(FadeIn(w3, scale=0.9), run_time=0.7)
        self.wait(1.2)

        rows = [
            ("正面 → 主视图", GOLD),
            ("左面 → 左视图", GREEN),
            ("上面 → 俯视图", BLUE),
        ]
        y = 1.5
        for s, col in rows:
            t = txt(s, size=22, color=col).move_to([4.9, y, 0])
            self.play(FadeIn(t, shift=RIGHT * 0.04), run_time=0.75)
            y -= 0.72
        self.wait(1.2)

        f = label_box("长对正　高平齐　宽相等", size=26, color=GOLD)
        f.move_to([0, -2.72, 0])
        self.play(FadeIn(f, scale=0.97), run_time=1.1)
        self.wait(10.5)
        self.finish_section()

    # ---------------- 3. 常见几何体的三视图 ---------------- 32.0
    def scene_table(self):
        self.section(3, "常见几何体的三视图")

        heads = [("几何体", -6.0), ("主视图", -3.55), ("左视图", 0.25), ("俯视图", 3.95)]
        for s, x in heads:
            t = txt(s, size=22, color=DIM).move_to([x, 2.55, 0])
            self.play(FadeIn(t, shift=UP * 0.04), run_time=0.45)
        self.wait(0.8)

        rows = [
            ("圆柱", 1.85, "cyl"),
            ("圆锥", 0.95, "cone"),
            ("球", 0.05, "ball"),
            ("正方体", -0.85, "cube"),
            ("三棱柱", -1.75, "prism"),
        ]
        u = 0.62
        for name, y, kind in rows:
            ln = txt(name, size=22, color=CHALK).move_to([-6.0, y, 0])
            if kind == "cyl":
                a = rect(-3.86, y - u / 2, u, u, CHALK, 2.2)
                b = rect(-0.06, y - u / 2, u, u, CHALK, 2.2)
                c = circ(3.95, y, u / 2, CHALK, 2.2)
            elif kind == "cone":
                a = iso_tri(-3.55, y - u / 2, u, u, CHALK, 2.2)
                b = iso_tri(0.25, y - u / 2, u, u, CHALK, 2.2)
                c = VGroup(circ(3.95, y, u / 2, CHALK, 2.2),
                           Dot(P(3.95, y), radius=0.05, color=CHALK))
            elif kind == "ball":
                a = circ(-3.55, y, u / 2, CHALK, 2.2)
                b = circ(0.25, y, u / 2, CHALK, 2.2)
                c = circ(3.95, y, u / 2, CHALK, 2.2)
            elif kind == "cube":
                a = rect(-3.86, y - u / 2, u, u, CHALK, 2.2)
                b = rect(-0.06, y - u / 2, u, u, CHALK, 2.2)
                c = rect(3.64, y - u / 2, u, u, CHALK, 2.2)
            else:
                a = rect(-3.86, y - u / 2, u, u, CHALK, 2.2)
                b = rect(-0.06, y - u / 2, u, u, CHALK, 2.2)
                c = iso_tri(3.95, y - u / 2, u * 1.1, u * 0.92, CHALK, 2.2)
            self.play(FadeIn(ln, shift=RIGHT * 0.04), run_time=0.4)
            self.play(Create(a), run_time=0.55)
            self.play(Create(b), run_time=0.55)
            self.play(Create(c), run_time=0.55)
            self.wait(0.25)
        self.wait(1.2)

        note = txt("主视图、左视图看「轮廓」，俯视图看「底面」", size=23, color=GOLD)
        note.move_to([0, -2.85, 0])
        self.play(FadeIn(note, shift=UP * 0.04), run_time=1.0)
        self.wait(9.5)
        self.finish_section()

    # ---------------- 4. 由三视图还原 ---------------- 28.3
    def scene_reverse(self):
        self.section(4, "由三视图还原几何体")

        head = txt("三视图　→　几何体", size=25, color=DIM).move_to([-1.2, 2.45, 0])
        self.play(FadeIn(head, shift=UP * 0.04), run_time=0.9)
        self.wait(0.8)

        s = 0.72
        rows = [
            ("圆柱", 1.35, "cyl"),
            ("圆锥", 0.0, "cone"),
            ("正方体", -1.35, "cube"),
        ]
        for name, y, kind in rows:
            if kind == "cyl":
                a = rect(-5.42, y - s / 2, s * 0.9, s, CHALK, 2.2)
                b = rect(-4.40, y - s / 2, s * 0.9, s, CHALK, 2.2)
                c = circ(-3.08, y, s * 0.45, CHALK, 2.2)
            elif kind == "cone":
                a = iso_tri(-4.97, y - s / 2, s * 0.9, s, CHALK, 2.2)
                b = iso_tri(-3.95, y - s / 2, s * 0.9, s, CHALK, 2.2)
                c = VGroup(circ(-2.63, y, s * 0.45, CHALK, 2.2),
                           Dot(P(-2.63, y), radius=0.05, color=CHALK))
            else:
                a = rect(-5.42, y - s / 2, s * 0.9, s, CHALK, 2.2)
                b = rect(-4.40, y - s / 2, s * 0.9, s, CHALK, 2.2)
                c = rect(-3.38, y - s / 2, s * 0.9, s, CHALK, 2.2)
            self.play(Create(a), Create(b), Create(c), run_time=1.1)
            ar = Arrow(P(-2.25, y), P(-0.85, y), color=GOLD, stroke_width=2.6,
                       buff=0, max_tip_length_to_length_ratio=0.2)
            self.play(GrowArrow(ar), run_time=0.6)
            nm = txt(name, size=28, color=GOLD).move_to([0.55, y, 0])
            self.play(FadeIn(nm, shift=RIGHT * 0.05), run_time=0.7)
            self.wait(0.35)
        self.wait(1.2)

        note = txt("俯视图看底面形状，主视图看高度", size=24, color=GREEN)
        note.move_to([1.45, -2.35, 0])
        self.play(FadeIn(note, shift=UP * 0.04), run_time=1.0)
        self.wait(11.0)
        self.finish_section()

    # ---------------- 5. 例题：俯视图标数字 ---------------- 31.9
    def scene_example(self):
        self.section(5, "例题：俯视图上标数字")

        head = txt("每个数字 = 这一列有几层", size=24, color=DIM).move_to([-4.7, 2.25, 0])
        self.play(FadeIn(head, shift=UP * 0.04), run_time=0.9)

        # 俯视图 3×3 网格
        side = 0.62
        x0, y0 = -5.86, -0.72
        cells = VGroup()
        for r in range(3):
            for c in range(3):
                cells.add(Rectangle(width=side, height=side, color=DIM,
                                    stroke_width=1.8,
                                    fill_color=CHALK, fill_opacity=0.03)
                          .move_to([x0 + side / 2 + c * side, y0 + side / 2 + r * side, 0]))
        self.play(LaggedStart(*[Create(c) for c in cells], lag_ratio=0.04), run_time=1.3)
        lab = txt("俯视图", size=22, color=BLUE).move_to([-4.93, 1.28, 0])
        self.play(FadeIn(lab), run_time=0.5)
        self.wait(0.4)

        n2 = txt("2", size=26, color=GOLD).move_to([x0 + side / 2, y0 + side * 2.5, 0])
        n1a = txt("1", size=26, color=GOLD).move_to([x0 + side * 1.5, y0 + side * 1.5, 0])
        n1b = txt("1", size=26, color=GOLD).move_to([x0 + side * 2.5, y0 + side * 0.5, 0])
        n1c = txt("1", size=26, color=GOLD).move_to([x0 + side * 2.5, y0 + side * 2.5, 0])
        self.play(FadeIn(n2, scale=0.9), run_time=0.6)
        self.play(FadeIn(n1a, scale=0.9), FadeIn(n1b, scale=0.9), run_time=0.7)
        self.play(FadeIn(n1c, scale=0.9), run_time=0.6)
        self.wait(0.8)

        total = txt("总数 = 2 + 1 + 1 + 1 = 5", size=28, color=GOLD)
        total.move_to([-4.7, -1.75, 0])
        self.play(FadeIn(total, scale=0.97), run_time=1.0)
        self.wait(0.9)

        # 主视图与左视图
        u = 0.48
        main_heights = [2, 1, 1]
        left_heights = [2, 1, 1]
        base_y = -0.95

        def stack(x_start, heights, color):
            g = VGroup()
            for i, h in enumerate(heights):
                for k in range(h):
                    g.add(Rectangle(width=u, height=u, color=color, stroke_width=1.8,
                                    fill_color=color, fill_opacity=0.08)
                          .move_to([x_start + u / 2 + i * u, base_y + u / 2 + k * u, 0]))
            return g

        vm = stack(0.45, main_heights, GOLD)
        vl = stack(3.35, left_heights, GREEN)
        self.play(Create(vm), run_time=1.2)
        self.play(Create(vl), run_time=1.2)

        lm = txt("主视图", size=22, color=GOLD).move_to([1.17, 0.45, 0])
        ll = txt("左视图", size=22, color=GREEN).move_to([4.07, 0.45, 0])
        self.play(FadeIn(lm), FadeIn(ll), run_time=0.8)
        self.wait(1.0)

        tip = txt("主视图三列高 2、1、1，左视图三列也高 2、1、1", size=21, color=DIM)
        tip.move_to([2.6, -2.35, 0])
        self.play(FadeIn(tip, shift=UP * 0.04), run_time=0.95)
        self.wait(9.0)
        self.finish_section()

    # ---------------- 6. 三个易错点 ---------------- 27.3
    def scene_traps(self):
        self.section(6, "三个易错点")

        rows = [
            ("① 三个视图的位置与对应", "长对正、高平齐、宽相等"),
            ("② 看不见的轮廓线", "要画虚线，不能漏"),
            ("③ 中心投影与平行投影", "灯泡和太阳，别混"),
        ]
        y = 1.65
        for a, b in rows:
            ta = txt(a, size=23, color=RED).move_to([-3.0, y, 0])
            self.play(FadeIn(ta, shift=RIGHT * 0.04), run_time=0.7)
            tb = txt(b, size=22, color=DIM).move_to([3.55, y, 0])
            self.play(FadeIn(tb, shift=RIGHT * 0.04), run_time=0.7)
            y -= 0.95
        self.wait(1.1)

        note = txt("主视图看长和高，俯视图看长和宽，左视图看宽和高",
                   size=22, color=CHALK)
        note.move_to([0, -1.35, 0])
        self.play(FadeIn(note, shift=UP * 0.04), run_time=1.0)
        self.wait(0.9)

        box = label_box("长对正，高平齐，宽相等", size=28, color=GOLD)
        box.move_to([0, -2.45, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.1)
        self.wait(11.5)
        self.finish_section()

    def construct(self):
        self.scene_intro()
        self.clear_stage()
        self.scene_types()
        self.clear_stage()
        self.scene_views()
        self.clear_stage()
        self.scene_table()
        self.clear_stage()
        self.scene_reverse()
        self.clear_stage()
        self.scene_example()
        self.clear_stage()
        self.scene_traps()
        self.clear_stage(0.8)