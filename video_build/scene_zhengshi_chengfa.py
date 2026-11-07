# -*- coding: utf-8 -*-
"""整式的乘法：单项式乘单项式、单项式乘多项式、多项式乘多项式、面积模型。七年级下。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


def place(g, x, y):
    """左边缘对齐 x，竖直中心落在 y。"""
    g.move_to([0, 0, 0])
    g.shift(RIGHT * (x - g.get_left()[0]) + UP * (y - g.get_center()[1]))
    return g


def pw(base_s: str, exp_s: str, size: int = 30, color: str = CHALK) -> VGroup:
    """手写「底数 + 上标指数」。"""
    b = txt(base_s, size=size, color=color)
    e = txt(exp_s, size=max(15, int(size * 0.6)), color=color)
    e.next_to(b, RIGHT, buff=0.03)
    e.shift(UP * b.height * 0.34)
    return VGroup(b, e)


def expr(*parts, size: int = 30, buff: float = 0.16, color: str = CHALK) -> VGroup:
    """把若干文字 / 幂拼成一行，底部对齐；中点乘号抬到字高中部。"""
    g = VGroup()
    dots = []
    for p in parts:
        if isinstance(p, str):
            t = txt(p, size=size, color=color)
            g.add(t)
            dots.append(p.strip() in ("·", "⋅"))
        else:
            g.add(p)
            dots.append(False)
    g.arrange(RIGHT, buff=buff, aligned_edge=DOWN)
    for m, is_dot in zip(g, dots):
        if is_dot:
            m.shift(UP * 0.17)
    return g


class ZhengshiChengfaScene(NarratedScene):
    lesson = "zhengshi-chengfa"

    def clear_stage(self, run_time: float = 0.5):
        keep = {id(self._track), id(self._fill)}
        junk = [m for m in self.mobjects if id(m) not in keep]
        if junk:
            self.play(*[FadeOut(m) for m in junk], run_time=run_time)
        self.cur_title = None
        self.cur_sub = None

    # ---------------- 0. 一间教室的座位 ---------------- 23.5
    def scene_story(self):
        self.section(0, "一间教室的座位")

        cells = VGroup()
        for _ in range(5):
            for _ in range(7):
                cells.add(Square(side_length=0.42, stroke_color=BLUE, stroke_width=1.5,
                                 fill_color=BLUE, fill_opacity=0.12))
        cells.arrange_in_grid(rows=5, cols=7, buff=0.08)
        cells.move_to([-4.35, 0.45, 0])
        self.play(LaggedStart(*[FadeIn(c, scale=0.6) for c in cells], lag_ratio=0.03),
                  run_time=2.8)

        top = txt("每排 7 张", size=25, color=BLUE).next_to(cells, UP, buff=0.28)
        left = txt("5 排", size=25, color=BLUE).next_to(cells, LEFT, buff=0.26)
        self.play(FadeIn(top, shift=UP * 0.05), run_time=0.7)
        self.play(FadeIn(left, shift=RIGHT * 0.05), run_time=0.7)

        q = txt("一共多少张桌子？", size=28, color=GOLD).move_to([3.3, 2.15, 0])
        self.play(FadeIn(q, shift=UP * 0.05), run_time=0.8)

        c1 = expr("7 × 5 = 35", size=34, color=CHALK).move_to([3.3, 1.35, 0])
        self.play(FadeIn(c1, shift=UP * 0.05), run_time=0.8)

        sep = Line([1.4, 0.75, 0], [5.4, 0.75, 0], color=DIM, stroke_width=1.6)
        self.play(Create(sep), run_time=0.5)

        q2 = txt("如果每张桌面长 a、宽 b 呢？", size=27, color=CHALK).move_to([3.3, 0.1, 0])
        self.play(FadeIn(q2, shift=UP * 0.05), run_time=0.8)

        c2 = txt("7a × 5b = 35ab", size=36, color=GOLD).move_to([3.3, -0.85, 0])
        self.play(FadeIn(c2, shift=UP * 0.05), run_time=1.0)

        note = txt("系数 7 × 5 = 35，字母 a · b = ab", size=26, color=DIM)
        note.move_to([3.3, -1.8, 0])
        self.play(FadeIn(note, shift=UP * 0.05), run_time=0.8)

        tail = txt("整式的乘法，就是把同类的东西并到一起", size=25, color=DIM)
        tail.move_to([0, -2.6, 0])
        self.play(FadeIn(tail, shift=UP * 0.05), run_time=0.8)
        self.wait(3.0)
        self.finish_section()

    # ---------------- 1. 单项式乘单项式 ---------------- 22.6
    def scene_mono(self):
        self.section(1, "单项式乘单项式")

        head = expr(pw("3x", "2", 34), "·", pw("2x", "3", 34), "=",
                    pw("6x", "5", 34, GOLD), size=34, buff=0.2)
        head.move_to([0, 2.15, 0])
        self.play(FadeIn(head, shift=UP * 0.05), run_time=1.1)

        b1 = label_box("系数：3 × 2 = 6", size=29, color=BLUE).move_to([-3.2, 0.95, 0])
        self.play(FadeIn(b1, scale=0.97), run_time=0.85)

        b2 = label_box("指数：2 + 3 = 5", size=29, color=GREEN).move_to([3.2, 0.95, 0])
        self.play(FadeIn(b2, scale=0.97), run_time=0.85)

        up = Arrow([-3.2, 0.5, 0], [-3.2, -0.1, 0], color=BLUE, buff=0.02,
                   stroke_width=2.6, max_tip_length_to_length_ratio=0.3)
        up2 = Arrow([3.2, 0.5, 0], [3.2, -0.1, 0], color=GREEN, buff=0.02,
                    stroke_width=2.6, max_tip_length_to_length_ratio=0.3)
        self.play(Create(up), Create(up2), run_time=0.7)

        term = VGroup(
            txt("= (3 × 2)", size=30, color=CHALK),
            pw("x", "2+3", 30, GOLD),
            txt("=", size=28, color=DIM),
            pw("6x", "5", 30, GOLD),
        ).arrange(RIGHT, buff=0.18).move_to([0, -0.6, 0])
        self.play(FadeIn(term, shift=UP * 0.05), run_time=0.9)

        rule = label_box("系数相乘，同底数幂相乘", size=30, color=GOLD).move_to([0, -1.75, 0])
        self.play(FadeIn(rule, scale=0.97), run_time=1.0)

        note = txt("字母不同就照抄，字母相同才加指数", size=25, color=DIM).move_to([0, -2.55, 0])
        self.play(FadeIn(note, shift=UP * 0.05), run_time=0.8)
        self.wait(2.6)
        self.finish_section()

    # ---------------- 2. 单项式乘多项式 ---------------- 20.6
    def scene_mono_poly(self):
        self.section(2, "单项式乘多项式：分配律")

        mono = txt("2x", size=36, color=GOLD).move_to([-5.2, 1.05, 0])
        body = txt("(3x + 1)", size=36, color=CHALK).move_to([-2.6, 1.05, 0])
        self.play(FadeIn(mono, shift=RIGHT * 0.05), run_time=0.8)
        self.play(FadeIn(body, shift=RIGHT * 0.05), run_time=0.8)

        u1 = Line([-3.44, 0.6, 0], [-2.95, 0.6, 0], color=GOLD, stroke_width=3.4)
        u2 = Line([-2.16, 0.6, 0], [-1.86, 0.6, 0], color=BLUE, stroke_width=3.4)
        self.play(Create(u1), run_time=0.6)
        self.play(Create(u2), run_time=0.6)

        r1 = expr("2x", "·", "3x", "=", pw("6x", "2", 30, GREEN), size=30)
        r1.move_to([-3.3, -0.5, 0])
        self.play(FadeIn(r1, shift=UP * 0.05), run_time=0.9)

        r2 = expr("2x", "·", "1", "=", "2x", size=30, color=BLUE).move_to([2.5, -0.5, 0])
        self.play(FadeIn(r2, shift=UP * 0.05), run_time=0.9)

        res = VGroup(
            txt("2x(3x + 1)", size=32, color=CHALK),
            txt("=", size=30, color=DIM),
            txt("6x² + 2x", size=32, color=GOLD),
        ).arrange(RIGHT, buff=0.3).move_to([0, -1.75, 0])
        self.play(FadeIn(res, shift=UP * 0.05), run_time=1.0)

        note = txt("括号里每一项都要乘，不能只乘第一项", size=25, color=DIM).move_to([0, -2.55, 0])
        self.play(FadeIn(note, shift=UP * 0.05), run_time=0.8)
        self.wait(2.2)
        self.finish_section()

    # ---------------- 3. 多项式乘多项式 ---------------- 25.0
    def scene_poly(self):
        self.section(3, "多项式乘多项式：逐个相乘")

        head = txt("(x + 2)(x + 3)", size=34, color=CHALK).move_to([0, 2.3, 0])
        self.play(FadeIn(head, shift=UP * 0.05), run_time=0.9)

        rows = VGroup(
            expr("x · x = ", pw("x", "2", 29, BLUE), size=29),
            txt("x · 3 = 3x", size=29, color=CHALK),
            txt("2 · x = 2x", size=29, color=CHALK),
            txt("2 · 3 = 6", size=29, color=CHALK),
        )
        rows.arrange_in_grid(rows=2, cols=2, buff=(1.35, 0.42)).move_to([0, 0.95, 0])
        for r in rows:
            self.play(FadeIn(r, shift=RIGHT * 0.05), run_time=0.7)

        merge = VGroup(
            txt("3x + 2x = 5x", size=30, color=GOLD),
            txt("（合并同类项）", size=24, color=DIM),
        ).arrange(RIGHT, buff=0.3).move_to([0, -0.7, 0])
        self.play(FadeIn(merge, shift=UP * 0.05), run_time=0.9)

        res = VGroup(
            txt("(x + 2)(x + 3)", size=32, color=CHALK),
            txt("=", size=30, color=DIM),
            txt("x² + 5x + 6", size=34, color=GREEN),
        ).arrange(RIGHT, buff=0.3).move_to([0, -1.75, 0])
        self.play(FadeIn(res, shift=UP * 0.05), run_time=1.1)

        note = txt("两个二项式相乘，先得四项，再合并", size=25, color=DIM).move_to([0, -2.6, 0])
        self.play(FadeIn(note, shift=UP * 0.05), run_time=0.8)
        self.wait(2.8)
        self.finish_section()

    # ---------------- 4. 面积模型 ---------------- 22.2
    def scene_area(self):
        self.section(4, "画成一块长方形")

        ox, oy = -4.7, -1.55
        w1, w2 = 1.85, 1.55
        h1, h2 = 1.85, 0.95

        b11 = Rectangle(width=w1, height=h1, stroke_color=GOLD, stroke_width=2,
                        fill_color=GOLD, fill_opacity=0.16)
        b11.move_to([ox + w1 / 2, oy + h2 + h1 / 2, 0])
        b12 = Rectangle(width=w2, height=h1, stroke_color=BLUE, stroke_width=2,
                        fill_color=BLUE, fill_opacity=0.14)
        b12.move_to([ox + w1 + w2 / 2, oy + h2 + h1 / 2, 0])
        b21 = Rectangle(width=w1, height=h2, stroke_color=GREEN, stroke_width=2,
                        fill_color=GREEN, fill_opacity=0.14)
        b21.move_to([ox + w1 / 2, oy + h2 / 2, 0])
        b22 = Rectangle(width=w2, height=h2, stroke_color=ORANGE, stroke_width=2,
                        fill_color=ORANGE, fill_opacity=0.16)
        b22.move_to([ox + w1 + w2 / 2, oy + h2 / 2, 0])

        self.play(Create(b11), Create(b12), Create(b21), Create(b22), run_time=1.4)

        l11 = expr(pw("x", "2", 30, GOLD), size=30).move_to(b11.get_center())
        l12 = txt("3x", size=30, color=BLUE).move_to(b12.get_center())
        l21 = txt("2x", size=30, color=GREEN).move_to(b21.get_center())
        l22 = txt("6", size=30, color=ORANGE).move_to(b22.get_center())
        for lab in (l11, l12, l21, l22):
            self.play(FadeIn(lab, scale=0.9), run_time=0.6)

        tx = txt("x", size=27, color=GOLD).move_to([ox + w1 / 2, oy + h1 + h2 + 0.3, 0])
        t3 = txt("3", size=27, color=BLUE).move_to([ox + w1 + w2 / 2, oy + h1 + h2 + 0.3, 0])
        lx = txt("x", size=27, color=GREEN).move_to([ox - 0.3, oy + h2 + h1 / 2, 0])
        l2 = txt("2", size=27, color=ORANGE).move_to([ox - 0.3, oy + h2 / 2, 0])
        self.play(FadeIn(tx), FadeIn(t3), FadeIn(lx), FadeIn(l2), run_time=0.9)

        cap = txt("长 x + 3，宽 x + 2", size=26, color=CHALK).move_to([2.75, 1.45, 0])
        self.play(FadeIn(cap, shift=UP * 0.05), run_time=0.8)

        sum1 = txt("四块面积相加：", size=26, color=CHALK).move_to([2.75, 0.7, 0])
        self.play(FadeIn(sum1, shift=UP * 0.05), run_time=0.7)

        sum2 = VGroup(
            pw("x", "2", 28, GOLD),
            txt("+ 3x + 2x + 6", size=28, color=CHALK),
        ).arrange(RIGHT, buff=0.12).move_to([2.75, -0.05, 0])
        self.play(FadeIn(sum2, shift=UP * 0.05), run_time=0.8)

        sum3 = VGroup(
            txt("=", size=28, color=DIM),
            pw("x", "2", 30, GREEN),
            txt("+ 5x + 6", size=30, color=GREEN),
        ).arrange(RIGHT, buff=0.16).move_to([2.75, -0.85, 0])
        self.play(FadeIn(sum3, shift=UP * 0.05), run_time=0.9)

        note = txt("分块求面积，再把同类项并起来", size=25, color=DIM).move_to([0, -2.6, 0])
        self.play(FadeIn(note, shift=UP * 0.05), run_time=0.8)
        self.wait(3.0)
        self.finish_section()

    # ---------------- 5. 例题 ---------------- 22.1
    def scene_ex(self):
        self.section(5, "例题：负号不要漏")

        head = txt("(2x − 1)(x + 3)", size=34, color=CHALK).move_to([0, 2.25, 0])
        self.play(FadeIn(head, shift=UP * 0.05), run_time=0.9)

        l1 = expr("2x", "·", "x", "=", pw("2x", "2", 29, BLUE), size=29)
        l2 = expr("2x", "·", "3 = 6x", size=29)
        l3 = txt("(−1) · x = −x", size=29, color=CHALK)
        l4 = txt("(−1) · 3 = −3", size=29, color=CHALK)
        rows = VGroup(l1, l2, l3, l4).arrange_in_grid(rows=2, cols=2, buff=(1.5, 0.4))
        rows.move_to([0, 0.85, 0])
        for r in rows:
            self.play(FadeIn(r, shift=RIGHT * 0.05), run_time=0.65)

        merge = VGroup(
            txt("6x − x = 5x", size=30, color=GOLD),
            txt("（合并同类项）", size=24, color=DIM),
        ).arrange(RIGHT, buff=0.3).move_to([0, -0.8, 0])
        self.play(FadeIn(merge, shift=UP * 0.05), run_time=0.9)

        res = VGroup(
            txt("(2x − 1)(x + 3)", size=31, color=CHALK),
            txt("=", size=29, color=DIM),
            txt("2x² + 5x − 3", size=32, color=GREEN),
        ).arrange(RIGHT, buff=0.28).move_to([0, -1.8, 0])
        self.play(FadeIn(res, shift=UP * 0.05), run_time=1.1)

        note = txt("负号乘进去要变号，最后别忘了合并", size=25, color=DIM).move_to([0, -2.6, 0])
        self.play(FadeIn(note, shift=UP * 0.05), run_time=0.8)
        self.wait(2.6)
        self.finish_section()

    # ---------------- 6. 三个易错点 ---------------- 23.7
    def scene_pitfall(self):
        self.section(6, "三个易错点")

        items = [
            ("漏乘：只乘了第一项", "每一项都要乘"),
            ("符号：负号乘进去没变号", "把括号看成整体"),
            ("最后没合并同类项", "3x + 2x = 5x"),
        ]
        y = 1.55
        for bad_s, good_s in items:
            bad = txt(bad_s, size=26, color=RED).move_to([-3.3, y, 0])
            good = txt(good_s, size=25, color=GREEN).move_to([3.4, y, 0])
            cross = Line([bad.get_left()[0] - 0.08, y - 0.075, 0],
                         [bad.get_right()[0] + 0.08, y - 0.075, 0],
                         color=RED, stroke_width=2.4)
            self.play(FadeIn(bad, shift=RIGHT * 0.05), run_time=0.6)
            self.play(Create(cross), run_time=0.4)
            self.play(FadeIn(good, shift=RIGHT * 0.05), run_time=0.6)
            y -= 1.15

        tip = label_box("先数项数，再合并同类项", size=30, color=GOLD).move_to([0, -2.2, 0])
        self.play(FadeIn(tip, scale=0.97), run_time=1.0)

        self.wait(2.4)
        self.finish_section()

    def construct(self):
        self.scene_story()
        self.clear_stage()
        self.scene_mono()
        self.clear_stage()
        self.scene_mono_poly()
        self.clear_stage()
        self.scene_poly()
        self.clear_stage()
        self.scene_area()
        self.clear_stage()
        self.scene_ex()
        self.clear_stage()
        self.scene_pitfall()
        self.clear_stage(0.8)