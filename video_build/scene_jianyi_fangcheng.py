# -*- coding: utf-8 -*-
"""简易方程：方程的意义、等式性质、解 x+b=c 与 ax±b=c、检验。五年级下册。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


def mark(ok: bool, center, size: float = 0.34) -> VGroup:
    """对勾 / 叉。"""
    cx, cy = center[0], center[1]
    if ok:
        g = VGroup(
            Line([cx - size, cy, 0], [cx - size * 0.28, cy - size * 0.72, 0],
                 color=GREEN, stroke_width=5),
            Line([cx - size * 0.28, cy - size * 0.72, 0], [cx + size, cy + size * 0.78, 0],
                 color=GREEN, stroke_width=5),
        )
    else:
        g = VGroup(
            Line([cx - size, cy - size * 0.7, 0], [cx + size, cy + size * 0.7, 0],
                 color=RED, stroke_width=4.5),
            Line([cx - size, cy + size * 0.7, 0], [cx + size, cy - size * 0.7, 0],
                 color=RED, stroke_width=4.5),
        )
    return g


def pan(beam_y: float, cx: float) -> VGroup:
    """挂在横梁上的秤盘。"""
    hanger = Line([cx, beam_y, 0], [cx, beam_y - 0.6, 0], color=DIM, stroke_width=2.2)
    plate = Rectangle(width=1.35, height=0.1, color=CHALK, stroke_width=2.5,
                      fill_color=CHALK, fill_opacity=0.12)
    plate.move_to([cx, beam_y - 0.66, 0])
    rim = VGroup(
        Line([cx - 0.62, beam_y - 0.66, 0], [cx - 0.78, beam_y - 0.5, 0], color=CHALK, stroke_width=2),
        Line([cx + 0.62, beam_y - 0.66, 0], [cx + 0.78, beam_y - 0.5, 0], color=CHALK, stroke_width=2),
    )
    return VGroup(hanger, plate, rim)


class JianyiFangchengScene(NarratedScene):
    lesson = "jianyi-fangcheng"

    def clear_stage(self, run_time: float = 0.5):
        keep = {id(self._track), id(self._fill)}
        junk = [m for m in self.mobjects if id(m) not in keep]
        if junk:
            self.play(*[FadeOut(m) for m in junk], run_time=run_time)
        self.cur_title = None
        self.cur_sub = None

    # ---------------- 0. 天平：x + 2 = 5 ---------------- 18.5
    def scene_story(self):
        self.section(0, "天平平衡了，苹果有多重")

        beam_y = 1.15
        cx = -3.3
        pillar = Line([cx, -1.95, 0], [cx, beam_y, 0], color=CHALK, stroke_width=4)
        base = Line([cx - 0.85, -1.95, 0], [cx + 0.85, -1.95, 0], color=CHALK, stroke_width=5)
        beam = Line([cx - 1.75, beam_y, 0], [cx + 1.75, beam_y, 0], color=CHALK, stroke_width=5)
        self.play(Create(pillar), Create(base), run_time=1.0)
        self.play(Create(beam), run_time=0.9)

        lp = pan(beam_y, cx - 1.55)
        rp = pan(beam_y, cx + 1.55)
        self.play(LaggedStart(Create(lp), Create(rp), lag_ratio=0.2), run_time=1.3)

        apple = Circle(radius=0.28, color=RED, stroke_width=2.5,
                       fill_color=RED, fill_opacity=0.45).move_to([cx - 1.88, beam_y - 0.35, 0])
        w2 = Rectangle(width=0.32, height=0.32, color=GOLD, stroke_width=2.5,
                       fill_color=GOLD, fill_opacity=0.4).move_to([cx - 1.22, beam_y - 0.38, 0])
        self.play(FadeIn(apple, shift=UP * 0.08), run_time=0.7)
        self.play(FadeIn(w2, shift=UP * 0.08), run_time=0.6)

        w5_block = Rectangle(width=1.0, height=0.46, color=GOLD, stroke_width=2.5,
                             fill_color=GOLD, fill_opacity=0.35).move_to([cx + 1.55, beam_y - 0.38, 0])
        w5_txt = txt("5 克", size=24, color=CHALK).move_to([cx + 1.55, beam_y - 0.38, 0])
        w5 = VGroup(w5_block, w5_txt)
        self.play(FadeIn(w5, shift=UP * 0.08), run_time=0.7)

        lab = VGroup(
            txt("苹果 + 2 克", size=24, color=RED),
            txt("正好平衡", size=24, color=GREEN),
        ).arrange(DOWN, buff=0.2).move_to([cx - 1.5, -2.45, 0])
        self.play(FadeIn(lab[0], shift=UP * 0.05), run_time=0.6)
        self.play(FadeIn(lab[1], shift=UP * 0.05), run_time=0.6)

        eq = txt("x + 2 = 5", size=54, color=GOLD).move_to([3.35, 1.55, 0])
        self.play(FadeIn(eq, shift=RIGHT * 0.06), run_time=0.9)

        note = VGroup(
            txt("把不知道的数记作 x", size=26, color=CHALK),
            txt("含有未知数的等式，叫方程", size=27, color=GREEN),
        ).arrange(DOWN, buff=0.24).move_to([3.35, -0.35, 0])
        self.play(FadeIn(note[0], shift=UP * 0.05), run_time=0.7)
        self.play(FadeIn(note[1], shift=UP * 0.05), run_time=0.8)
        self.wait(2.2)
        self.finish_section()

    # ---------------- 1. 两个条件 ---------------- 19.0
    def scene_def(self):
        self.section(1, "方程要同时满足两个条件")

        conds = VGroup(
            label_box("① 含有未知数", size=26, color=GOLD),
            label_box("② 必须是等式", size=26, color=BLUE),
        ).arrange(RIGHT, buff=0.7).move_to([0, 2.05, 0])
        self.play(FadeIn(conds[0], shift=UP * 0.05), run_time=0.7)
        self.play(FadeIn(conds[1], shift=UP * 0.05), run_time=0.7)

        rows = [
            ("x + 3", False, "只有式子，没有等号"),
            ("3 + 5 = 8", False, "是等式，但没有未知数"),
            ("x + 3 = 9", True, "两个条件都满足，是方程"),
        ]
        y = 0.85
        for expr, ok, why in rows:
            e = txt(expr, size=36, color=CHALK if not ok else GOLD).move_to([-3.4, y, 0])
            m = mark(ok, [-0.9, y, 0])
            w = txt(why, size=25, color=GREEN if ok else DIM).move_to([3.2, y, 0])
            self.play(FadeIn(e, shift=RIGHT * 0.05), run_time=0.6)
            self.play(Create(m), FadeIn(w, shift=RIGHT * 0.05), run_time=0.7)
            self.wait(0.6)
            y -= 1.15

        tip = txt("两个条件缺一不可", size=27, color=GOLD).move_to([0, -2.45, 0])
        self.play(FadeIn(tip, shift=UP * 0.06), run_time=0.8)
        self.wait(1.8)
        self.finish_section()

    # ---------------- 2. 等式的性质 ---------------- 18.5
    def scene_prop(self):
        self.section(2, "天平不动，等式也不变")

        top = txt("x + 3 = 9", size=44, color=CHALK).move_to([0, 2.15, 0])
        self.play(FadeIn(top, shift=UP * 0.05), run_time=0.8)

        al = txt("两边同时加 2", size=24, color=GOLD).move_to([0, 2.78, 0])
        arrow = Arrow([0, 1.72, 0], [0, 1.32, 0], color=GOLD, stroke_width=2.4,
                      buff=0.02, max_tip_length_to_length_ratio=0.55)
        self.play(FadeIn(al, shift=DOWN * 0.05), run_time=0.6)
        self.play(GrowArrow(arrow), run_time=0.7)

        bot = txt("x + 3 + 2 = 9 + 2", size=40, color=GOLD).move_to([0, 0.85, 0])
        self.play(FadeIn(bot, shift=UP * 0.05), run_time=0.8)

        rules = VGroup(
            label_box("两边同时加或减同一个数，等式不变", size=26, color=CHALK),
            label_box("两边同时乘或除以同一个不为 0 的数，等式不变", size=26, color=BLUE),
        ).arrange(DOWN, buff=0.3).move_to([0, -0.55, 0])
        self.play(FadeIn(rules[0], shift=RIGHT * 0.05), run_time=0.8)
        self.play(FadeIn(rules[1], shift=RIGHT * 0.05), run_time=0.9)

        note = txt("天平两边同时加、同时减，仍然平衡", size=26, color=DIM)
        note.move_to([0, -2.4, 0])
        self.play(FadeIn(note, shift=UP * 0.05), run_time=0.8)
        self.wait(2.4)
        self.finish_section()

    # ---------------- 3. 解 x + 3 = 9 ---------------- 17.7
    def scene_plus(self):
        self.section(3, "解 x + 3 = 9")

        l1 = txt("x + 3 = 9", size=42, color=CHALK).move_to([-1.2, 2.1, 0])
        self.play(FadeIn(l1), run_time=0.8)

        l2 = txt("x + 3 − 3 = 9 − 3", size=40, color=BLUE).move_to([-0.6, 1.0, 0])
        self.play(FadeIn(l2, shift=UP * 0.05), run_time=1.0)

        note = txt("两边同时减 3", size=25, color=BLUE).move_to([3.9, 1.0, 0])
        self.play(FadeIn(note, shift=LEFT * 0.05), run_time=0.8)

        l3 = txt("x = 6", size=42, color=GOLD).move_to([-3.0, -0.15, 0])
        self.play(FadeIn(l3, shift=UP * 0.05), run_time=0.9)

        chk = VGroup(
            txt("检验：6 + 3 = 9", size=29, color=GREEN),
            txt("左右相等，x = 6 正确", size=27, color=GREEN),
        ).arrange(DOWN, buff=0.22).move_to([1.9, -1.4, 0])
        self.play(FadeIn(chk[0], shift=UP * 0.05), run_time=0.8)
        self.play(FadeIn(chk[1], shift=UP * 0.05), run_time=0.8)

        tip = txt("解完一定要代回去检验", size=27, color=GOLD).move_to([0, -2.55, 0])
        self.play(FadeIn(tip, shift=UP * 0.05), run_time=0.8)
        self.wait(1.8)
        self.finish_section()

    # ---------------- 4. 2x + 4 = 12 ---------------- 17.5
    def scene_axb(self):
        self.section(4, "解 2x + 4 = 12")

        rows = [
            ("2x + 4 = 12", CHALK),
            ("2x + 4 − 4 = 12 − 4", BLUE),
            ("2x = 8", CHALK),
            ("2x ÷ 2 = 8 ÷ 2", BLUE),
            ("x = 4", GOLD),
        ]
        y = 2.3
        for s, c in rows:
            self.play(FadeIn(txt(s, size=38, color=c).move_to([-1.0, y, 0]), shift=UP * 0.04),
                      run_time=0.75)
            y -= 0.82

        n1 = txt("先减 4", size=24, color=BLUE).move_to([4.2, 1.5, 0])
        n2 = txt("再除以 2", size=24, color=BLUE).move_to([4.2, -0.05, 0])
        self.play(FadeIn(n1, shift=LEFT * 0.05), run_time=0.7)
        self.play(FadeIn(n2, shift=LEFT * 0.05), run_time=0.7)

        chk = txt("检验：2 × 4 + 4 = 12，正确", size=27, color=GREEN).move_to([0, -2.35, 0])
        self.play(FadeIn(chk, shift=UP * 0.05), run_time=0.9)
        self.wait(2.4)
        self.finish_section()

    # ---------------- 5. 2x − 4 = 12 ---------------- 17.7
    def scene_axminus(self):
        self.section(5, "解 2x − 4 = 12")

        rows = [
            ("2x − 4 = 12", CHALK),
            ("2x − 4 + 4 = 12 + 4", BLUE),
            ("2x = 16", CHALK),
            ("2x ÷ 2 = 16 ÷ 2", BLUE),
            ("x = 8", GOLD),
        ]
        y = 2.3
        for s, c in rows:
            self.play(FadeIn(txt(s, size=38, color=c).move_to([-1.0, y, 0]), shift=UP * 0.04),
                      run_time=0.75)
            y -= 0.82

        n1 = txt("先加 4", size=24, color=BLUE).move_to([4.2, 1.5, 0])
        n2 = txt("再除以 2", size=24, color=BLUE).move_to([4.2, -0.05, 0])
        self.play(FadeIn(n1, shift=LEFT * 0.05), run_time=0.7)
        self.play(FadeIn(n2, shift=LEFT * 0.05), run_time=0.7)

        chk = VGroup(
            txt("检验：2 × 8 − 4 = 12，正确", size=27, color=GREEN),
            txt("先处理加减，再处理乘除", size=26, color=GOLD),
        ).arrange(DOWN, buff=0.22).move_to([0, -2.1, 0])
        self.play(FadeIn(chk[0], shift=UP * 0.05), run_time=0.8)
        self.play(FadeIn(chk[1], shift=UP * 0.05), run_time=0.8)
        self.wait(2.2)
        self.finish_section()

    # ---------------- 6. 易错点 + 三句话 ---------------- 20.0
    def scene_warn(self):
        self.section(6, "三个易错点")

        items = [
            ("有等号就是方程", "还要含有未知数"),
            ("只变一边也行", "两边要同时变"),
            ("解完不用检验", "代回原方程检验"),
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
            label_box("① 方程：有未知数，还要是等式", size=24, color=GOLD),
            label_box("② 两边同加同减、同乘同除", size=24, color=CHALK),
            label_box("③ 先加减后乘除，解完必检验", size=24, color=GREEN),
        ).arrange(DOWN, buff=0.2).move_to([0, -1.65, 0])
        for r in rows:
            self.play(FadeIn(r, shift=RIGHT * 0.06), run_time=0.6)
            self.wait(0.55)

        self.wait(1.0)
        self.finish_section()

    def construct(self):
        self.scene_story()
        self.clear_stage()
        self.scene_def()
        self.clear_stage()
        self.scene_prop()
        self.clear_stage()
        self.scene_plus()
        self.clear_stage()
        self.scene_axb()
        self.clear_stage()
        self.scene_axminus()
        self.clear_stage()
        self.scene_warn()
        self.clear_stage(0.8)