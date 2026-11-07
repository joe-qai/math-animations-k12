# -*- coding: utf-8 -*-
"""函数概念与一次函数：从变量到 y = kx + b。八年级。"""

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


def P(x, y):
    return np.array([float(x), float(y), 0.0])


def axe(ox, oy, x0, x1, y0, y1, color=DIM, w=2.0):
    """简单的坐标轴：两条带箭头的轴线。"""
    xa = Arrow(P(x0, oy), P(x1, oy), color=color, stroke_width=w, buff=0,
               max_tip_length_to_length_ratio=0.045)
    ya = Arrow(P(ox, y0), P(ox, y1), color=color, stroke_width=w, buff=0,
               max_tip_length_to_length_ratio=0.045)
    return VGroup(xa, ya)


class HanshuYiciScene(NarratedScene):
    lesson = "hanshu_yici"

    def clear_stage(self, run_time: float = 0.5):
        keep = {id(self._track), id(self._fill)}
        junk = [m for m in self.mobjects if id(m) not in keep]
        if junk:
            self.play(*[FadeOut(m) for m in junk], run_time=run_time)
        self.cur_title = None
        self.cur_sub = None

    # ---------------- 0. 变量与常量 ---------------- 28.5
    def scene_intro(self):
        self.section(0, "一个量变，另一个跟着变")

        rows = [
            ("1 分钟", "200 米"),
            ("2 分钟", "400 米"),
            ("3 分钟", "600 米"),
        ]
        y = 1.55
        for a, b in rows:
            ta = txt(a, size=27, color=CHALK).move_to([-4.85, y, 0])
            ar = txt("→", size=26, color=DIM).move_to([-3.6, y, 0])
            tb = txt(b, size=27, color=GOLD).move_to([-2.55, y, 0])
            self.play(FadeIn(ta, shift=RIGHT * 0.05), run_time=0.5)
            self.play(FadeIn(ar), FadeIn(tb, shift=RIGHT * 0.05), run_time=0.5)
            y -= 0.78
        self.wait(1.2)

        eq = label_box("y = 200x", size=32, color=GOLD)
        eq.move_to([2.7, 1.6, 0])
        self.play(FadeIn(eq, scale=0.97), run_time=1.1)
        self.wait(1.0)

        v1 = txt("x 变，y 也变", size=26, color=CHALK).move_to([2.7, 0.5, 0])
        self.play(FadeIn(v1, shift=UP * 0.05), run_time=0.8)

        v2 = txt("→ 变量：x、y", size=27, color=GOLD).move_to([2.7, -0.35, 0])
        self.play(FadeIn(v2, shift=UP * 0.05), run_time=0.85)
        self.wait(0.8)

        v3 = txt("200 始终不变", size=26, color=CHALK).move_to([2.7, -1.2, 0])
        self.play(FadeIn(v3, shift=UP * 0.05), run_time=0.8)

        v4 = txt("→ 常量：200", size=27, color=BLUE).move_to([2.7, -2.0, 0])
        self.play(FadeIn(v4, shift=UP * 0.05), run_time=0.85)
        self.wait(1.0)

        note = txt("气温随时间变，身高随年龄变——都是这种关系", size=24, color=DIM)
        note.move_to([-1.2, -2.7, 0])
        self.play(FadeIn(note, shift=UP * 0.05), run_time=0.9)
        self.wait(3.0)
        self.finish_section()

    # ---------------- 1. 函数的定义 ---------------- 33.1
    def scene_def(self):
        self.section(1, "什么叫函数")

        d1 = txt("x 每取一个确定的值，", size=28, color=CHALK).move_to([0, 2.35, 0])
        d2 = txt("y 都有唯一确定的值和它对应", size=28, color=CHALK).move_to([0, 1.65, 0])
        self.play(FadeIn(d1, shift=UP * 0.05), run_time=0.9)
        self.play(FadeIn(d2, shift=UP * 0.05), run_time=0.9)
        self.wait(1.0)

        name = txt("y 是 x 的函数", size=34, color=GOLD).move_to([0, 0.75, 0])
        self.play(FadeIn(name, scale=0.97), run_time=1.0)

        roles = txt("x 叫自变量　　y 叫因变量", size=26, color=DIM).move_to([0, 0.0, 0])
        self.play(FadeIn(roles, shift=UP * 0.05), run_time=0.9)
        self.wait(1.2)

        e1 = txt("例：y = 200x", size=26, color=CHALK).move_to([-3.6, -1.05, 0])
        e2 = txt("例：S = a²（a 是边长）", size=26, color=CHALK).move_to([-3.6, -1.8, 0])
        self.play(FadeIn(e1, shift=RIGHT * 0.05), run_time=0.8)
        self.play(FadeIn(e2, shift=RIGHT * 0.05), run_time=0.8)
        self.wait(1.0)

        bad = txt("x = 4 时，y = 2 或 −2", size=25, color=RED).move_to([3.3, -1.05, 0])
        self.play(FadeIn(bad, shift=LEFT * 0.05), run_time=0.85)
        bad2 = txt("不是函数", size=26, color=RED).move_to([3.3, -1.8, 0])
        self.play(FadeIn(bad2), run_time=0.7)
        self.play(Create(Line([1.7, -1.45, 0], [4.7, -1.45, 0], color=RED, stroke_width=2.4)),
                  run_time=0.6)
        self.wait(1.2)

        key = label_box("关键词：唯一确定", size=28, color=GREEN)
        key.move_to([0, -2.65, 0])
        self.play(FadeIn(key, scale=0.97), run_time=1.1)
        self.wait(3.6)
        self.finish_section()

    # ---------------- 2. 三种表示方法 ---------------- 22.8
    def scene_repr(self):
        self.section(2, "三种表示方法")

        h1 = txt("解析式", size=28, color=GOLD).move_to([-4.5, 1.75, 0])
        self.play(FadeIn(h1, shift=UP * 0.05), run_time=0.6)
        f1 = txt("y = 200x", size=28, color=CHALK).move_to([-4.5, 0.95, 0])
        self.play(FadeIn(f1), run_time=0.6)

        h2 = txt("列表", size=28, color=GOLD).move_to([0, 1.75, 0])
        self.play(FadeIn(h2, shift=UP * 0.05), run_time=0.6)
        t1 = txt("x　1　2　3", size=24, color=CHALK).move_to([0, 1.0, 0])
        t2 = txt("y　200　400　600", size=24, color=CHALK).move_to([0, 0.55, 0])
        self.play(FadeIn(t1), FadeIn(t2), run_time=0.7)

        h3 = txt("图像", size=28, color=GOLD).move_to([4.5, 1.75, 0])
        self.play(FadeIn(h3, shift=UP * 0.05), run_time=0.6)

        ax = axe(4.0, 0.15, 2.9, 6.2, -1.2, 1.4)
        self.play(Create(ax), run_time=0.9)
        ln = Line(P(3.15, -0.75), P(5.35, 0.95), color=GOLD, stroke_width=3)
        self.play(Create(ln), run_time=1.0)
        self.wait(1.0)

        same = txt("三种方法说的是同一个关系", size=27, color=CHALK).move_to([0, -1.35, 0])
        self.play(FadeIn(same, shift=UP * 0.05), run_time=0.9)
        self.wait(0.6)

        tip = txt("题目给哪种，就先用哪种", size=25, color=DIM).move_to([0, -2.1, 0])
        self.play(FadeIn(tip, shift=UP * 0.05), run_time=0.9)
        self.wait(3.0)
        self.finish_section()

    # ---------------- 3. 一次函数的定义 ---------------- 28.9
    def scene_linear(self):
        self.section(3, "一次函数：y = kx + b")

        box = label_box("y = kx + b　（k、b 是常数，k ≠ 0）", size=32, color=GOLD)
        box.move_to([0, 1.9, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.2)
        self.wait(1.0)

        n1 = txt("k：一次项系数（不能为 0）", size=25, color=CHALK).move_to([0, 0.85, 0])
        self.play(FadeIn(n1, shift=UP * 0.04), run_time=0.8)
        n2 = txt("b：常数项", size=25, color=CHALK).move_to([0, 0.2, 0])
        self.play(FadeIn(n2, shift=UP * 0.04), run_time=0.7)
        self.wait(1.0)

        lh = txt("当 b = 0", size=26, color=DIM).move_to([-3.3, -0.85, 0])
        lf = txt("y = kx", size=30, color=GREEN).move_to([-3.3, -1.6, 0])
        ln = txt("正比例函数", size=25, color=GREEN).move_to([-3.3, -2.25, 0])
        self.play(FadeIn(lh), run_time=0.5)
        self.play(FadeIn(lf), FadeIn(ln), run_time=0.9)
        self.wait(1.2)

        rh = txt("当 k = 0", size=26, color=DIM).move_to([3.3, -0.85, 0])
        rf = txt("y = b", size=30, color=RED).move_to([3.3, -1.6, 0])
        rn = txt("不是一次函数", size=25, color=RED).move_to([3.3, -2.25, 0])
        self.play(FadeIn(rh), run_time=0.5)
        self.play(FadeIn(rf), FadeIn(rn), run_time=0.9)
        self.wait(3.0)
        self.finish_section()

    # ---------------- 4. 图像是一条直线 ---------------- 28.3
    def scene_graph(self):
        self.section(4, "图像：一条直线")

        ax = axe(-3.7, -0.8, -6.6, -1.0, -2.7, 2.0)
        self.play(Create(ax), run_time=1.1)
        lo = txt("O", size=22, color=DIM).move_to([-3.38, -1.02, 0])
        lx = txt("x", size=24, color=DIM).move_to([-0.95, -0.55, 0])
        ly = txt("y", size=24, color=DIM).move_to([-3.35, 2.1, 0])
        self.play(FadeIn(lo), FadeIn(lx), FadeIn(ly), run_time=0.7)

        # y = 2x + 3，取两点 (0,3)、(-1.5,0)
        ux, uy = 0.60, 0.30
        ox, oy = -3.7, -0.8
        cart = lambda x, y: (ox + x * ux, oy + y * uy)

        p0 = cart(-3.0, -3.0)
        p1 = cart(1.8, 6.6)
        line = Line(P(*p0), P(*p1), color=GOLD, stroke_width=3.4)
        self.play(Create(line), run_time=1.4)

        d1 = Dot(P(*cart(0, 3)), radius=0.09, color=GREEN)
        d2 = Dot(P(*cart(-1.5, 0)), radius=0.09, color=GREEN)
        self.play(FadeIn(d1), FadeIn(d2), run_time=0.7)
        l1 = txt("(0, 3)", size=24, color=GREEN).move_to([-2.95, 0.55, 0])
        l2 = txt("(−1.5, 0)", size=24, color=GREEN).move_to([-5.55, -0.42, 0])
        self.play(FadeIn(l1), FadeIn(l2), run_time=0.8)
        self.wait(1.2)

        eq = txt("y = 2x + 3", size=26, color=GOLD).move_to([-4.35, 1.55, 0])
        self.play(FadeIn(eq, shift=UP * 0.05), run_time=0.8)
        self.wait(1.0)

        n1 = txt("两点确定一条直线", size=27, color=CHALK).move_to([3.3, 2.0, 0])
        self.play(FadeIn(n1, shift=UP * 0.05), run_time=0.85)

        n2 = txt("取 x = 0：得 (0, b)", size=25, color=CHALK).move_to([3.3, 1.1, 0])
        self.play(FadeIn(n2, shift=UP * 0.05), run_time=0.8)

        n3 = txt("取 y = 0：得 (−b/k, 0)", size=25, color=CHALK).move_to([3.3, 0.3, 0])
        self.play(FadeIn(n3, shift=UP * 0.05), run_time=0.8)
        self.wait(1.0)

        n4 = txt("连起来，向两端延长", size=26, color=GOLD).move_to([3.3, -0.75, 0])
        self.play(FadeIn(n4, shift=UP * 0.05), run_time=0.9)

        n5 = txt("k > 0：从左往右上升", size=25, color=GREEN).move_to([3.3, -1.75, 0])
        self.play(FadeIn(n5, shift=UP * 0.05), run_time=0.9)
        self.wait(3.0)
        self.finish_section()

    # ---------------- 5. k 与 b 管什么 ---------------- 28.3
    def scene_kb(self):
        self.section(5, "k 管方向，b 管位置")

        ax = axe(-4.9, -0.4, -6.8, -2.9, -2.6, 2.2, w=1.8)
        self.play(Create(ax), run_time=1.0)

        up = Line(P(-6.3, -1.7), P(-3.6, 1.5), color=GREEN, stroke_width=3)
        dn = Line(P(-6.3, 1.3), P(-3.6, -1.9), color=RED, stroke_width=3)
        self.play(Create(up), run_time=0.9)
        self.play(Create(dn), run_time=0.9)
        lu = txt("k > 0", size=24, color=GREEN).move_to([-3.15, 1.2, 0])
        ld = txt("k < 0", size=24, color=RED).move_to([-3.15, -1.6, 0])
        self.play(FadeIn(lu), FadeIn(ld), run_time=0.8)
        self.wait(1.2)

        n1 = txt("k > 0：y 随 x 增大而增大", size=26, color=GREEN).move_to([2.6, 2.0, 0])
        self.play(FadeIn(n1, shift=UP * 0.05), run_time=0.85)

        n2 = txt("k < 0：y 随 x 增大而减小", size=26, color=RED).move_to([2.6, 1.2, 0])
        self.play(FadeIn(n2, shift=UP * 0.05), run_time=0.85)

        n3 = txt("|k| 越大，直线越陡", size=25, color=DIM).move_to([2.6, 0.45, 0])
        self.play(FadeIn(n3, shift=UP * 0.05), run_time=0.8)
        self.wait(1.4)

        b1 = txt("b 是与 y 轴交点的纵坐标", size=26, color=GOLD).move_to([1.6, -0.55, 0])
        self.play(FadeIn(b1, shift=UP * 0.05), run_time=0.9)

        b2 = txt("b > 0 在上方，b < 0 在下方", size=25, color=CHALK).move_to([1.6, -1.35, 0])
        self.play(FadeIn(b2, shift=UP * 0.05), run_time=0.9)

        b3 = txt("y = kx 平移 |b| 个单位 → y = kx + b", size=24, color=BLUE)
        b3.move_to([0.9, -2.25, 0])
        self.play(FadeIn(b3, shift=UP * 0.05), run_time=0.9)
        self.wait(3.0)
        self.finish_section()

    # ---------------- 6. 待定系数法与易错点 ---------------- 38.8
    def scene_coeff(self):
        self.section(6, "已知两点，求解析式")

        steps = [
            ("①", "设 y = kx + b"),
            ("②", "代入两点的坐标"),
            ("③", "解方程组，求 k、b"),
            ("④", "把 k、b 写回解析式"),
        ]
        y = 1.95
        for num, s in steps:
            n = txt(num, size=25, color=GOLD).move_to([-5.75, y, 0])
            t = txt(s, size=25, color=CHALK).move_to([-3.35, y, 0])
            self.play(FadeIn(n, shift=RIGHT * 0.05), run_time=0.45)
            self.play(FadeIn(t, shift=RIGHT * 0.05), run_time=0.6)
            y -= 0.72
        self.wait(1.2)

        q = txt("直线过 (0, 3) 和 (2, 7)", size=26, color=CHALK).move_to([3.2, 1.95, 0])
        self.play(FadeIn(q, shift=UP * 0.05), run_time=0.85)
        self.wait(0.8)

        s1 = txt("代入 (0, 3)：b = 3", size=25, color=BLUE).move_to([3.2, 1.05, 0])
        self.play(FadeIn(s1, shift=UP * 0.04), run_time=0.8)

        s2 = txt("代入 (2, 7)：2k + 3 = 7", size=25, color=BLUE).move_to([3.2, 0.3, 0])
        self.play(FadeIn(s2, shift=UP * 0.04), run_time=0.85)

        s3 = txt("解得 k = 2", size=25, color=CHALK).move_to([3.2, -0.4, 0])
        self.play(FadeIn(s3, shift=UP * 0.04), run_time=0.7)

        res = label_box("y = 2x + 3", size=29, color=GOLD)
        res.move_to([3.2, -1.5, 0])
        self.play(FadeIn(res, scale=0.97), run_time=1.0)
        self.wait(1.6)

        warn = txt("易错：k = 0 不是一次函数　·　b 不是距离　·　增减性看 k 的符号",
                   size=23, color=RED)
        warn.move_to([0, -2.85, 0])
        self.play(FadeIn(warn, shift=UP * 0.04), run_time=1.0)
        self.wait(4.0)
        self.finish_section()

    def construct(self):
        self.scene_intro()
        self.clear_stage()
        self.scene_def()
        self.clear_stage()
        self.scene_repr()
        self.clear_stage()
        self.scene_linear()
        self.clear_stage()
        self.scene_graph()
        self.clear_stage()
        self.scene_kb()
        self.clear_stage()
        self.scene_coeff()
        self.clear_stage(0.8)