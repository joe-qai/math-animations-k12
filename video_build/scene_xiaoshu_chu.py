# -*- coding: utf-8 -*-
"""小数除法：除数是整数、整数部分不够除、除数是小数、商不变。五年级上册。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


def step_row(n: str, s: str, color: str = CHALK, size: int = 30,
             y: float = 0.0) -> VGroup:
    """带序号的推导行，整体左对齐。"""
    c = Circle(radius=0.21, color=color, stroke_width=1.8).move_to([-5.05, y, 0])
    num = txt(n, size=19, color=color).move_to([-5.05, y, 0])
    body = txt(s, size=size, color=color)
    body.next_to(c, RIGHT, buff=0.42, aligned_edge=LEFT)
    return VGroup(c, num, body)


class XiaoshuChuScene(NarratedScene):
    lesson = "xiaoshu-chu"

    def clear_stage(self, run_time: float = 0.5):
        keep = {id(self._track), id(self._fill)}
        junk = [m for m in self.mobjects if id(m) not in keep]
        if junk:
            self.play(*[FadeOut(m) for m in junk], run_time=run_time)
        self.cur_title = None
        self.cur_sub = None

    # ---------------- 0. 三支笔 ---------------- 17.1
    def scene_story(self):
        self.section(0, "4.5 元买 3 支笔")

        pencils = VGroup()
        for i in range(3):
            x = -5.1 + i * 0.9
            body = Rectangle(width=0.28, height=1.9, color=GOLD, stroke_width=1.8,
                             fill_color=GOLD, fill_opacity=0.25).move_to([0, 0.15, 0])
            tip = Triangle(color=GOLD, stroke_width=1.6,
                           fill_color=GOLD, fill_opacity=0.25).scale(0.15)
            tip.rotate(PI).move_to([0, -0.95, 0])
            pencils.add(VGroup(body, tip).rotate(14 * DEGREES).move_to([x, 0.9, 0]))
        self.play(LaggedStart(*[FadeIn(p) for p in pencils], lag_ratio=0.16), run_time=1.5)

        p1 = txt("一共 4.5 元", size=28, color=GOLD).move_to([-4.2, -0.55, 0])
        q1 = txt("一支 = ?", size=34, color=CHALK).move_to([-4.2, -1.35, 0])
        self.play(FadeIn(p1, shift=UP * 0.05), run_time=0.7)
        self.play(FadeIn(q1, shift=UP * 0.06), run_time=0.7)

        rope = Line([2.0, 0.95, 0], [5.6, 0.95, 0], color=BLUE, stroke_width=6)
        cuts = VGroup(*[Line([2.0 + i * 0.9, 0.72, 0], [2.0 + i * 0.9, 1.18, 0],
                             color=CHALK, stroke_width=2) for i in range(5)])
        self.play(Create(rope), run_time=0.9)
        self.play(LaggedStart(*[Create(c) for c in cuts], lag_ratio=0.12), run_time=1.0)
        p2 = txt("2.4 米，平均分成 4 段", size=26, color=BLUE).move_to([3.8, 0.05, 0])
        q2 = txt("每段 = ?", size=32, color=CHALK).move_to([3.8, -0.7, 0])
        self.play(FadeIn(p2, shift=UP * 0.05), run_time=0.7)
        self.play(FadeIn(q2, shift=UP * 0.06), run_time=0.7)

        note = txt("4.5 ÷ 3 和 2.4 ÷ 4，都是小数除法", size=28, color=GREEN)
        note.move_to([0, -2.45, 0])
        self.play(FadeIn(note, shift=UP * 0.07), run_time=0.9)
        self.wait(1.6)
        self.finish_section()

    # ---------------- 1. 除数是整数 ---------------- 14.4
    def scene_int(self):
        self.section(1, "除数是整数：小数点对齐")

        big = txt("9.6 ÷ 3", size=50, color=GOLD).move_to([0, 2.35, 0])
        self.play(FadeIn(big, shift=UP * 0.06), run_time=0.8)

        r1 = step_row("1", "96 ÷ 3 = 32", CHALK, 30, y=1.35)
        r2 = step_row("2", "商的小数点，和被除数对齐", BLUE, 30, y=0.5)
        self.play(FadeIn(r1, shift=RIGHT * 0.06), run_time=0.7)
        self.play(FadeIn(r2, shift=RIGHT * 0.06), run_time=0.8)

        # 上下对齐示意
        def num_group(s: str, color: str, at) -> VGroup:
            g = VGroup(*[txt(ch, size=46, color=color) for ch in s])
            g.arrange(RIGHT, buff=0.02).move_to(at)
            return g

        a = num_group("9.6", CHALK, [-2.0, -0.55, 0])
        b = num_group("3.2", GREEN, [-2.0, -1.45, 0])
        line1 = Line([-3.0, -1.0, 0], [1.1, -1.0, 0], color=DIM, stroke_width=2)
        self.play(FadeIn(a), run_time=0.6)
        self.play(Create(line1), run_time=0.5)
        self.play(FadeIn(b), run_time=0.7)

        dash = VGroup()
        dx = a[1].get_center()[0] + 0.10
        y1 = a[1].get_center()[1] - 0.12
        y2 = b[1].get_center()[1] - 0.04
        xg = dx + 0.34
        dash.add(DashedLine([xg, y1, 0], [xg, y2, 0], color=GOLD,
                            stroke_width=2.6, dash_length=0.08))
        dash.add(Line([dx, y1, 0], [xg, y1, 0], color=GOLD, stroke_width=2.4))
        dash.add(Line([dx, y2, 0], [xg, y2, 0], color=GOLD, stroke_width=2.4))
        lab = txt("小数点上下对齐", size=25, color=GOLD).move_to([2.05, -1.0, 0])
        self.play(Create(dash), run_time=0.8)
        self.play(FadeIn(lab, shift=RIGHT * 0.05), run_time=0.7)

        ans = txt("9.6 ÷ 3 = 3.2", size=32, color=GREEN).move_to([0, -2.35, 0])
        self.play(FadeIn(ans, shift=UP * 0.06), run_time=0.8)
        self.wait(1.4)
        self.finish_section()

    # ---------------- 2. 整数部分不够除 ---------------- 14.2
    def scene_less(self):
        self.section(2, "个位不够商 1，就商 0")

        big = txt("1.2 ÷ 5", size=50, color=GOLD).move_to([0, 2.35, 0])
        self.play(FadeIn(big, shift=UP * 0.06), run_time=0.8)

        r1 = step_row("1", "个位 1 不够商 1，商 0", CHALK, 29, y=1.4)
        r2 = step_row("2", "点上小数点，12 个 0.1 继续除", CHALK, 29, y=0.55)
        r3 = step_row("3", "12 ÷ 5 = 2 余 2，添 0 得 24 个 0.01", BLUE, 25, y=-0.25)
        self.play(FadeIn(r1, shift=RIGHT * 0.06), run_time=0.8)
        self.play(FadeIn(r2, shift=RIGHT * 0.06), run_time=0.8)
        self.play(FadeIn(r3, shift=RIGHT * 0.06), run_time=0.9)

        zero = txt("0.", size=76, color=GOLD).move_to([-2.3, -1.55, 0])
        rest = txt("24", size=76, color=GREEN).move_to([-0.55, -1.55, 0])
        self.play(Write(zero), run_time=0.9)
        self.play(Write(rest), run_time=0.9)

        tip = txt("商的个位不够 1，一定要先写 0，再点小数点", size=26, color=GOLD)
        tip.move_to([1.0, -2.6, 0])
        self.play(FadeIn(tip, shift=UP * 0.06), run_time=0.9)
        self.wait(1.6)
        self.finish_section()

    # ---------------- 3. 除数是小数 ---------------- 15.3
    def scene_dec(self):
        self.section(3, "除数是小数，先变成整数")

        big = txt("0.6 ÷ 0.3", size=50, color=GOLD).move_to([0, 2.35, 0])
        self.play(FadeIn(big, shift=UP * 0.06), run_time=0.8)

        a = txt("0.6", size=44, color=CHALK).move_to([-3.2, 1.2, 0])
        b = txt("0.3", size=44, color=CHALK).move_to([1.8, 1.2, 0])
        div = txt("÷", size=44, color=DIM).move_to([-0.7, 1.2, 0])
        self.play(FadeIn(a), FadeIn(div), FadeIn(b), run_time=1.0)

        a2 = txt("6", size=44, color=GREEN).move_to([-3.2, 0.15, 0])
        b2 = txt("3", size=44, color=GREEN).move_to([1.8, 0.15, 0])
        ar1 = Arrow([-3.2, 0.85, 0], [-3.2, 0.5, 0], color=GOLD, stroke_width=2.2,
                    buff=0.02, max_tip_length_to_length_ratio=0.3)
        ar2 = Arrow([1.8, 0.85, 0], [1.8, 0.5, 0], color=GOLD, stroke_width=2.2,
                    buff=0.02, max_tip_length_to_length_ratio=0.3)
        m1 = txt("×10", size=24, color=GOLD).move_to([-2.35, 0.72, 0])
        m2 = txt("×10", size=24, color=GOLD).move_to([2.65, 0.72, 0])
        self.play(GrowArrow(ar1), GrowArrow(ar2), FadeIn(m1), FadeIn(m2), run_time=1.0)
        self.play(FadeIn(a2), FadeIn(b2), run_time=0.8)

        res = txt("6 ÷ 3 = 2", size=38, color=GREEN).move_to([0, -0.95, 0])
        self.play(FadeIn(res, shift=UP * 0.06), run_time=0.9)

        rule = label_box("被除数和除数同时扩大相同的倍数，商不变", size=24, color=BLUE)
        rule.move_to([0, -2.1, 0])
        self.play(FadeIn(rule, scale=0.97), run_time=0.9)
        self.wait(2.0)
        self.finish_section()

    # ---------------- 4. 都扩大，位数不够补 0 ---------------- 16.6
    def scene_move(self):
        self.section(4, "1.44 ÷ 1.2 怎么算")

        big = txt("1.44 ÷ 1.2", size=48, color=GOLD).move_to([0, 2.35, 0])
        self.play(FadeIn(big, shift=UP * 0.06), run_time=0.8)

        r1 = step_row("1", "除数 1.2 扩大 10 倍，变成 12", CHALK, 28, y=1.45)
        r2 = step_row("2", "被除数 1.44 也扩大 10 倍，变成 14.4", CHALK, 28, y=0.65)
        r3 = step_row("3", "14.4 ÷ 12 = 1.2", GREEN, 30, y=-0.15)
        self.play(FadeIn(r1, shift=RIGHT * 0.06), run_time=0.8)
        self.play(FadeIn(r2, shift=RIGHT * 0.06), run_time=0.8)
        self.play(FadeIn(r3, shift=RIGHT * 0.06), run_time=0.9)

        ans = txt("1.44 ÷ 1.2 = 1.2", size=32, color=GOLD).move_to([0, -1.2, 0])
        self.play(FadeIn(ans, shift=UP * 0.06), run_time=0.8)

        note = VGroup(
            txt("位数不够时，用 0 补足", size=25, color=BLUE),
            txt("1.2 ÷ 0.03 = 120 ÷ 3 = 40", size=30, color=CHALK),
        ).arrange(DOWN, buff=0.22).move_to([0, -2.35, 0])
        self.play(FadeIn(note[0], shift=UP * 0.05), run_time=0.8)
        self.play(FadeIn(note[1], shift=UP * 0.05), run_time=0.9)
        self.wait(1.8)
        self.finish_section()

    # ---------------- 5. 四个易错点 ---------------- 14.7
    def scene_warn(self):
        self.section(5, "四个易错点")

        items = [
            ("商的小数点没对齐", "点和被除数的小数点对齐"),
            ("只把除数扩大", "被除数要同样扩大"),
            ("商中间的 0 漏写", "不够商 1 就写 0 占位"),
            ("末尾有余数不管", "添 0 继续除"),
        ]
        y = 1.85
        for bad_s, note in items:
            bad = txt(bad_s, size=27, color=RED).move_to([-3.3, y, 0])
            n = txt(note, size=25, color=GREEN).move_to([3.25, y, 0])
            cross = Line(bad.get_left() + [-0.1, -0.12, 0],
                         bad.get_right() + [0.1, 0.14, 0],
                         color=RED, stroke_width=2.8)
            self.play(FadeIn(bad, shift=RIGHT * 0.05), run_time=0.55)
            self.play(Create(cross), FadeIn(n, shift=RIGHT * 0.05), run_time=0.65)
            self.wait(0.55)
            y -= 1.0

        tip = txt("小数除法，关键就一句：把除数变成整数", size=27, color=GOLD)
        tip.move_to([0, -2.5, 0])
        self.play(FadeIn(tip, shift=UP * 0.06), run_time=0.9)
        self.wait(1.2)
        self.finish_section()

    # ---------------- 6. 三句话 ---------------- 14.5
    def scene_summary(self):
        self.section(6, "三句话")

        rows = VGroup(
            label_box("① 除数是整数：商的小数点对齐", size=26, color=GOLD),
            label_box("② 除数是小数：先扩大成整数", size=26, color=CHALK),
            label_box("③ 不够除商 0，末尾添 0 继续", size=26, color=GREEN),
        ).arrange(DOWN, buff=0.3).move_to([0, 1.45, 0])
        for r in rows:
            self.play(FadeIn(r, shift=RIGHT * 0.07), run_time=0.65)
            self.wait(0.55)

        demo = txt("1.44 ÷ 1.2 = 14.4 ÷ 12 = 1.2", size=29, color=BLUE)
        demo.move_to([0, -1.2, 0])
        self.play(FadeIn(demo, shift=UP * 0.06), run_time=0.9)
        self.wait(0.6)

        end = txt("把除数变整数，小数除法就变整数除法", size=27, color=GOLD)
        end.move_to([0, -2.1, 0])
        self.play(FadeIn(end, shift=UP * 0.06), run_time=0.8)
        self.wait(1.6)
        self.finish_section()

    def construct(self):
        self.scene_story()
        self.clear_stage()
        self.scene_int()
        self.clear_stage()
        self.scene_less()
        self.clear_stage()
        self.scene_dec()
        self.clear_stage()
        self.scene_move()
        self.clear_stage()
        self.scene_warn()
        self.clear_stage()
        self.scene_summary()
        self.clear_stage(0.8)