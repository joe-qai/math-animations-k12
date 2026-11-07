# -*- coding: utf-8 -*-
"""圆的面积：分割拼成长方形、长=πr 宽=r、S=πr²、例题与易错点。六年级上册。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


class YuanMianjiScene(NarratedScene):
    lesson = "yuan-mianji"

    def clear_stage(self, run_time: float = 0.5):
        keep = {id(self._track), id(self._fill)}
        junk = [m for m in self.mobjects if id(m) not in keep]
        if junk:
            self.play(*[FadeOut(m) for m in junk], run_time=run_time)
        self.cur_title = None
        self.cur_sub = None

    # ---------- 工具：16 个扇形 + 拼好的长条 ----------
    def make_split(self, R, C, cx_strip, cy_strip, n=16):
        a = TAU / n
        w = PI * R / (n / 2)
        x0 = cx_strip - PI * R / 2
        secs, tgts = [], []
        for i in range(n):
            col = GOLD if i % 2 == 0 else BLUE
            s = Sector(radius=R, start_angle=i * a, angle=a, color=col,
                       stroke_width=1.6, fill_color=col, fill_opacity=0.42)
            s.shift(C)
            k = i // 2
            if i % 2 == 0:
                apex = [x0 + k * w, cy_strip - R / 2, 0]
                delta = PI / 2 - (i * a + a / 2)
            else:
                apex = [x0 + k * w + w / 2, cy_strip + R / 2, 0]
                delta = -PI / 2 - (i * a + a / 2)
            t = Sector(radius=R, start_angle=i * a, angle=a, color=col,
                       stroke_width=1.6, fill_color=col, fill_opacity=0.42)
            t.rotate(delta, about_point=ORIGIN).shift(apex)
            secs.append(s)
            tgts.append(t)
        return VGroup(*secs), VGroup(*tgts)

    # ---------------- 0. 圆形花坛 ---------------- 16.0
    def scene_story(self):
        self.section(0, "圆形花坛，要铺多少草皮")

        C = [-4.3, 0.35, 0]
        R = 1.65
        circ = Circle(radius=R, color=GOLD, stroke_width=3,
                      fill_color=GOLD, fill_opacity=0.16).move_to(C)
        self.play(Create(circ), run_time=1.5)

        rline = Line(C, [C[0] + R, C[1], 0], color=BLUE, stroke_width=2.6)
        rl = txt("半径 3 米", size=25, color=BLUE).move_to([C[0] + R / 2, C[1] + 0.32, 0])
        self.play(Create(rline), FadeIn(rl, shift=UP * 0.05), run_time=0.9)

        qs = VGroup(
            txt("圆形花坛，半径 3 米", size=28, color=CHALK),
            txt("铺满草皮，要多少平方米？", size=28, color=GOLD),
            txt("面积：圆里面一整块的大小", size=26, color=GREEN),
        ).arrange(DOWN, buff=0.34).move_to([3.4, 1.1, 0])
        for q in qs:
            self.play(FadeIn(q, shift=UP * 0.05), run_time=0.7)

        note = txt("和围一圈的周长，不是一回事", size=25, color=DIM).move_to([3.4, -0.5, 0])
        self.play(FadeIn(note, shift=UP * 0.05), run_time=0.8)
        self.wait(2.2)
        self.finish_section()

    # ---------------- 1. 分割、拼成长方形 ---------------- 16.7
    def scene_split(self):
        self.section(1, "切成 16 份，拼成一个长方形")

        C = [-3.9, 0.15, 0]
        R = 1.5
        circ = Circle(radius=R, color=CHALK, stroke_width=2.4).move_to(C)
        self.play(Create(circ), run_time=1.0)

        lines = VGroup()
        for i in range(16):
            ang = i * TAU / 16
            lines.add(Line(C, [C[0] + R * np.cos(ang), C[1] + R * np.sin(ang), 0],
                           color=DIM, stroke_width=1.2))
        self.play(LaggedStart(*[Create(l) for l in lines], lag_ratio=0.05), run_time=1.6)

        secs, tgts = self.make_split(R, C, 2.5, 0.05)
        self.play(FadeOut(circ), FadeOut(lines), FadeIn(secs), run_time=1.0)

        self.play(LaggedStart(*[ReplacementTransform(s, t) for s, t in zip(secs, tgts)],
                              lag_ratio=0.05), run_time=4.0, rate_func=smooth)

        cap = txt("分的份数越多，越接近长方形", size=26, color=GREEN)
        cap.move_to([0.6, -2.35, 0])
        self.play(FadeIn(cap, shift=UP * 0.05), run_time=0.9)
        self.wait(2.6)
        self.finish_section()

    # ---------------- 2. 长 = πr，宽 = r ---------------- 13.9
    def scene_dims(self):
        self.section(2, "长是 πr，宽是 r")

        _, strip = self.make_split(1.5, [-3.9, 0.15, 0], 2.5, 0.05)
        self.play(FadeIn(strip), run_time=0.9)

        x0 = 2.5 - PI * 1.5 / 2
        x1 = 2.5 + PI * 1.5 / 2
        br = Brace(Line([x0, -0.7, 0], [x1, -0.7, 0]), DOWN, buff=0.14, color=GOLD)
        bl = txt("长 ≈ 圆周长的一半 = πr", size=25, color=GOLD).next_to(br, DOWN, buff=0.1)
        self.play(Create(br), FadeIn(bl), run_time=1.0)

        vb = Brace(Line([x0 - 0.12, -0.7, 0], [x0 - 0.12, 0.8, 0]), LEFT, buff=0.14, color=BLUE)
        vl = txt("宽 = r", size=25, color=BLUE).next_to(vb, LEFT, buff=0.1)
        self.play(Create(vb), FadeIn(vl), run_time=0.9)

        rows = VGroup(
            txt("圆周长 = 2πr", size=28, color=CHALK),
            txt("一半就是 πr", size=28, color=GOLD),
            txt("所以 长 = πr，宽 = r", size=28, color=GREEN),
        ).arrange(DOWN, buff=0.32, aligned_edge=LEFT).move_to([2.9, 1.85, 0])
        for r_ in rows:
            self.play(FadeIn(r_, shift=RIGHT * 0.05), run_time=0.65)
            self.wait(0.2)
        self.wait(1.8)
        self.finish_section()

    # ---------------- 3. S = πr² ---------------- 14.7
    def scene_formula(self):
        self.section(3, "圆的面积公式")

        old = txt("长方形的面积 = 长 × 宽", size=32, color=CHALK).move_to([0, 2.05, 0])
        self.play(FadeIn(old, shift=UP * 0.05), run_time=0.9)

        mid = txt("圆的面积 = πr × r", size=34, color=BLUE).move_to([0, 1.05, 0])
        self.play(FadeIn(mid, shift=UP * 0.05), run_time=0.9)

        box = label_box("S = π r²", size=52, color=GOLD).move_to([0, -0.15, 0])
        self.play(FadeIn(box, scale=0.96), run_time=1.1)

        note = VGroup(
            txt("r² 表示 r × r，不是 r × 2", size=27, color=GREEN),
            txt("先算平方，再乘 π", size=26, color=DIM),
        ).arrange(DOWN, buff=0.26).move_to([0, -1.55, 0])
        self.play(FadeIn(note[0], shift=UP * 0.05), run_time=0.8)
        self.play(FadeIn(note[1], shift=UP * 0.05), run_time=0.8)
        self.wait(2.2)
        self.finish_section()

    # ---------------- 4. 例题：半径 3 米 ---------------- 16.0
    def scene_example(self):
        self.section(4, "半径 3 米，面积多少")

        prob = txt("半径 3 米的花坛，铺草皮要多少平方米", size=28, color=CHALK)
        prob.move_to([0, 2.2, 0])
        self.play(FadeIn(prob, shift=UP * 0.05), run_time=0.9)

        rows = [
            ("S = 3.14 × 3²", CHALK),
            ("= 3.14 × 9", BLUE),
            ("= 28.26（平方米）", GREEN),
        ]
        y = 0.95
        for s_, c_ in rows:
            self.play(FadeIn(txt(s_, size=36, color=c_).move_to([-1.0, y, 0]),
                             shift=UP * 0.04), run_time=0.85)
            y -= 0.82

        ans = txt("要买 28.26 平方米草皮", size=28, color=GOLD).move_to([0, -1.75, 0])
        self.play(FadeIn(ans, shift=UP * 0.05), run_time=0.9)

        tip = txt("先算 3 × 3 = 9，再乘 3.14", size=26, color=GREEN).move_to([0, -2.5, 0])
        self.play(FadeIn(tip, shift=UP * 0.05), run_time=0.8)
        self.wait(2.0)
        self.finish_section()

    # ---------------- 5. 先求半径 ---------------- 17.8
    def scene_reverse(self):
        self.section(5, "给直径或周长，先求半径")

        d = txt("直径 6 米 → 半径 3 米 → S = 28.26 平方米", size=28, color=CHALK)
        d.move_to([0, 2.15, 0])
        self.play(FadeIn(d, shift=UP * 0.05), run_time=0.9)

        c1 = txt("周长 18.84 米，怎么求面积？", size=28, color=GOLD).move_to([0, 1.15, 0])
        self.play(FadeIn(c1, shift=UP * 0.05), run_time=0.8)

        steps = VGroup(
            txt("r = 18.84 ÷ 3.14 ÷ 2 = 3（米）", size=33, color=BLUE),
            txt("S = 3.14 × 3² = 28.26（平方米）", size=33, color=GREEN),
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT).move_to([0, -0.1, 0])
        for s_ in steps:
            self.play(FadeIn(s_, shift=RIGHT * 0.05), run_time=0.9)

        note = VGroup(
            label_box("直径 ÷ 2 = 半径", size=26, color=CHALK),
            label_box("周长 ÷ π ÷ 2 = 半径", size=26, color=BLUE),
        ).arrange(RIGHT, buff=0.8).move_to([0, -1.7, 0])
        self.play(FadeIn(note[0], shift=UP * 0.05), run_time=0.7)
        self.play(FadeIn(note[1], shift=UP * 0.05), run_time=0.7)

        tip = txt("先求半径，再套面积公式", size=27, color=GOLD).move_to([0, -2.65, 0])
        self.play(FadeIn(tip, shift=UP * 0.05), run_time=0.8)
        self.wait(2.2)
        self.finish_section()

    # ---------------- 6. 易错点 + 三句话 ---------------- 18.4
    def scene_warn(self):
        self.section(6, "三个易错点")

        items = [
            ("r² 算成 r × 2", "r² 是 r 乘 r"),
            ("直径直接平方", "先除以 2 求半径"),
            ("面积单位写成厘米", "面积用平方厘米"),
        ]
        y = 2.05
        for bad_s, note in items:
            bad = txt(bad_s, size=28, color=RED).move_to([-3.2, y, 0])
            n = txt(note, size=25, color=GREEN).move_to([3.2, y, 0])
            cross = Line(bad.get_left() + [-0.1, -0.08, 0],
                         bad.get_right() + [0.1, 0.18, 0],
                         color=RED, stroke_width=2.8)
            self.play(FadeIn(bad, shift=RIGHT * 0.05), run_time=0.6)
            self.play(Create(cross), FadeIn(n, shift=RIGHT * 0.05), run_time=0.7)
            self.wait(0.7)
            y -= 0.92

        rows = VGroup(
            label_box("① 分割拼接，变成长方形", size=24, color=GOLD),
            label_box("② 长 = πr，宽 = r", size=24, color=CHALK),
            label_box("③ S = πr²，先平方再乘 π", size=24, color=GREEN),
        ).arrange(DOWN, buff=0.2).move_to([0, -1.65, 0])
        for r in rows:
            self.play(FadeIn(r, shift=RIGHT * 0.06), run_time=0.6)
            self.wait(0.55)

        self.wait(1.0)
        self.finish_section()

    def construct(self):
        self.scene_story()
        self.clear_stage()
        self.scene_split()
        self.clear_stage()
        self.scene_dims()
        self.clear_stage()
        self.scene_formula()
        self.clear_stage()
        self.scene_example()
        self.clear_stage()
        self.scene_reverse()
        self.clear_stage()
        self.scene_warn()
        self.clear_stage(0.8)