# -*- coding: utf-8 -*-
"""连加连减与混合运算：同级从左到右，有括号先算括号。二年级上册。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403

X0 = -5.4
BIG = 54


def line(s, y, size=BIG, color=CHALK, indent=0.0):
    t = txt(s, size=size, color=color)
    t.move_to([X0 + indent, y, 0], aligned_edge=LEFT)
    return t


def underline_under(t, frac_from=0.0, frac_to=1.0, color=GOLD, width=4.0):
    """在文本下方画一条线，按宽度比例截取。"""
    left = t.get_left()[0] + t.width * frac_from
    right = t.get_left()[0] + t.width * frac_to
    y = t.get_bottom()[1] - 0.14
    return Line([left, y, 0], [right, y, 0], color=color, stroke_width=width)


class HunheScene(NarratedScene):
    lesson = "lianjia-lianjian"

    def clear_stage(self, run_time: float = 0.5):
        keep = {id(self._track), id(self._fill)}
        junk = [m for m in self.mobjects if id(m) not in keep]
        if junk:
            self.play(*[FadeOut(m) for m in junk], run_time=run_time)
        self.cur_title = None
        self.cur_sub = None

    # ---------------- 0. 卡片情境 ----------------
    def scene_story(self):
        self.section(0, "先看一个真实的问题")

        cards = []
        data = [("28", "原有", GOLD), ("15", "妈妈给的", BLUE), ("9", "生日收到", GREEN)]
        for i, (num, lab, color) in enumerate(data):
            box = RoundedRectangle(corner_radius=0.16, width=1.5, height=1.5,
                                   stroke_color=color, stroke_width=2.6,
                                   fill_color=color, fill_opacity=0.1)
            box.move_to([-3.9 + i * 3.9, 0.7, 0])
            n = txt(num, size=52, color=color).move_to(box)
            l = txt(lab, size=26, color=DIM).move_to([box.get_x(), -0.55, 0])
            cards.append(VGroup(box, n, l))

        for c in cards:
            self.play(FadeIn(c, shift=UP * 0.1), run_time=0.55)

        q = txt("一共多少张？", size=38, color=CHALK).move_to([0, -1.55, 0])
        expr = txt("28 + 15 + 9 = ?", size=52, color=GOLD).move_to([0, -2.55, 0])
        self.play(FadeIn(q, shift=UP * 0.08), run_time=0.6)
        self.play(Write(expr), run_time=1.0)
        self.finish_section()

    # ---------------- 1. 连加：从左往右 ----------------
    def scene_add(self):
        self.section(1, "连加：先算前两个")

        eq1 = txt("28 + 15 = 43", size=60, color=CHALK).move_to([0, 1.55, 0])
        self.play(Write(eq1), run_time=1.2)
        ul = underline_under(eq1, 0.0, 0.42, color=GOLD, width=5)
        self.play(Create(ul), run_time=0.5)

        note1 = txt("先算 28 + 15", size=26, color=GOLD).move_to([4.1, 1.55, 0])
        self.play(FadeIn(note1), run_time=0.4)

        eq2 = txt("43 + 9 = 52", size=60, color=CHALK).move_to([0, -0.45, 0])
        arr = Arrow([0, 0.85, 0], [0, 0.05, 0], color=GOLD, stroke_width=3, buff=0,
                    max_tip_length_to_length_ratio=0.3)
        self.play(GrowArrow(arr), run_time=0.4)
        self.play(Write(eq2), run_time=1.0)

        res = label_box("一共 52 张", size=34, color=GREEN).move_to([0, -1.85, 0])
        note2 = txt("再加第三个", size=26, color=BLUE).move_to([4.1, -0.45, 0])
        self.play(FadeIn(note2), run_time=0.4)
        self.play(FadeIn(res, shift=UP * 0.08), run_time=0.7)
        self.play(Indicate(eq2, color=GOLD, scale_factor=1.03), run_time=0.7)
        self.finish_section()

    # ---------------- 2. 递等式 ----------------
    def scene_vertical(self):
        self.section(2, "把过程写成递等式")

        head = txt("28 + 15 + 9", size=52, color=CHALK)
        indent = txt("= ", size=52, color=GOLD).width
        head.move_to([X0 + indent, 1.55, 0], aligned_edge=LEFT)
        self.play(Write(head), run_time=1.1)

        l2 = line("= 43 + 9", 0.45)
        l3 = line("= 52", -0.65)

        self.play(Write(l2), run_time=0.9)
        s1 = txt("第一步", size=24, color=DIM).move_to([l2.get_right()[0] + 0.9, 0.45, 0])
        self.play(FadeIn(s1), run_time=0.4)
        self.play(Create(underline_under(l2, 0.0, 0.30, color=BLUE, width=3)), run_time=0.4)
        self.play(Write(l3), run_time=0.8)
        s2 = txt("第二步", size=24, color=DIM).move_to([l3.get_right()[0] + 0.9, -0.65, 0])
        self.play(FadeIn(s2), run_time=0.4)

        # 等号对齐提示
        eq_x = X0 + txt("=", size=52, color=GOLD).width / 2
        guide = DashedLine([eq_x, 1.92, 0], [eq_x, -0.25, 0], color=GOLD,
                           stroke_width=2, stroke_opacity=0.55)
        self.play(Create(guide), run_time=0.7)

        tip = txt("每行只算一步，等号上下对齐", size=28, color=GREEN).move_to([1.2, -1.85, 0])
        self.play(FadeIn(tip, shift=UP * 0.08), run_time=0.7)
        self.finish_section()

    # ---------------- 3. 连减 ----------------
    def scene_sub(self):
        self.section(3, "连减：还是一步一步算")

        q = txt("52 张，送出 12 张，又用掉 8 张", size=30, color=DIM).move_to([0, 2.4, 0])
        self.play(FadeIn(q, shift=DOWN * 0.06), run_time=0.5)

        indent = txt("= ", size=52, color=GOLD).width
        l1 = line("52 - 12 - 8", 1.5, indent=indent)
        self.play(Write(l1), run_time=1.0)
        self.play(Create(underline_under(l1, 0.0, 0.60, color=GOLD, width=4)), run_time=0.4)

        l2 = line("= 40 - 8", 0.4)
        l3 = line("= 32", -0.7)
        self.play(Write(l2), run_time=0.8)
        self.play(Write(l3), run_time=0.7)

        res = label_box("还剩 32 张", size=34, color=GREEN).move_to([2.1, -1.85, 0])
        self.play(FadeIn(res, shift=UP * 0.08), run_time=0.7)
        self.play(Indicate(l3, color=GOLD, scale_factor=1.04), run_time=0.7)
        self.finish_section()

    # ---------------- 4. 加减混合 ----------------
    def scene_mix(self):
        self.section(4, "加减混合：谁在前先算谁")

        indent = txt("= ", size=52, color=GOLD).width
        l1 = line("45 - 20 + 12", 1.6, indent=indent)
        l2 = line("= 25 + 12", 0.5)
        l3 = line("= 37", -0.6)
        self.play(Write(l1), run_time=1.0)

        self.play(Create(underline_under(l1, 0.0, 0.40, color=GOLD, width=4)), run_time=0.4)
        self.play(Write(l2), run_time=0.8)
        self.play(Create(underline_under(l2, 0.0, 0.42, color=BLUE, width=3)), run_time=0.4)
        self.play(Write(l3), run_time=0.7)

        note = txt("减号在前面，就先减", size=28, color=GREEN).move_to([1.6, -1.75, 0])
        self.play(FadeIn(note, shift=UP * 0.08), run_time=0.6)
        self.finish_section()

    # ---------------- 5. 括号 ----------------
    def scene_paren(self):
        self.section(5, "有括号：先算括号里的")

        indent = txt("= ", size=52, color=GOLD).width
        l1 = line("45 - (20 + 12)", 1.6, indent=indent)
        self.play(Write(l1), run_time=1.0)

        box = RoundedRectangle(corner_radius=0.1, width=txt("(20 + 12)", size=52).width + 0.8,
                               height=0.95, stroke_color=GOLD, stroke_width=2.4,
                               fill_color=GOLD, fill_opacity=0.06)
        box.move_to([l1.get_right()[0] - box.width / 2 + 0.1, l1.get_center()[1], 0])
        self.play(Create(box), run_time=0.6)

        l2 = line("= 45 - 32", 0.35)
        l3 = line("= 13", -0.85)
        self.play(Write(l2), run_time=0.8)
        self.play(Write(l3), run_time=0.7)

        note = txt("先算 20 + 12 = 32", size=28, color=GREEN).move_to([1.6, -1.9, 0])
        self.play(FadeIn(note, shift=UP * 0.08), run_time=0.6)

        cmp_t = txt("没有括号得 37，有括号得 13：顺序不同，结果不同", size=25, color=DIM)
        cmp_t.move_to([0, -2.55, 0])
        self.play(FadeIn(cmp_t, shift=UP * 0.08), run_time=0.7)
        self.finish_section()

    # ---------------- 6. 两条规则 ----------------
    def scene_rules(self):
        self.section(6, "两条规则，记住就不会错")

        r1 = label_box("① 同级运算：从左到右", size=34, color=GOLD).move_to([-3.2, 1.55, 0])
        r2 = label_box("② 有括号：先算括号", size=34, color=GREEN).move_to([3.2, 1.55, 0])
        self.play(FadeIn(r1, shift=UP * 0.08), run_time=0.6)
        self.play(FadeIn(r2, shift=UP * 0.08), run_time=0.6)

        e1 = txt("例：28 + 15 + 9", size=24, color=DIM).move_to([-3.2, 0.85, 0])
        e2 = txt("例：45 - (20 + 12)", size=24, color=DIM).move_to([3.2, 0.85, 0])
        self.play(FadeIn(e1), FadeIn(e2), run_time=0.6)

        ex = txt("25 - 10 + 5", size=48, color=CHALK).move_to([0, 0.05, 0])
        good = txt("= 20", size=48, color=GREEN).move_to([0, -0.95, 0])
        self.play(Write(ex), run_time=0.9)
        self.play(Write(good), run_time=0.6)

        bad = txt("先算 10 + 5 = 15，得 10", size=26, color=RED).move_to([0, -1.95, 0])
        cross = Cross(scale_factor=0.35, stroke_color=RED, stroke_width=5).move_to([0.1, -1.95, 0])
        self.play(FadeIn(bad), run_time=0.5)
        self.play(Create(cross), run_time=0.4)
        self.finish_section()

    def construct(self):
        self.scene_story()
        self.clear_stage()
        self.scene_add()
        self.clear_stage()
        self.scene_vertical()
        self.clear_stage()
        self.scene_sub()
        self.clear_stage()
        self.scene_mix()
        self.clear_stage()
        self.scene_paren()
        self.clear_stage()
        self.scene_rules()
        self.clear_stage(0.8)