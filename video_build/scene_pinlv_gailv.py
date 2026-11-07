# -*- coding: utf-8 -*-
"""频率与概率：次数多了，偶然就露出规律。八年级。"""

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


def P(x, y):
    return np.array([float(x), float(y), 0.0])


def frac(n, d, color=CHALK, size=30):
    """竖排分数（自建，不用 LaTeX）。"""
    t1 = txt(str(n), size=size, color=color)
    t2 = txt(str(d), size=size, color=color)
    line = Line(LEFT, RIGHT, color=color, stroke_width=2)
    line.set_width(max(t1.width, t2.width) + 0.12)
    return VGroup(t1, line, t2).arrange(DOWN, buff=0.08)


class PinlvGailvScene(NarratedScene):
    lesson = "pinlv_gailv"

    def clear_stage(self, run_time: float = 0.5):
        keep = {id(self._track), id(self._fill)}
        junk = [m for m in self.mobjects if id(m) not in keep]
        if junk:
            self.play(*[FadeOut(m) for m in junk], run_time=run_time)
        self.cur_title = None
        self.cur_sub = None

    # ---------------- 0. 抛硬币：偶然里有规律 ---------------- 26.7
    def scene_intro(self):
        self.section(0, "抛硬币：偶然里也有规律")

        coin = Circle(radius=0.62, color=GOLD, stroke_width=3).move_to([-4.7, 1.95, 0])
        face = txt("正", size=34, color=GOLD).move_to(coin.get_center())
        self.play(Create(coin), run_time=0.9)
        self.play(FadeIn(face, scale=0.9), run_time=0.7)

        f1 = txt("抛一次，猜不准", size=26, color=CHALK).move_to([-4.7, 0.9, 0])
        self.play(FadeIn(f1, shift=UP * 0.05), run_time=0.8)
        f2 = txt("抛一万次呢", size=26, color=DIM).move_to([-4.7, 0.15, 0])
        self.play(FadeIn(f2, shift=UP * 0.05), run_time=0.8)
        self.wait(1.0)

        head = txt("试验次数", size=23, color=DIM).move_to([-0.7, 2.45, 0])
        head2 = txt("正面次数", size=23, color=DIM).move_to([2.1, 2.45, 0])
        head3 = txt("频率", size=23, color=DIM).move_to([4.6, 2.45, 0])
        self.play(FadeIn(head), FadeIn(head2), FadeIn(head3), run_time=0.9)

        rows = [
            ("十次", "六次", "0.60", CHALK),
            ("一百次", "五十二次", "0.52", CHALK),
            ("一万次", "五千零三次", "0.5003", GOLD),
        ]
        y = 1.72
        for a, b, c, col in rows:
            ta = txt(a, size=25, color=CHALK).move_to([-0.9, y, 0])
            tb = txt(b, size=25, color=CHALK).move_to([2.05, y, 0])
            tc = txt(c, size=25, color=col).move_to([4.62, y, 0])
            self.play(FadeIn(ta), FadeIn(tb), run_time=0.55)
            self.play(FadeIn(tc, shift=RIGHT * 0.05), run_time=0.55)
            y -= 0.85
        self.wait(1.2)

        note = label_box("次数越多，正面占比越接近一半", size=27, color=GREEN)
        note.move_to([1.2, -1.75, 0])
        self.play(FadeIn(note, scale=0.97), run_time=1.1)
        self.wait(2.6)
        self.finish_section()

    # ---------------- 1. 频数与频率 ---------------- 28.3
    def scene_freq(self):
        self.section(1, "频数与频率")

        d = txt("做 n 次试验，某个结果出现了 m 次", size=27, color=CHALK)
        d.move_to([0, 2.6, 0])
        self.play(FadeIn(d, shift=UP * 0.05), run_time=0.9)
        self.wait(0.8)

        b1 = label_box("m 叫频数", size=29, color=GOLD).move_to([-3.5, 1.65, 0])
        self.play(FadeIn(b1, scale=0.97), run_time=1.0)
        self.wait(0.6)

        b2 = label_box("m ÷ n 叫频率", size=29, color=GREEN).move_to([3.2, 1.65, 0])
        self.play(FadeIn(b2, scale=0.97), run_time=1.0)
        self.wait(1.0)

        ex = txt("抛 20 次，正面 9 次", size=26, color=CHALK).move_to([0, 0.7, 0])
        self.play(FadeIn(ex, shift=UP * 0.05), run_time=0.8)
        self.wait(0.5)

        p1 = txt("频数 = 9", size=27, color=GOLD).move_to([-3.6, -0.35, 0])
        self.play(FadeIn(p1, shift=UP * 0.04), run_time=0.8)

        fr = frac("9", "20", color=GREEN, size=34).move_to([1.2, -0.4, 0])
        eq = txt("= 0.45", size=30, color=GREEN).move_to([2.75, -0.4, 0])
        self.play(FadeIn(fr), FadeIn(eq, shift=RIGHT * 0.05), run_time=1.0)
        self.wait(1.2)

        warn = txt("频数是次数，频率是一个比值", size=26, color=RED).move_to([0, -2.1, 0])
        self.play(FadeIn(warn, shift=UP * 0.05), run_time=0.9)

        sub = txt("频率 = 频数 ÷ 总次数", size=24, color=DIM).move_to([0, -2.8, 0])
        self.play(FadeIn(sub, shift=UP * 0.05), run_time=0.8)
        self.wait(3.0)
        self.finish_section()

    # ---------------- 2. 频率的稳定性 ---------------- 24.5
    def scene_stable(self):
        self.section(2, "频率的稳定性")

        ox = Line([-5.6, -1.5, 0], [5.9, -1.5, 0], color=DIM, stroke_width=2)
        oy = Line([-5.6, -1.5, 0], [-5.6, 2.5, 0], color=DIM, stroke_width=2)
        self.play(Create(ox), Create(oy), run_time=1.0)

        y5 = 0.35
        dash = DashedLine([-5.6, y5, 0], [5.9, y5, 0], color=GOLD, stroke_width=2)
        self.play(Create(dash), run_time=0.9)
        l5 = txt("0.5", size=24, color=GOLD).move_to([-6.05, y5, 0])
        self.play(FadeIn(l5), run_time=0.5)

        pts = [(-4.9, 1.85), (-4.0, -0.75), (-3.1, 1.15), (-2.2, -0.15),
               (-1.3, 0.72), (-0.4, 0.1), (0.5, 0.62), (1.4, 0.32),
               (2.3, 0.58), (3.2, 0.41), (4.2, 0.53), (5.2, 0.47)]
        dots = VGroup()
        for x, y in pts:
            dots.add(Dot(P(x, y), radius=0.075, color=BLUE))
        self.play(LaggedStart(*[FadeIn(d) for d in dots], lag_ratio=0.12), run_time=2.4)
        self.wait(1.0)

        n1 = txt("次数越多，摆动越小", size=27, color=CHALK).move_to([0, 2.78, 0])
        self.play(FadeIn(n1, shift=UP * 0.05), run_time=0.9)
        self.wait(0.8)

        n2 = label_box("频率稳定在 0.5 附近 → 频率的稳定性", size=26, color=GREEN)
        n2.move_to([0, -2.45, 0])
        self.play(FadeIn(n2, scale=0.97), run_time=1.1)
        self.wait(3.4)
        self.finish_section()

    # ---------------- 3. 概率 ---------------- 29.4
    def scene_prob(self):
        self.section(3, "概率：刻画可能性的大小")

        d1 = txt("概率 P(A)：事件 A 发生的可能性大小", size=28, color=GOLD)
        d1.move_to([0, 2.5, 0])
        self.play(FadeIn(d1, shift=UP * 0.05), run_time=1.0)
        self.wait(0.8)

        line = Line([-4.9, 0.9, 0], [4.9, 0.9, 0], color=CHALK, stroke_width=2.4)
        self.play(Create(line), run_time=0.8)
        t0 = txt("0", size=25, color=CHALK).move_to([-4.9, 0.45, 0])
        t1 = txt("1", size=25, color=CHALK).move_to([4.9, 0.45, 0])
        self.play(FadeIn(t0), FadeIn(t1), run_time=0.6)

        m0 = Dot([-4.9, 0.9, 0], radius=0.09, color=RED)
        m1 = Dot([4.9, 0.9, 0], radius=0.09, color=GREEN)
        self.play(FadeIn(m0), FadeIn(m1), run_time=0.6)

        c0 = txt("不可能事件", size=25, color=RED).move_to([-4.9, 1.55, 0])
        c1 = txt("必然事件", size=25, color=GREEN).move_to([4.9, 1.55, 0])
        self.play(FadeIn(c0, shift=UP * 0.04), FadeIn(c1, shift=UP * 0.04), run_time=0.9)
        self.wait(1.2)

        rng = label_box("任何事件的概率都在 0 到 1 之间：0 ≤ P ≤ 1", size=26, color=CHALK)
        rng.move_to([0, -0.25, 0])
        self.play(FadeIn(rng, scale=0.97), run_time=1.1)
        self.wait(1.0)

        e1 = txt("掷骰子，点数小于 7 → P = 1", size=25, color=GREEN).move_to([0, -1.35, 0])
        self.play(FadeIn(e1, shift=UP * 0.04), run_time=0.85)
        e2 = txt("点数等于 7 → P = 0", size=25, color=RED).move_to([0, -2.05, 0])
        self.play(FadeIn(e2, shift=UP * 0.04), run_time=0.85)
        self.wait(1.0)

        e3 = txt("概率是固定的数，不是凭感觉猜", size=25, color=DIM).move_to([0, -2.8, 0])
        self.play(FadeIn(e3, shift=UP * 0.04), run_time=0.9)
        self.wait(3.2)
        self.finish_section()

    # ---------------- 4. 两种求法 ---------------- 28.4
    def scene_methods(self):
        self.section(4, "求概率的两种办法")

        h1 = txt("① 用频率估计概率", size=29, color=GOLD).move_to([-3.3, 2.0, 0])
        self.play(FadeIn(h1, shift=UP * 0.05), run_time=0.9)

        s1 = txt("次数很大时，频率 ≈ 概率", size=25, color=CHALK).move_to([-3.3, 1.15, 0])
        self.play(FadeIn(s1, shift=UP * 0.04), run_time=0.8)

        s2 = txt("种子发芽率稳定在 0.9", size=25, color=CHALK).move_to([-3.3, 0.35, 0])
        self.play(FadeIn(s2, shift=UP * 0.04), run_time=0.8)

        s3 = txt("→ 任取一颗发芽的概率约 0.9", size=24, color=GREEN).move_to([-3.3, -0.45, 0])
        self.play(FadeIn(s3, shift=UP * 0.04), run_time=0.85)
        self.wait(1.4)

        sep = Line([0.05, 2.35, 0], [0.05, -0.9, 0], color=DIM, stroke_width=1.4)
        sep.set_opacity(0.35)
        self.play(Create(sep), run_time=0.6)

        h2 = txt("② 等可能时用公式", size=29, color=GOLD).move_to([3.5, 2.0, 0])
        self.play(FadeIn(h2, shift=UP * 0.05), run_time=0.9)

        pw = txt("P =", size=30, color=CHALK).move_to([2.35, 0.95, 0])
        fr = frac("所求结果数", "所有等可能结果数", color=GREEN, size=22).move_to([4.1, 0.95, 0])
        self.play(FadeIn(pw), FadeIn(fr), run_time=1.1)
        self.wait(1.2)

        cond = txt("前提：每种结果出现的可能性相等", size=25, color=RED)
        cond.move_to([3.5, -0.35, 0])
        self.play(FadeIn(cond, shift=UP * 0.04), run_time=0.9)
        self.wait(1.0)

        note = txt("次数多 → 用频率估；结果等可能 → 直接算", size=25, color=CHALK)
        note.move_to([0, -2.3, 0])
        self.play(FadeIn(note, shift=UP * 0.05), run_time=1.0)
        self.wait(3.2)
        self.finish_section()

    # ---------------- 5. 掷骰子 ---------------- 29.6
    def scene_dice(self):
        self.section(5, "掷骰子：数一数就行")

        faces = VGroup()
        for i in range(6):
            sq = RoundedRectangle(corner_radius=0.12, width=0.92, height=0.92,
                                  color=CHALK, stroke_width=2.2)
            sq.move_to([-4.6 + i * 1.15, 1.75, 0])
            lab = txt(str(i + 1), size=28, color=CHALK).move_to(sq.get_center())
            faces.add(VGroup(sq, lab))
        self.play(LaggedStart(*[FadeIn(f, shift=UP * 0.12) for f in faces], lag_ratio=0.12),
                  run_time=1.8)
        self.wait(1.0)

        q1 = txt("点数是 1 的概率", size=26, color=CHALK).move_to([-3.2, 0.55, 0])
        self.play(FadeIn(q1, shift=UP * 0.04), run_time=0.8)

        hi1 = faces[0][0].copy().scale(1.1).set_stroke(GOLD, 4).set_fill(opacity=0)
        self.play(Create(hi1), run_time=0.6)

        p1 = txt("P =", size=28, color=GOLD).move_to([1.1, 0.55, 0])
        fr1 = frac("1", "6", color=GOLD, size=32).move_to([1.85, 0.55, 0])
        self.play(FadeIn(p1), FadeIn(fr1), run_time=0.9)
        self.wait(1.2)

        q2 = txt("点数小于 3 的概率", size=26, color=CHALK).move_to([-3.2, -0.85, 0])
        self.play(FadeIn(q2, shift=UP * 0.04), run_time=0.8)

        hi2 = faces[1][0].copy().scale(1.1).set_stroke(GREEN, 4).set_fill(opacity=0)
        self.play(Create(hi2), run_time=0.6)

        p2 = txt("P =", size=28, color=GREEN).move_to([-0.2, -0.85, 0])
        fr2 = frac("2", "6", color=GREEN, size=32).move_to([0.55, -0.85, 0])
        e2 = txt("= 1/3", size=27, color=GREEN).move_to([1.85, -0.85, 0])
        self.play(FadeIn(p2), FadeIn(fr2), run_time=0.9)
        self.play(FadeIn(e2, shift=RIGHT * 0.04), run_time=0.6)
        self.wait(1.2)

        box = label_box("六个面等可能，才能直接数个数", size=26, color=GOLD)
        box.move_to([0, -2.45, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.1)
        self.wait(3.4)
        self.finish_section()

    # ---------------- 6. 例题与易错点 ---------------- 39.2
    def scene_example(self):
        self.section(6, "例题：摸到红球的概率")

        q = txt("袋中 3 个红球、2 个白球，摸到红球的概率", size=26, color=CHALK)
        q.move_to([0, 2.55, 0])
        self.play(FadeIn(q, shift=UP * 0.05), run_time=1.0)
        self.wait(0.8)

        balls = VGroup()
        for i in range(5):
            col = RED if i < 3 else CHALK
            balls.add(Circle(radius=0.31, color=col, stroke_width=2.6,
                             fill_color=col, fill_opacity=0.85 if i < 3 else 0.8)
                      .move_to([-2.4 + i * 0.82, 1.5, 0]))
        self.play(LaggedStart(*[FadeIn(b, shift=UP * 0.1) for b in balls], lag_ratio=0.12),
                  run_time=1.6)

        lab = txt("共 5 个，红球 3 个", size=25, color=DIM).move_to([0, 0.7, 0])
        self.play(FadeIn(lab, shift=UP * 0.04), run_time=0.8)
        self.wait(1.0)

        pw = txt("P =", size=30, color=GOLD).move_to([-0.9, -0.45, 0])
        fr = frac("3", "5", color=GOLD, size=38).move_to([-0.05, -0.45, 0])
        self.play(FadeIn(pw), FadeIn(fr), run_time=1.1)
        self.wait(1.2)

        warn = txt("易错：次数太少频率≠概率　·　频率会变、概率固定　·　先看是否等可能",
                   size=23, color=RED)
        warn.move_to([0, -2.05, 0])
        self.play(FadeIn(warn, shift=UP * 0.04), run_time=1.0)
        self.wait(1.2)

        box = label_box("次数多，频率稳，稳定值才是概率", size=28, color=GREEN)
        box.move_to([0, -2.85, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.1)
        self.wait(4.6)
        self.finish_section()

    def construct(self):
        self.scene_intro()
        self.clear_stage()
        self.scene_freq()
        self.clear_stage()
        self.scene_stable()
        self.clear_stage()
        self.scene_prob()
        self.clear_stage()
        self.scene_methods()
        self.clear_stage()
        self.scene_dice()
        self.clear_stage()
        self.scene_example()
        self.clear_stage(0.8)