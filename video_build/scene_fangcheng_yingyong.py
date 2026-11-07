# -*- coding: utf-8 -*-
"""用方程解应用题：四步法、设未知数、解方程步骤、两道例题、易错点。小升初衔接。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


def place(g, x, y):
    """左边缘对齐 x，竖直中心落在 y。"""
    g.move_to([0, 0, 0])
    g.shift(RIGHT * (x - g.get_left()[0]) + UP * (y - g.get_center()[1]))
    return g


class FangchengYingyongScene(NarratedScene):
    lesson = "fangcheng-yingyong"

    def clear_stage(self, run_time: float = 0.5):
        keep = {id(self._track), id(self._fill)}
        junk = [m for m in self.mobjects if id(m) not in keep]
        if junk:
            self.play(*[FadeOut(m) for m in junk], run_time=run_time)
        self.cur_title = None
        self.cur_sub = None

    # ---------------- 0. 买笔和本子 ---------------- 16.0
    def scene_story(self):
        self.section(0, "买笔和本子")

        c1 = label_box("3 支笔，每支 3 元", size=32, color=GOLD).move_to([-2.7, 1.75, 0])
        c2 = label_box("2 个本子", size=32, color=BLUE).move_to([-2.7, 0.6, 0])
        c3 = label_box("一共 19 元", size=32, color=GREEN).move_to([-2.7, -0.55, 0])
        for c in (c1, c2, c3):
            self.play(FadeIn(c, shift=RIGHT * 0.06), run_time=0.8)

        q = txt("本子多少钱一本？", size=36, color=GOLD).move_to([3.5, 1.1, 0])
        self.play(FadeIn(q, scale=0.97), run_time=0.9)

        note = VGroup(
            txt("算术要倒着推", size=28, color=DIM),
            txt("方程可以正着列", size=28, color=CHALK),
        ).arrange(DOWN, buff=0.3).move_to([3.5, -0.9, 0])
        self.play(FadeIn(note[0], shift=UP * 0.05), run_time=0.7)
        self.play(FadeIn(note[1], shift=UP * 0.05), run_time=0.7)
        self.wait(2.8)
        self.finish_section()

    # ---------------- 1. 列方程四步 ---------------- 17.8
    def scene_steps(self):
        self.section(1, "列方程四步法")

        steps = VGroup(
            txt("① 设：问什么设什么", size=31, color=GOLD),
            txt("② 找：圈出相等的那句话", size=31, color=CHALK),
            txt("③ 列：按等量关系写方程", size=31, color=CHALK),
            txt("④ 解：解完代回去检验", size=31, color=GREEN),
        ).arrange(DOWN, buff=0.45, aligned_edge=LEFT).move_to([-1.0, 1.05, 0])
        for s in steps:
            self.play(FadeIn(s, shift=RIGHT * 0.05), run_time=0.85)
            self.wait(0.15)

        flow = VGroup(
            label_box("设", size=24, color=GOLD),
            txt("→", size=26, color=DIM),
            label_box("找", size=24, color=CHALK),
            txt("→", size=26, color=DIM),
            label_box("列", size=24, color=CHALK),
            txt("→", size=26, color=DIM),
            label_box("解", size=24, color=GREEN),
            txt("→", size=26, color=DIM),
            label_box("验", size=24, color=GREEN),
        ).arrange(RIGHT, buff=0.2).move_to([0, -1.45, 0])
        self.play(FadeIn(flow), run_time=1.0)
        self.wait(2.0)
        self.finish_section()

    # ---------------- 2. 怎么设未知数 ---------------- 14.3
    def scene_set(self):
        self.section(2, "未知数怎么设")

        a = txt("问什么就设什么", size=34, color=GOLD).move_to([0, 2.1, 0])
        self.play(FadeIn(a, shift=UP * 0.05), run_time=0.9)

        rows1 = VGroup(
            txt("问本子多少钱，就设本子 x 元", size=30, color=CHALK),
            txt("一句话就能列式，最省事", size=29, color=DIM),
        ).arrange(DOWN, buff=0.36, aligned_edge=LEFT).move_to([-0.9, 1.0, 0])
        for r in rows1:
            self.play(FadeIn(r, shift=RIGHT * 0.05), run_time=0.7)

        b = txt("两个未知量，设关键的那个", size=34, color=BLUE).move_to([0, -0.5, 0])
        self.play(FadeIn(b, shift=UP * 0.05), run_time=0.9)

        rows2 = VGroup(
            txt("甲乙之和 48，甲是乙的 3 倍", size=29, color=CHALK),
            txt("设乙为 x，甲就写成 3x", size=29, color=GREEN),
        ).arrange(DOWN, buff=0.36, aligned_edge=LEFT).move_to([-0.6, -1.65, 0])
        for r in rows2:
            self.play(FadeIn(r, shift=RIGHT * 0.05), run_time=0.7)
        self.wait(1.8)
        self.finish_section()

    # ---------------- 3. 解方程步骤 ---------------- 14.5
    def scene_solve(self):
        self.section(3, "解方程的固定顺序")

        box = label_box("去分母 → 去括号 → 移项 → 合并 → 系数化 1", size=29, color=GOLD)
        box.move_to([0, 2.2, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.1)

        rows = VGroup(
            txt("有分母：两边同乘分母", size=30, color=CHALK),
            txt("有括号：先去括号，注意变号", size=30, color=CHALK),
            txt("移项：跨过等号要变号", size=30, color=RED),
            txt("最后除以系数，得到 x", size=30, color=GREEN),
        ).arrange(DOWN, buff=0.42, aligned_edge=LEFT).move_to([-0.8, -0.05, 0])
        for r in rows:
            self.play(FadeIn(r, shift=RIGHT * 0.05), run_time=0.8)
            self.wait(0.1)

        tip = txt("移项不变号，是失分最多的地方", size=28, color=GOLD)
        tip.move_to([0, -2.1, 0])
        self.play(FadeIn(tip, shift=UP * 0.05), run_time=0.8)
        self.wait(1.6)
        self.finish_section()

    # ---------------- 4. 例题一 ---------------- 18.6
    def scene_ex1(self):
        self.section(4, "三支笔两个本子")

        prob = txt("笔每支 3 元，2 个本子共 19 元", size=29, color=CHALK).move_to([0, 2.35, 0])
        self.play(FadeIn(prob, shift=UP * 0.05), run_time=0.8)

        head = txt("设本子每本 x 元", size=32, color=GOLD).move_to([-2.3, 1.55, 0])
        self.play(FadeIn(head, shift=RIGHT * 0.05), run_time=0.8)

        rows = [
            ("等量关系：笔的钱 + 本子的钱 = 19", DIM),
            ("9 + 2x = 19", CHALK),
            ("2x = 19 - 9", BLUE),
            ("2x = 10", BLUE),
            ("x = 5", GREEN),
        ]
        y = 0.7
        for s, c in rows:
            self.play(FadeIn(txt(s, size=31, color=c).move_to([-2.5, y, 0]),
                             shift=UP * 0.04), run_time=0.72)
            y -= 0.62

        ans = label_box("答：本子每本 5 元", size=30, color=GOLD).move_to([0, -2.45, 0])
        self.play(FadeIn(ans, scale=0.97), run_time=0.85)
        self.wait(2.0)
        self.finish_section()

    # ---------------- 5. 例题二：和倍问题 ---------------- 18.0
    def scene_ex2(self):
        self.section(5, "甲乙两数之和是 48")

        prob = txt("甲乙之和 48，甲是乙的 3 倍", size=30, color=CHALK).move_to([0, 2.35, 0])
        self.play(FadeIn(prob, shift=UP * 0.05), run_time=0.8)

        head = txt("设乙为 x，甲就是 3x", size=32, color=GOLD).move_to([-1.6, 1.55, 0])
        self.play(FadeIn(head, shift=RIGHT * 0.05), run_time=0.8)

        rows = [
            ("x + 3x = 48", CHALK),
            ("4x = 48", BLUE),
            ("x = 12", GREEN),
            ("甲 = 3 × 12 = 36", GREEN),
        ]
        y = 0.75
        for s, c in rows:
            self.play(FadeIn(txt(s, size=33, color=c).move_to([-1.4, y, 0]),
                             shift=UP * 0.04), run_time=0.75)
            y -= 0.68

        ans = label_box("答：乙是 12，甲是 36", size=30, color=GOLD).move_to([0, -2.4, 0])
        self.play(FadeIn(ans, scale=0.97), run_time=0.85)
        self.wait(2.0)
        self.finish_section()

    # ---------------- 6. 易错点 + 三句话 ---------------- 14.7
    def scene_warn(self):
        self.section(6, "三个易错点")

        items = [
            ("设未知数不写单位", "x 后面写明元、个"),
            ("移项忘记变号", "跨过等号就变号"),
            ("算完不检验、不写答", "代回去，再写答"),
        ]
        y = 2.05
        for bad_s, note in items:
            bad = txt(bad_s, size=27, color=RED).move_to([-3.2, y, 0])
            n = txt(note, size=24, color=GREEN).move_to([3.3, y, 0])
            cross = Line(bad.get_left() + [-0.1, -0.08, 0],
                         bad.get_right() + [0.1, 0.18, 0],
                         color=RED, stroke_width=2.8)
            self.play(FadeIn(bad, shift=RIGHT * 0.05), run_time=0.6)
            self.play(Create(cross), FadeIn(n, shift=RIGHT * 0.05), run_time=0.7)
            self.wait(0.4)
            y -= 0.9

        rows = VGroup(
            label_box("① 先设未知数", size=24, color=GOLD),
            label_box("② 找出等量关系", size=24, color=CHALK),
            label_box("③ 移项变号，最后检验", size=24, color=GREEN),
        ).arrange(DOWN, buff=0.18).move_to([0, -1.85, 0])
        for r in rows:
            self.play(FadeIn(r, shift=RIGHT * 0.06), run_time=0.6)
            self.wait(0.4)

        self.wait(0.8)
        self.finish_section()

    def construct(self):
        self.scene_story()
        self.clear_stage()
        self.scene_steps()
        self.clear_stage()
        self.scene_set()
        self.clear_stage()
        self.scene_solve()
        self.clear_stage()
        self.scene_ex1()
        self.clear_stage()
        self.scene_ex2()
        self.clear_stage()
        self.scene_warn()
        self.clear_stage(0.8)