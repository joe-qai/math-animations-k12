# -*- coding: utf-8 -*-
"""100 以内加减法：36 + 27、63 − 27。一年级下册「加与减」。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


class BaiYineiJiajianScene(NarratedScene):
    lesson = "bai-yinei-jiajian"

    # ---------- 小零件 ----------
    def bundle(self, at) -> VGroup:
        """一捆小棒（十根），用三根粗线加一条束带表示。"""
        g = VGroup()
        for k in range(3):
            g.add(Rectangle(
                width=0.085, height=1.05, stroke_width=0,
                fill_color=BLUE, fill_opacity=0.9,
            ).move_to([(k - 1) * 0.115, 0, 0]))
        g.add(Rectangle(
            width=0.42, height=0.14, stroke_width=0,
            fill_color=GOLD, fill_opacity=0.85,
        ).move_to([0, 0, 0]))
        g.move_to(at)
        return g

    def stick(self, at, h: float = 1.05, color: str = BLUE) -> Rectangle:
        s = Rectangle(width=0.1, height=h, stroke_width=0,
                      fill_color=color, fill_opacity=0.9)
        s.move_to(at)
        return s

    def digits(self, s: str, x_right: float, y: float,
               size: int = 48, color: str = CHALK, pitch: float = 0.64) -> VGroup:
        g = VGroup()
        for k, ch in enumerate(s):
            g.add(txt(ch, size=size, color=color).move_to(
                [x_right - pitch * (len(s) - 1 - k), y, 0]))
        return g

    def construct(self):
        # ================= 0. 生活问题 =================
        self.section(0, "一班 36 个，二班 27 个")

        n1 = txt("36", size=76, color=GOLD).move_to([-3.9, 0.95, 0])
        plus = txt("+", size=64, color=CHALK).move_to([-2.1, 0.95, 0])
        n2 = txt("27", size=76, color=GOLD).move_to([-0.3, 0.95, 0])
        eq = txt("= ?", size=64, color=CHALK).move_to([1.9, 0.95, 0])

        c1 = txt("一班", size=28, color=DIM).move_to([-3.9, -0.15, 0])
        c2 = txt("二班", size=28, color=DIM).move_to([-0.3, -0.15, 0])

        self.play(FadeIn(n1, shift=UP * 0.1), run_time=0.6)
        self.play(FadeIn(c1), run_time=0.4)
        self.play(FadeIn(plus), FadeIn(n2, shift=UP * 0.1), FadeIn(c2), run_time=0.7)
        self.play(FadeIn(eq), run_time=0.5)

        question = txt("两个班一共收集多少个？", size=38, color=CHALK).move_to([0, -1.65, 0])
        self.play(FadeIn(question, shift=UP * 0.1), run_time=0.7)
        self.finish_section()

        # ================= 1. 估算 =================
        self.section(1, "先估一估：大约七十")
        self.play(FadeOut(n1), FadeOut(plus), FadeOut(n2), FadeOut(eq),
                  FadeOut(c1), FadeOut(c2), FadeOut(question), run_time=0.6)

        axis = Line([-6.3, 0.35, 0], [6.3, 0.35, 0], color=DIM, stroke_width=2)

        def tick_x(v: int) -> float:
            return -6.0 + (v - 20) * 0.2

        ticks = VGroup()
        for v in range(20, 81, 10):
            x = tick_x(v)
            ticks.add(Line([x, 0.2, 0], [x, 0.5, 0], color=DIM, stroke_width=2))
            ticks.add(txt(str(v), size=22, color=DIM).move_to([x, -0.1, 0]))
        self.play(Create(axis), LaggedStart(*[FadeIn(t) for t in ticks], lag_ratio=0.03),
                  run_time=1.4)

        d36 = Dot([tick_x(36), 0.35, 0], radius=0.12, color=GOLD)
        l36 = txt("36", size=26, color=GOLD).move_to([tick_x(36) + 0.15, 0.85, 0])
        d27 = Dot([tick_x(27), 0.35, 0], radius=0.12, color=BLUE)
        l27 = txt("27", size=26, color=BLUE).move_to([tick_x(27) - 0.1, 0.85, 0])
        self.play(FadeIn(d36, scale=0.7), FadeIn(l36), run_time=0.5)
        self.play(FadeIn(d27, scale=0.7), FadeIn(l27), run_time=0.5)

        a36 = DashedLine([tick_x(36), 0.35, 0], [tick_x(40), 0.35, 0], color=GOLD, stroke_width=2)
        a27 = DashedLine([tick_x(27), 0.35, 0], [tick_x(30), 0.35, 0], color=BLUE, stroke_width=2)
        self.play(Create(a36), run_time=0.5)
        self.play(Create(a27), run_time=0.5)

        est = txt("40 + 30 = 70", size=44, color=GOLD).move_to([0, 1.75, 0])
        self.play(Write(est), run_time=0.8)

        note1 = txt("两个数都估大了", size=28, color=DIM).move_to([0, -1.35, 0])
        note2 = txt("真正的答案比 70 小一点 → 六十多", size=32, color=GREEN).move_to([0, -2.1, 0])
        self.play(FadeIn(note1), run_time=0.5)
        self.play(FadeIn(note2, shift=UP * 0.1), run_time=0.6)
        self.finish_section()

        # ================= 2. 摆小棒 =================
        self.section(2, "摆小棒：个位满十，捆一捆")
        self.play(FadeOut(axis), FadeOut(ticks), FadeOut(d36), FadeOut(l36),
                  FadeOut(d27), FadeOut(l27), FadeOut(a36), FadeOut(a27),
                  FadeOut(est), FadeOut(note1), FadeOut(note2), run_time=0.6)

        b36 = VGroup(*[self.bundle([-5.55 + k * 0.5, 1.4, 0]) for k in range(3)])
        s36 = VGroup(*[self.stick([-3.7 + k * 0.48, 1.4, 0]) for k in range(6)])
        b27 = VGroup(*[self.bundle([1.35 + k * 0.5, 1.4, 0]) for k in range(2)])
        s27 = VGroup(*[self.stick([2.55 + k * 0.48, 1.4, 0]) for k in range(7)])

        self.play(LaggedStart(*[FadeIn(m, shift=DOWN * 0.15) for m in b36], lag_ratio=0.12),
                  run_time=0.7)
        self.play(LaggedStart(*[FadeIn(m, shift=DOWN * 0.15) for m in s36], lag_ratio=0.08),
                  run_time=0.7)
        self.play(LaggedStart(*[FadeIn(m, shift=DOWN * 0.15) for m in b27], lag_ratio=0.12),
                  run_time=0.6)
        self.play(LaggedStart(*[FadeIn(m, shift=DOWN * 0.15) for m in s27], lag_ratio=0.06),
                  run_time=0.7)

        lab36 = txt("36", size=40, color=GOLD).move_to([-3.4, 0.35, 0])
        lab27 = txt("27", size=40, color=BLUE).move_to([3.35, 0.35, 0])
        self.play(FadeIn(lab36), FadeIn(lab27), run_time=0.5)

        self.play(
            Indicate(s36, color=GOLD, scale_factor=1.12),
            Indicate(s27, color=GOLD, scale_factor=1.12),
            run_time=1.2,
        )
        eq2 = txt("6 + 7 = 13", size=46, color=GOLD).move_to([0, -1.15, 0])
        self.play(Write(eq2), run_time=0.8)

        newb = self.bundle([0.35, 1.4, 0])
        newb.set_color(GREEN)
        self.play(FadeIn(newb, scale=0.7), run_time=0.6)
        note = txt("满十，把 10 根捆成一捆，进到十位", size=30, color=GREEN).move_to([0, -2.15, 0])
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.7)
        self.finish_section()

        # ================= 3. 竖式加法 =================
        self.section(3, "竖式加法：满十进一")
        self.play(FadeOut(b36), FadeOut(s36), FadeOut(b27), FadeOut(s27),
                  FadeOut(lab36), FadeOut(lab27), FadeOut(eq2),
                  FadeOut(newb), FadeOut(note), run_time=0.6)

        t36 = self.digits("36", 1.0, 1.30)
        sgn = txt("+", size=44, color=CHALK).move_to([-0.55, 0.60, 0])
        t27 = self.digits("27", 1.0, 0.60)
        rule = Line([-0.85, 0.02, 0], [1.55, 0.02, 0], color=CHALK, stroke_width=3)

        self.play(Write(t36), run_time=0.6)
        self.play(FadeIn(sgn), Write(t27), run_time=0.7)
        self.play(Create(rule), run_time=0.5)

        h_units = txt("个位：6 + 7 = 13", size=30, color=GOLD).move_to([4.25, 1.25, 0])
        self.play(FadeIn(h_units), run_time=0.5)

        carry = txt("1", size=26, color=ORANGE).move_to([0.36, 2.04, 0])
        r_units = txt("3", size=48, color=CHALK).move_to([1.0, -0.45, 0])
        self.play(FadeIn(carry, shift=DOWN * 0.1), run_time=0.5)
        self.play(Write(r_units), run_time=0.5)

        h_write = txt("写 3，向十位进 1", size=30, color=ORANGE).move_to([3.85, 0.45, 0])
        self.play(FadeIn(h_write), run_time=0.5)

        h_tens = txt("十位：3 + 2 + 1 = 6", size=30, color=GOLD).move_to([4.25, -0.35, 0])
        self.play(FadeIn(h_tens), run_time=0.5)

        r_tens = txt("6", size=48, color=GOLD).move_to([0.36, -0.45, 0])
        self.play(Write(r_tens), run_time=0.5)

        ans = txt("36 + 27 = 63", size=46, color=GOLD).move_to([0.2, -1.85, 0])
        self.play(Write(ans), run_time=0.8)
        self.finish_section()

        # ================= 4. 竖式减法 =================
        self.section(4, "竖式减法：不够减，借一当十")
        self.play(FadeOut(t36), FadeOut(sgn), FadeOut(t27), FadeOut(rule),
                  FadeOut(h_units), FadeOut(h_write), FadeOut(h_tens),
                  FadeOut(carry), FadeOut(r_units), FadeOut(r_tens),
                  FadeOut(ans), run_time=0.65)

        m63 = self.digits("63", 1.0, 1.30)
        msgn = txt("−", size=44, color=CHALK).move_to([-0.55, 0.60, 0])
        m27 = self.digits("27", 1.0, 0.60)
        mrule = Line([-0.85, 0.02, 0], [1.55, 0.02, 0], color=CHALK, stroke_width=3)

        self.play(Write(m63), run_time=0.6)
        self.play(FadeIn(msgn), Write(m27), run_time=0.7)
        self.play(Create(mrule), run_time=0.5)

        box3 = SurroundingRectangle(VGroup(m63[1], m27[1]), color=ORANGE,
                                    buff=0.10, stroke_width=2.5)
        self.play(Create(box3), run_time=0.5)
        warn = txt("3 不够减 7", size=32, color=ORANGE).move_to([4.2, 1.25, 0])
        self.play(FadeIn(warn), run_time=0.5)

        borrow = Arrow([1.45, 1.80, 0], [0.55, 1.80, 0], color=ORANGE,
                       stroke_width=2.5, buff=0, max_tip_length_to_length_ratio=0.22)
        self.play(GrowArrow(borrow), run_time=0.5)

        slash = Line([0.10, 1.58, 0], [0.66, 1.16, 0], color=ORANGE, stroke_width=2.5)
        small5 = txt("5", size=28, color=ORANGE).move_to([0.36, 2.14, 0])
        small13 = txt("13", size=28, color=ORANGE).move_to([1.0, 2.14, 0])
        self.play(Create(slash), run_time=0.4)
        self.play(FadeIn(small5), FadeIn(small13), run_time=0.6)

        tip = txt("向十位借 1，13 − 7 = 6", size=30, color=GOLD).move_to([3.95, 0.35, 0])
        self.play(FadeIn(tip), run_time=0.6)

        m_units = txt("6", size=48, color=CHALK).move_to([1.0, -0.45, 0])
        self.play(Write(m_units), run_time=0.5)

        tip2 = txt("十位剩 5，5 − 2 = 3", size=30, color=GREEN).move_to([3.9, -0.45, 0])
        self.play(FadeIn(tip2), run_time=0.5)

        m_tens = txt("3", size=48, color=GREEN).move_to([0.36, -0.45, 0])
        self.play(Write(m_tens), run_time=0.5)

        res = txt("63 − 27 = 36", size=46, color=GOLD).move_to([0.2, -1.85, 0])
        self.play(FadeOut(box3), FadeOut(borrow), run_time=0.4)
        self.play(Write(res), run_time=0.8)
        self.finish_section()

        # ================= 5. 验算 =================
        self.section(5, "算完要验算")
        self.play(FadeOut(m63), FadeOut(msgn), FadeOut(m27), FadeOut(mrule),
                  FadeOut(warn), FadeOut(slash), FadeOut(small5), FadeOut(small13),
                  FadeOut(tip), FadeOut(tip2), FadeOut(m_units), FadeOut(m_tens),
                  FadeOut(res), run_time=0.65)

        v1 = txt("36 + 27 = 63", size=46, color=CHALK).move_to([-1.0, 1.5, 0])
        ok1 = txt("✓", size=46, color=GREEN).move_to([2.6, 1.5, 0])
        self.play(Write(v1), run_time=0.8)
        self.play(FadeIn(ok1, scale=0.8), run_time=0.4)

        v2 = txt("63 − 27 = 36", size=46, color=CHALK).move_to([-1.0, 0.4, 0])
        ok2 = txt("✓", size=46, color=GREEN).move_to([2.6, 0.4, 0])
        self.play(Write(v2), run_time=0.8)
        self.play(FadeIn(ok2, scale=0.8), run_time=0.4)

        lab = txt("减法用加法验算，加法用减法验算", size=30, color=DIM).move_to([0, -1.0, 0])
        self.play(FadeIn(lab), run_time=0.6)

        est2 = txt("估算：60 − 30 = 30 → 三十多，合理", size=32, color=GOLD).move_to([0, -1.95, 0])
        self.play(FadeIn(est2, shift=UP * 0.1), run_time=0.7)
        self.finish_section()

        # ================= 6. 口诀 =================
        self.section(6, "四句话记住竖式")
        self.play(FadeOut(v1), FadeOut(ok1), FadeOut(v2), FadeOut(ok2),
                  FadeOut(lab), FadeOut(est2), run_time=0.6)

        big = txt("36 + 27 = 63", size=58, color=GOLD).move_to([0, 2.3, 0])
        self.play(Write(big), run_time=0.8)

        c1 = label_box("数位对齐", size=30, color=CHALK).move_to([-3.1, 0.3, 0])
        c2 = label_box("从个位算起", size=30, color=CHALK).move_to([2.7, 0.3, 0])
        c3 = label_box("满十进一", size=30, color=GOLD).move_to([-3.1, -0.9, 0])
        c4 = label_box("不够减借一", size=30, color=ORANGE).move_to([2.7, -0.9, 0])
        self.play(LaggedStart(*[FadeIn(m, shift=UP * 0.1) for m in (c1, c2, c3, c4)],
                             lag_ratio=0.18), run_time=1.2)

        final = txt("会算，更要会检查", size=34, color=GREEN).move_to([0, -2.25, 0])
        self.play(FadeIn(final, shift=UP * 0.1), run_time=0.6)
        self.finish_section()

        self.play(FadeOut(big), FadeOut(c1), FadeOut(c2), FadeOut(c3),
                  FadeOut(c4), FadeOut(final), run_time=0.8)