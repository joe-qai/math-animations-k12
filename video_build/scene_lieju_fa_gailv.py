# -*- coding: utf-8 -*-
"""列举法求概率：直接列举、列表、树状图。九年级上。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


def P(x, y):
    return np.array([float(x), float(y), 0.0])


def frac_cn(num: str, den: str, color=GOLD, size: int = 24,
            lw: float = 2.2, gap: float = 0.12) -> VGroup:
    """中文分式：分子 / 分母。"""
    n = txt(num, size=size, color=color)
    d = txt(den, size=size, color=color)
    w = max(n.width, d.width) + 0.24
    line = Line(P(-w / 2, 0), P(w / 2, 0), color=color, stroke_width=lw)
    n.next_to(line, UP, buff=gap)
    d.next_to(line, DOWN, buff=gap)
    return VGroup(n, line, d)


class LiejuFaGailvScene(NarratedScene):
    lesson = "lieju-fa-gailv"

    def clear_stage(self, run_time: float = 0.5):
        keep = {id(self._track), id(self._fill)}
        junk = [m for m in self.mobjects if id(m) not in keep]
        if junk:
            self.play(*[FadeOut(m) for m in junk], run_time=run_time)
        self.cur_title = None
        self.cur_sub = None

    # ---------------- 0. 什么是概率 ---------------- 29.8
    def scene_intro(self):
        self.section(0, "先数一数，再求概率")

        chips = [
            ("抛硬币", "正、反两种", -4.4, GOLD),
            ("掷骰子", "一到六，六种", 0.0, GREEN),
            ("摸球", "三红两白", 4.4, BLUE),
        ]
        for name, note, cx, col in chips:
            b = label_box(name, size=24, color=col).move_to([cx, 2.2, 0])
            n = txt(note, size=21, color=DIM).move_to([cx, 1.5, 0])
            self.play(FadeIn(b, scale=0.97), run_time=0.7)
            self.play(FadeIn(n, shift=UP * 0.04), run_time=0.6)
        self.wait(0.8)

        f = VGroup(
            txt("P =", size=34, color=GOLD),
            frac_cn("事件包含的结果数", "所有等可能的结果数", GOLD, 24),
        ).arrange(RIGHT, buff=0.24).move_to([0, 0.05, 0])
        self.play(FadeIn(f, scale=0.98), run_time=1.2)
        self.wait(0.9)

        d = txt("结果事先不能确定，但可能性有大小", size=24, color=CHALK)
        d.move_to([0, -1.5, 0])
        self.play(FadeIn(d, shift=UP * 0.04), run_time=0.95)

        box = label_box("每种结果必须等可能，且不重复、不遗漏", size=23, color=RED)
        box.move_to([0, -2.6, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.05)
        self.wait(14.0)
        self.finish_section()

    # ---------------- 1. 直接列举 ---------------- 26.2
    def scene_direct(self):
        self.section(1, "直接列举：结果少时")

        # 左：硬币
        c1 = Circle(radius=0.62, color=GOLD, stroke_width=2.4).move_to([-5.2, 1.35, 0])
        t1 = txt("正", size=28, color=GOLD).move_to(c1)
        c2 = Circle(radius=0.62, color=GOLD, stroke_width=2.4).move_to([-3.7, 1.35, 0])
        t2 = txt("反", size=28, color=GOLD).move_to(c2)
        self.play(Create(c1), FadeIn(t1), run_time=0.8)
        self.play(Create(c2), FadeIn(t2), run_time=0.8)

        h1 = txt("抛一枚硬币：2 种等可能结果", size=23, color=CHALK)
        h1.move_to([-4.45, 2.3, 0])
        self.play(FadeIn(h1, shift=UP * 0.04), run_time=0.8)

        p1 = txt("P(正面) = 1/2", size=30, color=GOLD).move_to([-4.45, 0.2, 0])
        self.play(FadeIn(p1, scale=0.98), run_time=0.9)
        self.wait(0.9)

        # 右：骰子六个面
        h2 = txt("掷一枚骰子：6 种等可能结果", size=23, color=CHALK)
        h2.move_to([2.9, 2.3, 0])
        self.play(FadeIn(h2, shift=UP * 0.04), run_time=0.8)

        nums = []
        for i in range(6):
            x = 0.15 + i * 1.15
            r = RoundedRectangle(corner_radius=0.08, width=0.92, height=0.92,
                                 color=CHALK, stroke_width=2.2)
            r.move_to([x, 1.2, 0])
            t = txt(str(i + 1), size=26, color=CHALK).move_to(r)
            nums.append((r, t, i + 1))
            self.play(Create(r), FadeIn(t), run_time=0.35)
        self.wait(0.5)

        for r, t, v in nums:
            if v % 2 == 0:
                self.play(r.animate.set_color(GREEN).set_fill(GREEN, 0.12),
                          t.animate.set_color(GREEN), run_time=0.3)
        self.wait(0.6)

        p2 = txt("P(偶数) = 3/6 = 1/2", size=30, color=GREEN).move_to([2.9, -0.35, 0])
        self.play(FadeIn(p2, scale=0.98), run_time=0.9)
        self.wait(0.8)

        note = txt("列举要写全：不重复、不遗漏", size=23, color=RED)
        note.move_to([0, -1.9, 0])
        self.play(FadeIn(note, shift=UP * 0.04), run_time=0.95)
        self.wait(9.0)
        self.finish_section()

    # ---------------- 2. 列表法 ---------------- 30.3
    def scene_table(self):
        self.section(2, "列表法：两枚骰子")

        head = txt("同时掷两枚骰子，求点数和为 7 的概率", size=24, color=CHALK)
        head.move_to([-3.6, 2.55, 0])
        self.play(FadeIn(head, shift=UP * 0.04), run_time=0.9)

        size = 0.5
        ox, oy = -5.55, 1.85
        grid = VGroup()
        hits = []
        for i in range(6):
            for j in range(6):
                v = (i + 1) + (j + 1)
                cell = Square(side_length=size, stroke_width=1.4)
                cell.move_to([ox + j * size + size / 2, oy - i * size - size / 2, 0])
                t = txt(str(v), size=16, color=CHALK).move_to(cell)
                grid.add(cell, t)
                if v == 7:
                    hits.append((cell, t))
        grid.set_color(DIM)
        self.play(FadeIn(grid), run_time=1.4)
        self.wait(0.7)

        for cell, t in hits:
            self.play(cell.animate.set_color(GOLD).set_fill(GOLD, 0.22),
                      t.animate.set_color(GOLD).scale(1.1), run_time=0.22)
        self.wait(0.8)

        rows = [
            ("第一枚 6 种，第二枚 6 种", CHALK),
            ("一共 6 × 6 = 36 种", CHALK),
            ("和是 7 的有 6 种", GOLD),
            ("P = 6/36 = 1/6", GOLD),
        ]
        y = 2.0
        for s, col in rows:
            t = txt(s, size=25, color=col).move_to([3.3, y, 0])
            self.play(FadeIn(t, shift=UP * 0.04), run_time=0.8)
            y -= 0.82
        self.wait(0.8)

        note = txt("两枚骰子要当成不同的：(1,2) 与 (2,1) 算两种", size=21, color=RED)
        note.move_to([0, -2.55, 0])
        self.play(FadeIn(note, shift=UP * 0.04), run_time=0.95)
        self.wait(11.0)
        self.finish_section()

    # ---------------- 3. 树状图 ---------------- 28.4
    def scene_tree(self):
        self.section(3, "树状图：分步完成")

        head = txt("袋中两红一白，不放回地摸两次", size=24, color=CHALK)
        head.move_to([-1.2, 2.5, 0])
        self.play(FadeIn(head, shift=UP * 0.04), run_time=0.9)

        root = P(-6.1, 0.1)
        self.play(Create(Dot(root, radius=0.07, color=CHALK)), run_time=0.5)

        lvl1 = [("红", -1.35, RED), ("红", 0.1, RED), ("白", 1.55, BLUE)]
        n1 = []
        for name, y, col in lvl1:
            node = P(-4.35, y)
            ln = Line(root, node, color=col, stroke_width=2.2)
            d = Dot(node, radius=0.055, color=col)
            t = txt(name, size=20, color=col).move_to(node + LEFT * 0.26)
            n1.append((node, col, name))
            self.play(Create(ln), FadeIn(d), FadeIn(t), run_time=0.5)

        self.wait(0.6)

        leaves = []
        for idx, (node, col, name) in enumerate(n1):
            rest = [("红", RED), ("白", BLUE)] if name == "红" else [("红", RED), ("红", RED)]
            for k, (nm, c2) in enumerate(rest):
                y = node[1] + (0.42 if k == 0 else -0.42)
                leaf = P(-2.45, y)
                ln = Line(node, leaf, color=c2, stroke_width=2.0)
                t = txt(nm, size=18, color=c2).move_to(leaf + RIGHT * 0.26)
                leaves.append((leaf, name, nm))
                self.play(Create(ln), FadeIn(t), run_time=0.35)

        self.wait(0.8)

        rows = [
            ("第一次 3 种，第二次 2 种", CHALK),
            ("一共 3 × 2 = 6 条路径", CHALK),
            ("两次都是红球：2 条", GOLD),
            ("P = 2/6 = 1/3", GOLD),
        ]
        y = 1.9
        for s, col in rows:
            t = txt(s, size=24, color=col).move_to([3.5, y, 0])
            self.play(FadeIn(t, shift=UP * 0.04), run_time=0.8)
            y -= 0.82
        self.wait(0.8)

        note = txt("分几步，就画几层；路径数就是总结果数", size=22, color=RED)
        note.move_to([3.5, -1.75, 0])
        self.play(FadeIn(note, shift=UP * 0.04), run_time=0.95)
        self.wait(11.5)
        self.finish_section()

    # ---------------- 4. 放回与不放回 ---------------- 24.0
    def scene_replace(self):
        self.section(4, "放回，还是不放回")

        t1 = txt("放回", size=30, color=GOLD).move_to([-3.6, 2.0, 0])
        t2 = txt("不放回", size=30, color=GREEN).move_to([3.6, 2.0, 0])
        self.play(FadeIn(t1), FadeIn(t2), run_time=0.9)

        r1 = [
            ("第一次：3 种", CHALK),
            ("第二次：还是 3 种", CHALK),
            ("一共 3 × 3 = 9 种", GOLD),
        ]
        y = 0.95
        for s, col in r1:
            t = txt(s, size=25, color=col).move_to([-3.6, y, 0])
            self.play(FadeIn(t, shift=UP * 0.04), run_time=0.8)
            y -= 0.85

        r2 = [
            ("第一次：3 种", CHALK),
            ("第二次：只剩 2 种", CHALK),
            ("一共 3 × 2 = 6 种", GREEN),
        ]
        y = 0.95
        for s, col in r2:
            t = txt(s, size=25, color=col).move_to([3.6, y, 0])
            self.play(FadeIn(t, shift=UP * 0.04), run_time=0.8)
            y -= 0.85
        self.wait(0.9)

        line = Line(P(0, 2.35), P(0, -1.4), color=DIM, stroke_width=1.6)
        self.play(Create(line), run_time=0.6)
        self.wait(0.6)

        box = label_box("不放回：每走一步，剩下的就少一个", size=23, color=RED)
        box.move_to([0, -2.35, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.05)
        self.wait(8.5)
        self.finish_section()

    # ---------------- 5. 公平与频率 ---------------- 25.3
    def scene_fair(self):
        self.section(5, "公平，还是不公平")

        f1 = txt("两人获胜概率相等 → 游戏公平", size=28, color=GOLD).move_to([0, 2.0, 0])
        f2 = txt("不相等 → 不公平，要改规则", size=26, color=CHALK).move_to([0, 1.15, 0])
        self.play(FadeIn(f1, shift=UP * 0.04), run_time=0.9)
        self.play(FadeIn(f2, shift=UP * 0.04), run_time=0.9)
        self.wait(0.9)

        h = txt("频率与概率", size=28, color=BLUE).move_to([0, 0.0, 0])
        self.play(FadeIn(h, scale=0.98), run_time=0.8)
        self.wait(0.5)

        rows = [
            ("频率 = 发生次数 ÷ 总次数，会上下波动", CHALK),
            ("概率是一个固定的数", GOLD),
            ("试验次数越多，频率越接近概率", GREEN),
        ]
        y = -0.95
        for s, col in rows:
            t = txt(s, size=24, color=col).move_to([0, y, 0])
            self.play(FadeIn(t, shift=UP * 0.04), run_time=0.85)
            y -= 0.82
        self.wait(0.9)

        box = label_box("概率算出来就固定，频率要试了才知道", size=23, color=RED)
        box.move_to([0, -2.75, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.05)
        self.wait(8.0)
        self.finish_section()

    # ---------------- 6. 四个易错点 ---------------- 25.6
    def scene_traps(self):
        self.section(6, "四个易错点")

        rows = [
            ("① 列举漏结果、或重复计", "先写全，再数个数"),
            ("② 没确认是否等可能", "不等可能不能直接数"),
            ("③ 放回与不放回弄混", "不放回每步少一个"),
            ("④ 把频率当成概率", "概率固定，频率波动"),
        ]
        y = 1.85
        for a, b in rows:
            ta = txt(a, size=23, color=RED).move_to([-2.6, y, 0])
            tb = txt(b, size=21, color=DIM).move_to([3.6, y, 0])
            self.play(FadeIn(ta, shift=RIGHT * 0.04), run_time=0.65)
            self.play(FadeIn(tb, shift=RIGHT * 0.04), run_time=0.65)
            y -= 0.86
        self.wait(1.0)

        box = label_box("写全结果，数清个数，再做除法", size=26, color=GOLD)
        box.move_to([0, -2.45, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.1)
        self.wait(10.5)
        self.finish_section()

    def construct(self):
        self.scene_intro()
        self.clear_stage()
        self.scene_direct()
        self.clear_stage()
        self.scene_table()
        self.clear_stage()
        self.scene_tree()
        self.clear_stage()
        self.scene_replace()
        self.clear_stage()
        self.scene_fair()
        self.clear_stage()
        self.scene_traps()
        self.clear_stage(0.8)