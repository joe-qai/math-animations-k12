# -*- coding: utf-8 -*-
"""圆的周长：绕绳滚动、周长与直径的倍数、圆周率、C=πd、C=2πr、例题与易错点。六年级上册。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


class YuanZhouchangScene(NarratedScene):
    lesson = "yuan-zhouchang"

    def clear_stage(self, run_time: float = 0.5):
        keep = {id(self._track), id(self._fill)}
        junk = [m for m in self.mobjects if id(m) not in keep]
        if junk:
            self.play(*[FadeOut(m) for m in junk], run_time=run_time)
        self.cur_title = None
        self.cur_sub = None

    # ---------------- 0. 车轮转一圈走多远 ---------------- 17.5
    def scene_story(self):
        self.section(0, "车轮转一圈，能走多远")

        c = [-4.8, 0.40, 0]
        wheel = Circle(radius=1.50, color=GOLD, stroke_width=3,
                       fill_color=GOLD, fill_opacity=0.10).move_to(c)
        self.play(Create(wheel), run_time=1.4)

        spokes = VGroup()
        for k in range(4):
            ang = PI / 4 + k * PI / 2
            spokes.add(Line(c, [c[0] + 1.50 * np.cos(ang), c[1] + 1.50 * np.sin(ang), 0],
                            color=GOLD, stroke_width=1.8))
        hub = Dot(c, radius=0.07, color=GOLD)
        self.play(Create(spokes), FadeIn(hub), run_time=1.1)

        ground = Line([-6.6, -1.10, 0], [1.9, -1.10, 0], color=DIM, stroke_width=2.4)
        self.play(Create(ground), run_time=0.8)

        mark = Dot([c[0], c[1] - 1.50, 0], radius=0.09, color=RED)
        self.play(FadeIn(mark), run_time=0.5)

        qs = VGroup(
            txt("车轮转一圈，能走多远？", size=29, color=CHALK),
            txt("答案是：量出车轮的周长", size=27, color=GOLD),
            txt("周长：围成圆那一圈的长度", size=26, color=GREEN),
        ).arrange(DOWN, buff=0.32).move_to([3.9, 1.1, 0])
        for q in qs:
            self.play(FadeIn(q, shift=UP * 0.05), run_time=0.7)

        note = txt("拿根绳子绕一圈，再拉直量一量", size=25, color=DIM).move_to([3.9, -0.35, 0])
        self.play(FadeIn(note, shift=UP * 0.05), run_time=0.8)
        self.wait(2.2)
        self.finish_section()

    # ---------------- 1. 绕绳法与滚动法 ---------------- 18.9
    def scene_measure(self):
        self.section(1, "两个办法量出周长")

        c = [-5.0, 1.0, 0]
        r = 0.9
        circ = Circle(radius=r, color=CHALK, stroke_width=2.6).move_to(c)
        rope = Circle(radius=r + 0.07, color=GOLD, stroke_width=3.2).move_to(c)
        self.play(Create(circ), run_time=0.9)
        self.play(Create(rope), run_time=1.4)

        tag = txt("绕绳法", size=26, color=GOLD).move_to([-5.0, 2.3, 0])
        self.play(FadeIn(tag, shift=UP * 0.05), run_time=0.6)

        length = 2 * PI * (r + 0.07)
        flat = Line([-5.5, -1.15, 0], [-5.5 + length, -1.15, 0], color=GOLD, stroke_width=3.2)
        self.play(ReplacementTransform(rope, flat), run_time=2.0)

        br = Brace(flat, DOWN, buff=0.16, color=GOLD)
        bl = txt("拉直了，就是周长", size=25, color=GOLD).next_to(br, DOWN, buff=0.1)
        self.play(Create(br), FadeIn(bl), run_time=0.9)

        steps = VGroup(
            txt("① 绕绳法：贴边绕一圈，拉直量", size=26, color=CHALK),
            txt("② 滚动法：做个记号，滚一周量", size=26, color=CHALK),
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT).move_to([2.2, 0.35, 0])
        for st in steps:
            self.play(FadeIn(st, shift=RIGHT * 0.05), run_time=0.85)

        tip = txt("两个办法都能量出周长", size=26, color=GREEN).move_to([2.2, -0.9, 0])
        self.play(FadeIn(tip, shift=UP * 0.05), run_time=0.8)
        self.wait(2.6)
        self.finish_section()

    # ---------------- 2. 周长总是直径的 3 倍多 ---------------- 15.8
    def scene_ratio(self):
        self.section(2, "周长总是直径的 3 倍多")

        specs = [(0.45, "直径 2", 6.28), (0.80, "直径 4", 12.56), (1.15, "直径 6", 18.84)]
        x = -6.5
        for rr, dl, cc in specs:
            circ = Circle(radius=rr, color=BLUE, stroke_width=2.6,
                          fill_color=BLUE, fill_opacity=0.10)
            circ.move_to([x + rr, -1.5 + rr, 0])
            dline = Line([x, -1.5, 0], [x + 2 * rr, -1.5, 0], color=GOLD, stroke_width=2.4)
            lab = txt(dl, size=22, color=GOLD).move_to([x + rr, -2.3, 0])
            self.play(Create(circ), Create(dline), run_time=0.8)
            self.play(FadeIn(lab), run_time=0.4)
            x += 2 * rr + 0.45

        head = VGroup(
            txt("直径 / 厘米", size=24, color=DIM),
            txt("周长 / 厘米", size=24, color=BLUE),
            txt("周长 ÷ 直径", size=24, color=GREEN),
        ).arrange_in_grid(rows=1, cols=3, buff=1.05).move_to([2.85, 1.6, 0])
        self.play(FadeIn(head, shift=UP * 0.05), run_time=0.9)

        rows = [("2", "6.28", "3.14"), ("4", "12.56", "3.14"), ("6", "18.84", "3.14")]
        y = 0.85
        for a, b, c_ in rows:
            row = VGroup(
                txt(a, size=26, color=CHALK),
                txt(b, size=26, color=BLUE),
                txt(c_, size=26, color=GREEN),
            ).arrange_in_grid(rows=1, cols=3, buff=1.55).move_to([2.85, y, 0])
            self.play(FadeIn(row, shift=RIGHT * 0.04), run_time=0.6)
            y -= 0.75

        concl = txt("周长总是直径的 3 倍多一点", size=27, color=GOLD).move_to([2.85, -1.6, 0])
        self.play(FadeIn(concl, shift=UP * 0.05), run_time=0.9)
        self.wait(2.4)
        self.finish_section()

    # ---------------- 3. 圆周率 π 与 C = πd ---------------- 13.9
    def scene_pi(self):
        self.section(3, "圆周率 π 和周长公式")

        pi_t = txt("π", size=80, color=GOLD).move_to([-4.9, 1.15, 0])
        pi_l = txt("圆周率", size=27, color=GOLD).move_to([-4.9, 0.08, 0])
        self.play(FadeIn(pi_t, scale=0.9), run_time=0.9)
        self.play(FadeIn(pi_l, shift=UP * 0.05), run_time=0.7)

        says = VGroup(
            txt("周长 ÷ 直径 ≈ 3.14", size=30, color=CHALK),
            txt("这个固定的数叫圆周率", size=28, color=GREEN),
            txt("π ≈ 3.14，是无限不循环小数", size=26, color=DIM),
        ).arrange(DOWN, buff=0.3).move_to([1.6, 1.35, 0])
        for s in says:
            self.play(FadeIn(s, shift=UP * 0.05), run_time=0.7)

        box = label_box("C = π d", size=50, color=GOLD).move_to([0.2, -0.9, 0])
        self.play(FadeIn(box, scale=0.96), run_time=1.0)

        note = txt("周长 = 圆周率 × 直径", size=27, color=CHALK).move_to([0.2, -2.0, 0])
        self.play(FadeIn(note, shift=UP * 0.05), run_time=0.8)
        self.wait(2.4)
        self.finish_section()

    # ---------------- 4. C = 2πr ---------------- 12.6
    def scene_radius(self):
        self.section(4, "知道半径也行")

        c = [-4.6, 0.7, 0]
        r = 1.25
        circ = Circle(radius=r, color=BLUE, stroke_width=2.8,
                      fill_color=BLUE, fill_opacity=0.08).move_to(c)
        self.play(Create(circ), run_time=1.0)

        rline = Line(c, [c[0] + r, c[1], 0], color=GOLD, stroke_width=2.8)
        rl = txt("r", size=30, color=GOLD).move_to([c[0] + r / 2, c[1] + 0.28, 0])
        self.play(Create(rline), FadeIn(rl), run_time=0.8)

        dline = Line([c[0] - r, c[1], 0], c, color=GREEN, stroke_width=2.4)
        dl = txt("d = 2r", size=26, color=GREEN).move_to([c[0] - r / 2, c[1] - 0.34, 0])
        self.play(Create(dline), FadeIn(dl), run_time=0.8)

        eq = VGroup(
            txt("直径 = 半径 × 2", size=30, color=CHALK),
            txt("C = π × 2r", size=36, color=BLUE),
        ).arrange(DOWN, buff=0.34).move_to([1.5, 1.45, 0])
        for e in eq:
            self.play(FadeIn(e, shift=UP * 0.05), run_time=0.8)

        box = label_box("C = 2πr", size=48, color=GOLD).move_to([1.5, -0.3, 0])
        self.play(FadeIn(box, scale=0.96), run_time=1.0)

        note = txt("知道半径，乘 2 再乘 3.14，不用先求直径", size=26, color=GREEN)
        note.move_to([1.5, -1.5, 0])
        self.play(FadeIn(note, shift=UP * 0.05), run_time=0.9)
        self.wait(2.2)
        self.finish_section()

    # ---------------- 5. 例题：车轮直径 50 厘米 ---------------- 14.4
    def scene_example(self):
        self.section(5, "车轮直径 50 厘米")

        prob = txt("车轮直径 50 厘米，转一圈走多远", size=29, color=CHALK).move_to([0, 2.2, 0])
        self.play(FadeIn(prob, shift=UP * 0.05), run_time=0.9)

        rows = [
            ("C = 3.14 × 50", CHALK),
            ("= 157（厘米）", GREEN),
            ("转 10 圈：157 × 10 = 1570", BLUE),
            ("= 15.7（米）", GOLD),
        ]
        y = 1.05
        for s_, c_ in rows:
            self.play(FadeIn(txt(s_, size=34, color=c_).move_to([-1.3, y, 0]),
                             shift=UP * 0.04), run_time=0.8)
            y -= 0.78

        tip = txt("转一圈走一个周长，转几圈就乘几", size=27, color=GREEN).move_to([0, -2.25, 0])
        self.play(FadeIn(tip, shift=UP * 0.05), run_time=0.9)
        self.wait(2.0)
        self.finish_section()

    # ---------------- 6. 易错点 + 三句话 ---------------- 17.9
    def scene_warn(self):
        self.section(6, "三个易错点")

        items = [
            ("把直径当半径", "半径要乘 2 才是直径"),
            ("半圆只算弧", "别忘加上那条直径"),
            ("直径半径单位不同", "先化成同一单位"),
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
            label_box("① 周长 ÷ 直径 ≈ 3.14", size=24, color=GOLD),
            label_box("② C = πd，也等于 2πr", size=24, color=CHALK),
            label_box("③ 半圆周长 = 弧 + 直径", size=24, color=GREEN),
        ).arrange(DOWN, buff=0.2).move_to([0, -1.65, 0])
        for r in rows:
            self.play(FadeIn(r, shift=RIGHT * 0.06), run_time=0.6)
            self.wait(0.55)

        self.wait(1.0)
        self.finish_section()

    def construct(self):
        self.scene_story()
        self.clear_stage()
        self.scene_measure()
        self.clear_stage()
        self.scene_ratio()
        self.clear_stage()
        self.scene_pi()
        self.clear_stage()
        self.scene_radius()
        self.clear_stage()
        self.scene_example()
        self.clear_stage()
        self.scene_warn()
        self.clear_stage(0.8)