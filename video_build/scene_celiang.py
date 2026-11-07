# -*- coding: utf-8 -*-
"""测量与时分秒：厘米与米、经过时间。二年级下册「测量」+「时、分、秒」。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403

PER_CM = 0.5          # 1 厘米 = 0.5 个场景单位
RULER_CM = 20


def ruler(x_left=-5.2, y=0.15, cm=RULER_CM, per_cm=PER_CM, height=0.9) -> VGroup:
    """刻度尺：20 厘米，每 1 厘米一短刻度，每 5 厘米一长刻度。"""
    width = cm * per_cm
    body = Rectangle(width=width, height=height, color=CHALK, stroke_width=2.4,
                     fill_color=CHALK, fill_opacity=0.06)
    body.move_to([x_left + width / 2, y, 0])

    g = VGroup(body)
    for i in range(cm + 1):
        x = x_left + i * per_cm
        major = i % 5 == 0
        top = y + height / 2
        length = 0.32 if major else 0.18
        g.add(Line([x, top, 0], [x, top - length, 0],
                   color=CHALK if major else DIM,
                   stroke_width=2.4 if major else 1.4))
        if major:
            g.add(txt(str(i), size=20, color=DIM).move_to([x, y - height / 2 - 0.26, 0]))
    return g


def clock_simple(center, r=1.5) -> VGroup:
    """简化钟面：外圈 + 12 个数字。"""
    cx, cy = center[0], center[1]
    ring = Circle(radius=r, color=CHALK, stroke_width=3,
                  fill_color=CHALK, fill_opacity=0.02).move_to([cx, cy, 0])
    nums = VGroup()
    for h in range(1, 13):
        ang = (90 - h * 30) * DEGREES
        nums.add(txt(str(h), size=20, color=CHALK).move_to(
            [cx + (r - 0.35) * np.cos(ang), cy + (r - 0.35) * np.sin(ang), 0]))
    return VGroup(ring, nums)


def hand(center, length, color, width, angle_deg=0.0) -> Line:
    cx, cy = center[0], center[1]
    h = Line([cx, cy, 0], [cx, cy + length, 0], color=color, stroke_width=width)
    if angle_deg:
        h.rotate(-angle_deg * DEGREES, about_point=[cx, cy, 0])
    return h


class CeliangScene(NarratedScene):
    lesson = "celiang-shifenmiao"

    def clear_stage(self, run_time: float = 0.5):
        keep = {id(self._track), id(self._fill)}
        junk = [m for m in self.mobjects if id(m) not in keep]
        if junk:
            self.play(*[FadeOut(m) for m in junk], run_time=run_time)
        self.cur_title = None
        self.cur_sub = None

    # ---------------- 0. 两个问题 ----------------
    def scene_life(self):
        self.section(0, "两个问题，两种单位")

        # 左：课桌
        desk = VGroup(
            Rectangle(width=3.0, height=0.14, color=GOLD, stroke_width=2,
                      fill_color=GOLD, fill_opacity=0.35).move_to([-2.6, 0.2, 0]),
            Line([-4.0, 0.13, 0], [-4.0, -1.15, 0], color=GOLD, stroke_width=4),
            Line([-1.2, 0.13, 0], [-1.2, -1.15, 0], color=GOLD, stroke_width=4),
            Line([-4.15, 0.92, 0], [-1.05, 0.92, 0], color=CHALK, stroke_width=2),
            Line([-4.15, 0.8, 0], [-4.15, 1.04, 0], color=CHALK, stroke_width=2),
            Line([-1.05, 0.8, 0], [-1.05, 1.04, 0], color=CHALK, stroke_width=2),
        )
        q1 = txt("课桌有多长？", size=30, color=GOLD).move_to([-2.6, 1.75, 0])
        a1 = txt("用长度单位", size=26, color=DIM).move_to([-2.6, -1.95, 0])

        # 右：一节课
        clock = clock_simple([2.6, 0.05], r=1.25)
        hh = hand([2.6, 0.05], 0.7, GOLD, 8, 270)
        mm = hand([2.6, 0.05], 1.05, BLUE, 5, 240)
        q2 = txt("一节课多久？", size=30, color=BLUE).move_to([2.6, 1.55, 0])
        a2 = txt("用时间单位", size=26, color=DIM).move_to([2.6, -2.15, 0])

        self.play(FadeIn(VGroup(desk, q1)), run_time=1.0)
        self.play(FadeIn(clock), Create(hh), Create(mm), FadeIn(q2), run_time=1.1)
        self.play(FadeIn(a1, shift=UP * 0.08), FadeIn(a2, shift=UP * 0.08), run_time=0.9)
        self.finish_section()

    # ---------------- 1. 用尺子量 ----------------
    def scene_measure(self):
        self.section(1, "量长度：一端对准 0")

        r = ruler()
        self.play(Create(r), run_time=1.2)

        # 铅笔：从 0 刻度开始，长 8 厘米
        x0 = -5.2
        pencil = VGroup(
            RoundedRectangle(corner_radius=0.06, width=8 * PER_CM - 0.35, height=0.36,
                             stroke_color=ORANGE, stroke_width=2,
                             fill_color=ORANGE, fill_opacity=0.45),
            Polygon([x0 + 8 * PER_CM - 0.35, 0.62, 0], [x0 + 8 * PER_CM, 0.62, 0],
                    [x0 + 8 * PER_CM, 0.44, 0],
                    color=ORANGE, stroke_width=2, fill_color=CHALK, fill_opacity=0.8),
        )
        pencil[0].move_to([x0 + (8 * PER_CM - 0.35) / 2, 0.62, 0])
        self.play(FadeIn(pencil, shift=UP * 0.1), run_time=1.0)

        zero_hi = Circle(radius=0.19, color=RED, stroke_width=3).move_to([x0, 0.15, 0])
        self.play(Create(zero_hi), run_time=0.5)
        lab0 = txt("0 刻度对齐", size=24, color=RED).move_to([x0 - 0.1, -1.05, 0])
        self.play(FadeIn(lab0, shift=UP * 0.06), run_time=0.5)

        end_x = x0 + 8 * PER_CM
        arr = Arrow([end_x, 1.35, 0], [end_x, 0.9, 0], color=GOLD, stroke_width=3, buff=0,
                    max_tip_length_to_length_ratio=0.35)
        read = txt("笔尾对着 8 → 长 8 厘米", size=30, color=GOLD).move_to([1.4, 1.55, 0])
        self.play(GrowArrow(arr), FadeIn(read, shift=UP * 0.06), run_time=0.9)
        self.finish_section()

    # ---------------- 2. 厘米与米 ----------------
    def scene_units(self):
        self.section(2, "厘米与米：1 米 = 100 厘米")

        # 米尺
        meter = VGroup()
        for i in range(10):
            meter.add(Rectangle(width=1.0, height=0.55, color=CHALK, stroke_width=1.8,
                                fill_color=GOLD if i % 2 == 0 else CHALK,
                                fill_opacity=0.16).move_to([-5.0 + i + 0.5, 0.95, 0]))
        m_lab = txt("1 米", size=34, color=GOLD).move_to([0, 1.75, 0])
        self.play(LaggedStart(*[FadeIn(m) for m in meter], lag_ratio=0.06), run_time=1.2)
        self.play(FadeIn(m_lab, shift=UP * 0.08), run_time=0.5)

        # 100 个 1 厘米
        small = VGroup()
        for i in range(100):
            small.add(Line([-5.0 + i * 0.1, 0.35, 0], [-5.0 + i * 0.1, 0.62, 0],
                           color=GREEN, stroke_width=1.4))
        c_lab = txt("100 厘米", size=30, color=GREEN).move_to([0, -0.15, 0])
        self.play(LaggedStart(*[Create(s) for s in small], lag_ratio=0.006), run_time=1.6)
        self.play(FadeIn(c_lab, shift=UP * 0.08), run_time=0.6)

        eq = txt("1 米 = 100 厘米", size=52, color=GOLD).move_to([0, -1.35, 0])
        self.play(Write(eq), run_time=1.1)

        tip = txt("量铅笔用厘米，量教室用米", size=27, color=DIM).move_to([0, -2.4, 0])
        self.play(FadeIn(tip), run_time=0.6)
        self.finish_section()

    # ---------------- 3. 时分秒 ----------------
    def scene_time_units(self):
        self.section(3, "1 时 = 60 分，1 分 = 60 秒")

        c = [-3.9, 0.15, 0]
        face = clock_simple(c, r=1.55)
        minute = hand(c, 1.28, BLUE, 5, 0)
        hub = Dot([c[0], c[1], 0], radius=0.08, color=CHALK)
        self.play(FadeIn(face), Create(minute), FadeIn(hub), run_time=1.0)

        counter = txt("0 分", size=40, color=BLUE).move_to([-3.9, -1.95, 0])
        self.play(FadeIn(counter), run_time=0.4)

        self.play(Rotate(minute, angle=-180 * DEGREES, about_point=[c[0], c[1], 0]),
                  Transform(counter, txt("30 分", size=40, color=BLUE).move_to(counter)),
                  run_time=1.4)
        self.play(Rotate(minute, angle=-180 * DEGREES, about_point=[c[0], c[1], 0]),
                  Transform(counter, txt("60 分", size=40, color=BLUE).move_to(counter)),
                  run_time=1.4)

        e1 = txt("1 时 = 60 分", size=48, color=GOLD).move_to([2.6, 1.25, 0])
        self.play(Write(e1), run_time=1.0)
        e2 = txt("1 分 = 60 秒", size=48, color=GREEN).move_to([2.6, 0.15, 0])
        self.play(Write(e2), run_time=1.0)

        note = txt("分针走 1 小格 = 1 分", size=25, color=DIM).move_to([2.6, -0.95, 0])
        self.play(FadeIn(note, shift=UP * 0.06), run_time=0.6)
        self.finish_section()

    # ---------------- 4. 经过时间 ----------------
    def scene_elapsed(self):
        self.section(4, "经过时间：结束减开始")

        line = Line([-5.2, 0.1, 0], [5.2, 0.1, 0], color=CHALK, stroke_width=3)
        self.play(Create(line), run_time=0.8)

        x1, x2 = -3.6, 3.4
        t1 = Line([x1, -0.05, 0], [x1, 0.25, 0], color=GOLD, stroke_width=4)
        t2 = Line([x2, -0.05, 0], [x2, 0.25, 0], color=GOLD, stroke_width=4)
        l1 = txt("8:10", size=34, color=GOLD).move_to([x1, -0.55, 0])
        l2 = txt("8:40", size=34, color=GOLD).move_to([x2, -0.55, 0])
        self.play(Create(t1), Create(t2), FadeIn(l1), FadeIn(l2), run_time=0.9)

        arc = CurvedArrow([x1 + 0.08, 0.35, 0], [x2 - 0.08, 0.35, 0],
                          angle=-1.1, color=BLUE, stroke_width=3)
        self.play(Create(arc), run_time=1.0)

        span = txt("经过 30 分", size=34, color=BLUE).move_to([0, 1.75, 0])
        self.play(FadeIn(span, shift=UP * 0.08), run_time=0.7)

        calc = txt("40 - 10 = 30（分）", size=46, color=CHALK).move_to([0, -1.45, 0])
        self.play(Write(calc), run_time=1.0)

        half = txt("30 分 = 半小时", size=30, color=GREEN).move_to([0, -2.3, 0])
        self.play(FadeIn(half, shift=UP * 0.06), run_time=0.6)
        self.finish_section()

    # ---------------- 5. 选单位 ----------------
    def scene_choose(self):
        self.section(5, "选单位：看对象大小")

        head_l = txt("长度", size=34, color=GOLD).move_to([-3.4, 2.3, 0])
        head_t = txt("时间", size=34, color=BLUE).move_to([3.4, 2.3, 0])
        self.play(FadeIn(head_l, shift=UP * 0.08), FadeIn(head_t, shift=UP * 0.08), run_time=0.7)

        left_rows = [("橡皮", "4 厘米"), ("课桌", "60 厘米"), ("教室", "8 米")]
        right_rows = [("眨一次眼", "1 秒"), ("跑 50 米", "10 秒"), ("一节课", "40 分")]

        for i, (name, val) in enumerate(left_rows):
            y = 1.25 - i * 0.95
            name_t = txt(name, size=28, color=DIM).move_to([-2.35, y, 0], aligned_edge=RIGHT)
            val_t = txt(val, size=32, color=GOLD).move_to([-1.95, y, 0], aligned_edge=LEFT)
            self.play(FadeIn(VGroup(name_t, val_t), shift=RIGHT * 0.08), run_time=0.55)

        for i, (name, val) in enumerate(right_rows):
            y = 1.25 - i * 0.95
            name_t = txt(name, size=28, color=DIM).move_to([1.75, y, 0], aligned_edge=RIGHT)
            val_t = txt(val, size=32, color=BLUE).move_to([2.15, y, 0], aligned_edge=LEFT)
            self.play(FadeIn(VGroup(name_t, val_t), shift=RIGHT * 0.08), run_time=0.55)

        tip = txt("单位选错，数再对也没意义", size=28, color=GREEN).move_to([0, -2.3, 0])
        self.play(FadeIn(tip, shift=UP * 0.08), run_time=0.7)
        self.finish_section()

    # ---------------- 6. 收束 ----------------
    def scene_summary(self):
        self.section(6, "记住这两组换算")

        b1 = RoundedRectangle(corner_radius=0.14, width=5.4, height=2.35,
                              stroke_color=GOLD, stroke_width=2.4,
                              fill_color=GOLD, fill_opacity=0.08).move_to([-3.5, 0.72, 0])
        t1 = txt("长度", size=34, color=GOLD).move_to([-3.5, 1.45, 0])
        f1 = txt("1 米 = 100 厘米", size=40, color=CHALK).move_to([-3.5, 0.55, 0])
        h1 = txt("用尺子量，一端对 0", size=22, color=DIM).move_to([-3.5, -0.15, 0])

        b2 = RoundedRectangle(corner_radius=0.14, width=5.4, height=2.35,
                              stroke_color=BLUE, stroke_width=2.4,
                              fill_color=BLUE, fill_opacity=0.08).move_to([3.5, 0.72, 0])
        t2 = txt("时间", size=34, color=BLUE).move_to([3.5, 1.45, 0])
        f2 = txt("1 时 = 60 分", size=38, color=CHALK).move_to([3.5, 0.68, 0])
        f3 = txt("1 分 = 60 秒", size=38, color=CHALK).move_to([3.5, 0.02, 0])

        self.play(FadeIn(b1, shift=UP * 0.08), FadeIn(t1), FadeIn(f1), FadeIn(h1), run_time=1.0)
        self.play(FadeIn(b2, shift=UP * 0.08), FadeIn(t2), FadeIn(f2), FadeIn(f3), run_time=1.0)

        tip = txt("长度看厘米与米，时间看分与秒", size=30, color=GREEN).move_to([0, -1.75, 0])
        self.play(FadeIn(tip, shift=UP * 0.08), run_time=0.8)
        self.finish_section()

    def construct(self):
        self.scene_life()
        self.clear_stage()
        self.scene_measure()
        self.clear_stage()
        self.scene_units()
        self.clear_stage()
        self.scene_time_units()
        self.clear_stage()
        self.scene_elapsed()
        self.clear_stage()
        self.scene_choose()
        self.clear_stage()
        self.scene_summary()
        self.clear_stage(0.8)