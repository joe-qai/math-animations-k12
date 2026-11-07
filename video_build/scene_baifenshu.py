# -*- coding: utf-8 -*-
"""百分数：意义与读写法、与分数小数互化、求百分之几、及格率、打折应用。六年级上册。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


class BaifenshuScene(NarratedScene):
    lesson = "baifenshu"

    def clear_stage(self, run_time: float = 0.5):
        keep = {id(self._track), id(self._fill)}
        junk = [m for m in self.mobjects if id(m) not in keep]
        if junk:
            self.play(*[FadeOut(m) for m in junk], run_time=run_time)
        self.cur_title = None
        self.cur_sub = None

    # ---------------- 0. 生活里的百分数 ---------------- 18.1
    def scene_story(self):
        self.section(0, "生活里的百分数")

        samples = [
            ("果汁含糖 10%", BLUE),
            ("今天出勤 95%", GREEN),
            ("产量增长 20%", GOLD),
        ]
        y = 1.85
        for s, c in samples:
            self.play(FadeIn(label_box(s, size=30, color=c).move_to([-3.5, y, 0]),
                             shift=RIGHT * 0.05), run_time=0.85)
            y -= 1.15

        cap = VGroup(
            txt("百分数：一个数是另一个数的百分之几", size=27, color=CHALK),
            txt("说白了，就是拿两个数比一比", size=26, color=DIM),
        ).arrange(DOWN, buff=0.3).move_to([-3.1, -1.85, 0])
        self.play(FadeIn(cap[0], shift=UP * 0.05), run_time=0.8)
        self.play(FadeIn(cap[1], shift=UP * 0.05), run_time=0.8)

        big = txt("%", size=140, color=GOLD).move_to([4.3, 1.0, 0])
        bl = txt("百分之几", size=28, color=GOLD).move_to([4.3, -0.15, 0])
        self.play(FadeIn(big, scale=0.92), run_time=1.0)
        self.play(FadeIn(bl, shift=UP * 0.05), run_time=0.8)
        self.wait(2.6)
        self.finish_section()

    # ---------------- 1. 写法与意义 ---------------- 16.3
    def scene_write(self):
        self.section(1, "百分数怎么写、什么意思")

        p = txt("45%", size=96, color=GOLD).move_to([-4.3, 1.15, 0])
        r = txt("读作：百分之四十五", size=28, color=GOLD).move_to([-4.3, 0.05, 0])
        self.play(FadeIn(p, scale=0.92), run_time=1.0)
        self.play(FadeIn(r, shift=UP * 0.05), run_time=0.8)

        eq = txt("45% = 45 ÷ 100 = 0.45", size=32, color=CHALK).move_to([-3.9, -1.15, 0])
        self.play(FadeIn(eq, shift=UP * 0.05), run_time=0.9)

        rows = VGroup(
            txt("分母固定是 100", size=30, color=GREEN),
            txt("就是 100 分之几", size=28, color=CHALK),
            txt("所以比较大小特别方便", size=26, color=DIM),
        ).arrange(DOWN, buff=0.36, aligned_edge=LEFT).move_to([3.0, 1.25, 0])
        for x in rows:
            self.play(FadeIn(x, shift=RIGHT * 0.05), run_time=0.75)
            self.wait(0.25)

        self.wait(1.6)
        self.finish_section()

    # ---------------- 2. 与小数、分数互化 ---------------- 17.4
    def scene_convert(self):
        self.section(2, "小数、分数怎么变百分数")

        rows = [
            ("0.8  →  80%", GOLD),
            ("80%  →  0.8", BLUE),
            ("3 ÷ 5 = 0.6  →  60%", GREEN),
        ]
        y = 1.8
        for s, c in rows:
            self.play(FadeIn(txt(s, size=40, color=c).move_to([-3.2, y, 0]),
                             shift=RIGHT * 0.05), run_time=0.9)
            y -= 1.25

        notes = VGroup(
            txt("小数 → 百分数", size=26, color=GOLD),
            txt("小数点右移两位，加 %", size=28, color=CHALK),
        ).arrange(DOWN, buff=0.2).move_to([3.4, 1.95, 0])
        self.play(FadeIn(notes[0], shift=UP * 0.05), run_time=0.7)
        self.play(FadeIn(notes[1], shift=UP * 0.05), run_time=0.7)

        notes2 = VGroup(
            txt("百分数 → 小数", size=26, color=BLUE),
            txt("去掉 %，小数点左移两位", size=28, color=CHALK),
        ).arrange(DOWN, buff=0.2).move_to([3.4, 0.45, 0])
        self.play(FadeIn(notes2[0], shift=UP * 0.05), run_time=0.7)
        self.play(FadeIn(notes2[1], shift=UP * 0.05), run_time=0.7)

        f = txt("分数 → 先化小数，再移小数点", size=28, color=GREEN).move_to([2.5, -1.15, 0])
        self.play(FadeIn(f, shift=UP * 0.05), run_time=0.8)
        self.wait(2.0)
        self.finish_section()

    # ---------------- 3. 求百分之几 ---------------- 13.3
    def scene_rate(self):
        self.section(3, "求一个数是另一个数的百分之几")

        box = label_box("及格率 = 及格人数 ÷ 总人数 × 100%", size=34, color=GOLD)
        box.move_to([0, 1.15, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.1)

        rows = VGroup(
            txt("谁和谁比，谁就做被除数", size=30, color=GREEN),
            txt("除完再乘 100%，写成百分数", size=28, color=CHALK),
            txt("除数弄反，结果就错了", size=27, color=RED),
        ).arrange(DOWN, buff=0.42).move_to([0, -0.85, 0])
        for r in rows:
            self.play(FadeIn(r, shift=UP * 0.05), run_time=0.8)
            self.wait(0.2)

        self.wait(1.4)
        self.finish_section()

    # ---------------- 4. 例题：及格率 ---------------- 16.9
    def scene_example(self):
        self.section(4, "40 人考试，32 人及格")

        prob = txt("全班 40 人参加考试，32 人及格，及格率是多少", size=29, color=CHALK)
        prob.move_to([0, 2.15, 0])
        self.play(FadeIn(prob, shift=UP * 0.05), run_time=0.9)

        rows = [
            ("32 ÷ 40 = 0.8", CHALK),
            ("0.8 × 100% = 80%", GREEN),
        ]
        y = 0.95
        for s, c in rows:
            self.play(FadeIn(txt(s, size=40, color=c).move_to([-0.8, y, 0]),
                             shift=UP * 0.04), run_time=0.95)
            y -= 1.0

        ans = txt("及格率是 80%", size=36, color=GOLD).move_to([0, -1.15, 0])
        self.play(FadeIn(ans, shift=UP * 0.05), run_time=0.9)

        tip = txt("也就是 100 个人里，有 80 个人及格", size=27, color=GREEN)
        tip.move_to([0, -2.1, 0])
        self.play(FadeIn(tip, shift=UP * 0.05), run_time=0.9)
        self.wait(1.8)
        self.finish_section()

    # ---------------- 5. 打折：求一个数的百分之几 ---------------- 17.1
    def scene_apply(self):
        self.section(5, "打折：求一个数的百分之几")

        prob = txt("一件衣服原价 200 元，打八折，现在多少钱", size=29, color=CHALK)
        prob.move_to([0, 2.2, 0])
        self.play(FadeIn(prob, shift=UP * 0.05), run_time=0.9)

        b = label_box("八折 = 80%", size=34, color=GOLD).move_to([0, 1.15, 0])
        self.play(FadeIn(b, scale=0.97), run_time=0.9)

        rows = [
            ("200 × 80% = 200 × 0.8", CHALK),
            ("= 160（元）", GREEN),
        ]
        y = 0.1
        for s, c in rows:
            self.play(FadeIn(txt(s, size=38, color=c).move_to([0, y, 0]),
                             shift=UP * 0.04), run_time=0.95)
            y -= 0.95

        tip = txt("求一个数的百分之几是多少，用乘法", size=28, color=GOLD)
        tip.move_to([0, -1.7, 0])
        self.play(FadeIn(tip, shift=UP * 0.05), run_time=0.9)

        note = txt("百分数先化成小数再乘，算起来更快", size=26, color=DIM)
        note.move_to([0, -2.5, 0])
        self.play(FadeIn(note, shift=UP * 0.05), run_time=0.8)
        self.wait(1.6)
        self.finish_section()

    # ---------------- 6. 易错点 + 三句话 ---------------- 18.0
    def scene_warn(self):
        self.section(6, "三个易错点")

        items = [
            ("百分数后面写单位", "百分数不带单位"),
            ("以为百分数不能超 100%", "可以大于 100%"),
            ("除以谁弄不清", "先找单位一"),
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
            label_box("① 百分数 = 分母 100 的分数", size=24, color=GOLD),
            label_box("② 谁比谁，谁就做被除数", size=24, color=CHALK),
            label_box("③ 求百分之几是多少，用乘法", size=24, color=GREEN),
        ).arrange(DOWN, buff=0.2).move_to([0, -1.65, 0])
        for r in rows:
            self.play(FadeIn(r, shift=RIGHT * 0.06), run_time=0.6)
            self.wait(0.55)

        self.wait(1.0)
        self.finish_section()

    def construct(self):
        self.scene_story()
        self.clear_stage()
        self.scene_write()
        self.clear_stage()
        self.scene_convert()
        self.clear_stage()
        self.scene_rate()
        self.clear_stage()
        self.scene_example()
        self.clear_stage()
        self.scene_apply()
        self.clear_stage()
        self.scene_warn()
        self.clear_stage(0.8)