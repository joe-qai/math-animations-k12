# -*- coding: utf-8 -*-
"""梯形的面积：两个梯形拼成平行四边形、上底加下底乘高除以二、例题与易错点。五年级上册。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403

# 梯形四个顶点（屏幕坐标）：下底 4.0，上底 2.4，高 2.4
A = [-4.8, -1.3, 0]
B = [-0.8, -1.3, 0]
C = [-1.6, 1.1, 0]
D = [-4.0, 1.1, 0]
M = [-1.2, -0.1, 0]          # 右腰中点，旋转中心


def trapezoid(color: str = CHALK, fill: float = 0.0) -> Polygon:
    return Polygon(A, B, C, D, color=color, stroke_width=3,
                   fill_color=color, fill_opacity=fill)


class TixingMianjiScene(NarratedScene):
    lesson = "tixing-mianji"

    def clear_stage(self, run_time: float = 0.5):
        keep = {id(self._track), id(self._fill)}
        junk = [m for m in self.mobjects if id(m) not in keep]
        if junk:
            self.play(*[FadeOut(m) for m in junk], run_time=run_time)
        self.cur_title = None
        self.cur_sub = None

    # ---------------- 0. 梯形花坛 ---------------- 16.8
    def scene_story(self):
        self.section(0, "梯形花坛，要铺多少草皮")

        shp = trapezoid(GOLD, 0.2)
        self.play(Create(shp), run_time=1.5)

        bot_br = Brace(Line(A, B, color=GOLD), DOWN, buff=0.16, color=GOLD)
        bot_l = txt("下底 5 米", size=25, color=GOLD).next_to(bot_br, DOWN, buff=0.1)
        top_br = Brace(Line(D, C, color=BLUE), UP, buff=0.16, color=BLUE)
        top_l = txt("上底 3 米", size=25, color=BLUE).next_to(top_br, UP, buff=0.1)
        self.play(Create(bot_br), FadeIn(bot_l), run_time=0.9)
        self.play(Create(top_br), FadeIn(top_l), run_time=0.9)

        h_x = -2.8
        h_line = DashedLine([h_x, 1.1, 0], [h_x, -1.3, 0], color=GREEN,
                            stroke_width=2.6, dash_length=0.13)
        right = Square(side_length=0.24, color=GREEN, stroke_width=2)
        right.move_to([h_x + 0.12, -1.3 + 0.12, 0])
        h_l = txt("高 2 米", size=24, color=GREEN).move_to([-2.1, -0.15, 0])
        self.play(Create(h_line), Create(right), run_time=0.9)
        self.play(FadeIn(h_l, shift=RIGHT * 0.05), run_time=0.7)

        q = VGroup(
            txt("要铺多少平方米草皮？", size=28, color=CHALK),
            txt("上底和下底不一样长", size=26, color=DIM),
            txt("先把它变成学过的图形", size=27, color=GREEN),
        ).arrange(DOWN, buff=0.26).move_to([3.7, 0.55, 0])
        for t in q:
            self.play(FadeIn(t, shift=UP * 0.05), run_time=0.7)
        self.wait(2.2)
        self.finish_section()

    # ---------------- 1. 两个梯形拼成平行四边形 ---------------- 14.9
    def scene_pair(self):
        self.section(1, "两个一样的梯形，拼一拼")

        t1 = trapezoid(GOLD, 0.25)
        self.play(Create(t1), run_time=1.2)

        t2 = trapezoid(BLUE, 0.28)
        self.play(FadeIn(t2), run_time=0.7)
        self.play(Rotate(t2, PI, about_point=M), run_time=2.2, rate_func=smooth)

        rect_note = txt("正好拼成一个平行四边形", size=28, color=GREEN)
        rect_note.move_to([0, -2.4, 0])
        self.play(FadeIn(rect_note, shift=UP * 0.06), run_time=0.9)

        note = txt("平行四边形的面积，是两个梯形的 2 倍", size=26, color=CHALK)
        note.move_to([0, 2.35, 0])
        self.play(FadeIn(note, shift=DOWN * 0.05), run_time=0.8)
        self.wait(2.4)
        self.finish_section()

    # ---------------- 2. 底 = 上底 + 下底 ---------------- 13.9
    def scene_base(self):
        self.section(2, "平行四边形的底 = 上底 + 下底")

        t1 = trapezoid(GOLD, 0.25)
        t2 = trapezoid(BLUE, 0.28)
        t2.rotate(PI, about_point=M)
        self.play(FadeIn(t1), FadeIn(t2), run_time=1.0)

        full = Line([A[0], A[1], 0], [2.4, A[1], 0], color=GREEN)
        br = Brace(full, DOWN, buff=0.18, color=GREEN)
        lab = txt("底 = 上底 + 下底 = 3 + 5 = 8", size=26, color=GREEN)
        lab.next_to(br, DOWN, buff=0.1)
        self.play(Create(br), FadeIn(lab), run_time=1.1)

        h_line = DashedLine([-1.0, 1.1, 0], [-1.0, -1.3, 0], color=CHALK,
                            stroke_width=2.2, dash_length=0.13)
        h_l = txt("高不变，还是 2 米", size=25, color=CHALK).move_to([1.6, 1.7, 0])
        self.play(Create(h_line), run_time=0.7)
        self.play(FadeIn(h_l, shift=DOWN * 0.05), run_time=0.7)

        eq = txt("平行四边形的面积 = 8 × 2 = 16（平方米）", size=27, color=GOLD)
        eq.move_to([0, 2.45, 0])
        self.play(FadeIn(eq, shift=DOWN * 0.05), run_time=0.9)
        self.wait(2.0)
        self.finish_section()

    # ---------------- 3. 除以二，得到梯形面积 ---------------- 18.9
    def scene_formula(self):
        self.section(3, "一个梯形，面积要除以 2")

        line1 = txt("平行四边形是两个梯形拼成的", size=30, color=CHALK).move_to([0, 2.15, 0])
        self.play(FadeIn(line1, shift=UP * 0.05), run_time=0.9)

        line2 = txt("所以一个梯形的面积 = 平行四边形面积 ÷ 2", size=30, color=CHALK)
        line2.move_to([0, 1.15, 0])
        self.play(FadeIn(line2, shift=UP * 0.05), run_time=0.9)

        box = label_box("S =（上底 + 下底）× 高 ÷ 2", size=36, color=GOLD)
        box.move_to([0, -0.05, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.0)

        letter = label_box("S =（a + b）× h ÷ 2", size=34, color=GREEN)
        letter.move_to([0, -1.3, 0])
        self.play(FadeIn(letter, scale=0.97), run_time=1.0)

        note = txt("上底、下底、高，都要和这个梯形对上", size=26, color=DIM)
        note.move_to([0, -2.45, 0])
        self.play(FadeIn(note, shift=UP * 0.05), run_time=0.8)
        self.wait(2.2)
        self.finish_section()

    # ---------------- 4. 例题 ---------------- 14.8
    def scene_example(self):
        self.section(4, "上底 3 米，下底 5 米，高 2 米")

        rows = [
            ("S =（3 + 5）× 2 ÷ 2", CHALK),
            ("= 8 × 2 ÷ 2", BLUE),
            ("= 16 ÷ 2", CHALK),
            ("= 8（平方米）", GREEN),
        ]
        y = 1.85
        for s, c in rows:
            self.play(FadeIn(txt(s, size=36, color=c).move_to([-0.6, y, 0]), shift=UP * 0.04),
                      run_time=0.8)
            y -= 0.85

        ans = txt("草皮要 8 平方米", size=28, color=GOLD).move_to([0, -1.85, 0])
        self.play(FadeIn(ans, shift=UP * 0.06), run_time=0.9)

        tip = txt("别忘最后那一步除以 2", size=27, color=RED).move_to([0, -2.6, 0])
        self.play(FadeIn(tip, shift=UP * 0.05), run_time=0.8)
        self.wait(2.0)
        self.finish_section()

    # ---------------- 5. 反求高 ---------------- 14.6
    def scene_reverse(self):
        self.section(5, "已知面积，怎么求高")

        given = txt("面积 24 平方米，上底 5 米，下底 7 米", size=28, color=CHALK)
        given.move_to([0, 2.25, 0])
        self.play(FadeIn(given, shift=UP * 0.05), run_time=0.9)

        box = label_box("h = S × 2 ÷（a + b）", size=34, color=GOLD)
        box.move_to([0, 1.05, 0])
        self.play(FadeIn(box, scale=0.97), run_time=0.9)

        steps = VGroup(
            txt("h = 24 × 2 ÷（5 + 7）", size=34, color=CHALK),
            txt("= 48 ÷ 12", size=34, color=BLUE),
            txt("= 4（米）", size=34, color=GREEN),
        ).arrange(DOWN, buff=0.32, aligned_edge=LEFT).move_to([-0.2, -0.6, 0])
        for s in steps:
            self.play(FadeIn(s, shift=RIGHT * 0.05), run_time=0.7)
            self.wait(0.2)

        why = txt("先乘 2 还原，再除以两底之和", size=27, color=GOLD)
        why.move_to([0, -2.45, 0])
        self.play(FadeIn(why, shift=UP * 0.05), run_time=0.8)
        self.wait(2.0)
        self.finish_section()

    # ---------------- 6. 易错点 + 三句话 ---------------- 17.6
    def scene_warn(self):
        self.section(6, "三个易错点")

        items = [
            ("忘记除以 2", "两个梯形才拼成平行四边形"),
            ("上底下底弄反", "长的叫下底，短的叫上底"),
            ("高量成斜边", "高要垂直在两底之间"),
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
            label_box("① 两个梯形拼成平行四边形", size=24, color=GOLD),
            label_box("② 面积 =（上底 + 下底）× 高 ÷ 2", size=24, color=CHALK),
            label_box("③ 求高先乘 2，再除以两底之和", size=24, color=GREEN),
        ).arrange(DOWN, buff=0.2).move_to([0, -1.65, 0])
        for r in rows:
            self.play(FadeIn(r, shift=RIGHT * 0.06), run_time=0.6)
            self.wait(0.55)

        self.wait(1.0)
        self.finish_section()

    def construct(self):
        self.scene_story()
        self.clear_stage()
        self.scene_pair()
        self.clear_stage()
        self.scene_base()
        self.clear_stage()
        self.scene_formula()
        self.clear_stage()
        self.scene_example()
        self.clear_stage()
        self.scene_reverse()
        self.clear_stage()
        self.scene_warn()
        self.clear_stage(0.8)