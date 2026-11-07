# -*- coding: utf-8 -*-
"""分类与整理：先定标准，再分组，最后数一数。一年级上册「分类」。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403

CLR = {"red": RED, "blue": BLUE, "yellow": GOLD}
CN = {"red": "红色", "blue": "蓝色", "yellow": "黄色"}
SHAPE_CN = {"circle": "圆", "triangle": "三角形", "square": "正方形"}

# 9 件玩具：(颜色, 形状) —— 红 4 / 蓝 3 / 黄 2，圆 3 / 三角 3 / 正方 3
ITEMS = [
    ("red", "circle"), ("red", "circle"), ("red", "triangle"), ("red", "square"),
    ("blue", "circle"), ("blue", "triangle"), ("blue", "square"),
    ("yellow", "triangle"), ("yellow", "square"),
]

SCATTER = [
    (-5.4, 1.6), (-3.9, 0.9), (-2.4, 1.8), (-0.9, 0.8), (0.6, 1.5),
    (2.1, 0.7), (3.6, 1.7), (5.0, 0.9), (4.2, -0.4),
]

COL_X = [-3.9, 0.0, 3.9]
COL_Y = [1.15, 0.4, -0.35, -1.1]
SHAPE_Y = [1.0, 0.1, -0.8]


def make_shape(kind: str, color: str):
    if kind == "circle":
        return Circle(radius=0.28, color=color, stroke_width=2.6,
                      fill_color=color, fill_opacity=0.85)
    if kind == "triangle":
        return Polygon([-0.32, -0.26, 0], [0.32, -0.26, 0], [0.0, 0.34, 0],
                       color=color, stroke_width=2.6,
                       fill_color=color, fill_opacity=0.85)
    return Square(side_length=0.56, color=color, stroke_width=2.6,
                  fill_color=color, fill_opacity=0.85)


class FenleiScene(NarratedScene):
    lesson = "fenlei-zhengli"

    def clear_stage(self, run_time: float = 0.5):
        keep = {id(self._track), id(self._fill)}
        junk = [m for m in self.mobjects if id(m) not in keep]
        if junk:
            self.play(*[FadeOut(m) for m in junk], run_time=run_time)
        self.cur_title = None
        self.cur_sub = None

    def construct(self):
        # ---------------- 0. 玩具撒了一地 ----------------
        self.section(0, "玩具撒了一地")

        TILT = [-0.22, 0.15, 0.26, -0.12, 0.18, -0.25, 0.1, 0.2, -0.16]

        items = VGroup()
        for (color, kind), pos, ang in zip(ITEMS, SCATTER, TILT):
            m = make_shape(kind, CLR[color])
            m.move_to([pos[0], pos[1], 0])
            m.rotate(ang)
            items.add(m)
        self.play(LaggedStart(*[GrowFromCenter(m) for m in items], lag_ratio=0.07),
                  run_time=1.4)

        q = txt("想找一块红色的积木，怎么找？", size=34, color=CHALK).move_to([0, -2.25, 0])
        self.play(FadeIn(q, shift=UP * 0.1), run_time=0.6)
        self.finish_section()

        # ---------------- 1. 按颜色分 ----------------
        self.section(1, "先按颜色分：红、蓝、黄")
        self.play(FadeOut(q), run_time=0.3)

        seen = {"red": 0, "blue": 0, "yellow": 0}
        targets = []
        for color, _kind in ITEMS:
            targets.append([COL_X[{"red": 0, "blue": 1, "yellow": 2}[color]],
                            COL_Y[seen[color]], 0])
            seen[color] += 1

        moves = [m.animate.move_to(t) for m, t in zip(items, targets)]
        self.play(*moves, lag_ratio=0.04, run_time=1.6)

        col_labels = VGroup()
        for i, key in enumerate(["red", "blue", "yellow"]):
            lab = txt(CN[key], size=32, color=CLR[key]).move_to([COL_X[i], 2.05, 0])
            col_labels.add(lab)
        self.play(LaggedStart(*[FadeIn(l, shift=DOWN * 0.1) for l in col_labels], lag_ratio=0.2),
                  run_time=0.8)
        self.finish_section()

        # ---------------- 2. 数一数 ----------------
        self.section(2, "数一数：4 个、3 个、2 个")
        counts = [4, 3, 2]
        big = VGroup()
        for i, n in enumerate(counts):
            num = txt(f"{n} 个", size=40, color=CLR[["red", "blue", "yellow"][i]])
            num.move_to([COL_X[i], -1.85, 0])
            big.add(num)
        self.play(LaggedStart(*[FadeIn(b, shift=UP * 0.08) for b in big], lag_ratio=0.2),
                  run_time=1.0)
        self.play(LaggedStart(*[Indicate(items[i], color=WHITE, scale_factor=1.05)
                                for i in range(2)], lag_ratio=0.3), run_time=0.6)
        self.finish_section()

        # ---------------- 3. 排成小柱子 ----------------
        self.section(3, "排成柱子，谁多谁少一眼看出")
        self.play(FadeOut(big), run_time=0.35)

        base_y = -1.55
        unit = 0.55
        bars = VGroup()
        bar_labs = VGroup()
        top_labs = VGroup()
        for i, n in enumerate(counts):
            key = ["red", "blue", "yellow"][i]
            h = n * unit
            bar = Rectangle(width=1.0, height=h, color=CLR[key], stroke_width=0,
                            fill_color=CLR[key], fill_opacity=0.75)
            bar.move_to([COL_X[i], base_y + h / 2, 0])
            bars.add(bar)
            top_labs.add(txt(str(n), size=30, color=CLR[key]).move_to([COL_X[i], base_y + h + 0.28, 0]))
            bar_labs.add(txt(CN[key], size=26, color=DIM).move_to([COL_X[i], -2.0, 0]))

        self.play(
            *[FadeOut(m) for m in items],
            *[FadeOut(l) for l in col_labels],
            run_time=0.5,
        )
        self.play(LaggedStart(*[GrowFromEdge(b, DOWN) for b in bars], lag_ratio=0.2),
                  run_time=1.2)
        self.play(FadeIn(top_labs), FadeIn(bar_labs), run_time=0.6)

        most = txt("红色最多，黄色最少", size=30, color=GREEN).move_to([0, 2.3, 0])
        self.play(FadeIn(most, shift=DOWN * 0.08), run_time=0.6)
        self.finish_section()

        # ---------------- 4. 换标准：按形状分 ----------------
        self.section(4, "换个标准：按形状分")
        self.play(*[FadeOut(b) for b in bars], FadeOut(top_labs), FadeOut(bar_labs),
                  FadeOut(most), run_time=0.5)

        shape_idx = {"circle": 0, "triangle": 1, "square": 2}
        seen_shape = {"circle": 0, "triangle": 0, "square": 0}
        for idx, (m, (color, kind)) in enumerate(zip(items, ITEMS)):
            cx = COL_X[shape_idx[kind]]
            cy = SHAPE_Y[seen_shape[kind]]
            seen_shape[kind] += 1
            m.move_to([cx, cy, 0])
            m.rotate(-TILT[idx])

        self.play(*[FadeIn(m) for m in items], lag_ratio=0.03, run_time=0.9)

        shape_labels = VGroup()
        for i, kind in enumerate(["circle", "triangle", "square"]):
            lab = txt(f"{SHAPE_CN[kind]} · 3 个", size=30, color=CHALK)
            lab.move_to([COL_X[i], 1.95, 0])
            shape_labels.add(lab)
        self.play(LaggedStart(*[FadeIn(l, shift=DOWN * 0.08) for l in shape_labels],
                              lag_ratio=0.2), run_time=0.9)

        same = txt("标准不同，分法不同", size=28, color=GOLD).move_to([0, -1.95, 0])
        self.play(FadeIn(same), run_time=0.5)
        self.finish_section()

        # ---------------- 5. 总数不变 ----------------
        self.section(5, "分法不同，总数不变")
        self.play(FadeOut(same), *[FadeOut(m) for m in items], FadeOut(shape_labels),
                  run_time=0.5)

        l1 = txt("按颜色：4 + 3 + 2 = 9", size=42, color=CHALK).move_to([0, 1.15, 0])
        l2 = txt("按形状：3 + 3 + 3 = 9", size=42, color=CHALK).move_to([0, 0.05, 0])
        self.play(Write(l1), run_time=0.8)
        self.play(Write(l2), run_time=0.8)

        total = txt("都是 9 个，一个也没多，一个也没少", size=32, color=GREEN).move_to([0, -1.25, 0])
        self.play(FadeIn(total, shift=UP * 0.1), run_time=0.7)
        self.finish_section()

        # ---------------- 6. 三步法 ----------------
        self.section(6, "三步：定标准 → 分组 → 数一数")
        self.play(FadeOut(l1), FadeOut(l2), FadeOut(total), run_time=0.5)

        steps = ["1 定标准", "2 分组", "3 数一数"]
        boxes = VGroup()
        for i, s in enumerate(steps):
            boxes.add(label_box(s, size=30, color=GOLD if i == 2 else CHALK,
                                pad_x=0.3, pad_y=0.18))
        boxes.arrange(RIGHT, buff=0.75).move_to([0, 0.6, 0])
        self.play(LaggedStart(*[FadeIn(b, shift=UP * 0.08) for b in boxes], lag_ratio=0.25),
                  run_time=1.0)

        for i in range(2):
            a = boxes[i].get_right()
            b = boxes[i + 1].get_left()
            self.play(GrowArrow(Arrow(a, b, color=GOLD, stroke_width=3, buff=0.15,
                                      max_tip_length_to_length_ratio=0.2)), run_time=0.35)

        final = txt("分类，是为了看得清、数得快", size=34, color=GREEN).move_to([0, -1.1, 0])
        self.play(FadeIn(final, shift=UP * 0.08), run_time=0.7)
        self.finish_section()

        self.clear_stage(0.8)