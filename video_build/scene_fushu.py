# -*- coding: utf-8 -*-
"""负数初步：温度计、数轴、相反意义的量、大小比较。北师大版四年级上册。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


def thermometer(x: float = 0.0, top: float = 10, bot: float = -10):
    """竖直温度计：返回 (管身, 液柱组, 刻度组)。"""
    cy = 0.55
    k = 0.19                      # 每度对应的高度

    tube = RoundedRectangle(corner_radius=0.25, width=0.46, height=4.4,
                            stroke_color=DIM, stroke_width=3)
    tube.move_to([x, cy, 0])
    bulb = Circle(radius=0.40, color=DIM, stroke_width=3).move_to([x, cy - 2.4, 0])

    ticks = VGroup()
    for t in range(int(bot), int(top) + 1):
        y = cy + t * k
        long = (t % 5 == 0)
        ticks.add(Line([x + 0.23, y, 0], [x + (0.52 if long else 0.40), y, 0],
                       color=DIM, stroke_width=2.2 if long else 1.4))
        if long and t != 0:
            ticks.add(txt(str(t), size=19, color=DIM).move_to([x + 0.92, y, 0]))

    return VGroup(tube, bulb), ticks, k, cy


def mercury(x: float, degree: float, k: float, cy: float, color: str = RED):
    y = cy + degree * k
    col = Rectangle(width=0.26, height=(y + 1.45), stroke_width=0,
                    fill_color=color, fill_opacity=1.0)
    col.move_to([x, (y - 1.45) / 2, 0])
    ball = Circle(radius=0.32, stroke_width=0, fill_color=color,
                  fill_opacity=1.0).move_to([x, cy - 2.4, 0])
    return VGroup(col, ball)


class FushuChubuScene(NarratedScene):
    lesson = "fushu-chubu"

    def clear_stage(self, run_time: float = 0.5):
        keep = {id(self._track), id(self._fill)}
        junk = [m for m in self.mobjects if id(m) not in keep]
        if junk:
            self.play(*[FadeOut(m) for m in junk], run_time=run_time)
        self.cur_title = None
        self.cur_sub = None

    # ---------------- 0. 生活里的负数 ---------------- 17.6
    def scene_story(self):
        self.section(0, "零下二十度，怎么记")

        left = VGroup(
            label_box("哈尔滨", size=28, color=BLUE),
            txt("零下 20 ℃", size=34, color=BLUE),
        ).arrange(DOWN, buff=0.24).move_to([-3.5, 1.85, 0])
        right = VGroup(
            label_box("三亚", size=28, color=GOLD),
            txt("零上 25 ℃", size=34, color=GOLD),
        ).arrange(DOWN, buff=0.24).move_to([3.5, 1.85, 0])

        self.play(FadeIn(left[0], scale=0.96), run_time=0.7)
        self.play(FadeIn(left[1], shift=UP * 0.06), run_time=0.7)
        self.play(FadeIn(right[0], scale=0.96), run_time=0.7)
        self.play(FadeIn(right[1], shift=UP * 0.06), run_time=0.8)

        rows = VGroup(
            txt("电梯：地下 2 层  →  -2 层", size=27, color=CHALK),
            txt("存折：支出 60 元  →  -60 元", size=27, color=CHALK),
        ).arrange(DOWN, buff=0.36, aligned_edge=LEFT).move_to([0, 0.05, 0])
        for r in rows:
            self.play(FadeIn(r, shift=RIGHT * 0.06), run_time=0.8)

        note = txt("和正数意思相反的量，就用负数记", size=28, color=GREEN)
        note.move_to([0, -1.7, 0])
        self.play(FadeIn(note, shift=UP * 0.07), run_time=0.9)

        self.wait(0.6)
        self.finish_section()

    # ---------------- 1. 温度计 ---------------- 16.0
    def scene_thermo(self):
        self.section(1, "零是分界线")

        body, ticks, k, cy = thermometer(x=-1.2)
        self.play(Create(body[0]), Create(body[1]), run_time=1.2)
        self.play(LaggedStart(*[Create(t) if isinstance(t, Line) else FadeIn(t)
                                for t in ticks], lag_ratio=0.03), run_time=1.4)

        zero = Line([-1.62, cy, 0], [-0.78, cy, 0], color=GOLD, stroke_width=3)
        zlab = txt("0 ℃", size=27, color=GOLD).move_to([0.05, cy, 0])
        self.play(Create(zero), FadeIn(zlab), run_time=0.8)

        m1 = mercury(-1.2, -5, k, cy, color=BLUE)
        self.play(FadeIn(m1), run_time=0.8)
        l1 = VGroup(
            txt("零下 5 ℃", size=27, color=BLUE),
            txt("记作  -5 ℃", size=34, color=BLUE),
        ).arrange(DOWN, buff=0.18).move_to([3.4, -0.55, 0])
        self.play(FadeIn(l1, shift=RIGHT * 0.07), run_time=0.8)
        self.wait(2.2)

        m2 = mercury(-1.2, 5, k, cy, color=RED)
        self.play(Transform(m1, m2), run_time=1.2)
        l2 = VGroup(
            txt("零上 5 ℃", size=27, color=RED),
            txt("记作  +5 ℃", size=34, color=RED),
        ).arrange(DOWN, buff=0.18).move_to([3.4, 1.55, 0])
        self.play(FadeIn(l2, shift=RIGHT * 0.07), run_time=0.9)

        tip = txt("0 ℃ 以上水不结冰，0 ℃ 以下水就结冰", size=26, color=CHALK)
        tip.move_to([0, -2.55, 0])
        self.play(FadeIn(tip, shift=UP * 0.06), run_time=0.9)
        self.wait(0.5)
        self.finish_section()

    # ---------------- 2. 数轴上的正负数 ---------------- 13.0
    def scene_axis(self):
        self.section(2, "把温度计拉直，就是数轴")

        y = 0.75
        axis = Line([-6.6, y, 0], [6.6, y, 0], color=CHALK, stroke_width=3)
        head = Arrow([5.9, y, 0], [6.75, y, 0], color=CHALK, stroke_width=3,
                     buff=0, max_tip_length_to_length_ratio=0.3)
        self.play(Create(axis), GrowArrow(head), run_time=1.1)

        marks = VGroup()
        for i in range(-6, 7):
            marks.add(Line([i, y - 0.13, 0], [i, y + 0.13, 0], color=CHALK, stroke_width=2))
            marks.add(txt(str(i), size=20, color=DIM).move_to([i, y - 0.48, 0]))
        self.play(LaggedStart(*[FadeIn(m) for m in marks], lag_ratio=0.02), run_time=1.2)

        zero = Dot([0, y, 0], radius=0.13, color=GOLD)
        zl = txt("0", size=26, color=GOLD).move_to([0, y + 0.45, 0])
        self.play(FadeIn(zero), FadeIn(zl), run_time=0.6)

        pos = txt("正数", size=30, color=GREEN).move_to([3.4, y + 0.75, 0])
        neg = txt("负数", size=30, color=BLUE).move_to([-3.4, y + 0.75, 0])
        self.play(FadeIn(pos, shift=RIGHT * 0.06), FadeIn(neg, shift=LEFT * 0.06),
                  run_time=0.9)

        note = txt("0 既不是正数，也不是负数", size=30, color=GOLD)
        note.move_to([0, -1.35, 0])
        self.play(FadeIn(note, shift=UP * 0.07), run_time=0.9)
        self.wait(0.7)
        self.finish_section()

    # ---------------- 3. 相反意义的量 ---------------- 17.0
    def scene_opposite(self):
        self.section(3, "一对相反意义的量")

        head1 = txt("生活中的事", size=25, color=DIM).move_to([-3.5, 2.15, 0])
        head2 = txt("记作", size=25, color=DIM).move_to([2.4, 2.15, 0])
        self.play(FadeIn(head1), FadeIn(head2), run_time=0.6)

        pairs = [
            ("上车 5 人", "+5 人", GREEN),
            ("下车 3 人", "-3 人", BLUE),
            ("收入 100 元", "+100 元", GREEN),
            ("支出 60 元", "-60 元", BLUE),
            ("水位上升 2 米", "+2 米", GREEN),
            ("水位下降 1 米", "-1 米", BLUE),
        ]
        y = 1.55
        for left, right, col in pairs:
            l = txt(left, size=26, color=CHALK).move_to([-3.5, y, 0])
            r = txt(right, size=28, color=col).move_to([2.4, y, 0])
            self.play(FadeIn(l, shift=RIGHT * 0.05),
                      FadeIn(r, shift=RIGHT * 0.05), run_time=0.45)
            y -= 0.62

        note = txt("先说清谁为正，和它相反的那个就是负", size=27, color=GOLD)
        note.move_to([0, -2.45, 0])
        self.play(FadeIn(note, shift=UP * 0.06), run_time=0.9)
        self.wait(0.6)
        self.finish_section()

    # ---------------- 4. 比较大小 ---------------- 13.3
    def scene_compare(self):
        self.section(4, "负五和负二，谁大")

        y = 1.55
        axis = Line([-6.4, y, 0], [2.3, y, 0], color=CHALK, stroke_width=3)
        head = Arrow([1.8, y, 0], [2.45, y, 0], color=CHALK, stroke_width=3,
                     buff=0, max_tip_length_to_length_ratio=0.32)
        self.play(Create(axis), GrowArrow(head), run_time=0.9)

        marks = VGroup()
        for i in range(-6, 2):
            marks.add(Line([i, y - 0.12, 0], [i, y + 0.12, 0], color=CHALK, stroke_width=2))
            marks.add(txt(str(i), size=21, color=DIM).move_to([i, y - 0.46, 0]))
        self.play(LaggedStart(*[FadeIn(m) for m in marks], lag_ratio=0.02), run_time=1.0)

        d5 = Dot([-5, y, 0], radius=0.14, color=BLUE)
        d2 = Dot([-2, y, 0], radius=0.14, color=GREEN)
        self.play(FadeIn(d5), FadeIn(d2), run_time=0.6)

        a5 = txt("-5", size=34, color=BLUE).move_to([-5, y + 0.5, 0])
        a2 = txt("-2", size=34, color=GREEN).move_to([-2, y + 0.5, 0])
        self.play(FadeIn(a5), FadeIn(a2), run_time=0.6)

        big = txt("-5 < -2", size=50, color=GOLD).move_to([0, -0.55, 0])
        self.play(FadeIn(big, shift=UP * 0.08), run_time=0.9)

        rule = txt("越往左数越小；负号后面的数越大，这个负数反而越小", size=26, color=CHALK)
        rule.move_to([0, -1.85, 0])
        self.play(FadeIn(rule, shift=UP * 0.06), run_time=0.9)
        self.wait(0.6)
        self.finish_section()

    # ---------------- 5. 三个易错点 ---------------- 16.0
    def scene_warn(self):
        self.section(5, "三个易错点")

        items = [
            ("0 是正数", "0 既不是正数，也不是负数"),
            ("-3 可以写成 3", "负号不能丢，否则数就变了"),
            ("-5 > -2", "负数越负越小，-5 更小"),
        ]
        y = 1.75
        for bad_s, note in items:
            bad = txt(bad_s, size=32, color=RED).move_to([-3.6, y, 0])
            n = txt(note, size=25, color=GREEN).move_to([3.05, y, 0])
            cross = Line(bad.get_left() + [-0.12, -0.13, 0],
                         bad.get_right() + [0.12, 0.15, 0],
                         color=RED, stroke_width=3)
            self.play(FadeIn(bad, shift=RIGHT * 0.05), run_time=0.6)
            self.play(Create(cross), run_time=0.45)
            self.play(FadeIn(n, shift=RIGHT * 0.05), run_time=0.55)
            y -= 1.3

        tip = txt("记住：0 是分界，负号要写，负数越负越小", size=27, color=GOLD)
        tip.move_to([0, -2.45, 0])
        self.play(FadeIn(tip, shift=UP * 0.07), run_time=0.9)
        self.wait(0.6)
        self.finish_section()

    # ---------------- 6. 总结 ---------------- 15.3
    def scene_summary(self):
        self.section(6, "三句话")

        rows = VGroup(
            label_box("① 0 是分界：右边正，左边负", size=27, color=GOLD),
            label_box("② 正负数表示相反意义的量", size=27, color=CHALK),
            label_box("③ 越往右越大，负数越负越小", size=27, color=GREEN),
        ).arrange(DOWN, buff=0.32).move_to([0, 1.35, 0])
        for r in rows:
            self.play(FadeIn(r, shift=RIGHT * 0.07), run_time=0.7)
            self.wait(0.5)

        demo = txt("零下 5 ℃ 记作 -5 ℃      -5 < -2", size=29, color=BLUE)
        demo.move_to([0, -1.3, 0])
        self.play(FadeIn(demo, shift=UP * 0.06), run_time=0.9)

        end = txt("有了负数，相反的量就能记清楚了", size=28, color=GOLD)
        end.move_to([0, -2.25, 0])
        self.play(FadeIn(end, shift=UP * 0.06), run_time=0.8)
        self.wait(1.0)
        self.finish_section()

    def construct(self):
        self.scene_story()
        self.clear_stage()
        self.scene_thermo()
        self.clear_stage()
        self.scene_axis()
        self.clear_stage()
        self.scene_opposite()
        self.clear_stage()
        self.scene_compare()
        self.clear_stage()
        self.scene_warn()
        self.clear_stage()
        self.scene_summary()
        self.clear_stage(0.8)