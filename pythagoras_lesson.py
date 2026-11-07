"""
勾股定理 · 通俗动画讲解（中文配音 + 常驻字幕）
================================================
叙事：
  1. 生活例子：梯子靠墙（3 米 / 4 米 / ？米）
  2. 抽象成直角三角形（a、b、c）
  3. 两条直角边上画正方形（9 格、16 格）
  4. 3² + 4² = 5²，梯子长 5 米
  5. 把正方形切成小方格
  6. 25 个小方格正好铺满斜边上的大正方形
  7. 面积相等 → a² + b² = c²

音频用 Scene.add_sound 逐段注入，每段结束自动补齐等待，音画严格同步。
"""

import json
from pathlib import Path

import numpy as np
from manim import *

AUDIO_DIR = Path(__file__).parent / "audio_segments"
TIMINGS = json.loads((AUDIO_DIR / "timings.json").read_text(encoding="utf-8"))

FONT = "Microsoft YaHei"
U = 0.55                     # 1 米 = 一个小方格
GROUND_Y = -1.3
WALL_X = -4.6
V_LEN, H_LEN = 4, 3          # 墙高 4 米，离墙 3 米

C_RED = RED_C
C_GREEN = GREEN_C
C_BLUE = BLUE_C

C_PT = np.array([WALL_X, GROUND_Y, 0.0])          # 直角顶点
A_PT = C_PT + np.array([0, V_LEN * U, 0])          # 墙顶
B_PT = C_PT + np.array([H_LEN * U, 0, 0])          # 梯脚

# 斜边上的正方形：沿 AB 方向 + 向外法向
_c_dir = (B_PT - A_PT)[:2]
_c_len = float(np.linalg.norm(_c_dir))
E1_C = np.array([*_c_dir / _c_len, 0.0])           # (0.6, -0.8)
E2_C = np.array([-_c_dir[1] / _c_len, _c_dir[0] / _c_len, 0.0])   # (0.8, 0.6) 指向外侧
C_ANG = float(np.arctan2(E1_C[1], E1_C[0]))
C_CENTER = A_PT + 2.5 * U * E1_C + 2.5 * U * E2_C


def make_grid(n, origin, e1, e2, color, fill_op=0.28):
    """n×n 的小方格正方形"""
    grid = VGroup()
    ang = np.arctan2(e1[1], e1[0])
    for j in range(n):
        for i in range(n):
            cell = Square(
                side_length=U, stroke_width=1.6, stroke_color=color,
                fill_color=color, fill_opacity=fill_op,
            )
            if abs(ang) > 1e-6:
                cell.rotate(ang)
            cell.move_to(origin + (i + 0.5) * U * e1 + (j + 0.5) * U * e2)
            grid.add(cell)
    return grid


def txt(s, size=30, color=WHITE, **kwargs):
    try:
        return Text(s, font=FONT, font_size=size, color=color, **kwargs)
    except Exception:
        return Text(s, font_size=size, color=color, **kwargs)


