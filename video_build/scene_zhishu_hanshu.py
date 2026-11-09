# -*- coding: utf-8 -*-
"""指数与指数函数：同底相乘，指数相加。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


def rtxt(s: str, y: float, size: int = 30, color: str = CHALK,
         width: float = 6.1, x: float = 3.55) -> Text:
    m = txt(s, size=size, color=color)
    if m.width > width:
        m.scale_to_fit_width(width)
    m.move_to([x, y, 0])
    return m


def ltxt(s: str, y: float, size: int = 30, color: str = CHALK,
         width: float = 5.4, x: float = -4.0) -> Text:
    m = txt(s, size=size, color=color)
    if m.width > width:
        m.scale_to_fit_width(width)
    m.move_to([x, y, 0])
    return m


def legend(entries, y: float = -1.88, x0: float = -6.2) -> VGroup:
    g = VGroup()
    x = x0
    for color, s in entries:
        d = Dot([x, y, 0], radius=0.07, color=color)
        t = txt(s, size=21, color=color).next_to(d, RIGHT, buff=0.12)
        g.add(d, t)
        x = t.get_right()[0] + 0.5
    return g


def axes_at(cx: float, cy: float, xr, yr, xlen: float = 4.6, ylen: float = 3.0) -> Axes:
    ax = Axes(x_range=xr, y_range=yr, x_length=xlen, y_length=ylen,
              tips=False, color=DIM, axis_config={"stroke_width": 2})
    ax.move_to([cx, cy, 0])
    return ax


class ZhishuHanshuScene(NarratedScene):
    lesson = "zhishu-hanshu"

    def construct(self):
        # ---------- 0. 细胞分裂 ----------
        self.section(0, "从细胞分裂说起")
        heads = ["第 0 小时", "第 1 小时", "第 2 小时", "第 3 小时"]
        counts = [1, 2, 4, 8]
        ys = [1.85, 0.95, 0.05, -0.85]
        row_labels = VGroup()
        dots = VGroup()
        for head, n, y in zip(heads, counts, ys):
            lb = txt(head, size=20, color=DIM).move_to([-6.05, y, 0])
            row_labels.add(lb)
            for k in range(n):
                d = Dot([-4.95 + k * 0.42, y, 0], radius=0.1, color=GOLD if k % 2 == 0 else BLUE)
                dots.add(d)
        self.play(FadeIn(row_labels), run_time=0.7)
        for i, d in enumerate(dots):
            self.play(FadeIn(d, scale=0.6), run_time=0.16)

        f = txt("2ˣ 个", size=42, color=GOLD).move_to([-4.0, -1.75, 0])
        note = txt("每小时翻一倍", size=24, color=DIM).move_to([-1.7, -1.75, 0])
        self.play(Write(f), FadeIn(note), run_time=0.7)

        r1 = rtxt("每小时分裂一次，一变二、二变四", 1.45, 27)
        r2 = rtxt("每一份都乘同一个倍数 2", 0.5, 30, GOLD)
        r3 = rtxt("x 小时后，数量是 2ˣ", -0.55, 31, GREEN)
        r4 = rtxt("这种变化会越来越快", -1.6, 26, DIM)
        for m in (r1, r2, r3, r4):
            self.play(Write(m), run_time=0.5)
        self.finish_section()

        # ---------- 1. 根式与分数指数幂 ----------
        self.section(1, "根式与分数指数幂")
        self.play(FadeOut(row_labels), FadeOut(dots), FadeOut(f), FadeOut(note),
                  FadeOut(r1), FadeOut(r2), FadeOut(r3), FadeOut(r4), run_time=0.5)

        sq = Square(side_length=1.2, color=BLUE, stroke_width=3)
        sq.move_to([-5.8, 0.6, 0])
        area = txt("a", size=26, color=CHALK).move_to(sq.get_center())
        side = txt("√a", size=22, color=BLUE).move_to([-5.8, -0.22, 0])
        self.play(Create(sq), run_time=0.8)
        self.play(FadeIn(area), FadeIn(side), run_time=0.6)

        f1 = ltxt("xⁿ = a  ⇒  x = ⁿ√a", 1.62, 28, CHALK, width=3.7, x=-3.35)
        f2 = ltxt("a^(1/n) = ⁿ√a", 0.6, 31, GOLD, width=3.4, x=-3.35)
        f3 = ltxt("a^(m/n) = ⁿ√(aᵐ)", -0.35, 31, BLUE, width=3.8, x=-3.35)
        ex = ltxt("8^(2/3) = ³√(8²) = 4", -1.45, 27, GREEN, width=4.2, x=-3.6)
        for m in (f1, f2, f3, ex):
            self.play(Write(m), run_time=0.5)

        r1 = rtxt("xⁿ = a 时，x 叫 a 的 n 次方根", 1.45, 27)
        r2 = rtxt("分数指数：先乘方，再开方", 0.5, 28, GOLD)
        r3 = rtxt("a^(m/n) = ⁿ√(aᵐ)", -0.55, 30, GREEN)
        r4 = rtxt("负指数是倒数：a⁻ⁿ = 1 / aⁿ", -1.6, 26, DIM)
        for m in (r1, r2, r3, r4):
            self.play(Write(m), run_time=0.5)
        self.finish_section()

        # ---------- 2. 指数运算三条律 ----------
        self.section(2, "指数运算三条律")
        self.play(FadeOut(sq), FadeOut(area), FadeOut(side), FadeOut(f1), FadeOut(f2),
                  FadeOut(f3), FadeOut(ex),
                  FadeOut(r1), FadeOut(r2), FadeOut(r3), FadeOut(r4), run_time=0.5)

        c1 = label_box("aᵐ · aⁿ = aᵐ⁺ⁿ", size=33, color=GOLD)
        c1.move_to([-4.1, 1.5, 0])
        c2 = label_box("(aᵐ)ⁿ = aᵐⁿ", size=33, color=GREEN)
        c2.move_to([-4.1, 0.5, 0])
        c3 = label_box("(ab)ⁿ = aⁿbⁿ", size=33, color=BLUE)
        c3.move_to([-4.1, -0.5, 0])
        self.play(FadeIn(c1), run_time=0.7)
        self.play(FadeIn(c2), run_time=0.7)
        self.play(FadeIn(c3), run_time=0.7)

        ex = txt("2³ · 2⁴ = 2⁷ = 128", size=27, color=CHALK).move_to([-4.1, -1.6, 0])
        self.play(Write(ex), run_time=0.7)

        r1 = rtxt("同底相乘：底数不变，指数相加", 1.45, 27)
        r2 = rtxt("幂的乘方：底数不变，指数相乘", 0.5, 27, GREEN)
        r3 = rtxt("积的乘方：分别乘方，再相乘", -0.55, 27, BLUE)
        r4 = rtxt("前提：底数 a > 0，b > 0", -1.6, 26, DIM)
        for m in (r1, r2, r3, r4):
            self.play(Write(m), run_time=0.5)
        self.finish_section()

        # ---------- 3. 指数函数的图像 ----------
        self.section(3, "指数函数的图像")
        self.play(FadeOut(c1), FadeOut(c2), FadeOut(c3), FadeOut(ex),
                  FadeOut(r1), FadeOut(r2), FadeOut(r3), FadeOut(r4), run_time=0.5)

        ax = axes_at(-4.15, 0.05, [-2, 2, 1], [-0.6, 4.2, 1], xlen=4.7, ylen=3.2)
        self.play(Create(ax), run_time=0.8)

        up = ax.plot(lambda x: 2 ** x, x_range=[-1.9, 1.85], color=GOLD, stroke_width=3.2)
        down = ax.plot(lambda x: 0.5 ** x, x_range=[-1.85, 1.9], color=BLUE, stroke_width=3.2)
        self.play(Create(up), run_time=1.1)
        self.play(Create(down), run_time=1.1)

        p0 = Dot(ax.c2p(0, 1), radius=0.1, color=RED)
        l0 = txt("(0, 1)", size=22, color=RED).move_to(ax.c2p(0, 1) + RIGHT * 0.62 + DOWN * 0.34)
        self.play(FadeIn(p0), FadeIn(l0), run_time=0.5)

        lg = legend([(GOLD, "y = 2ˣ"), (BLUE, "y = (1/2)ˣ")], y=-1.85, x0=-5.9)
        self.play(FadeIn(lg), run_time=0.5)

        r1 = rtxt("y = aˣ（a > 0，a ≠ 1）", 1.45, 28, GOLD)
        r2 = rtxt("定义域 R，值域 (0, +∞)", 0.5, 28)
        r3 = rtxt("无论底数多少，都过 (0, 1)", -0.55, 27, GREEN)
        r4 = rtxt("x 轴是水平渐近线", -1.6, 26, DIM)
        for m in (r1, r2, r3, r4):
            self.play(Write(m), run_time=0.5)
        self.finish_section()

        # ---------- 4. 底数越大越陡 ----------
        self.section(4, "底数越大越陡")
        self.play(FadeOut(ax), FadeOut(up), FadeOut(down), FadeOut(p0), FadeOut(l0),
                  FadeOut(lg),
                  FadeOut(r1), FadeOut(r2), FadeOut(r3), FadeOut(r4), run_time=0.5)

        ax = axes_at(-4.25, 0.05, [-1.5, 1.5, 1], [-0.6, 4.6, 1], xlen=4.4, ylen=3.3)
        self.play(Create(ax), run_time=0.8)

        c15 = ax.plot(lambda x: 1.5 ** x, x_range=[-1.4, 1.25], color=GREEN, stroke_width=3)
        c2 = ax.plot(lambda x: 2 ** x, x_range=[-1.4, 1.25], color=GOLD, stroke_width=3)
        c3 = ax.plot(lambda x: 3 ** x, x_range=[-1.4, 1.25], color=RED, stroke_width=3)
        self.play(Create(c15), run_time=0.8)
        self.play(Create(c2), run_time=0.8)
        self.play(Create(c3), run_time=0.8)

        lg = legend([(GREEN, "y = 1.5ˣ"), (GOLD, "y = 2ˣ"), (RED, "y = 3ˣ")],
                    y=-1.85, x0=-5.9)
        self.play(FadeIn(lg), run_time=0.6)

        p0 = Dot(ax.c2p(0, 1), radius=0.1, color=BLUE)
        self.play(FadeIn(p0), run_time=0.4)

        r1 = rtxt("a > 1 时，底数越大越陡", 1.45, 29, GOLD)
        r2 = rtxt("0 < a < 1 时，底数越小越陡", 0.5, 28, BLUE)
        r3 = rtxt("所有曲线都过 (0, 1)", -0.55, 28, GREEN)
        r4 = rtxt("底数互为倒数的两条关于 y 轴对称", -1.6, 24, DIM)
        for m in (r1, r2, r3, r4):
            self.play(Write(m), run_time=0.5)
        self.finish_section()

        # ---------- 5. 图像的平移 ----------
        self.section(5, "图像的平移")
        self.play(FadeOut(ax), FadeOut(c15), FadeOut(c2), FadeOut(c3), FadeOut(lg),
                  FadeOut(p0),
                  FadeOut(r1), FadeOut(r2), FadeOut(r3), FadeOut(r4), run_time=0.5)

        ax = axes_at(-4.2, 0.05, [-2, 4, 1], [-0.6, 4.2, 1], xlen=5.0, ylen=3.2)
        self.play(Create(ax), run_time=0.8)

        base = ax.plot(lambda x: 2 ** x, x_range=[-1.9, 1.5], color=GOLD, stroke_width=3.2)
        shift = ax.plot(lambda x: 2 ** (x - 2), x_range=[-0.1, 3.3], color=BLUE, stroke_width=3.2)
        self.play(Create(base), run_time=1.0)
        self.play(Create(shift), run_time=1.0)

        arrow = Arrow(ax.c2p(0.0, 0.55), ax.c2p(2.0, 0.55), color=GREEN,
                      stroke_width=3, buff=0, max_tip_length_to_length_ratio=0.22)
        al = txt("右移 2", size=22, color=GREEN).move_to(ax.c2p(1.0, 0.78))
        self.play(Create(arrow), FadeIn(al), run_time=0.7)

        lg = legend([(GOLD, "y = 2ˣ"), (BLUE, "y = 2^(x−2)")], y=-1.85, x0=-5.9)
        self.play(FadeIn(lg), run_time=0.5)

        r1 = rtxt("y = a^(x−h)：向右移 h 个单位", 1.45, 27)
        r2 = rtxt("y = a^(x+h)：向左移 h 个单位", 0.5, 27, BLUE)
        r3 = rtxt("口诀：左加右减", -0.55, 31, GOLD)
        r4 = rtxt("形状和渐近线都不变", -1.6, 26, DIM)
        for m in (r1, r2, r3, r4):
            self.play(Write(m), run_time=0.5)
        self.finish_section()

        # ---------- 6. 口诀 ----------
        self.section(6, "记一句话")
        self.play(FadeOut(ax), FadeOut(base), FadeOut(shift), FadeOut(arrow), FadeOut(al),
                  FadeOut(lg),
                  FadeOut(r1), FadeOut(r2), FadeOut(r3), FadeOut(r4), run_time=0.5)

        k1 = txt("同底相乘，指数相加", size=54, color=GOLD).move_to([0, 1.0, 0])
        k2 = txt("幂的乘方指数相乘，积的乘方分别乘方", size=30, color=CHALK).move_to([0, -0.1, 0])
        k3 = txt("指数函数恒过 (0, 1)，底数大于 1 就递增", size=30, color=GREEN).move_to([0, -1.15, 0])
        self.play(Write(k1), run_time=0.9)
        self.play(Write(k2), run_time=0.7)
        self.play(Write(k3), run_time=0.7)
        self.finish_section()

        self.play(FadeOut(k1), FadeOut(k2), FadeOut(k3), run_time=0.6)