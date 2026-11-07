# -*- coding: utf-8 -*-
"""中考专题 6：统计与概率。数据收集、统计图、平均数与方差、概率、频率估计。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


def P(x, y):
    return np.array([float(x), float(y), 0.0])


def pie_poly(cx, cy, r, a0, a1, color, n=40, fill_opacity=0.55):
    pts = [P(cx, cy)]
    for k in range(n + 1):
        a = (a0 + (a1 - a0) * k / n) * DEGREES
        pts.append(P(cx + r * np.cos(a), cy + r * np.sin(a)))
    poly = Polygon(*pts, color=color, stroke_width=2.0)
    poly.set_fill(color, opacity=fill_opacity)
    return poly


def mk_axes(xr, yr, xl=4.6, yl=3.0, pos=(-3.7, -0.4)):
    ax = Axes(
        x_range=xr,
        y_range=yr,
        x_length=xl,
        y_length=yl,
        axis_config={"color": DIM, "stroke_width": 2.0,
                     "include_numbers": False, "tip_length": 0.15},
    )
    ax.move_to(np.array([float(pos[0]), float(pos[1]), 0.0]))
    return ax


class ZhongkaoTongjiGailvScene(NarratedScene):
    lesson = "zhongkao-tongji-gailv"

    def clear_stage(self, run_time: float = 0.5):
        keep = {id(self._track), id(self._fill)}
        junk = [m for m in self.mobjects if id(m) not in keep]
        if junk:
            self.play(*[FadeOut(m) for m in junk], run_time=run_time)
        self.cur_title = None
        self.cur_sub = None

    # ---------------- 0. 送分题 ---------------- 24.6
    def scene_intro(self):
        self.section(0, "统计与概率：投入产出比最高")

        chips = [(-4.8, "数据收集", GOLD), (-1.6, "统计图", GREEN),
                 (1.6, "平均数与方差", BLUE), (4.8, "概率", ORANGE)]
        for cx, name, col in chips:
            c = label_box(name, size=20, color=col).move_to([cx, 1.75, 0])
            if c.width > 3.0:
                c.scale_to_fit_width(3.0)
            self.play(FadeIn(c, shift=UP * 0.04), run_time=0.7)
        self.wait(0.5)

        rows = [
            ("全是基础题，题型几乎不变", CHALK),
            ("约 15 分，是性价比最高的一块", GOLD),
            ("失分不在难度，在概念混淆", RED),
        ]
        y = 0.7
        for s, col in rows:
            t = txt(s, size=24, color=col).move_to([0, y, 0])
            self.play(FadeIn(t, shift=UP * 0.04), run_time=0.8)
            y -= 0.74
        self.wait(0.5)

        box = label_box("收集 · 描述 · 分析 · 推断", size=23, color=GOLD)
        box.move_to([0, -2.45, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.0)
        self.wait(9.0)
        self.finish_section()

    # ---------------- 1. 数据收集 ---------------- 25.0
    def scene_collect(self):
        self.section(1, "数据收集：随机才有代表性")

        b1 = label_box("全面调查（普查）", size=20, color=GOLD).move_to([-3.6, 2.05, 0])
        b2 = label_box("抽样调查", size=20, color=GREEN).move_to([3.6, 2.05, 0])
        self.play(FadeIn(b1, shift=UP * 0.04), FadeIn(b2, shift=UP * 0.04), run_time=0.9)
        n1 = txt("结果准确，花费大", size=20, color=DIM).move_to([-3.6, 1.35, 0])
        n2 = txt("省时省力，靠样本推断", size=20, color=DIM).move_to([3.6, 1.35, 0])
        self.play(FadeIn(n1), FadeIn(n2), run_time=0.8)
        self.wait(0.4)

        terms = [
            ("总体", "考察对象的全体", -3.6, 0.35),
            ("个体", "每一个考察对象", 3.6, 0.35),
            ("样本", "抽取的一部分个体", -3.6, -0.55),
            ("样本容量", "样本中个体的数目", 3.6, -0.55),
        ]
        for name, desc, cx, cy in terms:
            t1 = txt(name, size=21, color=BLUE).move_to([cx - 1.5, cy, 0])
            t2 = txt(desc, size=18, color=CHALK).move_to([cx + 1.15, cy, 0])
            self.play(FadeIn(t1, shift=RIGHT * 0.03), FadeIn(t2, shift=RIGHT * 0.03),
                      run_time=0.6)
        self.wait(0.5)

        box = label_box("抽样的关键：随机 + 有代表性", size=22, color=RED)
        box.move_to([0, -2.3, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.0)
        self.wait(10.5)
        self.finish_section()

    # ---------------- 2. 统计图 ---------------- 23.0
    def scene_charts(self):
        self.section(2, "统计图：先看目的再选图")

        rows = [
            ("条形图看数量，折线图看变化", CHALK),
            ("扇形图看占比，直方图看分布", CHALK),
        ]
        y = 2.35
        for s, col in rows:
            t = txt(s, size=22, color=col).move_to([0, y, 0])
            self.play(FadeIn(t, shift=UP * 0.04), run_time=0.7)
            y -= 0.62
        self.wait(0.3)

        # 条形图
        heights = [0.55, 0.95, 0.75, 1.15]
        bars = VGroup()
        for i, h in enumerate(heights):
            bar = Rectangle(width=0.34, height=h, color=GOLD,
                            stroke_width=1.6, fill_color=GOLD, fill_opacity=0.25)
            bar.move_to(P(-5.45 + i * 0.46, -1.05 + h / 2))
            bars.add(bar)
        base1 = Line(P(-5.85, -1.05), P(-3.6, -1.05), color=DIM, stroke_width=2.0)
        self.play(Create(base1), *[FadeIn(b) for b in bars], run_time=1.0)
        self.play(FadeIn(txt("条形", size=19, color=GOLD).move_to([-4.7, -1.75, 0])),
                  run_time=0.5)

        # 折线图
        base2 = Line(P(-2.9, -1.05), P(-1.0, -1.05), color=DIM, stroke_width=2.0)
        pts = [P(-2.8, -0.75), P(-2.35, -0.25), P(-1.9, -0.55), P(-1.45, 0.35)]
        line = VMobject(color=GREEN, stroke_width=2.8)
        line.set_points_as_corners(pts)
        dots = VGroup(*[Dot(p, radius=0.045, color=GREEN) for p in pts])
        self.play(Create(base2), Create(line), *[FadeIn(d) for d in dots], run_time=1.1)
        self.play(FadeIn(txt("折线", size=19, color=GREEN).move_to([-1.95, -1.75, 0])),
                  run_time=0.5)

        # 扇形图
        cx, cy, r = 1.15, -0.35, 0.72
        sectors = [(0, 130, GOLD), (130, 240, BLUE), (240, 360, ORANGE)]
        pies = VGroup(*[pie_poly(cx, cy, r, a0, a1, col) for a0, a1, col in sectors])
        self.play(*[FadeIn(s) for s in pies], run_time=1.1)
        self.play(FadeIn(txt("扇形", size=19, color=BLUE).move_to([1.15, -1.75, 0])),
                  run_time=0.5)

        # 直方图
        hs = [0.35, 0.85, 1.15, 0.6, 0.4]
        hist = VGroup()
        for i, h in enumerate(hs):
            r_ = Rectangle(width=0.35, height=h, color=BLUE,
                           stroke_width=1.4, fill_color=BLUE, fill_opacity=0.22)
            r_.move_to(P(2.95 + i * 0.35, -1.05 + h / 2))
            hist.add(r_)
        base3 = Line(P(2.75, -1.05), P(4.85, -1.05), color=DIM, stroke_width=2.0)
        self.play(Create(base3), *[FadeIn(r_) for r_ in hist], run_time=1.0)
        self.play(FadeIn(txt("直方图", size=19, color=BLUE).move_to([3.85, -1.75, 0])),
                  run_time=0.5)
        self.wait(0.5)

        box = label_box("想让人看到什么，就选什么图", size=22, color=RED)
        box.move_to([0, -2.5, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.0)
        self.wait(6.0)
        self.finish_section()

    # ---------------- 3. 平均数、中位数、众数、方差 ---------------- 21.4
    def scene_stats(self):
        self.section(3, "平均数、中位数、众数与方差")

        data = txt("数据：2, 3, 3, 5, 7", size=26, color=CHALK).move_to([0, 2.1, 0])
        self.play(FadeIn(data, shift=UP * 0.04), run_time=0.8)
        self.wait(0.3)

        cards = [
            ("平均数", "4", "受每个数据影响", GOLD, -4.55),
            ("中位数", "3", "排序后最中间", GREEN, -1.5),
            ("众数", "3", "出现次数最多", BLUE, 1.55),
            ("方差", "3.2", "越小越稳定", ORANGE, 4.6),
        ]
        for name, val, note, col, cx in cards:
            box = label_box(name, size=20, color=col).move_to([cx, 0.95, 0])
            v = txt(val, size=30, color=col).move_to([cx, 0.05, 0])
            n = txt(note, size=17, color=DIM).move_to([cx, -0.55, 0])
            self.play(FadeIn(box, shift=UP * 0.04), run_time=0.55)
            self.play(FadeIn(v), FadeIn(n), run_time=0.55)
        self.wait(0.5)

        f = txt("s² = [(x₁ − x̄)² + (x₂ − x̄)² + … ] / n", size=24, color=GOLD)
        f.move_to([0, -1.45, 0])
        self.play(FadeIn(f, shift=UP * 0.04), run_time=0.8)
        self.wait(0.4)

        box = label_box("方差越小，数据越集中", size=22, color=RED)
        box.move_to([0, -2.45, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.0)
        self.wait(6.5)
        self.finish_section()

    # ---------------- 4. 概率 ---------------- 23.5
    def scene_prob(self):
        self.section(4, "概率：m 比 n，不重不漏")

        f = txt("P = m / n", size=34, color=GOLD).move_to([-4.4, 2.05, 0])
        self.play(FadeIn(f, shift=UP * 0.04), run_time=0.8)
        n1 = txt("n：所有等可能结果数", size=20, color=DIM).move_to([-4.4, 1.35, 0])
        n2 = txt("m：所求事件包含的结果数", size=20, color=DIM).move_to([-4.4, 0.85, 0])
        self.play(FadeIn(n1), FadeIn(n2), run_time=0.7)
        self.wait(0.3)

        ex = txt("掷骰子：P(点数为偶数) = 3/6 = 1/2", size=22, color=GREEN)
        ex.move_to([-4.4, -0.05, 0])
        self.play(FadeIn(ex, shift=UP * 0.04), run_time=0.8)
        self.wait(0.3)

        e1 = txt("必然事件：P = 1", size=20, color=BLUE).move_to([-4.4, -0.95, 0])
        e2 = txt("不可能事件：P = 0", size=20, color=RED).move_to([-4.4, -1.6, 0])
        self.play(FadeIn(e1), FadeIn(e2), run_time=0.7)
        self.wait(0.4)

        # 两枚硬币的树状/表格
        head = txt("两枚硬币：4 种等可能", size=20, color=CHALK).move_to([3.4, 1.9, 0])
        self.play(FadeIn(head, shift=UP * 0.04), run_time=0.7)
        cells = [("正正", 0.25), ("正反", 0.25), ("反正", 0.25), ("反反", 0.25)]
        xs = [-1.6, -0.6]
        for i, (s, _) in enumerate(cells):
            cx = xs[i % 2]
            cy = 0.95 - (i // 2) * 0.85
            box = Rectangle(width=0.9, height=0.65, color=DIM, stroke_width=1.5)
            box.move_to(P(2.5 + (cx + 1.6) * 1.1, cy))
            lab = txt(s, size=19, color=CHALK).move_to(box.get_center())
            self.play(FadeIn(box), FadeIn(lab), run_time=0.5)
        self.wait(0.3)

        r = txt("P(两正) = 1/4", size=22, color=GREEN).move_to([3.4, -0.85, 0])
        self.play(FadeIn(r, shift=UP * 0.04), run_time=0.7)
        tip = txt("列表或树状图：做到不重不漏", size=19, color=DIM).move_to([3.4, -1.55, 0])
        self.play(FadeIn(tip), run_time=0.6)
        self.wait(0.4)

        box = label_box("先分类，再列举", size=22, color=RED)
        box.move_to([0, -2.5, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.0)
        self.wait(9.0)
        self.finish_section()

    # ---------------- 5. 频率与概率 ---------------- 21.8
    def scene_freq(self):
        self.section(5, "频率估计概率：试验越多越接近")

        ax = mk_axes([0, 10, 1], [0, 1, 0.5], 5.0, 3.0, (-3.9, -0.35))
        self.play(Create(ax), run_time=0.9)
        half = DashedLine(ax.c2p(0, 0.5), ax.c2p(10, 0.5), color=GOLD,
                          stroke_width=1.6, dash_length=0.08)
        self.play(Create(half), run_time=0.7)
        self.play(FadeIn(txt("0.5", size=18, color=GOLD).move_to([-1.15, 0.25, 0])),
                  run_time=0.4)

        vals = [0.8, 0.35, 0.62, 0.45, 0.55, 0.48, 0.52, 0.505, 0.5, 0.498]
        pts = [ax.c2p(k + 0.6, v) for k, v in enumerate(vals)]
        dots = VGroup(*[Dot(p, radius=0.056, color=GREEN) for p in pts])
        curve = VMobject(color=GREEN, stroke_width=2.4)
        curve.set_points_as_corners(pts)
        self.play(Create(curve), *[FadeIn(d) for d in dots], run_time=1.6)
        self.wait(0.4)

        rows = [
            ("频率会波动，概率是稳定值", GOLD),
            ("大量重复试验：频率 ≈ 概率", GREEN),
            ("游戏公平：双方获胜概率相等", BLUE),
        ]
        y = 2.2
        for s, col in rows:
            t = txt(s, size=22, color=col).move_to([3.5, y, 0])
            if t.width > 6.4:
                t.scale_to_fit_width(6.4)
            self.play(FadeIn(t, shift=RIGHT * 0.04), run_time=0.8)
            y -= 0.85
        self.wait(0.4)

        box = label_box("频率不是概率，只是估计", size=21, color=RED)
        box.move_to([3.5, -1.8, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.0)
        self.wait(9.5)
        self.finish_section()

    # ---------------- 6. 易错点 ---------------- 20.5
    def scene_traps(self):
        self.section(6, "四个易错点")

        rows = [
            ("① 求中位数忘了排序", "先从小到大排好"),
            ("② 扇形图用数量算圆心角", "要用占比 × 360°"),
            ("③ 列举时有序当无序", "重复计数会算错"),
            ("④ 把频率当概率", "频率只是估计"),
        ]
        y = 1.85
        for a, b in rows:
            ta = txt(a, size=22, color=RED).move_to([-2.7, y, 0])
            tb = txt(b, size=20, color=DIM).move_to([3.55, y, 0])
            self.play(FadeIn(ta, shift=RIGHT * 0.04), run_time=0.6)
            self.play(FadeIn(tb, shift=RIGHT * 0.04), run_time=0.6)
            y -= 0.86
        self.wait(0.8)

        box = label_box("先分类，再列举，不重不漏", size=26, color=GOLD)
        box.move_to([0, -2.45, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.1)
        self.wait(6.5)
        self.finish_section()

    def construct(self):
        self.scene_intro()
        self.clear_stage()
        self.scene_collect()
        self.clear_stage()
        self.scene_charts()
        self.clear_stage()
        self.scene_stats()
        self.clear_stage()
        self.scene_prob()
        self.clear_stage()
        self.scene_freq()
        self.clear_stage()
        self.scene_traps()
        self.clear_stage(0.8)