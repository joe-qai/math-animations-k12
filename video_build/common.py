# -*- coding: utf-8 -*-
"""
课时动画的公共脚手架。

- 统一黑板深色背景、粉笔字配色
- 按段落读取 edge-tts 的 timings.json，逐段注入声音
- 每段自带底部字幕，讲完自动补齐等待，保证"话音落、画面才走"
- 顶部一条进度线，方便学生知道讲到哪儿了
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
from manim import *

BG = "#0f1220"          # 黑板背景（与已完成的勾股定理视频保持一致）
CHALK = "#f4efe2"       # 粉笔白
DIM = "#94a3a0"         # 次要说明
GOLD = "#f2c14e"        # 粉笔黄：标题 / 关键公式
RED = RED_C             # #FC6255
GREEN = GREEN_C         # #83C167
BLUE = BLUE_C           # #58C4DD
ORANGE = "#e8813a"
PURPLE = "#b39ddb"

FONT = "Microsoft YaHei"
AUDIO_ROOT = Path(__file__).resolve().parent / "audio"
FRAME_W = 14.22
FRAME_H = 8.0
TOP_Y = 3.45
SUB_BOTTOM = 0.28


def txt(s: str, size: int = 30, color: str = CHALK, weight: str = NORMAL, **kw) -> Text:
    """中文文本，统一字体。"""
    try:
        return Text(s, font=FONT, font_size=size, color=color, weight=weight, **kw)
    except Exception:
        return Text(s, font_size=size, color=color, weight=weight, **kw)


def fit(mob: Mobject, width: float = 12.4) -> Mobject:
    if mob.width > width:
        mob.scale_to_fit_width(width)
    return mob


def label_box(
    s: str,
    size: int = 30,
    color: str = CHALK,
    pad_x: float = 0.26,
    pad_y: float = 0.16,
    radius: float = 0.12,
    fill: str | None = None,
    fill_opacity: float = 0.12,
) -> VGroup:
    """带底色的文字小卡片。"""
    t = txt(s, size=size, color=color)
    box = RoundedRectangle(
        corner_radius=radius,
        width=t.width + pad_x * 2,
        height=t.height + pad_y * 2,
        stroke_color=color,
        stroke_width=1.6,
        fill_color=fill or color,
        fill_opacity=fill_opacity,
    )
    box.move_to(t)
    return VGroup(box, t)


class NarratedScene(Scene):
    """所有课时场景的基类。子类只需实现 construct()。"""

    lesson = ""          # 对应 audio/<lesson>/ 目录名
    total_sections = 7

    def setup(self) -> None:
        super().setup()
        self.camera.background_color = BG
        path = AUDIO_ROOT / self.lesson / "timings.json"
        self.timings = json.loads(path.read_text(encoding="utf-8"))
        self.total_sections = len(self.timings)
        self._t0 = 0.0
        self.cur_title: Mobject | None = None
        self.cur_sub: Mobject | None = None

        # 顶部进度线
        self._track = Line(
            [-FRAME_W / 2, 3.96, 0], [FRAME_W / 2, 3.96, 0],
            color=WHITE, stroke_width=2, stroke_opacity=0.16,
        )
        self._fill = Line(
            [-FRAME_W / 2, 3.96, 0], [-FRAME_W / 2 + 0.01, 3.96, 0],
            color=GOLD, stroke_width=4,
        )
        self.add(self._track, self._fill)

    # ---------- 声音与时间 ----------
    def begin(self, idx: int) -> None:
        self._t0 = self.renderer.time
        sound = (AUDIO_ROOT / self.lesson / f"seg_{idx:02d}.mp3").resolve()
        self.add_sound(str(sound))

    def finish(self, idx: int) -> None:
        if self.cur_sub is not None:
            self.play(FadeOut(self.cur_sub), run_time=0.28)
            self.cur_sub = None
        used = self.renderer.time - self._t0
        pad = self.timings[idx]["duration"] - used - 0.04
        if pad > 0:
            self.wait(pad)

    def _progress(self, idx: int) -> None:
        x = -FRAME_W / 2 + FRAME_W * (idx + 1) / self.total_sections
        target = Line([-FRAME_W / 2, 3.96, 0], [x, 3.96, 0], color=GOLD, stroke_width=4)
        self.play(Transform(self._fill, target), run_time=0.3)

    # ---------- 段落 ----------
    def section(self, idx: int, title: str | None = None, title_size: int = 36) -> None:
        """开场：换标题 + 显示字幕 + 开始放音。"""
        if self.cur_title is not None:
            self.play(FadeOut(self.cur_title), run_time=0.28)
            self.cur_title = None

        if title:
            t = txt(title, size=title_size, color=GOLD)
            if t.width > 9.6:
                t.scale_to_fit_width(9.6)
            t.move_to([0, TOP_Y, 0])
            self.play(FadeIn(t, shift=DOWN * 0.08), run_time=0.35)
            self.cur_title = t

        sub = txt(self.timings[idx]["text"], size=25, color=CHALK)
        if sub.width > 12.4:
            sub.scale_to_fit_width(12.4)
        sub.to_edge(DOWN, buff=SUB_BOTTOM)
        self.play(FadeIn(sub, shift=UP * 0.08), run_time=0.35)
        self.cur_sub = sub

        self._progress(idx)
        self._last_idx = idx
        self.begin(idx)

    def finish_section(self) -> None:
        self.finish(self._last_idx)

    # ---------- 常用画面元素 ----------
    def header_note(self, s: str, color: str = DIM, size: int = 24) -> Text:
        m = fit(txt(s, size=size, color=color), 12.6)
        m.move_to([0, 2.62, 0])
        return m

    def formula(self, s: str, size: int = 60, color: str = GOLD, at=(0, -1.0, 0)) -> Text:
        m = fit(txt(s, size=size, color=color), 12.6)
        m.move_to(at)
        return m

    def rule(self, width: float = 3.2, color: str = GOLD) -> Line:
        return Line([-width / 2, 0, 0], [width / 2, 0, 0], color=color, stroke_width=3)

    def dot(self, x: float, y: float, color: str = BLUE, r: float = 0.15) -> Dot:
        return Dot([x, y, 0], radius=r, color=color)

    def cell(self, x: float, y: float, w: float, h: float, color: str,
             fill_opacity: float = 0.18, stroke_width: float = 2.0) -> Rectangle:
        return Rectangle(
            width=w, height=h, color=color,
            fill_color=color, fill_opacity=fill_opacity,
            stroke_width=stroke_width,
        ).move_to([x, y, 0])

    def arrow(self, start, end, color: str = GOLD, width: float = 3.0) -> Arrow:
        return Arrow(
            np.array(start), np.array(end), color=color,
            stroke_width=width, buff=0,
            max_tip_length_to_length_ratio=0.12,
        )