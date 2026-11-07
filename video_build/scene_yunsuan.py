# -*- coding: utf-8 -*-
"""运算律：加法/乘法交换与结合、乘法分配律、简便计算。四年级上册。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


def dot_grid(rows: int, cols: int, center, color: str = GOLD,
             gap: float = 0.52, r: float = 0.12) -> VGroup:
    g = VGroup()
    w = (cols - 1) * gap
    h = (rows - 1) * gap
    for i in range(rows):
        for j in range(cols):
            g.add(Dot([center[0] - w / 2 + j * gap,
                       center[1] + h / 2 - i * gap, 0],
                      radius=r, color=color))
    return g


class YunSuanLvScene(NarratedScene):
    lesson = "yun-suanlv"

    def clear_stage(self, run_time: float = 0.5):
        keep = {id(self._track), id(self._fill)}
        junk = [m for m in self.mobjects if id(m) not in keep]
        if junk:
            self.play(*[FadeOut(m) for m in junk], run_time=run_time)
        self.cur_title = None
        self.cur_sub = None

    # ---------------- 0. 摆椅子 ---------------- 14.3
    def scene_story(self):
        self.section(0, "四行六把，六行四把")

        left = dot_grid(4, 6, [-4.3, 0.85])
        self.play(LaggedStart(*[FadeIn(d) for d in left], lag_ratio=0.02), run_time=1.6)
        l_lab = txt("4 行 × 6 把", size=28, color=GOLD).move_to([-4.3, -0.55, 0])
        l_eq = txt("4 × 6 = 24", size=34, color=CHALK).move_to([-4.3, -1.35, 0])
        self.play(FadeIn(l_lab, shift=UP * 0.05), run_time=0.6)

        right = dot_grid(6, 4, [3.3, 1.15], color=BLUE, gap=0.44)
        self.play(LaggedStart(*[FadeIn(d) for d in right], lag_ratio=0.02), run_time=1.6)
        r_lab = txt("6 行 × 4 把", size=28, color=BLUE).move_to([3.3, -0.55, 0])
        r_eq = txt("6 × 4 = 24", size=34, color=CHALK).move_to([3.3, -1.35, 0])
        self.play(FadeIn(r_lab, shift=UP * 0.05), run_time=0.6)

        self.play(FadeIn(l_eq, shift=UP * 0.06), run_time=0.7)
        self.play(FadeIn(r_eq, shift=UP * 0.06), run_time=0.7)

        note = txt("换个顺序、换个分组，结果都一样", size=28, color=GREEN)
        note.move_to([-0.5, -2.35, 0])
        self.play(FadeIn(note, shift=UP * 0.08), run_time=0.9)
        self.finish_section()

    # ---------------- 1. 加法交换、结合 ---------------- 19.1
    def scene_add(self):
        self.section(1, "加法交换律、结合律")

        f1 = txt("35 + 65 = 65 + 35", size=36, color=GOLD).move_to([0, 2.15, 0])
        r1 = txt("交换位置，和不变", size=25, color=DIM).move_to([0, 1.55, 0])
        self.play(FadeIn(f1, shift=UP * 0.06), run_time=0.9)
        self.play(FadeIn(r1), run_time=0.6)

        a = txt("(28 + 35) + 65", size=32, color=CHALK).move_to([-2.2, 0.55, 0])
        a2 = txt("= 63 + 65 = 128", size=32, color=CHALK).move_to([3.0, 0.55, 0])
        b = txt("28 + (35 + 65)", size=32, color=CHALK).move_to([-2.2, -0.5, 0])
        b2 = txt("= 28 + 100 = 128", size=32, color=BLUE).move_to([3.0, -0.5, 0])
        self.play(FadeIn(a, shift=RIGHT * 0.06), run_time=0.7)
        self.play(FadeIn(a2, shift=LEFT * 0.06), run_time=0.7)
        self.play(FadeIn(b, shift=RIGHT * 0.06), run_time=0.7)

        hl = Indicate(b, color=GOLD, scale_factor=1.05)
        self.play(hl, run_time=0.8)
        self.play(FadeIn(b2, shift=LEFT * 0.06), run_time=0.8)

        note = txt("先把能凑成整百的两个数加起来", size=28, color=GREEN)
        note.move_to([0, -1.55, 0])
        tip = txt("这叫加法结合律：先加哪两个，结果一样", size=25, color=DIM)
        tip.move_to([0, -2.25, 0])
        self.play(FadeIn(note, shift=UP * 0.08), run_time=0.8)
        self.play(FadeIn(tip, shift=UP * 0.06), run_time=0.8)
        self.finish_section()

    # ---------------- 2. 乘法交换、结合 ---------------- 19.1
    def scene_mul(self):
        self.section(2, "乘法交换律、结合律")

        f1 = txt("3 × 4 = 4 × 3 = 12", size=36, color=GOLD).move_to([0, 2.15, 0])
        r1 = txt("交换位置，积不变", size=25, color=DIM).move_to([0, 1.55, 0])
        self.play(FadeIn(f1, shift=UP * 0.06), run_time=0.9)
        self.play(FadeIn(r1), run_time=0.6)

        a = txt("(17 × 2) × 5", size=32, color=CHALK).move_to([-2.5, 0.55, 0])
        a2 = txt("= 34 × 5 = 170", size=32, color=CHALK).move_to([3.0, 0.55, 0])
        b = txt("17 × (2 × 5)", size=32, color=CHALK).move_to([-2.5, -0.5, 0])
        b2 = txt("= 17 × 10 = 170", size=32, color=BLUE).move_to([3.0, -0.5, 0])
        self.play(FadeIn(a, shift=RIGHT * 0.06), run_time=0.7)
        self.play(FadeIn(a2, shift=LEFT * 0.06), run_time=0.7)
        self.play(FadeIn(b, shift=RIGHT * 0.06), run_time=0.7)

        hl = Indicate(b, color=GOLD, scale_factor=1.05)
        self.play(hl, run_time=0.8)
        self.play(FadeIn(b2, shift=LEFT * 0.06), run_time=0.8)

        note = txt("先算 2 × 5 得整十，再乘就简单", size=28, color=GREEN)
        note.move_to([0, -1.55, 0])
        tip = txt("这叫乘法结合律：先乘哪两个，结果一样", size=25, color=DIM)
        tip.move_to([0, -2.25, 0])
        self.play(FadeIn(note, shift=UP * 0.08), run_time=0.8)
        self.play(FadeIn(tip, shift=UP * 0.06), run_time=0.8)
        self.finish_section()

    # ---------------- 3. 乘法分配律 ---------------- 17.1
    def scene_dist(self):
        self.section(3, "乘法分配律：拆开算")

        # 面积模型：长 (4 + 6)，宽 25
        y0 = 1.05
        h = 2.0
        left_w, right_w = 1.9, 2.85
        x0 = -6.0
        big = Rectangle(width=left_w + right_w, height=h, color=CHALK, stroke_width=2.2)
        big.move_to([x0 + (left_w + right_w) / 2, y0, 0])
        p1 = Rectangle(width=left_w, height=h, color=GOLD, stroke_width=1.6,
                       fill_color=GOLD, fill_opacity=0.2).move_to([x0 + left_w / 2, y0, 0])
        p2 = Rectangle(width=right_w, height=h, color=BLUE, stroke_width=1.6,
                       fill_color=BLUE, fill_opacity=0.2).move_to([x0 + left_w + right_w / 2, y0, 0])
        self.play(Create(big), run_time=0.8)
        self.play(FadeIn(p1), FadeIn(p2), run_time=0.9)

        t1 = txt("4 × 25", size=26, color=GOLD).move_to([x0 + left_w / 2, y0, 0])
        t2 = txt("6 × 25", size=26, color=BLUE).move_to([x0 + left_w + right_w / 2, y0, 0])
        self.play(FadeIn(t1), FadeIn(t2), run_time=0.7)

        d4 = txt("4", size=26, color=GOLD).move_to([x0 + left_w / 2, y0 - h / 2 - 0.28, 0])
        d6 = txt("6", size=26, color=BLUE).move_to([x0 + left_w + right_w / 2, y0 - h / 2 - 0.28, 0])
        d25 = txt("25", size=26, color=CHALK).move_to([x0 - 0.4, y0, 0])
        self.play(FadeIn(d4), FadeIn(d6), FadeIn(d25), run_time=0.7)

        e1 = txt("(4 + 6) × 25", size=30, color=CHALK).move_to([3.3, 1.25, 0])
        e2 = txt("= 4 × 25 + 6 × 25", size=30, color=CHALK).move_to([3.3, 0.45, 0])
        e3 = txt("= 100 + 150 = 250", size=30, color=GOLD).move_to([3.3, -0.35, 0])
        self.play(FadeIn(e1, shift=RIGHT * 0.06), run_time=0.8)
        self.play(FadeIn(e2, shift=RIGHT * 0.06), run_time=0.9)
        self.play(FadeIn(e3, shift=RIGHT * 0.06), run_time=0.8)

        note = txt("反过来：两个积相加，也能合成和乘一个数", size=25, color=GREEN)
        note.move_to([0, -1.85, 0])
        self.play(FadeIn(note, shift=UP * 0.08), run_time=0.9)
        self.finish_section()

    # ---------------- 4. 简便计算 ---------------- 15.9
    def scene_quick(self):
        self.section(4, "看到 25 找 4，看到 125 找 8")

        g1 = label_box("25 × 4 = 100", size=32, color=GOLD)
        g2 = label_box("125 × 8 = 1000", size=32, color=GOLD)
        g1.move_to([-3.4, 1.75, 0])
        g2.move_to([3.4, 1.75, 0])
        self.play(FadeIn(g1, scale=0.95), run_time=0.9)
        self.play(FadeIn(g2, scale=0.95), run_time=0.9)

        q1 = txt("99 × 26 = (100 − 1) × 26", size=30, color=CHALK).move_to([0, 0.6, 0])
        q1c = txt("= 2600 − 26 = 2574", size=30, color=GREEN).move_to([0, -0.1, 0])
        self.play(FadeIn(q1), run_time=0.8)
        self.play(FadeIn(q1c, shift=UP * 0.05), run_time=0.9)

        q2 = txt("101 × 26 = (100 + 1) × 26", size=30, color=CHALK).move_to([0, -1.15, 0])
        q2c = txt("= 2600 + 26 = 2626", size=30, color=GREEN).move_to([0, -1.85, 0])
        self.play(FadeIn(q2), run_time=0.8)
        self.play(FadeIn(q2c, shift=UP * 0.05), run_time=0.9)
        self.finish_section()

    # ---------------- 5. 易错 ---------------- 16.2
    def scene_warn(self):
        self.section(5, "分配律只对加减管用")

        ok = txt("25 × (4 + 8)", size=32, color=GREEN).move_to([-4.5, 1.55, 0])
        ok2 = txt("= 25 × 4 + 25 × 8", size=30, color=CHALK).move_to([0.7, 1.55, 0])
        ok3 = txt("= 300", size=30, color=GREEN).move_to([4.4, 1.55, 0])
        self.play(FadeIn(ok), run_time=0.6)
        self.play(FadeIn(ok2, shift=RIGHT * 0.06), run_time=0.8)
        self.play(FadeIn(ok3, shift=RIGHT * 0.06), run_time=0.6)

        bad = txt("25 × (4 × 8) = 800", size=32, color=CHALK).move_to([-3.35, 0.3, 0])
        self.play(FadeIn(bad), run_time=0.7)

        bad2 = txt("错：不能拆成 25 × 4 + 25 × 8", size=29, color=RED)
        bad2.move_to([-0.05, -0.5, 0])
        self.play(FadeIn(bad2, shift=RIGHT * 0.06), run_time=0.9)

        n1 = txt("乘法对乘法不能分配", size=27, color=DIM)
        n1.move_to([0, -1.35, 0])
        self.play(FadeIn(n1, shift=UP * 0.06), run_time=0.8)

        n2 = txt("减法和除法没有交换律", size=28, color=GOLD).move_to([0, -2.0, 0])
        ex = txt("8 − 3 ≠ 3 − 8", size=30, color=CHALK).move_to([0, -2.6, 0])
        self.play(FadeIn(n2, shift=UP * 0.06), run_time=0.7)
        self.play(FadeIn(ex, shift=UP * 0.06), run_time=0.7)
        self.finish_section()

    # ---------------- 6. 总结 ---------------- 15.0
    def scene_summary(self):
        self.section(6, "五个运算律，一句话")

        top = VGroup(
            label_box("加法交换", size=28, color=GOLD),
            label_box("加法结合", size=28, color=GOLD),
            label_box("乘法交换", size=28, color=BLUE),
        ).arrange(RIGHT, buff=0.45).move_to([0, 2.05, 0])
        bot = VGroup(
            label_box("乘法结合", size=28, color=BLUE),
            label_box("乘法分配", size=28, color=GREEN),
        ).arrange(RIGHT, buff=0.45).move_to([0, 1.2, 0])
        self.play(LaggedStart(*[FadeIn(m, shift=UP * 0.06) for m in top], lag_ratio=0.25), run_time=1.2)
        self.play(LaggedStart(*[FadeIn(m, shift=UP * 0.06) for m in bot], lag_ratio=0.25), run_time=1.0)

        tips = VGroup(
            label_box("见 25 找 4", size=28, color=ORANGE),
            label_box("见 125 找 8", size=28, color=ORANGE),
            label_box("见 99 想 100 − 1", size=28, color=ORANGE),
        ).arrange(RIGHT, buff=0.4).move_to([0, -0.25, 0])
        self.play(LaggedStart(*[FadeIn(t, scale=0.95) for t in tips], lag_ratio=0.3), run_time=1.4)

        note = txt("先观察数字特点，再决定用哪条律", size=27, color=GREEN)
        note.move_to([0, -1.55, 0])
        self.play(FadeIn(note, shift=UP * 0.08), run_time=0.8)

        end = txt("算得对，还要算得快", size=30, color=GOLD).move_to([0, -2.3, 0])
        self.play(FadeIn(end, shift=UP * 0.06), run_time=0.8)
        self.wait(1.0)
        self.finish_section()

    def construct(self):
        self.scene_story()
        self.clear_stage()
        self.scene_add()
        self.clear_stage()
        self.scene_mul()
        self.clear_stage()
        self.scene_dist()
        self.clear_stage()
        self.scene_quick()
        self.clear_stage()
        self.scene_warn()
        self.clear_stage()
        self.scene_summary()
        self.clear_stage(0.8)