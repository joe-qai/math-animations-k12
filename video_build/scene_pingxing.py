# -*- coding: utf-8 -*-
"""平行四边形的认识与梯形：对边平行、高与底、等腰梯形、四边形关系。四年级下册。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


def tick_marks(p, q, count: int = 1, color: str = CHALK,
               stroke: float = 2.2) -> VGroup:
    """在线段 p-q 的中点画 count 条垂直小短线，表示「相等 / 平行」。"""
    pa = np.array(p, dtype=float)
    qa = np.array(q, dtype=float)
    mid = (pa + qa) / 2.0
    d = qa - pa
    d = d / np.linalg.norm(d)
    n = np.array([-d[1], d[0], 0.0])
    g = VGroup()
    for i in range(count):
        c = mid + (i - (count - 1) / 2.0) * d * 0.16
        g.add(Line(c - n * 0.13 + d * 0.05, c + n * 0.13 - d * 0.05,
                   color=color, stroke_width=stroke))
    return g


def para_vertices(shift=(0.0, 0.0), rot: float = 0.0):
    """顶点按「边长不变、只改变倾斜角」构造，方便演示不稳定性。"""
    A = np.array([-4.9, 1.25, 0.0])
    u = np.array([4.8, 0.0, 0.0])
    v = np.array([1.2, -2.0, 0.0])
    if rot:
        c, s = np.cos(rot), np.sin(rot)
        v = np.array([v[0] * c - v[1] * s, v[0] * s + v[1] * c, 0.0])
    off = np.array([shift[0], shift[1], 0.0])
    return [A + off, A + u + off, A + u + v + off, A + v + off]


class PingxingSibianxingScene(NarratedScene):
    lesson = "pingxing-sibianxing"

    def clear_stage(self, run_time: float = 0.5):
        keep = {id(self._track), id(self._fill)}
        junk = [m for m in self.mobjects if id(m) not in keep]
        if junk:
            self.play(*[FadeOut(m) for m in junk], run_time=run_time)
        self.cur_title = None
        self.cur_sub = None

    # ---------------- 0. 生活里的平行四边形和梯形 ---------------- 16.8
    def scene_story(self):
        self.section(0, "伸缩门、篱笆、梯子")

        # 左：伸缩门（交叉的菱形格子）
        rails = VGroup(
            Line([-6.2, 1.55, 0], [-2.5, 1.55, 0], color=CHALK, stroke_width=3.4),
            Line([-6.2, -0.15, 0], [-2.5, -0.15, 0], color=CHALK, stroke_width=3.4),
        )
        self.play(Create(rails), run_time=0.9)

        bars = VGroup()
        n = 4
        for i in range(n):
            x0 = -6.0 + i * 0.9
            bars.add(Line([x0, -0.15, 0], [x0 + 0.9, 1.55, 0],
                          color=GOLD, stroke_width=2.4))
            bars.add(Line([x0, 1.55, 0], [x0 + 0.9, -0.15, 0],
                          color=GOLD, stroke_width=2.4))
        self.play(LaggedStart(*[Create(b) for b in bars], lag_ratio=0.06), run_time=1.6)
        l1 = txt("伸缩门：一格一格在变形", size=22, color=GOLD).move_to([-4.35, -0.72, 0])
        self.play(FadeIn(l1, shift=UP * 0.05), run_time=0.7)

        # 中：篱笆（平行四边形网格）
        fence = VGroup()
        for i in range(3):
            for j in range(2):
                x = -1.55 + i * 0.85 + j * 0.0
                y = 1.3 - j * 0.85
                fence.add(Polygon([x, y, 0], [x + 0.85, y, 0],
                                  [x + 1.15, y - 0.85, 0], [x + 0.3, y - 0.85, 0],
                                  color=GREEN, stroke_width=2.0))
        self.play(LaggedStart(*[Create(f) for f in fence], lag_ratio=0.1), run_time=1.8)
        l2 = txt("篱笆：一个个平行四边形", size=22, color=GREEN).move_to([-0.2, -0.72, 0])
        self.play(FadeIn(l2, shift=UP * 0.05), run_time=0.7)

        # 右：梯子（梯形）
        lad = Polygon([3.15, 1.6, 0], [4.15, 1.6, 0],
                      [5.5, -0.3, 0], [1.9, -0.3, 0],
                      color=BLUE, stroke_width=3.0)
        self.play(Create(lad), run_time=1.0)
        rungs = VGroup()
        for i in range(5):
            t = 0.16 + i * 0.17
            y = 1.6 + (t) * (-1.9)
            xl = 3.15 + t * (1.9 - 3.15)
            xr = 4.15 + t * (5.5 - 4.15)
            rungs.add(Line([xl, y, 0], [xr, y, 0], color=BLUE, stroke_width=2.0))
        self.play(LaggedStart(*[Create(r) for r in rungs], lag_ratio=0.12), run_time=1.5)
        l3 = txt("梯子：只有两条边平行", size=22, color=BLUE).move_to([3.7, -0.78, 0])
        self.play(FadeIn(l3, shift=UP * 0.05), run_time=0.7)

        note = txt("同样是四边形，边的平行关系不一样", size=27, color=GOLD)
        note.move_to([0, -2.15, 0])
        self.play(FadeIn(note, shift=UP * 0.08), run_time=0.9)
        self.finish_section()

    # ---------------- 1. 平行四边形的特征 ---------------- 16.9
    def scene_para(self):
        self.section(1, "两组对边分别平行且相等")

        vs = para_vertices(shift=(-0.9, 0.35))
        shape = Polygon(*vs, color=GOLD, stroke_width=3.2,
                        fill_color=GOLD, fill_opacity=0.1)
        self.play(Create(shape), run_time=1.1)

        # 上下两条边：双短线
        t_top = tick_marks(vs[0], vs[1], 2, color=BLUE)
        t_bot = tick_marks(vs[3], vs[2], 2, color=BLUE)
        self.play(Create(t_top), Create(t_bot), run_time=0.8)
        # 左右两条边：单短线
        t_left = tick_marks(vs[0], vs[3], 1, color=GREEN)
        t_right = tick_marks(vs[1], vs[2], 1, color=GREEN)
        self.play(Create(t_left), Create(t_right), run_time=0.8)

        r1 = label_box("两组对边分别平行", size=25, color=BLUE)
        r2 = label_box("两组对边分别相等", size=25, color=GREEN)
        r3 = label_box("容易变形：不稳定", size=25, color=ORANGE)
        right = VGroup(r1, r2, r3).arrange(DOWN, buff=0.32).move_to([4.15, 0.75, 0])
        for r in right:
            self.play(FadeIn(r, shift=LEFT * 0.08), run_time=0.65)
            self.wait(0.35)

        # 推一推：边长不变，形状改变
        tilted_vs = para_vertices(shift=(-0.9, 0.35), rot=-0.52)
        tilted = Polygon(*tilted_vs, color=ORANGE, stroke_width=3.0,
                         fill_color=ORANGE, fill_opacity=0.1)
        tt_top = tick_marks(tilted_vs[0], tilted_vs[1], 2, color=BLUE)
        tt_bot = tick_marks(tilted_vs[3], tilted_vs[2], 2, color=BLUE)
        tt_left = tick_marks(tilted_vs[0], tilted_vs[3], 1, color=GREEN)
        tt_right = tick_marks(tilted_vs[1], tilted_vs[2], 1, color=GREEN)

        core = VGroup(shape, t_top, t_bot, t_left, t_right)
        core_tilted = VGroup(tilted, tt_top, tt_bot, tt_left, tt_right)
        self.play(Transform(core, core_tilted), run_time=1.2)
        self.play(Transform(core, VGroup(
            Polygon(*vs, color=GOLD, stroke_width=3.2,
                    fill_color=GOLD, fill_opacity=0.1),
            tick_marks(vs[0], vs[1], 2, color=BLUE),
            tick_marks(vs[3], vs[2], 2, color=BLUE),
            tick_marks(vs[0], vs[3], 1, color=GREEN),
            tick_marks(vs[1], vs[2], 1, color=GREEN),
        )), run_time=1.1)

        arr = Arrow([-0.9, -1.35, 0], [-0.1, -1.35, 0], color=ORANGE,
                    stroke_width=2.6, buff=0, max_tip_length_to_length_ratio=0.22)
        tag = txt("推一推：边长没变，形状变了", size=25, color=ORANGE)
        tag.move_to([0.4, -1.95, 0])
        self.play(GrowArrow(arr), run_time=0.7)
        self.play(FadeIn(tag, shift=UP * 0.06), run_time=0.8)
        self.finish_section()

    # ---------------- 2. 底和高 ---------------- 15.1
    def scene_height(self):
        self.section(2, "从一条边上的点，向对边作垂线")

        vs = para_vertices(shift=(-1.1, 0.55))
        shape = Polygon(*vs, color=CHALK, stroke_width=3.0)
        self.play(Create(shape), run_time=1.0)

        base = Line(vs[3], vs[2], color=GOLD, stroke_width=5)
        self.play(Create(base), run_time=0.8)
        base_lab = txt("底", size=28, color=GOLD).move_to([-0.7, -0.7, 0])
        self.play(FadeIn(base_lab, shift=UP * 0.05), run_time=0.6)

        # 底上取一点，向上作垂线段
        px = -1.15
        p_bot = np.array([px, -0.95 + 0.55, 0])
        p_top = np.array([px, 1.05 + 0.55, 0])
        dash = DashedLine(p_top, p_bot, color=RED, stroke_width=2.8)
        self.play(Create(dash), run_time=1.0)

        s = 0.26
        sq = Polygon([px, p_bot[1], 0], [px + s, p_bot[1], 0],
                     [px + s, p_bot[1] + s, 0], [px, p_bot[1] + s, 0],
                     color=RED, stroke_width=2.0)
        self.play(Create(sq), run_time=0.6)

        h_lab = txt("高", size=28, color=RED).move_to([px + 0.75, 0.3, 0])
        top_dot = Dot(p_top, radius=0.08, color=RED)
        self.play(FadeIn(top_dot), FadeIn(h_lab), run_time=0.7)

        # 多条高：说明有无数条
        for qx in (-3.55, -2.35, -0.7):
            g = DashedLine([qx, p_top[1], 0], [qx, p_bot[1], 0],
                           color=DIM, stroke_width=2.0)
            self.play(Create(g), run_time=0.5)

        n1 = txt("高和对边必须互相垂直", size=27, color=GREEN).move_to([0, -1.85, 0])
        n2 = txt("平行四边形有无数条高", size=26, color=DIM).move_to([0, -2.5, 0])
        self.play(FadeIn(n1, shift=UP * 0.07), run_time=0.8)
        self.play(FadeIn(n2, shift=UP * 0.06), run_time=0.8)
        self.finish_section()

    # ---------------- 3. 梯形 ---------------- 15.6
    def scene_trap(self):
        self.section(3, "梯形：只有一组对边平行")

        top = np.array([-3.5, 1.05, 0])
        top_r = np.array([-0.5, 1.05, 0])
        bot = np.array([-4.4, -0.95, 0])
        bot_r = np.array([0.7, -0.95, 0])
        trap = Polygon(top, top_r, bot_r, bot, color=BLUE, stroke_width=3.2,
                       fill_color=BLUE, fill_opacity=0.1)
        self.play(Create(trap), run_time=1.1)

        t_top = tick_marks(top, top_r, 2, color=GOLD)
        t_bot = tick_marks(bot, bot_r, 2, color=GOLD)
        self.play(Create(t_top), Create(t_bot), run_time=0.8)

        up = txt("上底", size=25, color=GOLD).move_to([-2.0, 1.45, 0])
        dn = txt("下底", size=25, color=GOLD).move_to([-1.8, -1.42, 0])
        leg1 = txt("腰", size=24, color=GREEN).move_to([-4.55, 0.05, 0])
        leg2 = txt("腰", size=24, color=GREEN).move_to([0.66, 0.1, 0])
        self.play(FadeIn(up), FadeIn(dn), run_time=0.7)
        self.play(FadeIn(leg1), FadeIn(leg2), run_time=0.7)

        hx = -1.55
        hd = DashedLine([hx, 1.05, 0], [hx, -0.95, 0], color=RED, stroke_width=2.6)
        s = 0.24
        sq = Polygon([hx, -0.95, 0], [hx + s, -0.95, 0],
                     [hx + s, -0.95 + s, 0], [hx, -0.95 + s, 0],
                     color=RED, stroke_width=1.9)
        hl = txt("高", size=24, color=RED).move_to([hx - 0.42, -0.1, 0])
        self.play(Create(hd), run_time=0.8)
        self.play(Create(sq), FadeIn(hl), run_time=0.7)

        # 右侧：等腰梯形
        it = Polygon([2.7, 1.05, 0], [4.4, 1.05, 0], [5.15, -0.95, 0], [1.95, -0.95, 0],
                     color=PURPLE, stroke_width=3.0,
                     fill_color=PURPLE, fill_opacity=0.1)
        self.play(Create(it), run_time=1.0)
        it_l = tick_marks([2.7, 1.05, 0], [1.95, -0.95, 0], 1, color=PURPLE)
        it_r = tick_marks([4.4, 1.05, 0], [5.15, -0.95, 0], 1, color=PURPLE)
        self.play(Create(it_l), Create(it_r), run_time=0.7)
        it_lab = txt("等腰梯形", size=25, color=PURPLE).move_to([3.55, -1.5, 0])
        self.play(FadeIn(it_lab, shift=UP * 0.05), run_time=0.7)

        note = txt("另一组对边不平行，所以梯形不是平行四边形", size=25, color=DIM)
        note.move_to([0, -2.35, 0])
        self.play(FadeIn(note, shift=UP * 0.06), run_time=0.9)
        self.finish_section()

    # ---------------- 4. 四边形家族 ---------------- 19.1
    def scene_family(self):
        self.section(4, "四边形家族：谁包含谁")

        root = label_box("四边形", size=27, color=CHALK).move_to([-5.35, 0.35, 0])
        para = label_box("平行四边形", size=26, color=GOLD).move_to([-1.75, 1.75, 0])
        trap = label_box("梯形", size=26, color=BLUE).move_to([-1.75, -0.85, 0])
        rect = label_box("长方形", size=26, color=GREEN).move_to([1.55, 1.75, 0])
        sq = label_box("正方形", size=26, color=PURPLE).move_to([4.55, 1.75, 0])

        self.play(FadeIn(root, scale=0.95), run_time=0.7)
        a1 = Arrow([-4.5, 0.72, 0], [-2.9, 1.5, 0], color=DIM, stroke_width=2.2,
                   buff=0.06, max_tip_length_to_length_ratio=0.2)
        a2 = Arrow([-4.5, 0.0, 0], [-2.9, -0.62, 0], color=DIM, stroke_width=2.2,
                   buff=0.06, max_tip_length_to_length_ratio=0.2)
        self.play(GrowArrow(a1), FadeIn(para, scale=0.95), run_time=0.9)
        self.play(GrowArrow(a2), FadeIn(trap, scale=0.95), run_time=0.9)

        a3 = Arrow([-0.62, 1.75, 0], [0.42, 1.75, 0], color=DIM, stroke_width=2.2,
                   buff=0.06, max_tip_length_to_length_ratio=0.2)
        self.play(GrowArrow(a3), FadeIn(rect, scale=0.95), run_time=0.9)

        a4 = Arrow([2.42, 1.75, 0], [3.42, 1.75, 0], color=DIM, stroke_width=2.2,
                   buff=0.06, max_tip_length_to_length_ratio=0.2)
        self.play(GrowArrow(a4), FadeIn(sq, scale=0.95), run_time=0.9)

        n1 = txt("长方形是特殊的平行四边形：四个角都是直角", size=24, color=GREEN)
        n1.move_to([1.35, 0.62, 0])
        self.play(FadeIn(n1, shift=UP * 0.05), run_time=0.8)

        n2 = txt("正方形又是特殊的长方形：四条边都相等", size=24, color=PURPLE)
        n2.move_to([2.2, 0.05, 0])
        self.play(FadeIn(n2, shift=UP * 0.05), run_time=0.8)

        n3 = txt("梯形只有一组对边平行，单独一支", size=24, color=BLUE)
        n3.move_to([1.5, -0.95, 0])
        self.play(FadeIn(n3, shift=UP * 0.05), run_time=0.8)

        tip = txt("正方形、长方形、平行四边形都有两组对边平行", size=25, color=GOLD)
        tip.move_to([0, -2.35, 0])
        self.play(FadeIn(tip, shift=UP * 0.07), run_time=0.9)
        self.finish_section()

    # ---------------- 5. 易错点 ---------------- 13.8
    def scene_warn(self):
        self.section(5, "三个易错点")

        # 左：斜线不是高
        left_shape = Polygon([-5.4, 1.5, 0], [-2.4, 1.5, 0],
                             [-1.8, 0.0, 0], [-4.8, 0.0, 0],
                             color=DIM, stroke_width=2.2)
        self.play(Create(left_shape), run_time=0.8)
        bad = Line([-3.9, 1.5, 0], [-2.9, 0.0, 0], color=RED, stroke_width=2.6)
        self.play(Create(bad), run_time=0.8)
        no = txt("错：斜线不是高", size=24, color=RED).move_to([-3.5, -0.62, 0])
        self.play(FadeIn(no, shift=UP * 0.05), run_time=0.7)

        # 右：等腰梯形的腰
        it = Polygon([2.55, 1.5, 0], [4.15, 1.5, 0],
                     [4.8, 0.0, 0], [1.9, 0.0, 0],
                     color=PURPLE, stroke_width=2.6)
        self.play(Create(it), run_time=0.9)
        it_l = tick_marks([2.55, 1.5, 0], [1.9, 0.0, 0], 1, color=PURPLE)
        it_r = tick_marks([4.15, 1.5, 0], [4.8, 0.0, 0], 1, color=PURPLE)
        self.play(Create(it_l), Create(it_r), run_time=0.7)
        yes = txt("对：两腰相等", size=24, color=GREEN).move_to([3.35, -0.62, 0])
        self.play(FadeIn(yes, shift=UP * 0.05), run_time=0.7)

        n1 = txt("高要垂直于底，斜着画的不算", size=26, color=GOLD)
        n1.move_to([0, -1.5, 0])
        n2 = txt("梯形是「只有一组」对边平行，另一组不能平行", size=26, color=CHALK)
        n2.move_to([0, -2.1, 0])
        n3 = txt("等腰梯形是两腰相等，不是两条底相等", size=26, color=CHALK)
        n3.move_to([0, -2.68, 0])
        self.play(FadeIn(n1, shift=UP * 0.06), run_time=0.8)
        self.play(FadeIn(n2, shift=UP * 0.05), run_time=0.8)
        self.play(FadeIn(n3, shift=UP * 0.05), run_time=0.8)
        self.finish_section()

    # ---------------- 6. 总结 ---------------- 13.0
    def scene_summary(self):
        self.section(6, "三句话记住它们")

        rows = VGroup(
            label_box("① 平行四边形：两组对边分别平行且相等", size=25, color=GOLD),
            label_box("② 梯形：只有一组对边平行", size=25, color=BLUE),
            label_box("③ 长方形、正方形是特殊的平行四边形", size=25, color=GREEN),
        ).arrange(DOWN, buff=0.34).move_to([0, 1.35, 0])
        for r in rows:
            self.play(FadeIn(r, shift=RIGHT * 0.07), run_time=0.7)
            self.wait(0.55)

        # 底线示意图：底与高
        base = Line([-4.6, -1.35, 0], [-1.1, -1.35, 0], color=GOLD, stroke_width=4)
        h = DashedLine([-3.0, -1.35, 0], [-3.0, -2.05, 0], color=RED, stroke_width=2.4)
        s = 0.2
        sq = Polygon([-3.0, -1.35, 0], [-3.0 + s, -1.35, 0],
                     [-3.0 + s, -1.35 + s, 0], [-3.0, -1.35 + s, 0],
                     color=RED, stroke_width=1.8)
        b_lab = txt("底", size=24, color=GOLD).move_to([-0.72, -1.32, 0])
        h_lab = txt("高", size=24, color=RED).move_to([-2.72, -1.78, 0])
        self.play(Create(base), Create(h), run_time=0.9)
        self.play(Create(sq), FadeIn(b_lab), FadeIn(h_lab), run_time=0.7)

        note = txt("底和高必须互相垂直", size=28, color=RED).move_to([2.35, -1.85, 0])
        self.play(FadeIn(note, shift=UP * 0.07), run_time=0.8)
        self.wait(0.9)
        self.finish_section()

    def construct(self):
        self.scene_story()
        self.clear_stage()
        self.scene_para()
        self.clear_stage()
        self.scene_height()
        self.clear_stage()
        self.scene_trap()
        self.clear_stage()
        self.scene_family()
        self.clear_stage()
        self.scene_warn()
        self.clear_stage()
        self.scene_summary()
        self.clear_stage(0.8)