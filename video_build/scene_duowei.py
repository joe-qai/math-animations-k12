# -*- coding: utf-8 -*-
"""多位数乘一位数：口算拆分、竖式、进位。三年级上册。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403

STEP = 0.62          # 数字列间距


def digits(s: str, x_right: float, y: float, size: int = 62,
           color: str = CHALK) -> VGroup:
    """把一串数字按固定列宽排好，右对齐到 x_right。"""
    g = VGroup()
    for i, ch in enumerate(reversed(s)):
        g.add(txt(ch, size=size, color=color).move_to([x_right - i * STEP, y, 0]))
    return g


def underline(x_right: float, y: float, cols: int, color: str = CHALK) -> Line:
    left = x_right - (cols - 1) * STEP - 0.42
    return Line([left, y, 0], [x_right + 0.42, y, 0], color=color, stroke_width=3)


class DuoweiScene(NarratedScene):
    lesson = "duowei-cheng-yiwei"

    def clear_stage(self, run_time: float = 0.5):
        keep = {id(self._track), id(self._fill)}
        junk = [m for m in self.mobjects if id(m) not in keep]
        if junk:
            self.play(*[FadeOut(m) for m in junk], run_time=run_time)
        self.cur_title = None
        self.cur_sub = None

    # ---------------- 0. 三箱牛奶 ----------------
    def scene_story(self):
        self.section(0, "三箱牛奶，一共多少盒")

        crates = VGroup()
        for i in range(3):
            box = RoundedRectangle(corner_radius=0.12, width=2.0, height=1.55,
                                   stroke_color=GOLD, stroke_width=2.4,
                                   fill_color=GOLD, fill_opacity=0.08)
            box.move_to([-3.6 + i * 3.6, 0.55, 0])
            n = txt("24 盒", size=34, color=GOLD).move_to(box)
            crates.add(VGroup(box, n))
        self.play(LaggedStart(*[FadeIn(c, shift=UP * 0.1) for c in crates], lag_ratio=0.18),
                  run_time=1.4)

        lab = txt("每箱 24 盒", size=26, color=DIM).move_to([0, -0.65, 0])
        self.play(FadeIn(lab), run_time=0.5)

        q = txt("一共多少盒？", size=36, color=CHALK).move_to([0, -1.5, 0])
        expr = txt("24 × 3 = ?", size=54, color=GOLD).move_to([0, -2.45, 0])
        self.play(FadeIn(q, shift=UP * 0.08), run_time=0.6)
        self.play(Write(expr), run_time=1.0)
        self.finish_section()

    # ---------------- 1. 口算：拆成整十和个位 ----------------
    def scene_split(self):
        self.section(1, "口算：先拆成 20 和 4")

        split = VGroup(
            txt("24", size=54, color=CHALK),
            txt("=", size=54, color=DIM),
            txt("20", size=54, color=GOLD),
            txt("+", size=54, color=DIM),
            txt("4", size=54, color=BLUE),
        ).arrange(RIGHT, buff=0.28).move_to([0, 2.05, 0])
        self.play(Write(split), run_time=1.2)

        l1 = VGroup(
            txt("20 × 3 = 60", size=50, color=GOLD),
        ).move_to([-2.6, 0.85, 0])
        l2 = txt("4 × 3 = 12", size=50, color=BLUE).move_to([-2.6, -0.2, 0])
        self.play(Write(l1), run_time=0.9)
        self.play(Write(l2), run_time=0.9)

        plus = txt("60 + 12 = 72", size=54, color=GREEN).move_to([0.4, -1.35, 0])
        self.play(Write(plus), run_time=1.1)

        res = txt("24 × 3 = 72", size=50, color=GOLD).move_to([0, -2.5, 0])
        self.play(FadeIn(res, shift=UP * 0.08), run_time=0.8)
        self.finish_section()

    # ---------------- 2. 竖式：从个位乘起 ----------------
    def scene_vertical(self):
        self.section(2, "竖式：从个位开始乘")

        x_r = 1.2
        top = digits("24", x_r, 1.95)
        mul = digits("3", x_r, 1.05, color=BLUE)
        times = txt("×", size=60, color=BLUE).move_to([x_r + 0.82, 1.05, 0])
        line = underline(x_r, 0.6, 2)
        self.play(Write(top), run_time=0.8)
        self.play(Write(times), Write(mul), run_time=0.6)
        self.play(Create(line), run_time=0.5)

        # 个位：3 × 4 = 12
        box4 = SurroundingRectangle(top[0], color=GOLD, buff=0.08, stroke_width=2)
        self.play(Create(box4), run_time=0.5)
        n1 = txt("3 × 4 = 12", size=28, color=GOLD).move_to([4.5, 1.95, 0])
        self.play(FadeIn(n1, shift=LEFT * 0.08), run_time=0.6)

        unit = digits("2", x_r, 0.05, color=GOLD)
        carry = txt("1", size=24, color=RED).move_to([x_r - STEP + 0.08, 2.5, 0])
        self.play(Write(unit), run_time=0.5)
        self.play(FadeIn(carry, shift=UP * 0.05), run_time=0.4)

        # 十位：3 × 2 = 6，再加进位 1
        n2 = txt("3 × 2 = 6，6 + 1 = 7", size=25, color=GOLD).move_to([4.6, 0.32, 0])
        self.play(FadeIn(n2, shift=LEFT * 0.08), run_time=0.7)
        ten = digits("7", x_r - STEP, 0.05, color=GOLD)
        self.play(Indicate(carry, color=RED, scale_factor=1.25), run_time=0.5)
        self.play(Write(ten), run_time=0.6)

        ans = txt("24 × 3 = 72", size=40, color=GREEN).move_to([0, -1.55, 0])
        self.play(FadeIn(ans, shift=UP * 0.08), run_time=0.7)
        self.finish_section()

    # ---------------- 3. 进位规则 ----------------
    def scene_carry(self):
        self.section(3, "进位：满几十，进几")

        big = txt("满几十，就向前一位进几", size=48, color=GOLD).move_to([0, 2.1, 0])
        self.play(Write(big), run_time=1.2)

        ex = txt("3 × 4 = 12", size=56, color=CHALK).move_to([-3.4, 0.6, 0])
        self.play(Write(ex), run_time=0.9)

        a1 = label_box("个位写 2", size=30, color=CHALK).move_to([1.2, 1.05, 0])
        a2 = label_box("十位进 1", size=30, color=RED).move_to([1.2, 0.15, 0])
        self.play(FadeIn(a1, shift=UP * 0.06), run_time=0.5)
        self.play(FadeIn(a2, shift=UP * 0.06), run_time=0.5)

        note = txt("进位的 1 写小一点，放在前一位的右下角", size=26, color=DIM)
        note.move_to([0, -0.95, 0])
        self.play(FadeIn(note), run_time=0.6)

        warn = txt("算下一位时，别忘了把这个 1 加上", size=30, color=GREEN)
        warn.move_to([0, -1.95, 0])
        self.play(FadeIn(warn, shift=UP * 0.08), run_time=0.7)
        self.finish_section()

    # ---------------- 4. 连续进位 ----------------
    def scene_chain(self):
        self.section(4, "连续进位：128 × 4")

        x_r = 0.5
        top = digits("128", x_r, 2.0, size=58)
        mul = digits("4", x_r, 1.16, size=58, color=BLUE)
        times = txt("×", size=56, color=BLUE).move_to([x_r + 0.82, 1.16, 0])
        line = underline(x_r, 0.72, 3)
        self.play(Write(top), run_time=1.0)
        self.play(Write(times), Write(mul), run_time=0.5)
        self.play(Create(line), run_time=0.5)

        # 个位
        n1 = txt("4 × 8 = 32 → 写 2 进 3", size=23, color=GOLD).move_to([4.3, 2.0, 0])
        self.play(FadeIn(n1, shift=LEFT * 0.06), run_time=0.6)
        c3 = txt("3", size=22, color=RED).move_to([x_r - STEP + 0.05, 2.55, 0])
        r2 = digits("2", x_r, 0.16, size=58, color=GOLD)
        self.play(Write(r2), FadeIn(c3), run_time=0.7)

        # 十位
        n2 = txt("4 × 2 = 8，8 + 3 = 11 → 写 1 进 1", size=21, color=GOLD).move_to([4.6, 1.16, 0])
        self.play(FadeIn(n2, shift=LEFT * 0.06), run_time=0.6)
        c1 = txt("1", size=22, color=RED).move_to([x_r - 2 * STEP + 0.05, 2.55, 0])
        r1 = digits("1", x_r - STEP, 0.16, size=58, color=GOLD)
        self.play(Write(r1), FadeIn(c1), run_time=0.7)

        # 百位
        n3 = txt("4 × 1 = 4，4 + 1 = 5", size=23, color=GOLD).move_to([4.3, 0.32, 0])
        self.play(FadeIn(n3, shift=LEFT * 0.06), run_time=0.5)
        r5 = digits("5", x_r - 2 * STEP, 0.16, size=58, color=GOLD)
        self.play(Write(r5), run_time=0.6)

        ans = txt("128 × 4 = 512", size=40, color=GREEN).move_to([0, -1.5, 0])
        self.play(FadeIn(ans, shift=UP * 0.08), run_time=0.7)
        self.finish_section()

    # ---------------- 5. 末尾有 0 ----------------
    def scene_zero(self):
        self.section(5, "末尾有 0：先算再添 0")

        e1 = txt("240 × 3", size=54, color=CHALK).move_to([0, 1.7, 0])
        self.play(Write(e1), run_time=0.8)

        s1 = txt("先算 24 × 3 = 72", size=40, color=GOLD).move_to([0, 0.65, 0])
        self.play(Write(s1), run_time=0.9)

        arr = Arrow([0, 0.15, 0], [0, -0.35, 0], color=GOLD, stroke_width=3, buff=0,
                    max_tip_length_to_length_ratio=0.35)
        self.play(GrowArrow(arr), run_time=0.4)

        base = txt("72", size=60, color=CHALK).move_to([-0.5, -0.95, 0])
        zero = txt("0", size=60, color=GOLD).move_to([0.25, -0.95, 0])
        self.play(Write(base), run_time=0.5)
        self.play(FadeIn(zero, scale=0.6), run_time=0.5)

        circ = Circle(radius=0.42, color=GOLD, stroke_width=3).move_to(zero)
        self.play(Create(circ), run_time=0.5)

        add = txt("添上一个 0", size=28, color=DIM).move_to([2.6, -0.95, 0])
        self.play(FadeIn(add, shift=LEFT * 0.06), run_time=0.5)

        res = txt("240 × 3 = 720", size=52, color=GREEN).move_to([0, -2.15, 0])
        self.play(Write(res), run_time=0.9)
        self.finish_section()

    # ---------------- 6. 三步 ----------------
    def scene_summary(self):
        self.section(6, "竖式三步，记住就不会错")

        chips = VGroup(
            label_box("① 数位对齐", size=30, color=CHALK),
            label_box("② 从个位乘起", size=30, color=CHALK),
            label_box("③ 满几十进几", size=30, color=CHALK),
        ).arrange(DOWN, buff=0.45).move_to([-2.6, 0.35, 0])
        for c in chips:
            self.play(FadeIn(c, shift=RIGHT * 0.1), run_time=0.55)

        big = txt("多位数\n乘一位数", size=44, color=GOLD).move_to([3.4, 0.6, 0])
        self.play(Write(big), run_time=1.0)

        tip = txt("算完回头检查：进位加了吗？", size=28, color=GREEN).move_to([0, -2.35, 0])
        self.play(FadeIn(tip, shift=UP * 0.08), run_time=0.7)
        self.finish_section()

    def construct(self):
        self.scene_story()
        self.clear_stage()
        self.scene_split()
        self.clear_stage()
        self.scene_vertical()
        self.clear_stage()
        self.scene_carry()
        self.clear_stage()
        self.scene_chain()
        self.clear_stage()
        self.scene_zero()
        self.clear_stage()
        self.scene_summary()
        self.clear_stage(0.8)