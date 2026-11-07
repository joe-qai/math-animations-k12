# -*- coding: utf-8 -*-
"""认识钟表：时针、分针，整时与半时。一年级上册「认识钟表」。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403

CENTER = [-2.95, -0.2, 0]
R = 2.0


def clock_face(center=CENTER, r=R, num_size=22, show_minor=True) -> VGroup:
    """钟面：外圈 + 刻度 + 12 个数字。"""
    cx, cy = center[0], center[1]
    ring = Circle(radius=r, color=CHALK, stroke_width=3,
                  fill_color=CHALK, fill_opacity=0.02).move_to([cx, cy, 0])

    ticks = VGroup()
    for i in range(60):
        if i % 5 and not show_minor:
            continue
        ang = (90 - i * 6) * DEGREES
        major = i % 5 == 0
        length = 0.2 if major else 0.09
        p1 = [cx + (r - 0.05 - length) * np.cos(ang), cy + (r - 0.05 - length) * np.sin(ang), 0]
        p2 = [cx + (r - 0.05) * np.cos(ang), cy + (r - 0.05) * np.sin(ang), 0]
        ticks.add(Line(p1, p2, color=CHALK if major else DIM,
                       stroke_width=3 if major else 1.2,
                       stroke_opacity=1 if major else 0.45))

    nums = VGroup()
    for h in range(1, 13):
        ang = (90 - h * 30) * DEGREES
        nums.add(txt(str(h), size=num_size, color=CHALK).move_to(
            [cx + (r - 0.42) * np.cos(ang), cy + (r - 0.42) * np.sin(ang), 0]))

    return VGroup(ring, ticks, nums)


def hand(center, length, color, width, angle_deg=0.0) -> Line:
    """从圆心指向 12 点的指针，按顺时针角度旋转。"""
    cx, cy = center[0], center[1]
    h = Line([cx, cy, 0], [cx, cy + length, 0], color=color, stroke_width=width)
    if angle_deg:
        h.rotate(-angle_deg * DEGREES, about_point=[cx, cy, 0])
    return h


class ZhongbiaoScene(NarratedScene):
    lesson = "renshi-zhongbiao"

    def clear_stage(self, run_time: float = 0.5):
        keep = {id(self._track), id(self._fill)}
        junk = [m for m in self.mobjects if id(m) not in keep]
        if junk:
            self.play(*[FadeOut(m) for m in junk], run_time=run_time)
        self.cur_title = None
        self.cur_sub = None

    # ---------------- 0. 生活里的时间 ----------------
    def scene_life(self):
        self.section(0, "我们怎么知道几点了")

        left_c = [-3.45, 0.55, 0]
        right_c = [3.45, 0.55, 0]
        left = clock_face(left_c, r=1.05, num_size=13, show_minor=False)
        right = clock_face(right_c, r=1.05, num_size=13, show_minor=False)

        l_hand = hand(left_c, 0.5, GOLD, 7, 7 * 30)
        l_min = hand(left_c, 0.82, BLUE, 4.5, 0)
        r_hand = hand(right_c, 0.5, GOLD, 7, 8 * 30)
        r_min = hand(right_c, 0.82, BLUE, 4.5, 0)

        self.play(FadeIn(left), FadeIn(right), run_time=0.9)
        self.play(Create(l_hand), Create(l_min), Create(r_hand), Create(r_min), run_time=0.9)

        l_lab = txt("早上 7 时 · 起床", size=30, color=GOLD).move_to([-3.45, -0.95, 0])
        r_lab = txt("早上 8 时 · 上学", size=30, color=GOLD).move_to([3.45, -0.95, 0])
        self.play(FadeIn(l_lab, shift=UP * 0.08), FadeIn(r_lab, shift=UP * 0.08), run_time=0.7)

        q = txt("怎么知道现在是几点？看钟表", size=36, color=CHALK).move_to([0, -2.15, 0])
        self.play(FadeIn(q, shift=UP * 0.08), run_time=0.7)
        self.finish_section()

    # ---------------- 1. 钟面上有什么 ----------------
    def scene_face(self):
        self.section(1, "钟面：12 个数字，三根针")
        face = clock_face()
        self.play(Create(face[0]), run_time=0.7)
        self.play(LaggedStart(*[FadeIn(t) for t in face[1]], lag_ratio=0.015), run_time=0.8)
        self.play(LaggedStart(*[FadeIn(n) for n in face[2]], lag_ratio=0.05), run_time=1.0)

        hour = hand(CENTER, 1.0, GOLD, 10, 300)
        minute = hand(CENTER, 1.5, BLUE, 6, 60)
        second = hand(CENTER, 1.8, RED, 2.2, 180)
        hub = Dot([CENTER[0], CENTER[1], 0], radius=0.09, color=CHALK)

        self.play(Create(hour), FadeIn(hub), run_time=0.6)
        self.play(Create(minute), run_time=0.6)
        self.play(Create(second), run_time=0.6)

        x = 2.5
        t1 = txt("时针", size=32, color=GOLD).move_to([x, 1.35, 0])
        d1 = txt("短、粗，走得慢", size=23, color=DIM).move_to([x, 0.85, 0])
        t2 = txt("分针", size=32, color=BLUE).move_to([x, 0.1, 0])
        d2 = txt("长、细，走一圈一小时", size=23, color=DIM).move_to([x, -0.4, 0])
        t3 = txt("秒针", size=32, color=RED).move_to([x, -1.15, 0])
        d3 = txt("最细，走得最快", size=23, color=DIM).move_to([x, -1.65, 0])
        self.play(FadeIn(t1, shift=UP * 0.06), FadeIn(d1), run_time=0.5)
        self.play(FadeIn(t2, shift=UP * 0.06), FadeIn(d2), run_time=0.5)
        self.play(FadeIn(t3, shift=UP * 0.06), FadeIn(d3), run_time=0.5)
        self.play(Indicate(hour, color=GOLD, scale_factor=1.02),
                  Indicate(minute, color=BLUE, scale_factor=1.02), run_time=0.9)
        self.finish_section()

    # ---------------- 2. 分针走一圈 = 60 分钟 ----------------
    def scene_minute(self):
        self.section(2, "分针走一大格 = 5 分钟")
        c = [-2.75, -0.15, 0]
        face = clock_face(center=c, r=R)
        minute = hand(c, 1.58, BLUE, 6, 0)
        hub = Dot([c[0], c[1], 0], radius=0.08, color=CHALK)
        self.play(FadeIn(face), Create(minute), FadeIn(hub), run_time=1.0)

        one = label_box("1 小格 = 1 分钟", size=26, color=CHALK).move_to([2.75, 1.55, 0])
        five = label_box("1 大格 = 5 分钟", size=28, color=GOLD).move_to([2.75, 0.75, 0])
        counter = txt("0 分钟", size=46, color=BLUE).move_to([2.75, -0.55, 0])
        self.play(FadeIn(one), run_time=0.5)
        self.play(FadeIn(five), run_time=0.5)
        self.play(FadeIn(counter), run_time=0.4)

        self.play(Rotate(minute, angle=-30 * DEGREES, about_point=[c[0], c[1], 0]), run_time=0.8)
        self.play(Transform(counter, txt("5 分钟", size=46, color=BLUE).move_to(counter)),
                  run_time=0.4)

        for k in range(2, 13):
            self.play(Rotate(minute, angle=-30 * DEGREES, about_point=[c[0], c[1], 0]),
                      run_time=0.42)
            self.play(Transform(counter, txt(f"{k * 5} 分钟", size=46, color=BLUE).move_to(counter)),
                      run_time=0.18)

        wrap = txt("60 分钟 = 1 小时", size=34, color=GREEN).move_to([2.75, -1.65, 0])
        self.play(FadeIn(wrap, shift=UP * 0.08), run_time=0.6)
        self.finish_section()

    # ---------------- 3. 整时 ----------------
    def scene_whole(self):
        self.section(3, "整时：分针指 12")
        face = clock_face()
        self.play(FadeIn(face), run_time=0.8)

        minute = hand(CENTER, 1.58, BLUE, 6, 0)
        hour = hand(CENTER, 1.0, GOLD, 10, 0)
        hub = Dot([CENTER[0], CENTER[1], 0], radius=0.08, color=CHALK)
        self.play(Create(hour), Create(minute), FadeIn(hub), run_time=0.8)

        self.play(Rotate(hour, angle=-90 * DEGREES,
                         about_point=[CENTER[0], CENTER[1], 0]), run_time=0.9)

        digital = txt("3:00", size=76, color=GOLD).move_to([2.75, 1.15, 0])
        read = txt("三时（三点）", size=38, color=CHALK).move_to([2.75, 0.15, 0])
        rule_t = txt("分针指 12 → 整时", size=27, color=GREEN).move_to([2.75, -0.85, 0])
        self.play(Write(digital), run_time=0.9)
        self.play(FadeIn(read, shift=UP * 0.08), run_time=0.6)
        self.play(FadeIn(rule_t), run_time=0.6)

        # 再看一个：8 时
        self.play(Rotate(hour, angle=-150 * DEGREES,
                         about_point=[CENTER[0], CENTER[1], 0]), run_time=1.6)
        self.play(Transform(digital, txt("8:00", size=76, color=GOLD).move_to(digital)),
                  Transform(read, txt("八时（八点）", size=38, color=CHALK).move_to(read)),
                  run_time=0.7)
        self.finish_section()

    # ---------------- 4. 半时 ----------------
    def scene_half(self):
        self.section(4, "半时：分针指 6")
        face = clock_face()
        self.play(FadeIn(face), run_time=0.8)

        minute = hand(CENTER, 1.58, BLUE, 6, 0)
        hour = hand(CENTER, 1.0, GOLD, 10, 90)
        hub = Dot([CENTER[0], CENTER[1], 0], radius=0.08, color=CHALK)
        self.play(FadeIn(hour), Create(minute), FadeIn(hub), run_time=0.7)

        half_note = txt("分针从 12 走到 6：半圈", size=28, color=BLUE).move_to([2.75, 1.55, 0])
        self.play(FadeIn(half_note), run_time=0.5)
        self.play(Rotate(minute, angle=-180 * DEGREES,
                         about_point=[CENTER[0], CENTER[1], 0]), run_time=1.4)
        self.play(Rotate(hour, angle=-15 * DEGREES,
                         about_point=[CENTER[0], CENTER[1], 0]), run_time=0.8)

        digital = txt("3:30", size=76, color=GOLD).move_to([2.75, 0.55, 0])
        read = txt("三时半 / 三时三十分", size=34, color=CHALK).move_to([2.75, -0.35, 0])
        rule_t = txt("时针在 3 和 4 中间", size=26, color=GREEN).move_to([2.75, -1.2, 0])
        self.play(Write(digital), run_time=0.8)
        self.play(FadeIn(read, shift=UP * 0.08), run_time=0.5)
        self.play(FadeIn(rule_t), run_time=0.5)

        # 再看一个：8 时半，分针还是指 6，只是时针换了位置
        self.play(Rotate(hour, angle=-150 * DEGREES,
                         about_point=[CENTER[0], CENTER[1], 0]), run_time=1.5)
        self.play(Transform(digital, txt("8:30", size=76, color=GOLD).move_to(digital)),
                  Transform(read, txt("八时半 / 八时三十分", size=34, color=CHALK).move_to(read)),
                  Transform(rule_t, txt("时针在 8 和 9 中间", size=26, color=GREEN).move_to(rule_t)),
                  run_time=0.7)
        self.finish_section()

    # ---------------- 5. 两步读法 ----------------
    def scene_read(self):
        self.section(5, "读时间：先看时针，再看分针")

        s1 = label_box("① 看时针（短）→ 几时", size=30, color=GOLD).move_to([-2.9, 1.4, 0])
        s2 = label_box("② 看分针（长）→ 几分", size=30, color=BLUE).move_to([2.9, 1.4, 0])
        self.play(FadeIn(s1, shift=UP * 0.08), run_time=0.6)
        self.play(FadeIn(s2, shift=UP * 0.08), run_time=0.6)

        ex1 = VGroup(
            txt("8:00", size=40, color=CHALK),
            txt("时针指 8，分针指 12 → 8 时", size=28, color=DIM),
        ).arrange(DOWN, buff=0.18, aligned_edge=LEFT).move_to([-2.9, -0.15, 0])
        ex2 = VGroup(
            txt("8:30", size=40, color=CHALK),
            txt("时针在 8、9 之间，分针指 6 → 8 时半", size=24, color=DIM),
        ).arrange(DOWN, buff=0.18, aligned_edge=LEFT).move_to([2.9, -0.15, 0])

        self.play(FadeIn(ex1, shift=UP * 0.06), run_time=0.7)
        self.play(FadeIn(ex2, shift=UP * 0.06), run_time=0.7)

        warn = txt("别把短针当分针：短针走得慢，长针走得快", size=27, color=RED).move_to([0, -1.95, 0])
        self.play(FadeIn(warn, shift=UP * 0.08), run_time=0.7)
        self.play(Indicate(s1, color=GOLD, scale_factor=1.03), run_time=0.7)
        self.play(Indicate(ex1, color=CHALK, scale_factor=1.02), run_time=0.7)
        self.play(Indicate(s2, color=BLUE, scale_factor=1.03), run_time=0.7)
        self.play(Indicate(ex2, color=CHALK, scale_factor=1.02), run_time=0.7)
        self.finish_section()

    # ---------------- 6. 收束 ----------------
    def scene_summary(self):
        self.section(6, "短针定几时，长针定几分")

        big = txt("短针定几时，长针定几分", size=54, color=GOLD).move_to([0, 1.55, 0])
        self.play(Write(big), run_time=1.0)

        b1 = label_box("整时：分针指 12", size=32, color=GREEN).move_to([-3.0, 0.0, 0])
        b2 = label_box("半时：分针指 6", size=32, color=GREEN).move_to([3.0, 0.0, 0])
        self.play(FadeIn(b1, shift=UP * 0.08), FadeIn(b2, shift=UP * 0.08), run_time=0.8)

        tip = txt("多看一眼钟，就不会迟到", size=32, color=CHALK).move_to([0, -1.35, 0])
        self.play(FadeIn(tip, shift=UP * 0.08), run_time=0.7)
        self.finish_section()

    def construct(self):
        self.scene_life()
        self.clear_stage()
        self.scene_face()
        self.clear_stage()
        self.scene_minute()
        self.clear_stage()
        self.scene_whole()
        self.clear_stage()
        self.scene_half()
        self.clear_stage()
        self.scene_read()
        self.clear_stage()
        self.scene_summary()
        self.clear_stage(0.8)