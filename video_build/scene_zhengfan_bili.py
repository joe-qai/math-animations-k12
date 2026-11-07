# -*- coding: utf-8 -*-
"""正比例与反比例：相关联的量、商一定与积一定、图像、对比、例题。六年级下册。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


class ZhengfanBiliScene(NarratedScene):
    lesson = "zhengfan-bili"

    def clear_stage(self, run_time: float = 0.5):
        keep = {id(self._track), id(self._fill)}
        junk = [m for m in self.mobjects if id(m) not in keep]
        if junk:
            self.play(*[FadeOut(m) for m in junk], run_time=run_time)
        self.cur_title = None
        self.cur_sub = None

    # ---------------- 0. 买铅笔 ---------------- 18.2
    def scene_story(self):
        self.section(0, "买铅笔，总价和支数")

        x0 = -6.1
        xs = [x0, x0 + 1.35, x0 + 2.7, x0 + 4.05, x0 + 5.4]
        head = txt("支数", size=27, color=GOLD).move_to([xs[0], 1.95, 0])
        self.play(FadeIn(head), run_time=0.6)
        for i, v in enumerate(["1", "2", "3", "4"]):
            self.play(FadeIn(txt(v, size=30, color=CHALK).move_to([xs[i + 1], 1.95, 0])),
                      run_time=0.35)

        line = Line([xs[0] - 0.55, 1.58, 0], [xs[4] + 0.5, 1.58, 0],
                    color=DIM, stroke_width=2)
        self.play(Create(line), run_time=0.6)

        lab2 = txt("总价", size=27, color=BLUE).move_to([xs[0], 1.05, 0])
        self.play(FadeIn(lab2), run_time=0.6)
        for i, v in enumerate(["2", "4", "6", "8"]):
            self.play(FadeIn(txt(v, size=30, color=BLUE).move_to([xs[i + 1], 1.05, 0])),
                      run_time=0.35)

        rows = VGroup(
            txt("2 ÷ 1 = 2", size=27, color=DIM),
            txt("4 ÷ 2 = 2", size=27, color=DIM),
            txt("6 ÷ 3 = 2", size=27, color=DIM),
        ).arrange(DOWN, buff=0.22, aligned_edge=LEFT).move_to([-4.4, -0.55, 0])
        for r in rows:
            self.play(FadeIn(r, shift=RIGHT * 0.04), run_time=0.5)

        box = label_box("总价 ÷ 支数 = 单价（一定）", size=28, color=GOLD)
        box.move_to([2.7, 1.5, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.0)

        res = txt("商一定 → 成正比例", size=32, color=GREEN).move_to([2.7, 0.35, 0])
        self.play(FadeIn(res, shift=UP * 0.05), run_time=0.9)

        note = VGroup(
            txt("支数越多，总价越高", size=27, color=CHALK),
            txt("但每支的价钱始终是 2 元", size=27, color=CHALK),
        ).arrange(DOWN, buff=0.24).move_to([2.5, -1.0, 0])
        self.play(FadeIn(note[0], shift=UP * 0.05), run_time=0.7)
        self.play(FadeIn(note[1], shift=UP * 0.05), run_time=0.7)
        self.wait(1.6)
        self.finish_section()

    # ---------------- 1. 正比例的意义 ---------------- 19.3
    def scene_direct(self):
        self.section(1, "什么叫成正比例")

        steps = VGroup(
            txt("① 两种相关联的量", size=30, color=CHALK),
            txt("② 一种量变化，另一种也跟着变化", size=30, color=CHALK),
            txt("③ 对应的两个数的比值一定", size=30, color=CHALK),
        ).arrange(DOWN, buff=0.45, aligned_edge=LEFT).move_to([-1.2, 1.45, 0])
        for s in steps:
            self.play(FadeIn(s, shift=RIGHT * 0.05), run_time=0.9)
            self.wait(0.25)

        arrow = Arrow([-1.0, -0.55, 0], [-1.0, -1.25, 0], color=DIM, buff=0.08,
                      stroke_width=3, max_tip_length_to_length_ratio=0.3)
        self.play(Create(arrow), run_time=0.6)

        res = label_box("这两种量成正比例", size=36, color=GREEN).move_to([-1.0, -2.0, 0])
        self.play(FadeIn(res, scale=0.97), run_time=1.0)

        note = VGroup(
            txt("也可以说", size=26, color=DIM),
            txt("它们成正比例关系", size=26, color=DIM),
        ).arrange(DOWN, buff=0.2).move_to([4.6, -1.7, 0])
        self.play(FadeIn(note, shift=UP * 0.05), run_time=0.8)
        self.wait(1.8)
        self.finish_section()

    # ---------------- 2. 图像是一条直线 ---------------- 14.0
    def scene_graph(self):
        self.section(2, "正比例的图像是一条直线")

        ox, oy = -4.9, -2.35
        ax = Line([ox, oy, 0], [ox + 3.2, oy, 0], color=DIM, stroke_width=2.2)
        ay = Line([ox, oy, 0], [ox, oy + 2.9, 0], color=DIM, stroke_width=2.2)
        self.play(Create(ax), Create(ay), run_time=0.9)
        self.play(FadeIn(txt("时间", size=24, color=DIM).move_to([ox + 3.5, oy - 0.28, 0])),
                  FadeIn(txt("路程", size=24, color=DIM).move_to([ox - 0.42, oy + 3.05, 0])),
                  run_time=0.7)

        pts = []
        for k in (1, 2, 3, 4):
            pts.append([ox + 0.62 * k, oy + 0.62 * k, 0])

        dots = VGroup(*[Dot(p, radius=0.075, color=GOLD) for p in pts])
        self.play(LaggedStart(*[FadeIn(d, scale=0.6) for d in dots], lag_ratio=0.15),
                  run_time=1.4)

        seg = Line([ox, oy, 0], pts[-1], color=GREEN, stroke_width=2.8)
        self.play(Create(seg), run_time=1.4)

        notes = VGroup(
            txt("按数据描点，再连线", size=27, color=CHALK),
            txt("点都落在一条直线上", size=27, color=GREEN),
            txt("而且是经过原点的直线", size=27, color=GOLD),
        ).arrange(DOWN, buff=0.34).move_to([3.6, 0.85, 0])
        for n in notes:
            self.play(FadeIn(n, shift=LEFT * 0.05), run_time=0.7)
        self.wait(1.4)
        self.finish_section()

    # ---------------- 3. 反比例的意义 ---------------- 14.3
    def scene_inverse(self):
        self.section(3, "什么叫成反比例")

        box = label_box("速度 × 时间 = 路程（一定）", size=30, color=GOLD)
        box.move_to([0, 1.85, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.0)

        xs = [-4.6, -2.9, -1.2, 0.5]
        names = ["速度", "2", "4", "8"]
        times = ["时间", "12", "6", "3"]
        for x, s, c in zip(xs, names, [GOLD, CHALK, CHALK, CHALK]):
            self.play(FadeIn(txt(s, size=29, color=c).move_to([x, 0.75, 0])), run_time=0.4)
        for x, s, c in zip(xs, times, [BLUE, CHALK, CHALK, CHALK]):
            self.play(FadeIn(txt(s, size=29, color=c).move_to([x, 0.05, 0])), run_time=0.4)

        prod = txt("2 × 12 = 4 × 6 = 8 × 3 = 24", size=28, color=DIM)
        prod.move_to([-2.0, -0.85, 0])
        self.play(FadeIn(prod, shift=UP * 0.05), run_time=0.8)

        res = txt("积一定 → 成反比例", size=32, color=GREEN).move_to([-2.0, -1.85, 0])
        self.play(FadeIn(res, shift=UP * 0.05), run_time=0.9)

        note = VGroup(
            txt("速度越快", size=26, color=GOLD),
            txt("用的时间越短", size=26, color=BLUE),
        ).arrange(DOWN, buff=0.24).move_to([4.6, 0.4, 0])
        self.play(FadeIn(note[0], shift=UP * 0.05), run_time=0.7)
        self.play(FadeIn(note[1], shift=UP * 0.05), run_time=0.7)
        self.wait(1.6)
        self.finish_section()

    # ---------------- 4. 正 vs 反 ---------------- 16.6
    def scene_compare(self):
        self.section(4, "正比例和反比例怎么分")

        h1 = txt("正比例", size=32, color=GREEN).move_to([-3.0, 2.0, 0])
        h2 = txt("反比例", size=32, color=BLUE).move_to([3.0, 2.0, 0])
        self.play(FadeIn(h1, shift=DOWN * 0.05), FadeIn(h2, shift=DOWN * 0.05), run_time=0.8)

        rows = [
            ("商一定", "积一定"),
            ("一个变大，另一个也变大", "一个变大，另一个反而变小"),
            ("图像是直线", "图像是曲线"),
        ]
        y = 1.0
        for a, b in rows:
            ga = txt(a, size=27, color=CHALK).move_to([-3.0, y, 0])
            gb = txt(b, size=27, color=CHALK).move_to([3.0, y, 0])
            self.play(FadeIn(ga, shift=RIGHT * 0.04), run_time=0.5)
            self.play(FadeIn(gb, shift=LEFT * 0.04), run_time=0.5)
            y -= 1.0

        tip = txt("判断时，先看是商不变，还是积不变", size=30, color=GOLD)
        tip.move_to([0, -2.25, 0])
        self.play(FadeIn(tip, shift=UP * 0.05), run_time=0.9)
        self.wait(1.8)
        self.finish_section()

    # ---------------- 5. 例题：路程与时间 ---------------- 17.5
    def scene_example(self):
        self.section(5, "路程和时间，成正还是成反")

        r1 = VGroup(
            txt("速度一定", size=29, color=GOLD),
            txt("路程 ÷ 时间 = 速度（商一定）", size=29, color=CHALK),
            txt("→ 路程和时间成正比例", size=30, color=GREEN),
        ).arrange(DOWN, buff=0.28, aligned_edge=LEFT).move_to([-1.1, 1.55, 0])
        for x in r1:
            self.play(FadeIn(x, shift=RIGHT * 0.05), run_time=0.8)

        r2 = VGroup(
            txt("路程一定", size=29, color=GOLD),
            txt("速度 × 时间 = 路程（积一定）", size=29, color=CHALK),
            txt("→ 速度和时间成反比例", size=30, color=BLUE),
        ).arrange(DOWN, buff=0.28, aligned_edge=LEFT).move_to([-1.1, -1.1, 0])
        for x in r2:
            self.play(FadeIn(x, shift=RIGHT * 0.05), run_time=0.8)

        self.wait(1.6)
        self.finish_section()

    # ---------------- 6. 易错点 + 三句话 ---------------- 20.3
    def scene_warn(self):
        self.section(6, "三个易错点")

        items = [
            ("变大就说是正比例", "还要看比值是否一定"),
            ("商一定、积一定搞混", "商一定正，积一定反"),
            ("两个量不相关也判断", "先看是否相关联"),
        ]
        y = 2.0
        for bad_s, note in items:
            bad = txt(bad_s, size=27, color=RED).move_to([-3.3, y, 0])
            n = txt(note, size=24, color=GREEN).move_to([3.2, y, 0])
            cross = Line(bad.get_left() + [-0.1, -0.08, 0],
                         bad.get_right() + [0.1, 0.18, 0],
                         color=RED, stroke_width=2.8)
            self.play(FadeIn(bad, shift=RIGHT * 0.05), run_time=0.6)
            self.play(Create(cross), FadeIn(n, shift=RIGHT * 0.05), run_time=0.7)
            self.wait(0.5)
            y -= 0.9

        rows = VGroup(
            label_box("① 比值一定 → 正比例", size=24, color=GREEN),
            label_box("② 乘积一定 → 反比例", size=24, color=BLUE),
            label_box("③ 正比例图像是一条直线", size=24, color=GOLD),
        ).arrange(DOWN, buff=0.2).move_to([0, -1.6, 0])
        for r in rows:
            self.play(FadeIn(r, shift=RIGHT * 0.06), run_time=0.6)
            self.wait(0.5)

        self.wait(1.2)
        self.finish_section()

    def construct(self):
        self.scene_story()
        self.clear_stage()
        self.scene_direct()
        self.clear_stage()
        self.scene_graph()
        self.clear_stage()
        self.scene_inverse()
        self.clear_stage()
        self.scene_compare()
        self.clear_stage()
        self.scene_example()
        self.clear_stage()
        self.scene_warn()
        self.clear_stage(0.8)