class PythagorasLesson(Scene):
    # ---------- 时间轴 ----------
    def begin(self, idx):
        self._t0 = self.renderer.time
        self.add_sound(TIMINGS[idx]["file"])

    def end(self, idx):
        used = self.renderer.time - self._t0
        pad = TIMINGS[idx]["duration"] - used - 0.12
        if pad > 0:
            self.wait(pad)

    def start_section(self, idx, title_text, color=GOLD, size=34):
        """开始一段：切换标题 + 立即显示字幕 + 播放配音"""
        self.begin(idx)
        if getattr(self, "cur_title", None) is not None:
            self.play(FadeOut(self.cur_title), run_time=0.35)
            self.cur_title = None
        if title_text:
            self.cur_title = txt(title_text, size=size, color=color).to_edge(UP, buff=0.38)
            self.play(FadeIn(self.cur_title, shift=DOWN * 0.1), run_time=0.45)

        sub = txt(TIMINGS[idx]["text"], size=26, color=WHITE)
        if sub.width > 12.6:
            sub.scale_to_fit_width(12.6)
        sub.to_edge(DOWN, buff=0.30)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.45)
        self.cur_sub = sub

    def finish_section(self, idx):
        if getattr(self, "cur_sub", None) is not None:
            self.play(FadeOut(self.cur_sub), run_time=0.35)
            self.cur_sub = None
        self.end(idx)

    # ---------- 主流程 ----------
    def construct(self):
        self.camera.background_color = "#0f1220"

        ground_line = Line([-6.9, GROUND_Y, 0], [-1.0, GROUND_Y, 0], color=GREY_B, stroke_width=6)
        wall_line = Line([WALL_X, GROUND_Y, 0], [WALL_X, GROUND_Y + V_LEN * U, 0],
                         color=GREY_B, stroke_width=6)
        ladder = Line(B_PT, A_PT, color=ORANGE, stroke_width=7)
        mid_ab = (A_PT + B_PT) / 2

        # ============ 0. 生活例子 ============
        self.start_section(0, "生活中的数学问题")
        self.play(Create(ground_line), Create(wall_line), run_time=1.4)
        self.play(Create(ladder), run_time=1.2)

        lab_3 = txt("3 米", size=30, color=C_GREEN).move_to([-3.72, GROUND_Y + 0.30, 0])
        lab_4 = txt("4 米", size=30, color=C_RED).move_to([WALL_X - 0.45, GROUND_Y + 1.35, 0])
        lab_q = txt("？米", size=32, color=ORANGE).move_to(mid_ab + 0.45 * E2_C)
        self.play(FadeIn(lab_3), FadeIn(lab_4), run_time=0.8)
        self.play(FadeIn(lab_q, scale=0.8), run_time=0.7)
        self.finish_section(0)

        # ============ 1. 抽象成直角三角形 ============
        self.start_section(1, "抽象成直角三角形")
        tri = Polygon(A_PT, B_PT, C_PT, color=GOLD, fill_opacity=0.12, stroke_width=4)
        tri.set_z_index(-5)          # 填充不要压住文字
        right_angle = RightAngle(Line(C_PT, A_PT), Line(C_PT, B_PT), length=0.26, color=WHITE)
        self.play(FadeIn(tri), run_time=0.8)
        self.play(Create(right_angle), run_time=0.6)

        self.play(
            Transform(lab_3, txt("a = 3", size=30, color=C_GREEN).move_to(lab_3)),
            Transform(lab_4, txt("b = 4", size=30, color=C_RED).move_to(lab_4)),
            run_time=0.9,
        )
        self.play(Transform(lab_q, txt("c = ？", size=32, color=ORANGE).move_to(lab_q)), run_time=0.7)
        self.finish_section(1)

        # ============ 2. 两条直角边上画正方形 ============
        self.start_section(2, "在每条边上画一个正方形")
        # b = 4 在三角形内太挤，画正方形时淡出，用 b²=16 代替
        self.play(FadeOut(lab_4), run_time=0.4)

        sq_red = make_grid(V_LEN, C_PT, np.array([-1.0, 0, 0]), np.array([0, 1.0, 0]), C_RED)
        sq_green = make_grid(H_LEN, C_PT, np.array([1.0, 0, 0]), np.array([0, -1.0, 0]), C_GREEN)

        self.play(Create(sq_red), run_time=2.0)
        area_16 = txt("b² = 16", size=34, color=C_RED).move_to(
            C_PT + np.array([-V_LEN * U / 2, V_LEN * U / 2, 0])
        )
        self.play(FadeIn(area_16, scale=0.8), run_time=0.7)

        self.play(Create(sq_green), run_time=1.8)
        area_9 = txt("a² = 9", size=34, color=C_GREEN).move_to(
            C_PT + np.array([H_LEN * U / 2, -H_LEN * U / 2, 0])
        )
        self.play(FadeIn(area_9, scale=0.8), run_time=0.7)
        self.play(FadeOut(lab_q), run_time=0.4)
        self.finish_section(2)

        # ============ 3. 3² + 4² = 5²，梯子长 5 米 ============
        self.start_section(3, "答案：梯子长 5 米")
        # 斜边上的正方形（先画淡淡的格子）
        sq_blue = make_grid(5, A_PT, E1_C, E2_C, C_BLUE, fill_op=0.05)
        for cell in sq_blue:
            cell.set_stroke(opacity=0.5)
        self.play(FadeIn(sq_blue), run_time=2.0)
        area_25 = txt("c² = 25", size=36, color=C_BLUE).move_to(C_CENTER)
        self.play(FadeIn(area_25, scale=0.8), run_time=0.7)

        eq = txt("3² + 4² = 5²", size=44, color=GOLD).move_to([2.9, 2.35, 0])
        answer = txt("c = 5 米", size=40, color=ORANGE).move_to([2.9, 1.25, 0])
        self.play(FadeIn(eq, shift=DOWN * 0.1), run_time=0.8)
        self.play(FadeIn(answer, shift=UP * 0.1), run_time=0.8)
        self.finish_section(3)

        # ============ 4. 切成小方格 ============
        self.start_section(4, "把正方形切成小方格")
        self.play(
            *[Indicate(c, scale_factor=1.1, color=WHITE) for c in sq_red],
            lag_ratio=0.06, run_time=2.4,
        )
        self.play(
            *[Indicate(c, scale_factor=1.1, color=WHITE) for c in sq_green],
            lag_ratio=0.09, run_time=1.6,
        )
        self.finish_section(4)

        # ============ 5. 9 + 16 = 25 ============
        self.start_section(5, "数一数：一共几个小方格？")
        eq2 = txt("9 + 16 = 25", size=46, color=GOLD).move_to([2.9, 2.35, 0])
        self.play(Transform(eq, eq2), run_time=0.9)
        cells_hint = txt("25 个小方格", size=34, color=WHITE).move_to([2.9, 1.25, 0])
        self.play(Transform(answer, cells_hint), run_time=0.8)
        self.play(Indicate(sq_blue, color=WHITE, scale_factor=1.02), run_time=1.2)
        self.finish_section(5)

        # ============ 6. 搬进大正方形 ============
        self.start_section(6, "搬进斜边上的大正方形")
        targets = [
            A_PT + (i + 0.5) * U * E1_C + (j + 0.5) * U * E2_C
            for j in range(5) for i in range(5)
        ]
        sources = list(sq_red) + list(sq_green)      # 16 + 9 = 25
        assert len(sources) == 25

        # 留下原来两个正方形的虚线轮廓，方便对比
        ghost_red = DashedVMobject(
            Polygon(C_PT, A_PT, A_PT + np.array([-V_LEN * U, 0, 0]),
                    C_PT + np.array([-V_LEN * U, 0, 0]), color=C_RED, stroke_width=2),
            num_dashes=48,
        ).set_opacity(0.5)
        ghost_green = DashedVMobject(
            Polygon(C_PT, B_PT, B_PT + np.array([0, -H_LEN * U, 0]),
                    C_PT + np.array([0, -H_LEN * U, 0]), color=C_GREEN, stroke_width=2),
            num_dashes=40,
        ).set_opacity(0.5)
        self.add(ghost_red, ghost_green)

        self.play(FadeOut(area_16), FadeOut(area_9), FadeOut(area_25), FadeOut(lab_3), run_time=0.6)
        self.play(
            *[cell.animate(path_arc=PI / 8).move_to(t).rotate(C_ANG)
              for cell, t in zip(sources, targets)],
            lag_ratio=0.02, run_time=4.6,
        )

        border_c = Polygon(
            A_PT, B_PT, B_PT + E2_C * 5 * U, A_PT + E2_C * 5 * U,
            color=C_BLUE, stroke_width=4, fill_opacity=0,
        )
        self.play(Create(border_c), run_time=1.0)
        filled = txt("正好 25 格", size=40, color=GOLD).move_to([2.9, 1.25, 0])
        self.play(Transform(answer, filled), run_time=0.8)
        self.finish_section(6)

        # ============ 7. 面积之和相等 ============
        self.start_section(7, "两个小正方形面积之和 = 大正方形面积", size=32)
        eq3 = txt("9 + 16 = 25", size=46, color=GOLD).move_to([2.9, 2.35, 0])
        self.play(Transform(eq, eq3), run_time=0.7)
        self.play(Indicate(sq_red, color=WHITE, scale_factor=1.03), run_time=1.1)
        self.play(Indicate(sq_green, color=WHITE, scale_factor=1.03), run_time=1.1)
        self.play(Indicate(sq_blue, color=WHITE, scale_factor=1.02), run_time=1.1)
        self.finish_section(7)

        # ============ 8. a² + b² = c² ============
        self.start_section(8, None)
        everything = VGroup(
            ground_line, wall_line, ladder, lab_3, lab_4, lab_q, tri, right_angle,
            sq_red, sq_green, sq_blue, border_c, area_16, area_9, area_25,
            ghost_red, ghost_green, eq, answer,
        )
        formula = txt("a² + b² = c²", size=88, color=GOLD).move_to([0, 0.55, 0])
        rule = txt("勾股定理", size=46, color=WHITE).next_to(formula, UP, buff=0.55)
        note = txt("直角三角形，两条直角边的平方和，等于斜边的平方",
                   size=27, color=GREY_A).next_to(formula, DOWN, buff=0.6)
        example = txt("例如：3² + 4² = 5²", size=30, color=C_GREEN).next_to(note, DOWN, buff=0.3)

        self.play(FadeOut(everything), run_time=1.1)
        self.play(FadeIn(rule, shift=DOWN * 0.15), run_time=0.6)
        self.play(Write(formula), run_time=1.4)
        self.play(FadeIn(note, shift=UP * 0.1), FadeIn(example, shift=UP * 0.1), run_time=0.9)
        self.finish_section(8)

        self.play(FadeOut(formula), FadeOut(rule), FadeOut(note),
                  FadeOut(example), run_time=1.2)