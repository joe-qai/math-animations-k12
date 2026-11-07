# -*- coding: utf-8 -*-
"""统计图的选择与综合实践：四种图的分工、抽样估计、测量与方案设计。九年级下。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


def P(x, y):
    return np.array([float(x), float(y), 0.0])


class TongjituXuanzeScene(NarratedScene):
    lesson = "tongjitu-xuanze"

    def clear_stage(self, run_time: float = 0.5):
        keep = {id(self._track), id(self._fill)}
        junk = [m for m in self.mobjects if id(m) not in keep]
        if junk:
            self.play(*[FadeOut(m) for m in junk], run_time=run_time)
        self.cur_title = None
        self.cur_sub = None

    # ---------- 小图元件 ----------
    def mini_bar(self, cx, cy, col, w=1.5, h=1.1):
        base = Line(P(cx - w / 2, cy - h / 2), P(cx + w / 2, cy - h / 2),
                    color=DIM, stroke_width=1.8)
        bars = VGroup()
        hs = [0.34, 0.78, 0.52, 0.24]
        for i, hh in enumerate(hs):
            x = cx - w / 2 + 0.28 + i * 0.28
            bars.add(Rectangle(width=0.17, height=hh, color=col, fill_color=col,
                               fill_opacity=0.55, stroke_width=1.3)
                     .move_to([x, cy - h / 2 + hh / 2 + 0.02, 0]))
        return VGroup(base, bars)

    def mini_line(self, cx, cy, col, w=1.5, h=1.1):
        base = Line(P(cx - w / 2, cy - h / 2), P(cx + w / 2, cy - h / 2),
                    color=DIM, stroke_width=1.8)
        left = Line(P(cx - w / 2, cy - h / 2), P(cx - w / 2, cy + h / 2),
                    color=DIM, stroke_width=1.8)
        pts = [(cx - w / 2 + 0.12, cy - h / 2 + 0.3),
               (cx - w / 2 + 0.42, cy - h / 2 + 0.72),
               (cx - w / 2 + 0.72, cy - h / 2 + 0.5),
               (cx - w / 2 + 1.02, cy - h / 2 + 1.0),
               (cx - w / 2 + 1.32, cy - h / 2 + 0.85)]
        poly = VMobject(color=col, stroke_width=2.6)
        poly.set_points_as_corners([P(x, y) for x, y in pts])
        dots = VGroup(*[Dot(P(x, y), radius=0.035, color=col) for x, y in pts])
        return VGroup(base, left, poly, dots)

    def mini_pie(self, cx, cy, cols, r=0.62):
        vals = [0.4, 0.35, 0.25]
        parts = VGroup()
        start = 0.0
        for v, c in zip(vals, cols):
            pts = [P(cx, cy)]
            n = 14
            for k in range(n + 1):
                a = (start + v * k / n) * TAU
                pts.append(P(cx + r * np.cos(a), cy + r * np.sin(a)))
            poly = Polygon(*pts, color=c, fill_color=c, fill_opacity=0.55,
                           stroke_width=1.4)
            parts.add(poly)
            start += v
        return parts

    def mini_hist(self, cx, cy, col, total_w=1.5, h=1.1):
        base = Line(P(cx - total_w / 2, cy - h / 2), P(cx + total_w / 2, cy - h / 2),
                    color=DIM, stroke_width=1.8)
        left = Line(P(cx - total_w / 2, cy - h / 2), P(cx - total_w / 2, cy + h / 2),
                    color=DIM, stroke_width=1.8)
        hs = [0.22, 0.5, 0.86, 0.62, 0.3]
        bw = total_w / len(hs)
        bars = VGroup()
        for i, hh in enumerate(hs):
            bars.add(Rectangle(width=bw, height=hh, color=col, fill_color=col,
                               fill_opacity=0.35, stroke_width=1.4)
                     .move_to([cx - total_w / 2 + bw / 2 + i * bw,
                               cy - h / 2 + hh / 2 + 0.01, 0]))
        return VGroup(base, left, bars)

    # ---------------- 0. 三个需求 ---------------- 23.9
    def scene_intro(self):
        self.section(0, "三种需求，三种图")

        cards = [
            (-4.55, "比人数", "每种运动各有多少人", GOLD, "bar"),
            (0.0, "看趋势", "一周气温怎么变", GREEN, "line"),
            (4.55, "看占比", "各项支出占多少", BLUE, "pie"),
        ]
        for cx, name, why, col, kind in cards:
            self.play(FadeIn(txt(name, size=26, color=col).move_to([cx, 2.2, 0])),
                      run_time=0.6)
            if kind == "bar":
                g = self.mini_bar(cx, 0.55, col)
            elif kind == "line":
                g = self.mini_line(cx, 0.55, col)
            else:
                g = self.mini_pie(cx, 0.55, [BLUE, GOLD, GREEN])
            self.play(Create(g), run_time=0.9)
            self.play(FadeIn(txt(why, size=20, color=DIM).move_to([cx, -0.55, 0])),
                      run_time=0.6)
        self.wait(0.7)

        d = txt("同一组数据，选错图就看不出重点", size=26, color=CHALK).move_to([0, -1.55, 0])
        self.play(FadeIn(d, shift=UP * 0.04), run_time=0.95)
        box = label_box("先想清楚：这张图要回答什么问题", size=23, color=GOLD)
        box.move_to([0, -2.45, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.0)
        self.wait(14.0)
        self.finish_section()

    # ---------------- 1. 四种图各自擅长 ---------------- 24.8
    def scene_types(self):
        self.section(1, "四种统计图的分工")

        items = [
            (-3.55, 1.35, "条形图：比多少", GOLD, "bar"),
            (3.55, 1.35, "折线图：看趋势", GREEN, "line"),
            (-3.55, -1.05, "扇形图：看占比", BLUE, "pie"),
            (3.55, -1.05, "直方图：看分布", ORANGE, "hist"),
        ]
        for cx, cy, name, col, kind in items:
            self.play(FadeIn(txt(name, size=23, color=col).move_to([cx, cy + 1.05, 0])),
                      run_time=0.6)
            if kind == "bar":
                g = self.mini_bar(cx, cy - 0.25, col)
            elif kind == "line":
                g = self.mini_line(cx, cy - 0.25, col)
            elif kind == "pie":
                g = self.mini_pie(cx, cy - 0.25, [BLUE, GOLD, GREEN])
            else:
                g = self.mini_hist(cx, cy - 0.25, col)
            self.play(Create(g), run_time=0.9)
        self.wait(0.8)

        note = txt("横轴是类别，纵轴是数量；直方图的横轴是分组", size=23, color=CHALK)
        note.move_to([0, -2.55, 0])
        self.play(FadeIn(note, shift=UP * 0.04), run_time=0.95)
        self.wait(13.5)
        self.finish_section()

    # ---------------- 2. 口诀与规矩 ---------------- 25.7
    def scene_rules(self):
        self.section(2, "选图口诀")

        rows = [
            ("比多少", "条形图", GOLD),
            ("看变化", "折线图", GREEN),
            ("看占比", "扇形图", BLUE),
            ("看分布", "直方图", ORANGE),
        ]
        y = 2.0
        for a, b, col in rows:
            ta = txt(a, size=24, color=DIM).move_to([-4.3, y, 0])
            arrow = Arrow(P(-3.2, y), P(-2.1, y), color=col, stroke_width=2.4,
                          buff=0.05, max_tip_length_to_length_ratio=0.22)
            tb = txt(b, size=26, color=col).move_to([-0.95, y, 0])
            self.play(FadeIn(ta), GrowArrow(arrow), FadeIn(tb, shift=RIGHT * 0.04),
                      run_time=0.75)
            y -= 0.88
        self.wait(0.6)

        notes = [
            ("扇形图必须先知道总数", BLUE),
            ("百分比 × 360° = 圆心角", BLUE),
            ("直方图：面积表示频数", ORANGE),
            ("条形图：直条等宽、等距", GOLD),
        ]
        y = 1.95
        for s, col in notes:
            t = txt(s, size=22, color=col).move_to([3.4, y, 0])
            self.play(FadeIn(t, shift=RIGHT * 0.04), run_time=0.8)
            y -= 0.82
        self.wait(0.6)

        box = label_box("选错图，等于没读数据", size=23, color=RED).move_to([0, -2.55, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.0)
        self.wait(11.0)
        self.finish_section()

    # ---------------- 3. 抽样与估计 ---------------- 28.6
    def scene_sample(self):
        self.section(3, "抽样与估计")

        chips = [
            (-5.0, "总体", "被考察的全体"),
            (-1.7, "个体", "其中的每一个"),
            (1.7, "样本", "抽取的一部分"),
            (5.0, "样本容量", "样本中个体数"),
        ]
        for cx, name, why in chips:
            self.play(FadeIn(txt(name, size=24, color=GOLD).move_to([cx, 2.05, 0])),
                      run_time=0.55)
            self.play(FadeIn(txt(why, size=19, color=DIM).move_to([cx, 1.55, 0])),
                      run_time=0.5)
        self.wait(0.6)

        key = txt("样本要随机抽取，要有代表性", size=24, color=GREEN).move_to([0, 0.75, 0])
        self.play(FadeIn(key, shift=UP * 0.04), run_time=0.9)
        self.wait(0.5)

        q1 = txt("抽查 200 人，近视率 30%", size=26, color=CHALK).move_to([0, -0.15, 0])
        self.play(FadeIn(q1, shift=UP * 0.04), run_time=0.8)
        q2 = txt("200 × 30% = 60 人", size=23, color=DIM).move_to([0, -0.95, 0])
        self.play(FadeIn(q2), run_time=0.7)
        q3 = txt("全校 1200 人：1200 × 30% = 360 人", size=26, color=GOLD)
        q3.move_to([0, -1.75, 0])
        self.play(FadeIn(q3, shift=UP * 0.04), run_time=0.95)
        self.wait(0.6)

        box = label_box("样本比例 ≈ 总体比例", size=23, color=RED).move_to([0, -2.6, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.0)
        self.wait(11.5)
        self.finish_section()

    # ---------------- 4. 综合实践：测量 ---------------- 24.2
    def scene_measure(self):
        self.section(4, "综合实践：把不可测变成可测")

        h1 = txt("测旗杆高", size=23, color=GOLD).move_to([-3.9, 2.25, 0])
        self.play(FadeIn(h1, shift=UP * 0.04), run_time=0.7)

        pole = Line(P(-5.6, -1.35), P(-5.6, 1.45), color=CHALK, stroke_width=3.0)
        shadow = Line(P(-5.6, -1.35), P(-2.7, -1.35), color=DIM, stroke_width=2.4)
        hl = Line(P(-5.6, -1.35), P(-2.7, -1.35), color=DIM, stroke_width=0)
        ray = DashedLine(P(-5.6, 1.45), P(-2.7, -1.35), color=GOLD, stroke_width=1.8,
                         dash_length=0.09)
        self.play(Create(pole), Create(shadow), run_time=0.9)
        self.play(Create(ray), run_time=0.8)
        self.play(FadeIn(txt("物高", size=20, color=GOLD).move_to([-6.1, 0.25, 0])),
                  FadeIn(txt("影长", size=20, color=DIM).move_to([-4.15, -1.7, 0])),
                  run_time=0.7)
        self.wait(0.5)

        f = txt("物高 : 影长 = 物高 : 影长", size=23, color=CHALK).move_to([-4.0, -2.35, 0])
        self.play(FadeIn(f, shift=UP * 0.04), run_time=0.8)

        h2 = txt("测池塘两端距离", size=23, color=BLUE).move_to([3.6, 2.25, 0])
        self.play(FadeIn(h2, shift=UP * 0.04), run_time=0.7)

        pond = Ellipse(width=3.8, height=1.5, color=BLUE, fill_color=BLUE,
                       fill_opacity=0.10, stroke_width=1.6).move_to([3.6, -0.95, 0])
        self.play(Create(pond), run_time=0.7)

        A = P(2.3, -0.55)
        B = P(4.8, -0.8)
        C = P(3.55, -1.35)
        D = P(2 * C[0] - A[0], 2 * C[1] - A[1])
        E = P(2 * C[0] - B[0], 2 * C[1] - B[1])
        self.play(FadeIn(Dot(A, radius=0.05, color=GOLD)),
                  FadeIn(Dot(B, radius=0.05, color=GOLD)), run_time=0.5)
        self.play(FadeIn(txt("A", size=18, color=GOLD).move_to(A + LEFT * 0.22 + UP * 0.12)),
                  FadeIn(txt("B", size=18, color=GOLD).move_to(B + RIGHT * 0.22 + UP * 0.12)),
                  run_time=0.5)
        self.play(Create(DashedLine(A, C, color=DIM, stroke_width=1.8, dash_length=0.08)),
                  Create(DashedLine(B, C, color=DIM, stroke_width=1.8, dash_length=0.08)),
                  run_time=0.8)
        self.play(Create(Line(C, D, color=GOLD, stroke_width=2.2)),
                  Create(Line(C, E, color=GOLD, stroke_width=2.2)),
                  run_time=0.8)
        self.play(Create(Line(D, E, color=GREEN, stroke_width=2.8)), run_time=0.7)
        self.play(FadeIn(txt("C", size=18, color=DIM).move_to(C + RIGHT * 0.24 + DOWN * 0.1)),
                  FadeIn(txt("D", size=18, color=GOLD).move_to(D + RIGHT * 0.22)),
                  FadeIn(txt("E", size=18, color=GOLD).move_to(E + LEFT * 0.24)),
                  run_time=0.6)
        self.play(FadeIn(txt("DE = AB", size=20, color=GREEN).move_to([5.9, -1.9, 0])),
                  run_time=0.6)
        self.play(FadeIn(txt("构造全等三角形", size=21, color=GREEN).move_to([3.6, -2.45, 0])),
                  run_time=0.8)
        self.wait(0.6)

        box = label_box("先设计方案，再动手测量", size=23, color=RED).move_to([0, -2.95, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.0)
        self.wait(8.0)
        self.finish_section()

    # ---------------- 5. 综合实践：方案设计 ---------------- 25.4
    def scene_plan(self):
        self.section(5, "综合实践：方案设计")

        # 矩形菜地
        rx, ry, rw, rh = -4.2, 0.3, 3.2, 1.9
        wall = DashedLine(P(rx - rw / 2, ry - rh / 2), P(rx + rw / 2, ry - rh / 2),
                          color=DIM, stroke_width=2.6, dash_length=0.12)
        f1 = Line(P(rx - rw / 2, ry - rh / 2), P(rx - rw / 2, ry + rh / 2),
                  color=GOLD, stroke_width=2.4)
        f2 = Line(P(rx - rw / 2, ry + rh / 2), P(rx + rw / 2, ry + rh / 2),
                  color=GOLD, stroke_width=2.4)
        f3 = Line(P(rx + rw / 2, ry + rh / 2), P(rx + rw / 2, ry - rh / 2),
                  color=GOLD, stroke_width=2.4)
        self.play(Create(wall), Create(f1), Create(f2), Create(f3), run_time=1.0)
        self.play(FadeIn(txt("墙（不用围）", size=19, color=DIM).move_to([rx, ry - rh / 2 - 0.42, 0])),
                  FadeIn(txt("篱笆", size=20, color=GOLD).move_to([rx, ry + rh / 2 + 0.38, 0])),
                  run_time=0.7)
        self.play(FadeIn(txt("x", size=22, color=BLUE).move_to([rx - rw / 2 - 0.32, ry, 0])),
                  run_time=0.5)
        self.wait(0.5)

        steps = [
            ("① 设变量：一边为 x", CHALK),
            ("② 列关系式：S = x(L − 2x)/2", CHALK),
            ("③ 写取值范围：0 < x < L/2", CHALK),
            ("④ 配方求最值，顶点取不到取端点", GOLD),
        ]
        y = 2.0
        for s, col in steps:
            t = txt(s, size=22, color=col).move_to([3.3, y, 0])
            self.play(FadeIn(t, shift=RIGHT * 0.04), run_time=0.8)
            y -= 0.85
        self.wait(0.6)

        box = label_box("忘了写范围，最值根本取不到", size=22, color=RED)
        box.move_to([0, -2.6, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.0)
        self.wait(10.0)
        self.finish_section()

    # ---------------- 6. 易错点 ---------------- 21.5
    def scene_traps(self):
        self.section(6, "四个易错点")

        rows = [
            ("① 没总数就用扇形图", "百分比算不出来"),
            ("② 折线连了类别数据", "类别之间没有趋势"),
            ("③ 样本不随机", "估计就不可靠"),
            ("④ 方案不写范围", "最值取不到"),
        ]
        y = 1.85
        for a, b in rows:
            ta = txt(a, size=23, color=RED).move_to([-2.6, y, 0])
            tb = txt(b, size=21, color=DIM).move_to([3.6, y, 0])
            self.play(FadeIn(ta, shift=RIGHT * 0.04), run_time=0.65)
            self.play(FadeIn(tb, shift=RIGHT * 0.04), run_time=0.65)
            y -= 0.86
        self.wait(1.0)

        box = label_box("先看目的选图，再用数据说话", size=24, color=GOLD)
        box.move_to([0, -2.45, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.1)
        self.wait(8.0)
        self.finish_section()

    def construct(self):
        self.scene_intro()
        self.clear_stage()
        self.scene_types()
        self.clear_stage()
        self.scene_rules()
        self.clear_stage()
        self.scene_sample()
        self.clear_stage()
        self.scene_measure()
        self.clear_stage()
        self.scene_plan()
        self.clear_stage()
        self.scene_traps()
        self.clear_stage(0.8)