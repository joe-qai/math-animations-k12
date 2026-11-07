# -*- coding: utf-8 -*-
"""特殊平行四边形：矩形、菱形、正方形。八年级下。"""

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


def P(x, y):
    return np.array([float(x), float(y), 0.0])


def quad(A, B, C, D, color=CHALK, width=3.0, fill=0.06) -> Polygon:
    return Polygon(P(*A), P(*B), P(*C), P(*D),
                   color=color, stroke_width=width,
                   fill_color=color, fill_opacity=fill)


def rect(x0, y0, w, h, color=CHALK, width=3.0) -> Polygon:
    return quad((x0, y0), (x0 + w, y0), (x0 + w, y0 + h), (x0, y0 + h),
                color=color, width=width)


def vlabel(ch, pos, color=CHALK, size=26) -> Text:
    t = txt(ch, size=size, color=color)
    t.move_to(P(*pos))
    return t


def corner_mark(corner, d1, d2, size=0.26, color=GOLD, width=2.2) -> VGroup:
    """在顶点处画直角小方框。d1、d2 是从顶点指向角内部的两个单位方向。"""
    p0 = np.array([float(corner[0]), float(corner[1]), 0.0])
    v1 = np.array([float(d1[0]), float(d1[1]), 0.0]) * size
    v2 = np.array([float(d2[0]), float(d2[1]), 0.0]) * size
    return VGroup(
        Line(p0 + v1, p0 + v1 + v2, color=color, stroke_width=width),
        Line(p0 + v1 + v2, p0 + v2, color=color, stroke_width=width),
    )


