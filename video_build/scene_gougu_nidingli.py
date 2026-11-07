# -*- coding: utf-8 -*-
"""勾股定理的逆定理：用边长判断直角。八年级。"""

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


def P(x, y):
    return np.array([float(x), float(y), 0.0])


def tri(a, b, c, color=CHALK, fill=0.0, width=3.0):
    t = Polygon(P(*a), P(*b), P(*c), color=color, stroke_width=width)
    if fill:
        t.set_fill(color, opacity=fill)
    return t


def right_angle(v, p1, p2, size=0.34, color=CHALK):
    a1 = math.atan2(p1[1] - v[1], p1[0] - v[0])
    a2 = math.atan2(p2[1] - v[1], p2[0] - v[0])
    u1 = np.array([math.cos(a1), math.sin(a1), 0]) * size
    u2 = np.array([math.cos(a2), math.sin(a2), 0]) * size
    o = P(*v)
    return Polygon(o + u1, o + u1 + u2, o + u2,
                   color=color, stroke_width=2.4, fill_color=color, fill_opacity=0.12)


def cross_out(mob, color=RED, pad=0.10):
    l = mob.get_left()[0] - pad
    r = mob.get_right()[0] + pad
    b = mob.get_bottom()[1] - pad
    t = mob.get_top()[1] + pad
    return VGroup(
        Line([l, b, 0], [r, t, 0], color=color, stroke_width=2.4),
        Line([l, t, 0], [r, b, 0], color=color, stroke_width=2.4),
    )


