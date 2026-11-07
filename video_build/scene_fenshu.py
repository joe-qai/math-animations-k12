# -*- coding: utf-8 -*-
"""分数的初步认识：平均分、几分之一、几分之几、分数单位、比大小。三年级上册。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


def frac(num: str, den: str, center, size: int = 54, color: str = CHALK) -> VGroup:
    """竖排分数：分子在上，分数线居中，分母在下。"""
    off = 0.0074 * size
    cx, cy = center[0], center[1]
    top = txt(num, size=size, color=color)
    bot = txt(den, size=size, color=color)
    w = max(top.width, bot.width) + 0.34
    line = Line([-w / 2, 0, 0], [w / 2, 0, 0], color=color, stroke_width=3)
    top.move_to([0, off, 0])
    bot.move_to([0, -off, 0])
    return VGroup(top, line, bot).move_to([cx, cy, 0])


def square_cells(cols: int, rows: int, unit: float, center) -> VGroup:
    """平均分成 cols×rows 格的方形，每格一个可单独上色的矩形。"""
    cx, cy = center[0], center[1]
    w, h = cols * unit, rows * unit
    x0, y0 = cx - w / 2, cy - h / 2
    g = VGroup()
    for r in range(rows):
        for c in range(cols):
            g.add(Rectangle(width=unit, height=unit, color=CHALK, stroke_width=2,
                            fill_color=CHALK, fill_opacity=0.0)
                  .move_to([x0 + (c + 0.5) * unit, y0 + (r + 0.5) * unit, 0]))
    return g


def arc_piece(center, r: float, a0_deg: float, a1_deg: float,
              color: str, opacity: float = 0.26) -> Polygon:
    """由一段圆弧和它的弦围成的弓形（用于表现「一块饼」的一部分）。"""
    pts = []
    for t in np.linspace(a0_deg, a1_deg, 64):
        a = t * DEGREES
        pts.append(np.array([center[0] + r * np.cos(a), center[1] + r * np.sin(a), 0]))
    return Polygon(*pts, color=color, fill_color=color, fill_opacity=opacity,
                   stroke_width=2)


def bar(n: int, cell: float, center, color: str = CHALK) -> VGroup:
    """n 等分的条形，返回 n 个可单独上色的格子。"""
    cx, cy = center[0], center[1]
    x0 = cx - n * cell / 2
    g = VGroup()
    for i in range(n):
        g.add(Rectangle(width=cell, height=cell * 1.15, color=color, stroke_width=2,
                        fill_color=color, fill_opacity=0.0)
              .move_to([x0 + (i + 0.5) * cell, cy, 0]))
    return g


class FenshuChubuScene(NarratedScene):
    lesson = "fenshu-chubu"

    def clear_stage(self, run_time: float = 0.5):
        keep = {id(self._track), id(self._fill)}
        junk = [m for m in self.mobjects if id(m) not in keep]
        if junk:
            self.play(*[FadeOut(m) for m in junk], run_time=run_time)
        self.cur_title = None
        self.cur_sub = None

    # ---------------- 0. 一块月饼 ---------------- 一块月饼，两个人分
    def scene_story(self):
        self.section(0, "一块月饼，两人分")

        c = [-3.5, 0.4, 0]
        plate = Circle(radius=1.35, color=CHALK, stroke_width=2.6,
                       fill_color=GOLD, fill_opacity=0.14).move_to(c)
        self.play(Create(plate), run_time=1.0)

        lab = txt("1 块", size=28, color=GOLD).move_to([-3.5, 0.4, 0])
        self.play(FadeIn(lab), run_time=0.5)

        cut = Line([-3.5, 1.75, 0], [-3.5, -0.95, 0], color=CHALK, stroke_width=2.4)
        self.play(Create(cut), run_time=0.7)

        h1 = txt("一块月饼", size=30, color=CHALK).move_to([2.9, 1.5, 0])
        h2 = txt("2 人平均分", size=30, color=CHALK).move_to([2.9, 0.7, 0])
        q = txt("每人多少？", size=34, color=GOLD).move_to([2.9, -0.2, 0])
        self.play(FadeIn(h1, shift=UP * 0.06), run_time=0.6)
        self.play(FadeIn(h2, shift=UP * 0.06), run_time=0.6)
        self.play(FadeIn(q, shift=UP * 0.06), run_time=0.6)

        half = VGroup(
            txt("半个", size=30, color=BLUE),
            txt("=", size=30, color=DIM),
            frac("1", "2", [0, 0, 0], size=40, color=BLUE),
        ).arrange(RIGHT, buff=0.35).move_to([2.9, -1.5, 0])
        self.play(FadeIn(half, shift=UP * 0.08), run_time=1.0)
        self.finish_section()

    # ---------------- 1. 必须平均分 ----------------
    def scene_average(self):
        self.section(1, "必须平均分")

        # 左：平均分成两半
        c1 = [-3.7, 0.55, 0]
        r = 1.15
        ring1 = Circle(radius=r, color=CHALK, stroke_width=2.6).move_to(c1)
        left1 = arc_piece(c1, r, 90, 270, GOLD, 0.28)
        right1 = arc_piece(c1, r, 270, 450, BLUE, 0.24)
        self.play(Create(ring1), run_time=0.8)
        self.play(FadeIn(left1), FadeIn(right1), run_time=0.9)

        t1 = txt("✓ 平均分", size=28, color=GREEN).move_to([-3.7, -1.15, 0])
        f1 = frac("1", "2", [-5.45, 0.55], size=34, color=GOLD)
        f2 = frac("1", "2", [-1.95, 0.55], size=34, color=BLUE)
        self.play(Create(t1), FadeIn(f1), FadeIn(f2), run_time=0.7)

        # 右：一大一小（刀口不在正中间）
        c2 = [3.2, 0.55, 0]
        ring2 = Circle(radius=r, color=CHALK, stroke_width=2.6).move_to(c2)
        dx = 0.42
        dy = float(np.sqrt(r * r - dx * dx))
        cut2 = Line([c2[0] + dx, c2[1] + dy, 0], [c2[0] + dx, c2[1] - dy, 0],
                    color=CHALK, stroke_width=2.4)
        a_edge = float(np.degrees(np.arcsin(dy / r)))
        big = arc_piece(c2, r, a_edge, 360 - a_edge, ORANGE, 0.24)
        small = arc_piece(c2, r, -a_edge, a_edge, PURPLE, 0.28)
        self.play(Create(ring2), Create(cut2), run_time=0.8)
        self.play(FadeIn(big), FadeIn(small), run_time=0.8)

        t2 = txt("✗ 不是平均分", size=28, color=RED).move_to([3.2, -1.15, 0])
        note1 = txt("一块大、一块小", size=24, color=DIM).move_to([3.2, -1.95, 0])
        note2 = txt("都不能叫二分之一", size=24, color=DIM).move_to([3.2, -2.55, 0])
        self.play(Create(t2), run_time=0.6)
        self.play(FadeIn(note1, shift=UP * 0.06), run_time=0.5)
        self.play(FadeIn(note2, shift=UP * 0.06), run_time=0.5)
        self.finish_section()

    # ---------------- 2. 1/2 的读写 ----------------
    def scene_read(self):
        self.section(2, "分数线、分母、分子")

        big = frac("1", "2", [-3.3, 0.35], size=110, color=GOLD)
        self.play(Write(big), run_time=1.4)

        # 三根引线
        num_lab = txt("分子：取几份", size=27, color=BLUE).move_to([2.9, 1.55, 0])
        line_lab = txt("分数线：平均分", size=27, color=GOLD).move_to([2.9, 0.4, 0])
        den_lab = txt("分母：分成几份", size=27, color=GREEN).move_to([2.9, -0.75, 0])
        self.play(FadeIn(num_lab, shift=LEFT * 0.08), run_time=0.7)
        self.play(FadeIn(line_lab, shift=LEFT * 0.08), run_time=0.7)
        self.play(FadeIn(den_lab, shift=LEFT * 0.08), run_time=0.7)

        r1 = txt("读作：二分之一", size=34, color=CHALK).move_to([0, -1.6, 0])
        r2 = txt("先读分母，再读分子", size=26, color=DIM).move_to([0, -2.35, 0])
        self.play(FadeIn(r1, shift=UP * 0.06), run_time=0.7)
        self.play(FadeIn(r2, shift=UP * 0.06), run_time=0.6)
        self.finish_section()

    # ---------------- 3. 几分之几 ----------------
    def scene_thirds(self):
        self.section(3, "四分之一到四分之三")

        center = [-3.3, 0.55, 0]
        u = 1.05
        cells = square_cells(2, 2, u, center)
        fr = Square(side_length=2 * u, color=CHALK, stroke_width=3).move_to(center)
        self.play(Create(fr), run_time=0.7)
        self.play(LaggedStart(*[Create(c) for c in cells], lag_ratio=0.12), run_time=1.0)

        lab1 = frac("1", "4", [-3.3, -1.35], size=38, color=GOLD)
        self.play(cells[0].animate.set_fill(GOLD, opacity=0.35), run_time=0.8)
        self.play(FadeIn(lab1, shift=UP * 0.06), run_time=0.5)

        lab3 = frac("3", "4", [-3.3, -1.35], size=38, color=GOLD)
        self.play(cells[1].animate.set_fill(GOLD, opacity=0.35),
                  cells[2].animate.set_fill(GOLD, opacity=0.35),
                  run_time=0.9)
        self.play(Transform(lab1, lab3), run_time=0.6)

        h = txt("平均分成 4 份", size=28, color=DIM).move_to([2.95, 1.45, 0])
        h2 = txt("涂了几份，分子就是几", size=26, color=CHALK).move_to([2.95, 0.65, 0])
        self.play(FadeIn(h, shift=UP * 0.06), run_time=0.6)
        self.play(FadeIn(h2, shift=UP * 0.06), run_time=0.6)

        e1 = txt("涂 1 份 → 四分之一", size=26, color=GOLD).move_to([2.95, -0.35, 0])
        e2 = txt("涂 3 份 → 四分之三", size=26, color=GOLD).move_to([2.95, -1.1, 0])
        self.play(FadeIn(e1, shift=UP * 0.06), run_time=0.6)
        self.play(FadeIn(e2, shift=UP * 0.06), run_time=0.6)
        self.finish_section()

    # ---------------- 4. 分数单位 ----------------
    def scene_unit(self):
        self.section(4, "四分之三里有 3 个四分之一")

        cells = bar(4, 1.05, [-2.5, 0.95], color=CHALK)
        tags = VGroup()
        for i, c in enumerate(cells):
            tags.add(frac("1", "4", [c.get_center()[0], -0.05, 0], size=28, color=DIM))
        self.play(LaggedStart(*[Create(c) for c in cells], lag_ratio=0.1), run_time=1.0)
        self.play(LaggedStart(*[FadeIn(t) for t in tags], lag_ratio=0.1), run_time=0.9)

        unit_lab = txt("四分之一是分数单位", size=27, color=GOLD).move_to([-2.5, 1.9, 0])
        self.play(FadeIn(unit_lab, shift=UP * 0.06), run_time=0.6)

        for i in range(3):
            self.play(cells[i].animate.set_fill(GOLD, opacity=0.32), run_time=0.45)

        eq = VGroup(
            frac("1", "4", [0, 0, 0], size=34, color=GOLD),
            txt("+", size=32, color=DIM),
            frac("1", "4", [0, 0, 0], size=34, color=GOLD),
            txt("+", size=32, color=DIM),
            frac("1", "4", [0, 0, 0], size=34, color=GOLD),
            txt("=", size=32, color=DIM),
            frac("3", "4", [0, 0, 0], size=34, color=GREEN),
        ).arrange(RIGHT, buff=0.3).move_to([0, -1.55, 0])
        self.play(FadeIn(unit_lab), run_time=0.3)
        self.play(Write(eq), run_time=1.4)

        tip = txt("3 个四分之一，就是四分之三", size=28, color=GREEN).move_to([0, -2.55, 0])
        self.play(FadeIn(tip, shift=UP * 0.08), run_time=0.7)
        self.finish_section()

    # ---------------- 5. 比大小 ----------------
    def scene_compare(self):
        self.section(5, "同分母比分子，同分子比分母")

        # 上排：同分母
        b1 = bar(5, 0.52, [-2.5, 1.45], color=CHALK)
        b2 = bar(5, 0.52, [3.0, 1.45], color=CHALK)
        self.play(LaggedStart(*[Create(c) for c in b1], lag_ratio=0.06), run_time=0.8)
        self.play(LaggedStart(*[Create(c) for c in b2], lag_ratio=0.06), run_time=0.8)

        for i in range(2):
            self.play(b1[i].animate.set_fill(BLUE, opacity=0.35), run_time=0.3)
        for i in range(4):
            self.play(b2[i].animate.set_fill(BLUE, opacity=0.35), run_time=0.25)

        f1 = frac("2", "5", [-4.35, 1.45], size=34, color=BLUE)
        lt = txt("＜", size=40, color=RED).move_to([0.25, 1.45, 0])
        f2 = frac("4", "5", [4.85, 1.45], size=34, color=BLUE)
        self.play(FadeIn(f1), FadeIn(lt), FadeIn(f2), run_time=0.8)

        r1 = txt("分母相同，分子大的大", size=25, color=DIM).move_to([0.25, 0.55, 0])
        self.play(FadeIn(r1, shift=UP * 0.05), run_time=0.6)

        # 下排：同分子
        c1 = bar(2, 0.9, [-2.9, -1.55], color=CHALK)
        c2 = bar(4, 0.62, [3.0, -1.55], color=CHALK)
        self.play(LaggedStart(*[Create(c) for c in c1], lag_ratio=0.1), run_time=0.7)
        self.play(LaggedStart(*[Create(c) for c in c2], lag_ratio=0.08), run_time=0.8)

        self.play(c1[0].animate.set_fill(GREEN, opacity=0.35), run_time=0.5)
        self.play(c2[0].animate.set_fill(GREEN, opacity=0.35), run_time=0.5)

        g1 = frac("1", "2", [-4.35, -1.55], size=34, color=GREEN)
        gt = txt("＞", size=40, color=RED).move_to([0.25, -1.55, 0])
        g2 = frac("1", "4", [4.85, -1.55], size=34, color=GREEN)
        self.play(FadeIn(g1), FadeIn(gt), FadeIn(g2), run_time=0.8)

        r2 = txt("分子相同，分母大的反而小", size=25, color=DIM).move_to([0.25, -2.55, 0])
        self.play(FadeIn(r2, shift=UP * 0.05), run_time=0.7)
        self.finish_section()

    # ---------------- 6. 收束 ----------------
    def scene_summary(self):
        self.section(6, "分数三句话")

        rows = VGroup(
            label_box("① 必须平均分", size=30, color=GOLD),
            label_box("② 分母是分成几份，分子是取几份", size=28, color=CHALK),
            label_box("③ 同分母比分子，同分子比分母", size=28, color=CHALK),
        ).arrange(DOWN, buff=0.45).move_to([0, 0.55, 0])
        for r in rows:
            self.play(FadeIn(r, shift=RIGHT * 0.1), run_time=0.6)

        tip = txt("分的份数越多，每份越小", size=29, color=GREEN).move_to([0, -1.85, 0])
        self.play(FadeIn(tip, shift=UP * 0.08), run_time=0.8)
        self.finish_section()

    def construct(self):
        self.scene_story()
        self.clear_stage()
        self.scene_average()
        self.clear_stage()
        self.scene_read()
        self.clear_stage()
        self.scene_thirds()
        self.clear_stage()
        self.scene_unit()
        self.clear_stage()
        self.scene_compare()
        self.clear_stage()
        self.scene_summary()
        self.clear_stage(0.8)