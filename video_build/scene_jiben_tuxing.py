# -*- coding: utf-8 -*-
"""基本图形：线段、射线、直线、角的度量与角平分线。七年级上。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


def place(g, x, y):
    """左边缘对齐 x，竖直中心落在 y。"""
    g.move_to([0, 0, 0])
    g.shift(RIGHT * (x - g.get_left()[0]) + UP * (y - g.get_center()[1]))
    return g


def card(name: str, value: str, color: str, width: float = 1.95, height: float = 1.15) -> VGroup:
    body = VGroup(
        txt(name, size=27, color=color),
        txt(value, size=24, color=CHALK),
    ).arrange(DOWN, buff=0.16)
    box = RoundedRectangle(corner_radius=0.12, width=width, height=height,
                           stroke_color=color, stroke_width=1.6,
                           fill_color=color, fill_opacity=0.1)
    return VGroup(box, body)


class JibenTuxingScene(NarratedScene):
    lesson = "jiben-tuxing"

    def clear_stage(self, run_time: float = 0.5):
        keep = {id(self._track), id(self._fill)}
        junk = [m for m in self.mobjects if id(m) not in keep]
        if junk:
            self.play(*[FadeOut(m) for m in junk], run_time=run_time)
        self.cur_title = None
        self.cur_sub = None

    # ---------------- 0. 三样基本图形 ---------------- 17.8
    def scene_story(self):
        self.section(0, "线段、射线、直线")

        seg = Line([-6.2, 1.9, 0], [-2.9, 1.9, 0], color=CHALK, stroke_width=3)
        d1 = Dot([-6.2, 1.9, 0], radius=0.1, color=GOLD)
        d2 = Dot([-2.9, 1.9, 0], radius=0.1, color=GOLD)
        self.play(Create(seg), run_time=0.8)
        self.play(FadeIn(d1, scale=0.7), FadeIn(d2, scale=0.7), run_time=0.5)
        t1 = place(txt("线段：两个端点，长度固定", size=26, color=CHALK), -2.5, 1.9)
        self.play(FadeIn(t1, shift=RIGHT * 0.05), run_time=0.75)

        ray = Arrow([-6.2, 0.55, 0], [-2.9, 0.55, 0], color=CHALK, buff=0,
                    stroke_width=3, max_tip_length_to_length_ratio=0.07)
        dr = Dot([-6.2, 0.55, 0], radius=0.1, color=GOLD)
        self.play(Create(ray), run_time=0.8)
        self.play(FadeIn(dr, scale=0.7), run_time=0.45)
        t2 = place(txt("射线：一个端点，向一方无限延伸", size=26, color=BLUE), -2.5, 0.55)
        self.play(FadeIn(t2, shift=RIGHT * 0.05), run_time=0.75)

        line = DoubleArrow([-6.2, -0.8, 0], [-2.9, -0.8, 0], color=CHALK, buff=0,
                           stroke_width=3, max_tip_length_to_length_ratio=0.07)
        self.play(Create(line), run_time=0.8)
        t3 = place(txt("直线：没有端点，向两方无限延伸", size=26, color=GREEN), -2.5, -0.8)
        self.play(FadeIn(t3, shift=RIGHT * 0.05), run_time=0.8)

        note = txt("先数端点，再看能不能延伸", size=29, color=GOLD).move_to([0, -2.15, 0])
        self.play(FadeIn(note, shift=UP * 0.05), run_time=0.8)
        self.wait(3.2)
        self.finish_section()

    # ---------------- 1. 对比表 ---------------- 15.0
    def scene_table(self):
        self.section(1, "三样图形的区别")

        heads = ["名称", "端点个数", "能否延伸", "记法"]
        xs = [-6.2, -4.5, -2.0, 2.5]
        for h, x in zip(heads, xs):
            self.play(FadeIn(txt(h, size=27, color=GOLD).move_to([0, 0, 0]).shift(
                RIGHT * (x + 0.5) + UP * 2.2), shift=UP * 0.05), run_time=0.45)

        rows = [
            ("线段", "2 个", "不能延伸", "线段 AB", CHALK),
            ("射线", "1 个", "向一方延伸", "射线 OA", BLUE),
            ("直线", "0 个", "向两方延伸", "直线 AB", GREEN),
        ]
        y = 1.45
        for name, ends, extend, how, color in rows:
            self.play(FadeIn(txt(name, size=29, color=color).move_to(
                [0, 0, 0]).shift(RIGHT * (-5.7) + UP * y), shift=RIGHT * 0.05), run_time=0.45)
            self.play(FadeIn(txt(ends, size=27, color=CHALK).move_to(
                [0, 0, 0]).shift(RIGHT * (-3.6) + UP * y), shift=RIGHT * 0.05), run_time=0.45)
            self.play(FadeIn(txt(extend, size=27, color=CHALK).move_to(
                [0, 0, 0]).shift(RIGHT * (-0.9) + UP * y), shift=RIGHT * 0.05), run_time=0.45)
            self.play(FadeIn(txt(how, size=27, color=DIM).move_to(
                [0, 0, 0]).shift(RIGHT * 3.4 + UP * y), shift=RIGHT * 0.05), run_time=0.45)
            y -= 1.0

        tip = txt("射线记法里，端点写在前面", size=27, color=GOLD).move_to([0, -2.15, 0])
        self.play(FadeIn(tip, shift=UP * 0.05), run_time=0.8)
        self.wait(2.2)
        self.finish_section()

    # ---------------- 2. 比较线段与中点 ---------------- 14.1
    def scene_seg(self):
        self.section(2, "比长短，找中点")

        s1 = Line([-6.3, 1.75, 0], [-1.3, 1.75, 0], color=GOLD, stroke_width=4)
        s2 = Line([-6.3, 1.1, 0], [-2.8, 1.1, 0], color=BLUE, stroke_width=4)
        self.play(Create(s1), run_time=0.7)
        self.play(Create(s2), run_time=0.7)
        tip1 = txt("左端对齐，看谁更长", size=26, color=CHALK).move_to([3.3, 1.45, 0])
        self.play(FadeIn(tip1, shift=RIGHT * 0.05), run_time=0.7)

        ab = Line([-5.8, -0.55, 0], [1.0, -0.55, 0], color=CHALK, stroke_width=3.5)
        da = Dot([-5.8, -0.55, 0], radius=0.1, color=GOLD)
        dc = Dot([-2.4, -0.55, 0], radius=0.11, color=GREEN)
        db = Dot([1.0, -0.55, 0], radius=0.1, color=GOLD)
        self.play(Create(ab), run_time=0.8)
        self.play(FadeIn(da, scale=0.7), FadeIn(dc, scale=0.7), FadeIn(db, scale=0.7), run_time=0.6)

        la = txt("A", size=27, color=GOLD).next_to(da, DOWN, buff=0.22)
        lc = txt("C", size=27, color=GREEN).next_to(dc, DOWN, buff=0.22)
        lb = txt("B", size=27, color=GOLD).next_to(db, DOWN, buff=0.22)
        self.play(FadeIn(la), FadeIn(lc), FadeIn(lb), run_time=0.6)

        ac = txt("AC = CB", size=27, color=GREEN).move_to([-2.4, 0.1, 0])
        mid = txt("C 是中点", size=27, color=GOLD).move_to([3.3, -0.55, 0])
        self.play(FadeIn(ac, shift=UP * 0.05), run_time=0.7)
        self.play(FadeIn(mid, shift=RIGHT * 0.05), run_time=0.7)

        note = txt("两点之间，线段最短", size=28, color=GOLD).move_to([0, -2.1, 0])
        self.play(FadeIn(note, shift=UP * 0.05), run_time=0.8)
        self.wait(2.0)
        self.finish_section()

    # ---------------- 3. 角与度分秒 ---------------- 15.2
    def scene_angle(self):
        self.section(3, "角：顶点与两条边")

        apex = [-4.7, -0.25, 0]
        oa = Line(apex, [-0.7, 1.75, 0], color=GOLD, stroke_width=3)
        ob = Line(apex, [-0.7, -1.9, 0], color=BLUE, stroke_width=3)
        self.play(Create(oa), run_time=0.8)
        self.play(Create(ob), run_time=0.8)

        arc = Angle(oa, ob, radius=0.85, color=GREEN, stroke_width=3)
        self.play(Create(arc), run_time=0.8)

        dot = Dot(apex, radius=0.09, color=CHALK)
        self.play(FadeIn(dot, scale=0.7), run_time=0.4)
        lo = txt("顶点 O", size=26, color=CHALK).move_to([-4.9, -1.0, 0])
        la = txt("边 OA", size=26, color=GOLD).move_to([-2.9, 1.15, 0])
        lb = txt("边 OB", size=26, color=BLUE).move_to([-2.9, -1.35, 0])
        self.play(FadeIn(lo), FadeIn(la), FadeIn(lb), run_time=0.7)

        head = label_box("两条有公共端点的射线", size=26, color=GOLD).move_to([3.5, 2.0, 0])
        self.play(FadeIn(head, scale=0.97), run_time=0.75)

        rows = VGroup(
            txt("公共端点叫顶点", size=26, color=CHALK),
            txt("两条射线叫边", size=26, color=CHALK),
        ).arrange(DOWN, buff=0.28, aligned_edge=LEFT).move_to([3.5, 0.95, 0])
        for r in rows:
            self.play(FadeIn(r, shift=RIGHT * 0.05), run_time=0.6)

        unit = label_box("1° = 60′，1′ = 60″", size=28, color=GOLD).move_to([3.5, -0.3, 0])
        self.play(FadeIn(unit, scale=0.97), run_time=0.75)

        ex = txt("30.5° = 30°30′", size=26, color=BLUE).move_to([3.5, -1.25, 0])
        self.play(FadeIn(ex, shift=UP * 0.05), run_time=0.65)

        note = txt("度分秒是六十进制，不是十进制", size=26, color=RED).move_to([0, -2.4, 0])
        self.play(FadeIn(note, shift=UP * 0.05), run_time=0.75)
        self.wait(1.8)
        self.finish_section()

    # ---------------- 4. 角的分类 ---------------- 13.1
    def scene_kind(self):
        self.section(4, "锐角、直角、钝角、平角、周角")

        items = [
            ("锐角", "< 90°", GOLD),
            ("直角", "= 90°", BLUE),
            ("钝角", "90°~180°", ORANGE),
            ("平角", "= 180°", GREEN),
            ("周角", "= 360°", PURPLE),
        ]
        cards = VGroup(*[card(n, v, c) for n, v, c in items]).arrange(RIGHT, buff=0.28)
        cards.move_to([0, 1.35, 0])
        for c in cards:
            self.play(FadeIn(c, shift=UP * 0.05), run_time=0.5)

        r1 = txt("0° < 锐角 < 90° < 钝角 < 180°", size=28, color=CHALK).move_to([0, -0.1, 0])
        self.play(FadeIn(r1, shift=UP * 0.05), run_time=0.75)

        r2 = txt("平角的两边成一条直线", size=27, color=GREEN).move_to([0, -0.95, 0])
        r3 = txt("周角的两边重合在一起", size=27, color=PURPLE).move_to([0, -1.65, 0])
        self.play(FadeIn(r2, shift=UP * 0.05), run_time=0.65)
        self.play(FadeIn(r3, shift=UP * 0.05), run_time=0.65)

        note = txt("看角的大小，就是看张开多大", size=26, color=DIM).move_to([0, -2.35, 0])
        self.play(FadeIn(note, shift=UP * 0.05), run_time=0.7)
        self.wait(1.6)
        self.finish_section()

    # ---------------- 5. 角平分线 ---------------- 15.3
    def scene_bisect(self):
        self.section(5, "角平分线：分成相等的两半")

        apex = [-4.4, -0.2, 0]
        oa = Line(apex, [-1.0, 1.95, 0], color=GOLD, stroke_width=3)
        ob = Line(apex, [-1.0, -1.95, 0], color=BLUE, stroke_width=3)
        oc = Line(apex, [0.6, -0.2, 0], color=GREEN, stroke_width=3)
        self.play(Create(oa), Create(ob), run_time=0.9)
        self.play(Create(oc), run_time=0.8)

        a1 = Angle(oc, oa, radius=0.75, color=GOLD, stroke_width=2.6)
        a2 = Angle(ob, oc, radius=0.75, color=GREEN, stroke_width=2.6)
        self.play(Create(a1), run_time=0.6)
        self.play(Create(a2), run_time=0.6)

        laa = txt("A", size=26, color=GOLD).move_to([-1.15, 1.75, 0])
        lac = txt("C", size=26, color=GREEN).move_to([0.45, -0.55, 0])
        lab = txt("B", size=26, color=BLUE).move_to([-1.15, -1.75, 0])
        lo = txt("O", size=26, color=CHALK).move_to([-4.75, -0.6, 0])
        self.play(FadeIn(laa), FadeIn(lac), FadeIn(lab), FadeIn(lo), run_time=0.7)

        head = label_box("从顶点出发，把角分成两半", size=26, color=GOLD).move_to([3.5, 1.9, 0])
        self.play(FadeIn(head, scale=0.97), run_time=0.8)

        f = txt("∠AOC = ∠BOC = ½∠AOB", size=28, color=GREEN).move_to([3.5, 0.8, 0])
        self.play(FadeIn(f, shift=UP * 0.05), run_time=0.8)

        n1 = txt("见到平分线，先想一半", size=27, color=CHALK).move_to([3.5, -0.3, 0])
        n2 = txt("反过来，一半乘 2 就是整个角", size=26, color=DIM).move_to([3.5, -1.05, 0])
        self.play(FadeIn(n1, shift=UP * 0.05), run_time=0.7)
        self.play(FadeIn(n2, shift=UP * 0.05), run_time=0.7)

        tail = txt("角平分线必须从顶点出发", size=26, color=RED).move_to([0, -2.45, 0])
        self.play(FadeIn(tail, shift=UP * 0.05), run_time=0.7)
        self.wait(1.6)
        self.finish_section()

    # ---------------- 6. 例题 + 易错点 ---------------- 20.9
    def scene_ex(self):
        self.section(6, "两道小题与三个易错点")

        left = txt("AB = 8，C 是中点", size=29, color=GOLD).move_to([-3.6, 2.3, 0])
        self.play(FadeIn(left, shift=UP * 0.05), run_time=0.7)

        ab = Line([-6.1, 1.55, 0], [-1.1, 1.55, 0], color=CHALK, stroke_width=3.4)
        da = Dot([-6.1, 1.55, 0], radius=0.1, color=GOLD)
        dc = Dot([-3.6, 1.55, 0], radius=0.11, color=GREEN)
        db = Dot([-1.1, 1.55, 0], radius=0.1, color=GOLD)
        self.play(Create(ab), run_time=0.7)
        self.play(FadeIn(da, scale=0.7), FadeIn(dc, scale=0.7), FadeIn(db, scale=0.7), run_time=0.5)
        for d, s, c in ((da, "A", GOLD), (dc, "C", GREEN), (db, "B", GOLD)):
            self.add(txt(s, size=24, color=c).next_to(d, DOWN, buff=0.2))
        self.play(FadeIn(txt("AC = 8 ÷ 2 = 4（厘米）", size=28, color=GREEN).move_to([-3.6, 0.5, 0]),
                        shift=UP * 0.05), run_time=0.8)

        right = txt("∠AOB = 70°，OC 平分", size=29, color=GOLD).move_to([3.6, 2.3, 0])
        self.play(FadeIn(right, shift=UP * 0.05), run_time=0.7)
        r2 = txt("∠AOC = 70° ÷ 2 = 35°", size=28, color=GREEN).move_to([3.6, 0.5, 0])
        self.play(FadeIn(r2, shift=UP * 0.05), run_time=0.8)

        note = txt("几何题先画图，再把条件标到图上", size=27, color=CHALK).move_to([0, -0.35, 0])
        self.play(FadeIn(note, shift=UP * 0.05), run_time=0.75)

        items = [
            ("把射线当成直线", "端点个数不同"),
            ("度分秒按十进制算", "1° = 60′"),
            ("角平分线当成两倍", "是分成一半"),
        ]
        y = -1.15
        for bad_s, good_s in items:
            bad = txt(bad_s, size=25, color=RED).move_to([-3.3, y, 0])
            good = txt(good_s, size=24, color=GREEN).move_to([3.4, y, 0])
            cross = Line(bad.get_left() + [-0.1, -0.07, 0],
                         bad.get_right() + [0.1, 0.16, 0],
                         color=RED, stroke_width=2.6)
            self.play(FadeIn(bad, shift=RIGHT * 0.05), run_time=0.5)
            self.play(Create(cross), FadeIn(good, shift=RIGHT * 0.05), run_time=0.6)
            y -= 0.66

        self.wait(1.2)
        self.finish_section()

    def construct(self):
        self.scene_story()
        self.clear_stage()
        self.scene_table()
        self.clear_stage()
        self.scene_seg()
        self.clear_stage()
        self.scene_angle()
        self.clear_stage()
        self.scene_kind()
        self.clear_stage()
        self.scene_bisect()
        self.clear_stage()
        self.scene_ex()
        self.clear_stage(0.8)