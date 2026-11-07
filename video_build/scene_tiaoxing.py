# -*- coding: utf-8 -*-
"""条形统计图：横轴、纵轴、直条，一格代表几人。二年级下册。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403

Y0 = -2.0
X_L = -5.5
X_R = 3.0
CAT_X = [-4.6, -2.3, 0.0, 2.3]
NAMES = ["苹果", "香蕉", "橘子", "葡萄"]
COUNTS = [8, 4, 6, 2]
COLORS = [RED, GOLD, ORANGE, GREEN]


def axes(max_v=8, unit=0.5, tick_step=1, label_of=None) -> VGroup:
    """坐标系：原点左下，横轴、纵轴、刻度和刻度数字。"""
    g = VGroup()
    g.add(Line([X_L, Y0, 0], [X_R, Y0, 0], color=CHALK, stroke_width=3))
    g.add(Line([X_L, Y0, 0], [X_L, Y0 + max_v * unit + 0.4, 0], color=CHALK, stroke_width=3))
    # 箭头
    g.add(Arrow([X_R - 0.5, Y0, 0], [X_R, Y0, 0], color=CHALK, stroke_width=3, buff=0,
                max_tip_length_to_length_ratio=0.5))
    g.add(Arrow([X_L, Y0 + max_v * unit, 0], [X_L, Y0 + max_v * unit + 0.4, 0],
                color=CHALK, stroke_width=3, buff=0, max_tip_length_to_length_ratio=0.5))

    for v in range(0, max_v + 1, tick_step):
        y = Y0 + v * unit
        g.add(Line([X_L - 0.08, y, 0], [X_L + 0.08, y, 0], color=CHALK, stroke_width=2))
        label = label_of(v) if label_of else str(v)
        g.add(txt(label, size=20, color=DIM).move_to([X_L - 0.42, y, 0]))
    return g


def category_labels() -> VGroup:
    g = VGroup()
    for x, name in zip(CAT_X, NAMES):
        g.add(txt(name, size=26, color=CHALK).move_to([x, Y0 - 0.42, 0]))
    return g


def bars(unit=0.5, counts=None) -> VGroup:
    counts = counts or COUNTS
    g = VGroup()
    for x, n, color in zip(CAT_X, counts, COLORS):
        g.add(Rectangle(width=1.45, height=n * unit, color=color, stroke_width=2,
                        fill_color=color, fill_opacity=0.55)
              .align_to([0, Y0, 0], DOWN).move_to([x, Y0 + n * unit / 2, 0]))
    return g


def bar_labels(unit=0.5, counts=None) -> VGroup:
    counts = counts or COUNTS
    g = VGroup()
    for x, n, color in zip(CAT_X, counts, COLORS):
        g.add(txt(str(n), size=26, color=color).move_to([x, Y0 + n * unit + 0.28, 0]))
    return g


class TiaoxingScene(NarratedScene):
    lesson = "tiaoxing-tongji"

    def clear_stage(self, run_time: float = 0.5):
        keep = {id(self._track), id(self._fill)}
        junk = [m for m in self.mobjects if id(m) not in keep]
        if junk:
            self.play(*[FadeOut(m) for m in junk], run_time=run_time)
        self.cur_title = None
        self.cur_sub = None

    # ---------------- 0. 投票 ----------------
    def scene_vote(self):
        self.section(0, "先投票：四种水果")

        cards = VGroup()
        for i, (name, color) in enumerate(zip(NAMES, COLORS)):
            box = RoundedRectangle(corner_radius=0.14, width=1.8, height=1.1,
                                   stroke_color=color, stroke_width=2.4,
                                   fill_color=color, fill_opacity=0.1)
            t = txt(name, size=32, color=color).move_to(box)
            cards.add(VGroup(box, t))
        cards.arrange(RIGHT, buff=1.1).move_to([0, 1.2, 0])
        self.play(LaggedStart(*[FadeIn(c, shift=UP * 0.1) for c in cards], lag_ratio=0.15),
                  run_time=1.4)

        q = txt("每人选一种，票怎么数才清楚？", size=34, color=CHALK).move_to([0, -0.9, 0])
        self.play(FadeIn(q, shift=UP * 0.08), run_time=0.7)

        hint = txt("一票画一个圈，五个一排", size=26, color=DIM).move_to([0, -1.85, 0])
        self.play(FadeIn(hint), run_time=0.6)
        self.finish_section()

    # ---------------- 1. 数票 ----------------
    def scene_count(self):
        self.section(1, "数一数：8、4、6、2")

        rows = VGroup()
        ys = [1.9, 0.85, -0.2, -1.25]
        for name, n, color, y in zip(NAMES, COUNTS, COLORS, ys):
            row = VGroup()
            row.add(txt(name, size=28, color=color).move_to([-5.4, y, 0]))
            dots = VGroup()
            for k in range(n):
                dots.add(Dot([-3.9 + k * 0.4, y, 0], radius=0.1, color=color))
            row.add(dots)
            row.add(txt(str(n), size=32, color=color).move_to([0.9, y, 0]))
            rows.add(row)

        for row in rows:
            self.play(FadeIn(row[0]), run_time=0.25)
            self.play(LaggedStart(*[GrowFromCenter(d) for d in row[1]], lag_ratio=0.08),
                      run_time=0.5)
            self.play(FadeIn(row[2], shift=LEFT * 0.06), run_time=0.25)

        tip = txt("数票的结果，就是统计图里的数据", size=26, color=GREEN).move_to([2.9, -2.2, 0])
        self.play(FadeIn(tip, shift=UP * 0.06), run_time=0.6)
        self.finish_section()

    # ---------------- 2. 认识横轴纵轴 ----------------
    def scene_axes(self):
        self.section(2, "横轴写水果，纵轴写人数")

        ax = axes()
        self.play(Create(ax[0]), Create(ax[1]), run_time=0.8)
        self.play(Create(ax[2]), Create(ax[3]), run_time=0.4)
        self.play(FadeIn(ax[4:]), run_time=0.7)

        cats = category_labels()
        self.play(LaggedStart(*[FadeIn(c) for c in cats], lag_ratio=0.12), run_time=0.8)

        x_lab = txt("水果", size=24, color=DIM).move_to([3.9, -2.42, 0])
        y_lab = txt("人数", size=24, color=DIM).move_to([-5.0, 2.55, 0])
        self.play(FadeIn(x_lab), FadeIn(y_lab), run_time=0.5)

        note = txt("每一小格代表 1 人", size=27, color=GOLD).move_to([4.7, 1.4, 0])
        self.play(FadeIn(note, shift=UP * 0.06), run_time=0.6)
        self.finish_section()

    # ---------------- 3. 三步画直条 ----------------
    def scene_draw(self):
        self.section(3, "三步画出直条")

        ax = axes()
        cats = category_labels()
        self.play(FadeIn(ax), FadeIn(cats), run_time=1.0)

        steps = VGroup(
            label_box("① 定刻度", size=25, color=CHALK),
            label_box("② 画直条", size=25, color=GOLD),
            label_box("③ 标数字", size=25, color=CHALK),
        ).arrange(RIGHT, buff=0.4).move_to([4.0, 2.85, 0])
        self.play(FadeIn(steps[0]), run_time=0.4)

        b = bars()
        for i, rect in enumerate(b):
            self.play(GrowFromEdge(rect, DOWN), run_time=0.22)
        self.play(FadeIn(steps[1]), run_time=0.3)

        labs = bar_labels()
        self.play(LaggedStart(*[FadeIn(l, shift=UP * 0.05) for l in labs], lag_ratio=0.12),
                  run_time=0.8)
        self.play(FadeIn(steps[2]), run_time=0.35)
        self.finish_section()

    # ---------------- 4. 读图 ----------------
    def scene_read(self):
        self.section(4, "读图：最多、最少、相差、合计")

        ax = axes()
        cats = category_labels()
        b = bars()
        labs = bar_labels()
        self.play(FadeIn(ax), FadeIn(cats), run_time=0.9)
        self.play(LaggedStart(*[GrowFromEdge(r, DOWN) for r in b], lag_ratio=0.1),
                  run_time=1.0)
        self.play(FadeIn(labs), run_time=0.5)

        most = txt("最多：苹果 8 人", size=28, color=RED).move_to([4.9, 2.35, 0])
        least = txt("最少：葡萄 2 人", size=28, color=GREEN).move_to([4.9, 1.6, 0])
        self.play(FadeIn(most, shift=UP * 0.06), run_time=0.5)
        self.play(FadeIn(least, shift=UP * 0.06), run_time=0.5)

        diff = txt("苹果比香蕉多 4 人", size=28, color=GOLD).move_to([4.9, 0.85, 0])
        self.play(FadeIn(diff, shift=UP * 0.06), run_time=0.5)
        self.play(Indicate(b[0], color=RED, scale_factor=1.04),
                  Indicate(b[1], color=GOLD, scale_factor=1.04), run_time=0.6)

        total = txt("8 + 4 + 6 + 2 = 20（票）", size=24, color=CHALK).move_to([4.9, 0.1, 0])
        self.play(FadeIn(total, shift=UP * 0.06), run_time=0.7)
        self.finish_section()

    # ---------------- 5. 一格代表 2 人 ----------------
    def scene_unit2(self):
        self.section(5, "一格也可以代表 2 人")

        ax = axes(max_v=8, unit=0.25, tick_step=2, label_of=lambda v: str(v // 2))
        cats = category_labels()
        self.play(FadeIn(ax), FadeIn(cats), run_time=1.0)

        y_lab = txt("格数", size=24, color=DIM).move_to([-5.0, 2.55, 0])
        self.play(FadeIn(y_lab), run_time=0.4)

        note = txt("1 格 = 2 人", size=30, color=GOLD).move_to([4.8, 2.45, 0])
        self.play(FadeIn(note, shift=UP * 0.06), run_time=0.5)

        b = bars(unit=0.25, counts=COUNTS)
        self.play(LaggedStart(*[GrowFromEdge(r, DOWN) for r in b], lag_ratio=0.12),
                  run_time=1.1)

        labs = VGroup()
        for x, n, color in zip(CAT_X, COUNTS, COLORS):
            y = Y0 + n * 0.25 + 0.27
            labs.add(txt(f"{n} 人", size=24, color=color).move_to([x, y, 0]))
        self.play(FadeIn(labs), run_time=0.6)

        calc = txt("苹果占 4 格：4 × 2 = 8 人", size=26, color=CHALK).move_to([4.8, 1.75, 0])
        self.play(FadeIn(calc, shift=UP * 0.06), run_time=0.6)

        warn = txt("先读格数，再乘 2", size=27, color=GREEN).move_to([4.8, 1.05, 0])
        self.play(FadeIn(warn), run_time=0.5)
        self.finish_section()

    # ---------------- 6. 五要素 ----------------
    def scene_summary(self):
        self.section(6, "一幅完整的统计图，五样齐全")

        items = ["标题", "横轴", "纵轴", "直条", "数据"]
        boxes = VGroup()
        for i, name in enumerate(items):
            color = GOLD if i == 4 else CHALK
            boxes.add(label_box(name, size=30, color=color))
        boxes.arrange(RIGHT, buff=0.45).move_to([0, 1.15, 0])
        self.play(LaggedStart(*[FadeIn(b, shift=UP * 0.08) for b in boxes], lag_ratio=0.18),
                  run_time=1.2)

        big = txt("标题、横轴、纵轴、直条、数据", size=36, color=GOLD).move_to([0, -0.2, 0])
        self.play(Write(big), run_time=1.0)

        tip = txt("缺一样，别人就看不懂你的图", size=28, color=GREEN).move_to([0, -1.45, 0])
        self.play(FadeIn(tip, shift=UP * 0.08), run_time=0.7)
        self.finish_section()

    def construct(self):
        self.scene_vote()
        self.clear_stage()
        self.scene_count()
        self.clear_stage()
        self.scene_axes()
        self.clear_stage()
        self.scene_draw()
        self.clear_stage()
        self.scene_read()
        self.clear_stage()
        self.scene_unit2()
        self.clear_stage()
        self.scene_summary()
        self.clear_stage(0.8)