class TeshuPingxingSibianxingScene(NarratedScene):
    lesson = "teshu_pingxing_sibianxing"

    def clear_stage(self, run_time: float = 0.5):
        keep = {id(self._track), id(self._fill)}
        junk = [m for m in self.mobjects if id(m) not in keep]
        if junk:
            self.play(*[FadeOut(m) for m in junk], run_time=run_time)
        self.cur_title = None
        self.cur_sub = None

    # ---------------- 0. 加一个条件 ---------------- 30.0
    def scene_intro(self):
        self.section(0, "加一个条件，就变特殊")

        head = txt("平行四边形　+　一个条件", size=27, color=CHALK).move_to([0, 2.72, 0])
        self.play(FadeIn(head, shift=UP * 0.05), run_time=0.95)
        self.wait(1.0)

        # 三个小图形
        r = rect(-5.3, 0.1, 2.1, 1.35, GOLD)
        rl = txt("矩形", size=25, color=GOLD).move_to([-4.25, 1.85, 0])
        self.play(Create(r), FadeIn(rl, shift=UP * 0.04), run_time=1.0)

        m1 = quad((-1.5, 0.8), (-0.55, 1.45), (0.4, 0.8), (-0.55, 0.15), GREEN)
        ml = txt("菱形", size=25, color=GREEN).move_to([-0.55, 1.85, 0])
        self.play(Create(m1), FadeIn(ml, shift=UP * 0.04), run_time=1.0)

        s1 = rect(2.9, 0.05, 1.5, 1.5, BLUE)
        sl = txt("正方形", size=25, color=BLUE).move_to([3.65, 1.85, 0])
        self.play(Create(s1), FadeIn(sl, shift=UP * 0.04), run_time=1.0)
        self.wait(1.0)

        c1 = txt("加一个直角", size=23, color=DIM).move_to([-4.25, -0.45, 0])
        c2 = txt("加一组邻边相等", size=23, color=DIM).move_to([-0.55, -0.45, 0])
        c3 = txt("两个都加", size=23, color=DIM).move_to([3.65, -0.45, 0])
        self.play(LaggedStart(*[FadeIn(c, shift=UP * 0.04) for c in (c1, c2, c3)],
                              lag_ratio=0.15), run_time=1.5)
        self.wait(1.2)

        note = txt("矩形、菱形、正方形，都是特殊的平行四边形", size=26, color=CHALK)
        note.move_to([0, -1.35, 0])
        self.play(FadeIn(note, shift=UP * 0.04), run_time=0.95)
        self.wait(1.0)

        box = label_box("加了条件，性质就变多", size=27, color=GOLD)
        box.move_to([0, -2.25, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.1)
        self.wait(6.0)
        self.finish_section()

    # ---------------- 1. 矩形的性质 ---------------- 25.1
    def scene_rect_props(self):
        self.section(1, "矩形：四个直角，对角线相等")

        A, B, C, D = (-5.2, -1.45), (-0.8, -1.45), (-0.8, 1.25), (-5.2, 1.25)
        shape = quad(A, B, C, D, CHALK)
        self.play(Create(shape), run_time=1.0)

        marks = [
            corner_mark(A, (1, 0), (0, 1)),
            corner_mark(B, (-1, 0), (0, 1)),
            corner_mark(C, (-1, 0), (0, -1)),
            corner_mark(D, (1, 0), (0, -1)),
        ]
        self.play(LaggedStart(*[Create(m) for m in marks], lag_ratio=0.15), run_time=1.6)
        self.wait(1.0)

        O = (-3.0, -0.1)
        d1 = Line(P(*A), P(*C), color=GOLD, stroke_width=2.4)
        d2 = Line(P(*B), P(*D), color=GOLD, stroke_width=2.4)
        dot = Dot(P(*O), radius=0.07, color=GOLD)
        self.play(Create(d1), Create(d2), FadeIn(dot), run_time=1.5)

        ol = txt("O", size=21, color=GOLD).move_to([O[0] + 0.26, O[1] - 0.34, 0])
        self.play(FadeIn(ol), run_time=0.5)
        self.wait(1.0)

        rows = [
            ("① 四个角都是直角", CHALK),
            ("② 对角线相等", GOLD),
            ("③ 对角线互相平分", GOLD),
        ]
        y = 1.7
        for s, col in rows:
            t = txt(s, size=24, color=col).move_to([3.15, y, 0])
            self.play(FadeIn(t, shift=RIGHT * 0.04), run_time=0.8)
            y -= 0.85
        self.wait(1.0)

        note = txt("直角三角形斜边上的中线，等于斜边的一半", size=23, color=GREEN)
        note.move_to([0, -2.3, 0])
        self.play(FadeIn(note, shift=UP * 0.04), run_time=1.0)
        self.wait(4.2)
        self.finish_section()

    # ---------------- 2. 矩形的判定 ---------------- 25.3
    def scene_rect_rules(self):
        self.section(2, "矩形怎么判定")

        small = rect(3.5, 0.0, 2.2, 1.4, CHALK, width=2.4)
        self.play(Create(small), run_time=0.95)
        sm = corner_mark((3.5, 0.0), (1, 0), (0, 1), color=GOLD)
        self.play(Create(sm), run_time=0.7)
        slot = txt("一个直角", size=22, color=DIM).move_to([4.6, -0.55, 0])
        self.play(FadeIn(slot, shift=UP * 0.04), run_time=0.7)
        self.wait(0.8)

        rows = [
            ("①", "有一个角是直角的平行四边形"),
            ("②", "对角线相等的平行四边形"),
            ("③", "有三个角是直角的四边形"),
        ]
        y = 2.0
        for num, s in rows:
            n = txt(num, size=23, color=GOLD).move_to([-5.9, y, 0])
            t = txt(s, size=24, color=CHALK)
            t.next_to(n, RIGHT, buff=0.3)
            t.move_to([t.get_center()[0], n.get_center()[1], 0])
            self.play(FadeIn(n, shift=RIGHT * 0.05), run_time=0.4)
            self.play(FadeIn(t, shift=RIGHT * 0.04), run_time=0.6)
            y -= 0.9
        self.wait(1.2)

        warn = label_box("前提不同，别混用", size=26, color=RED)
        warn.move_to([-2.9, -1.55, 0])
        self.play(FadeIn(warn, scale=0.97), run_time=1.0)

        tip = txt("先看已知是边、角，还是对角线", size=23, color=DIM)
        tip.move_to([-2.9, -2.3, 0])
        self.play(FadeIn(tip, shift=UP * 0.04), run_time=0.95)
        self.wait(5.0)
        self.finish_section()

    # ---------------- 3. 菱形的性质 ---------------- 23.4
    def scene_rhombus_props(self):
        self.section(3, "菱形：四条边相等，对角线垂直")

        A, B, C, D = (-5.1, 0), (-2.4, 1.5), (0.3, 0), (-2.4, -1.5)
        shape = quad(A, B, C, D, CHALK)
        self.play(Create(shape), run_time=1.0)
        self.wait(0.6)

        sides = [
            Line(P(*A), P(*B), color=GREEN, stroke_width=5),
            Line(P(*B), P(*C), color=GREEN, stroke_width=5),
            Line(P(*C), P(*D), color=GREEN, stroke_width=5),
            Line(P(*D), P(*A), color=GREEN, stroke_width=5),
        ]
        self.play(LaggedStart(*[Create(s) for s in sides], lag_ratio=0.2), run_time=1.8)
        self.wait(0.9)

        d1 = Line(P(*A), P(*C), color=GOLD, stroke_width=2.4)
        d2 = Line(P(*B), P(*D), color=GOLD, stroke_width=2.4)
        dot = Dot(P(-2.4, 0), radius=0.07, color=GOLD)
        self.play(Create(d1), Create(d2), FadeIn(dot), run_time=1.5)
        rm = corner_mark((-2.4, 0), (1, 0), (0, 1), size=0.3, color=GOLD)
        self.play(Create(rm), run_time=0.7)
        self.wait(1.0)

        rows = [
            ("① 四条边都相等", GREEN),
            ("② 对角线互相垂直", GOLD),
            ("③ 每条对角线平分一组对角", GOLD),
            ("④ 面积 = 对角线乘积的一半", CHALK),
        ]
        y = 1.95
        for s, col in rows:
            t = txt(s, size=23, color=col).move_to([3.75, y, 0])
            self.play(FadeIn(t, shift=RIGHT * 0.04), run_time=0.75)
            y -= 0.82
        self.wait(1.0)

        f = txt("S = 对角线乘积的一半", size=29, color=GOLD).move_to([0, -2.35, 0])
        self.play(FadeIn(f, scale=0.97), run_time=1.0)
        self.wait(3.6)
        self.finish_section()

    # ---------------- 4. 菱形的判定 ---------------- 20.5
    def scene_rhombus_rules(self):
        self.section(4, "菱形怎么判定")

        rows = [
            ("①", "有一组邻边相等的平行四边形"),
            ("②", "对角线互相垂直的平行四边形"),
            ("③", "四条边都相等的四边形"),
        ]
        y = 1.9
        for num, s in rows:
            n = txt(num, size=23, color=GOLD).move_to([-5.9, y, 0])
            t = txt(s, size=24, color=CHALK)
            t.next_to(n, RIGHT, buff=0.3)
            t.move_to([t.get_center()[0], n.get_center()[1], 0])
            self.play(FadeIn(n, shift=RIGHT * 0.05), run_time=0.4)
            self.play(FadeIn(t, shift=RIGHT * 0.04), run_time=0.6)
            y -= 0.9
        self.wait(1.2)

        small = quad((2.4, -1.1), (3.9, -0.35), (2.4, 0.4), (0.9, -0.35), GREEN, width=2.4)
        self.play(Create(small), run_time=1.0)
        self.wait(1.0)

        tip = txt("还是先分清已知条件：边、角，还是对角线", size=23, color=DIM)
        tip.move_to([0, -2.15, 0])
        self.play(FadeIn(tip, shift=UP * 0.04), run_time=1.0)
        self.wait(4.4)
        self.finish_section()

    # ---------------- 5. 正方形 ---------------- 30.0
    def scene_square(self):
        self.section(5, "正方形：矩形与菱形的合体")

        A, B, C, D = (-5.25, -1.15), (-2.65, -1.15), (-2.65, 1.45), (-5.25, 1.45)
        shape = quad(A, B, C, D, BLUE)
        self.play(Create(shape), run_time=1.0)

        marks = [
            corner_mark(A, (1, 0), (0, 1), color=BLUE),
            corner_mark(B, (-1, 0), (0, 1), color=BLUE),
            corner_mark(C, (-1, 0), (0, -1), color=BLUE),
            corner_mark(D, (1, 0), (0, -1), color=BLUE),
        ]
        self.play(LaggedStart(*[Create(m) for m in marks], lag_ratio=0.15), run_time=1.6)

        d1 = Line(P(*A), P(*C), color=GOLD, stroke_width=2.2)
        d2 = Line(P(*B), P(*D), color=GOLD, stroke_width=2.2)
        self.play(Create(d1), Create(d2), run_time=1.3)
        rm = corner_mark((-3.95, 0.15), (1, 0), (0, 1), size=0.28, color=GOLD)
        self.play(Create(rm), run_time=0.7)
        self.wait(1.0)

        rows = [
            ("四个角都是直角", BLUE),
            ("四条边都相等", GREEN),
            ("对角线相等、垂直、互相平分", GOLD),
            ("每条对角线平分一组对角", GOLD),
        ]
        y = 2.15
        for s, col in rows:
            t = txt(s, size=23, color=col).move_to([3.0, y, 0])
            self.play(FadeIn(t, shift=RIGHT * 0.04), run_time=0.75)
            y -= 0.72
        self.wait(1.0)

        n1 = txt("判定：先证矩形，再证一组邻边相等", size=23, color=CHALK)
        n1.move_to([3.0, -0.95, 0])
        self.play(FadeIn(n1, shift=UP * 0.04), run_time=0.9)
        n2 = txt("或者：先证菱形，再证一个角是直角", size=23, color=CHALK)
        n2.move_to([3.0, -1.68, 0])
        self.play(FadeIn(n2, shift=UP * 0.04), run_time=0.9)
        self.wait(1.0)

        note = txt("既是矩形，又是菱形", size=25, color=GOLD).move_to([0, -2.35, 0])
        self.play(FadeIn(note, shift=UP * 0.04), run_time=1.0)
        self.wait(8.0)
        self.finish_section()

    # ---------------- 6. 关系图与易错点 ---------------- 36.3
    def scene_map(self):
        self.section(6, "三者关系与三个易错点")

        big = Circle(radius=2.35, color=DIM, stroke_width=2.0)
        big.move_to([-3.5, 0.05, 0])
        bl = txt("平行四边形", size=22, color=DIM).move_to([-3.5, 1.95, 0])
        self.play(Create(big), FadeIn(bl), run_time=1.2)

        cr = Circle(radius=1.5, color=GOLD, stroke_width=2.4).move_to([-4.0, -0.2, 0])
        cd = Circle(radius=1.5, color=GREEN, stroke_width=2.4).move_to([-3.0, -0.2, 0])
        self.play(Create(cr), Create(cd), run_time=1.5)

        lr = txt("矩形", size=21, color=GOLD).move_to([-5.2, -0.2, 0])
        ld = txt("菱形", size=21, color=GREEN).move_to([-1.8, -0.2, 0])
        ls = txt("正方形", size=20, color=BLUE).move_to([-3.5, -0.2, 0])
        self.play(FadeIn(lr), FadeIn(ld), run_time=1.0)
        self.play(FadeIn(ls, scale=0.9), run_time=0.8)
        self.wait(1.2)

        rows = [
            ("① 对角线别混", "矩形相等，菱形垂直"),
            ("② 菱形面积", "对角线乘积的一半"),
            ("③ 判定前提", "必须是平行四边形"),
        ]
        y = 1.85
        for a, b in rows:
            ta = txt(a, size=24, color=RED)
            ta.move_to([2.6, y, 0])
            self.play(FadeIn(ta, shift=RIGHT * 0.04), run_time=0.7)
            tb = txt(b, size=22, color=DIM)
            tb.move_to([2.6, y - 0.52, 0])
            self.play(FadeIn(tb, shift=RIGHT * 0.04), run_time=0.7)
            y -= 1.35
        self.wait(1.2)

        box = label_box("矩形看角，菱形看边，正方形全占", size=26, color=GOLD)
        box.move_to([2.6, -2.45, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.1)
        self.wait(9.0)
        self.finish_section()

    def construct(self):
        self.scene_intro()
        self.clear_stage()
        self.scene_rect_props()
        self.clear_stage()
        self.scene_rect_rules()
        self.clear_stage()
        self.scene_rhombus_props()
        self.clear_stage()
        self.scene_rhombus_rules()
        self.clear_stage()
        self.scene_square()
        self.clear_stage()
        self.scene_map()
        self.clear_stage(0.8)