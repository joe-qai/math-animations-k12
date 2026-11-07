# -*- coding: utf-8 -*-
"""因数与倍数：意义、找因数、找倍数、2/5/3 的倍数特征。五年级上册。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


def rule_row(tag: str, body: str, color: str, y: float, tag_w: float = 2.6):
    """左边彩色标签、右边说明。"""
    t = label_box(tag, size=24, color=color).move_to([-4.6, y, 0])
    b = txt(body, size=26, color=CHALK).move_to([1.15, y, 0])
    return VGroup(t, b)


class YinshuBeishuScene(NarratedScene):
    lesson = "yinshu-beishu"

    def clear_stage(self, run_time: float = 0.5):
        keep = {id(self._track), id(self._fill)}
        junk = [m for m in self.mobjects if id(m) not in keep]
        if junk:
            self.play(*[FadeOut(m) for m in junk], run_time=run_time)
        self.cur_title = None
        self.cur_sub = None

    # ---------------- 0. 十二人排队 ---------------- 16.4
    def scene_queue(self):
        self.section(0, "12 个人，正好排成几行")

        def grid(rows: int, cols: int, at=(-3.4, 0.9, 0)):
            g = VGroup()
            for r in range(rows):
                for c in range(cols):
                    x = at[0] + (c - (cols - 1) / 2) * 0.72
                    y = at[1] + ((rows - 1) / 2 - r) * 0.72
                    g.add(Circle(radius=0.19, color=BLUE, stroke_width=0,
                                 fill_color=BLUE, fill_opacity=0.85).move_to([x, y, 0]))
            return g

        g1 = grid(3, 4)
        self.play(LaggedStart(*[FadeIn(d) for d in g1], lag_ratio=0.06), run_time=1.6)
        t1 = txt("3 行 × 每行 4 人", size=26, color=BLUE).move_to([-3.4, -1.15, 0])
        self.play(FadeIn(t1, shift=UP * 0.05), run_time=0.7)
        self.wait(1.2)

        g2 = grid(2, 6)
        self.play(Transform(g1, g2), run_time=1.5)
        t2 = txt("2 行 × 每行 6 人", size=26, color=GOLD).move_to([-3.4, -1.15, 0])
        self.play(Transform(t1, t2), run_time=0.8)
        self.wait(1.2)

        q = VGroup(
            txt("3 × 4 = 12", size=40, color=CHALK),
            txt("2 × 6 = 12", size=40, color=CHALK),
        ).arrange(DOWN, buff=0.34).move_to([3.2, 1.1, 0])
        self.play(FadeIn(q[0], shift=RIGHT * 0.06), run_time=0.7)
        self.play(FadeIn(q[1], shift=RIGHT * 0.06), run_time=0.7)

        note = txt("都正好排完，没有剩下的人", size=27, color=GREEN)
        note.move_to([3.2, -0.5, 0])
        self.play(FadeIn(note, shift=UP * 0.05), run_time=0.8)

        tail = txt("这种「正好」的关系，就叫因数与倍数", size=28, color=GOLD)
        tail.move_to([0, -2.3, 0])
        self.play(FadeIn(tail, shift=UP * 0.06), run_time=0.9)
        self.wait(2.0)
        self.finish_section()

    # ---------------- 1. 因数和倍数 ---------------- 15.2
    def scene_def(self):
        self.section(1, "3 和 4 是因数，12 是倍数")

        big = txt("3 × 4 = 12", size=64, color=CHALK).move_to([0, 1.35, 0])
        self.play(FadeIn(big, shift=UP * 0.06), run_time=0.9)

        bl = Brace(Line([-2.45, 0.95, 0], [-0.25, 0.95, 0], color=BG, stroke_opacity=0),
                   DOWN, buff=0.12, color=GOLD)
        lb = txt("因数", size=28, color=GOLD).next_to(bl, DOWN, buff=0.1)

        br = Brace(Line([1.45, 0.95, 0], [2.95, 0.95, 0], color=BG, stroke_opacity=0),
                   DOWN, buff=0.12, color=GREEN)
        rb = txt("倍数", size=28, color=GREEN).next_to(br, DOWN, buff=0.1)

        self.play(Create(bl), FadeIn(lb), run_time=0.9)
        self.play(Create(br), FadeIn(rb), run_time=0.9)

        s1 = txt("3 和 4 都是 12 的因数", size=30, color=GOLD).move_to([0, -0.9, 0])
        s2 = txt("12 是 3 的倍数，也是 4 的倍数", size=30, color=GREEN)
        s2.move_to([0, -1.65, 0])
        self.play(FadeIn(s1, shift=UP * 0.05), run_time=0.8)
        self.play(FadeIn(s2, shift=UP * 0.05), run_time=0.9)

        tip = txt("因数和倍数，必须在整数范围里说", size=25, color=DIM)
        tip.move_to([0, -2.45, 0])
        self.play(FadeIn(tip, shift=UP * 0.05), run_time=0.8)
        self.wait(2.2)
        self.finish_section()

    # ---------------- 2. 找因数：成对找 ---------------- 15.4
    def scene_factor(self):
        self.section(2, "找 12 的因数：一对一对找")

        rows = VGroup(
            txt("1 × 12 = 12", size=32, color=CHALK),
            txt("2 × 6 = 12", size=32, color=CHALK),
            txt("3 × 4 = 12", size=32, color=CHALK),
        ).arrange(DOWN, buff=0.28, aligned_edge=LEFT).move_to([-3.0, 1.5, 0])
        for r in rows:
            self.play(FadeIn(r, shift=RIGHT * 0.06), run_time=0.6)
            self.wait(0.35)

        arrow = Arrow([-2.9, -0.1, 0], [-2.9, -0.75, 0], color=DIM, stroke_width=2.2,
                      buff=0.02, max_tip_length_to_length_ratio=0.3)
        self.play(GrowArrow(arrow), run_time=0.6)

        res = txt("12 的因数：1、2、3、4、6、12", size=32, color=GOLD)
        res.move_to([0, -1.35, 0])
        self.play(FadeIn(res, shift=UP * 0.06), run_time=0.9)

        cnt = txt("一共 6 个，个数有限", size=27, color=BLUE).move_to([0, -2.15, 0])
        self.play(FadeIn(cnt, shift=UP * 0.05), run_time=0.8)

        side = VGroup(
            txt("最小：1", size=24, color=DIM),
            txt("最大：12（它自己）", size=24, color=DIM),
        ).arrange(DOWN, buff=0.2).move_to([3.9, 0.35, 0])
        self.play(FadeIn(side[0]), run_time=0.5)
        self.play(FadeIn(side[1]), run_time=0.5)
        self.wait(2.4)
        self.finish_section()

    # ---------------- 3. 找倍数：一直乘 ---------------- 17.9
    def scene_multiple(self):
        self.section(3, "找 12 的倍数：一直乘下去")

        rows = VGroup(
            txt("12 × 1 = 12", size=31, color=CHALK),
            txt("12 × 2 = 24", size=31, color=CHALK),
            txt("12 × 3 = 36", size=31, color=CHALK),
            txt("12 × 4 = 48", size=31, color=CHALK),
        ).arrange(DOWN, buff=0.24, aligned_edge=LEFT).move_to([-2.6, 1.65, 0])
        for r in rows:
            self.play(FadeIn(r, shift=RIGHT * 0.05), run_time=0.55)

        dots = txt("…… 一直乘下去", size=29, color=DIM).move_to([-0.4, -0.55, 0])
        self.play(FadeIn(dots, shift=UP * 0.05), run_time=0.7)

        line = VGroup(
            txt("12 的倍数：12、24、36、48、60 ……", size=29, color=GOLD),
            txt("有无限多个，写不完", size=27, color=BLUE),
        ).arrange(DOWN, buff=0.26).move_to([0, -1.62, 0])
        self.play(FadeIn(line[0], shift=UP * 0.05), run_time=0.8)
        self.play(FadeIn(line[1], shift=UP * 0.05), run_time=0.8)

        side = VGroup(
            txt("最小：12（它自己）", size=24, color=DIM),
            txt("最大：没有", size=24, color=RED),
        ).arrange(DOWN, buff=0.2).move_to([4.05, 1.35, 0])
        self.play(FadeIn(side[0]), run_time=0.5)
        self.play(FadeIn(side[1]), run_time=0.5)
        self.wait(2.8)
        self.finish_section()

    # ---------------- 4. 2、5、3 的倍数特征 ---------------- 15.5
    def scene_feature(self):
        self.section(4, "看个位，看数字和")

        r1 = rule_row("2 的倍数", "个位是 0、2、4、6、8", BLUE, 1.85)
        r2 = rule_row("5 的倍数", "个位是 0 或 5", GOLD, 0.85)
        r3 = rule_row("3 的倍数", "各位数字的和是 3 的倍数", GREEN, -0.15)
        for r in (r1, r2, r3):
            self.play(FadeIn(r[0], scale=0.96), run_time=0.6)
            self.play(FadeIn(r[1], shift=RIGHT * 0.05), run_time=0.6)
            self.wait(0.4)

        ex = VGroup(
            txt("例：12、24、38 都是 2 的倍数", size=25, color=BLUE),
            txt("15、40 是 5 的倍数", size=25, color=GOLD),
            txt("1 + 2 = 3，所以 12 是 3 的倍数", size=25, color=GREEN),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT).move_to([0, -1.75, 0])
        for e in ex:
            self.play(FadeIn(e, shift=UP * 0.05), run_time=0.55)

        wait_t = txt("先看个位，再看数字和", size=26, color=CHALK).move_to([0, -2.78, 0])
        self.play(FadeIn(wait_t, shift=UP * 0.05), run_time=0.7)
        self.wait(2.0)
        self.finish_section()

    # ---------------- 5. 三个易错点 ---------------- 15.5
    def scene_warn(self):
        self.section(5, "三个易错点")

        items = [
            ("1 有两个因数", "1 只有它自己一个因数"),
            ("因数有无限多个", "因数有限，倍数才无限"),
            ("12 是倍数", "要说清：12 是谁的倍数"),
        ]
        y = 1.75
        for bad_s, note in items:
            bad = txt(bad_s, size=30, color=RED).move_to([-3.2, y, 0])
            n = txt(note, size=25, color=GREEN).move_to([3.2, y, 0])
            cross = Line(bad.get_left() + [-0.1, -0.06, 0],
                         bad.get_right() + [0.1, 0.2, 0],
                         color=RED, stroke_width=2.8)
            self.play(FadeIn(bad, shift=RIGHT * 0.05), run_time=0.6)
            self.play(Create(cross), FadeIn(n, shift=RIGHT * 0.05), run_time=0.7)
            self.wait(0.9)
            y -= 1.3

        tip = txt("因数和倍数，永远是「谁是谁的」", size=27, color=GOLD)
        tip.move_to([0, -2.4, 0])
        self.play(FadeIn(tip, shift=UP * 0.06), run_time=0.9)
        self.wait(2.6)
        self.finish_section()

    # ---------------- 6. 三句话 ---------------- 16.5
    def scene_summary(self):
        self.section(6, "三句话")

        rows = VGroup(
            label_box("① 3 × 4 = 12：3、4 是因数，12 是倍数", size=25, color=GOLD),
            label_box("② 因数成对找，个数有限", size=26, color=CHALK),
            label_box("③ 倍数一直乘，个数无限", size=26, color=GREEN),
        ).arrange(DOWN, buff=0.3).move_to([0, 1.4, 0])
        for r in rows:
            self.play(FadeIn(r, shift=RIGHT * 0.07), run_time=0.7)
            self.wait(0.6)

        demo = txt("12 的因数：1、2、3、4、6、12", size=27, color=BLUE)
        demo.move_to([0, -1.25, 0])
        self.play(FadeIn(demo, shift=UP * 0.06), run_time=0.8)
        self.wait(0.6)

        end = txt("因数和倍数，说的都是整数之间的关系", size=27, color=GOLD)
        end.move_to([0, -2.1, 0])
        self.play(FadeIn(end, shift=UP * 0.06), run_time=0.8)
        self.wait(2.2)
        self.finish_section()

    def construct(self):
        self.scene_queue()
        self.clear_stage()
        self.scene_def()
        self.clear_stage()
        self.scene_factor()
        self.clear_stage()
        self.scene_multiple()
        self.clear_stage()
        self.scene_feature()
        self.clear_stage()
        self.scene_warn()
        self.clear_stage()
        self.scene_summary()
        self.clear_stage(0.8)