# -*- coding: utf-8 -*-
"""长方体的体积：小正方体摆一摆、长×宽×高、正方体、体积单位与进率。五年级下册。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


def box(x0, y0, w, h, dx, dy, color=CHALK, fill=0.12, sw=3.0):
    """斜二测长方体：正面 + 顶面 + 右侧面。"""
    front = Polygon(
        [x0, y0, 0], [x0 + w, y0, 0], [x0 + w, y0 + h, 0], [x0, y0 + h, 0],
        color=color, stroke_width=sw, fill_color=color, fill_opacity=fill,
    )
    top = Polygon(
        [x0, y0 + h, 0], [x0 + w, y0 + h, 0],
        [x0 + w + dx, y0 + h + dy, 0], [x0 + dx, y0 + h + dy, 0],
        color=color, stroke_width=sw, fill_color=color, fill_opacity=fill * 1.3,
    )
    side = Polygon(
        [x0 + w, y0, 0], [x0 + w + dx, y0 + dy, 0],
        [x0 + w + dx, y0 + h + dy, 0], [x0 + w, y0 + h, 0],
        color=color, stroke_width=sw, fill_color=color, fill_opacity=fill * 0.8,
    )
    return VGroup(front, top, side)


def cube3d(x0, y0, s, ox, oy, color=BLUE, fill=0.10):
    """小正方体：正面正方形 + 顶面 + 右侧面。"""
    front = Polygon(
        [x0, y0, 0], [x0 + s, y0, 0], [x0 + s, y0 + s, 0], [x0, y0 + s, 0],
        color=color, stroke_width=1.3, fill_color=color, fill_opacity=fill,
    )
    top = Polygon(
        [x0, y0 + s, 0], [x0 + s, y0 + s, 0],
        [x0 + s + ox, y0 + s + oy, 0], [x0 + ox, y0 + s + oy, 0],
        color=color, stroke_width=1.3, fill_color=color, fill_opacity=fill * 1.4,
    )
    side = Polygon(
        [x0 + s, y0, 0], [x0 + s + ox, y0 + oy, 0],
        [x0 + s + ox, y0 + s + oy, 0], [x0 + s, y0 + s, 0],
        color=color, stroke_width=1.3, fill_color=color, fill_opacity=fill * 0.8,
    )
    return VGroup(front, top, side)


class ChangfangtiTijiScene(NarratedScene):
    lesson = "changfangti-tiji"

    def clear_stage(self, run_time: float = 0.5):
        keep = {id(self._track), id(self._fill)}
        junk = [m for m in self.mobjects if id(m) not in keep]
        if junk:
            self.play(*[FadeOut(m) for m in junk], run_time=run_time)
        self.cur_title = None
        self.cur_sub = None

    # ---------------- 0. 长方体纸箱 ---------------- 17.5
    def scene_story(self):
        self.section(0, "长方体纸箱，能装多少")

        x0, y0, w, h, dx, dy = -4.9, -1.6, 3.0, 1.85, 0.95, 0.70
        bx = box(x0, y0, w, h, dx, dy, GOLD, 0.16)
        self.play(Create(bx), run_time=1.6)

        lb = Brace(Line([x0, y0, 0], [x0 + w, y0, 0]), DOWN, buff=0.14, color=GOLD)
        ll = txt("长 5 分米", size=25, color=GOLD).next_to(lb, DOWN, buff=0.1)
        self.play(Create(lb), FadeIn(ll), run_time=0.9)

        lh = Brace(Line([x0, y0, 0], [x0, y0 + h, 0]), LEFT, buff=0.14, color=BLUE)
        lht = txt("高 3 分米", size=25, color=BLUE).next_to(lh, LEFT, buff=0.1)
        self.play(Create(lh), FadeIn(lht), run_time=0.9)

        depth = Line([x0 + w, y0 + h, 0], [x0 + w + dx, y0 + h + dy, 0],
                     color=GREEN, stroke_width=2.6)
        lead = Line([x0 + w + dx, y0 + h + dy, 0], [-0.45, 1.15, 0],
                    color=GREEN, stroke_width=1.6)
        ld = txt("宽 4 分米", size=24, color=GREEN).move_to([-0.15, 1.35, 0])
        self.play(Create(depth), run_time=0.6)
        self.play(Create(lead), FadeIn(ld, shift=UP * 0.05), run_time=0.8)

        qs = VGroup(
            txt("这个箱子能装多少东西？", size=28, color=CHALK),
            txt("体积：物体占空间的大小", size=27, color=GOLD),
            txt("它的体积是多少？", size=28, color=GREEN),
        ).arrange(DOWN, buff=0.34).move_to([3.6, 0.9, 0])
        for q in qs:
            self.play(FadeIn(q, shift=UP * 0.05), run_time=0.7)

        tip = txt("先要知道体积怎么算", size=26, color=DIM).move_to([3.6, -0.95, 0])
        self.play(FadeIn(tip, shift=UP * 0.05), run_time=0.8)
        self.wait(2.0)
        self.finish_section()

    # ---------------- 1. 小正方体摆一摆 ---------------- 17.6
    def scene_fill(self):
        self.section(1, "用 1 立方厘米的小正方体摆")

        s, ox, oy = 0.60, 0.40, 0.29
        x0, y0 = -5.4, -2.05

        layers = []
        for k in range(3):
            lay = VGroup()
            for j in range(4):
                for i in range(5):
                    lay.add(cube3d(x0 + i * s + j * ox, y0 + k * s + j * oy,
                                   s, ox, oy, BLUE, 0.10))
            layers.append(lay)

        self.play(LaggedStart(*[Create(c) for c in layers[0]], lag_ratio=0.04),
                  run_time=2.2)
        self.play(LaggedStart(*[Create(c) for c in layers[1]], lag_ratio=0.04),
                  run_time=2.0)
        self.play(LaggedStart(*[Create(c) for c in layers[2]], lag_ratio=0.04),
                  run_time=2.0)

        rows = [
            ("长 5 厘米：一排 5 个", GOLD),
            ("宽 4 厘米：一层 4 排", BLUE),
            ("高 3 厘米：一共 3 层", GREEN),
        ]
        y = 2.0
        for t, c in rows:
            self.play(FadeIn(txt(t, size=26, color=c).move_to([3.7, y, 0]),
                             shift=RIGHT * 0.05), run_time=0.7)
            y -= 0.78

        cnt = VGroup(
            txt("一层：5 × 4 = 20 个", size=27, color=BLUE),
            txt("三层：20 × 3 = 60 个", size=27, color=GREEN),
            txt("体积 = 60 立方厘米", size=28, color=GOLD),
        ).arrange(DOWN, buff=0.26, aligned_edge=LEFT).move_to([3.4, -1.25, 0])
        for c in cnt:
            self.play(FadeIn(c, shift=RIGHT * 0.05), run_time=0.65)
            self.wait(0.2)
        self.wait(1.6)
        self.finish_section()

    # ---------------- 2. 长 × 宽 × 高 ---------------- 15.6
    def scene_formula(self):
        self.section(2, "长方体的体积公式")

        bx = box(-5.3, -1.75, 2.7, 1.7, 0.85, 0.62, CHALK, 0.10)
        self.play(Create(bx), run_time=1.2)

        e1 = txt("长 5", size=30, color=GOLD).move_to([-3.95, -2.15, 0])
        e3 = txt("高 3", size=30, color=GREEN).move_to([-6.05, -0.95, 0])
        lead = Line([-1.75, 0.57, 0], [-1.15, 0.92, 0], color=BLUE, stroke_width=1.6)
        e2 = txt("宽 4", size=30, color=BLUE).move_to([-0.45, 1.02, 0])
        self.play(FadeIn(e1), FadeIn(e3), run_time=0.9)
        self.play(Create(lead), FadeIn(e2, shift=UP * 0.04), run_time=0.8)

        steps = VGroup(
            txt("5 × 4 = 20", size=34, color=BLUE),
            txt("20 × 3 = 60", size=34, color=GREEN),
        ).arrange(DOWN, buff=0.34, aligned_edge=LEFT).move_to([2.1, 1.45, 0])
        for st in steps:
            self.play(FadeIn(st, shift=RIGHT * 0.05), run_time=0.8)

        frm = txt("体积 = 长 × 宽 × 高", size=34, color=GOLD).move_to([2.3, 0.05, 0])
        self.play(FadeIn(frm, shift=UP * 0.05), run_time=0.9)

        let = label_box("V = a × b × h", size=42, color=GREEN)
        let.move_to([2.3, -1.15, 0])
        self.play(FadeIn(let, scale=0.97), run_time=0.9)

        note = txt("a、b、h 分别是长、宽、高", size=25, color=DIM).move_to([2.3, -2.1, 0])
        self.play(FadeIn(note, shift=UP * 0.05), run_time=0.8)
        self.wait(2.0)
        self.finish_section()

    # ---------------- 3. 正方体 ---------------- 18.5
    def scene_cube(self):
        self.section(3, "正方体：棱长乘棱长乘棱长")

        bx = box(-4.9, -1.35, 2.05, 2.05, 0.75, 0.55, GOLD, 0.14)
        self.play(Create(bx), run_time=1.4)

        l1 = txt("棱长 3 厘米", size=26, color=GOLD).move_to([-3.9, -1.9, 0])
        l2 = txt("棱长 3", size=26, color=BLUE).move_to([-1.35, 1.05, 0])
        l3 = txt("棱长 3", size=26, color=GREEN).move_to([-6.0, -0.2, 0])
        self.play(FadeIn(l1), FadeIn(l2), FadeIn(l3), run_time=0.9)

        say = txt("正方体是长、宽、高都相等的长方体", size=27, color=CHALK)
        say.move_to([2.4, 2.0, 0])
        self.play(FadeIn(say, shift=UP * 0.05), run_time=0.9)

        eq = VGroup(
            txt("V = 3 × 3 × 3", size=36, color=CHALK),
            txt("= 27（立方厘米）", size=34, color=GREEN),
        ).arrange(DOWN, buff=0.3).move_to([2.3, 0.75, 0])
        for e in eq:
            self.play(FadeIn(e, shift=UP * 0.05), run_time=0.8)

        let = label_box("V = a × a × a", size=40, color=GOLD)
        let.move_to([2.3, -0.75, 0])
        self.play(FadeIn(let, scale=0.97), run_time=0.9)

        note = txt("也叫棱长的立方，记作 a³", size=26, color=DIM).move_to([2.3, -1.85, 0])
        self.play(FadeIn(note, shift=UP * 0.05), run_time=0.8)
        self.wait(2.2)
        self.finish_section()

    # ---------------- 4. 例题：纸箱 ---------------- 14.6
    def scene_example(self):
        self.section(4, "纸箱的体积是多少")

        prob = txt("长 5 分米，宽 4 分米，高 3 分米", size=29, color=CHALK)
        prob.move_to([0, 2.1, 0])
        self.play(FadeIn(prob, shift=UP * 0.05), run_time=0.9)

        rows = [
            ("V = 5 × 4 × 3", CHALK),
            ("= 20 × 3", BLUE),
            ("= 60（立方分米）", GREEN),
        ]
        y = 0.95
        for s_, c in rows:
            self.play(FadeIn(txt(s_, size=36, color=c).move_to([-1.1, y, 0]),
                             shift=UP * 0.04), run_time=0.8)
            y -= 0.82

        ans = txt("这个纸箱的体积是 60 立方分米", size=28, color=GOLD).move_to([0, -1.55, 0])
        self.play(FadeIn(ans, shift=UP * 0.05), run_time=0.9)

        tip = txt("三个长度单位要统一，都用分米", size=26, color=RED).move_to([0, -2.35, 0])
        self.play(FadeIn(tip, shift=UP * 0.05), run_time=0.8)
        self.wait(2.0)
        self.finish_section()

    # ---------------- 5. 体积单位与进率 ---------------- 20.3
    def scene_units(self):
        self.section(5, "体积单位与进率")

        bx = box(-5.4, -0.85, 1.35, 1.35, 0.5, 0.38, GOLD, 0.16)
        self.play(Create(bx), run_time=1.2)
        lab = txt("棱长 1 分米", size=24, color=GOLD).move_to([-4.7, -1.35, 0])
        self.play(FadeIn(lab), run_time=0.7)

        rows = VGroup(
            txt("1 立方分米 = 1000 立方厘米", size=30, color=GREEN),
            txt("因为 10 × 10 × 10 = 1000", size=26, color=DIM),
            txt("1 升 = 1 立方分米", size=28, color=BLUE),
            txt("1 毫升 = 1 立方厘米", size=28, color=BLUE),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT).move_to([1.9, 1.15, 0])
        for r in rows:
            self.play(FadeIn(r, shift=RIGHT * 0.05), run_time=0.7)
            self.wait(0.2)

        n1 = txt("体积单位：立方厘米、立方分米、立方米", size=26, color=CHALK)
        n1.move_to([1.2, -1.55, 0])
        n2 = txt("容积单位：升、毫升", size=26, color=GOLD).move_to([1.2, -2.2, 0])
        self.play(FadeIn(n1, shift=UP * 0.05), run_time=0.8)
        self.play(FadeIn(n2, shift=UP * 0.05), run_time=0.8)
        self.wait(2.6)
        self.finish_section()

    # ---------------- 6. 易错点 + 三句话 ---------------- 18.0
    def scene_warn(self):
        self.section(6, "三个易错点")

        items = [
            ("单位不统一就相乘", "先统一单位再算"),
            ("体积用面积单位", "体积要带立方"),
            ("算容积从外面量", "容积从里面量"),
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
            label_box("① 摆小正方体，数出个数", size=24, color=GOLD),
            label_box("② 体积 = 长 × 宽 × 高", size=24, color=CHALK),
            label_box("③ 单位先统一，体积带立方", size=24, color=GREEN),
        ).arrange(DOWN, buff=0.2).move_to([0, -1.65, 0])
        for r in rows:
            self.play(FadeIn(r, shift=RIGHT * 0.06), run_time=0.6)
            self.wait(0.55)

        self.wait(1.0)
        self.finish_section()

    def construct(self):
        self.scene_story()
        self.clear_stage()
        self.scene_fill()
        self.clear_stage()
        self.scene_formula()
        self.clear_stage()
        self.scene_cube()
        self.clear_stage()
        self.scene_example()
        self.clear_stage()
        self.scene_units()
        self.clear_stage()
        self.scene_warn()
        self.clear_stage(0.8)