# -*- coding: utf-8 -*-
"""扇形统计图：圆表示总数、扇形表示百分比、读图、圆心角、例题、三种统计图对比。六年级上册。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403

# 数据：篮球 40%、足球 25%、跳绳 20%、其他 15%
DATA = [
    (0.40, GOLD, "篮球 40%"),
    (0.25, BLUE, "足球 25%"),
    (0.20, GREEN, "跳绳 20%"),
    (0.15, PURPLE, "其他 15%"),
]


def pie(center, radius=1.9, data=None, opacity=0.50, labels=True, start=PI / 2):
    """画扇形统计图：圆表示总数，从正上方顺时针铺开。"""
    data = data or DATA
    secs = VGroup()
    a = start
    for frac, c, name in data:
        ang = TAU * frac
        s = Sector(radius=radius, start_angle=a - ang, angle=ang, color=c,
                   stroke_width=2.0, fill_color=c, fill_opacity=opacity)
        s.shift(center)
        secs.add(s)
        a -= ang
    return secs


def pie_labels(center, radius=1.9, data=None):
    data = data or DATA
    out = VGroup()
    a = PI / 2
    for frac, c, name in data:
        ang = TAU * frac
        mid = a - ang / 2
        p = [center[0] + 0.62 * radius * np.cos(mid),
             center[1] + 0.62 * radius * np.sin(mid), 0]
        out.add(txt(name, size=22, color=BG).move_to(p))
        a -= ang
    return out


def pie_marks(center, radius, items, color=BG, size=26, rf=0.66):
    """在每个扇形中部标字，位置按扇形中角计算。"""
    out = VGroup()
    a = PI / 2
    for frac, s in items:
        ang = TAU * frac
        mid = a - ang / 2
        p = [center[0] + rf * radius * np.cos(mid),
             center[1] + rf * radius * np.sin(mid), 0]
        out.add(txt(s, size=size, color=color).move_to(p))
        a -= ang
    return out


def icon_pie(center, r=0.38):
    g = VGroup()
    a = PI / 2
    for frac, c in [(0.40, GOLD), (0.25, BLUE), (0.20, GREEN), (0.15, PURPLE)]:
        ang = TAU * frac
        s = Sector(radius=r, start_angle=a - ang, angle=ang, color=c,
                   stroke_width=1.2, fill_color=c, fill_opacity=0.6)
        s.shift(center)
        g.add(s)
        a -= ang
    return g


def icon_bar(center):
    g = VGroup()
    for i, h in enumerate((0.42, 0.66, 0.90)):
        r = Rectangle(width=0.24, height=h, color=BLUE_C,
                      stroke_width=1.2, fill_color=BLUE_C, fill_opacity=0.45)
        r.move_to([center[0] - 0.34 + i * 0.34, center[1] - 0.45 + h / 2, 0])
        g.add(r)
    return g


def icon_line(center):
    cols = [GREEN_C] * 4
    pts = [[-0.45, -0.35], [-0.15, 0.05], [0.15, -0.1], [0.45, 0.42]]
    pts = [[center[0] + p[0], center[1] + p[1], 0] for p in pts]
    g = VGroup(Line(pts[0], pts[1], color=cols[0], stroke_width=2.2),
               Line(pts[1], pts[2], color=cols[0], stroke_width=2.2),
               Line(pts[2], pts[3], color=cols[0], stroke_width=2.2))
    g.add(*[Dot(p, radius=0.055, color=GREEN) for p in pts])
    return g


class ShanxingTongjituScene(NarratedScene):
    lesson = "shanxing-tongjitu"

    def clear_stage(self, run_time: float = 0.5):
        keep = {id(self._track), id(self._fill)}
        junk = [m for m in self.mobjects if id(m) not in keep]
        if junk:
            self.play(*[FadeOut(m) for m in junk], run_time=run_time)
        self.cur_title = None
        self.cur_sub = None

    # ---------------- 0. 调查最喜欢的运动 ---------------- 19.0
    def scene_story(self):
        self.section(0, "调查最喜欢的运动")

        legend = VGroup()
        for frac, c, name in DATA:
            dot = Dot([-6.0, 0, 0], radius=0.10, color=c)
            t = txt(name, size=27, color=CHALK)
            row = VGroup(dot, t).arrange(RIGHT, buff=0.28)
            legend.add(row)
        legend.arrange(DOWN, buff=0.42, aligned_edge=LEFT).move_to([-3.6, 0.55, 0])
        for row in legend:
            self.play(FadeIn(row, shift=RIGHT * 0.05), run_time=0.5)

        c0 = [3.4, 0.55, 0]
        secs = pie(c0, 1.95)
        self.play(LaggedStart(*[FadeIn(s) for s in secs], lag_ratio=0.18), run_time=2.2)

        labs = pie_labels(c0, 1.95)
        self.play(FadeIn(labs), run_time=1.0)

        note = txt("圆 = 全班人数", size=26, color=DIM).move_to([3.4, -2.05, 0])
        self.play(FadeIn(note, shift=UP * 0.05), run_time=0.8)
        self.wait(2.4)
        self.finish_section()

    # ---------------- 1. 圆表示总数，扇形表示百分比 ---------------- 13.7
    def scene_meaning(self):
        self.section(1, "扇形统计图表示什么")

        c0 = [-4.2, 0.2, 0]
        secs = pie(c0, 1.55)
        self.play(LaggedStart(*[FadeIn(s) for s in secs], lag_ratio=0.15), run_time=1.6)

        whole = txt("100%", size=32, color=CHALK).move_to([c0[0], c0[1] - 0.05, 0])
        self.play(FadeIn(whole, scale=0.9), run_time=0.7)

        rows = VGroup(
            txt("整个圆 = 总数（100%）", size=29, color=CHALK),
            txt("每个扇形 = 一部分占总数的百分比", size=28, color=GREEN),
            txt("所有扇形加起来，正好是 100%", size=28, color=GOLD),
        ).arrange(DOWN, buff=0.45, aligned_edge=LEFT).move_to([2.3, 0.75, 0])
        for r in rows:
            self.play(FadeIn(r, shift=RIGHT * 0.05), run_time=0.8)
            self.wait(0.2)
        self.wait(1.4)
        self.finish_section()

    # ---------------- 2. 怎么读图 ---------------- 15.0
    def scene_read(self):
        self.section(2, "怎么读扇形统计图")

        c0 = [0.2, 0.45, 0]
        secs = pie(c0, 1.85)
        self.play(LaggedStart(*[FadeIn(s) for s in secs], lag_ratio=0.15), run_time=1.8)

        labs = pie_marks(c0, 1.85,
                         [(0.40, "40%"), (0.25, "25%"), (0.20, "20%"), (0.15, "15%")],
                         size=30, rf=0.62)
        self.play(FadeIn(labs), run_time=1.0)

        notes = VGroup(
            txt("先看整个圆代表什么", size=27, color=CHALK),
            txt("再看每个扇形的百分数", size=27, color=CHALK),
            txt("扇形越大，占比越大", size=28, color=GOLD),
        ).arrange(DOWN, buff=0.34).move_to([4.9, 0.2, 0])
        for n in notes:
            self.play(FadeIn(n, shift=LEFT * 0.05), run_time=0.8)
        self.wait(1.6)
        self.finish_section()

    # ---------------- 3. 圆心角 = 360° × 百分比 ---------------- 18.2
    def scene_angle(self):
        self.section(3, "扇形多大：圆心角怎么算")

        box = label_box("圆心角 = 360° × 百分比", size=32, color=GOLD).move_to([0, 2.1, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.0)

        c0 = [-3.7, -1.25, 0]
        q = Sector(radius=2.0, start_angle=0, angle=PI / 2,
                   color=BLUE, stroke_width=2.4, fill_color=BLUE, fill_opacity=0.35)
        q.shift(c0)
        self.play(FadeIn(q), run_time=1.4)

        ra = Line(c0, [c0[0] + 2.0, c0[1], 0], color=CHALK, stroke_width=2.2)
        ua = Line(c0, [c0[0], c0[1] + 2.0, 0], color=CHALK, stroke_width=2.2)
        self.play(Create(ra), Create(ua), run_time=0.8)

        right = Polygon([c0[0], c0[1], 0], [c0[0] + 0.32, c0[1], 0],
                        [c0[0] + 0.32, c0[1] + 0.32, 0], [c0[0], c0[1] + 0.32, 0],
                        color=RED, stroke_width=1.8)
        self.play(Create(right), run_time=0.6)

        deg = txt("90°", size=30, color=RED).move_to([c0[0] + 1.78, c0[1] + 1.72, 0])
        pct = txt("25%", size=30, color=BLUE).move_to([c0[0] + 1.45, c0[1] + 0.52, 0])
        self.play(FadeIn(deg), FadeIn(pct), run_time=0.8)

        steps = VGroup(
            txt("360° × 25%", size=36, color=CHALK),
            txt("= 360° × 0.25", size=36, color=BLUE),
            txt("= 90°", size=36, color=GREEN),
        ).arrange(DOWN, buff=0.32, aligned_edge=LEFT).move_to([2.9, -0.15, 0])
        for s in steps:
            self.play(FadeIn(s, shift=UP * 0.04), run_time=0.8)

        note = txt("所有圆心角加起来是 360°", size=27, color=GOLD).move_to([2.9, -1.95, 0])
        self.play(FadeIn(note, shift=UP * 0.05), run_time=0.8)
        self.wait(1.8)
        self.finish_section()

    # ---------------- 4. 例题：40 人的 40% ---------------- 16.3
    def scene_example(self):
        self.section(4, "40 人的 40% 是多少人")

        prob = txt("全班 40 人，喜欢篮球的占 40%", size=30, color=CHALK).move_to([0, 2.2, 0])
        self.play(FadeIn(prob, shift=UP * 0.05), run_time=0.9)

        rows = [
            ("40 × 40%", CHALK),
            ("= 40 × 0.4", BLUE),
            ("= 16（人）", GREEN),
        ]
        y = 1.0
        for s, c in rows:
            self.play(FadeIn(txt(s, size=42, color=c).move_to([-1.0, y, 0]),
                             shift=UP * 0.04), run_time=0.9)
            y -= 0.95

        ans = txt("喜欢篮球的有 16 人", size=32, color=GOLD).move_to([0, -1.55, 0])
        self.play(FadeIn(ans, shift=UP * 0.05), run_time=0.9)

        tip = txt("已知总数和百分比，求部分量用乘法", size=28, color=GREEN)
        tip.move_to([0, -2.35, 0])
        self.play(FadeIn(tip, shift=UP * 0.05), run_time=0.8)
        self.wait(1.6)
        self.finish_section()

    # ---------------- 5. 三种统计图 ---------------- 13.8
    def scene_kinds(self):
        self.section(5, "三种统计图怎么选")

        cards = [
            ("扇形统计图", "看各部分占的百分比", GOLD, icon_pie([-5.6, 0, 0])),
            ("条形统计图", "比较数量的多少", BLUE, icon_bar([-5.6, 0, 0])),
            ("折线统计图", "看数量的变化趋势", GREEN, icon_line([-5.6, 0, 0])),
        ]
        ys = [1.75, 0.25, -1.25]
        for (name, use, c, ic), y in zip(cards, ys):
            ic.move_to([-5.5, y, 0])
            self.play(FadeIn(ic), run_time=0.6)
            a = txt(name, size=30, color=c).move_to([-3.5, y, 0])
            b = txt(use, size=28, color=CHALK).move_to([2.6, y, 0])
            self.play(FadeIn(a, shift=RIGHT * 0.05), run_time=0.5)
            self.play(FadeIn(b, shift=LEFT * 0.05), run_time=0.5)

        tip = label_box("看比例用扇形，比多少用条形，看变化用折线", size=25, color=GREEN)
        tip.move_to([0, -2.5, 0])
        self.play(FadeIn(tip, scale=0.97), run_time=0.9)
        self.wait(1.2)
        self.finish_section()

    # ---------------- 6. 易错点 + 三句话 ---------------- 20.0
    def scene_warn(self):
        self.section(6, "三个易错点")

        items = [
            ("把百分数当人数", "百分数要乘总数才是人数"),
            ("扇形加起来不是 100%", "检查各部分加起来"),
            ("圆心角算成 360 × 人数", "是 360° 乘百分比"),
        ]
        y = 2.0
        for bad_s, note in items:
            bad = txt(bad_s, size=27, color=RED).move_to([-3.3, y, 0])
            n = txt(note, size=23, color=GREEN).move_to([3.2, y, 0])
            cross = Line(bad.get_left() + [-0.1, -0.08, 0],
                         bad.get_right() + [0.1, 0.18, 0],
                         color=RED, stroke_width=2.8)
            self.play(FadeIn(bad, shift=RIGHT * 0.05), run_time=0.6)
            self.play(Create(cross), FadeIn(n, shift=RIGHT * 0.05), run_time=0.7)
            self.wait(0.5)
            y -= 0.9

        rows = VGroup(
            label_box("① 圆表示总数，扇形表示百分比", size=23, color=GOLD),
            label_box("② 圆心角 = 360° × 百分比", size=23, color=CHALK),
            label_box("③ 求部分人数 = 总数 × 百分比", size=23, color=GREEN),
        ).arrange(DOWN, buff=0.2).move_to([0, -1.65, 0])
        for r in rows:
            self.play(FadeIn(r, shift=RIGHT * 0.06), run_time=0.6)
            self.wait(0.5)

        self.wait(1.0)
        self.finish_section()

    def construct(self):
        self.scene_story()
        self.clear_stage()
        self.scene_meaning()
        self.clear_stage()
        self.scene_read()
        self.clear_stage()
        self.scene_angle()
        self.clear_stage()
        self.scene_example()
        self.clear_stage()
        self.scene_kinds()
        self.clear_stage()
        self.scene_warn()
        self.clear_stage(0.8)