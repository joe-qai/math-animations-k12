# -*- coding: utf-8 -*-
"""大数的认识与万以内加减法：数位表、读写、比大小、竖式、验算。四年级上册。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


def digits_row(s: str, y: float, right_x: float, size: int = 54,
               color: str = CHALK) -> VGroup:
    """把数字逐位摆放，保证不同行按数位对齐。索引 0 是个位。"""
    pitch = size * 0.0078
    g = VGroup()
    for i, ch in enumerate(reversed(s)):
        g.add(txt(ch, size=size, color=color).move_to([right_x - i * pitch, y, 0]))
    return g


def op_symbol(ch: str, y: float, right_x: float, size: int = 50,
              color: str = BLUE, pitch_size: int = 54) -> Text:
    """竖式左边的运算符，贴在数字块的左侧。"""
    x = right_x - 3 * (pitch_size * 0.0078) - 0.62
    return txt(ch, size=size, color=color).move_to([x, y, 0])


class DashuJianfaScene(NarratedScene):
    lesson = "dashu-jianfa"

    def clear_stage(self, run_time: float = 0.5):
        keep = {id(self._track), id(self._fill)}
        junk = [m for m in self.mobjects if id(m) not in keep]
        if junk:
            self.play(*[FadeOut(m) for m in junk], run_time=run_time)
        self.cur_title = None
        self.cur_sub = None

    # ---------------- 0. 图书馆 ---------------- 12.3
    def scene_story(self):
        self.section(0, "图书馆有多少本书")

        # 左：三层书架
        shelf = VGroup()
        for i in range(3):
            y = 1.5 - i * 1.1
            shelf.add(Line([-5.2, y - 0.2, 0], [-2.4, y - 0.2, 0],
                           color=CHALK, stroke_width=3))
            for j in range(6):
                h = 0.5 + 0.12 * ((i + j) % 3)
                w = 0.3
                x = -5.05 + j * 0.44
                c = [GOLD, BLUE, GREEN][(i + j) % 3]
                shelf.add(Rectangle(width=w, height=h, color=c, stroke_width=1.4,
                                    fill_color=c, fill_opacity=0.45)
                          .move_to([x, y - 0.2 + h / 2, 0]))
        self.play(LaggedStart(*[FadeIn(m) for m in shelf], lag_ratio=0.02), run_time=1.5)

        s_lab = txt("学校图书馆", size=26, color=DIM).move_to([-3.8, -1.95, 0])
        self.play(FadeIn(s_lab), run_time=0.5)

        t1 = txt("原来 3865 本", size=30, color=CHALK).move_to([2.6, 1.75, 0])
        t2 = txt("又买 1240 本", size=30, color=BLUE).move_to([2.6, 0.95, 0])
        self.play(FadeIn(t1, shift=UP * 0.06), run_time=0.7)
        self.play(FadeIn(t2, shift=UP * 0.06), run_time=0.7)

        q = txt("现在一共多少本？", size=36, color=GOLD).move_to([2.6, -0.25, 0])
        self.play(FadeIn(q, shift=UP * 0.08), run_time=0.9)

        tip = txt("要算这道题，先认清大数", size=24, color=DIM).move_to([2.6, -1.35, 0])
        self.play(FadeIn(tip), run_time=0.6)
        self.finish_section()

    # ---------------- 1. 数位表 ---------------- 15.4
    def scene_places(self):
        self.section(1, "个十百千万：每级都是十进制")

        cols = [(-2.9, "万"), (-1.6, "千"), (-0.3, "百"), (1.0, "十"), (2.3, "个")]
        frame = Rectangle(width=6.5, height=1.7, color=CHALK, stroke_width=2.2)
        frame.move_to([-0.3, 1.2, 0])
        self.play(Create(frame), run_time=0.8)

        seps = VGroup()
        for x in (-2.25, -0.95, 0.35, 1.65):
            seps.add(Line([x, 0.35, 0], [x, 2.05, 0], color=DIM, stroke_width=1.6))
        hline = Line([-3.55, 1.05, 0], [2.95, 1.05, 0], color=DIM, stroke_width=1.6)
        self.play(Create(seps), Create(hline), run_time=0.8)

        labels = VGroup()
        for x, name in cols:
            labels.add(txt(name, size=30, color=GOLD).move_to([x, 1.55, 0]))
        self.play(LaggedStart(*[FadeIn(l) for l in labels], lag_ratio=0.12), run_time=1.0)

        ds = ["3", "8", "6", "5"]
        xs = [-1.6, -0.3, 1.0, 2.3]
        nums = VGroup()
        for x, ch in zip(xs, ds):
            nums.add(txt(ch, size=44, color=CHALK).move_to([x, 0.7, 0]))
        self.play(LaggedStart(*[FadeIn(n) for n in nums], lag_ratio=0.12), run_time=1.1)

        r1 = txt("相邻两个数位，进率都是 10", size=28, color=CHALK).move_to([-0.3, -0.35, 0])
        r2 = txt("10 个一千 = 1 个一万", size=32, color=GOLD).move_to([-0.3, -1.25, 0])
        r3 = txt("3865 读作：三千八百六十五", size=26, color=DIM).move_to([-0.3, -2.15, 0])
        self.play(FadeIn(r1, shift=UP * 0.06), run_time=0.7)
        self.play(FadeIn(r2, shift=UP * 0.06), run_time=0.7)
        self.play(FadeIn(r3, shift=UP * 0.06), run_time=0.7)
        self.finish_section()

    # ---------------- 2. 读数写数 ---------------- 14.4
    def scene_read(self):
        self.section(2, "读数写数：0 什么时候读")

        a = txt("3005", size=76, color=GOLD).move_to([-3.7, 1.45, 0])
        a1 = txt("三千零五", size=32, color=CHALK).move_to([-3.7, 0.35, 0])
        a2 = txt("中间的 0 要读", size=26, color=GOLD).move_to([-3.7, -0.5, 0])
        b = txt("3050", size=76, color=BLUE).move_to([2.6, 1.45, 0])
        b1 = txt("三千零五十", size=32, color=CHALK).move_to([2.6, 0.35, 0])
        b2 = txt("末尾的 0 不读", size=26, color=GOLD).move_to([2.6, -0.5, 0])

        self.play(Write(a), run_time=0.9)
        self.play(FadeIn(a1, shift=UP * 0.06), run_time=0.7)
        self.play(FadeIn(a2, shift=UP * 0.06), run_time=0.6)
        self.play(Write(b), run_time=0.9)
        self.play(FadeIn(b1, shift=UP * 0.06), run_time=0.7)
        self.play(FadeIn(b2, shift=UP * 0.06), run_time=0.6)

        note = txt("哪一位一个单位也没有，就用 0 占位", size=28, color=GREEN)
        note.move_to([-0.4, -1.6, 0])
        self.play(FadeIn(note, shift=UP * 0.08), run_time=0.8)

        tip = txt("写数先看数位，再补 0", size=25, color=DIM).move_to([-0.4, -2.35, 0])
        self.play(FadeIn(tip, shift=UP * 0.06), run_time=0.7)
        self.finish_section()

    # ---------------- 3. 比大小 ---------------- 9.7
    def scene_compare(self):
        self.section(3, "比大小：先比位数，再比高位")

        n1 = txt("3865", size=62, color=GOLD).move_to([-3.9, 1.55, 0])
        g1 = txt("＞", size=54, color=RED).move_to([-1.85, 1.55, 0])
        n2 = txt("985", size=62, color=CHALK).move_to([-0.35, 1.55, 0])
        r1 = txt("四位数比三位数大", size=26, color=CHALK).move_to([3.55, 1.55, 0])
        self.play(FadeIn(n1), FadeIn(n2), run_time=0.7)
        self.play(FadeIn(g1), FadeIn(r1), run_time=0.7)

        rx_l, rx_r = -3.4, 0.5
        m1 = digits_row("5860", -0.35, rx_l, size=62, color=GOLD)
        m2 = digits_row("5840", -0.35, rx_r, size=62, color=CHALK)
        g2 = txt("＞", size=54, color=RED).move_to([-2.1, -0.35, 0])
        r2 = txt("位数相同，从高位比", size=26, color=CHALK).move_to([3.9, -0.35, 0])
        self.play(FadeIn(m1), FadeIn(m2), run_time=0.7)
        self.play(FadeIn(g2), FadeIn(r2), run_time=0.7)

        # 十位 6 与 4 圈出来
        px = 62 * 0.0078
        c1 = Ellipse(width=0.46, height=0.8, color=GREEN, stroke_width=2.4)
        c1.move_to([rx_l - px, -0.35, 0])
        c2 = Ellipse(width=0.46, height=0.8, color=GREEN, stroke_width=2.4)
        c2.move_to([rx_r - px, -0.35, 0])
        self.play(Create(c1), Create(c2), run_time=0.8)

        note = txt("先看位数，位数相同再从百位、十位依次比", size=26, color=GOLD)
        note.move_to([-0.3, -1.75, 0])
        self.play(FadeIn(note, shift=UP * 0.08), run_time=0.8)

        tip = txt("哪一位大，那个数就大", size=27, color=DIM).move_to([-0.3, -2.5, 0])
        self.play(FadeIn(tip, shift=UP * 0.06), run_time=0.7)
        self.finish_section()

    # ---------------- 4. 加法竖式 ---------------- 16.0
    def scene_add(self):
        self.section(4, "竖式：数位对齐，满十进一")

        rx = 2.6
        a = digits_row("3865", 2.05, rx, size=54, color=CHALK)
        b = digits_row("1240", 1.2, rx, size=54, color=BLUE)
        plus = op_symbol("+", 1.2, rx)
        line = Line([rx - 1.98, 0.78, 0], [rx + 0.18, 0.78, 0],
                    color=CHALK, stroke_width=3)
        self.play(FadeIn(a), run_time=0.6)
        self.play(FadeIn(b), FadeIn(plus), run_time=0.6)
        self.play(Create(line), run_time=0.5)

        # 步骤说明（左）
        s1 = txt("① 个位 5+0=5", size=23, color=DIM).move_to([-3.7, 1.85, 0])
        s2 = txt("② 十位 6+4=10", size=23, color=GOLD).move_to([-3.7, 1.2, 0])
        s3 = txt("写 0，进 1 到百位", size=23, color=GOLD).move_to([-3.7, 0.6, 0])
        s4 = txt("③ 百位 8+2+1=11", size=23, color=GOLD).move_to([-3.7, -0.1, 0])
        s5 = txt("写 1，进 1 到千位", size=23, color=GOLD).move_to([-3.7, -0.7, 0])
        s6 = txt("④ 千位 3+1+1=5", size=23, color=DIM).move_to([-3.7, -1.45, 0])
        for s in (s1, s2, s3, s4, s5, s6):
            self.play(FadeIn(s, shift=RIGHT * 0.06), run_time=0.5)

        c1 = txt("1", size=26, color=RED).move_to([rx - 2 * (54 * 0.0078), 2.55, 0])
        c2 = txt("1", size=26, color=RED).move_to([rx - 3 * (54 * 0.0078), 2.55, 0])
        self.play(FadeIn(c1), run_time=0.5)
        self.play(FadeIn(c2), run_time=0.5)

        res = digits_row("5105", 0.32, rx, size=54, color=GREEN)
        self.play(Write(res), run_time=1.2)

        ans = txt("5105 本", size=34, color=GREEN).move_to([-3.6, -2.35, 0])
        self.play(FadeIn(ans, shift=UP * 0.08), run_time=0.8)
        self.finish_section()

    # ---------------- 5. 验算 ---------------- 14.3
    def scene_check(self):
        self.section(5, "验算：用减法倒推")

        rx = 2.6
        a = digits_row("5105", 2.05, rx, size=54, color=CHALK)
        b = digits_row("3865", 1.2, rx, size=54, color=BLUE)
        minus = op_symbol("−", 1.2, rx)
        line = Line([rx - 1.98, 0.78, 0], [rx + 0.18, 0.78, 0],
                    color=CHALK, stroke_width=3)
        self.play(FadeIn(a), run_time=0.6)
        self.play(FadeIn(b), FadeIn(minus), run_time=0.6)
        self.play(Create(line), run_time=0.5)

        # 借位提示
        k1 = txt("5 减 5 得 0", size=23, color=DIM).move_to([-3.8, 1.85, 0])
        k2 = txt("0 减 6 不够，借 1 当 10", size=23, color=GOLD).move_to([-3.8, 1.2, 0])
        k3 = txt("10 − 6 = 4", size=23, color=GOLD).move_to([-3.8, 0.6, 0])
        k4 = txt("百位、千位同样借位再减", size=23, color=DIM).move_to([-3.8, -0.2, 0])
        for s in (k1, k2, k3, k4):
            self.play(FadeIn(s, shift=RIGHT * 0.06), run_time=0.55)

        res = digits_row("1240", 0.32, rx, size=54, color=GREEN)
        self.play(Write(res), run_time=1.2)

        ok = txt("正好是原来的 1240，算对了", size=28, color=GREEN).move_to([-0.9, -1.55, 0])
        self.play(FadeIn(ok, shift=UP * 0.08), run_time=0.8)

        tip = txt("加法用减法验算，减法用加法验算", size=26, color=DIM).move_to([-0.9, -2.35, 0])
        self.play(FadeIn(tip, shift=UP * 0.06), run_time=0.7)
        self.finish_section()

    # ---------------- 6. 收束 ---------------- 11.7
    def scene_summary(self):
        self.section(6, "大数计算三句话")

        rows = VGroup(
            label_box("① 数位对齐，从个位算起", size=28, color=GOLD),
            label_box("② 满十进一，不够减借一", size=28, color=CHALK),
            label_box("③ 算完用相反运算验算", size=28, color=CHALK),
        ).arrange(DOWN, buff=0.45).move_to([0, 0.95, 0])
        for r in rows:
            self.play(FadeIn(r, shift=RIGHT * 0.1), run_time=0.6)

        est = txt("估算：3865 ≈ 4000，1240 ≈ 1200，和约 5200", size=25, color=BLUE)
        est.move_to([0, -1.2, 0])
        self.play(FadeIn(est, shift=UP * 0.06), run_time=0.8)

        tip = txt("实际 5105，离 5200 不远，答案合理", size=27, color=GREEN).move_to([0, -2.05, 0])
        self.play(FadeIn(tip, shift=UP * 0.08), run_time=0.8)
        self.finish_section()

    def construct(self):
        self.scene_story()
        self.clear_stage()
        self.scene_places()
        self.clear_stage()
        self.scene_read()
        self.clear_stage()
        self.scene_compare()
        self.clear_stage()
        self.scene_add()
        self.clear_stage()
        self.scene_check()
        self.clear_stage()
        self.scene_summary()
        self.clear_stage(0.8)