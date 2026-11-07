# -*- coding: utf-8 -*-
"""比与比例的应用：按比分配三步法、分数法、比例尺意义、两道例题、易错点。小升初衔接。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


def frac(n, d, color=CHALK, size=32):
    """竖排分数（自建，不用 LaTeX）。"""
    t1 = txt(str(n), size=size, color=color)
    t2 = txt(str(d), size=size, color=color)
    line = Line(LEFT, RIGHT, color=color, stroke_width=2)
    line.set_width(max(t1.width, t2.width) + 0.12)
    return VGroup(t1, line, t2).arrange(DOWN, buff=0.08)


def expr(parts, size=32, buff=0.10):
    """把若干文字 / 分数拼成一行，竖直居中对齐。"""
    g = VGroup()
    for p in parts:
        if isinstance(p, str):
            g.add(txt(p, size=size, color=CHALK))
        else:
            g.add(p)
    g.arrange(RIGHT, buff=buff)
    g.move_to([0, 0, 0])
    return g


def place(g, x, y):
    """左边缘对齐 x，竖直中心落在 y。"""
    g.move_to([0, 0, 0])
    g.shift(RIGHT * (x - g.get_left()[0]) + UP * (y - g.get_center()[1]))
    return g


class BiliYingyongScene(NarratedScene):
    lesson = "bili-yingyong"

    def clear_stage(self, run_time: float = 0.5):
        keep = {id(self._track), id(self._fill)}
        junk = [m for m in self.mobjects if id(m) not in keep]
        if junk:
            self.play(*[FadeOut(m) for m in junk], run_time=run_time)
        self.cur_title = None
        self.cur_sub = None

    # ---------------- 0. 一百颗糖怎么分 ---------------- 16.5
    def scene_story(self):
        self.section(0, "一百颗糖怎么分")

        total = label_box("100 颗糖", size=36, color=GOLD).move_to([-3.3, 2.0, 0])
        self.play(FadeIn(total, scale=0.96), run_time=0.9)

        c1 = txt("一班：30 人", size=31, color=CHALK).move_to([-3.4, 0.95, 0])
        c2 = txt("二班：20 人", size=31, color=CHALK).move_to([-3.4, 0.2, 0])
        self.play(FadeIn(c1, shift=RIGHT * 0.05), run_time=0.8)
        self.play(FadeIn(c2, shift=RIGHT * 0.05), run_time=0.8)

        ratio = txt("按 3 : 2 分", size=44, color=GOLD).move_to([3.6, 1.55, 0])
        self.play(FadeIn(ratio, scale=0.95), run_time=0.9)

        q = txt("一班拿多少颗？", size=32, color=GREEN).move_to([3.5, 0.35, 0])
        self.play(FadeIn(q, shift=UP * 0.05), run_time=0.8)

        note = VGroup(
            txt("不是平均分", size=28, color=RED),
            txt("是按一定的比来分", size=28, color=CHALK),
        ).arrange(DOWN, buff=0.28).move_to([0.1, -1.5, 0])
        self.play(FadeIn(note[0], shift=UP * 0.05), run_time=0.7)
        self.play(FadeIn(note[1], shift=UP * 0.05), run_time=0.7)
        self.wait(2.4)
        self.finish_section()

    # ---------------- 1. 按比分三步 ---------------- 15.3
    def scene_steps(self):
        self.section(1, "按比分，三步走")

        steps = VGroup(
            txt("① 总份数：把比的各项加起来", size=30, color=GOLD),
            txt("② 每份：总量 ÷ 总份数", size=30, color=BLUE),
            txt("③ 各部分：每份 × 各自的份数", size=30, color=GREEN),
        ).arrange(DOWN, buff=0.55, aligned_edge=LEFT).move_to([-0.9, 1.55, 0])
        for s in steps:
            self.play(FadeIn(s, shift=RIGHT * 0.05), run_time=0.9)
            self.wait(0.2)

        flow = VGroup(
            label_box("总量", size=26, color=CHALK),
            txt("÷ 总份数", size=25, color=DIM),
            label_box("每份", size=26, color=BLUE),
            txt("× 份数", size=25, color=DIM),
            label_box("各部分", size=26, color=GREEN),
        ).arrange(RIGHT, buff=0.24).move_to([0, -1.5, 0])
        self.play(FadeIn(flow), run_time=1.2)
        self.wait(2.2)
        self.finish_section()

    # ---------------- 2. 也可以看成分数 ---------------- 15.6
    def scene_fraction(self):
        self.section(2, "换个想法：看占总数的几分之几")

        head = txt("3 : 2  →  一共 5 份", size=32, color=CHALK).move_to([0, 2.1, 0])
        self.play(FadeIn(head, shift=UP * 0.05), run_time=0.8)

        r1 = expr([txt("一班：100 × ", size=30, color=CHALK), frac(3, 5),
                   txt(" = 60（颗）", size=30, color=GREEN)], size=30)
        place(r1, -4.1, 1.2)
        self.play(FadeIn(r1, shift=RIGHT * 0.05), run_time=0.9)

        r2 = expr([txt("二班：100 × ", size=30, color=CHALK), frac(2, 5),
                   txt(" = 40（颗）", size=30, color=BLUE)], size=30)
        place(r2, -4.1, 0.15)
        self.play(FadeIn(r2, shift=RIGHT * 0.05), run_time=0.9)

        note = VGroup(
            txt("3 + 2 = 5，所以分母是 5", size=28, color=GOLD),
            txt("两条路，结果一样", size=28, color=CHALK),
            txt("哪条顺手走哪条", size=27, color=DIM),
        ).arrange(DOWN, buff=0.28, aligned_edge=LEFT).move_to([-1.9, -2.1, 0])
        for n in note:
            self.play(FadeIn(n, shift=UP * 0.05), run_time=0.75)
        self.wait(1.8)
        self.finish_section()

    # ---------------- 3. 比例尺 ---------------- 17.3
    def scene_scale(self):
        self.section(3, "比例尺：图上 1 厘米代表多远")

        box = label_box("图上距离 : 实际距离 = 1 : 1000000", size=30, color=GOLD)
        box.move_to([0, 1.9, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.1)

        rows = VGroup(
            txt("图上 1 厘米  →  实际 1000000 厘米", size=30, color=CHALK),
            txt("1000000 厘米 = 10000 米 = 10 千米", size=30, color=GREEN),
        ).arrange(DOWN, buff=0.45, aligned_edge=LEFT).move_to([-0.5, 0.55, 0])
        for r in rows:
            self.play(FadeIn(r, shift=UP * 0.05), run_time=0.85)

        warn = VGroup(
            txt("用比例尺之前，先把单位统一", size=29, color=RED),
            txt("1 千米 = 1000 米 = 100000 厘米", size=27, color=DIM),
        ).arrange(DOWN, buff=0.3).move_to([0, -1.55, 0])
        self.play(FadeIn(warn[0], shift=UP * 0.05), run_time=0.8)
        self.play(FadeIn(warn[1], shift=UP * 0.05), run_time=0.8)
        self.wait(2.6)
        self.finish_section()

    # ---------------- 4. 例题：按比分配 ---------------- 17.7
    def scene_ex1(self):
        self.section(4, "100 颗按 3 : 2 分")

        prob = txt("总数 100 颗，按 3 : 2 分给两个班", size=30, color=CHALK).move_to([0, 2.4, 0])
        self.play(FadeIn(prob, shift=UP * 0.05), run_time=0.8)

        rows = [
            ("总份数 3 + 2 = 5", GOLD),
            ("每份 100 ÷ 5 = 20（颗）", BLUE),
            ("一班 20 × 3 = 60（颗）", GREEN),
            ("二班 20 × 2 = 40（颗）", GREEN),
        ]
        y = 1.45
        for s, c in rows:
            self.play(FadeIn(txt(s, size=32, color=c).move_to([-1.3, y, 0]),
                             shift=UP * 0.04), run_time=0.8)
            y -= 0.8

        chk = txt("验算：60 : 40 = 3 : 2  ✓", size=30, color=GOLD).move_to([0, -2.0, 0])
        self.play(FadeIn(chk, shift=UP * 0.05), run_time=0.8)
        self.wait(2.0)
        self.finish_section()

    # ---------------- 5. 比例尺例题 ---------------- 20.6
    def scene_ex2(self):
        self.section(5, "图上 6 厘米，实际多远")

        prob = txt("比例尺 1 : 1000000，图上量得 6 厘米", size=30, color=CHALK)
        prob.move_to([0, 2.4, 0])
        self.play(FadeIn(prob, shift=UP * 0.05), run_time=0.8)

        rows = [
            ("实际 = 6 × 1000000", CHALK),
            ("= 6000000（厘米）", BLUE),
            ("= 60000（米）", BLUE),
            ("= 60（千米）", GREEN),
        ]
        y = 1.45
        for s, c in rows:
            self.play(FadeIn(txt(s, size=32, color=c).move_to([-1.8, y, 0]),
                             shift=UP * 0.04), run_time=0.75)
            y -= 0.75

        note = txt("换算口诀：厘米去两个零是米，再去三个零是千米", size=27, color=GOLD)
        note.move_to([0, -2.05, 0])
        self.play(FadeIn(note, shift=UP * 0.05), run_time=0.85)
        self.wait(2.2)
        self.finish_section()

    # ---------------- 6. 易错点 + 三句话 ---------------- 16.3
    def scene_warn(self):
        self.section(6, "三个易错点")

        items = [
            ("按比分当成平均分", "人多的班要多拿"),
            ("不先求总份数就乱乘", "先加份数，再除"),
            ("比例尺单位不统一", "先化成同一单位"),
        ]
        y = 2.15
        for bad_s, note in items:
            bad = txt(bad_s, size=27, color=RED).move_to([-3.2, y, 0])
            n = txt(note, size=24, color=GREEN).move_to([3.3, y, 0])
            cross = Line(bad.get_left() + [-0.1, -0.08, 0],
                         bad.get_right() + [0.1, 0.18, 0],
                         color=RED, stroke_width=2.8)
            self.play(FadeIn(bad, shift=RIGHT * 0.05), run_time=0.6)
            self.play(Create(cross), FadeIn(n, shift=RIGHT * 0.05), run_time=0.7)
            self.wait(0.5)
            y -= 0.95

        rows = VGroup(
            label_box("① 先算总份数", size=24, color=GOLD),
            label_box("② 每份 = 总量 ÷ 总份数", size=24, color=CHALK),
            label_box("③ 比例尺先统一单位", size=24, color=GREEN),
        ).arrange(DOWN, buff=0.18).move_to([0, -1.95, 0])
        for r in rows:
            self.play(FadeIn(r, shift=RIGHT * 0.06), run_time=0.6)
            self.wait(0.5)

        self.wait(0.8)
        self.finish_section()

    def construct(self):
        self.scene_story()
        self.clear_stage()
        self.scene_steps()
        self.clear_stage()
        self.scene_fraction()
        self.clear_stage()
        self.scene_scale()
        self.clear_stage()
        self.scene_ex1()
        self.clear_stage()
        self.scene_ex2()
        self.clear_stage()
        self.scene_warn()
        self.clear_stage(0.8)