# -*- coding: utf-8 -*-
"""方程与不等式应用：审设列解验答，一元一次、分式、一元二次与不等式方案。九年级下。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


def P(x, y):
    return np.array([float(x), float(y), 0.0])


class FangchengBudengshiYingyongScene(NarratedScene):
    lesson = "fangcheng-budengshi-yingyong"

    def clear_stage(self, run_time: float = 0.5):
        keep = {id(self._track), id(self._fill)}
        junk = [m for m in self.mobjects if id(m) not in keep]
        if junk:
            self.play(*[FadeOut(m) for m in junk], run_time=run_time)
        self.cur_title = None
        self.cur_sub = None

    # ---------------- 0. 三个生活场景 ---------------- 32.9
    def scene_intro(self):
        self.section(0, "三个生活场景")

        cols = [
            (-4.5, "买奖品", GOLD, ["钢笔 8 元，笔记本 5 元", "一共花了 130 元", "各买了几件？"], "8x + 5y = 130"),
            (0.0, "春游租车", GREEN, ["大车 45 座 400 元", "小车 30 座 300 元", "怎么租最省钱？"], "总费用最小"),
            (4.5, "苹果装箱", BLUE, ["大箱 40 个，小箱 25 个", "一共 800 个苹果", "怎么装正好装完？"], "40a + 25b = 800"),
        ]
        for cx, name, col, lines, expr in cols:
            h = txt(name, size=26, color=col).move_to([cx, 2.25, 0])
            self.play(FadeIn(h, shift=UP * 0.04), run_time=0.7)
            y = 1.45
            for s in lines:
                t = txt(s, size=19, color=CHALK).move_to([cx, y, 0])
                self.play(FadeIn(t, shift=UP * 0.04), run_time=0.55)
                y -= 0.62
            e = txt(expr, size=21, color=col).move_to([cx, -0.55, 0])
            self.play(FadeIn(e, scale=0.98), run_time=0.7)
        self.wait(0.8)

        d = txt("先找关系，再设未知数，把文字翻译成式子", size=26, color=CHALK)
        d.move_to([0, -1.55, 0])
        self.play(FadeIn(d, shift=UP * 0.04), run_time=0.95)
        box = label_box("相等关系写成方程，不等关系写成不等式", size=23, color=GOLD)
        box.move_to([0, -2.45, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.0)
        self.wait(14.0)
        self.finish_section()

    # ---------------- 1. 六步 ---------------- 31.4
    def scene_steps(self):
        self.section(1, "审、设、列、解、验、答")

        steps = [
            ("审", "读懂题，找已知和未知"),
            ("设", "设未知数，问什么设什么"),
            ("列", "找相等关系，写成方程"),
            ("解", "解方程，注意步骤"),
            ("验", "验方程，也验实际意义"),
            ("答", "写清单位和结论"),
        ]
        xs = [-4.4, 0.0, 4.4]
        ys = [2.05, 0.4]
        for i, (tag, body) in enumerate(steps):
            cx = xs[i % 3]
            cy = ys[i // 3]
            disc = Circle(radius=0.42, color=GOLD, stroke_width=2.2).move_to([cx, cy, 0])
            chip = txt(tag, size=32, color=GOLD).move_to(disc)
            self.play(Create(disc), FadeIn(chip, scale=0.95), run_time=0.7)
            b = txt(body, size=19, color=CHALK).move_to([cx, cy - 0.62, 0])
            self.play(FadeIn(b, shift=UP * 0.04), run_time=0.6)
        self.wait(0.8)

        note = txt("不等式应用只把等号换成不等号，答案取整数", size=24, color=GREEN)
        note.move_to([0, -1.15, 0])
        self.play(FadeIn(note, shift=UP * 0.04), run_time=0.95)
        box = label_box("第五步最容易被跳过", size=23, color=RED).move_to([0, -2.1, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.0)
        self.wait(13.5)
        self.finish_section()

    # ---------------- 2. 一元一次方程 ---------------- 29.8
    def scene_linear(self):
        self.section(2, "一元一次方程：追及问题")

        road = Line(P(-6.1, 0.95), P(6.1, 0.95), color=DIM, stroke_width=2.2)
        self.play(Create(road), run_time=0.7)
        a = Dot(P(-5.2, 0.95), radius=0.09, color=GOLD)
        b = Dot(P(-1.3, 0.95), radius=0.09, color=BLUE)
        self.play(FadeIn(a), FadeIn(b), run_time=0.6)
        self.play(FadeIn(txt("甲 4 km/h", size=21, color=GOLD).move_to([-5.2, 1.5, 0])), run_time=0.5)
        self.play(FadeIn(txt("乙 6 km/h", size=21, color=BLUE).move_to([-1.3, 1.5, 0])), run_time=0.5)
        note = txt("乙晚出发半小时，追上甲用多久？", size=20, color=DIM).move_to([2.6, 1.5, 0])
        self.play(FadeIn(note), run_time=0.7)
        self.wait(0.6)

        e1 = txt("路程相同：6t = 4(t + 0.5)", size=29, color=CHALK).move_to([0, -0.1, 0])
        self.play(FadeIn(e1, shift=UP * 0.04), run_time=1.0)
        e2 = txt("解得 t = 1，即 1 小时追上", size=27, color=GOLD).move_to([0, -0.95, 0])
        self.play(FadeIn(e2, shift=UP * 0.04), run_time=0.95)
        self.wait(0.7)

        rows = [
            ("工程：效率 = 工作量 ÷ 时间，总量看作 1", GREEN),
            ("销售：利润 = 售价 − 进价", BLUE),
            ("利润率 = 利润 ÷ 进价 × 100%", BLUE),
        ]
        y = -1.8
        for s, col in rows:
            t = txt(s, size=22, color=col).move_to([0, y, 0])
            self.play(FadeIn(t, shift=UP * 0.04), run_time=0.75)
            y -= 0.5
        self.wait(9.5)
        self.finish_section()

    # ---------------- 3. 分式方程 ---------------- 30.5
    def scene_frac(self):
        self.section(3, "分式方程：合作几天完成")

        rows = [
            ("甲单独 10 天完成 → 每天做 1/10", GOLD),
            ("乙单独 15 天完成 → 每天做 1/15", GREEN),
            ("两人合作 x 天完成 → 每天做 1/x", BLUE),
        ]
        y = 1.85
        for s, col in rows:
            t = txt(s, size=24, color=col).move_to([0, y, 0])
            self.play(FadeIn(t, shift=UP * 0.04), run_time=0.9)
            y -= 0.78
        self.wait(0.8)

        e1 = txt("x/10 + x/15 = 1", size=36, color=CHALK).move_to([0, -0.72, 0])
        self.play(FadeIn(e1, scale=0.98), run_time=1.0)
        e2 = txt("通分：3x + 2x = 30，x = 6", size=25, color=GOLD).move_to([0, -1.65, 0])
        self.play(FadeIn(e2, shift=UP * 0.04), run_time=0.95)
        self.wait(0.7)

        box = label_box("分式方程必须验根：分母不为零，也要合实际", size=22, color=RED)
        box.move_to([0, -2.6, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.0)
        self.wait(11.0)
        self.finish_section()

    # ---------------- 4. 一元二次方程 ---------------- 30.0
    def scene_quad(self):
        self.section(4, "一元二次方程：增长率与面积")

        h1 = txt("连续两次降价：100 元 → 81 元", size=25, color=GOLD).move_to([0, 2.15, 0])
        self.play(FadeIn(h1, shift=UP * 0.04), run_time=0.9)

        p1 = txt("原价 100", size=22, color=CHALK).move_to([-4.5, 1.25, 0])
        ar1 = Arrow(P(-3.3, 1.25), P(-1.5, 1.25), color=DIM, stroke_width=2.0, buff=0.1)
        p2 = txt("第一次降价", size=20, color=DIM).move_to([-2.4, 1.62, 0])
        ar2 = Arrow(P(-1.0, 1.25), P(0.8, 1.25), color=DIM, stroke_width=2.0, buff=0.1)
        p3 = txt("81", size=22, color=GREEN).move_to([1.5, 1.25, 0])
        self.play(FadeIn(p1), GrowArrow(ar1), FadeIn(p2), run_time=0.9)
        self.play(GrowArrow(ar2), FadeIn(p3), run_time=0.9)
        self.wait(0.6)

        e1 = txt("100(1 − x)² = 81", size=32, color=CHALK).move_to([0, 0.15, 0])
        self.play(FadeIn(e1, scale=0.98), run_time=1.0)
        e2 = txt("(1 − x)² = 0.81，1 − x = ±0.9", size=24, color=CHALK).move_to([0, -0.65, 0])
        self.play(FadeIn(e2, shift=UP * 0.04), run_time=0.9)
        e3 = txt("x₁ = 0.1 = 10%    x₂ = 1.9（舍去）", size=24, color=GOLD).move_to([0, -1.35, 0])
        self.play(FadeIn(e3, shift=UP * 0.04), run_time=0.9)
        self.wait(0.7)

        box = label_box("增长率带平方；面积类：长 × 宽，靠墙不围", size=21, color=RED)
        box.move_to([0, -2.5, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.0)
        self.wait(10.0)
        self.finish_section()

    # ---------------- 5. 不等式方案 ---------------- 29.2
    def scene_ineq(self):
        self.section(5, "不等式：取整数解")

        q = txt("不超过 1200 元，买 80 元和 50 元的奖品共 20 件", size=23, color=CHALK)
        q.move_to([0, 2.1, 0])
        self.play(FadeIn(q, shift=UP * 0.04), run_time=0.9)

        e1 = txt("80x + 50(20 − x) ≤ 1200", size=31, color=CHALK).move_to([0, 1.05, 0])
        self.play(FadeIn(e1, scale=0.98), run_time=1.0)
        e2 = txt("30x + 1000 ≤ 1200", size=27, color=CHALK).move_to([0, 0.25, 0])
        self.play(FadeIn(e2, shift=UP * 0.04), run_time=0.9)
        e3 = txt("x ≤ 6.67", size=29, color=GOLD).move_to([0, -0.55, 0])
        self.play(FadeIn(e3, shift=UP * 0.04), run_time=0.9)
        self.wait(0.7)

        key = txt("件数必须是整数 → 最多买 6 件", size=26, color=GREEN).move_to([0, -1.45, 0])
        self.play(FadeIn(key, shift=UP * 0.04), run_time=0.95)
        self.wait(0.6)

        box = label_box("方案题：每种方案分别算总费用再比较", size=22, color=RED)
        box.move_to([0, -2.45, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.0)
        self.wait(11.0)
        self.finish_section()

    # ---------------- 6. 易错点 ---------------- 24.8
    def scene_traps(self):
        self.section(6, "四个易错点")

        rows = [
            ("① 设未知数不带单位", "单位先统一，再代入"),
            ("② 增长率漏平方", "两次变化要平方"),
            ("③ 分式方程不验根", "增根不能当答案"),
            ("④ 忘了取整数解", "件数、人数取整数"),
        ]
        y = 1.85
        for a, b in rows:
            ta = txt(a, size=23, color=RED).move_to([-2.6, y, 0])
            tb = txt(b, size=21, color=DIM).move_to([3.6, y, 0])
            self.play(FadeIn(ta, shift=RIGHT * 0.04), run_time=0.65)
            self.play(FadeIn(tb, shift=RIGHT * 0.04), run_time=0.65)
            y -= 0.86
        self.wait(1.0)

        box = label_box("审、设、列、解、验、答", size=27, color=GOLD)
        box.move_to([0, -2.45, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.1)
        self.wait(10.0)
        self.finish_section()

    def construct(self):
        self.scene_intro()
        self.clear_stage()
        self.scene_steps()
        self.clear_stage()
        self.scene_linear()
        self.clear_stage()
        self.scene_frac()
        self.clear_stage()
        self.scene_quad()
        self.clear_stage()
        self.scene_ineq()
        self.clear_stage()
        self.scene_traps()
        self.clear_stage(0.8)