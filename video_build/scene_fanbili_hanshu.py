# -*- coding: utf-8 -*-
"""反比例函数：乘积不变，两个量此消彼长。八年级下。"""

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


def P(x, y):
    return np.array([float(x), float(y), 0.0])


def make_plane(cx: float, cy: float, u: float, xr=5, yr=5) -> VGroup:
    """手绘平面直角坐标系（避免 LaTeX 数字）。u = 每个数学单位对应的场景长度。"""
    g = VGroup()
    ax = Arrow(P(cx - xr * u, cy), P(cx + xr * u + 0.18, cy), buff=0,
               color=DIM, stroke_width=2.0,
               max_tip_length_to_length_ratio=0.035)
    ay = Arrow(P(cx, cy - yr * u), P(cx, cy + yr * u + 0.18), buff=0,
               color=DIM, stroke_width=2.0,
               max_tip_length_to_length_ratio=0.035)
    g.add(ax, ay)
    for i in (-4, -2, 2, 4):
        g.add(Line(P(cx + i * u, cy - 0.05), P(cx + i * u, cy + 0.05),
                   color=DIM, stroke_width=1.8))
    for j in (-4, -2, 2, 4):
        g.add(Line(P(cx - 0.05, cy + j * u), P(cx + 0.05, cy + j * u),
                   color=DIM, stroke_width=1.8))
    g.add(txt("O", size=18, color=DIM).move_to(P(cx - 0.18, cy - 0.18)))
    g.add(txt("x", size=20, color=DIM).move_to(P(cx + xr * u + 0.36, cy - 0.17)))
    g.add(txt("y", size=20, color=DIM).move_to(P(cx - 0.21, cy + yr * u + 0.3)))
    return g


def branch(cx: float, cy: float, u: float, k: float, sign: int,
           color: str = GOLD, tmin: float = 0.42) -> ParametricFunction:
    """双曲线的一支。sign = +1 取 x > 0，-1 取 x < 0。"""
    def f(t):
        return P(cx + t * u, cy + (k / t) * u)

    rng = (tmin, 4.6) if sign > 0 else (-4.6, -tmin)
    return ParametricFunction(f, t_range=rng, color=color, stroke_width=3)


