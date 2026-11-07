# -*- coding: utf-8 -*-
"""数据收集与整理：全面调查与抽样、总体样本、划记法与频率、统计图选择。七年级上。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


def place(g, x, y):
    """左边缘对齐 x，竖直中心落在 y。"""
    g.move_to([0, 0, 0])
    g.shift(RIGHT * (x - g.get_left()[0]) + UP * (y - g.get_center()[1]))
    return g


def pie_slice(cx, cy, r, a0, a1, color, opacity=0.45, stroke=2.0, steps=28):
    """手工拼扇形（Sector 在本机渲染异常，改用多边近似）。角度用「度」。"""
    pts = []
    for i in range(steps + 1):
        a = np.radians(a0 + (a1 - a0) * i / steps)
        pts.append(np.array([cx + r * np.cos(a), cy + r * np.sin(a), 0.0]))
    pts.append(np.array([cx, cy, 0.0]))
    return Polygon(*pts, color=color, stroke_width=stroke,
                   fill_color=color, fill_opacity=opacity)


class ShujuShoujiScene(NarratedScene):
    lesson = "shuju-shouji"

    def clear_stage(self, run_time: float = 0.5):
        keep = {id(self._track), id(self._fill)}
        junk = [m for m in self.mobjects if id(m) not in keep]
        if junk:
            self.play(*[FadeOut(m) for m in junk], run_time=run_time)
        self.cur_title = None
        self.cur_sub = None

    # ---------------- 0. 运动会投票 ---------------- 13.6
    def scene_story(self):
        self.section(0, "先问一问，才有数据")

        box = RoundedRectangle(corner_radius=0.14, width=1.9, height=1.7,
                               stroke_color=GOLD, stroke_width=2.2,
                               fill_color=GOLD, fill_opacity=0.1).move_to([-4.7, 0.55, 0])
        slot = Line([-5.35, 1.2, 0], [-4.05, 1.2, 0], color=GOLD, stroke_width=3)
        blab = txt("投票箱", size=25, color=GOLD).move_to([-4.7, -0.75, 0])
        self.play(Create(box), run_time=0.9)
        self.play(Create(slot), run_time=0.5)
        self.play(FadeIn(blab, shift=UP * 0.05), run_time=0.6)

        q = txt("运动会，大家最喜欢哪个项目？", size=30, color=CHALK).move_to([0, 2.35, 0])
        self.play(FadeIn(q, shift=UP * 0.05), run_time=0.8)

        cards = VGroup(
            label_box("跑步", size=27, color=ORANGE),
            label_box("跳绳", size=27, color=GREEN),
            label_box("篮球", size=27, color=BLUE),
        ).arrange(RIGHT, buff=0.45).move_to([1.6, 1.35, 0])
        for c in cards:
            self.play(FadeIn(c, scale=0.95), run_time=0.55)

        one = txt("每人只投一票，票数就是数据", size=27, color=CHALK).move_to([1.6, 0.05, 0])
        self.play(FadeIn(one, shift=UP * 0.05), run_time=0.8)

        warn = txt("光靠猜不行，得去问", size=28, color=GOLD).move_to([0, -1.55, 0])
        self.play(FadeIn(warn, shift=UP * 0.05), run_time=0.8)

        tail = txt("问的过程，就是收集数据", size=26, color=DIM).move_to([0, -2.25, 0])
        self.play(FadeIn(tail, shift=UP * 0.05), run_time=0.7)
        self.wait(2.6)
        self.finish_section()

    # ---------------- 1. 收集数据的方法 ---------------- 13.4
    def scene_methods(self):
        self.section(1, "收集数据的方法")

        chips = VGroup(*[label_box(s, size=25, color=c) for s, c in (
            ("问卷调查", GOLD), ("举手投票", BLUE), ("实地观察", GREEN),
            ("查阅资料", PURPLE), ("做试验", ORANGE),
        )]).arrange(RIGHT, buff=0.3).move_to([0, 1.75, 0])
        for c in chips:
            self.play(FadeIn(c, scale=0.96), run_time=0.45)
        self.wait(0.3)

        a = Arrow([-2.0, 1.2, 0], [-2.0, 0.55, 0], color=DIM, buff=0.02,
                  stroke_width=2.6, max_tip_length_to_length_ratio=0.3)
        self.play(Create(a), run_time=0.5)

        full = label_box("把每一个都问到", size=30, color=GOLD).move_to([-2.4, 0.1, 0])
        self.play(FadeIn(full, scale=0.96), run_time=0.9)

        ar1 = Arrow(full.get_right() + RIGHT * 0.15, full.get_right() + RIGHT * 1.35,
                    color=GOLD, buff=0, stroke_width=2.6,
                    max_tip_length_to_length_ratio=0.3)
        fname = txt("全面调查", size=33, color=GREEN).next_to(ar1, RIGHT, buff=0.25)
        self.play(Create(ar1), FadeIn(fname, shift=RIGHT * 0.05), run_time=0.8)

        b = Arrow([-2.4, -0.55, 0], [-2.4, -1.15, 0], color=DIM, buff=0.02,
                  stroke_width=2.6, max_tip_length_to_length_ratio=0.3)
        self.play(Create(b), run_time=0.5)

        part = label_box("人太多，只抽一部分", size=30, color=BLUE).move_to([-2.4, -1.6, 0])
        self.play(FadeIn(part, scale=0.96), run_time=0.9)

        ar2 = Arrow(part.get_right() + RIGHT * 0.15, part.get_right() + RIGHT * 1.35,
                    color=BLUE, buff=0, stroke_width=2.6,
                    max_tip_length_to_length_ratio=0.3)
        pname = txt("抽样调查", size=33, color=BLUE).next_to(ar2, RIGHT, buff=0.25)
        self.play(Create(ar2), FadeIn(pname, shift=RIGHT * 0.05), run_time=0.8)

        note = txt("能问到每一个，就别抽样", size=26, color=DIM).move_to([0, -2.45, 0])
        self.play(FadeIn(note, shift=UP * 0.05), run_time=0.7)
        self.wait(1.6)
        self.finish_section()

    # ---------------- 2. 总体、个体、样本 ---------------- 13.2
    def scene_sample(self):
        self.section(2, "总体、个体、样本")

        outer = Rectangle(width=4.5, height=2.5, color=DIM, stroke_width=2)
        outer.move_to([-3.6, 0.45, 0])
        self.play(Create(outer), run_time=0.9)

        dots = VGroup()
        for r in range(3):
            for c in range(6):
                dots.add(Dot([-5.45 + c * 0.75, -0.35 + r * 0.8, 0], radius=0.065, color=DIM))
        self.play(LaggedStart(*[FadeIn(d, scale=0.6) for d in dots], lag_ratio=0.04), run_time=1.4)

        sample_box = Rectangle(width=2.0, height=1.55, color=GOLD, stroke_width=2.4)
        sample_box.move_to([-4.55, 0.45, 0])
        self.play(Create(sample_box), run_time=0.8)

        t1 = txt("总体：全班 40 人", size=25, color=CHALK).move_to([-3.6, -1.1, 0])
        t2 = txt("样本：抽到的 6 人", size=25, color=GOLD).move_to([-3.6, -1.7, 0])
        self.play(FadeIn(t1, shift=UP * 0.05), run_time=0.7)
        self.play(FadeIn(t2, shift=UP * 0.05), run_time=0.7)

        rows = VGroup(
            txt("总体：要考察的全体", size=26, color=CHALK),
            txt("个体：其中每一个对象", size=26, color=CHALK),
            txt("样本：被抽取的一部分", size=26, color=GOLD),
            txt("样本容量：样本中个体的数目", size=26, color=BLUE),
        ).arrange(DOWN, buff=0.42, aligned_edge=LEFT).move_to([2.9, 1.15, 0])
        for r in rows:
            self.play(FadeIn(r, shift=RIGHT * 0.05), run_time=0.6)

        note = txt("样本容量只是一个数，不带单位", size=26, color=RED).move_to([2.9, -1.35, 0])
        self.play(FadeIn(note, shift=UP * 0.05), run_time=0.7)
        self.wait(1.4)
        self.finish_section()

    # ---------------- 3. 划记法、频数、频率 ---------------- 14.7
    def scene_tally(self):
        self.section(3, "划记法：数清每一个")

        heads = ["项目", "划记", "频数"]
        cols = [-4.9, -1.6, 1.7]
        for h, x in zip(heads, cols):
            self.play(FadeIn(txt(h, size=27, color=GOLD).move_to([x, 1.95, 0]),
                             shift=UP * 0.05), run_time=0.45)

        rows = [("跑步", "正||", "7"), ("跳绳", "正", "5"), ("篮球", "正|||", "8")]
        y = 1.1
        for name, tally, num in rows:
            line = VGroup(
                txt(name, size=27, color=CHALK).move_to([cols[0], y, 0]),
                txt(tally, size=29, color=BLUE).move_to([cols[1], y, 0]),
                txt(num, size=29, color=GREEN).move_to([cols[2], y, 0]),
            )
            self.play(FadeIn(line, shift=UP * 0.05), run_time=0.7)
            y -= 0.72

        total = VGroup(
            txt("合计", size=26, color=DIM).move_to([cols[0], y, 0]),
            txt("20", size=28, color=DIM).move_to([cols[2], y, 0]),
        )
        self.play(FadeIn(total, shift=UP * 0.05), run_time=0.6)

        form = label_box("频率 = 频数 ÷ 总数", size=29, color=GOLD).move_to([0, -1.75, 0])
        self.play(FadeIn(form, scale=0.96), run_time=0.9)

        ex = txt("跑步：7 ÷ 20 = 0.35", size=26, color=CHALK).move_to([0, -2.4, 0])
        self.play(FadeIn(ex, shift=UP * 0.05), run_time=0.7)

        note = txt("频数是次数，频率是比值", size=25, color=DIM).move_to([0, -2.95, 0])
        self.play(FadeIn(note, shift=UP * 0.05), run_time=0.6)
        self.wait(1.2)
        self.finish_section()

    # ---------------- 4. 三种统计图 ---------------- 11.4
    def scene_charts(self):
        self.section(4, "三种统计图，各看各的")

        bar = VGroup(
            Rectangle(width=0.42, height=0.8, color=ORANGE, fill_color=ORANGE, fill_opacity=0.5),
            Rectangle(width=0.42, height=1.35, color=ORANGE, fill_color=ORANGE, fill_opacity=0.5),
            Rectangle(width=0.42, height=1.05, color=ORANGE, fill_color=ORANGE, fill_opacity=0.5),
        ).arrange(RIGHT, buff=0.22, aligned_edge=DOWN)
        bar.move_to([-4.5, 0.22, 0], aligned_edge=DOWN)
        self.play(FadeIn(bar, shift=UP * 0.06), run_time=0.8)

        pts = [[-0.85, 0.0, 0], [-0.3, 0.5, 0], [0.25, 0.3, 0], [0.8, 0.85, 0]]
        pts = [[x, y * 1.5 + 0.25, 0] for x, y, _ in pts]
        line = VGroup()
        for i in range(len(pts) - 1):
            line.add(Line(pts[i], pts[i + 1], color=BLUE, stroke_width=3))
        dots = VGroup(*[Dot(p, radius=0.07, color=BLUE) for p in pts])
        self.play(Create(line), FadeIn(dots), run_time=0.9)

        pcx, pcy, pr = 4.5, 1.0, 0.78
        pie = Circle(radius=pr, color=GREEN, stroke_width=2.2).move_to([pcx, pcy, 0])
        fills = VGroup(
            pie_slice(pcx, pcy, pr, 90, 200, GREEN, 0.42, 1.4),
            pie_slice(pcx, pcy, pr, 200, 300, GREEN, 0.22, 1.4),
            pie_slice(pcx, pcy, pr, 300, 450, GREEN, 0.12, 1.4),
        )
        self.play(Create(pie), run_time=0.7)
        self.play(FadeIn(fills), run_time=0.7)

        tags = VGroup(
            txt("条形图：看数量", size=25, color=ORANGE),
            txt("折线图：看趋势", size=25, color=BLUE),
            txt("扇形图：看占比", size=25, color=GREEN),
        ).arrange(RIGHT, buff=0.85).move_to([0, -1.35, 0])
        for t in tags:
            self.play(FadeIn(t, shift=UP * 0.05), run_time=0.55)

        note = txt("先想清楚要问什么，再选图", size=26, color=GOLD).move_to([0, -2.25, 0])
        self.play(FadeIn(note, shift=UP * 0.05), run_time=0.7)
        self.wait(1.4)
        self.finish_section()

    # ---------------- 5. 扇形图的圆心角 ---------------- 12.7
    def scene_pie(self):
        self.section(5, "扇形图的圆心角")

        c = [-2.9, 0.15, 0]
        circle = Circle(radius=1.4, color=DIM, stroke_width=2).move_to(c)
        self.play(Create(circle), run_time=0.9)

        quarter = pie_slice(-2.9, 0.15, 1.4, 90, 180, GOLD, 0.42, 2.4)
        self.play(FadeIn(quarter), run_time=0.9)

        lab = txt("篮球 25%", size=27, color=GOLD).move_to([-4.35, 1.72, 0])
        self.play(FadeIn(lab, shift=UP * 0.05), run_time=0.7)

        form = label_box("圆心角 = 360° × 频率", size=28, color=GOLD).move_to([3.4, 1.5, 0])
        self.play(FadeIn(form, scale=0.96), run_time=0.9)

        calc = txt("360° × 25% = 90°", size=30, color=GREEN).move_to([3.4, 0.45, 0])
        self.play(FadeIn(calc, shift=UP * 0.05), run_time=0.8)

        same = txt("正好是整圆的四分之一", size=26, color=CHALK).move_to([3.4, -0.5, 0])
        self.play(FadeIn(same, shift=UP * 0.05), run_time=0.7)

        note = txt("整个圆是 360°，所有扇形加起来是 100%", size=26, color=DIM).move_to([0, -2.15, 0])
        self.play(FadeIn(note, shift=UP * 0.05), run_time=0.7)
        self.wait(1.4)
        self.finish_section()

    # ---------------- 6. 例题 + 易错点 ---------------- 18.7
    def scene_ex(self):
        self.section(6, "例题与三个易错点")

        q = txt("全班 40 人，喜欢跳绳的有 10 人", size=29, color=CHALK).move_to([0, 2.3, 0])
        self.play(FadeIn(q, shift=UP * 0.05), run_time=0.8)

        s1 = txt("频率 = 10 ÷ 40 = 0.25 = 25%", size=32, color=BLUE).move_to([0, 1.45, 0])
        self.play(FadeIn(s1, shift=UP * 0.05), run_time=0.85)

        s2 = txt("圆心角 = 360° × 25% = 90°", size=32, color=GREEN).move_to([0, 0.6, 0])
        self.play(FadeIn(s2, shift=UP * 0.05), run_time=0.85)

        note = txt("先算频率，再算圆心角，两步别跳", size=26, color=GOLD).move_to([0, -0.2, 0])
        self.play(FadeIn(note, shift=UP * 0.05), run_time=0.7)

        items = [
            ("把总体当成样本", "样本是抽出来的"),
            ("频数和频率混为一谈", "次数对次数，比值对比值"),
            ("圆心角直接填百分比", "要乘 360°"),
        ]
        y = -1.05
        for bad_s, good_s in items:
            bad = txt(bad_s, size=25, color=RED).move_to([-3.3, y, 0])
            good = txt(good_s, size=24, color=GREEN).move_to([3.5, y, 0])
            cross = Line(bad.get_left() + [-0.1, -0.07, 0],
                         bad.get_right() + [0.1, 0.16, 0],
                         color=RED, stroke_width=2.6)
            self.play(FadeIn(bad, shift=RIGHT * 0.05), run_time=0.55)
            self.play(Create(cross), FadeIn(good, shift=RIGHT * 0.05), run_time=0.65)
            y -= 0.68

        self.wait(1.4)
        self.finish_section()

    def construct(self):
        self.scene_story()
        self.clear_stage()
        self.scene_methods()
        self.clear_stage()
        self.scene_sample()
        self.clear_stage()
        self.scene_tally()
        self.clear_stage()
        self.scene_charts()
        self.clear_stage()
        self.scene_pie()
        self.clear_stage()
        self.scene_ex()
        self.clear_stage(0.8)