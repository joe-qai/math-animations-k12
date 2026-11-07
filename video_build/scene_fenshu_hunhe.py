# -*- coding: utf-8 -*-
"""分数四则混合运算：运算顺序、加减乘除法则、两道例题、简算、易错点。小升初衔接。"""

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
    """把若干文字 / 分数拼成一行算式，竖直居中对齐。"""
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
    """把算式放到指定位置：左边缘对齐 x，竖直中心落在 y。"""
    g.move_to([0, 0, 0])
    g.shift(RIGHT * (x - g.get_left()[0]) + UP * (y - g.get_center()[1]))
    return g


def frac_card(prefix, n, d, color, size=30):
    """带底色的「文字 + 分数」小卡片。"""
    t = txt(prefix, size=size, color=color)
    f = frac(n, d, color=color, size=24)
    g = VGroup(t, f).arrange(RIGHT, buff=0.18)
    box = RoundedRectangle(
        corner_radius=0.18,
        width=g.width + 0.75,
        height=g.height + 0.34,
        stroke_color=color,
        stroke_width=1.6,
        fill_color=color,
        fill_opacity=0.07,
    )
    box.move_to(g)
    return VGroup(box, g)


class FenshuHunheScene(NarratedScene):
    lesson = "fenshu-hunhe"

    def clear_stage(self, run_time: float = 0.5):
        keep = {id(self._track), id(self._fill)}
        junk = [m for m in self.mobjects if id(m) not in keep]
        if junk:
            self.play(*[FadeOut(m) for m in junk], run_time=run_time)
        self.cur_title = None
        self.cur_sub = None

    # ---------------- 0. 一桶油 ---------------- 20.3
    def scene_story(self):
        self.section(0, "一桶油用了多少")

        cards = [
            frac_card("第一次用去", 1, 3, GOLD),
            frac_card("第二次用去剩下的", 1, 2, BLUE),
            label_box("两次一共用去多少？", size=30, color=GREEN),
        ]
        y = 1.85
        for c in cards:
            c.move_to([-2.9, y, 0])
            self.play(FadeIn(c, shift=RIGHT * 0.05), run_time=0.9)
            y -= 1.2

        note = VGroup(
            txt("小学六年学到这儿", size=28, color=CHALK),
            txt("不只是会算，还要会用", size=28, color=DIM),
        ).arrange(DOWN, buff=0.3).move_to([-2.6, -2.0, 0])
        self.play(FadeIn(note[0], shift=UP * 0.05), run_time=0.8)
        self.play(FadeIn(note[1], shift=UP * 0.05), run_time=0.8)

        big = txt("四则", size=96, color=GOLD).move_to([4.2, 1.15, 0])
        sub = txt("混合运算", size=34, color=GOLD).move_to([4.2, 0.15, 0])
        hint = txt("顺序对了，结果才对", size=26, color=DIM).move_to([4.2, -1.05, 0])
        self.play(FadeIn(big, scale=0.93), run_time=1.0)
        self.play(FadeIn(sub, shift=UP * 0.05), run_time=0.8)
        self.play(FadeIn(hint, shift=UP * 0.05), run_time=0.8)
        self.wait(3.4)
        self.finish_section()

    # ---------------- 1. 运算顺序 ---------------- 15.9
    def scene_order(self):
        self.section(1, "分数混合运算的顺序")

        rows = VGroup(
            txt("① 有括号，先算括号里面的", size=31, color=GOLD),
            txt("② 没有括号，先乘除，后加减", size=31, color=CHALK),
            txt("③ 同一级运算，从左往右算", size=31, color=CHALK),
        ).arrange(DOWN, buff=0.55, aligned_edge=LEFT).move_to([-0.7, 1.35, 0])
        for r in rows:
            self.play(FadeIn(r, shift=RIGHT * 0.05), run_time=0.85)
            self.wait(0.2)

        line = expr(["2 + 3 × 4"], size=40).move_to([0, -1.35, 0])
        self.play(FadeIn(line), run_time=0.8)

        wrong = txt("= 20  ✗", size=32, color=RED).move_to([-2.6, -2.2, 0])
        right = txt("= 14  ✓", size=32, color=GREEN).move_to([2.6, -2.2, 0])
        self.play(FadeIn(wrong, shift=UP * 0.05), run_time=0.7)
        self.play(FadeIn(right, shift=UP * 0.05), run_time=0.7)
        self.wait(2.2)
        self.finish_section()

    # ---------------- 2. 加减乘除怎么算 ---------------- 18.6
    def scene_rules(self):
        self.section(2, "加减乘除各自的规矩")

        r1 = expr([txt("加减：", size=30, color=GOLD), frac(1, 2), " + ", frac(1, 3),
                   " = ", frac(5, 6)], size=30)
        place(r1, -3.3, 2.25)
        self.play(FadeIn(r1, shift=RIGHT * 0.05), run_time=0.9)

        r2 = expr([txt("乘法：", size=30, color=BLUE), frac(2, 3), " × ", frac(3, 4),
                   " = ", frac(1, 2)], size=30)
        place(r2, -3.3, 1.25)
        self.play(FadeIn(r2, shift=RIGHT * 0.05), run_time=0.9)

        r3 = expr([txt("除法：", size=30, color=GREEN), frac(3, 4), " ÷ 2 = ",
                   frac(3, 8)], size=30)
        place(r3, -3.3, 0.25)
        self.play(FadeIn(r3, shift=RIGHT * 0.05), run_time=0.9)

        tips = VGroup(
            txt("加减：先通分，再算", size=27, color=GOLD),
            txt("乘法：分子乘分子，分母乘分母", size=27, color=BLUE),
            txt("除法：除以一个数 = 乘它的倒数", size=27, color=GREEN),
        ).arrange(DOWN, buff=0.24, aligned_edge=LEFT).move_to([-0.4, -1.95, 0])
        for t in tips:
            self.play(FadeIn(t, shift=UP * 0.05), run_time=0.7)
        self.wait(1.8)
        self.finish_section()

    # ---------------- 3. 例题一 ---------------- 17.8
    def scene_ex1(self):
        self.section(3, "先算乘法，再通分相加")

        e1 = expr([frac(3, 4), " + ", frac(1, 2), " × ", frac(1, 3)], size=36)
        place(e1, -3.2, 2.35)
        self.play(FadeIn(e1), run_time=0.9)

        rows = [
            expr(["= ", frac(3, 4), " + ", frac(1, 6)], size=34),
            expr(["= ", frac(9, 12), " + ", frac(2, 12)], size=34),
            expr(["= ", frac(11, 12)], size=34),
        ]
        ys = [1.2, -0.1, -1.4]
        for r, y in zip(rows, ys):
            place(r, -3.2, y)
            self.play(FadeIn(r, shift=UP * 0.04), run_time=0.85)

        note = txt("先算 1/2 × 1/3 = 1/6，再通分：分母都变 12", size=27, color=GREEN)
        note.move_to([0, -2.42, 0])
        self.play(FadeIn(note, shift=UP * 0.05), run_time=0.8)
        self.wait(2.2)
        self.finish_section()

    # ---------------- 4. 例题二：带括号 ---------------- 17.6
    def scene_ex2(self):
        self.section(4, "有括号，先算括号")

        e1 = expr(["(", frac(1, 2), " + ", frac(1, 3), ") ÷ ", frac(5, 6)], size=36)
        place(e1, -3.2, 2.35)
        self.play(FadeIn(e1), run_time=0.9)

        rows = [
            expr(["= ", frac(5, 6), " ÷ ", frac(5, 6)], size=34),
            expr(["= ", frac(5, 6), " × ", frac(6, 5)], size=34),
            expr(["= 1"], size=34),
        ]
        ys = [1.2, -0.1, -1.4]
        for r, y in zip(rows, ys):
            place(r, -3.2, y)
            self.play(FadeIn(r, shift=UP * 0.04), run_time=0.85)

        note = txt("括号先通分，除法变乘法，分子分母正好约掉", size=27, color=GREEN)
        note.move_to([0, -2.42, 0])
        self.play(FadeIn(note, shift=UP * 0.05), run_time=0.8)
        self.wait(2.2)
        self.finish_section()

    # ---------------- 5. 简算：乘法分配律 ---------------- 15.9
    def scene_short(self):
        self.section(5, "能简算就别硬算")

        e1 = expr([frac(5, 12), " × 7 + ", frac(5, 12), " × 5"], size=36)
        place(e1, -3.2, 2.35)
        self.play(FadeIn(e1), run_time=0.9)

        rows = [
            expr(["= ", frac(5, 12), " × (7 + 5)"], size=34),
            expr(["= ", frac(5, 12), " × 12"], size=34),
            expr(["= 5"], size=34),
        ]
        ys = [1.2, -0.1, -1.4]
        for r, y in zip(rows, ys):
            place(r, -3.2, y)
            self.play(FadeIn(r, shift=UP * 0.04), run_time=0.85)

        note = txt("提取公因数 5/12，乘法分配律在分数里一样好用", size=27, color=GOLD)
        note.move_to([0, -2.42, 0])
        self.play(FadeIn(note, shift=UP * 0.05), run_time=0.8)
        self.wait(1.8)
        self.finish_section()

    # ---------------- 6. 易错点 + 三句话 ---------------- 17.5
    def scene_warn(self):
        self.section(6, "三个易错点")

        items = [
            ("加减不先通分", "分母不同，先通分"),
            ("除法忘了变乘倒数", "÷ 变 ×，后面取倒数"),
            ("不按顺序，从左往右一路算", "先乘除，后加减"),
        ]
        y = 2.0
        for bad_s, note in items:
            bad = txt(bad_s, size=27, color=RED).move_to([-3.1, y, 0])
            n = txt(note, size=24, color=GREEN).move_to([3.3, y, 0])
            cross = Line(bad.get_left() + [-0.1, -0.08, 0],
                         bad.get_right() + [0.1, 0.18, 0],
                         color=RED, stroke_width=2.8)
            self.play(FadeIn(bad, shift=RIGHT * 0.05), run_time=0.6)
            self.play(Create(cross), FadeIn(n, shift=RIGHT * 0.05), run_time=0.7)
            self.wait(0.5)
            y -= 0.9

        rows = VGroup(
            label_box("① 先乘除，后加减", size=24, color=GOLD),
            label_box("② 有括号，先算括号", size=24, color=CHALK),
            label_box("③ 加减先通分，除法变乘倒数", size=24, color=GREEN),
        ).arrange(DOWN, buff=0.2).move_to([0, -1.6, 0])
        for r in rows:
            self.play(FadeIn(r, shift=RIGHT * 0.06), run_time=0.6)
            self.wait(0.5)

        self.wait(1.0)
        self.finish_section()

    def construct(self):
        self.scene_story()
        self.clear_stage()
        self.scene_order()
        self.clear_stage()
        self.scene_rules()
        self.clear_stage()
        self.scene_ex1()
        self.clear_stage()
        self.scene_ex2()
        self.clear_stage()
        self.scene_short()
        self.clear_stage()
        self.scene_warn()
        self.clear_stage(0.8)