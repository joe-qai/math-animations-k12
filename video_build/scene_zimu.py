# -*- coding: utf-8 -*-
"""用字母表示数：字母代数、定律公式、书写规则、代入求值。四年级下册。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


class ZimuBiaoshiScene(NarratedScene):
    lesson = "zimu-biaoshi"

    def clear_stage(self, run_time: float = 0.5):
        keep = {id(self._track), id(self._fill)}
        junk = [m for m in self.mobjects if id(m) not in keep]
        if junk:
            self.play(*[FadeOut(m) for m in junk], run_time=run_time)
        self.cur_title = None
        self.cur_sub = None

    # ---------------- 0. 边长叫 a ---------------- 16.0
    def scene_story(self):
        self.section(0, "不知道的数，叫它 a")

        # 左：正方形
        sq = Polygon([-5.3, 0.2, 0], [-2.4, 0.2, 0], [-2.4, 2.3, 0], [-5.3, 2.3, 0],
                     color=GOLD, stroke_width=3.2,
                     fill_color=GOLD, fill_opacity=0.12)
        self.play(Create(sq), run_time=1.0)

        a_lab = txt("a", size=36, color=GOLD).move_to([-3.85, -0.18, 0])
        a_tick = Line([-5.3, 0.08, 0], [-2.4, 0.08, 0], color=GOLD, stroke_width=2.0)
        self.play(FadeIn(a_lab), FadeIn(a_tick), run_time=0.7)

        p_lab = txt("周长 = 4a", size=30, color=BLUE).move_to([-3.85, -0.85, 0])
        s_lab = txt("面积 = a²", size=30, color=GREEN).move_to([-3.85, -1.55, 0])
        self.play(FadeIn(p_lab, shift=UP * 0.06), run_time=0.8)
        self.play(FadeIn(s_lab, shift=UP * 0.06), run_time=0.8)

        # 右：年龄关系
        m1 = label_box("小明：n 岁", size=27, color=CHALK).move_to([3.3, 1.75, 0])
        m2 = label_box("妈妈：n + 26 岁", size=27, color=GOLD).move_to([3.3, 0.95, 0])
        self.play(FadeIn(m1, scale=0.96), run_time=0.8)
        self.play(FadeIn(m2, scale=0.96), run_time=0.8)

        rows = VGroup(
            txt("n = 10  →  妈妈 36 岁", size=26, color=DIM),
            txt("n = 12  →  妈妈 38 岁", size=26, color=DIM),
        ).arrange(DOWN, buff=0.26).move_to([3.3, -0.1, 0])
        for r in rows:
            self.play(FadeIn(r, shift=UP * 0.05), run_time=0.7)

        note = txt("数在变，关系不变", size=29, color=GREEN).move_to([0, -2.3, 0])
        self.play(FadeIn(note, shift=UP * 0.07), run_time=0.8)
        self.finish_section()

    # ---------------- 1. 字母表示任何数 ---------------- 17.6
    def scene_any(self):
        self.section(1, "字母可以表示任何数")

        rule = label_box("a 可以是 1、20、0.5 …… 任何数", size=28, color=GOLD)
        rule.move_to([0, 2.35, 0])
        self.play(FadeIn(rule, scale=0.96), run_time=0.9)

        # 年龄轴
        axis = Line([-5.0, 0.95, 0], [5.0, 0.95, 0], color=DIM, stroke_width=2.6)
        self.play(Create(axis), run_time=0.9)

        marks = VGroup()
        for n_val, x in ((8, -4.0), (10, -1.4), (12, 1.2)):
            marks.add(Line([x, 0.82, 0], [x, 1.08, 0], color=DIM, stroke_width=2.0))
            marks.add(txt(f"{n_val} 岁", size=21, color=DIM).move_to([x, 0.46, 0]))
        self.play(LaggedStart(*[FadeIn(m) for m in marks], lag_ratio=0.08), run_time=1.0)

        # 小明年龄点滑动，妈妈年龄跟着变
        dot = Dot([-4.0, 0.95, 0], radius=0.12, color=BLUE)
        n_lab = txt("n = 8", size=30, color=BLUE).move_to([-4.0, 1.55, 0])
        mom = txt("妈妈 = 8 + 26 = 34 岁", size=27, color=GOLD).move_to([-0.4, -0.35, 0])
        self.play(FadeIn(dot), FadeIn(n_lab), run_time=0.7)
        self.play(FadeIn(mom, shift=UP * 0.05), run_time=0.7)

        for x, n in ((-1.4, 10), (1.2, 12)):
            self.play(dot.animate.move_to([x, 0.95, 0]),
                      Transform(n_lab, txt(f"n = {n}", size=30, color=BLUE).move_to([x, 1.55, 0])),
                      run_time=1.0)
            self.play(Transform(mom, txt(f"妈妈 = {n} + 26 = {n + 26} 岁",
                                        size=27, color=GOLD).move_to([-0.4, -0.35, 0])),
                      run_time=0.7)

        n1 = txt("n 每变一次，妈妈的年龄就跟着变一次", size=27, color=CHALK)
        n1.move_to([0, -1.35, 0])
        n2 = txt("但「大 26 岁」这个关系，一直没变", size=27, color=GREEN)
        n2.move_to([0, -2.0, 0])
        self.play(FadeIn(n1, shift=UP * 0.06), run_time=0.8)
        self.play(FadeIn(n2, shift=UP * 0.06), run_time=0.8)
        self.wait(1.0)
        self.finish_section()

    # ---------------- 2. 定律与公式 ---------------- 16.5
    def scene_law(self):
        self.section(2, "用字母写定律、写公式")

        rows = VGroup(
            VGroup(txt("加法交换律", size=26, color=DIM),
                   txt("a + b = b + a", size=34, color=GOLD)),
            VGroup(txt("长方形面积", size=26, color=DIM),
                   txt("S = a × b", size=34, color=BLUE)),
            VGroup(txt("正方形周长", size=26, color=DIM),
                   txt("C = 4a", size=34, color=GREEN)),
        )
        y = 1.85
        for row in rows:
            row[0].move_to([-4.1, y, 0])
            row[1].move_to([1.5, y, 0])
            self.play(FadeIn(row[0], shift=RIGHT * 0.06), run_time=0.55)
            self.play(FadeIn(row[1], shift=RIGHT * 0.06), run_time=0.75)
            y -= 1.05

        note = txt("一条式子，就把一条规律说明白了", size=28, color=CHALK)
        note.move_to([0, -1.5, 0])
        self.play(FadeIn(note, shift=UP * 0.07), run_time=0.9)

        tip = VGroup(
            txt("S 是面积", size=24, color=BLUE),
            txt("C 是周长", size=24, color=GREEN),
            txt("a、b 是边长", size=24, color=GOLD),
        ).arrange(RIGHT, buff=0.8).move_to([0, -2.25, 0])
        self.play(LaggedStart(*[FadeIn(t, shift=UP * 0.05) for t in tip], lag_ratio=0.3),
                  run_time=1.0)
        self.finish_section()

    # ---------------- 3. 书写规则 ---------------- 16.0
    def scene_write(self):
        self.section(3, "四个书写规矩")

        pairs = [
            ("a × b", "ab", "字母乘字母，乘号省略"),
            ("3 × a", "3a", "数字写在字母前面"),
            ("1 × a", "a", "1 乘 a，就写 a"),
            ("a × a", "a²", "两个 a 相乘，写 a 的平方"),
        ]
        y = 1.9
        for left, right, note in pairs:
            l = txt(left, size=32, color=DIM).move_to([-4.7, y, 0])
            arr = Arrow([-3.0, y, 0], [-1.7, y, 0], color=DIM, stroke_width=2.0,
                        buff=0.05, max_tip_length_to_length_ratio=0.2)
            r = txt(right, size=36, color=GOLD).move_to([-0.9, y, 0])
            n = txt(note, size=24, color=CHALK).move_to([2.7, y, 0])
            self.play(FadeIn(l), run_time=0.4)
            self.play(GrowArrow(arr), FadeIn(r, shift=RIGHT * 0.06), run_time=0.7)
            self.play(FadeIn(n, shift=RIGHT * 0.05), run_time=0.5)
            y -= 1.0

        warn = txt("注意：4a 是 4 × a，中间的乘号只是省略了", size=26, color=ORANGE)
        warn.move_to([0, -2.3, 0])
        self.play(FadeIn(warn, shift=UP * 0.07), run_time=0.9)
        self.finish_section()

    # ---------------- 4. 代入求值 ---------------- 15.2
    def scene_value(self):
        self.section(4, "当 a = 5，值是多少")

        cond = label_box("当 a = 5 时", size=30, color=GOLD).move_to([0, 2.3, 0])
        self.play(FadeIn(cond, scale=0.96), run_time=0.8)

        r1 = txt("4a", size=38, color=BLUE).move_to([-4.3, 0.95, 0])
        r1b = txt("= 4 × 5 = 20", size=34, color=CHALK).move_to([1.0, 0.95, 0])
        self.play(FadeIn(r1), run_time=0.6)
        self.play(FadeIn(r1b, shift=RIGHT * 0.06), run_time=0.9)

        hl = SurroundingRectangle(r1, color=GOLD, stroke_width=2.2, buff=0.14)
        self.play(Create(hl), run_time=0.6)
        h_note = txt("省略的乘号，代回时要补上", size=24, color=GOLD)
        h_note.move_to([-2.0, 0.25, 0])
        self.play(FadeIn(h_note, shift=UP * 0.05), run_time=0.7)

        r2 = txt("a²", size=38, color=GREEN).move_to([-4.3, -0.95, 0])
        r2b = txt("= 5 × 5 = 25", size=34, color=CHALK).move_to([1.0, -0.95, 0])
        self.play(FadeIn(r2), run_time=0.6)
        self.play(FadeIn(r2b, shift=RIGHT * 0.06), run_time=0.9)

        note = txt("平方就是两个相同的数相乘，不是乘 2", size=26, color=DIM)
        note.move_to([0, -2.1, 0])
        self.play(FadeIn(note, shift=UP * 0.06), run_time=0.9)
        self.finish_section()

    # ---------------- 5. 三个易错点 ---------------- 15.4
    def scene_warn(self):
        self.section(5, "a² 不是 2a")

        items = [
            ("a² = a × a", "a² = 2a", "两个 a 相乘，不是二 a"),
            ("a + a = 2a", "a + a = a²", "相加才是二 a"),
            ("3a = 3 × a", "3a = 3 + a", "是三乘 a，不是三加 a"),
        ]
        y = 1.75
        for ok_s, bad_s, note in items:
            ok = txt(ok_s, size=32, color=GREEN).move_to([-3.6, y, 0])
            bad = txt(bad_s, size=32, color=RED).move_to([1.25, y, 0])
            cross = Line([-0.15, y - 0.12, 0], [2.65, y + 0.14, 0],
                         color=RED, stroke_width=3)
            n = txt(note, size=21, color=DIM).move_to([4.85, y, 0])
            self.play(FadeIn(ok, shift=RIGHT * 0.05), run_time=0.55)
            self.play(FadeIn(bad, shift=RIGHT * 0.05), run_time=0.55)
            self.play(Create(cross), run_time=0.4)
            self.play(FadeIn(n), run_time=0.4)
            y -= 1.2

        tip = txt("写的时候：数字在前，字母在后，乘号省略", size=26, color=GOLD)
        tip.move_to([0, -2.3, 0])
        self.play(FadeIn(tip, shift=UP * 0.07), run_time=0.9)
        self.finish_section()

    # ---------------- 6. 总结 ---------------- 14.3
    def scene_summary(self):
        self.section(6, "三句话")

        rows = VGroup(
            label_box("① 字母能表示任何数", size=28, color=GOLD),
            label_box("② 数写在字母前，乘号可省略：3a", size=28, color=CHALK),
            label_box("③ a² 就是 a × a", size=28, color=GREEN),
        ).arrange(DOWN, buff=0.34).move_to([0, 1.3, 0])
        for r in rows:
            self.play(FadeIn(r, shift=RIGHT * 0.07), run_time=0.7)
            self.wait(0.5)

        demo = txt("a = 5  →  3a = 15   a² = 25", size=30, color=BLUE)
        demo.move_to([0, -1.35, 0])
        self.play(FadeIn(demo, shift=UP * 0.06), run_time=0.9)

        end = txt("用字母，就是把关系写下来", size=29, color=GOLD)
        end.move_to([0, -2.2, 0])
        self.play(FadeIn(end, shift=UP * 0.06), run_time=0.8)
        self.wait(1.0)
        self.finish_section()

    def construct(self):
        self.scene_story()
        self.clear_stage()
        self.scene_any()
        self.clear_stage()
        self.scene_law()
        self.clear_stage()
        self.scene_write()
        self.clear_stage()
        self.scene_value()
        self.clear_stage()
        self.scene_warn()
        self.clear_stage()
        self.scene_summary()
        self.clear_stage(0.8)