class FanbiliHanshuScene(NarratedScene):
    lesson = "fanbili_hanshu"

    def clear_stage(self, run_time: float = 0.5):
        keep = {id(self._track), id(self._fill)}
        junk = [m for m in self.mobjects if id(m) not in keep]
        if junk:
            self.play(*[FadeOut(m) for m in junk], run_time=run_time)
        self.cur_title = None
        self.cur_sub = None

    # ---------------- 0. 此消彼长 ---------------- 20.1
    def scene_intro(self):
        self.section(0, "此消彼长：乘积不变")

        q = txt("1200 米路，走得越快，用时越少", size=27, color=CHALK)
        q.move_to([0, 2.4, 0])
        self.play(FadeIn(q, shift=UP * 0.05), run_time=0.95)
        self.wait(0.9)

        b1 = label_box("速度 × 时间 = 1200", size=27, color=GOLD).move_to([-3.4, 1.05, 0])
        self.play(FadeIn(b1, scale=0.97), run_time=0.9)
        b2 = label_box("长 × 宽 = 12", size=27, color=GREEN).move_to([3.4, 1.05, 0])
        self.play(FadeIn(b2, scale=0.97), run_time=0.9)
        self.wait(1.0)

        n1 = txt("一个量变大，另一个量反而变小", size=26, color=CHALK).move_to([0, 0.0, 0])
        self.play(FadeIn(n1, shift=UP * 0.04), run_time=0.9)
        n2 = txt("但两个量的乘积始终不变", size=26, color=GOLD).move_to([0, -0.8, 0])
        self.play(FadeIn(n2, shift=UP * 0.04), run_time=0.9)
        self.wait(1.0)

        box = label_box("这样的关系，叫成反比例", size=28, color=CHALK)
        box.move_to([0, -2.1, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.1)
        self.wait(3.4)
        self.finish_section()

    # ---------------- 1. 定义 ---------------- 23.3
    def scene_def(self):
        self.section(1, "反比例函数：y = k / x")

        box = label_box("y = k / x　（k ≠ 0）", size=32, color=GOLD).move_to([0, 1.95, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.1)
        self.wait(0.9)

        n1 = txt("也可以写成 x y = k", size=27, color=CHALK).move_to([0, 0.95, 0])
        self.play(FadeIn(n1, shift=UP * 0.04), run_time=0.9)
        n2 = txt("k 叫比例系数，不能等于零", size=25, color=DIM).move_to([0, 0.2, 0])
        self.play(FadeIn(n2, shift=UP * 0.04), run_time=0.85)
        self.wait(1.0)

        c = label_box("x ≠ 0，y ≠ 0", size=28, color=GREEN).move_to([0, -0.85, 0])
        self.play(FadeIn(c, scale=0.97), run_time=0.95)
        w = txt("所以图像永远碰不到坐标轴", size=25, color=RED).move_to([0, -1.75, 0])
        self.play(FadeIn(w, shift=UP * 0.04), run_time=0.9)
        self.wait(1.0)

        fin = txt("两个量的乘积是常数，就是成反比例", size=25, color=DIM).move_to([0, -2.6, 0])
        self.play(FadeIn(fin, shift=UP * 0.04), run_time=0.9)
        self.wait(3.2)
        self.finish_section()

    # ---------------- 2. 图像与性质 ---------------- 26.8
    def scene_graph(self):
        self.section(2, "图像与性质：两支双曲线")

        lcx, rcx, cy, u = -3.5, 3.5, 0.5, 0.28
        lp = make_plane(lcx, cy, u)
        rp = make_plane(rcx, cy, u)
        self.play(Create(lp), Create(rp), run_time=1.2)

        c1 = txt("k > 0", size=27, color=GOLD).move_to([lcx, 2.62, 0])
        c2 = txt("k < 0", size=27, color=BLUE).move_to([rcx, 2.62, 0])
        self.play(FadeIn(c1, shift=UP * 0.05), FadeIn(c2, shift=UP * 0.05), run_time=0.9)
        self.wait(0.6)

        k = 2
        l1 = branch(lcx, cy, u, k, 1, GOLD)
        l2 = branch(lcx, cy, u, k, -1, GOLD)
        self.play(Create(l1), Create(l2), run_time=1.8)
        self.wait(1.0)

        r1 = branch(rcx, cy, u, -k, 1, BLUE)
        r2 = branch(rcx, cy, u, -k, -1, BLUE)
        self.play(Create(r1), Create(r2), run_time=1.8)
        self.wait(1.0)

        q1 = txt("一、三象限", size=24, color=GOLD).move_to([lcx, -1.32, 0])
        q2 = txt("二、四象限", size=24, color=BLUE).move_to([rcx, -1.32, 0])
        self.play(FadeIn(q1, shift=UP * 0.04), FadeIn(q2, shift=UP * 0.04), run_time=0.9)
        self.wait(0.8)

        d1 = txt("每一支：y 随 x 增大而减小", size=20, color=CHALK).move_to([lcx, -1.95, 0])
        d2 = txt("每一支：y 随 x 增大而增大", size=20, color=CHALK).move_to([rcx, -1.95, 0])
        self.play(FadeIn(d1, shift=UP * 0.04), FadeIn(d2, shift=UP * 0.04), run_time=0.95)
        self.wait(1.0)

        warn = txt("性质只在同一支上成立，跨支不能比较", size=23, color=RED)
        warn.move_to([0, -2.72, 0])
        self.play(FadeIn(warn, shift=UP * 0.04), run_time=0.95)
        self.wait(3.6)
        self.finish_section()

    # ---------------- 3. 画图三步 ---------------- 20.8
    def scene_draw(self):
        self.section(3, "画图：列表、描点、连线")

        rx = txt("x：−4　−2　−1　　1　　2　　4", size=23, color=CHALK)
        rx.move_to([0, 2.55, 0])
        ry = txt("y：−1　−2　−4　　4　　2　　1", size=23, color=GOLD)
        ry.move_to([0, 2.05, 0])
        self.play(FadeIn(rx, shift=UP * 0.04), run_time=0.9)
        self.play(FadeIn(ry, shift=UP * 0.04), run_time=0.9)
        self.wait(1.0)

        cx, cy, u = 0.0, -0.55, 0.38
        plane = make_plane(cx, cy, u, xr=5, yr=5)
        self.play(Create(plane), run_time=1.0)
        self.wait(0.5)

        pts = []
        for xv in (1, 2, 4, -1, -2, -4):
            pts.append(Dot(P(cx + xv * u, cy + (4 / xv) * u), radius=0.075, color=GOLD))
        self.play(LaggedStart(*[FadeIn(d, scale=0.9) for d in pts], lag_ratio=0.18),
                  run_time=1.9)
        self.wait(1.0)

        b1 = branch(cx, cy, u, 4, 1, GREEN, tmin=0.9)
        b2 = branch(cx, cy, u, 4, -1, GREEN, tmin=0.9)
        self.play(Create(b1), Create(b2), run_time=1.9)
        self.wait(0.9)

        note = txt("平滑曲线，越来越近坐标轴，但不相交", size=22, color=DIM)
        note.move_to([0, -2.95, 0])
        self.play(FadeIn(note, shift=UP * 0.04), run_time=0.9)
        self.wait(2.8)
        self.finish_section()

    # ---------------- 4. 待定系数法 ---------------- 22.5
    def scene_k(self):
        self.section(4, "求解析式：一个点就够")

        q = txt("图像经过点 (2, 3)，求解析式", size=27, color=CHALK).move_to([0, 2.4, 0])
        self.play(FadeIn(q, shift=UP * 0.05), run_time=0.95)
        self.wait(0.9)

        s1 = txt("① 设 y = k / x", size=28, color=CHALK).move_to([0, 1.45, 0])
        self.play(FadeIn(s1, shift=UP * 0.04), run_time=0.85)
        s2 = txt("② 代入：3 = k / 2", size=28, color=CHALK).move_to([0, 0.6, 0])
        self.play(FadeIn(s2, shift=UP * 0.04), run_time=0.85)
        s3 = txt("得 k = 2 × 3 = 6", size=29, color=GREEN).move_to([0, -0.25, 0])
        self.play(FadeIn(s3, shift=UP * 0.04), run_time=0.9)
        self.wait(1.0)

        s4 = txt("③ y = 6 / x", size=32, color=GOLD).move_to([0, -1.25, 0])
        self.play(FadeIn(s4, scale=0.98), run_time=0.95)
        self.wait(1.0)

        note = txt("k = x · y，一对坐标就能定 k", size=25, color=DIM).move_to([0, -2.3, 0])
        self.play(FadeIn(note, shift=UP * 0.04), run_time=0.9)
        self.wait(3.2)
        self.finish_section()

    # ---------------- 5. 应用 ---------------- 26.3
    def scene_apply(self):
        self.section(5, "用起来：面积与求解析式")

        h1 = txt("① 矩形面积 12", size=27, color=GOLD).move_to([-3.4, 2.15, 0])
        self.play(FadeIn(h1, shift=UP * 0.05), run_time=0.85)
        a1 = txt("x · y = 12", size=28, color=CHALK).move_to([-3.4, 1.3, 0])
        self.play(FadeIn(a1, shift=UP * 0.04), run_time=0.8)
        a2 = txt("y = 12 / x", size=30, color=GOLD).move_to([-3.4, 0.5, 0])
        self.play(FadeIn(a2, shift=UP * 0.04), run_time=0.85)
        a3 = txt("长扩大几倍，宽就缩小几倍", size=22, color=DIM).move_to([-3.4, -0.45, 0])
        self.play(FadeIn(a3, shift=UP * 0.04), run_time=0.85)
        self.wait(1.4)

        sep = Line([0.0, 2.4, 0], [0.0, -0.9, 0], color=DIM, stroke_width=1.4)
        sep.set_opacity(0.3)
        self.play(Create(sep), run_time=0.6)

        h2 = txt("② 图像过 (−2, 3)", size=27, color=BLUE).move_to([3.5, 2.15, 0])
        self.play(FadeIn(h2, shift=UP * 0.05), run_time=0.85)
        b1 = txt("k = −2 × 3 = −6", size=27, color=CHALK).move_to([3.5, 1.3, 0])
        self.play(FadeIn(b1, shift=UP * 0.04), run_time=0.85)
        b2 = txt("y = −6 / x", size=30, color=BLUE).move_to([3.5, 0.5, 0])
        self.play(FadeIn(b2, shift=UP * 0.04), run_time=0.85)
        b3 = txt("图像在第二、第四象限", size=22, color=DIM).move_to([3.5, -0.45, 0])
        self.play(FadeIn(b3, shift=UP * 0.04), run_time=0.85)
        self.wait(1.6)

        tip = label_box("乘积不变，是反比例题目的总开关", size=26, color=GREEN)
        tip.move_to([0, -2.15, 0])
        self.play(FadeIn(tip, scale=0.97), run_time=1.1)
        self.wait(4.2)
        self.finish_section()

    # ---------------- 6. 易错点 ---------------- 24.1
    def scene_traps(self):
        self.section(6, "三个易错点")

        rows = [
            ("① k 不能等于零", "k = 0 就不是反比例函数", RED),
            ("② 比较大小看是否同一支", "跨支不能直接用增减性", RED),
            ("③ 图像是平滑曲线", "不画折线，也不与坐标轴相交", RED),
        ]
        y = 1.95
        for a, b, col in rows:
            ta = txt(a, size=26, color=col).move_to([-3.35, y, 0])
            self.play(FadeIn(ta, shift=RIGHT * 0.04), run_time=0.7)
            tb = txt(b, size=24, color=DIM).move_to([3.05, y, 0])
            self.play(FadeIn(tb, shift=RIGHT * 0.04), run_time=0.75)
            y -= 0.95
        self.wait(1.2)

        note = txt("k 的正负决定图像在哪两个象限", size=25, color=CHALK)
        note.move_to([0, -1.25, 0])
        self.play(FadeIn(note, shift=UP * 0.04), run_time=0.9)
        self.wait(1.0)

        box = label_box("k 定象限，一支一个样", size=30, color=GOLD)
        box.move_to([0, -2.4, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.1)
        self.wait(4.4)
        self.finish_section()

    def construct(self):
        self.scene_intro()
        self.clear_stage()
        self.scene_def()
        self.clear_stage()
        self.scene_graph()
        self.clear_stage()
        self.scene_draw()
        self.clear_stage()
        self.scene_k()
        self.clear_stage()
        self.scene_apply()
        self.clear_stage()
        self.scene_traps()
        self.clear_stage(0.8)