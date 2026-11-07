# -*- coding: utf-8 -*-
"""分数的意义与性质：单位 1、分数单位、分数与除法、基本性质、约分、通分。五年级下册。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


def frac(num: str, den: str, center, size: int = 50, color: str = CHALK) -> VGroup:
    """竖排分数：分子、分数线、分母。"""
    off = 0.0074 * size
    top = txt(num, size=size, color=color)
    bot = txt(den, size=size, color=color)
    w = max(top.width, bot.width) + 0.3
    line = Line([-w / 2, 0, 0], [w / 2, 0, 0], color=color, stroke_width=3)
    top.move_to([0, off, 0])
    bot.move_to([0, -off, 0])
    return VGroup(top, line, bot).move_to([center[0], center[1], 0])


def cells(n: int, cell: float, center, color: str = CHALK, height_ratio: float = 1.15) -> VGroup:
    """n 等分的条形，返回 n 个可单独上色的格子。"""
    x0 = center[0] - n * cell / 2
    g = VGroup()
    for i in range(n):
        g.add(Rectangle(width=cell, height=cell * height_ratio, color=color, stroke_width=2,
                        fill_color=color, fill_opacity=0.0)
              .move_to([x0 + (i + 0.5) * cell, center[1], 0]))
    return g


def shade(group: VGroup, k: int, color: str, opacity: float = 0.55):
    return [group[i].animate.set_fill(color, opacity=opacity) for i in range(k)]


class FenshuXingzhiScene(NarratedScene):
    lesson = "fenshu-xingzhi"

    def clear_stage(self, run_time: float = 0.5):
        keep = {id(self._track), id(self._fill)}
        junk = [m for m in self.mobjects if id(m) not in keep]
        if junk:
            self.play(*[FadeOut(m) for m in junk], run_time=run_time)
        self.cur_title = None
        self.cur_sub = None

    # ---------------- 0. 分饼 ---------------- 15.6
    def scene_story(self):
        self.section(0, "一张饼，平均分给 4 个人")

        pie = VGroup()
        for i in range(4):
            s = AnnularSector(inner_radius=0, outer_radius=1.5, angle=PI / 2,
                              start_angle=i * PI / 2, color=CHALK, stroke_width=2,
                              fill_color=GOLD, fill_opacity=0.0)
            pie.add(s)
        pie.move_to([-3.6, 0.75, 0])
        self.play(LaggedStart(*[FadeIn(s) for s in pie], lag_ratio=0.12), run_time=1.6)

        for i in range(3):
            self.play(pie[i].animate.set_fill(GOLD, opacity=0.5), run_time=0.35)

        lab = VGroup(
            txt("平均分成 4 份", size=26, color=BLUE),
            txt("拿走 3 份", size=26, color=GOLD),
        ).arrange(DOWN, buff=0.26).move_to([-3.6, -1.6, 0])
        self.play(FadeIn(lab[0], shift=UP * 0.05), run_time=0.7)
        self.play(FadeIn(lab[1], shift=UP * 0.05), run_time=0.7)

        f1 = frac("3", "4", [2.9, 1.15, 0], 54, GOLD)
        f2 = frac("1", "4", [2.9, -0.75, 0], 40, BLUE)
        self.play(FadeIn(f1, shift=RIGHT * 0.07), run_time=0.9)
        self.play(FadeIn(f2, shift=RIGHT * 0.07), run_time=0.8)

        note = txt("把一张纸、一根绳子平均分，也能用分数表示", size=27, color=GREEN)
        note.move_to([0, -2.55, 0])
        self.play(FadeIn(note, shift=UP * 0.06), run_time=0.9)
        self.wait(1.6)
        self.finish_section()

    # ---------------- 1. 意义、分母、分子 ---------------- 14.1
    def scene_def(self):
        self.section(1, "平均分成 5 份，取 2 份")

        g = cells(5, 1.15, [-3.3, 1.0, 0])
        self.play(LaggedStart(*[FadeIn(c) for c in g], lag_ratio=0.12), run_time=1.5)
        self.play(*shade(g, 2, GOLD), run_time=0.9)

        u = txt("单位「1」", size=24, color=DIM).move_to([-3.3, 2.15, 0])
        self.play(FadeIn(u), run_time=0.6)

        fv = frac("2", "5", [0.55, 0.55, 0], 62, GOLD)
        self.play(FadeIn(fv, shift=UP * 0.06), run_time=0.9)

        a1 = Arrow(fv[2].get_bottom() + [0, -0.15, 0], fv[2].get_bottom() + [0.05, -1.15, 0],
                   color=BLUE, stroke_width=2.4, buff=0.02,
                   max_tip_length_to_length_ratio=0.28)
        l1 = txt("分母：平均分成 5 份", size=25, color=BLUE).move_to([2.55, -1.65, 0])
        self.play(GrowArrow(a1), run_time=0.6)
        self.play(FadeIn(l1, shift=RIGHT * 0.05), run_time=0.7)

        a2 = Arrow(fv[0].get_top() + [0, 0.15, 0], fv[0].get_top() + [0.05, 1.15, 0],
                   color=GOLD, stroke_width=2.4, buff=0.02,
                   max_tip_length_to_length_ratio=0.28)
        l2 = txt("分子：取了 2 份", size=25, color=GOLD).move_to([2.55, 2.05, 0])
        self.play(GrowArrow(a2), run_time=0.6)
        self.play(FadeIn(l2, shift=RIGHT * 0.05), run_time=0.7)

        unit = txt("分数单位：五分之一", size=27, color=GREEN).move_to([0, -2.45, 0])
        self.play(FadeIn(unit, shift=UP * 0.06), run_time=0.9)
        self.wait(1.4)
        self.finish_section()

    # ---------------- 2. 分数与除法 ---------------- 15.4
    def scene_div(self):
        self.section(2, "3 个饼分给 4 个人")

        pies = VGroup()
        for i in range(3):
            c = Circle(radius=0.52, color=GOLD, stroke_width=2.5,
                       fill_color=GOLD, fill_opacity=0.3).move_to([-3.3 + i * 1.25, 1.55, 0])
            pies.add(c)
        self.play(LaggedStart(*[FadeIn(p) for p in pies], lag_ratio=0.15), run_time=1.2)

        q = VGroup(
            txt("平均分给 4 个人", size=26, color=BLUE),
            txt("每人分到多少？", size=30, color=CHALK),
        ).arrange(DOWN, buff=0.22).move_to([-2.0, 0.1, 0])
        self.play(FadeIn(q[0], shift=UP * 0.05), run_time=0.7)
        self.play(FadeIn(q[1], shift=UP * 0.05), run_time=0.7)

        expr = VGroup(
            txt("3 ÷ 4", size=48, color=CHALK),
            txt("=", size=48, color=DIM),
            frac("3", "4", [3.35, -1.35, 0], 48, GOLD),
        ).arrange(RIGHT, buff=0.42).move_to([0.35, -1.35, 0])
        self.play(FadeIn(expr[0], shift=UP * 0.05), run_time=0.7)
        self.play(FadeIn(expr[1]), run_time=0.5)
        self.play(FadeIn(expr[2], scale=0.95), run_time=0.8)

        rule = label_box("a ÷ b = b 分之 a（b ≠ 0）", size=27, color=GREEN)
        rule.move_to([0, -2.55, 0])
        self.play(FadeIn(rule, scale=0.97), run_time=0.9)
        self.wait(1.6)
        self.finish_section()

    # ---------------- 3. 基本性质 ---------------- 16.2
    def scene_prop(self):
        self.section(3, "二分之一 = 四分之二 = 八分之四")

        ys = [1.85, 0.35, -1.25]
        sizes = [(2, 1), (4, 2), (8, 4)]
        groups, labels = [], []
        for (n, k), y, cell in zip(sizes, ys, [1.5, 0.75, 0.38]):
            g = cells(n, cell, [-3.9, y, 0])
            groups.append(g)
            self.play(LaggedStart(*[FadeIn(c) for c in g], lag_ratio=0.05), run_time=0.7)
            self.play(*shade(g, k, GOLD), run_time=0.5)
            labels.append(frac(str(k), str(n), [0.3, y, 0], 36, GOLD))
            self.play(FadeIn(labels[-1], shift=RIGHT * 0.05), run_time=0.45)

        mul = VGroup(
            txt("×2", size=24, color=BLUE),
            txt("×2", size=24, color=BLUE),
        ).arrange(DOWN, buff=1.0).move_to([-1.55, 1.1, 0])
        self.play(FadeIn(mul, shift=RIGHT * 0.05), run_time=0.9)

        note = VGroup(
            txt("分子、分母同时乘相同的数", size=26, color=CHALK),
            txt("块数变多，每块变小，涂色部分没变", size=25, color=DIM),
        ).arrange(DOWN, buff=0.24).move_to([2.5, 0.5, 0])
        self.play(FadeIn(note[0], shift=UP * 0.05), run_time=0.8)
        self.play(FadeIn(note[1], shift=UP * 0.05), run_time=0.8)

        rule = txt("分数的分子和分母同时乘或除以相同的数（0 除外），分数的大小不变", size=24, color=GREEN)
        rule.move_to([0, -2.45, 0])
        self.play(FadeIn(rule, shift=UP * 0.05), run_time=0.9)
        self.wait(1.4)
        self.finish_section()

    # ---------------- 4. 约分 ---------------- 15.2
    def scene_reduce(self):
        self.section(4, "十八分之十二，约成三分之二")

        f1 = frac("12", "18", [-3.4, 0.85, 0], 56, CHALK)
        self.play(FadeIn(f1, scale=0.96), run_time=0.8)

        op = txt("同时除以 6", size=28, color=BLUE).move_to([0.15, 0.85, 0])
        self.play(FadeIn(op, shift=RIGHT * 0.05), run_time=0.7)

        f2 = frac("2", "3", [3.35, 0.85, 0], 56, GREEN)
        self.play(FadeIn(f2, scale=0.96), run_time=0.8)

        arrows = VGroup(
            Arrow([-3.0, 1.55, 0], [-0.95, 1.05, 0], color=BLUE, stroke_width=2,
                  buff=0.05, max_tip_length_to_length_ratio=0.2),
            Arrow([-3.0, 0.2, 0], [-0.95, 0.65, 0], color=BLUE, stroke_width=2,
                  buff=0.05, max_tip_length_to_length_ratio=0.2),
        )
        self.play(LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.15), run_time=1.0)

        r1 = txt("12 ÷ 6 = 2，18 ÷ 6 = 3", size=27, color=CHALK).move_to([0, -0.55, 0])
        self.play(FadeIn(r1, shift=UP * 0.05), run_time=0.8)

        r2 = VGroup(
            txt("分子、分母只有公因数 1 的分数，叫最简分数", size=26, color=GOLD),
            txt("计算结果一般都要约成最简分数", size=26, color=GREEN),
        ).arrange(DOWN, buff=0.24).move_to([0, -1.85, 0])
        self.play(FadeIn(r2[0], shift=UP * 0.05), run_time=0.8)
        self.play(FadeIn(r2[1], shift=UP * 0.05), run_time=0.8)
        self.wait(1.8)
        self.finish_section()

    # ---------------- 5. 通分 ---------------- 17.4
    def scene_common(self):
        self.section(5, "分母不同，先通分再比")

        f1 = frac("1", "2", [-4.0, 2.25, 0], 46, GOLD)
        f2 = frac("1", "3", [-0.6, 2.25, 0], 46, BLUE)
        self.play(FadeIn(f1, scale=0.96), FadeIn(f2, scale=0.96), run_time=1.0)

        a1 = Arrow([-4.0, 1.78, 0], [-4.0, 1.02, 0], color=GOLD, stroke_width=2.2,
                   buff=0.02, max_tip_length_to_length_ratio=0.3)
        a2 = Arrow([-0.6, 1.78, 0], [-0.6, 1.02, 0], color=BLUE, stroke_width=2.2,
                   buff=0.02, max_tip_length_to_length_ratio=0.3)
        m1 = txt("×3", size=24, color=GOLD).move_to([-3.05, 1.4, 0])
        m2 = txt("×2", size=24, color=BLUE).move_to([0.35, 1.4, 0])
        self.play(GrowArrow(a1), GrowArrow(a2), run_time=0.9)
        self.play(FadeIn(m1), FadeIn(m2), run_time=0.5)

        g1 = frac("3", "6", [-4.0, 0.35, 0], 46, GOLD)
        g2 = frac("2", "6", [-0.6, 0.35, 0], 46, BLUE)
        self.play(FadeIn(g1, shift=DOWN * 0.05), run_time=0.75)
        self.play(FadeIn(g2, shift=DOWN * 0.05), run_time=0.75)

        res = VGroup(
            txt("六分之三 > 六分之二", size=29, color=GREEN),
            txt("所以 二分之一 > 三分之一", size=29, color=GREEN),
        ).arrange(DOWN, buff=0.26).move_to([4.15, 1.45, 0])
        self.play(FadeIn(res[0], shift=RIGHT * 0.05), run_time=0.8)
        self.play(FadeIn(res[1], shift=RIGHT * 0.05), run_time=0.8)

        note = VGroup(
            txt("6 是 2 和 3 的最小公倍数", size=25, color=CHALK),
            txt("这个相同的分母，叫公分母", size=25, color=GOLD),
        ).arrange(DOWN, buff=0.22).move_to([0, -1.35, 0])
        self.play(FadeIn(note[0], shift=UP * 0.05), run_time=0.7)
        self.play(FadeIn(note[1], shift=UP * 0.05), run_time=0.7)
        self.wait(1.8)
        self.finish_section()

    # ---------------- 6. 易错点 + 三句话 ---------------- 20.3
    def scene_warn(self):
        self.section(6, "三个易错点")

        items = [
            ("随便分也能用分数", "必须是平均分"),
            ("只把分子乘 2", "分母要同时乘"),
            ("约分约一半就停", "要约到最简分数"),
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
            label_box("① 平均分才有分数", size=24, color=GOLD),
            label_box("② 分子分母同乘同除，大小不变", size=24, color=CHALK),
            label_box("③ 约分到最简，通分找最小公倍数", size=24, color=GREEN),
        ).arrange(DOWN, buff=0.2).move_to([0, -1.65, 0])
        for r in rows:
            self.play(FadeIn(r, shift=RIGHT * 0.06), run_time=0.6)
            self.wait(0.5)

        self.wait(1.0)
        self.finish_section()

    def construct(self):
        self.scene_story()
        self.clear_stage()
        self.scene_def()
        self.clear_stage()
        self.scene_div()
        self.clear_stage()
        self.scene_prop()
        self.clear_stage()
        self.scene_reduce()
        self.clear_stage()
        self.scene_common()
        self.clear_stage()
        self.scene_warn()
        self.clear_stage(0.8)