class GouguNidingliScene(NarratedScene):
    lesson = "gougu_nidingli"

    def clear_stage(self, run_time: float = 0.5):
        keep = {id(self._track), id(self._fill)}
        junk = [m for m in self.mobjects if id(m) not in keep]
        if junk:
            self.play(*[FadeOut(m) for m in junk], run_time=run_time)
        self.cur_title = None
        self.cur_sub = None

    # ---------------- 0. 装修画直角 ---------------- 25.5
    def scene_intro(self):
        self.section(0, "不用量角器，也能画直角")

        O, A, B = (-5.0, -1.3), (-1.0, -1.3), (-5.0, 0.95)
        base = Line(P(*O), P(*A), color=CHALK, stroke_width=3)
        up = Line(P(*O), P(*B), color=CHALK, stroke_width=3)
        self.play(Create(base), Create(up), run_time=1.2)
        self.play(Create(right_angle(O, A, B, size=0.4, color=GOLD)), run_time=0.7)

        l80 = txt("80", size=26, color=DIM).move_to([-3.0, -1.72, 0])
        l60 = txt("60", size=26, color=DIM).move_to([-5.45, -0.18, 0])
        self.play(FadeIn(l80), FadeIn(l60), run_time=0.8)
        self.wait(1.2)

        hyp = Line(P(*A), P(*B), color=GOLD, stroke_width=5)
        self.play(Create(hyp), run_time=1.0)
        l100 = txt("100", size=28, color=GOLD).move_to([-2.25, -0.05, 0])
        self.play(FadeIn(l100, shift=LEFT * 0.05), run_time=0.8)
        self.wait(2.0)

        c1 = txt("量出 60、80，再让两端相距 100", size=26, color=CHALK)
        c1.move_to([3.1, 1.0, 0])
        self.play(FadeIn(c1, shift=UP * 0.05), run_time=0.9)

        c2 = txt("这个角，正好是直角", size=27, color=GREEN)
        c2.move_to([3.1, 0.1, 0])
        self.play(FadeIn(c2, shift=UP * 0.05), run_time=0.9)
        self.wait(2.2)

        c3 = txt("三条边一定，角也就定了", size=25, color=DIM)
        c3.move_to([3.1, -0.9, 0])
        self.play(FadeIn(c3, shift=UP * 0.05), run_time=0.9)
        self.wait(1.0)

        c4 = txt("反过来：边的关系 → 角的大小", size=26, color=GOLD)
        c4.move_to([0, -2.55, 0])
        self.play(FadeIn(c4, shift=UP * 0.05), run_time=1.0)
        self.wait(2.6)
        self.finish_section()

    # ---------------- 1. 定理 ---------------- 19.4
    def scene_theorem(self):
        self.section(1, "逆定理：边的关系决定角")

        box = label_box("a² + b² = c²　→　直角三角形", size=32, color=GOLD)
        box.move_to([0, 2.15, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.2)
        self.wait(1.2)

        A, B, C = (-5.0, -2.3), (-1.6, -2.3), (-1.6, 0.6)
        t = tri(A, B, C, CHALK, 0.09)
        self.play(Create(t), run_time=1.2)

        ra = right_angle(B, A, C, size=0.34, color=DIM)
        self.play(Create(ra), run_time=0.6)

        lab_b = txt("b", size=27, color=BLUE).move_to([-3.3, -2.62, 0])
        lab_a = txt("a", size=27, color=BLUE).move_to([-1.22, -0.85, 0])
        lab_c = txt("c", size=30, color=GOLD).move_to([-3.9, -0.5, 0])
        self.play(FadeIn(lab_b), FadeIn(lab_a), FadeIn(lab_c), run_time=0.9)
        self.wait(1.2)

        n1 = txt("c 是三条边里最长的那条", size=26, color=CHALK)
        n1.move_to([3.2, -0.35, 0])
        self.play(FadeIn(n1, shift=UP * 0.05), run_time=0.9)

        n2 = txt("c 所对的角，就是直角", size=28, color=GOLD)
        n2.move_to([3.2, -1.4, 0])
        self.play(FadeIn(n2, shift=UP * 0.05), run_time=0.9)
        self.wait(1.0)

        n3 = txt("边长满足关系，形状就唯一确定", size=24, color=DIM)
        n3.move_to([3.2, -2.35, 0])
        self.play(FadeIn(n3, shift=UP * 0.05), run_time=0.9)
        self.wait(2.4)
        self.finish_section()

    # ---------------- 2. 原定理 vs 逆定理 ---------------- 27.3
    def scene_compare(self):
        self.section(2, "原定理和逆定理，正好反过来")

        lh = txt("勾股定理", size=30, color=CHALK).move_to([-3.4, 2.15, 0])
        rh = txt("逆定理", size=30, color=GOLD).move_to([3.4, 2.15, 0])
        self.play(FadeIn(lh, shift=UP * 0.05), run_time=0.8)
        self.play(FadeIn(rh, shift=UP * 0.05), run_time=0.8)

        sep = Line([0, 2.5, 0], [0, -0.7, 0], color=DIM, stroke_width=1.5)
        sep.set_opacity(0.4)
        self.play(Create(sep), run_time=0.6)

        l1 = txt("已知：是直角三角形", size=25, color=CHALK).move_to([-3.4, 1.25, 0])
        l2 = txt("得到：a² + b² = c²", size=26, color=GOLD).move_to([-3.4, 0.35, 0])
        l3 = txt("用途：算边长", size=25, color=BLUE).move_to([-3.4, -0.45, 0])
        self.play(FadeIn(l1, shift=UP * 0.04), run_time=0.8)
        self.play(FadeIn(l2, shift=UP * 0.04), run_time=0.8)
        self.play(FadeIn(l3, shift=UP * 0.04), run_time=0.8)
        self.wait(1.4)

        r1 = txt("已知：a² + b² = c²", size=25, color=GOLD).move_to([3.4, 1.25, 0])
        r2 = txt("得到：是直角三角形", size=26, color=CHALK).move_to([3.4, 0.35, 0])
        r3 = txt("用途：判断形状", size=25, color=GREEN).move_to([3.4, -0.45, 0])
        self.play(FadeIn(r1, shift=UP * 0.04), run_time=0.8)
        self.play(FadeIn(r2, shift=UP * 0.04), run_time=0.8)
        self.play(FadeIn(r3, shift=UP * 0.04), run_time=0.8)
        self.wait(1.6)

        arrow = Arrow([-1.2, 2.15, 0], [1.2, 2.15, 0], color=DIM, stroke_width=2.4,
                      max_tip_length_to_length_ratio=0.18)
        self.play(Create(arrow), run_time=0.8)

        bottom = label_box("先看题目问什么，再决定用哪一个", size=27, color=CHALK)
        bottom.move_to([0, -1.75, 0])
        self.play(FadeIn(bottom, scale=0.97), run_time=1.1)
        self.wait(2.8)
        self.finish_section()

    # ---------------- 3. 三步判断 ---------------- 25.0
    def scene_steps(self):
        self.section(3, "判断只有三步")

        items = [
            ("①", "找出最长边，记作 c", GOLD),
            ("②", "算出另外两边的平方和", CHALK),
            ("③", "和最长的平方比一比", CHALK),
        ]
        y = 2.2
        for num, text_s, col in items:
            n = txt(num, size=28, color=GOLD).move_to([-5.2, y, 0])
            t = txt(text_s, size=27, color=col).move_to([-1.6, y, 0])
            self.play(FadeIn(n, shift=RIGHT * 0.05), run_time=0.6)
            self.play(FadeIn(t, shift=RIGHT * 0.05), run_time=0.7)
            y -= 0.95
        self.wait(1.2)

        ex1 = txt("例：三边 6、8、10", size=27, color=CHALK)
        ex1.move_to([0, -0.85, 0])
        self.play(FadeIn(ex1, shift=UP * 0.05), run_time=0.8)

        ex2 = txt("6² + 8² = 36 + 64 = 100", size=27, color=BLUE)
        ex2.move_to([0, -1.65, 0])
        self.play(FadeIn(ex2, shift=UP * 0.05), run_time=0.9)

        ex3 = txt("10² = 100　→　相等，是直角三角形", size=27, color=GREEN)
        ex3.move_to([0, -2.4, 0])
        self.play(FadeIn(ex3, shift=UP * 0.05), run_time=0.9)
        self.wait(1.6)

        warn = txt("比的是平方，不是边长：6 + 8 ≠ 10", size=24, color=RED)
        warn.move_to([0, -3.15, 0])
        self.play(FadeIn(warn, shift=UP * 0.05), run_time=0.9)
        self.wait(2.2)
        self.finish_section()

    # ---------------- 4. 勾股数 ---------------- 24.6
    def scene_triples(self):
        self.section(4, "这几组数，最好记住")

        data = [
            ("3、4、5", "9 + 16 = 25", (-3.5, 1.75)),
            ("5、12、13", "25 + 144 = 169", (1.6, 1.75)),
            ("8、15、17", "64 + 225 = 289", (-3.5, 0.35)),
            ("7、24、25", "49 + 576 = 625", (1.6, 0.35)),
        ]
        for head, sub, pos in data:
            h = txt(head, size=32, color=GOLD).move_to([pos[0], pos[1] + 0.16, 0])
            s = txt(sub, size=22, color=DIM).move_to([pos[0], pos[1] - 0.42, 0])
            self.play(FadeIn(h, shift=UP * 0.04), run_time=0.6)
            self.play(FadeIn(s, shift=UP * 0.04), run_time=0.55)
            self.wait(0.5)
        self.wait(1.0)

        multi = txt("整数倍也成立：6、8、10　9、12、15", size=26, color=CHALK)
        multi.move_to([0, -0.95, 0])
        self.play(FadeIn(multi, shift=UP * 0.05), run_time=0.9)

        tip = label_box("看到这几组数，先想到直角", size=26, color=GREEN)
        tip.move_to([0, -2.0, 0])
        self.play(FadeIn(tip, scale=0.97), run_time=1.1)
        self.wait(3.0)
        self.finish_section()

    # ---------------- 5. 例题 ---------------- 23.4
    def scene_example(self):
        self.section(5, "例题：三边 5、12、13")

        A, B, C = (5.5, -2.5), (2.4, -2.5), (2.4, -1.2)
        t = tri(A, B, C, CHALK, 0.09)
        self.play(Create(t), run_time=1.2)

        l12 = txt("12", size=26, color=BLUE).move_to([3.95, -2.82, 0])
        l5 = txt("5", size=26, color=BLUE).move_to([2.05, -1.85, 0])
        l13 = txt("13", size=28, color=GOLD).move_to([4.12, -1.62, 0])
        self.play(FadeIn(l12), FadeIn(l5), FadeIn(l13), run_time=0.9)
        self.wait(1.0)

        s1 = txt("最长边是 13，所以 c = 13", size=25, color=CHALK)
        s1.move_to([-2.9, 1.55, 0])
        self.play(FadeIn(s1, shift=UP * 0.04), run_time=0.8)

        s2 = txt("5² + 12² = 25 + 144 = 169", size=25, color=BLUE)
        s2.move_to([-2.9, 0.65, 0])
        self.play(FadeIn(s2, shift=UP * 0.04), run_time=0.85)

        s3 = txt("13² = 169", size=25, color=CHALK)
        s3.move_to([-2.9, -0.2, 0])
        self.play(FadeIn(s3, shift=UP * 0.04), run_time=0.75)

        s4 = txt("169 = 169，是直角三角形", size=26, color=GREEN)
        s4.move_to([-2.9, -1.1, 0])
        self.play(FadeIn(s4, shift=UP * 0.04), run_time=0.85)

        ra = right_angle(B, A, C, size=0.34, color=GREEN)
        self.play(Create(ra), run_time=0.6)

        s5 = txt("∠B = 90°，它就是 13 所对的角", size=26, color=GOLD)
        s5.move_to([0.6, -3.05, 0])
        self.play(FadeIn(s5, shift=UP * 0.04), run_time=0.9)
        self.wait(2.6)
        self.finish_section()

    # ---------------- 6. 易错点 ---------------- 24.4
    def scene_pitfalls(self):
        self.section(6, "三个易错点")

        items = [
            ("没找最长边就套公式", "先确定 c"),
            ("拿边长相加减去比", "比的是平方"),
            ("顺手写出另外两个角", "只能判定直角"),
        ]
        y = 1.95
        for bad_s, good_s in items:
            bad = txt(bad_s, size=26, color=RED).move_to([-2.6, y, 0])
            good = txt(good_s, size=26, color=GREEN).move_to([2.6, y, 0])
            self.play(FadeIn(bad, shift=RIGHT * 0.05), run_time=0.6)
            self.play(Create(cross_out(bad)), run_time=0.4)
            self.play(FadeIn(good, shift=RIGHT * 0.05), run_time=0.6)
            y -= 1.0
            self.wait(0.4)

        line = label_box("边满足关系，角才是直角", size=29, color=GOLD)
        line.move_to([0, -1.55, 0])
        self.play(FadeIn(line, scale=0.97), run_time=1.1)
        self.wait(3.2)
        self.finish_section()

    def construct(self):
        self.scene_intro()
        self.clear_stage()
        self.scene_theorem()
        self.clear_stage()
        self.scene_compare()
        self.clear_stage()
        self.scene_steps()
        self.clear_stage()
        self.scene_triples()
        self.clear_stage()
        self.scene_example()
        self.clear_stage()
        self.scene_pitfalls()
        self.clear_stage(0.8)