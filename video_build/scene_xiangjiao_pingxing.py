# -*- coding: utf-8 -*-
"""相交线与平行线：对顶角、邻补角、垂线、三线八角、平行线的判定与性质。七年级下。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


def P(x, y):
    return np.array([float(x), float(y), 0.0])


def ang_arc(O, A, B, color=GOLD, radius=0.8, lab=None, lab_r=1.22,
            size=23, lab_color=None, width=2.6):
    """以 O 为顶点、OA 与 OB 为边的角弧，可带标签。"""
    o, a, b = P(*O), P(*A), P(*B)
    arc = Angle.from_three_points(a, o, b, radius=radius, color=color,
                                  stroke_width=width)
    grp = VGroup(arc)
    if lab:
        va, vb = a - o, b - o
        va = va / np.linalg.norm(va)
        vb = vb / np.linalg.norm(vb)
        d = va + vb
        if np.linalg.norm(d) < 1e-6:
            d = va
        d = d / np.linalg.norm(d)
        pos = o + d * lab_r
        grp.add(txt(lab, size=size, color=lab_color or color)
                .move_to([pos[0], pos[1], 0]))
    return grp


def right_angle(vertex, u, v, size=0.32, color=GOLD):
    """直角小方块。"""
    o = P(*vertex)
    uu = P(*u) - o
    vv = P(*v) - o
    uu = uu / np.linalg.norm(uu) * size
    vv = vv / np.linalg.norm(vv) * size
    pts = [o + uu, o + uu + vv, o + vv]
    m = VGroup(*[Line(pts[0], pts[1], color=color, stroke_width=2.2),
                 Line(pts[1], pts[2], color=color, stroke_width=2.2)])
    return m


class XiangjiaoPingxingScene(NarratedScene):
    lesson = "xiangjiao-pingxing"

    def clear_stage(self, run_time: float = 0.5):
        keep = {id(self._track), id(self._fill)}
        junk = [m for m in self.mobjects if id(m) not in keep]
        if junk:
            self.play(*[FadeOut(m) for m in junk], run_time=run_time)
        self.cur_title = None
        self.cur_sub = None

    # ---------------- 0. 铁轨与十字路口 ---------------- 26.8
    def scene_story(self):
        self.section(0, "铁轨与十字路口")

        rail1 = Line(P(-6.5, 1.25), P(-1.1, 1.25), color=GOLD, stroke_width=5)
        rail2 = Line(P(-6.5, 0.45), P(-1.1, 0.45), color=GOLD, stroke_width=5)
        self.play(Create(rail1), Create(rail2), run_time=1.4)
        sleepers = VGroup()
        for i in range(13):
            x = -6.35 + i * 0.42
            sleepers.add(Line(P(x, 0.45), P(x, 1.25), color=DIM, stroke_width=2))
        self.play(LaggedStart(*[FadeIn(s) for s in sleepers], lag_ratio=0.05),
                  run_time=1.6)

        lt = txt("两根铁轨，永远不相交", size=26, color=CHALK).move_to([-3.8, -0.45, 0])
        self.play(FadeIn(lt, shift=UP * 0.05), run_time=0.8)
        b1 = label_box("平行", size=30, color=GOLD).move_to([-3.8, -1.45, 0])
        self.play(FadeIn(b1, scale=0.97), run_time=0.9)

        road1 = Line(P(1.3, 1.05), P(6.5, 1.05), color=BLUE, stroke_width=5)
        road2 = Line(P(3.85, -0.65), P(3.85, 2.55), color=BLUE, stroke_width=5)
        self.play(Create(road1), Create(road2), run_time=1.4)
        dot = Dot(P(3.85, 1.05), radius=0.09, color=RED)
        self.play(FadeIn(dot, scale=0.6), run_time=0.6)
        self.play(Indicate(dot, color=RED, scale_factor=2.0), run_time=0.9)

        rt = txt("两条路，交叉出一个点", size=26, color=CHALK).move_to([3.85, -1.15, 0])
        self.play(FadeIn(rt, shift=UP * 0.05), run_time=0.8)
        b2 = label_box("相交", size=30, color=BLUE).move_to([3.85, -2.05, 0])
        self.play(FadeIn(b2, scale=0.97), run_time=0.9)

        tail = txt("同一平面内，两条直线要么相交，要么平行", size=27, color=GREEN)
        tail.move_to([0, -2.95, 0])
        self.play(FadeIn(tail, shift=UP * 0.05), run_time=1.0)
        self.wait(3.2)
        self.finish_section()

    # ---------------- 1. 邻补角与对顶角 ---------------- 26.4
    def scene_angles(self):
        self.section(1, "邻补角与对顶角")

        O = (-3.5, -0.55)
        l1a, l1b = (-6.3, -0.55), (-0.7, -0.55)
        l2a, l2b = (-5.5, 1.05), (-1.5, -2.15)

        L1 = Line(P(*l1a), P(*l1b), color=CHALK, stroke_width=3)
        self.play(Create(L1), run_time=1.1)
        L2 = Line(P(*l2a), P(*l2b), color=CHALK, stroke_width=3)
        self.play(Create(L2), run_time=1.1)
        self.play(FadeIn(Dot(P(*O), radius=0.07, color=RED)), run_time=0.5)

        ur = (1.0, 0.0)
        ul = (-1.0, 0.0)
        uu = (-0.76, 0.65)
        ud = (0.76, -0.65)

        a1 = ang_arc(O, ul, uu, color=GOLD, lab="∠1", lab_r=1.12)
        a2 = ang_arc(O, uu, ur, color=BLUE, lab="∠2", lab_r=1.12, lab_color=BLUE)
        a3 = ang_arc(O, ur, ud, color=GREEN, lab="∠3", lab_r=1.12, lab_color=GREEN)
        a4 = ang_arc(O, ud, ul, color=ORANGE, lab="∠4", lab_r=1.12, lab_color=ORANGE)
        for g in (a1, a2, a3, a4):
            self.play(FadeIn(g, scale=0.9), run_time=0.75)

        t1 = VGroup(
            txt("∠1 与 ∠2 相邻，拼成一条直线", size=25, color=CHALK),
            txt("∠1 + ∠2 = 180°", size=27, color=GOLD),
            txt("叫邻补角", size=24, color=DIM),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT).move_to([2.6, 1.35, 0])
        for m in t1:
            self.play(FadeIn(m, shift=UP * 0.05), run_time=0.8)

        t2 = VGroup(
            txt("∠1 与 ∠3 相对，开口一样大", size=25, color=CHALK),
            txt("∠1 = ∠3", size=27, color=GREEN),
            txt("叫对顶角", size=24, color=DIM),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT).move_to([2.6, -1.15, 0])
        for m in t2:
            self.play(FadeIn(m, shift=UP * 0.05), run_time=0.8)

        self.wait(2.6)
        self.finish_section()

    # ---------------- 2. 垂线与垂线段最短 ---------------- 22.0
    def scene_perp(self):
        self.section(2, "垂直与垂线段最短")

        L = Line(P(-6.2, -1.5), P(1.0, -1.5), color=CHALK, stroke_width=3)
        self.play(Create(L), run_time=1.1)

        A = (-2.4, 1.6)
        F = (-2.4, -1.5)
        self.play(FadeIn(Dot(P(*A), radius=0.08, color=GOLD)), run_time=0.5)
        self.play(FadeIn(txt("P", size=25, color=GOLD).move_to([-2.15, 1.85, 0])),
                  run_time=0.5)

        perp = Line(P(*A), P(*F), color=GREEN, stroke_width=3)
        self.play(Create(perp), run_time=1.0)
        ra = right_angle(F, (1, 0), (0, 1), size=0.34, color=GREEN)
        self.play(Create(ra), run_time=0.6)

        s1 = Line(P(*A), P(-5.6, -1.5), color=BLUE, stroke_width=2)
        s2 = Line(P(*A), P(0.4, -1.5), color=BLUE, stroke_width=2)
        self.play(Create(s1), Create(s2), run_time=1.2)
        self.play(Indicate(perp, color=GREEN, scale_factor=1.04), run_time=1.0)

        t1 = VGroup(
            txt("相交成直角，叫互相垂直", size=26, color=GREEN),
            txt("垂线段最短", size=30, color=GOLD),
        ).arrange(DOWN, buff=0.42).move_to([4.0, 1.3, 0])
        for m in t1:
            self.play(FadeIn(m, shift=UP * 0.05), run_time=0.9)

        t2 = txt("过马路走垂直的方向，路最短", size=25, color=DIM).move_to([4.0, -0.1, 0])
        self.play(FadeIn(t2, shift=UP * 0.05), run_time=0.8)

        note = txt("点到直线的距离，就是这个垂线段的长度", size=25, color=CHALK)
        note.move_to([0, -2.55, 0])
        self.play(FadeIn(note, shift=UP * 0.05), run_time=0.9)
        self.wait(2.8)
        self.finish_section()

    # ---------------- 3. 三线八角 ---------------- 31.3
    def scene_three_lines(self):
        self.section(3, "三条线，八个角")

        y1, y2 = 1.0, -1.0
        l1 = Line(P(-6.4, y1), P(0.6, y1), color=CHALK, stroke_width=3)
        l2 = Line(P(-6.4, y2), P(0.6, y2), color=CHALK, stroke_width=3)
        self.play(Create(l1), Create(l2), run_time=1.3)
        self.play(FadeIn(VGroup(
            txt("a", size=24, color=DIM).move_to([-6.75, y1, 0]),
            txt("b", size=24, color=DIM).move_to([-6.75, y2, 0]),
        )), run_time=0.6)

        ta, tb = P(-6.1, -2.35), P(-1.4, 2.35)
        tv = tb - ta
        k = tv[1] / tv[0]

        def x_on(y):
            return float(ta[0] + (y - ta[1]) / k)

        px, qx = x_on(y1), x_on(y2)
        tline = Line(ta, tb, color=GOLD, stroke_width=3)
        self.play(Create(tline), run_time=1.2)
        tp = txt("c", size=24, color=GOLD).move_to([-1.15, 2.5, 0])
        self.play(FadeIn(tp), run_time=0.5)

        Pp = (px, y1)
        Qq = (qx, y2)
        self.play(FadeIn(Dot(P(*Pp), radius=0.06, color=RED)),
                  FadeIn(Dot(P(*Qq), radius=0.06, color=RED)), run_time=0.7)

        ul, ur, dl, dr = (-1, 0), (1, 0), (-0.92, 0.38), (0.92, -0.38)
        angs = [
            (Pp, ul, dl, "1", GOLD, 8), (Pp, dr, ur, "2", BLUE, 8),
            (Pp, ur, ul, "3", GREEN, 8), (Pp, dl, dr, "4", ORANGE, 8),
        ]
        # 手工放置 1-4 与 5-8，避免弧方向判断出错
        def lab_at(v, dx, dy, s, color):
            return txt(s, size=23, color=color).move_to([v[0] + dx, v[1] + dy, 0])

        g1 = ang_arc(Pp, (px - 1.0, y1), (px - 0.5, y1 + 0.45), color=GOLD, radius=0.55)
        g2 = ang_arc(Pp, (px + 1.0, y1), (px + 0.5, y1 + 0.45), color=BLUE, radius=0.55)
        g3 = ang_arc(Pp, (px + 1.0, y1), (px + 0.5, y1 - 0.45), color=GREEN, radius=0.55)
        g4 = ang_arc(Pp, (px - 1.0, y1), (px - 0.5, y1 - 0.45), color=ORANGE, radius=0.55)
        g5 = ang_arc(Qq, (qx - 1.0, y2), (qx - 0.5, y2 + 0.45), color=GOLD, radius=0.55)
        g6 = ang_arc(Qq, (qx + 1.0, y2), (qx + 0.5, y2 + 0.45), color=BLUE, radius=0.55)
        g7 = ang_arc(Qq, (qx + 1.0, y2), (qx + 0.5, y2 - 0.45), color=GREEN, radius=0.55)
        g8 = ang_arc(Qq, (qx - 1.0, y2), (qx - 0.5, y2 - 0.45), color=ORANGE, radius=0.55)
        nums = VGroup(
            lab_at(Pp, -0.78, 0.42, "1", GOLD), lab_at(Pp, 0.78, 0.42, "2", BLUE),
            lab_at(Pp, 0.78, -0.42, "3", GREEN), lab_at(Pp, -0.78, -0.42, "4", ORANGE),
            lab_at(Qq, -0.78, 0.42, "5", GOLD), lab_at(Qq, 0.78, 0.42, "6", BLUE),
            lab_at(Qq, 0.78, -0.42, "7", GREEN), lab_at(Qq, -0.78, -0.42, "8", ORANGE),
        )
        self.play(LaggedStart(*[FadeIn(g, scale=0.85) for g in
                                (g1, g2, g3, g4, g5, g6, g7, g8)], lag_ratio=0.08),
                  run_time=2.4)
        self.play(LaggedStart(*[FadeIn(n, scale=0.8) for n in nums], lag_ratio=0.06),
                  run_time=1.8)

        rows = VGroup(
            VGroup(txt("同位角", size=26, color=GOLD), txt("∠1 与 ∠5（F 形）", size=25, color=CHALK)),
            VGroup(txt("内错角", size=26, color=BLUE), txt("∠4 与 ∠6（Z 形）", size=25, color=CHALK)),
            VGroup(txt("同旁内角", size=26, color=ORANGE), txt("∠4 与 ∠5（U 形）", size=25, color=CHALK)),
        )
        for i, r in enumerate(rows):
            r.arrange(RIGHT, buff=0.35).move_to([3.65, 1.5 - i * 1.15, 0])
            self.play(FadeIn(r, shift=RIGHT * 0.05), run_time=0.8)
            if i == 0:
                self.play(g1.animate.set_stroke(width=4.6), g5.animate.set_stroke(width=4.6),
                          run_time=0.5)
            elif i == 1:
                self.play(g4.animate.set_stroke(width=4.6), g6.animate.set_stroke(width=4.6),
                          run_time=0.5)
            else:
                self.play(g4.animate.set_stroke(width=4.6), g5.animate.set_stroke(width=4.6),
                          run_time=0.5)

        note = txt("记住形状，比背定义快", size=25, color=DIM).move_to([3.65, -2.35, 0])
        self.play(FadeIn(note, shift=UP * 0.05), run_time=0.8)
        self.wait(2.4)
        self.finish_section()

    # ---------------- 4. 平行线的判定 ---------------- 24.4
    def scene_judge(self):
        self.section(4, "平行线的判定：由角推平行")

        head = VGroup(
            txt("角的关系", size=27, color=DIM),
            txt("→", size=27, color=DIM),
            txt("两条直线平行", size=27, color=GOLD),
        ).arrange(RIGHT, buff=0.35).move_to([0, 2.35, 0])
        self.play(FadeIn(head, shift=UP * 0.05), run_time=0.9)

        items = [
            ("同位角相等", "两直线平行", GOLD),
            ("内错角相等", "两直线平行", BLUE),
            ("同旁内角互补", "两直线平行", ORANGE),
        ]
        y = 1.25
        for cond, res, col in items:
            left = label_box(cond, size=28, color=col)
            arrow = txt("⟹", size=30, color=DIM)
            right = txt(res, size=28, color=GREEN)
            row = VGroup(left, arrow, right).arrange(RIGHT, buff=0.4)
            row.move_to([0, y, 0])
            self.play(FadeIn(left, scale=0.97), run_time=0.7)
            self.play(FadeIn(arrow, shift=RIGHT * 0.05), run_time=0.5)
            self.play(FadeIn(right, shift=RIGHT * 0.05), run_time=0.7)
            y -= 1.15

        note = txt("反过来不一定成立，所以要先判断再下结论", size=25, color=DIM)
        note.move_to([0, -2.35, 0])
        self.play(FadeIn(note, shift=UP * 0.05), run_time=0.9)
        self.wait(3.0)
        self.finish_section()

    # ---------------- 5. 平行线的性质 ---------------- 26.7
    def scene_property(self):
        self.section(5, "平行线的性质：由平行推角")

        head = VGroup(
            txt("两条直线平行", size=27, color=GOLD),
            txt("→", size=27, color=DIM),
            txt("角的关系", size=27, color=DIM),
        ).arrange(RIGHT, buff=0.35).move_to([0, 2.35, 0])
        self.play(FadeIn(head, shift=UP * 0.05), run_time=0.9)

        items = [
            ("两直线平行", "同位角相等", GOLD),
            ("两直线平行", "内错角相等", BLUE),
            ("两直线平行", "同旁内角互补", ORANGE),
        ]
        y = 1.25
        for cond, res, col in items:
            left = txt(cond, size=28, color=GOLD)
            arrow = txt("⟹", size=30, color=DIM)
            right = label_box(res, size=27, color=col)
            row = VGroup(left, arrow, right).arrange(RIGHT, buff=0.4)
            row.move_to([0, y, 0])
            self.play(FadeIn(left, shift=RIGHT * 0.05), run_time=0.6)
            self.play(FadeIn(arrow, shift=RIGHT * 0.05), run_time=0.45)
            self.play(FadeIn(right, scale=0.97), run_time=0.7)
            y -= 1.15

        box = label_box("判定：角 ⟹ 平行　性质：平行 ⟹ 角", size=27, color=CHALK)
        box.move_to([0, -2.35, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.1)
        self.wait(3.2)
        self.finish_section()

    # ---------------- 6. 例题与三个易错点 ---------------- 27.8
    def scene_ex(self):
        self.section(6, "例题与三个易错点")

        q = VGroup(
            txt("已知 ∠1 = ∠2，∠1 与 ∠2 是同位角", size=26, color=CHALK),
        ).move_to([0, 2.3, 0])
        self.play(FadeIn(q, shift=UP * 0.05), run_time=0.9)

        s1 = VGroup(
            txt("因为", size=26, color=DIM),
            txt("∠1 = ∠2", size=28, color=GOLD),
        ).arrange(RIGHT, buff=0.2).move_to([0, 1.5, 0])
        self.play(FadeIn(s1, shift=UP * 0.05), run_time=0.8)

        s2 = VGroup(
            txt("所以", size=26, color=DIM),
            txt("a ∥ b", size=30, color=GREEN),
        ).arrange(RIGHT, buff=0.2).move_to([0, 0.72, 0])
        self.play(FadeIn(s2, shift=UP * 0.05), run_time=0.8)

        s3 = txt("（同位角相等，两直线平行）", size=25, color=DIM).move_to([0, 0.05, 0])
        self.play(FadeIn(s3, shift=UP * 0.05), run_time=0.8)

        items = [
            ("位置看错：把内错角当同位角", "画图先标出截线"),
            ("判定和性质用反", "由角推平行用判定"),
            ("同旁内角当成相等", "同旁内角是互补"),
        ]
        y = -1.05
        for bad_s, good_s in items:
            bad = txt(bad_s, size=24, color=RED).move_to([-2.8, y, 0])
            good = txt(good_s, size=23, color=GREEN).move_to([3.7, y, 0])
            cross = Line([bad.get_left()[0] - 0.07, y - 0.07, 0],
                         [bad.get_right()[0] + 0.07, y - 0.07, 0],
                         color=RED, stroke_width=2.2)
            self.play(FadeIn(bad, shift=RIGHT * 0.05), run_time=0.55)
            self.play(Create(cross), run_time=0.35)
            self.play(FadeIn(good, shift=RIGHT * 0.05), run_time=0.55)
            y -= 0.72

        self.wait(2.8)
        self.finish_section()

    def construct(self):
        self.scene_story()
        self.clear_stage()
        self.scene_angles()
        self.clear_stage()
        self.scene_perp()
        self.clear_stage()
        self.scene_three_lines()
        self.clear_stage()
        self.scene_judge()
        self.clear_stage()
        self.scene_property()
        self.clear_stage()
        self.scene_ex()
        self.clear_stage(0.8)