# -*- coding: utf-8 -*-
"""位置与顺序：前后、上下、左右。一年级上册「位置与顺序」。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


def kid(x: float, y: float, color: str, name: str) -> VGroup:
    head = Circle(radius=0.23, stroke_width=2, stroke_color=color,
                  fill_color=color, fill_opacity=0.22).move_to([x, y + 0.55, 0])
    body = RoundedRectangle(corner_radius=0.1, width=0.46, height=0.62,
                            stroke_width=2, stroke_color=color,
                            fill_color=color, fill_opacity=0.12).move_to([x, y, 0])
    nm = txt(name, size=20, color=color).next_to(body, DOWN, buff=0.12)
    return VGroup(head, body, nm)


def person(x: float, y: float, color: str) -> VGroup:
    head = Circle(radius=0.26, stroke_width=2.2, stroke_color=color,
                  fill_color=color, fill_opacity=0.15).move_to([x, y + 0.85, 0])
    body = Line([x, y + 0.55, 0], [x, y - 0.35, 0], color=color, stroke_width=2.4)
    armL = Line([x, y + 0.35, 0], [x - 0.55, y + 0.05, 0], color=color, stroke_width=2.4)
    armR = Line([x, y + 0.35, 0], [x + 0.55, y + 0.05, 0], color=color, stroke_width=2.4)
    legL = Line([x, y - 0.35, 0], [x - 0.35, y - 0.95, 0], color=color, stroke_width=2.4)
    legR = Line([x, y - 0.35, 0], [x + 0.35, y - 0.95, 0], color=color, stroke_width=2.4)
    return VGroup(head, body, armL, armR, legL, legR)


class WeizhiShunxuScene(NarratedScene):
    lesson = "weizhi-shunxu"

    def construct(self):
        # ---------- 0. 排队 ----------
        self.section(0, "排队时，谁在前面？")
        kids = VGroup(
            kid(-5.35, 0.55, GOLD, "小明"),
            kid(-4.15, 0.55, BLUE, "小红"),
            kid(-2.95, 0.55, GREEN, "小刚"),
            kid(-1.75, 0.55, ORANGE, "小丽"),
        )
        self.play(LaggedStart(*[FadeIn(k, shift=RIGHT * 0.1) for k in kids],
                              lag_ratio=0.18), run_time=1.2)

        face = Arrow([-5.9, -1.15, 0], [-1.15, -1.15, 0], buff=0, color=GOLD,
                     stroke_width=3, tip_length=0.2)
        flab = txt("前面", size=26, color=GOLD).next_to(face, DOWN, buff=0.08)
        self.play(GrowArrow(face), FadeIn(flab), run_time=0.8)

        q1 = txt("队伍里", size=36, color=CHALK).move_to([3.7, 1.2, 0])
        q2 = txt("谁站在前面", size=40, color=GOLD).move_to([3.7, 0.3, 0])
        q3 = txt("谁站在后面？", size=40, color=GOLD).move_to([3.7, -0.6, 0])
        self.play(Write(q1), run_time=0.5)
        self.play(Write(q2), run_time=0.6)
        self.play(Write(q3), run_time=0.6)
        self.finish_section()

        # ---------- 1. 前后是一组方向 ----------
        self.section(1, "面朝的是前，背对的是后")
        self.play(FadeOut(q1), FadeOut(q2), FadeOut(q3), FadeOut(flab),
                  FadeOut(face), run_time=0.4)

        front = Arrow([-2.0, 1.85, 0], [-0.4, 1.85, 0], buff=0, color=GREEN,
                      stroke_width=4, tip_length=0.2)
        back = Arrow([-2.0, -0.75, 0], [-3.6, -0.75, 0], buff=0, color=RED,
                     stroke_width=4, tip_length=0.2)
        f1 = txt("前", size=36, color=GREEN).next_to(front, UP, buff=0.08)
        f2 = txt("后", size=36, color=RED).next_to(back, DOWN, buff=0.08)
        self.play(GrowArrow(front), FadeIn(f1), run_time=0.7)
        self.play(GrowArrow(back), FadeIn(f2), run_time=0.7)

        t1 = txt("面朝的方向是「前」", size=36, color=GREEN).move_to([3.5, 1.2, 0])
        t2 = txt("背对的方向是「后」", size=36, color=RED).move_to([3.5, 0.2, 0])
        self.play(Write(t1), run_time=0.6)
        self.play(Write(t2), run_time=0.6)

        t3 = txt("前后不是固定的", size=34, color=GOLD).move_to([3.5, -0.85, 0])
        t4 = txt("要看大家面朝哪边", size=30, color=DIM).move_to([3.5, -1.7, 0])
        self.play(FadeIn(t3, shift=UP * 0.1), run_time=0.5)
        self.play(FadeIn(t4), run_time=0.5)
        self.finish_section()

        # ---------- 2. 前后是相对的 ----------
        self.section(2, "换个说法，前后是相对的")
        self.play(FadeOut(front), FadeOut(back), FadeOut(f1), FadeOut(f2),
                  FadeOut(t1), FadeOut(t2), FadeOut(t3), FadeOut(t4),
                  FadeOut(kids), run_time=0.5)

        b1 = label_box("小明在小红的前面", size=36, color=GOLD).move_to([0, 1.5, 0])
        swap = txt("换 个 说 法", size=28, color=DIM).move_to([0, 0.45, 0])
        down_arrow = Arrow([0, 0.1, 0], [0, -0.35, 0], buff=0, color=GOLD,
                           stroke_width=2.6, tip_length=0.16)
        b2 = label_box("小红在小明的后面", size=36, color=GREEN).move_to([0, -1.1, 0])
        self.play(FadeIn(b1, shift=UP * 0.1), run_time=0.7)
        self.play(FadeIn(swap), GrowArrow(down_arrow), run_time=0.6)
        self.play(FadeIn(b2, shift=DOWN * 0.1), run_time=0.7)

        n1 = txt("前后是相对的", size=34, color=CHALK).move_to([0, -2.35, 0])
        self.play(FadeIn(n1), run_time=0.5)
        self.finish_section()

        # ---------- 3. 上下 ----------
        self.section(3, "书架上的上和下")
        self.play(FadeOut(b1), FadeOut(swap), FadeOut(down_arrow), FadeOut(b2),
                  FadeOut(n1), run_time=0.5)

        shell = VGroup(
            Rectangle(width=3.8, height=3.2, stroke_color=CHALK, stroke_width=2.2),
            Line([-1.9, 0.53, 0], [1.9, 0.53, 0], color=CHALK, stroke_width=1.8),
            Line([-1.9, -0.53, 0], [1.9, -0.53, 0], color=CHALK, stroke_width=1.8),
        ).move_to([-3.6, 0.15, 0])
        self.play(Create(shell), run_time=0.9)

        books = VGroup(
            Rectangle(width=0.34, height=0.72, stroke_width=0, fill_color=BLUE,
                      fill_opacity=0.6).move_to([-4.5, 1.15, 0]),
            Rectangle(width=0.34, height=0.72, stroke_width=0, fill_color=GOLD,
                      fill_opacity=0.6).move_to([-4.05, 1.15, 0]),
            Rectangle(width=0.34, height=0.72, stroke_width=0, fill_color=GREEN,
                      fill_opacity=0.6).move_to([-3.6, 1.15, 0]),
            Rectangle(width=0.34, height=0.72, stroke_width=0, fill_color=ORANGE,
                      fill_opacity=0.6).move_to([-3.0, -0.9, 0]),
        )
        self.play(LaggedStart(*[FadeIn(b, shift=UP * 0.1) for b in books],
                              lag_ratio=0.15), run_time=1.0)

        up_lab = txt("上面", size=26, color=GOLD).move_to([-1.2, 1.15, 0])
        mid_lab = txt("中间", size=26, color=DIM).move_to([-1.2, 0.0, 0])
        dn_lab = txt("下面", size=26, color=GREEN).move_to([-1.2, -0.9, 0])
        self.play(LaggedStart(*[FadeIn(t) for t in (up_lab, mid_lab, dn_lab)],
                              lag_ratio=0.2), run_time=0.8)

        u1 = txt("上层的书在上面", size=34, color=GOLD).move_to([3.3, 1.1, 0])
        u2 = txt("下层的书在下面", size=34, color=GREEN).move_to([3.3, 0.05, 0])
        u3 = txt("和前后一样，上下也是相对的", size=30, color=DIM).move_to([3.3, -1.05, 0])
        self.play(Write(u1), run_time=0.6)
        self.play(Write(u2), run_time=0.6)
        self.play(FadeIn(u3), run_time=0.5)
        self.finish_section()

        # ---------- 4. 左右 ----------
        self.section(4, "左右，要看自己")
        self.play(FadeOut(shell), FadeOut(books), FadeOut(up_lab), FadeOut(mid_lab),
                  FadeOut(dn_lab), FadeOut(u1), FadeOut(u2), FadeOut(u3), run_time=0.5)

        pA = person(-4.8, 0.35, GOLD)
        pB = person(-1.6, 0.35, BLUE)
        self.play(FadeIn(pA), FadeIn(pB), run_time=0.8)

        la = txt("我的左手", size=24, color=GOLD).move_to([-6.0, 1.55, 0])
        ra = txt("我的右手", size=24, color=GOLD).move_to([-3.6, 1.55, 0])
        lb = txt("对方的左手", size=24, color=BLUE).move_to([-0.95, 1.55, 0])
        self.play(FadeIn(la), FadeIn(ra), run_time=0.6)
        self.play(FadeIn(lb), run_time=0.5)

        r1 = txt("写字的手是右手", size=34, color=GOLD).move_to([3.4, 0.9, 0])
        r2 = txt("另一只是左手", size=34, color=GOLD).move_to([3.4, -0.05, 0])
        r3 = txt("面对面站着时", size=30, color=CHALK).move_to([3.4, -1.1, 0])
        r4 = txt("你的左，就是对方的右", size=30, color=GREEN).move_to([3.4, -1.9, 0])
        self.play(Write(r1), run_time=0.6)
        self.play(Write(r2), run_time=0.6)
        self.play(FadeIn(r3), run_time=0.4)
        self.play(FadeIn(r4, shift=UP * 0.1), run_time=0.6)
        self.finish_section()

        # ---------- 5. 说完整 ----------
        self.section(5, "说位置，要说完整")
        self.play(FadeOut(pA), FadeOut(pB), FadeOut(la), FadeOut(ra), FadeOut(lb),
                  FadeOut(r1), FadeOut(r2), FadeOut(r3), FadeOut(r4), run_time=0.5)

        s1 = txt("谁", size=44, color=GOLD).move_to([-4.3, 1.1, 0])
        s2 = txt("在", size=30, color=DIM).move_to([-2.9, 1.1, 0])
        s3 = txt("谁", size=44, color=BLUE).move_to([-1.5, 1.1, 0])
        s4 = txt("的", size=30, color=DIM).move_to([-0.35, 1.1, 0])
        s5 = txt("哪一面", size=44, color=GREEN).move_to([1.25, 1.1, 0])
        self.play(LaggedStart(*[FadeIn(t, shift=UP * 0.1) for t in (s1, s2, s3, s4, s5)],
                              lag_ratio=0.15), run_time=1.2)

        ex1 = txt("小明在小红的左面", size=34, color=CHALK).move_to([-2.0, -0.35, 0])
        ex2 = txt("书在书架的上面", size=34, color=CHALK).move_to([-2.0, -1.3, 0])
        self.play(Write(ex1), run_time=0.7)
        self.play(Write(ex2), run_time=0.7)

        wrong = txt("✗ 只说「在上面」，别人不知道是谁的上面", size=28, color=RED)
        wrong.move_to([0, -2.35, 0])
        self.play(FadeIn(wrong), run_time=0.6)
        self.finish_section()

        # ---------- 6. 三个方向 ----------
        self.section(6, "前后、上下、左右")
        self.play(FadeOut(s1), FadeOut(s2), FadeOut(s3), FadeOut(s4), FadeOut(s5),
                  FadeOut(ex1), FadeOut(ex2), FadeOut(wrong), run_time=0.5)

        k1 = label_box("前后", size=44, color=GOLD).move_to([-3.9, 1.15, 0])
        k2 = label_box("上下", size=44, color=BLUE).move_to([0, 1.15, 0])
        k3 = label_box("左右", size=44, color=GREEN).move_to([3.9, 1.15, 0])
        self.play(LaggedStart(*[FadeIn(k, shift=UP * 0.12) for k in (k1, k2, k3)],
                              lag_ratio=0.22), run_time=1.3)

        big1 = txt("说位置，带上参照的人或物", size=40, color=CHALK).move_to([0, -0.15, 0])
        big2 = txt("「谁在谁的哪一面」", size=44, color=GOLD).move_to([0, -1.15, 0])
        self.play(Write(big1), run_time=0.8)
        self.play(Write(big2), run_time=0.8)

        fin = txt("前后、上下、左右，位置才说得清", size=28, color=DIM).move_to([0, -2.2, 0])
        self.play(FadeIn(fin, shift=UP * 0.1), run_time=0.6)
        self.finish_section()

        self.play(FadeOut(k1), FadeOut(k2), FadeOut(k3),
                  FadeOut(big1), FadeOut(big2), FadeOut(fin), run_time=0.6)