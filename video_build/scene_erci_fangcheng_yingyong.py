# -*- coding: utf-8 -*-
"""一元二次方程的应用与判别式：增长率、面积、利润、含参数。九年级上。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


def P(x, y):
    return np.array([float(x), float(y), 0.0])


def rect(x0, y0, w, h, color=CHALK, width=2.8, fill=0.06) -> Rectangle:
    return Rectangle(width=w, height=h, color=color, stroke_width=width,
                     fill_color=color, fill_opacity=fill).move_to([x0 + w / 2, y0 + h / 2, 0])


class ErciFangchengYingyongScene(NarratedScene):
    lesson = "erci-fangcheng-yingyong"

    def clear_stage(self, run_time: float = 0.5):
        keep = {id(self._track), id(self._fill)}
        junk = [m for m in self.mobjects if id(m) not in keep]
        if junk:
            self.play(*[FadeOut(m) for m in junk], run_time=run_time)
        self.cur_title = None
        self.cur_sub = None

    # ---------------- 0. 三类问题 ---------------- 25.8
    def scene_intro(self):
        self.section(0, "三类最常见的问题")

        chips = [
            ("增长率", "两年翻了多少", -4.4, GOLD),
            ("面积问题", "长宽各是多少", 0.0, GREEN),
            ("销售利润", "降价多少钱", 4.4, BLUE),
        ]
        for name, note, cx, col in chips:
            t = label_box(name, size=24, color=col).move_to([cx, 2.2, 0])
            self.play(FadeIn(t, scale=0.97), run_time=0.8)
            n = txt(note, size=21, color=DIM).move_to([cx, 1.5, 0])
            self.play(FadeIn(n, shift=UP * 0.04), run_time=0.7)
        self.wait(1.1)

        l1 = txt("列方程之前，先找等量关系", size=28, color=CHALK).move_to([0, 0.5, 0])
        self.play(FadeIn(l1, shift=UP * 0.05), run_time=0.95)
        self.wait(0.9)

        b1 = label_box("总利润 = 每件利润 × 销量", size=26, color=GOLD)
        b1.move_to([0, -0.75, 0])
        self.play(FadeIn(b1, scale=0.97), run_time=1.0)
        self.wait(0.9)

        note = txt("解出来的根，还要回到题目里检验", size=24, color=RED)
        note.move_to([0, -1.95, 0])
        self.play(FadeIn(note, shift=UP * 0.04), run_time=0.95)
        self.wait(9.0)
        self.finish_section()

    # ---------------- 1. 增长率 ---------------- 35.6
    def scene_growth(self):
        self.section(1, "增长率：连乘两次")

        boxes = [
            ("第一年", "100 万件", -4.7, CHALK),
            ("第二年", "100(1+x)", 0.0, CHALK),
            ("第三年", "121 万件", 4.7, GOLD),
        ]
        for name, val, cx, col in boxes:
            r = rect(cx - 1.55, 1.35, 3.1, 1.15, col, 2.2)
            t1 = txt(name, size=21, color=DIM).move_to([cx, 2.2, 0])
            t2 = txt(val, size=24, color=col).move_to([cx, 1.72, 0])
            self.play(Create(r), FadeIn(t1), FadeIn(t2), run_time=1.0)
        a1 = Arrow(P(-3.1, 1.92), P(-1.75, 1.92), color=GOLD, stroke_width=3,
                   buff=0, max_tip_length_to_length_ratio=0.2)
        a2 = Arrow(P(1.6, 1.92), P(2.95, 1.92), color=GOLD, stroke_width=3,
                   buff=0, max_tip_length_to_length_ratio=0.2)
        m1 = txt("×(1 + x)", size=22, color=GOLD).move_to([-2.42, 2.5, 0])
        m2 = txt("×(1 + x)", size=22, color=GOLD).move_to([2.28, 2.5, 0])
        self.play(GrowArrow(a1), GrowArrow(a2), run_time=1.0)
        self.play(FadeIn(m1), FadeIn(m2), run_time=0.7)
        self.wait(0.9)

        e1 = txt("100 (1 + x)² = 121", size=34, color=GOLD).move_to([0, 0.35, 0])
        self.play(FadeIn(e1, shift=UP * 0.04), run_time=1.0)
        self.wait(0.8)

        steps = [
            ("(1 + x)² = 1.21", CHALK),
            ("1 + x = ±1.1", CHALK),
            ("x = 0.1　或　x = −2.1（舍）", GREEN),
        ]
        y = -0.55
        for s, col in steps:
            t = txt(s, size=30, color=col).move_to([0, y, 0])
            self.play(FadeIn(t, shift=UP * 0.04), run_time=0.9)
            y -= 0.85
        self.wait(0.8)

        note = txt("增长率要写成一加 x，连乘两次就是平方", size=23, color=RED)
        note.move_to([0, -2.55, 0])
        self.play(FadeIn(note, shift=UP * 0.04), run_time=0.95)
        self.wait(13.0)
        self.finish_section()

    # ---------------- 2. 面积问题 ---------------- 32.2
    def scene_area(self):
        self.section(2, "面积问题：长比宽多 3 米")

        rc = rect(-6.3, -0.2, 3.3, 2.0, GREEN)
        self.play(Create(rc), run_time=1.0)
        wl = txt("宽 x", size=23, color=GREEN).move_to([-4.65, -0.72, 0])
        ll = txt("长 x + 3", size=23, color=GREEN).move_to([-4.65, 2.05, 0])
        ar = txt("面积 40 m²", size=22, color=DIM).move_to([-4.65, 0.85, 0])
        self.play(FadeIn(wl), FadeIn(ll), FadeIn(ar), run_time=1.0)
        self.wait(1.0)

        rows = [
            ("x (x + 3) = 40", CHALK),
            ("x² + 3x − 40 = 0", CHALK),
            ("(x + 8)(x − 5) = 0", GOLD),
            ("x = −8（舍）或 x = 5", GREEN),
        ]
        y = 1.72
        for s, col in rows:
            t = txt(s, size=27, color=col).move_to([3.1, y, 0])
            self.play(FadeIn(t, shift=UP * 0.04), run_time=0.85)
            y -= 0.82
        self.wait(1.0)

        res = txt("宽 5 米，长 8 米", size=29, color=GOLD).move_to([3.1, -1.75, 0])
        self.play(FadeIn(res, scale=0.97), run_time=1.0)
        self.wait(0.8)

        note = txt("宽度不能是负数，负根一定要舍去", size=23, color=RED)
        note.move_to([-2.0, -2.6, 0])
        self.play(FadeIn(note, shift=UP * 0.04), run_time=0.95)
        self.wait(9.5)
        self.finish_section()

    # ---------------- 3. 利润问题 ---------------- 38.7
    def scene_profit(self):
        self.section(3, "利润问题：每件利润 × 销量")

        b = label_box("总利润 = 每件利润 × 销量", size=25, color=GOLD)
        b.move_to([0, 2.45, 0])
        self.play(FadeIn(b, scale=0.97), run_time=1.0)
        self.wait(0.7)

        l1 = txt("原来：每件利润 40 元，每天卖 20 件", size=24, color=CHALK)
        l1.move_to([0, 1.45, 0])
        self.play(FadeIn(l1, shift=UP * 0.04), run_time=0.9)
        l2 = txt("降价 x 元：每件利润 40 − x，每天卖 20 + 2x", size=24, color=GOLD)
        l2.move_to([0, 0.7, 0])
        self.play(FadeIn(l2, shift=UP * 0.04), run_time=0.9)
        self.wait(1.0)

        e1 = txt("(40 − x)(20 + 2x) = 1200", size=32, color=CHALK).move_to([0, -0.25, 0])
        self.play(FadeIn(e1, shift=UP * 0.04), run_time=0.95)
        e2 = txt("x² − 30x + 200 = 0", size=30, color=CHALK).move_to([0, -1.05, 0])
        self.play(FadeIn(e2, shift=UP * 0.04), run_time=0.95)
        e3 = txt("x = 10　或　x = 20", size=32, color=GREEN).move_to([0, -1.9, 0])
        self.play(FadeIn(e3, scale=0.97), run_time=1.0)
        self.wait(0.8)

        note = txt("要「让顾客更优惠」，就取降 20 元", size=23, color=RED)
        note.move_to([0, -2.7, 0])
        self.play(FadeIn(note, shift=UP * 0.04), run_time=0.95)
        self.wait(16.0)
        self.finish_section()

    # ---------------- 4. 含参数的判别式 ---------------- 33.5
    def scene_param(self):
        self.section(4, "含参数：两个不相等实根")

        head = txt("(m − 1)x² + 2x + 1 = 0 有两个不相等实根", size=25, color=CHALK)
        head.move_to([0, 2.3, 0])
        self.play(FadeIn(head, shift=UP * 0.04), run_time=1.0)
        self.wait(0.8)

        c1 = txt("① 二次项系数不为零：m − 1 ≠ 0", size=26, color=GOLD)
        c1.move_to([0, 1.15, 0])
        self.play(FadeIn(c1, shift=UP * 0.04), run_time=0.9)
        r1 = txt("得  m ≠ 1", size=26, color=CHALK).move_to([0, 0.45, 0])
        self.play(FadeIn(r1, shift=UP * 0.04), run_time=0.8)
        self.wait(0.8)

        c2 = txt("② 判别式大于零：Δ = 4 − 4(m − 1) > 0", size=26, color=GOLD)
        c2.move_to([0, -0.45, 0])
        self.play(FadeIn(c2, shift=UP * 0.04), run_time=0.9)
        r2 = txt("4 − 4m + 4 > 0　→　m < 2", size=26, color=CHALK)
        r2.move_to([0, -1.15, 0])
        self.play(FadeIn(r2, shift=UP * 0.04), run_time=0.85)
        self.wait(1.0)

        box = label_box("m < 2 且 m ≠ 1", size=30, color=GREEN)
        box.move_to([0, -2.15, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.1)
        self.wait(0.8)

        warn = txt("两个条件缺一不可，m ≠ 1 最容易漏", size=22, color=RED)
        warn.move_to([0, -2.75, 0])
        self.play(FadeIn(warn, shift=UP * 0.04), run_time=0.9)
        self.wait(11.5)
        self.finish_section()

    # ---------------- 5. 证明总有实根 ---------------- 28.2
    def scene_proof(self):
        self.section(5, "证明：判别式总不小于零")

        head = txt("证明 x² − (k + 2)x + 2k = 0 总有实数根", size=26, color=CHALK)
        head.move_to([0, 2.3, 0])
        self.play(FadeIn(head, shift=UP * 0.04), run_time=1.0)
        self.wait(0.8)

        rows = [
            ("Δ = (k + 2)² − 4 · 1 · 2k", CHALK, 30),
            ("= k² + 4k + 4 − 8k", CHALK, 30),
            ("= k² − 4k + 4", CHALK, 30),
            ("= (k − 2)²", GOLD, 32),
        ]
        y = 1.35
        for s, col, sz in rows:
            t = txt(s, size=sz, color=col).move_to([0, y, 0])
            self.play(FadeIn(t, shift=UP * 0.04), run_time=0.85)
            y -= 0.78
        self.wait(1.0)

        note = txt("平方一定大于等于零，所以 Δ ≥ 0", size=25, color=GREEN)
        note.move_to([0, -1.55, 0])
        self.play(FadeIn(note, shift=UP * 0.04), run_time=0.95)
        self.wait(0.8)

        box = label_box("判别式配成平方，方程总有实根", size=25, color=GOLD)
        box.move_to([0, -2.5, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.05)
        self.wait(9.5)
        self.finish_section()

    # ---------------- 6. 四个易错点 ---------------- 26.4
    def scene_traps(self):
        self.section(6, "四个易错点")

        rows = [
            ("① 增长率写成一加 x 的平方", "不是 x 的平方"),
            ("② 降价后销量加括号", "写成 20 + 2x"),
            ("③ 含参数题别忘 a ≠ 0", "二次项系数不为零"),
            ("④ 求出根要检验取舍", "负数、不合理的一律舍去"),
        ]
        y = 1.85
        for a, b in rows:
            ta = txt(a, size=23, color=RED).move_to([-2.8, y, 0])
            self.play(FadeIn(ta, shift=RIGHT * 0.04), run_time=0.65)
            tb = txt(b, size=21, color=DIM).move_to([3.75, y, 0])
            self.play(FadeIn(tb, shift=RIGHT * 0.04), run_time=0.65)
            y -= 0.86
        self.wait(1.0)

        box = label_box("先列等量关系，再解方程，最后检验", size=26, color=GOLD)
        box.move_to([0, -2.45, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.1)
        self.wait(9.0)
        self.finish_section()

    def construct(self):
        self.scene_intro()
        self.clear_stage()
        self.scene_growth()
        self.clear_stage()
        self.scene_area()
        self.clear_stage()
        self.scene_profit()
        self.clear_stage()
        self.scene_param()
        self.clear_stage()
        self.scene_proof()
        self.clear_stage()
        self.scene_traps()
        self.clear_stage(0.8)