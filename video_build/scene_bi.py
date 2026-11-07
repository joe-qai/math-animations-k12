# -*- coding: utf-8 -*-
"""比：意义与各部分、比与除法分数的关系、化简比、分数比小数比、求比值。六年级上册。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


def frac(n, d, color=CHALK, size=30):
    """竖排分数（自建，不用 LaTeX）。"""
    t1 = txt(str(n), size=size, color=color)
    t2 = txt(str(d), size=size, color=color)
    line = Line(LEFT, RIGHT, color=color, stroke_width=2)
    line.set_width(max(t1.width, t2.width) + 0.12)
    return VGroup(t1, line, t2).arrange(DOWN, buff=0.08)


class BiScene(NarratedScene):
    lesson = "bi"

    def clear_stage(self, run_time: float = 0.5):
        keep = {id(self._track), id(self._fill)}
        junk = [m for m in self.mobjects if id(m) not in keep]
        if junk:
            self.play(*[FadeOut(m) for m in junk], run_time=run_time)
        self.cur_title = None
        self.cur_sub = None

    # ---------------- 0. 生活里的比 ---------------- 19.7
    def scene_story(self):
        self.section(0, "生活里的比")

        cards = [
            ("蜂蜜 : 水 = 1 : 9", GOLD),
            ("男生 : 女生 = 3 : 2", BLUE),
            ("比例尺 = 1 : 1000000", GREEN),
        ]
        y = 1.95
        for s, c in cards:
            self.play(FadeIn(label_box(s, size=28, color=c).move_to([-3.4, y, 0]),
                             shift=RIGHT * 0.05), run_time=0.85)
            y -= 1.15

        cap = VGroup(
            txt("比：表示两个数的相除关系", size=27, color=CHALK),
            txt("两个数之间，用比号隔开", size=26, color=DIM),
        ).arrange(DOWN, buff=0.3).move_to([-3.2, -1.9, 0])
        self.play(FadeIn(cap[0], shift=UP * 0.05), run_time=0.8)
        self.play(FadeIn(cap[1], shift=UP * 0.05), run_time=0.8)

        big = txt("3 : 2", size=86, color=GOLD).move_to([4.1, 1.0, 0])
        l1 = txt("前项 : 后项", size=28, color=DIM).move_to([4.1, 0.0, 0])
        l2 = txt("也就是 3 ÷ 2", size=28, color=GREEN).move_to([4.1, -0.8, 0])
        self.play(FadeIn(big, scale=0.93), run_time=1.0)
        self.play(FadeIn(l1, shift=UP * 0.05), run_time=0.7)
        self.play(FadeIn(l2, shift=UP * 0.05), run_time=0.7)
        self.wait(2.0)
        self.finish_section()

    # ---------------- 1. 比的各部分 ---------------- 15.6
    def scene_parts(self):
        self.section(1, "比的各部分叫什么")

        a = txt("3", size=96, color=GOLD).move_to([-1.7, 0.85, 0])
        colon = txt(":", size=96, color=DIM).move_to([0, 0.85, 0])
        b = txt("2", size=96, color=BLUE).move_to([1.7, 0.85, 0])
        self.play(FadeIn(a, scale=0.9), FadeIn(colon), FadeIn(b, scale=0.9), run_time=1.0)

        la = txt("前项", size=28, color=GOLD).move_to([-1.7, -0.2, 0])
        lc = txt("比号", size=28, color=DIM).move_to([0, -0.2, 0])
        lb = txt("后项", size=28, color=BLUE).move_to([1.7, -0.2, 0])
        self.play(FadeIn(la, shift=UP * 0.05), run_time=0.6)
        self.play(FadeIn(lc, shift=UP * 0.05), run_time=0.6)
        self.play(FadeIn(lb, shift=UP * 0.05), run_time=0.6)

        r1 = txt("比值 = 前项 ÷ 后项 = 3 ÷ 2 = 1.5", size=32, color=CHALK)
        r1.move_to([0, -1.35, 0])
        self.play(FadeIn(r1, shift=UP * 0.05), run_time=0.9)

        r2 = txt("3 : 2 也可以写成分数形式 3/2", size=30, color=GREEN)
        r2.move_to([0, -2.15, 0])
        self.play(FadeIn(r2, shift=UP * 0.05), run_time=0.9)
        self.wait(1.6)
        self.finish_section()

    # ---------------- 2. 比、除法、分数 ---------------- 17.6
    def scene_link(self):
        self.section(2, "比、除法、分数是一回事")

        xs = [-4.3, 0.1, 4.4]
        heads = ["比", "除法", "分数"]
        cols = [GOLD, BLUE, GREEN]
        for x, h, c in zip(xs, heads, cols):
            t = txt(h, size=32, color=c).move_to([x, 1.85, 0])
            ln = Line([x - 0.75, 1.55, 0], [x + 0.75, 1.55, 0], color=c, stroke_width=2.4)
            self.play(FadeIn(t, shift=DOWN * 0.05), Create(ln), run_time=0.6)

        rows = [
            ("前项", "被除数", "分子"),
            ("后项", "除数", "分母"),
            ("比值", "商", "分数值"),
        ]
        y = 0.85
        for r in rows:
            g = VGroup()
            for x, s in zip(xs, r):
                g.add(txt(s, size=30, color=CHALK).move_to([x, y, 0]))
            self.play(FadeIn(g, shift=RIGHT * 0.04), run_time=0.8)
            y -= 0.85

        note = txt("后项不能是 0：除数、分母都不能是 0", size=30, color=RED)
        note.move_to([0, -1.95, 0])
        self.play(FadeIn(note, shift=UP * 0.05), run_time=0.9)
        self.wait(2.0)
        self.finish_section()

    # ---------------- 3. 化简比 ---------------- 17.6
    def scene_simplify(self):
        self.section(3, "化简比：化成互质的整数")

        left = txt("12 : 18", size=62, color=CHALK).move_to([-4.0, 1.15, 0])
        arrow = Arrow([-1.6, 1.15, 0], [0.6, 1.15, 0], color=DIM, buff=0.1,
                      stroke_width=3, max_tip_length_to_length_ratio=0.16)
        op = txt("同时除以 6", size=28, color=GOLD).move_to([-0.5, 1.95, 0])
        right = txt("2 : 3", size=62, color=GREEN).move_to([2.7, 1.15, 0])
        self.play(FadeIn(left, shift=RIGHT * 0.05), run_time=0.9)
        self.play(Create(arrow), FadeIn(op, shift=UP * 0.05), run_time=0.9)
        self.play(FadeIn(right, shift=RIGHT * 0.05), run_time=0.9)

        rows = VGroup(
            txt("前项和后项，同乘或同除一个不为 0 的数", size=28, color=CHALK),
            txt("比值不变，和分数的基本性质一样", size=28, color=GREEN),
            txt("结果要化成最简整数比", size=28, color=GOLD),
        ).arrange(DOWN, buff=0.36).move_to([0, -0.75, 0])
        for r in rows:
            self.play(FadeIn(r, shift=UP * 0.05), run_time=0.8)
            self.wait(0.2)
        self.wait(1.6)
        self.finish_section()

    # ---------------- 4. 分数比、小数比 ---------------- 16.5
    def scene_kinds(self):
        self.section(4, "分数比、小数比怎么化简")

        f1 = VGroup(frac(1, 2, CHALK), txt(":", size=30, color=DIM),
                    frac(1, 3, CHALK)).arrange(RIGHT, buff=0.16)
        f1.move_to([-4.6, 1.35, 0])
        a1 = Arrow([-3.2, 1.35, 0], [-1.3, 1.35, 0], color=DIM, buff=0.08,
                   stroke_width=2.6, max_tip_length_to_length_ratio=0.2)
        o1 = txt("同乘 6", size=26, color=GOLD).move_to([-2.25, 1.85, 0])
        r1 = txt("3 : 2", size=40, color=GREEN).move_to([-0.35, 1.35, 0])
        self.play(FadeIn(f1), run_time=0.9)
        self.play(Create(a1), FadeIn(o1), run_time=0.8)
        self.play(FadeIn(r1, shift=RIGHT * 0.05), run_time=0.8)

        d1 = txt("0.5 : 0.2", size=42, color=CHALK).move_to([-4.7, -0.15, 0])
        a2 = Arrow([-3.0, -0.15, 0], [-1.3, -0.15, 0], color=DIM, buff=0.08,
                   stroke_width=2.6, max_tip_length_to_length_ratio=0.2)
        o2 = txt("同乘 10", size=26, color=GOLD).move_to([-2.15, 0.35, 0])
        r2 = txt("5 : 2", size=40, color=BLUE).move_to([-0.35, -0.15, 0])
        self.play(FadeIn(d1), run_time=0.8)
        self.play(Create(a2), FadeIn(o2), run_time=0.8)
        self.play(FadeIn(r2, shift=RIGHT * 0.05), run_time=0.8)

        notes = VGroup(
            txt("分数比：先乘分母的最小公倍数", size=27, color=GOLD),
            txt("小数比：先乘 10 或 100，去掉小数点", size=27, color=BLUE),
            txt("化成整数比，再约分到最简", size=27, color=GREEN),
        ).arrange(DOWN, buff=0.3).move_to([0, -1.7, 0])
        for n in notes:
            self.play(FadeIn(n, shift=LEFT * 0.05), run_time=0.7)

        self.wait(1.6)
        self.finish_section()

    # ---------------- 5. 例题：化简并求比值 ---------------- 15.6
    def scene_example(self):
        self.section(5, "24 : 36 怎么化简")

        top = txt("化简 24 : 36", size=32, color=CHALK).move_to([0, 2.1, 0])
        self.play(FadeIn(top, shift=UP * 0.05), run_time=0.8)

        steps = VGroup(
            txt("24 : 36", size=40, color=CHALK),
            txt("同时除以 12 → 2 : 3", size=40, color=GREEN),
        ).arrange(DOWN, buff=0.45).move_to([0, 0.85, 0])
        for s in steps:
            self.play(FadeIn(s, shift=UP * 0.04), run_time=0.9)

        val = txt("比值 = 2 ÷ 3 = 2/3", size=36, color=GOLD).move_to([0, -0.75, 0])
        self.play(FadeIn(val, shift=UP * 0.05), run_time=0.9)

        tip = VGroup(
            txt("化简比 → 结果还是一个比（2 : 3）", size=27, color=GREEN),
            txt("求比值 → 结果是一个数（2/3）", size=27, color=GOLD),
        ).arrange(DOWN, buff=0.28).move_to([0, -1.85, 0])
        self.play(FadeIn(tip[0], shift=UP * 0.05), run_time=0.7)
        self.play(FadeIn(tip[1], shift=UP * 0.05), run_time=0.7)
        self.wait(1.4)
        self.finish_section()

    # ---------------- 6. 易错点 + 三句话 ---------------- 15.6
    def scene_warn(self):
        self.section(6, "三个易错点")

        items = [
            ("后项写成 0", "后项相当于除数，不能为 0"),
            ("化简后还有小数", "结果要是最简整数比"),
            ("化简比当成求比值", "一个是比，一个是数"),
        ]
        y = 2.05
        for bad_s, note in items:
            bad = txt(bad_s, size=28, color=RED).move_to([-3.2, y, 0])
            n = txt(note, size=24, color=GREEN).move_to([3.2, y, 0])
            cross = Line(bad.get_left() + [-0.1, -0.08, 0],
                         bad.get_right() + [0.1, 0.18, 0],
                         color=RED, stroke_width=2.8)
            self.play(FadeIn(bad, shift=RIGHT * 0.05), run_time=0.6)
            self.play(Create(cross), FadeIn(n, shift=RIGHT * 0.05), run_time=0.7)
            self.wait(0.6)
            y -= 0.92

        rows = VGroup(
            label_box("① 比就是两个数相除", size=24, color=GOLD),
            label_box("② 前项后项同乘同除，比值不变", size=24, color=CHALK),
            label_box("③ 结果化成最简整数比", size=24, color=GREEN),
        ).arrange(DOWN, buff=0.2).move_to([0, -1.65, 0])
        for r in rows:
            self.play(FadeIn(r, shift=RIGHT * 0.06), run_time=0.6)
            self.wait(0.5)

        self.wait(0.8)
        self.finish_section()

    def construct(self):
        self.scene_story()
        self.clear_stage()
        self.scene_parts()
        self.clear_stage()
        self.scene_link()
        self.clear_stage()
        self.scene_simplify()
        self.clear_stage()
        self.scene_kinds()
        self.clear_stage()
        self.scene_example()
        self.clear_stage()
        self.scene_warn()
        self.clear_stage(0.8)