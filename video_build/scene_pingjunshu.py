# -*- coding: utf-8 -*-
"""平均数、中位数、众数：三个统计量的算法、适用场景与易错点。七年级下。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


def P(x, y):
    return np.array([float(x), float(y), 0.0])


def bars(values, base_y, x0, bw=0.62, gap=0.42, scale=0.36, color=BLUE,
         max_h=None):
    """在 base_y 上画一排柱子，返回值柱组与柱宽。"""
    g = VGroup()
    for i, v in enumerate(values):
        h = v * scale
        if max_h is not None:
            h = min(h, max_h)
        x = x0 + i * (bw + gap)
        r = Rectangle(width=bw, height=max(h, 0.06), stroke_width=2,
                      stroke_color=color, fill_color=color, fill_opacity=0.28)
        r.move_to([x + bw / 2, base_y + h / 2, 0])
        g.add(r)
    return g


class PingjunshuScene(NarratedScene):
    lesson = "pingjunshu"

    def clear_stage(self, run_time: float = 0.5):
        keep = {id(self._track), id(self._fill)}
        junk = [m for m in self.mobjects if id(m) not in keep]
        if junk:
            self.play(*[FadeOut(m) for m in junk], run_time=run_time)
        self.cur_title = None
        self.cur_sub = None

    # ---------------- 0. 三个数，三种眼光 ---------------- 24.7
    def scene_intro(self):
        self.section(0, "三个数，三种眼光")

        rows = [
            ("考试分数", "平均分", [1.0, 0.78, 0.92, 0.7, 1.15], GOLD),
            ("鞋码销量", "众数", [0.5, 1.15, 1.2, 0.45, 0.35], ORANGE),
            ("身高排队", "中位数", [0.6, 0.8, 1.0, 1.25, 1.45], GREEN),
        ]
        y = 1.55
        for label, name, vals, col in rows:
            b = bars(vals, y - 0.55, -6.55, bw=0.4, gap=0.16,
                     scale=0.5, color=col)
            self.play(LaggedStart(*[GrowFromEdge(r, DOWN) for r in b],
                                  lag_ratio=0.12), run_time=1.3)
            lb = txt(label, size=26, color=CHALK).move_to([-3.55, y - 0.18, 0])
            ar = txt("→", size=26, color=DIM).move_to([-1.75, y - 0.18, 0])
            nm = label_box(name, size=28, color=col).move_to([0.55, y - 0.18, 0])
            self.play(FadeIn(lb, shift=RIGHT * 0.05), run_time=0.6)
            self.play(FadeIn(ar, shift=RIGHT * 0.05), run_time=0.4)
            self.play(FadeIn(nm, scale=0.97), run_time=0.7)
            desc = txt(self._desc(name), size=24, color=DIM).move_to([4.6, y - 0.18, 0])
            self.play(FadeIn(desc, shift=RIGHT * 0.05), run_time=0.6)
            y -= 1.42

        note = txt("都在描述一组数据，但看的角度不一样", size=27, color=CHALK)
        note.move_to([0, -2.85, 0])
        self.play(FadeIn(note, shift=UP * 0.05), run_time=1.0)
        self.wait(3.0)
        self.finish_section()

    @staticmethod
    def _desc(name):
        return {"平均分": "算总分再分", "众数": "出现最多",
                "中位数": "排中间的"}[name]

    # ---------------- 1. 平均数怎么算 ---------------- 27.9
    def scene_mean(self):
        self.section(1, "平均数：加起来再除")

        data = ["1.5", "1.6", "1.6", "1.7"]
        boxes = VGroup()
        for i, d in enumerate(data):
            bx = Rectangle(width=1.35, height=1.0, stroke_width=2,
                           stroke_color=BLUE, fill_color=BLUE, fill_opacity=0.12)
            bx.move_to([-4.6 + i * 1.65, 1.95, 0])
            boxes.add(VGroup(bx, txt(d + " m", size=26, color=CHALK).move_to(bx)))
        self.play(LaggedStart(*[FadeIn(b, scale=0.94) for b in boxes],
                              lag_ratio=0.12), run_time=1.4)
        cap = txt("四个人的身高", size=24, color=DIM).move_to([-2.1, 1.1, 0])
        self.play(FadeIn(cap), run_time=0.6)

        s1 = VGroup(
            txt("1.5 + 1.6 + 1.6 + 1.7", size=28, color=CHALK),
            txt("=", size=28, color=DIM),
            txt("6.4", size=28, color=GOLD),
        ).arrange(RIGHT, buff=0.24).move_to([-1.5, 0.05, 0])
        self.play(FadeIn(s1, shift=UP * 0.05), run_time=0.9)

        s2 = VGroup(
            txt("6.4 ÷ 4", size=30, color=CHALK),
            txt("=", size=30, color=DIM),
            txt("1.6", size=34, color=GREEN),
        ).arrange(RIGHT, buff=0.24).move_to([-1.5, -1.05, 0])
        self.play(FadeIn(s2, shift=UP * 0.05), run_time=0.9)

        note = txt("平均数 = 所有数据之和 ÷ 数据个数", size=26, color=CHALK)
        note.move_to([2.4, 1.9, 0])
        self.play(FadeIn(note, shift=UP * 0.05), run_time=0.9)

        w = label_box("加权平均数：成绩×0.6 + 平时×0.4", size=25, color=BLUE)
        w.move_to([2.4, 0.55, 0])
        self.play(FadeIn(w, scale=0.97), run_time=1.0)

        note2 = txt("数据有轻有重，就按权重乘一乘", size=24, color=DIM)
        note2.move_to([2.4, -0.5, 0])
        self.play(FadeIn(note2, shift=UP * 0.05), run_time=0.8)

        tail = txt("优点：每个数据都参与了计算", size=25, color=GREEN)
        tail.move_to([0, -2.55, 0])
        self.play(FadeIn(tail, shift=UP * 0.05), run_time=0.9)
        self.wait(2.6)
        self.finish_section()

    # ---------------- 2. 平均数怕极端值 ---------------- 22.6
    def scene_outlier(self):
        self.section(2, "平均数怕极端值")

        vals = [10, 10, 10, 10, 100]
        g = bars(vals, -2.0, -4.6, bw=0.7, gap=0.5, scale=0.024, color=BLUE)
        self.play(LaggedStart(*[GrowFromEdge(r, DOWN) for r in g],
                              lag_ratio=0.14), run_time=1.6)
        base = Line(P(-5.0, -2.0), P(1.8, -2.0), color=DIM, stroke_width=2)
        self.play(Create(base), run_time=0.5)

        labs = VGroup()
        for i, v in enumerate(vals):
            labs.add(txt(str(v), size=22, color=CHALK)
                     .move_to([-4.25 + i * 1.2, -2.32, 0]))
        self.play(FadeIn(labs), run_time=0.7)

        big = txt("一个人 100 元", size=24, color=ORANGE).move_to([0.3, 1.35, 0])
        self.play(FadeIn(big, shift=UP * 0.05), run_time=0.7)

        mline = DashedLine(P(-5.0, -1.33), P(1.9, -1.33), color=ORANGE,
                           stroke_width=2.4, dash_length=0.14)
        mlab = txt("平均数 28", size=25, color=ORANGE).move_to([3.6, -1.33, 0])
        self.play(Create(mline), run_time=0.9)
        self.play(FadeIn(mlab, shift=RIGHT * 0.05), run_time=0.7)

        tline = DashedLine(P(-5.0, -1.76), P(1.9, -1.76), color=GREEN,
                           stroke_width=2.4, dash_length=0.14)
        tlab = txt("大多数人 10", size=25, color=GREEN).move_to([3.8, -1.76, 0])
        self.play(Create(tline), run_time=0.8)
        self.play(FadeIn(tlab, shift=RIGHT * 0.05), run_time=0.7)

        note = txt("被那个特别大的数拉偏了，代表不了大多数人", size=26, color=CHALK)
        note.move_to([0, -2.95, 0])
        self.play(FadeIn(note, shift=UP * 0.05), run_time=1.0)
        self.wait(2.6)
        self.finish_section()

    # ---------------- 3. 中位数：排好队取中间 ---------------- 30.5
    def scene_median(self):
        self.section(3, "中位数：排好队，取中间")

        raw = ["100", "10", "10", "10", "10"]
        row = VGroup()
        for i, v in enumerate(raw):
            row.add(txt(v, size=28, color=CHALK).move_to([-4.4 + i * 1.5, 2.15, 0]))
        self.play(FadeIn(row), run_time=0.9)
        l0 = txt("原数据", size=23, color=DIM).move_to([-6.35, 2.15, 0])
        self.play(FadeIn(l0), run_time=0.5)

        order = ["10", "10", "10", "10", "100"]
        row2 = VGroup()
        for i, v in enumerate(order):
            row2.add(txt(v, size=28, color=CHALK).move_to([-4.4 + i * 1.5, 1.1, 0]))
        l1 = txt("从小到大排好", size=23, color=DIM).move_to([-6.9, 1.1, 0])
        a1 = txt("① 先排序", size=24, color=GOLD).move_to([4.9, 2.15, 0])
        self.play(FadeIn(l1, shift=RIGHT * 0.05), run_time=0.6)
        self.play(FadeIn(row2, shift=UP * 0.05), run_time=1.0)
        self.play(FadeIn(a1, shift=RIGHT * 0.05), run_time=0.7)

        hl = SurroundingRectangle(row2[2], color=GOLD, buff=0.22,
                                  stroke_width=2.6)
        a2 = txt("② 取正中间那个", size=24, color=GOLD).move_to([4.9, 0.55, 0])
        self.play(Create(hl), run_time=0.8)
        self.play(FadeIn(a2, shift=RIGHT * 0.05), run_time=0.7)

        ev = txt("偶数个数据：中间有两个，取它们的平均数", size=26, color=CHALK)
        ev.move_to([0, -0.35, 0])
        self.play(FadeIn(ev, shift=UP * 0.05), run_time=0.9)

        six = ["2", "3", "5", "7", "9", "12"]
        row3 = VGroup()
        for i, v in enumerate(six):
            row3.add(txt(v, size=28, color=CHALK).move_to([-4.2 + i * 1.45, -1.35, 0]))
        self.play(FadeIn(row3), run_time=0.9)
        m1 = SurroundingRectangle(row3[2], color=BLUE, buff=0.18, stroke_width=2.4)
        m2 = SurroundingRectangle(row3[3], color=BLUE, buff=0.18, stroke_width=2.4)
        self.play(Create(m1), Create(m2), run_time=0.9)

        res = VGroup(
            txt("(5 + 7) ÷ 2", size=28, color=CHALK),
            txt("=", size=28, color=DIM),
            txt("6", size=32, color=GREEN),
        ).arrange(RIGHT, buff=0.22).move_to([3.7, -1.35, 0])
        self.play(FadeIn(res, shift=UP * 0.05), run_time=0.9)

        note = txt("中位数不受极端值影响，位置在中间就稳", size=25, color=GREEN)
        note.move_to([0, -2.75, 0])
        self.play(FadeIn(note, shift=UP * 0.05), run_time=0.9)
        self.wait(2.8)
        self.finish_section()

    # ---------------- 4. 众数：出现最多的 ---------------- 26.3
    def scene_mode(self):
        self.section(4, "众数：出现次数最多的")

        vals = ["10", "10", "10", "10", "100"]
        row = VGroup()
        for i, v in enumerate(vals):
            row.add(txt(v, size=30, color=CHALK).move_to([-4.3 + i * 1.55, 1.75, 0]))
        self.play(FadeIn(row), run_time=0.9)

        ticks = VGroup()
        for i in range(4):
            ticks.add(Line(P(-4.35 + i * 1.55, 1.25), P(-4.25 + i * 1.55, 1.35),
                           color=GOLD, stroke_width=3))
        self.play(LaggedStart(*[Create(t) for t in ticks], lag_ratio=0.1),
                  run_time=1.2)
        cnt = txt("出现 4 次", size=26, color=GOLD).move_to([0.6, 1.3, 0])
        self.play(FadeIn(cnt, shift=RIGHT * 0.05), run_time=0.7)

        res = VGroup(
            txt("众数", size=30, color=DIM),
            txt("=", size=30, color=DIM),
            txt("10", size=34, color=GREEN),
        ).arrange(RIGHT, buff=0.22).move_to([2.6, 2.6, 0])
        self.play(FadeIn(res, shift=UP * 0.05), run_time=0.9)

        t1 = VGroup(
            txt("出现次数最多的那个数", size=26, color=CHALK),
            txt("可以不止一个：两个并列最多，就都是众数", size=24, color=BLUE),
            txt("也可能没有：每个数都只出现一次", size=24, color=ORANGE),
        ).arrange(DOWN, buff=0.32, aligned_edge=LEFT).move_to([0.2, -0.35, 0])
        for m in t1:
            self.play(FadeIn(m, shift=UP * 0.05), run_time=0.8)

        note = txt("鞋店进货看尺码的众数，因为它最畅销", size=26, color=CHALK)
        note.move_to([0, -2.6, 0])
        self.play(FadeIn(note, shift=UP * 0.05), run_time=0.9)
        self.wait(2.6)
        self.finish_section()

    # ---------------- 5. 三个数怎么选 ---------------- 25.9
    def scene_choose(self):
        self.section(5, "三个数，怎么选")

        head = txt("看数据长什么样，再决定用哪个", size=27, color=CHALK)
        head.move_to([0, 2.4, 0])
        self.play(FadeIn(head, shift=UP * 0.05), run_time=0.9)

        cards = [
            ("平均数", "数据整齐、没有极端值", "信息用得最全", GOLD),
            ("中位数", "有极端值、只看中间水平", "稳定，不被拉偏", GREEN),
            ("众数", "关心哪种最常见、最畅销", "看出现次数", ORANGE),
        ]
        x = -4.55
        for name, cond, why, col in cards:
            box = RoundedRectangle(width=4.1, height=3.2, corner_radius=0.18,
                                   stroke_width=2.2, stroke_color=col,
                                   fill_color=col, fill_opacity=0.08)
            box.move_to([x, -0.35, 0])
            self.play(Create(box), run_time=0.8)
            nm = label_box(name, size=30, color=col).move_to([x, 0.95, 0])
            self.play(FadeIn(nm, scale=0.97), run_time=0.7)
            c1 = txt(cond, size=24, color=CHALK).move_to([x, 0.05, 0])
            self.play(FadeIn(c1, shift=UP * 0.05), run_time=0.7)
            c2 = txt(why, size=23, color=DIM).move_to([x, -0.75, 0])
            self.play(FadeIn(c2, shift=UP * 0.05), run_time=0.7)
            x += 4.55

        note = txt("题目问「谁更能代表」，通常就在问有没有极端值", size=25, color=CHALK)
        note.move_to([0, -2.85, 0])
        self.play(FadeIn(note, shift=UP * 0.05), run_time=1.0)
        self.wait(2.8)
        self.finish_section()

    # ---------------- 6. 例题与三个易错点 ---------------- 29.1
    def scene_ex(self):
        self.section(6, "例题与三个易错点")

        q = txt("五次成绩：70、75、80、85、95", size=27, color=CHALK)
        q.move_to([0, 2.4, 0])
        self.play(FadeIn(q, shift=UP * 0.05), run_time=0.9)

        r1 = VGroup(
            txt("平均数", size=26, color=GOLD),
            txt("(70+75+80+85+95) ÷ 5 = 81", size=26, color=CHALK),
        ).arrange(RIGHT, buff=0.3).move_to([0, 1.35, 0])
        self.play(FadeIn(r1, shift=RIGHT * 0.05), run_time=0.9)

        r2 = VGroup(
            txt("中位数", size=26, color=GREEN),
            txt("正中间是 80", size=26, color=CHALK),
        ).arrange(RIGHT, buff=0.3).move_to([0, 0.6, 0])
        self.play(FadeIn(r2, shift=RIGHT * 0.05), run_time=0.9)

        r3 = VGroup(
            txt("众数", size=26, color=ORANGE),
            txt("没有（每个数只出现一次）", size=26, color=CHALK),
        ).arrange(RIGHT, buff=0.3).move_to([0, -0.15, 0])
        self.play(FadeIn(r3, shift=RIGHT * 0.05), run_time=0.9)

        items = [
            ("求中位数不排序", "先从小到大排"),
            ("偶数个只取一个中间数", "取两个的平均"),
            ("以为众数只能有一个", "可多个，也可没有"),
        ]
        y = -1.15
        for bad_s, good_s in items:
            bad = txt(bad_s, size=24, color=RED).move_to([-3.0, y, 0])
            good = txt(good_s, size=23, color=GREEN).move_to([3.7, y, 0])
            cross = Line([bad.get_left()[0] - 0.07, y - 0.07, 0],
                         [bad.get_right()[0] + 0.07, y - 0.07, 0],
                         color=RED, stroke_width=2.2)
            self.play(FadeIn(bad, shift=RIGHT * 0.05), run_time=0.55)
            self.play(Create(cross), run_time=0.35)
            self.play(FadeIn(good, shift=RIGHT * 0.05), run_time=0.55)
            y -= 0.72

        self.wait(2.8)
        self.finish_section()

    def construct(self):
        self.scene_intro()
        self.clear_stage()
        self.scene_mean()
        self.clear_stage()
        self.scene_outlier()
        self.clear_stage()
        self.scene_median()
        self.clear_stage()
        self.scene_mode()
        self.clear_stage()
        self.scene_choose()
        self.clear_stage()
        self.scene_ex()
        self.clear_stage(0.8)