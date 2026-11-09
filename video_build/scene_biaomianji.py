# -*- coding: utf-8 -*-
"""长方体的表面积：六个面的面积总和。五年级下册「长方体和正方体」。"""

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


def cuboid(w: float, h: float, d: float, cx: float = 0.0, cy: float = 0.0,
           front: str = CHALK, top: str = CHALK, right: str = CHALK,
           opacity: float = 0.10) -> VGroup:
    """等轴测长方体：正面矩形 + 顶面、右面平行四边形。"""
    ox, oy = d * 0.62, d * 0.48
    A = [-w / 2, -h / 2, 0]
    B = [w / 2, -h / 2, 0]
    C = [w / 2, h / 2, 0]
    D = [-w / 2, h / 2, 0]
    off = np.array([ox, oy, 0])
    F = np.array(B) + off
    G = np.array(C) + off
    H = np.array(D) + off

    f_front = Polygon(A, B, C, D, stroke_width=0,
                      fill_color=front, fill_opacity=opacity)
    f_top = Polygon(D, C, G, H, stroke_width=0,
                    fill_color=top, fill_opacity=opacity * 1.4)
    f_right = Polygon(B, C, G, F, stroke_width=0,
                      fill_color=right, fill_opacity=opacity * 1.2)

    edges = VGroup(
        Line(A, B, color=CHALK, stroke_width=2.6),
        Line(B, C, color=CHALK, stroke_width=2.6),
        Line(C, D, color=CHALK, stroke_width=2.6),
        Line(D, A, color=CHALK, stroke_width=2.6),
        Line(D, H, color=CHALK, stroke_width=2.2),
        Line(C, G, color=CHALK, stroke_width=2.2),
        Line(B, F, color=CHALK, stroke_width=2.2),
        Line(H, G, color=CHALK, stroke_width=2.6),
        Line(G, F, color=CHALK, stroke_width=2.6),
    )
    g = VGroup(f_front, f_top, f_right, edges)
    g.shift([cx, cy, 0])
    return g


