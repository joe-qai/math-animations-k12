# -*- coding: utf-8 -*-
"""平均数：移多补少、总数÷份数、取值范围、例题、人数不同的陷阱、易错点。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403

VALS = [120, 130, 140, 150]


class PingjunShuScene(NarratedScene):
    lesson = "pingjun-shu"

    def clear_stage(self, run_time: float = 0.5):
        keep = {id(self._track), id(self._fill)}
        junk = [m for m in self.mobjects if id(m) not in keep]
        if junk:
            self.play(*[FadeOut(m) for m in junk], run_time=run_time)
        self.cur_title = None
        self.cur_sub = None

    # ---------------- 0. 体育课跳绳 ---------------- 18.9
    def scene_story(self):
        self.section(0, "体育课跳绳")

        hdr = txt("第一组四个同学，每人跳的个数", size=28, color=DIM).move_to([0, 2.35, 0])
        self.play(FadeIn(hdr, shift=UP * 0.05), run_time=0.8)

        xs = [-4.5, -1.5, 1.5, 4.5]
        for x, v in zip(xs, VALS):
            box = label_box(str(v), size=44, color=CHALK).move_to([x, 1.2, 0])
            self.play(FadeIn(box, scale=0.95), run_time=0.7)

        q = txt("这一组大概能跳多少个？", size=32, color=GOLD).move_to([0, -0.35, 0])
        self.play(FadeIn(q, shift=UP * 0.05), run_time=0.9)

        a = Arrow([0, -0.95, 0], [0, -1.5, 0], color=DIM, buff=0.06, stroke_width=3,
                  max_tip_length_to_length_ratio=0.3)
        self.play(Create(a), run_time=0.6)

        ans = label_box("平均每人 135 个", size=36, color=GREEN).move_to([0, -2.0, 0])
        self.play(FadeIn(ans, scale=0.96), run_time=0.9)

        name = txt("这个 135，就叫平均数", size=28, color=CHALK).move_to([0, -2.72, 0])
        self.play(FadeIn(name, shift=UP * 0.05), run_time=0.8)
        self.wait(3.0)
        self.finish_section()

    # ---------------- 1. 移多补少 ---------------- 13.7
    def scene_balance(self):
        self.section(1, "把多的移给少的")

        base = -1.95
        xs = [-5.4, -3.6, -1.8, 0.0]
        hs = [1.5, 1.9, 2.3, 2.7]
        cols = [BLUE, BLUE, GREEN, GREEN]

        bars = VGroup()
        labs = VGroup()
        for x, h, v, c in zip(xs, hs, VALS, cols):
            b = Rectangle(width=0.92, height=h, color=c, stroke_width=2.0,
                          fill_color=c, fill_opacity=0.35)
            b.move_to([x, base + h / 2, 0])
            bars.add(b)
            labs.add(txt(str(v), size=24, color=DIM).move_to([x, base - 0.34, 0]))
        self.play(LaggedStart(*[GrowFromEdge(b, DOWN) for b in bars], lag_ratio=0.18),
                  run_time=2.0)
        self.play(FadeIn(labs), run_time=0.8)

        line = DashedLine([-6.0, base + 2.1, 0], [0.7, base + 2.1, 0],
                          color=GOLD, stroke_width=2.4, dash_length=0.16)
        self.play(Create(line), run_time=0.9)

        mv1 = Arrow([xs[3] + 0.5, base + 2.55, 0], [xs[0] + 0.5, base + 1.65, 0],
                    color=ORANGE, buff=0.06, stroke_width=2.6,
                    max_tip_length_to_length_ratio=0.12)
        mv2 = Arrow([xs[2] + 0.5, base + 2.15, 0], [xs[1] + 0.5, base + 1.9, 0],
                    color=ORANGE, buff=0.06, stroke_width=2.6,
                    max_tip_length_to_length_ratio=0.16)
        self.play(Create(mv1), run_time=0.7)
        self.play(Create(mv2), run_time=0.7)

        rows = VGroup(
            txt("多的移给少的", size=30, color=CHALK),
            txt("让四个数变得一样多", size=29, color=GOLD),
            txt("这个一样多的数", size=27, color=DIM),
            txt("就是平均数", size=27, color=GREEN),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT).move_to([3.55, 0.55, 0])
        for r in rows:
            self.play(FadeIn(r, shift=RIGHT * 0.05), run_time=0.7)
        self.wait(1.6)
        self.finish_section()

    # ---------------- 2. 总数 ÷ 份数 ---------------- 15.4
    def scene_formula(self):
        self.section(2, "怎么算平均数")

        box = label_box("平均数 = 总数 ÷ 份数", size=40, color=GOLD).move_to([0, 1.75, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.1)

        rows = VGroup(
            txt("总数：把这几个数加起来", size=30, color=CHALK),
            txt("份数：一共有几个数", size=30, color=CHALK),
            txt("除出来的商，就是平均数", size=30, color=GREEN),
        ).arrange(DOWN, buff=0.5, aligned_edge=LEFT).move_to([-0.6, 0.0, 0])
        for r in rows:
            self.play(FadeIn(r, shift=RIGHT * 0.05), run_time=0.8)
            self.wait(0.2)

        ex = txt("120 + 130 + 140 + 150 = 540", size=26, color=DIM).move_to([0, -2.15, 0])
        self.play(FadeIn(ex, shift=UP * 0.05), run_time=0.8)
        self.wait(1.8)
        self.finish_section()

    # ---------------- 3. 平均数的取值范围 ---------------- 14.6
    def scene_range(self):
        self.section(3, "平均数一定在最大和最小之间")

        y0 = 0.55
        axis = Line([-5.6, y0, 0], [5.0, y0, 0], color=DIM, stroke_width=2.2)
        self.play(Create(axis), run_time=0.8)

        marks = [(-4.4, "120"), (-1.5, "130"), (1.4, "140"), (4.3, "150")]
        for x, s in marks:
            tick = Line([x, y0 - 0.12, 0], [x, y0 + 0.12, 0], color=DIM, stroke_width=2.2)
            lab = txt(s, size=28, color=CHALK).move_to([x, y0 - 0.5, 0])
            self.play(Create(tick), FadeIn(lab), run_time=0.45)

        mn = txt("最小", size=24, color=BLUE).move_to([-4.4, y0 - 1.05, 0])
        mx = txt("最大", size=24, color=RED).move_to([4.3, y0 - 1.05, 0])
        self.play(FadeIn(mn), FadeIn(mx), run_time=0.6)

        mid_x = -0.05
        dot = Dot([mid_x, y0, 0], radius=0.13, color=GOLD)
        mid = txt("135", size=32, color=GOLD).move_to([mid_x, y0 + 0.75, 0])
        stem = Line([mid_x, y0 + 0.05, 0], [mid_x, y0 + 0.5, 0], color=GOLD, stroke_width=2.2)
        self.play(FadeIn(dot, scale=0.7), Create(stem), FadeIn(mid), run_time=0.9)

        rows = VGroup(
            txt("平均数比最大的数小", size=29, color=RED),
            txt("比最小的数大", size=29, color=BLUE),
            txt("算出来超出范围，一定是算错了", size=27, color=GREEN),
        ).arrange(DOWN, buff=0.38).move_to([0, -1.85, 0])
        for r in rows:
            self.play(FadeIn(r, shift=UP * 0.05), run_time=0.8)
        self.wait(1.4)
        self.finish_section()

    # ---------------- 4. 例题：540 ÷ 4 ---------------- 18.1
    def scene_example(self):
        self.section(4, "四个同学的平均成绩")

        prob = txt("120、130、140、150，平均每人跳多少个", size=29, color=CHALK)
        prob.move_to([0, 2.3, 0])
        self.play(FadeIn(prob, shift=UP * 0.05), run_time=0.9)

        rows = [
            ("总数 = 120 + 130 + 140 + 150", CHALK),
            ("= 540（个）", BLUE),
            ("份数 = 4", CHALK),
            ("平均数 = 540 ÷ 4 = 135（个）", GREEN),
        ]
        y = 1.25
        for s, c in rows:
            self.play(FadeIn(txt(s, size=34, color=c).move_to([-0.5, y, 0]),
                             shift=UP * 0.04), run_time=0.85)
            y -= 0.75

        ans = label_box("平均每人跳 135 个", size=32, color=GOLD).move_to([0, -2.15, 0])
        self.play(FadeIn(ans, scale=0.97), run_time=0.9)
        self.wait(2.2)
        self.finish_section()

    # ---------------- 5. 人数不同不能直接平均 ---------------- 15.7
    def scene_trap(self):
        self.section(5, "两个班的平均分，能再平均吗")

        d1 = txt("一班：30 人，平均 80 分", size=30, color=CHALK).move_to([-2.4, 2.15, 0])
        d2 = txt("二班：20 人，平均 90 分", size=30, color=CHALK).move_to([-2.4, 1.45, 0])
        self.play(FadeIn(d1, shift=RIGHT * 0.05), run_time=0.7)
        self.play(FadeIn(d2, shift=RIGHT * 0.05), run_time=0.7)

        wrong = txt("(80 + 90) ÷ 2 = 85", size=34, color=RED).move_to([-2.2, 0.4, 0])
        cross = Line(wrong.get_left() + [-0.12, -0.12, 0], wrong.get_right() + [0.12, 0.12, 0],
                     color=RED, stroke_width=3.0)
        self.play(FadeIn(wrong, shift=RIGHT * 0.05), run_time=0.7)
        self.play(Create(cross), run_time=0.5)

        bad = txt("人数不一样，不能这样平均", size=28, color=RED).move_to([3.5, 0.4, 0])
        self.play(FadeIn(bad, shift=LEFT * 0.05), run_time=0.7)

        right = VGroup(
            txt("先算总分：30×80 + 20×90 = 4200", size=28, color=CHALK),
            txt("再除总人数：4200 ÷ 50 = 84", size=28, color=GREEN),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT).move_to([-0.35, -0.75, 0])
        for r in right:
            self.play(FadeIn(r, shift=UP * 0.05), run_time=0.8)

        tip = label_box("平均数 = 总分 ÷ 总人数", size=28, color=GOLD).move_to([0, -2.1, 0])
        self.play(FadeIn(tip, scale=0.97), run_time=0.9)
        self.wait(1.8)
        self.finish_section()

    # ---------------- 6. 易错点 + 三句话 ---------------- 18.0
    def scene_warn(self):
        self.section(6, "三个易错点")

        items = [
            ("总数加错或漏加", "先把每个数都加进去"),
            ("份数数错", "有几个数就除以几"),
            ("两个平均数直接再平均", "人数不同要先算总分"),
        ]
        y = 2.0
        for bad_s, note in items:
            bad = txt(bad_s, size=27, color=RED).move_to([-3.2, y, 0])
            n = txt(note, size=24, color=GREEN).move_to([3.25, y, 0])
            cross = Line(bad.get_left() + [-0.1, -0.08, 0],
                         bad.get_right() + [0.1, 0.18, 0],
                         color=RED, stroke_width=2.8)
            self.play(FadeIn(bad, shift=RIGHT * 0.05), run_time=0.6)
            self.play(Create(cross), FadeIn(n, shift=RIGHT * 0.05), run_time=0.7)
            self.wait(0.5)
            y -= 0.9

        rows = VGroup(
            label_box("① 平均数 = 总数 ÷ 份数", size=24, color=GOLD),
            label_box("② 它比最大的小，比最小的大", size=24, color=CHALK),
            label_box("③ 人数不同，要按总分算", size=24, color=GREEN),
        ).arrange(DOWN, buff=0.2).move_to([0, -1.6, 0])
        for r in rows:
            self.play(FadeIn(r, shift=RIGHT * 0.06), run_time=0.6)
            self.wait(0.5)

        self.wait(1.0)
        self.finish_section()

    def construct(self):
        self.scene_story()
        self.clear_stage()
        self.scene_balance()
        self.clear_stage()
        self.scene_formula()
        self.clear_stage()
        self.scene_range()
        self.clear_stage()
        self.scene_example()
        self.clear_stage()
        self.scene_trap()
        self.clear_stage()
        self.scene_warn()
        self.clear_stage(0.8)