# -*- coding: utf-8 -*-
"""二次函数：抛物线、顶点式、最值与应用。九年级上。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


def P(x, y):
    return np.array([float(x), float(y), 0.0])


def frac(num: Mobject, den: Mobject, color=CHALK, lw: float = 2.4,
         gap: float = 0.10, pad: float = 0.08) -> VGroup:
    """竖排分数。"""
    w = max(num.width, den.width) + pad * 2
    line = Line(P(-w / 2, 0), P(w / 2, 0), color=color, stroke_width=lw)
    num.next_to(line, UP, buff=gap)
    den.next_to(line, DOWN, buff=gap)
    return VGroup(num, line, den)


def axes(cx: float, cy: float, w: float, h: float,
         color=DIM, lw: float = 2.0) -> VGroup:
    """简易坐标系：两条带箭头的线，中心在 (cx, cy)。"""
    ax = Arrow(P(cx - w / 2, cy), P(cx + w / 2, cy), color=color, stroke_width=lw,
               buff=0, max_tip_length_to_length_ratio=0.07)
    ay = Arrow(P(cx, cy - h / 2), P(cx, cy + h / 2), color=color, stroke_width=lw,
               buff=0, max_tip_length_to_length_ratio=0.07)
    return VGroup(ax, ay)


def parabola(cx: float, cy: float, f, t0: float, t1: float,
             color=GOLD, width: float = 3.4) -> ParametricFunction:
    """以 (cx, cy) 为顶点画 y = f(t) 的曲线，t 为相对横坐标。"""
    return ParametricFunction(lambda t: P(cx + t, cy + f(t)), t_range=[t0, t1, 0.02],
                              color=color, stroke_width=width)


def strip_label(s: str, color: str, size: int = 22) -> Mobject:
    return txt(s, size=size, color=color)


class ErciHanshuScene(NarratedScene):
    lesson = "erci-hanshu"

    def clear_stage(self, run_time: float = 0.5):
        keep = {id(self._track), id(self._fill)}
        junk = [m for m in self.mobjects if id(m) not in keep]
        if junk:
            self.play(*[FadeOut(m) for m in junk], run_time=run_time)
        self.cur_title = None
        self.cur_sub = None

    # ---------------- 0. 三条抛物线 ---------------- 26.1
    def scene_intro(self):
        self.section(0, "生活里的抛物线")

        chips = [
            ("喷泉水柱", "中间高两边低", -4.4, GOLD),
            ("投篮弧线", "先上升后下落", 0.0, GREEN),
            ("拱桥桥洞", "一条对称的弯", 4.4, BLUE),
        ]
        for name, note, cx, col in chips:
            b = label_box(name, size=24, color=col).move_to([cx, 2.15, 0])
            n = txt(note, size=21, color=DIM).move_to([cx, 1.45, 0])
            self.play(FadeIn(b, scale=0.97), run_time=0.75)
            self.play(FadeIn(n, shift=UP * 0.04), run_time=0.65)
        self.wait(0.9)

        f = txt("y = ax² + bx + c", size=52, color=GOLD).move_to([-0.6, 0.05, 0])
        cond = txt("(a ≠ 0)", size=30, color=RED).next_to(f, RIGHT, buff=0.26)
        cond.align_to(f, DOWN)
        self.play(FadeIn(f, scale=0.98), run_time=1.05)
        self.play(FadeIn(cond, shift=LEFT * 0.05), run_time=0.75)
        self.wait(0.7)

        d = txt("最高次是 2，这样的函数叫二次函数", size=26, color=CHALK)
        d.move_to([0, -1.15, 0])
        self.play(FadeIn(d, shift=UP * 0.04), run_time=0.95)

        box = label_box("图像是一条抛物线", size=26, color=GOLD)
        box.move_to([0, -2.25, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.0)
        self.wait(11.5)
        self.finish_section()

    # ---------------- 1. y = ax² 的图像 ---------------- 25.8
    def scene_basic(self):
        self.section(1, "最简单的 y = ax²")

        ax = axes(-3.6, 0.05, 4.2, 3.2)
        self.play(Create(ax), run_time=1.1)

        curve = parabola(-3.6, 0.05, lambda t: 0.40 * t * t, -1.9, 1.9, GOLD, 3.6)
        self.play(Create(curve), run_time=1.8)
        dot = Dot(P(-3.6, 0.05), radius=0.075, color=GOLD)
        self.play(FadeIn(dot), run_time=0.5)
        vp = txt("顶点在原点", size=22, color=GOLD).move_to([-2.35, -0.72, 0])
        self.play(FadeIn(vp, shift=RIGHT * 0.04), run_time=0.7)
        self.wait(0.8)

        l1 = strip_label("关于 y 轴对称", GOLD).move_to([-3.6, 2.55, 0])
        self.play(FadeIn(l1, shift=UP * 0.04), run_time=0.8)
        self.wait(0.9)

        # 右侧：a 的正负
        up = parabola(3.9, 1.0, lambda t: 0.42 * t * t, -1.3, 1.3, GOLD, 3.0)
        dn = parabola(3.9, -0.35, lambda t: -0.42 * t * t, -1.3, 1.3, GREEN, 3.0)
        t1 = txt("a > 0 开口向上", size=23, color=GOLD).move_to([3.9, 2.15, 0])
        t2 = txt("a < 0 开口向下", size=23, color=GREEN).move_to([3.9, -1.5, 0])
        self.play(Create(up), run_time=1.2)
        self.play(FadeIn(t1, shift=UP * 0.04), run_time=0.7)
        self.play(Create(dn), run_time=1.2)
        self.play(FadeIn(t2, shift=UP * 0.04), run_time=0.7)
        self.wait(1.2)

        note = txt("|a| 越大，开口越小、越窄", size=24, color=CHALK)
        note.move_to([2.6, -2.05, 0])
        self.play(FadeIn(note, shift=UP * 0.04), run_time=0.95)

        box = label_box("开口看 a 的符号，宽窄看 a 的大小", size=22, color=GOLD)
        box.move_to([0, -2.75, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.0)
        self.wait(9.0)
        self.finish_section()

    # ---------------- 2. 平移与顶点式 ---------------- 26.0
    def scene_shift(self):
        self.section(2, "平移与顶点式")

        f = txt("y = a(x − h)² + k", size=46, color=GOLD).move_to([-0.4, 2.1, 0])
        self.play(FadeIn(f, scale=0.98), run_time=1.0)
        self.wait(0.7)

        v = txt("顶点 (h, k)", size=30, color=GREEN).move_to([-3.3, 1.1, 0])
        s = txt("对称轴 x = h", size=30, color=GREEN).move_to([2.9, 1.1, 0])
        self.play(FadeIn(v, shift=UP * 0.04), run_time=0.8)
        self.play(FadeIn(s, shift=UP * 0.04), run_time=0.8)
        self.wait(0.9)

        r1 = txt("左右：左加右减", size=27, color=BLUE).move_to([0, 0.1, 0])
        r2 = txt("上下：上加下减", size=27, color=BLUE).move_to([0, -0.65, 0])
        self.play(FadeIn(r1, shift=UP * 0.04), run_time=0.85)
        self.play(FadeIn(r2, shift=UP * 0.04), run_time=0.85)
        self.wait(0.9)

        # 基础抛物线 → 平移后的抛物线
        ax = axes(-3.4, -1.85, 3.6, 3.0)
        base = parabola(-3.4, -1.85, lambda t: 0.30 * t * t, -1.5, 1.5, DIM, 2.6)
        self.play(Create(ax), Create(base), run_time=1.4)
        moved = parabola(-1.8, -1.25, lambda t: 0.30 * t * t, -1.3, 1.3, GOLD, 3.2)
        ar = Arrow(P(-3.0, -1.35), P(-1.75, -1.35), color=GOLD, stroke_width=2.4,
                   buff=0, max_tip_length_to_length_ratio=0.2)
        self.play(Create(moved), GrowArrow(ar), run_time=1.6)

        ex = txt("y = (x − 2)² + 3", size=27, color=GOLD).move_to([3.4, -1.35, 0])
        ev = txt("顶点 (2, 3)", size=25, color=GREEN).move_to([3.4, -2.05, 0])
        self.play(FadeIn(ex, shift=UP * 0.04), run_time=0.85)
        self.play(FadeIn(ev, shift=UP * 0.04), run_time=0.85)
        self.wait(9.0)
        self.finish_section()

    # ---------------- 3. 配方法化顶点式 ---------------- 26.8
    def scene_complete(self):
        self.section(3, "一般式化顶点式：配方")

        head = txt("y = x² − 4x + 5", size=38, color=CHALK).move_to([0, 2.35, 0])
        self.play(FadeIn(head, shift=UP * 0.04), run_time=0.9)
        self.wait(0.7)

        rows = [
            ("= (x² − 4x + 4) + 1", CHALK),
            ("= (x − 2)² + 1", GOLD),
            ("顶点 (2, 1)，对称轴 x = 2", GREEN),
        ]
        y = 1.7
        for s, col in rows:
            t = txt(s, size=31, color=col).move_to([0, y, 0])
            self.play(FadeIn(t, shift=UP * 0.04), run_time=0.9)
            y -= 0.78
        self.wait(0.9)

        note = txt("加上一次项系数一半的平方，再减掉", size=22, color=DIM)
        note.move_to([0, -0.55, 0])
        self.play(FadeIn(note, shift=UP * 0.04), run_time=0.9)
        self.wait(0.8)

        # 一般式结论（两行，居中排列）
        l1 = txt("一般式 y = ax² + bx + c", size=25, color=CHALK)
        l1.move_to([0, -1.15, 0])

        n1 = txt("−b", size=23, color=GOLD)
        d1 = txt("2a", size=23, color=GOLD)
        s1 = VGroup(txt("对称轴 x =", size=26, color=GOLD), frac(n1, d1))
        s1.arrange(RIGHT, buff=0.16).move_to([-2.55, -2.10, 0])

        n2 = txt("4ac − b²", size=21, color=GOLD)
        d2 = txt("4a", size=21, color=GOLD)
        s2 = VGroup(txt("顶点纵坐标 =", size=26, color=GOLD), frac(n2, d2))
        s2.arrange(RIGHT, buff=0.16).move_to([2.75, -2.10, 0])

        self.play(FadeIn(l1, shift=UP * 0.04), run_time=0.8)
        self.play(FadeIn(s1, scale=0.98), run_time=0.9)
        self.play(FadeIn(s2, scale=0.98), run_time=0.9)
        self.wait(7.0)
        self.finish_section()

    # ---------------- 4. 开口与最值 ---------------- 23.3
    def scene_extreme(self):
        self.section(4, "顶点就是最值")

        ax1 = axes(-4.2, -0.2, 3.6, 2.8)
        up = parabola(-4.2, -1.05, lambda t: 0.45 * t * t, -1.75, 1.75, GOLD, 3.2)
        d1 = Dot(P(-4.2, -1.05), radius=0.075, color=GOLD)
        self.play(Create(ax1), run_time=0.9)
        self.play(Create(up), run_time=1.4)
        self.play(FadeIn(d1), run_time=0.45)

        t1 = txt("a > 0：最低点", size=24, color=GOLD).move_to([-4.2, 1.62, 0])
        t2 = txt("有最小值", size=25, color=CHALK).move_to([-4.2, -1.95, 0])
        self.play(FadeIn(t1, shift=UP * 0.04), run_time=0.75)
        self.play(FadeIn(t2, shift=UP * 0.04), run_time=0.75)
        self.wait(0.9)

        ax2 = axes(3.6, -0.2, 3.6, 2.8)
        dn = parabola(3.6, 0.55, lambda t: -0.45 * t * t, -1.75, 1.75, GREEN, 3.2)
        d2 = Dot(P(3.6, 0.55), radius=0.075, color=GREEN)
        self.play(Create(ax2), run_time=0.9)
        self.play(Create(dn), run_time=1.4)
        self.play(FadeIn(d2), run_time=0.45)

        t3 = txt("a < 0：最高点", size=24, color=GREEN).move_to([3.6, 1.62, 0])
        t4 = txt("有最大值", size=25, color=CHALK).move_to([3.6, -1.95, 0])
        self.play(FadeIn(t3, shift=UP * 0.04), run_time=0.75)
        self.play(FadeIn(t4, shift=UP * 0.04), run_time=0.75)
        self.wait(1.0)

        box = label_box("先看 a 的符号，再算顶点的纵坐标", size=23, color=GOLD)
        box.move_to([0, -2.68, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.05)
        self.wait(8.5)
        self.finish_section()

    # ---------------- 5. 应用：最大面积 ---------------- 25.6
    def scene_apply(self):
        self.section(5, "应用：篱笆围出最大面积")

        head = txt("20 米篱笆靠墙围矩形", size=25, color=DIM).move_to([-4.4, 2.6, 0])
        self.play(FadeIn(head, shift=UP * 0.04), run_time=0.9)

        wall = Line(P(-6.6, 1.5), P(-6.6, -1.5), color=DIM, stroke_width=8)
        self.play(Create(wall), run_time=0.8)
        r = Rectangle(width=2.6, height=2.6, color=GREEN, stroke_width=2.6,
                      fill_color=GREEN, fill_opacity=0.06)
        r.move_to([-5.3, 0, 0])
        self.play(Create(r), run_time=1.1)

        wl = txt("宽 x", size=23, color=GREEN).move_to([-5.3, -1.62, 0])
        ll = txt("长 20 − 2x", size=23, color=GREEN).move_to([-5.3, 1.78, 0])
        self.play(FadeIn(wl), FadeIn(ll), run_time=0.9)
        self.wait(1.0)

        rows = [
            ("S = x(20 − 2x)", CHALK),
            ("= −2x² + 20x", CHALK),
            ("= −2(x − 5)² + 50", GOLD),
        ]
        y = 1.55
        for s, col in rows:
            t = txt(s, size=27, color=col).move_to([2.5, y, 0])
            self.play(FadeIn(t, shift=UP * 0.04), run_time=0.85)
            y -= 0.85
        self.wait(0.9)

        res = txt("x = 5 时，面积最大 50 m²", size=27, color=GREEN)
        res.move_to([2.5, -1.45, 0])
        self.play(FadeIn(res, scale=0.97), run_time=1.0)
        self.wait(0.9)

        note = txt("周长固定时，正方形面积最大", size=23, color=RED)
        note.move_to([0, -2.4, 0])
        self.play(FadeIn(note, shift=UP * 0.04), run_time=0.95)
        self.wait(7.5)
        self.finish_section()

    # ---------------- 6. 四个注意 ---------------- 24.9
    def scene_traps(self):
        self.section(6, "四个注意事项")

        rows = [
            ("① a 不能等于 0", "否则就不是二次函数"),
            ("② 对称轴 x = −b / 2a", "负号别丢"),
            ("③ 平移左加右减、上加下减", "方向别反"),
            ("④ 实际问题 x 有范围", "最值要在范围内取"),
        ]
        y = 1.85
        for a, b in rows:
            ta = txt(a, size=23, color=RED).move_to([-2.7, y, 0])
            tb = txt(b, size=21, color=DIM).move_to([3.7, y, 0])
            self.play(FadeIn(ta, shift=RIGHT * 0.04), run_time=0.65)
            self.play(FadeIn(tb, shift=RIGHT * 0.04), run_time=0.65)
            y -= 0.86
        self.wait(1.0)

        box = label_box("先看开口，再找顶点", size=28, color=GOLD)
        box.move_to([0, -2.45, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.1)
        self.wait(9.0)
        self.finish_section()

    def construct(self):
        self.scene_intro()
        self.clear_stage()
        self.scene_basic()
        self.clear_stage()
        self.scene_shift()
        self.clear_stage()
        self.scene_complete()
        self.clear_stage()
        self.scene_extreme()
        self.clear_stage()
        self.scene_apply()
        self.clear_stage()
        self.scene_traps()
        self.clear_stage(0.8)