class BiaomianjiScene(NarratedScene):
    lesson = "biaomianji"

    def construct(self):
        K = 0.52
        w, h, d = 5 * K, 3 * K, 4 * K
        cx, cy = -3.55, 0.15

        # ---------- 0. 包彩纸，需要多少纸？ ----------
        self.section(0, "包一层彩纸，需要多少？")
        box = cuboid(w, h, d, cx=cx, cy=cy)
        self.play(Create(box), run_time=1.3)

        q1 = txt("给长方体纸盒包彩纸", size=36, color=CHALK).move_to([3.7, 1.55, 0])
        q2 = txt("需要多少彩纸？", size=40, color=GOLD).move_to([3.7, 0.55, 0])
        q3 = txt("就是求它的表面积", size=34, color=GREEN).move_to([3.7, -0.55, 0])
        self.play(FadeIn(q1, shift=UP * 0.1), run_time=0.7)
        self.play(Write(q2), run_time=0.8)
        self.play(FadeIn(q3), run_time=0.6)
        self.finish_section()

        # ---------- 1. 表面积 = 六个面的面积和 ----------
        self.section(1, "表面积 = 六个面的面积和")
        self.play(FadeOut(q1), FadeOut(q2), FadeOut(q3), FadeOut(box), run_time=0.5)

        box2 = cuboid(w, h, d, cx=cx, cy=cy,
                      front=GOLD, top=BLUE, right=GREEN, opacity=0.30)
        self.play(FadeIn(box2), run_time=0.7)

        a1 = txt("六个面都算上", size=36, color=CHALK).move_to([3.7, 1.55, 0])
        a2 = txt("相对的面完全相同", size=34, color=GOLD).move_to([3.7, 0.55, 0])
        a3 = txt("只要算 3 组面，再乘 2", size=34, color=GREEN).move_to([3.7, -0.5, 0])
        self.play(Write(a1), run_time=0.7)
        self.play(FadeIn(a2, shift=UP * 0.1), run_time=0.6)
        self.play(Write(a3), run_time=0.8)
        self.finish_section()

        # ---------- 2. 长 5 宽 4 高 3：三组面 ----------
        self.section(2, "长 5、宽 4、高 3 的盒子")
        self.play(FadeOut(a1), FadeOut(a2), FadeOut(a3), run_time=0.4)

        # 三条棱的长度标注
        m5 = txt("5", size=28, color=GOLD).move_to([cx, cy - h / 2 - 0.32, 0])
        m3 = txt("3", size=28, color=GREEN).move_to([cx + w / 2 + d * 0.62 + 0.24, cy, 0])
        m4 = txt("4", size=28, color=BLUE).move_to([cx + w / 2 + d * 0.34 + 0.18,
                                                   cy + h / 2 + d * 0.26 + 0.16, 0])
        self.play(FadeIn(m5), FadeIn(m3), FadeIn(m4), run_time=0.6)

        b1 = txt("上下面：5 × 4 = 20", size=36, color=BLUE).move_to([3.8, 1.75, 0])
        b2 = txt("前后面：5 × 3 = 15", size=36, color=GOLD).move_to([3.8, 0.65, 0])
        b3 = txt("左右面：4 × 3 = 12", size=36, color=GREEN).move_to([3.8, -0.45, 0])
        b4 = txt("三组面，各有两个", size=28, color=DIM).move_to([3.8, -1.45, 0])
        self.play(Write(b1), run_time=0.8)
        self.play(Write(b2), run_time=0.8)
        self.play(Write(b3), run_time=0.8)
        self.play(FadeIn(b4), run_time=0.5)
        self.finish_section()

        # ---------- 3. 加起来再乘 2 ----------
        self.section(3, "二十加十五加十二，再乘二")
        self.play(FadeOut(box2), FadeOut(m5), FadeOut(m3), FadeOut(m4),
                  FadeOut(b1), FadeOut(b2), FadeOut(b3), FadeOut(b4), run_time=0.6)

        c1 = txt("20 + 15 + 12 = 47", size=44, color=CHALK).move_to([0, 1.65, 0])
        c2 = txt("47 × 2 = 94", size=50, color=GOLD).move_to([0, 0.45, 0])
        c3 = txt("表面积 = 94 平方厘米", size=44, color=GREEN).move_to([0, -0.85, 0])
        self.play(Write(c1), run_time=0.9)
        self.play(Write(c2), run_time=0.9)
        self.play(FadeIn(c3, shift=UP * 0.1), run_time=0.7)

        c4 = txt("先算三组面，别忘了乘 2", size=28, color=DIM).move_to([0, -2.1, 0])
        self.play(FadeIn(c4), run_time=0.5)
        self.finish_section()

        # ---------- 4. 正方体：一个面乘 6 ----------
        self.section(4, "正方体：一个面乘 6")
        self.play(FadeOut(c1), FadeOut(c2), FadeOut(c3), FadeOut(c4), run_time=0.5)

        cube = cuboid(1.5, 1.5, 1.5, cx=-3.8, cy=0.15,
                      front=GOLD, top=BLUE, right=GREEN, opacity=0.28)
        self.play(Create(cube), run_time=1.0)

        d1 = txt("棱长 3 厘米", size=36, color=CHALK).move_to([3.7, 1.6, 0])
        d2 = txt("一个面：3 × 3 = 9", size=36, color=GOLD).move_to([3.7, 0.6, 0])
        d3 = txt("六个面：9 × 6 = 54", size=40, color=GREEN).move_to([3.7, -0.45, 0])
        d4 = txt("54 平方厘米", size=34, color=CHALK).move_to([3.7, -1.45, 0])
        self.play(Write(d1), run_time=0.7)
        self.play(Write(d2), run_time=0.7)
        self.play(Write(d3), run_time=0.8)
        self.play(FadeIn(d4), run_time=0.5)
        self.finish_section()

        # ---------- 5. 三个易错点 ----------
        self.section(5, "三个容易错的地方")
        self.play(FadeOut(cube), FadeOut(d1), FadeOut(d2), FadeOut(d3), FadeOut(d4),
                  run_time=0.5)

        e1 = txt("✗ 漏算面：只算了 5 个面", size=36, color=RED).move_to([0, 1.65, 0])
        e2 = txt("✗ 把棱长总和当成表面积", size=36, color=RED).move_to([0, 0.55, 0])
        e3 = txt("✗ 单位写成厘米，应该是平方厘米", size=36, color=RED).move_to([0, -0.55, 0])
        self.play(Write(e1), run_time=0.8)
        self.play(Write(e2), run_time=0.8)
        self.play(Write(e3), run_time=0.8)

        e4 = txt("算完问一句：六个面都算到了吗？", size=32, color=GREEN).move_to([0, -1.85, 0])
        self.play(FadeIn(e4, shift=UP * 0.1), run_time=0.6)
        self.finish_section()

        # ---------- 6. 公式 ----------
        self.section(6, "三组面相加再乘二")
        self.play(FadeOut(e1), FadeOut(e2), FadeOut(e3), FadeOut(e4), run_time=0.5)

        f1 = txt("长方体：S =（长×宽 + 长×高 + 宽×高）× 2",
                 size=33, color=GOLD).move_to([0, 1.55, 0])
        f2 = txt("正方体：S = 棱长 × 棱长 × 6", size=40, color=GREEN).move_to([0, 0.35, 0])
        f3 = txt("面积单位：平方厘米、平方分米、平方米", size=30, color=CHALK).move_to([0, -0.8, 0])
        self.play(Write(f1), run_time=1.0)
        self.play(Write(f2), run_time=0.9)
        self.play(FadeIn(f3), run_time=0.6)

        fin = txt("表面积是面积，不是棱长总和", size=30, color=DIM).move_to([0, -2.05, 0])
        self.play(FadeIn(fin, shift=UP * 0.1), run_time=0.6)
        self.finish_section()

        self.play(FadeOut(f1), FadeOut(f2), FadeOut(f3), FadeOut(fin), run_time=0.6)