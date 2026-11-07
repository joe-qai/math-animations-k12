# -*- coding: utf-8 -*-
"""平方差公式：剪拼图形、代数展开、(a+b)(a-b)=a²-b²。七年级下。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


def place(g, x, y):
    g.move_to([0, 0, 0])
    g.shift(RIGHT * (x - g.get_left()[0]) + UP * (y - g.get_center()[1]))
    return g


def pw(base_s: str, exp_s: str, size: int = 30, color: str = CHALK) -> VGroup:
    b = txt(base_s, size=size, color=color)
    e = txt(exp_s, size=max(15, int(size * 0.6)), color=color)
    e.next_to(b, RIGHT, buff=0.03)
    e.shift(UP * b.height * 0.34)
    return VGroup(b, e)


def expr(*parts, size: int = 30, buff: float = 0.16, color: str = CHALK) -> VGroup:
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


class PingfangChaScene(NarratedScene):
    lesson = "pingfang-cha"

    def clear_stage(self, run_time: float = 0.5):
        keep = {id(self._track), id(self._fill)}
        junk = [m for m in self.mobjects if id(m) not in keep]
        if junk:
            self.play(*[FadeOut(m) for m in junk], run_time=run_time)
        self.cur_title = None
        self.cur_sub = None

    # ---------------- 0. 剪掉一个小正方形 ---------------- 16.5
    def scene_cut(self):
        self.section(0, "剪掉一个角，剩下 L 形")

        a, b = 2.6, 0.95
        ox, oy = -4.6, -1.3
        big = Square(side_length=a, stroke_color=CHALK, stroke_width=2.2,
                     fill_color=CHALK, fill_opacity=0.07)
        big.move_to([ox + a / 2, oy + a / 2, 0])
        self.play(Create(big), run_time=1.1)

        side_a1 = txt("a", size=27, color=GOLD).move_to([ox + a / 2, oy + a + 0.3, 0])
        side_a2 = txt("a", size=27, color=GOLD).move_to([ox - 0.3, oy + a / 2, 0])
        self.play(FadeIn(side_a1), FadeIn(side_a2), run_time=0.7)

        small = Square(side_length=b, stroke_color=RED, stroke_width=2,
                       fill_color=RED, fill_opacity=0.24)
        small.move_to([ox + a - b / 2, oy + a - b / 2, 0])
        self.play(Create(small), run_time=0.9)

        sb = VGroup(
            txt("b", size=24, color=RED).move_to([ox + a - b / 2, oy + a + 0.24, 0]),
            txt("b", size=24, color=RED).move_to([ox + a + 0.26, oy + a - b / 2, 0]),
        )
        self.play(FadeIn(sb), run_time=0.6)

        sl = expr(pw("b", "2", 26, RED), size=26).move_to(small.get_center())
        self.play(FadeIn(sl, scale=0.9), run_time=0.7)

        right = VGroup(
            txt("大正方形：", size=27, color=CHALK),
            pw("a", "2", 28, GOLD),
        ).arrange(RIGHT, buff=0.18).move_to([2.9, 1.15, 0])
        self.play(FadeIn(right, shift=UP * 0.05), run_time=0.8)

        right2 = VGroup(
            txt("小正方形：", size=27, color=CHALK),
            pw("b", "2", 28, RED),
        ).arrange(RIGHT, buff=0.18).move_to([2.9, 0.2, 0])
        self.play(FadeIn(right2, shift=UP * 0.05), run_time=0.8)

        self.play(FadeOut(small), FadeOut(sl), FadeOut(sb), run_time=0.9)

        lshape = Polygon(
            [ox, oy, 0], [ox + a, oy, 0], [ox + a, oy + a - b, 0],
            [ox + a - b, oy + a - b, 0], [ox + a - b, oy + a, 0], [ox, oy + a, 0],
            color=GOLD, stroke_width=2.2, fill_color=GOLD, fill_opacity=0.2,
        )
        self.play(Create(lshape), run_time=1.2)

        res = VGroup(
            txt("剩下的面积 =", size=27, color=CHALK),
            pw("a", "2", 30, GOLD),
            txt("−", size=27, color=DIM),
            pw("b", "2", 30, RED),
        ).arrange(RIGHT, buff=0.18).move_to([2.9, -0.9, 0])
        self.play(FadeIn(res, shift=UP * 0.05), run_time=0.9)

        note = txt("面积没有凭空消失，只是少了一块", size=25, color=DIM).move_to([2.9, -1.85, 0])
        self.play(FadeIn(note, shift=UP * 0.05), run_time=0.8)
        self.wait(2.0)
        self.finish_section()

    # ---------------- 1. 剪拼成长方形 ---------------- 17.0
    def scene_puzzle(self):
        self.section(1, "剪一刀，拼成长方形")

        a, b = 2.6, 0.95
        ox, oy = -4.6, -1.3
        w1, h1 = a, a - b

        p1 = Rectangle(width=w1, height=h1, stroke_color=GOLD, stroke_width=2,
                       fill_color=GOLD, fill_opacity=0.2)
        p1.move_to([ox + w1 / 2, oy + h1 / 2, 0])
        p2 = Rectangle(width=a - b, height=b, stroke_color=BLUE, stroke_width=2,
                       fill_color=BLUE, fill_opacity=0.22)
        p2.move_to([ox + (a - b) / 2, oy + h1 + b / 2, 0])

        self.play(Create(p1), run_time=0.9)
        self.play(Create(p2), run_time=0.9)

        l1 = txt("①", size=28, color=GOLD).move_to(p1.get_center())
        l2 = txt("②", size=28, color=BLUE).move_to(p2.get_center())
        self.play(FadeIn(l1), FadeIn(l2), run_time=0.6)

        cut = Line([ox, oy + h1, 0], [ox + a - b, oy + h1, 0],
                   color=DIM, stroke_width=2)
        self.play(Create(cut), run_time=0.6)

        self.play(p2.animate.rotate(-PI / 2).move_to([ox + a + b / 2, oy + h1 / 2, 0]),
                  run_time=1.8)
        l2.move_to([ox + a + b / 2, oy + h1 / 2, 0])
        self.play(Indicate(p2, color=BLUE, scale_factor=1.03), run_time=0.8)

        self.play(FadeOut(cut, l1, l2), run_time=0.5)

        bw = txt("a + b", size=27, color=GOLD).move_to([ox + (a + b) / 2, oy - 0.35, 0])
        hh = txt("a − b", size=27, color=BLUE).move_to([ox - 0.55, oy + h1 / 2, 0])
        self.play(FadeIn(bw, shift=UP * 0.05), run_time=0.7)
        self.play(FadeIn(hh, shift=RIGHT * 0.05), run_time=0.7)

        right = VGroup(
            txt("长：", size=27, color=DIM), txt("a + b", size=28, color=GOLD),
        ).arrange(RIGHT, buff=0.14).move_to([2.9, 1.0, 0])
        right2 = VGroup(
            txt("宽：", size=27, color=DIM), txt("a − b", size=28, color=BLUE),
        ).arrange(RIGHT, buff=0.14).move_to([2.9, 0.15, 0])
        self.play(FadeIn(right, shift=UP * 0.05), run_time=0.7)
        self.play(FadeIn(right2, shift=UP * 0.05), run_time=0.7)

        res = txt("(a + b)(a − b)", size=34, color=GOLD).move_to([2.9, -0.95, 0])
        self.play(FadeIn(res, shift=UP * 0.05), run_time=0.9)

        note = txt("拼之前和拼之后，纸的大小一样", size=25, color=DIM).move_to([2.9, -1.85, 0])
        self.play(FadeIn(note, shift=UP * 0.05), run_time=0.7)
        self.wait(2.2)
        self.finish_section()

    # ---------------- 2. 代数展开 ---------------- 20.5
    def scene_expand(self):
        self.section(2, "用乘法算一遍")

        head = txt("(a + b)(a − b)", size=34, color=CHALK).move_to([0, 2.25, 0])
        self.play(FadeIn(head, shift=UP * 0.05), run_time=0.9)

        r1 = VGroup(
            txt("=", size=30, color=DIM),
            pw("a", "2", 30, GOLD),
            txt("−", size=30, color=CHALK),
            txt("ab", size=30, color=RED),
            txt("+", size=30, color=CHALK),
            txt("ab", size=30, color=RED),
            txt("−", size=30, color=CHALK),
            pw("b", "2", 30, BLUE),
        ).arrange(RIGHT, buff=0.2).move_to([0, 1.15, 0])
        self.play(FadeIn(r1, shift=UP * 0.05), run_time=1.0)

        canc = Line([r1[3].get_left()[0] - 0.05, 1.04, 0],
                    [r1[5].get_right()[0] + 0.05, 1.04, 0],
                    color=RED, stroke_width=2.2)
        clab = txt("一减一加，抵消", size=24, color=RED).move_to([1.0, 0.62, 0])
        self.play(Create(canc), run_time=0.7)
        self.play(FadeIn(clab, shift=UP * 0.05), run_time=0.7)

        r2 = VGroup(
            txt("=", size=32, color=DIM),
            pw("a", "2", 34, GOLD),
            txt("−", size=32, color=CHALK),
            pw("b", "2", 34, BLUE),
        ).arrange(RIGHT, buff=0.2).move_to([0, -0.45, 0])
        self.play(FadeIn(r2, shift=UP * 0.05), run_time=1.0)

        steps = VGroup(
            txt("a · a = a²", size=25, color=GOLD),
            txt("a · (−b) = −ab", size=25, color=RED),
            txt("b · a = ab", size=25, color=RED),
            txt("b · (−b) = −b²", size=25, color=BLUE),
        ).arrange(DOWN, buff=0.26, aligned_edge=LEFT).move_to([-3.9, -1.6, 0])
        for s in steps:
            self.play(FadeIn(s, shift=RIGHT * 0.05), run_time=0.6)

        note = txt("中间两项互为相反数，相加得 0", size=25, color=DIM).move_to([2.2, -1.6, 0])
        self.play(FadeIn(note, shift=UP * 0.05), run_time=0.7)
        self.wait(2.0)
        self.finish_section()

    # ---------------- 3. 公式与结构 ---------------- 14.4
    def scene_formula(self):
        self.section(3, "平方差公式：看结构")

        box = label_box("(a + b)(a − b) = a² − b²", size=38, color=GOLD)
        box.move_to([0, 1.85, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.1)

        rows = VGroup(
            txt("两数的和 × 两数的差", size=28, color=CHALK),
            txt("= 相同项的平方 − 相反项的平方", size=28, color=GREEN),
        ).arrange(DOWN, buff=0.45).move_to([0, 0.35, 0])
        for r in rows:
            self.play(FadeIn(r, shift=UP * 0.05), run_time=0.9)

        same = txt("a 符号相同 → 平方", size=26, color=GOLD).move_to([-3.5, -1.0, 0])
        diff = txt("b 一正一负 → 平方", size=26, color=BLUE).move_to([3.5, -1.0, 0])
        self.play(FadeIn(same, shift=RIGHT * 0.05), run_time=0.8)
        self.play(FadeIn(diff, shift=LEFT * 0.05), run_time=0.8)

        note = txt("结果是两项，中间没有一次项", size=26, color=DIM).move_to([0, -2.05, 0])
        self.play(FadeIn(note, shift=UP * 0.05), run_time=0.8)
        self.wait(2.2)
        self.finish_section()

    # ---------------- 4. 两个例子 ---------------- 21.0
    def scene_examples(self):
        self.section(4, "两个例子")

        q1 = txt("(x + 3)(x − 3)", size=33, color=CHALK).move_to([0, 2.2, 0])
        self.play(FadeIn(q1, shift=UP * 0.05), run_time=0.8)

        s1 = VGroup(
            txt("相同的是 x，相反的是 3", size=27, color=CHALK),
        ).move_to([0, 1.35, 0])
        self.play(FadeIn(s1, shift=UP * 0.05), run_time=0.8)

        r1 = VGroup(
            txt("=", size=30, color=DIM),
            pw("x", "2", 32, GOLD),
            txt("−", size=30, color=DIM),
            txt("9", size=32, color=BLUE),
        ).arrange(RIGHT, buff=0.2).move_to([0, 0.55, 0])
        self.play(FadeIn(r1, shift=UP * 0.05), run_time=0.9)

        q2 = txt("(2a + b)(2a − b)", size=33, color=CHALK).move_to([0, -0.55, 0])
        self.play(FadeIn(q2, shift=UP * 0.05), run_time=0.8)

        s2 = txt("相同的是 2a，相反的是 b", size=27, color=CHALK).move_to([0, -1.35, 0])
        self.play(FadeIn(s2, shift=UP * 0.05), run_time=0.8)

        r2 = VGroup(
            txt("=", size=30, color=DIM),
            pw("4a", "2", 32, GOLD),
            txt("−", size=30, color=DIM),
            pw("b", "2", 32, BLUE),
        ).arrange(RIGHT, buff=0.2).move_to([0, -2.15, 0])
        self.play(FadeIn(r2, shift=UP * 0.05), run_time=0.9)

        warn = txt("系数 2 也要平方，2² = 4", size=25, color=RED).move_to([3.9, -2.15, 0])
        self.play(FadeIn(warn, shift=LEFT * 0.05), run_time=0.7)
        self.wait(2.6)
        self.finish_section()

    # ---------------- 5. 顺序乱了先调整 ---------------- 21.8
    def scene_reorder(self):
        self.section(5, "顺序乱了怎么办")

        q = txt("(y − 2x)(y + 2x)", size=34, color=CHALK).move_to([0, 2.2, 0])
        self.play(FadeIn(q, shift=UP * 0.05), run_time=0.9)

        step = VGroup(
            txt("先交换位置", size=26, color=GOLD),
            txt("→", size=28, color=DIM),
            txt("(y + 2x)(y − 2x)", size=30, color=CHALK),
        ).arrange(RIGHT, buff=0.3).move_to([0, 1.25, 0])
        self.play(FadeIn(step, shift=UP * 0.05), run_time=1.0)

        rule = txt("把两项调成「和 × 差」的样子，再套公式", size=26, color=DIM)
        rule.move_to([0, 0.45, 0])
        self.play(FadeIn(rule, shift=UP * 0.05), run_time=0.8)

        s1 = VGroup(
            txt("相同的是", size=27, color=CHALK),
            txt("y", size=30, color=GOLD),
            txt("，相反的是", size=27, color=CHALK),
            txt("2x", size=30, color=BLUE),
        ).arrange(RIGHT, buff=0.12).move_to([0, -0.45, 0])
        self.play(FadeIn(s1, shift=UP * 0.05), run_time=0.9)

        res = VGroup(
            txt("=", size=30, color=DIM),
            pw("y", "2", 34, GOLD),
            txt("−", size=30, color=DIM),
            pw("4x", "2", 34, BLUE),
        ).arrange(RIGHT, buff=0.2).move_to([0, -1.4, 0])
        self.play(FadeIn(res, shift=UP * 0.05), run_time=1.0)

        note = txt("2x 整体平方：(2x)² = 4x²，不能只平方 x", size=25, color=RED)
        note.move_to([0, -2.25, 0])
        self.play(FadeIn(note, shift=UP * 0.05), run_time=0.8)
        self.wait(2.8)
        self.finish_section()

    # ---------------- 6. 例题与三个易错点 ---------------- 31.4
    def scene_ex(self):
        self.section(6, "例题与三个易错点")

        q = txt("(−2x + y)(2x + y)", size=33, color=CHALK).move_to([0, 2.3, 0])
        self.play(FadeIn(q, shift=UP * 0.05), run_time=0.9)

        s1 = VGroup(
            txt("第一项改写成", size=26, color=CHALK),
            txt("y − 2x", size=30, color=GOLD),
        ).arrange(RIGHT, buff=0.2).move_to([0, 1.45, 0])
        self.play(FadeIn(s1, shift=UP * 0.05), run_time=0.9)

        s2 = txt("= (y + 2x)(y − 2x)", size=31, color=CHALK).move_to([0, 0.65, 0])
        self.play(FadeIn(s2, shift=UP * 0.05), run_time=0.9)

        s3 = VGroup(
            txt("相同的是 y，相反的是 2x", size=27, color=CHALK),
        ).move_to([0, -0.1, 0])
        self.play(FadeIn(s3, shift=UP * 0.05), run_time=0.8)

        res = VGroup(
            txt("=", size=30, color=DIM),
            pw("y", "2", 34, GOLD),
            txt("−", size=30, color=DIM),
            pw("4x", "2", 34, BLUE),
        ).arrange(RIGHT, buff=0.2).move_to([0, -0.95, 0])
        self.play(FadeIn(res, shift=UP * 0.05), run_time=1.0)

        items = [
            ("和完全平方公式搞混", "平方差只有两项"),
            ("把 (a+b)(a+b) 当平方差", "要一加一减才算"),
            ("系数忘了平方", "(2a)² = 4a²"),
        ]
        y = -1.75
        for bad_s, good_s in items:
            bad = txt(bad_s, size=24, color=RED).move_to([-2.7, y, 0])
            good = txt(good_s, size=23, color=GREEN).move_to([3.5, y, 0])
            cross = Line([bad.get_left()[0] - 0.07, y - 0.07, 0],
                         [bad.get_right()[0] + 0.07, y - 0.07, 0],
                         color=RED, stroke_width=2.2)
            self.play(FadeIn(bad, shift=RIGHT * 0.05), run_time=0.5)
            self.play(Create(cross), run_time=0.35)
            self.play(FadeIn(good, shift=RIGHT * 0.05), run_time=0.5)
            y -= 0.62

        self.wait(3.0)
        self.finish_section()

    def construct(self):
        self.scene_cut()
        self.clear_stage()
        self.scene_puzzle()
        self.clear_stage()
        self.scene_expand()
        self.clear_stage()
        self.scene_formula()
        self.clear_stage()
        self.scene_examples()
        self.clear_stage()
        self.scene_reorder()
        self.clear_stage()
        self.scene_ex()
        self.clear_stage(0.8)