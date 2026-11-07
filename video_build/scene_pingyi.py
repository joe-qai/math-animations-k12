# -*- coding: utf-8 -*-
"""平移、旋转与轴对称：三种图形运动。三年级下册。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403

GRID_W, GRID_H = 9, 6
CELL = 0.62


def grid(bg_center, cols: int = GRID_W, rows: int = GRID_H,
         cell: float = CELL, color: str = DIM) -> VGroup:
    cx, cy = bg_center[0], bg_center[1]
    x0, y0 = cx - cols * cell / 2, cy - rows * cell / 2
    g = VGroup()
    for i in range(cols + 1):
        g.add(Line([x0 + i * cell, y0, 0], [x0 + i * cell, y0 + rows * cell, 0],
                   color=color, stroke_width=1.0, stroke_opacity=0.55))
    for j in range(rows + 1):
        g.add(Line([x0, y0 + j * cell, 0], [x0 + cols * cell, y0 + j * cell, 0],
                   color=color, stroke_width=1.0, stroke_opacity=0.55))
    return g


def flag(anchor, color: str = GOLD) -> VGroup:
    """小旗子：anchor 是旗杆底端，便于判断平移了几格。"""
    ax, ay = anchor[0], anchor[1]
    pole = Line([ax, ay, 0], [ax, ay + 3 * CELL, 0], color=color, stroke_width=5)
    cloth = Polygon([ax, ay + 3 * CELL, 0],
                    [ax + 2.2 * CELL, ay + 2.45 * CELL, 0],
                    [ax, ay + 1.9 * CELL, 0],
                    color=color, stroke_width=2.5,
                    fill_color=color, fill_opacity=0.3)
    return VGroup(pole, cloth)


def butterfly(center, color: str = GREEN) -> VGroup:
    """左右对称的小蝴蝶，用来表现轴对称。"""
    def wing(x: float, y: float, w: float, h: float, ang: float):
        e = Ellipse(width=w, height=h, color=color, stroke_width=2.2,
                    fill_color=color, fill_opacity=0.22)
        e.rotate(ang * DEGREES)
        return e.move_to([x, y, 0])

    left = VGroup(wing(-0.52, 0.38, 1.0, 0.72, 26), wing(-0.40, -0.42, 0.72, 0.54, -22))
    right = VGroup(wing(0.52, 0.38, 1.0, 0.72, -26), wing(0.40, -0.42, 0.72, 0.54, 22))
    body = Line([0, -0.7, 0], [0, 0.52, 0], color=CHALK, stroke_width=7)
    head = Dot([0, 0.64, 0], radius=0.07, color=CHALK)
    return VGroup(left, right, body, head).move_to(center)


class PingyiScene(NarratedScene):
    lesson = "pingyi-xuanzhuan"

    def clear_stage(self, run_time: float = 0.5):
        keep = {id(self._track), id(self._fill)}
        junk = [m for m in self.mobjects if id(m) not in keep]
        if junk:
            self.play(*[FadeOut(m) for m in junk], run_time=run_time)
        self.cur_title = None
        self.cur_sub = None

    # ---------------- 0. 三种现象 ----------------
    def scene_story(self):
        self.section(0, "电梯、风车、蝴蝶")

        # 左：电梯（平移）
        shaft = Rectangle(width=1.5, height=3.2, color=DIM, stroke_width=2.2)
        shaft.move_to([-4.4, 0.3, 0])
        car = Rectangle(width=1.1, height=0.85, color=GOLD, stroke_width=2.4,
                        fill_color=GOLD, fill_opacity=0.25).move_to([-4.4, -0.55, 0])
        arr = Arrow([-3.35, -0.35, 0], [-3.35, 0.85, 0], color=GOLD, stroke_width=3, buff=0,
                    max_tip_length_to_length_ratio=0.3)
        self.play(Create(shaft), FadeIn(car), run_time=0.8)
        self.play(GrowArrow(arr), car.animate.shift(UP * 1.6), run_time=1.2)

        # 中：风车（旋转）
        hub = [0.4, 0.35, 0]
        blades = VGroup()
        for k in range(4):
            ang = k * 90 * DEGREES
            blade = Polygon([0, 0, 0], [0, 1.15, 0], [0.5, 1.15, 0], [0.5, 0.15, 0],
                            color=BLUE, stroke_width=2,
                            fill_color=BLUE, fill_opacity=0.28)
            blade.rotate(ang, about_point=[0, 0, 0])
            blades.add(blade)
        blades.move_to(hub)
        dot = Dot(hub, radius=0.09, color=CHALK)
        self.play(FadeIn(blades), FadeIn(dot), run_time=0.9)
        self.play(Rotate(blades, angle=-240 * DEGREES, about_point=hub), run_time=1.8)

        # 右：蝴蝶（轴对称）
        bf = butterfly([4.35, 0.35, 0])
        self.play(FadeIn(bf, scale=0.9), run_time=0.9)
        self.play(Indicate(bf, color=GREEN, scale_factor=1.06), run_time=0.9)

        l1 = txt("平移", size=28, color=GOLD).move_to([-4.4, -1.85, 0])
        l2 = txt("旋转", size=28, color=BLUE).move_to([0.4, -1.85, 0])
        l3 = txt("轴对称", size=28, color=GREEN).move_to([4.3, -1.85, 0])
        self.play(FadeIn(l1), FadeIn(l2), FadeIn(l3), run_time=0.9)
        self.finish_section()

    # ---------------- 1. 平移：直着走 ----------------
    def scene_translate(self):
        self.section(1, "平移：方向不变，位置变")

        g = grid([-1.0, 0.45])
        self.play(Create(g), run_time=1.0)

        start = flag([-3.48, -0.9], color=GOLD)
        self.play(Create(start), run_time=0.8)

        ghost = VGroup(*[DashedVMobject(m.copy(), num_dashes=12).set_color(DIM)
                         for m in start])
        self.play(FadeIn(ghost), run_time=0.5)

        self.play(start.animate.set_color(BLUE).shift(RIGHT * 5 * CELL), run_time=1.8)

        arr = Arrow([-3.48, 1.62, 0], [-3.48 + 5 * CELL, 1.62, 0], color=BLUE,
                    stroke_width=2.6, buff=0, max_tip_length_to_length_ratio=0.14)
        arr_lab = txt("平移 5 格", size=26, color=BLUE).move_to([-1.9, 2.0, 0])
        self.play(GrowArrow(arr), FadeIn(arr_lab), run_time=0.8)

        note = txt("方向不变 · 形状大小不变 · 只有位置变了", size=26, color=GREEN)
        note.move_to([0, -2.35, 0])
        self.play(FadeIn(note, shift=UP * 0.06), run_time=0.8)
        self.finish_section()

    # ---------------- 2. 数格子的方法 ----------------
    def scene_count(self):
        self.section(2, "数平移几格：找对应点")

        g = grid([-1.0, 0.45])
        self.play(Create(g), run_time=1.0)

        ax, ay = -3.48, -0.9
        start = flag([ax, ay], color=GOLD)
        self.play(Create(start), run_time=0.7)

        vx, vy = ax, ay
        v = Dot([vx, vy, 0], radius=0.1, color=RED)
        v_lab = txt("对应点", size=24, color=RED).move_to([vx - 0.82, vy + 0.06, 0])
        v_arr = Arrow([vx - 0.5, vy + 0.05, 0], [vx - 0.16, vy, 0], color=RED,
                      buff=0, max_tip_length_to_length_ratio=0.3)
        self.play(FadeIn(v), FadeIn(v_lab), GrowArrow(v_arr), run_time=0.7)

        # 沿对应点连线一格一格数过去
        meas = Line([vx, vy, 0], [vx + 4 * CELL, vy, 0], color=RED, stroke_width=1.6)
        self.play(Create(meas), run_time=0.6)
        marks = VGroup()
        for i in range(1, 5):
            x = vx + i * CELL
            marks.add(Line([x, vy - 0.12, 0], [x, vy + 0.12, 0],
                           color=RED, stroke_width=2.4))
        nums = VGroup()
        for i in range(4):
            x = vx + (i + 0.5) * CELL
            nums.add(txt(str(i + 1), size=20, color=RED).move_to([x, vy - 0.3, 0]))
        self.play(LaggedStart(*[FadeIn(m) for m in marks], lag_ratio=0.2), run_time=1.0)
        self.play(LaggedStart(*[FadeIn(n) for n in nums], lag_ratio=0.2), run_time=1.0)

        end = flag([vx + 4 * CELL, vy], color=BLUE)
        self.play(Create(end), run_time=0.9)
        v2 = Dot([vx + 4 * CELL, vy, 0], radius=0.1, color=BLUE)
        self.play(FadeIn(v2), run_time=0.4)

        count = txt("对应点走 4 格 → 图形平移 4 格", size=27, color=BLUE)
        count.move_to([-1.0, 2.45, 0])
        self.play(FadeIn(count, shift=UP * 0.06), run_time=0.8)

        warn = txt("不是数两个图形中间的空格", size=26, color=RED).move_to([0, -2.35, 0])
        self.play(FadeIn(warn, shift=UP * 0.06), run_time=0.7)
        self.finish_section()

    # ---------------- 3. 旋转 ----------------
    def scene_rotate(self):
        self.section(3, "旋转：绕一个点转")

        c = [-2.4, 0.4, 0]
        tri = Polygon([-2.4, 0.4, 0], [-2.4 + 2.0, 0.4, 0], [-2.4, 1.5, 0],
                      color=GOLD, stroke_width=3, fill_color=GOLD, fill_opacity=0.22)
        dot = Dot(c, radius=0.11, color=RED)
        dot_lab = txt("绕这个点", size=24, color=RED).move_to([-2.4, -0.35, 0])
        self.play(Create(tri), FadeIn(dot), run_time=0.9)
        self.play(FadeIn(dot_lab), run_time=0.5)

        ghost = VGroup(*[DashedVMobject(m.copy(), num_dashes=10).set_color(DIM)
                         for m in tri])
        arc = Arc(radius=1.2, start_angle=0, angle=90 * DEGREES, color=BLUE,
                  stroke_width=2.4).move_arc_center_to(c)
        self.play(Create(arc), run_time=0.8)
        self.play(Rotate(tri, angle=90 * DEGREES, about_point=c), run_time=1.9)
        self.play(FadeIn(ghost), run_time=0.5)

        h1 = txt("形状、大小不变", size=28, color=GREEN).move_to([3.2, 1.35, 0])
        h2 = txt("方向变了", size=28, color=GOLD).move_to([3.2, 0.55, 0])
        h3 = txt("钟表指针、风车都是旋转", size=24, color=DIM).move_to([3.2, -0.35, 0])
        self.play(FadeIn(h1, shift=UP * 0.06), run_time=0.6)
        self.play(FadeIn(h2, shift=UP * 0.06), run_time=0.6)
        self.play(FadeIn(h3, shift=UP * 0.06), run_time=0.7)

        tip = txt("旋转要看三件事：绕哪点、转多少度、往哪边转", size=25, color=BLUE)
        tip.move_to([0, -2.35, 0])
        self.play(FadeIn(tip, shift=UP * 0.06), run_time=0.8)
        self.finish_section()

    # ---------------- 4. 轴对称 ----------------
    def scene_symmetry(self):
        self.section(4, "轴对称：对折能完全重合")

        axis_x = -0.6
        k = 2.0 / 22.0
        dy = 0.62 - (-6 * k)
        pts = []
        for t in np.linspace(np.pi, 2 * np.pi, 80):
            hx = 16 * np.sin(t) ** 3
            hy = (13 * np.cos(t) - 5 * np.cos(2 * t)
                  - 2 * np.cos(3 * t) - np.cos(4 * t))
            pts.append([axis_x + hx * k, hy * k + dy, 0])

        axis = DashedLine([axis_x, -1.85, 0], [axis_x, 2.2, 0],
                          color=BLUE, stroke_width=2.4)
        self.play(Create(axis), run_time=0.8)

        half = Polygon(*pts, color=GOLD, stroke_width=3,
                       fill_color=GOLD, fill_opacity=0.22)
        self.play(Create(half), run_time=1.1)

        mirror = half.copy().set_color(GREEN)
        mirror.set_fill(GREEN, opacity=0.18)
        mirror.flip(UP, about_point=[axis_x, 0, 0])
        self.play(Create(mirror), run_time=1.1)
        self.bring_to_front(axis)
        self.wait(2.0)

        self.play(mirror.animate.flip(UP, about_point=[axis_x, 0, 0]), run_time=2.0)

        ok = txt("两边完全重合", size=28, color=GREEN).move_to([3.5, 1.25, 0])
        ok2 = txt("就是轴对称图形", size=28, color=GREEN).move_to([3.5, 0.55, 0])
        ax_lab = txt("折痕这条线叫对称轴", size=26, color=BLUE).move_to([3.5, -0.35, 0])
        self.play(FadeIn(ok, shift=UP * 0.06), run_time=0.7)
        self.play(FadeIn(ok2, shift=UP * 0.06), run_time=0.7)
        self.play(FadeIn(ax_lab, shift=UP * 0.06), run_time=0.7)

        ax_tag = txt("对称轴", size=24, color=BLUE).move_to([axis_x, -2.15, 0])
        tip = txt("对折后两边一模一样，这条折痕就是对称轴", size=25, color=DIM)
        tip.move_to([0, -2.75, 0])
        self.play(FadeIn(ax_tag), run_time=0.4)
        self.play(FadeIn(tip, shift=UP * 0.06), run_time=0.8)
        self.finish_section()

    # ---------------- 5. 几条对称轴 ----------------
    def scene_axes(self):
        self.section(5, "长方形 2 条，正方形 4 条")

        # 长方形
        rect = Rectangle(width=2.4, height=1.5, color=GOLD, stroke_width=3).move_to([-4.3, 0.55, 0])
        self.play(Create(rect), run_time=0.6)
        ax_v = DashedLine([-4.3, -0.45, 0], [-4.3, 1.55, 0], color=BLUE, stroke_width=2)
        ax_h = DashedLine([-5.7, 0.55, 0], [-2.9, 0.55, 0], color=BLUE, stroke_width=2)
        self.play(Create(ax_v), run_time=0.6)
        self.play(Create(ax_h), run_time=0.6)
        r_lab = txt("长方形 2 条", size=26, color=GOLD).move_to([-4.3, -1.0, 0])
        self.play(FadeIn(r_lab), run_time=0.5)

        # 正方形
        sq = Square(side_length=1.6, color=GOLD, stroke_width=3).move_to([-0.2, 0.55, 0])
        self.play(Create(sq), run_time=0.6)
        s_axes = VGroup(
            DashedLine([-0.2, -0.4, 0], [-0.2, 1.5, 0], color=BLUE, stroke_width=2),
            DashedLine([-1.15, 0.55, 0], [0.75, 0.55, 0], color=BLUE, stroke_width=2),
            DashedLine([-0.95, -0.2, 0], [0.55, 1.3, 0], color=BLUE, stroke_width=2),
            DashedLine([-0.95, 1.3, 0], [0.55, -0.2, 0], color=BLUE, stroke_width=2),
        )
        self.play(LaggedStart(*[Create(a) for a in s_axes], lag_ratio=0.2), run_time=1.2)
        s_lab = txt("正方形 4 条", size=26, color=GOLD).move_to([-0.2, -1.0, 0])
        self.play(FadeIn(s_lab), run_time=0.5)

        # 圆
        circ = Circle(radius=0.95, color=GOLD, stroke_width=3).move_to([4.1, 0.55, 0])
        self.play(Create(circ), run_time=0.6)
        c_axes = VGroup(
            DashedLine([4.1, -0.55, 0], [4.1, 1.65, 0], color=BLUE, stroke_width=2),
            DashedLine([3.0, 0.55, 0], [5.2, 0.55, 0], color=BLUE, stroke_width=2),
            DashedLine([3.42, -0.13, 0], [4.78, 1.23, 0], color=BLUE, stroke_width=2),
        )
        self.play(LaggedStart(*[Create(a) for a in c_axes], lag_ratio=0.2), run_time=1.0)
        c_lab = txt("圆有无数条", size=26, color=GOLD).move_to([4.1, -1.0, 0])
        self.play(FadeIn(c_lab), run_time=0.5)

        tip = txt("等腰三角形只有 1 条对称轴", size=25, color=DIM).move_to([0, -2.35, 0])
        self.play(FadeIn(tip, shift=UP * 0.06), run_time=0.7)
        self.finish_section()

    # ---------------- 6. 收束 ----------------
    def scene_summary(self):
        self.section(6, "三种运动，一句话分清")

        rows = VGroup(
            label_box("平移：直着走，方向不变", size=28, color=GOLD),
            label_box("旋转：绕一点转，方向变了", size=28, color=BLUE),
            label_box("轴对称：对折完全重合", size=28, color=GREEN),
        ).arrange(DOWN, buff=0.45).move_to([0, 0.5, 0])
        for r in rows:
            self.play(FadeIn(r, shift=RIGHT * 0.1), run_time=0.6)

        tip = txt("三种运动，形状和大小都不变", size=29, color=CHALK).move_to([0, -1.95, 0])
        self.play(FadeIn(tip, shift=UP * 0.08), run_time=0.8)
        self.finish_section()

    def construct(self):
        self.scene_story()
        self.clear_stage()
        self.scene_translate()
        self.clear_stage()
        self.scene_count()
        self.clear_stage()
        self.scene_rotate()
        self.clear_stage()
        self.scene_symmetry()
        self.clear_stage()
        self.scene_axes()
        self.clear_stage()
        self.scene_summary()
        self.clear_stage(0.8)