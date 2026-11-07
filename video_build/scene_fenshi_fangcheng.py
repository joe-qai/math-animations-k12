# -*- coding: utf-8 -*-
"""分式方程：定义、去分母解法、增根与检验、无解情形、工程应用。八年级。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


def P(x, y):
    return np.array([float(x), float(y), 0.0])


def frac(num: str, den: str, center, size: int = 40, color: str = CHALK) -> VGroup:
    """竖排分式：分子、分数线、分母。"""
    off = 0.0074 * size
    top = txt(num, size=size, color=color)
    bot = txt(den, size=size, color=color)
    w = max(top.width, bot.width) + 0.3
    line = Line([-w / 2, 0, 0], [w / 2, 0, 0], color=color, stroke_width=3)
    top.move_to([0, off, 0])
    bot.move_to([0, -off, 0])
    return VGroup(top, line, bot).move_to([center[0], center[1], 0])


class FenshiFangchengScene(NarratedScene):
    lesson = "fenshi_fangcheng"

    def clear_stage(self, run_time: float = 0.5):
        keep = {id(self._track), id(self._fill)}
        junk = [m for m in self.mobjects if id(m) not in keep]
        if junk:
            self.play(*[FadeOut(m) for m in junk], run_time=run_time)
        self.cur_title = None
        self.cur_sub = None

    # ---------------- 0. 未知数跑到了分母里 ---------------- 24.2
    def scene_intro(self):
        self.section(0, "未知数跑到了分母里")

        lh = txt("整式方程", size=26, color=DIM)
        lh.move_to([-4.0, 2.35, 0])
        self.play(FadeIn(lh), run_time=0.6)
        e1 = txt("2x + 3 = 7", size=36, color=CHALK)
        e1.move_to([-4.0, 1.5, 0])
        self.play(FadeIn(e1, shift=UP * 0.05), run_time=0.8)
        n1 = txt("未知数在分子", size=23, color=DIM)
        n1.move_to([-4.0, 0.85, 0])
        self.play(FadeIn(n1), run_time=0.7)

        rh = txt("分式方程", size=26, color=GOLD)
        rh.move_to([3.0, 2.35, 0])
        self.play(FadeIn(rh), run_time=0.6)
        f1 = frac("2", "x", [1.5, 1.45, 0], 40, CHALK)
        eq = txt("=", size=32, color=DIM)
        eq.move_to([2.55, 1.45, 0])
        t3 = txt("3", size=40, color=CHALK)
        t3.move_to([3.35, 1.45, 0])
        f2 = frac("3", "x − 1", [4.9, 1.45, 0], 36, CHALK)
        eq2 = txt("=", size=30, color=DIM)
        eq2.move_to([5.85, 1.45, 0])
        f3 = frac("2", "x", [6.5, 1.45, 0], 32, CHALK)
        self.play(FadeIn(f1, scale=0.94), FadeIn(eq), FadeIn(t3), run_time=0.9)
        self.play(FadeIn(f2, scale=0.94), FadeIn(eq2), FadeIn(f3, scale=0.94),
                  run_time=1.0)
        n2 = txt("未知数在分母", size=23, color=GOLD)
        n2.move_to([4.0, 0.55, 0])
        self.play(FadeIn(n2), run_time=0.7)

        b1 = SurroundingRectangle(f1[2], color=BLUE, buff=0.12, stroke_width=2.4)
        b2 = SurroundingRectangle(f2[2], color=BLUE, buff=0.12, stroke_width=2.4)
        self.play(Create(b1), Create(b2), run_time=0.9)

        d = label_box("分母里含未知数的方程，叫分式方程", size=28, color=GOLD)
        d.move_to([0, -0.55, 0])
        self.play(FadeIn(d, scale=0.97), run_time=1.0)

        w = txt("先圈出使分母为 0 的 x：这些值不能当答案", size=25, color=CHALK)
        w.move_to([0, -1.65, 0])
        self.play(FadeIn(w, shift=UP * 0.05), run_time=0.9)

        w2 = VGroup(
            txt("2/x：x ≠ 0", size=24, color=RED),
            txt("3/(x − 1)：x ≠ 1", size=24, color=RED),
        ).arrange(RIGHT, buff=1.4).move_to([0, -2.5, 0])
        for m in w2:
            self.play(FadeIn(m, shift=UP * 0.05), run_time=0.7)

        self.wait(2.0)
        self.finish_section()

    # ---------------- 1. 去分母 ---------------- 24.4
    def scene_solve(self):
        self.section(1, "去分母：化整式方程")

        f0 = VGroup(
            frac("2", "x", [0, 0, 0], 42, CHALK),
            txt("=", size=34, color=DIM),
            txt("3", size=42, color=CHALK),
        ).arrange(RIGHT, buff=0.5).move_to([0, 2.05, 0])
        self.play(FadeIn(f0, shift=UP * 0.05), run_time=1.1)

        m = txt("两边同乘 x", size=27, color=GOLD)
        m.move_to([0, 1.05, 0])
        self.play(FadeIn(m, shift=UP * 0.05), run_time=0.9)

        r1 = VGroup(
            txt("2", size=36, color=CHALK),
            txt("=", size=32, color=DIM),
            txt("3x", size=36, color=CHALK),
        ).arrange(RIGHT, buff=0.45).move_to([0, 0.1, 0])
        self.play(FadeIn(r1, shift=UP * 0.05), run_time=0.9)

        r2 = VGroup(
            txt("x", size=36, color=CHALK),
            txt("=", size=32, color=DIM),
            frac("2", "3", [0, 0, 0], 36, GREEN),
        ).arrange(RIGHT, buff=0.4).move_to([0, -0.95, 0])
        self.play(FadeIn(r2, shift=UP * 0.05), run_time=1.0)

        chk = txt("检验：x = 2/3，原分母 x ≠ 0，成立", size=25, color=GREEN)
        chk.move_to([0, -1.95, 0])
        self.play(FadeIn(chk, shift=UP * 0.05), run_time=0.9)

        steps = VGroup(
            txt("① 去分母", size=24, color=GOLD),
            txt("② 解整式方程", size=24, color=GOLD),
            txt("③ 检验", size=24, color=RED),
        ).arrange(RIGHT, buff=1.1).move_to([0, -2.75, 0])
        self.play(FadeIn(steps, shift=UP * 0.05), run_time=1.0)

        self.wait(1.8)
        self.finish_section()

    # ---------------- 2. 增根从哪来 ---------------- 25.5
    def scene_extraneous(self):
        self.section(2, "增根：乘了个 0")

        h = txt("两边同乘的整式，有可能正好等于 0", size=27, color=CHALK)
        h.move_to([0, 2.45, 0])
        self.play(FadeIn(h, shift=UP * 0.05), run_time=0.9)

        ok = VGroup(
            txt("3 = 3", size=36, color=CHALK),
            txt("两边同乘 2", size=24, color=DIM),
            txt("6 = 6", size=36, color=GREEN),
        ).arrange(RIGHT, buff=0.7).move_to([-2.9, 1.3, 0])
        self.play(FadeIn(ok, shift=UP * 0.05), run_time=1.1)

        bad = VGroup(
            txt("3 = 3", size=36, color=CHALK),
            txt("两边同乘 0", size=24, color=DIM),
            txt("0 = 0", size=36, color=RED),
        ).arrange(RIGHT, buff=0.7).move_to([-2.9, 0.1, 0])
        self.play(FadeIn(bad, shift=UP * 0.05), run_time=1.1)

        tip = txt("乘 0 之后，什么都变得相等，信息就丢了", size=25, color=RED)
        tip.move_to([0, -0.85, 0])
        self.play(FadeIn(tip, shift=UP * 0.05), run_time=0.9)

        d = label_box("使公分母为 0 的根，叫增根，必须舍去", size=28, color=GOLD)
        d.move_to([0, -1.85, 0])
        self.play(FadeIn(d, scale=0.97), run_time=1.1)

        n = txt("所以检验不是可选项，是必做的一步", size=25, color=CHALK)
        n.move_to([0, -2.75, 0])
        self.play(FadeIn(n, shift=UP * 0.05), run_time=0.9)

        self.wait(1.8)
        self.finish_section()

    # ---------------- 3. 检验怎么做 ---------------- 24.1
    def scene_check(self):
        self.section(3, "检验：代回公分母")

        h = txt("把解出来的 x 代回最简公分母", size=27, color=CHALK)
        h.move_to([0, 2.4, 0])
        self.play(FadeIn(h, shift=UP * 0.05), run_time=0.9)

        box = label_box("最简公分母 = 0 ？", size=30, color=GOLD)
        box.move_to([0, 1.45, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.0)

        y1 = VGroup(
            txt("是 → 增根，舍去", size=27, color=RED),
            txt("原方程可能无解", size=23, color=DIM),
        ).arrange(DOWN, buff=0.3).move_to([-3.4, 0.1, 0])
        y2 = VGroup(
            txt("否 → 是原方程的根", size=27, color=GREEN),
            txt("写进答案", size=23, color=DIM),
        ).arrange(DOWN, buff=0.3).move_to([3.4, 0.1, 0])
        a1 = Arrow(P(-1.5, 1.3), P(-2.6, 0.75), color=RED, stroke_width=2.6,
                   max_tip_length_to_length_ratio=0.22)
        a2 = Arrow(P(1.5, 1.3), P(2.6, 0.75), color=GREEN, stroke_width=2.6,
                   max_tip_length_to_length_ratio=0.22)
        self.play(Create(a1), run_time=0.6)
        self.play(FadeIn(y1, shift=UP * 0.05), run_time=0.9)
        self.play(Create(a2), run_time=0.6)
        self.play(FadeIn(y2, shift=UP * 0.05), run_time=0.9)

        warn = txt("要代进原方程的分母，不能只看自己乘的式子", size=25, color=CHALK)
        warn.move_to([0, -1.5, 0])
        self.play(FadeIn(warn, shift=UP * 0.05), run_time=0.9)

        br = txt("漏掉这一步，等于白做", size=24, color=RED)
        br.move_to([0, -2.4, 0])
        self.play(FadeIn(br, shift=UP * 0.05), run_time=0.8)

        self.wait(1.8)
        self.finish_section()

    # ---------------- 4. 例题：x = 1 是增根 ---------------- 34.0
    def scene_ex_nosolution(self):
        self.section(4, "例题：解出增根，原方程无解")

        f0 = VGroup(
            frac("1", "x − 1", [0, 0, 0], 36, CHALK),
            txt("=", size=32, color=DIM),
            frac("2", "x² − 1", [0, 0, 0], 36, CHALK),
        ).arrange(RIGHT, buff=0.55).move_to([0, 2.2, 0])
        self.play(FadeIn(f0, shift=UP * 0.05), run_time=1.2)

        s1 = txt("分母分解：x² − 1 = (x + 1)(x − 1)", size=25, color=BLUE)
        s1.move_to([0, 1.3, 0])
        self.play(FadeIn(s1, shift=UP * 0.05), run_time=0.9)

        s2 = txt("最简公分母：(x + 1)(x − 1)", size=25, color=GOLD)
        s2.move_to([0, 0.65, 0])
        self.play(FadeIn(s2, shift=UP * 0.05), run_time=0.9)

        s3 = txt("两边同乘它：x + 1 = 2　→　x = 1", size=30, color=CHALK)
        s3.move_to([0, -0.2, 0])
        self.play(FadeIn(s3, shift=UP * 0.05), run_time=1.1)

        s4 = VGroup(
            txt("检验：x = 1 时，x − 1 = 0", size=27, color=RED),
            txt("公分母为 0，x = 1 是增根，舍去", size=27, color=RED),
        ).arrange(DOWN, buff=0.3).move_to([0, -1.25, 0])
        for m in s4:
            self.play(FadeIn(m, shift=UP * 0.05), run_time=0.9)

        res = label_box("结论：原方程无解", size=30, color=GREEN)
        res.move_to([0, -2.45, 0])
        self.play(FadeIn(res, scale=0.97), run_time=1.1)

        self.wait(2.2)
        self.finish_section()

    # ---------------- 5. 工程问题 ---------------- 29.3
    def scene_application(self):
        self.section(5, "应用：工程问题")

        h = VGroup(
            txt("甲单独做 x 天，乙单独做 x + 3 天", size=26, color=CHALK),
            txt("两人合作 2 天完成，求 x", size=26, color=CHALK),
        ).arrange(DOWN, buff=0.3).move_to([0, 2.35, 0])
        for m in h:
            self.play(FadeIn(m, shift=UP * 0.05), run_time=0.8)

        eq = VGroup(
            frac("2", "x", [0, 0, 0], 36, GOLD),
            txt("+", size=30, color=DIM),
            frac("2", "x + 3", [0, 0, 0], 36, GOLD),
            txt("=", size=30, color=DIM),
            txt("1", size=36, color=GOLD),
        ).arrange(RIGHT, buff=0.42).move_to([0, 1.05, 0])
        self.play(FadeIn(eq, shift=UP * 0.05), run_time=1.3)

        note = txt("总工作量看作 1，甲每天做 1/x，乙每天做 1/(x+3)", size=24, color=DIM)
        note.move_to([0, 0.2, 0])
        self.play(FadeIn(note, shift=UP * 0.05), run_time=0.9)

        l1 = txt("去分母：2(x + 3) + 2x = x(x + 3)", size=26, color=CHALK)
        l1.move_to([0, -0.6, 0])
        self.play(FadeIn(l1, shift=UP * 0.05), run_time=0.9)

        l2 = txt("整理：x² − x − 6 = 0", size=28, color=CHALK)
        l2.move_to([0, -1.3, 0])
        self.play(FadeIn(l2, shift=UP * 0.05), run_time=0.9)

        l3 = VGroup(
            txt("因式分解：(x − 3)(x + 2) = 0", size=26, color=GREEN),
            txt("→", size=26, color=DIM),
            txt("x = 3 或 x = −2", size=26, color=GREEN),
        ).arrange(RIGHT, buff=0.45).move_to([0, -2.0, 0])
        self.play(FadeIn(l3, shift=UP * 0.05), run_time=1.1)

        l4 = txt("天数不能为负，x = −2 舍去；检验 x = 3 分母不为 0 → x = 3", size=23, color=GOLD)
        l4.move_to([0, -2.8, 0])
        self.play(FadeIn(l4, shift=UP * 0.05), run_time=1.0)

        self.wait(1.8)
        self.finish_section()

    # ---------------- 6. 例题与三个易错点 ---------------- 38.0
    def scene_ex(self):
        self.section(6, "例题与三个易错点")

        q = txt("解方程", size=27, color=CHALK)
        q.move_to([-5.6, 2.35, 0])
        self.play(FadeIn(q, shift=RIGHT * 0.05), run_time=0.6)
        f0 = VGroup(
            frac("2", "x − 2", [0, 0, 0], 34, CHALK),
            txt("=", size=30, color=DIM),
            frac("3", "x + 1", [0, 0, 0], 34, CHALK),
        ).arrange(RIGHT, buff=0.5).move_to([-1.5, 2.35, 0])
        self.play(FadeIn(f0, shift=UP * 0.05), run_time=1.1)

        l1 = txt("交叉相乘：2(x + 1) = 3(x − 2)", size=27, color=CHALK)
        l1.move_to([0, 1.25, 0])
        self.play(FadeIn(l1, shift=UP * 0.05), run_time=0.9)

        l2 = VGroup(
            txt("2x + 2 = 3x − 6", size=28, color=CHALK),
            txt("→", size=26, color=DIM),
            txt("x = 8", size=32, color=GREEN),
        ).arrange(RIGHT, buff=0.45).move_to([0, 0.45, 0])
        self.play(FadeIn(l2, shift=UP * 0.05), run_time=1.1)

        l3 = txt("检验：x = 8 时，分母 6 与 9 都不为 0，x = 8 是根", size=25, color=GREEN)
        l3.move_to([0, -0.4, 0])
        self.play(FadeIn(l3, shift=UP * 0.05), run_time=1.0)

        items = [
            ("不检验，把增根当答案", "必代公分母"),
            ("去分母漏乘不含分母的项", "每一项都要乘"),
            ("检验只算乘的式子", "代回原分母"),
        ]
        y = -1.55
        for bad_s, good_s in items:
            bad = txt(bad_s, size=24, color=RED).move_to([-3.1, y, 0])
            good = txt(good_s, size=23, color=GREEN).move_to([3.9, y, 0])
            cross = Line([bad.get_left()[0] - 0.07, y - 0.02, 0],
                         [bad.get_right()[0] + 0.07, y - 0.02, 0],
                         color=RED, stroke_width=2.2)
            self.play(FadeIn(bad, shift=RIGHT * 0.05), run_time=0.6)
            self.play(Create(cross), run_time=0.35)
            self.play(FadeIn(good, shift=RIGHT * 0.05), run_time=0.6)
            y -= 0.78

        self.wait(3.0)
        self.finish_section()

    def construct(self):
        self.scene_intro()
        self.clear_stage()
        self.scene_solve()
        self.clear_stage()
        self.scene_extraneous()
        self.clear_stage()
        self.scene_check()
        self.clear_stage()
        self.scene_ex_nosolution()
        self.clear_stage()
        self.scene_application()
        self.clear_stage()
        self.scene_ex()
        self.clear_stage(0.8)