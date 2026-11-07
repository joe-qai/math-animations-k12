# -*- coding: utf-8 -*-
"""线与角：线段/射线/直线、角的分类、平行与垂直。四年级上册。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


def angle_figure(vertex, deg: float, length: float = 1.2, color: str = CHALK,
                 mark: bool = True, mark_color: str = GOLD) -> VGroup:
    """顶点在下、开口朝上的角。deg 为角的度数。"""
    vx, vy = vertex[0], vertex[1]
    half = deg / 2.0
    a1, a2 = 90 - half, 90 + half

    def endp(a):
        return [vx + length * np.cos(a * DEGREES),
                vy + length * np.sin(a * DEGREES), 0]

    ray1 = Line([vx, vy, 0], endp(a1), color=color, stroke_width=3)
    ray2 = Line([vx, vy, 0], endp(a2), color=color, stroke_width=3)
    g = VGroup(ray1, ray2)

    if mark and deg < 180:
        r = 0.42 if deg >= 90 else 0.5
        arc = Arc(radius=r, start_angle=a1 * DEGREES, angle=deg * DEGREES,
                  color=mark_color, stroke_width=2.4)
        arc.move_arc_center_to([vx, vy, 0])
        g.add(arc)
    if mark and deg == 90:
        s = 0.3
        g.add(Polygon([vx, vy, 0], [vx + s, vy, 0],
                      [vx + s, vy + s, 0], [vx, vy + s, 0],
                      color=mark_color, stroke_width=1.8))
    return g


class XianYuJiaoScene(NarratedScene):
    lesson = "xian-yujiao"

    def clear_stage(self, run_time: float = 0.5):
        keep = {id(self._track), id(self._fill)}
        junk = [m for m in self.mobjects if id(m) not in keep]
        if junk:
            self.play(*[FadeOut(m) for m in junk], run_time=run_time)
        self.cur_title = None
        self.cur_sub = None

    # ---------------- 0. 生活里的线和角 ---------------- 12.4
    def scene_story(self):
        self.section(0, "生活里的线和角")

        # 左：斑马线
        road = Rectangle(width=3.3, height=1.9, color=DIM, stroke_width=1.8,
                         fill_color=DIM, fill_opacity=0.12)
        road.move_to([-4.4, 0.85, 0])
        self.play(Create(road), run_time=0.8)
        stripes = VGroup()
        for i in range(6):
            r = Rectangle(width=0.26, height=1.55, color=CHALK, stroke_width=1.2,
                          fill_color=CHALK, fill_opacity=0.55)
            r.move_to([-5.35 + i * 0.42, 0.85, 0])
            stripes.add(r)
        self.play(LaggedStart(*[FadeIn(s) for s in stripes], lag_ratio=0.12), run_time=1.2)
        l1 = txt("斑马线：一条条平行", size=24, color=GOLD).move_to([-4.4, -0.6, 0])
        self.play(FadeIn(l1, shift=UP * 0.06), run_time=0.7)

        # 中：铁轨
        rail = VGroup(
            Line([-1.55, 0.55, 0], [1.55, 0.55, 0], color=CHALK, stroke_width=4),
            Line([-1.55, 1.15, 0], [1.55, 1.15, 0], color=CHALK, stroke_width=4),
        )
        ties = VGroup()
        for i in range(7):
            x = -1.4 + i * 0.47
            ties.add(Line([x, 0.42, 0], [x, 1.3, 0], color=DIM, stroke_width=2.2))
        self.play(Create(rail), run_time=0.9)
        self.play(LaggedStart(*[FadeIn(t) for t in ties], lag_ratio=0.1), run_time=0.9)
        l2 = txt("铁轨：一直不相交", size=24, color=GOLD).move_to([0, -0.6, 0])
        self.play(FadeIn(l2, shift=UP * 0.06), run_time=0.7)

        # 右：阳光
        src = Dot([4.5, 0.15, 0], radius=0.13, color=GOLD)
        rays = VGroup()
        for a in (58, 74, 90, 106, 122):
            ex = 4.5 + 1.35 * np.cos(a * DEGREES)
            ey = 0.15 + 1.35 * np.sin(a * DEGREES)
            rays.add(Arrow([4.5, 0.15, 0], [ex, ey, 0], color=GOLD, stroke_width=2.4,
                           buff=0, max_tip_length_to_length_ratio=0.16))
        self.play(FadeIn(src), run_time=0.6)
        self.play(LaggedStart(*[GrowArrow(r) for r in rays], lag_ratio=0.1), run_time=1.2)
        l3 = txt("阳光：从一个点射出来", size=24, color=GOLD).move_to([4.5, -0.6, 0])
        self.play(FadeIn(l3, shift=UP * 0.06), run_time=0.7)

        note = txt("有线，就有角；有线，就有平行和垂直", size=28, color=GREEN)
        note.move_to([0, -2.15, 0])
        self.play(FadeIn(note, shift=UP * 0.08), run_time=0.8)
        self.finish_section()

    # ---------------- 1. 线段、射线、直线 ---------------- 16.2
    def scene_lines(self):
        self.section(1, "线段、射线、直线")

        rows = [
            ("线段", 1.8, 1.6, "两个端点 · 能量出长度", GOLD, False, False),
            ("射线", 0.15, 2.35, "一个端点 · 只向一端无限延长", BLUE, True, False),
            ("直线", -1.5, 2.45, "没有端点 · 两端都无限延长", GREEN, True, True),
        ]
        for name, y, half, note, color, arr_r, arr_l in rows:
            lab = txt(name, size=32, color=color).move_to([-5.35, y, 0])
            self.play(FadeIn(lab, shift=RIGHT * 0.06), run_time=0.5)

            if arr_r and arr_l:
                ln = DoubleArrow([-half, y, 0], [half, y, 0], color=color,
                                 stroke_width=3, buff=0,
                                 max_tip_length_to_length_ratio=0.1)
            elif arr_r:
                ln = Arrow([-half, y, 0], [half, y, 0], color=color, stroke_width=3,
                           buff=0, max_tip_length_to_length_ratio=0.1)
            else:
                ln = Line([-half, y, 0], [half, y, 0], color=color, stroke_width=3)
            self.play(Create(ln), run_time=0.9)

            if name == "线段":
                d1 = Dot([-half, y, 0], radius=0.09, color=color)
                d2 = Dot([half, y, 0], radius=0.09, color=color)
                self.play(FadeIn(d1), FadeIn(d2), run_time=0.5)
            elif name == "射线":
                d1 = Dot([-half, y, 0], radius=0.09, color=color)
                self.play(FadeIn(d1), run_time=0.4)

            n = txt(note, size=24, color=DIM).move_to([0.55, y - 0.5, 0])
            self.play(FadeIn(n, shift=UP * 0.05), run_time=0.6)
            self.wait(0.9)

        tip = txt("线段可以量长短，射线和直线量不出来", size=27, color=GREEN)
        tip.move_to([0, -2.55, 0])
        self.play(FadeIn(tip, shift=UP * 0.08), run_time=0.8)
        self.finish_section()

    # ---------------- 2. 什么是角 ---------------- 14.4
    def scene_angle(self):
        self.section(2, "从一点引出两条射线，就是角")

        v = [-3.1, -1.25, 0]
        r1 = Line(v, [-3.1 + 3.5 * np.cos(30 * DEGREES),
                      -1.25 + 3.5 * np.sin(30 * DEGREES), 0], color=GOLD, stroke_width=3)
        r2 = Line(v, [-3.1 + 3.3 * np.cos(115 * DEGREES),
                      -1.25 + 3.3 * np.sin(115 * DEGREES), 0], color=GOLD, stroke_width=3)
        self.play(Create(r1), Create(r2), run_time=1.3)

        arc = Arc(radius=1.0, start_angle=30 * DEGREES, angle=85 * DEGREES,
                  color=BLUE, stroke_width=2.6).move_arc_center_to(v)
        self.play(Create(arc), run_time=0.8)

        d = Dot(v, radius=0.11, color=RED)
        v_lab = txt("顶点", size=26, color=RED).move_to([-3.5, -1.8, 0])
        self.play(FadeIn(d), FadeIn(v_lab), run_time=0.7)

        s1 = txt("边", size=26, color=GOLD).move_to([-1.35, -0.78, 0])
        s2 = txt("边", size=26, color=GOLD).move_to([-4.55, 0.35, 0])
        self.play(FadeIn(s1), FadeIn(s2), run_time=0.6)

        # 右侧：边长短不影响角的大小
        g1 = angle_figure([2.95, 0.62], 60, length=0.75, color=BLUE, mark_color=BLUE)
        g2 = angle_figure([4.35, 0.05], 60, length=1.75, color=GREEN, mark_color=GREEN)
        self.play(Create(g1), run_time=0.7)
        self.play(Create(g2), run_time=0.9)

        n1 = txt("边画得短", size=23, color=BLUE).move_to([2.35, -0.5, 0])
        n2 = txt("边画得长", size=23, color=GREEN).move_to([5.35, -0.6, 0])
        self.play(FadeIn(n1), FadeIn(n2), run_time=0.6)

        eq = txt("角一样大", size=27, color=GOLD).move_to([3.6, 2.0, 0])
        note = txt("角的大小只看两条边张开的程度", size=27, color=GREEN)
        note.move_to([0, -2.4, 0])
        self.play(FadeIn(eq, shift=UP * 0.06), run_time=0.7)
        self.play(FadeIn(note, shift=UP * 0.08), run_time=0.8)
        self.finish_section()

    # ---------------- 3. 角的分类 ---------------- 13.8
    def scene_kinds(self):
        self.section(3, "锐角、直角、钝角、平角、周角")

        specs = [
            (-5.45, "锐角", "小于 90°", 45, GOLD),
            (-2.75, "直角", "等于 90°", 90, GREEN),
            (0.05, "钝角", "大于 90°", 130, ORANGE),
            (2.85, "平角", "等于 180°", 180, BLUE),
        ]
        vy = 0.95
        for x, name, deg, ang, color in specs:
            fig = angle_figure([x, vy], ang, length=1.15, color=CHALK, mark_color=color)
            self.play(Create(fig), run_time=0.7)
            nm = txt(name, size=28, color=color).move_to([x, 0.05, 0])
            dg = txt(deg, size=22, color=DIM).move_to([x, -0.42, 0])
            self.play(FadeIn(nm, shift=UP * 0.05), run_time=0.4)
            self.play(FadeIn(dg), run_time=0.3)

        # 周角：一整圈
        cx = 5.35
        circ = Circle(radius=0.72, color=PURPLE, stroke_width=2.6).move_to([cx, 1.15, 0])
        rad = Line([cx, 1.15, 0], [cx + 0.72, 1.15, 0], color=CHALK, stroke_width=3)
        self.play(Create(circ), Create(rad), run_time=0.9)
        nm = txt("周角", size=28, color=PURPLE).move_to([cx, 0.05, 0])
        dg = txt("等于 360°", size=22, color=DIM).move_to([cx, -0.42, 0])
        self.play(FadeIn(nm, shift=UP * 0.05), FadeIn(dg), run_time=0.6)

        n1 = txt("量角器：中心对顶点，零刻度线对一条边", size=26, color=GOLD)
        n1.move_to([0, -1.45, 0])
        n2 = txt("看另一条边落在哪一格，就是多少度", size=26, color=CHALK)
        n2.move_to([0, -2.15, 0])
        self.play(FadeIn(n1, shift=UP * 0.08), run_time=0.8)
        self.play(FadeIn(n2, shift=UP * 0.08), run_time=0.7)
        self.finish_section()

    # ---------------- 4. 平行 ---------------- 15.8
    def scene_parallel(self):
        self.section(4, "平行：同一平面内，永不相交")

        a = Line([-5.6, 1.55, 0], [3.6, 1.55, 0], color=GOLD, stroke_width=4)
        b = Line([-5.6, -0.25, 0], [3.6, -0.25, 0], color=BLUE, stroke_width=4)
        self.play(Create(a), run_time=0.9)
        self.play(Create(b), run_time=0.9)

        # 两端延长，示意"无论多长都不碰面"
        ext = VGroup(
            DashedLine([3.6, 1.55, 0], [5.9, 1.55, 0], color=GOLD, stroke_width=2.4),
            DashedLine([3.6, -0.25, 0], [5.9, -0.25, 0], color=BLUE, stroke_width=2.4),
            DashedLine([-5.6, 1.55, 0], [-6.6, 1.55, 0], color=GOLD, stroke_width=2.4),
            DashedLine([-5.6, -0.25, 0], [-6.6, -0.25, 0], color=BLUE, stroke_width=2.4),
        )
        self.play(LaggedStart(*[Create(e) for e in ext], lag_ratio=0.1), run_time=1.1)

        # 距离处处相等
        arrs = VGroup()
        for x in (-4.6, -1.8, 1.0):
            arrs.add(DoubleArrow([x, -0.25, 0], [x, 1.55, 0], color=GREEN,
                                 stroke_width=2.2, buff=0,
                                 max_tip_length_to_length_ratio=0.12))
        self.play(LaggedStart(*[GrowArrow(x) for x in arrs], lag_ratio=0.25), run_time=1.5)

        d_lab = txt("距离处处相等", size=25, color=GREEN).move_to([-1.8, 0.28, 0])
        self.play(FadeIn(d_lab, shift=UP * 0.05), run_time=0.6)

        n1 = txt("同一平面内，不相交的两条直线互相平行", size=27, color=GOLD)
        n1.move_to([-0.8, -1.45, 0])
        n2 = txt("铁轨、斑马线、双杠，都是平行线", size=26, color=CHALK)
        n2.move_to([-0.8, -2.1, 0])
        self.play(FadeIn(n1, shift=UP * 0.08), run_time=0.8)
        self.play(FadeIn(n2, shift=UP * 0.08), run_time=0.7)
        self.finish_section()

    # ---------------- 5. 垂直 ---------------- 16.0
    def scene_perp(self):
        self.section(5, "垂直：相交成直角")

        h = Line([-6.6, -0.95, 0], [4.6, -0.95, 0], color=CHALK, stroke_width=3.6)
        v = Line([0.55, -2.2, 0], [0.55, 1.75, 0], color=BLUE, stroke_width=3.6)
        self.play(Create(h), run_time=0.9)
        self.play(Create(v), run_time=0.9)

        s = 0.32
        sq = Polygon([0.55, -0.95, 0], [0.55 + s, -0.95, 0],
                     [0.55 + s, -0.95 + s, 0], [0.55, -0.95 + s, 0],
                     color=GREEN, stroke_width=2.2)
        self.play(Create(sq), run_time=0.7)

        foot = Dot([0.55, -0.95, 0], radius=0.09, color=GREEN)
        f_lab = txt("垂足", size=25, color=GREEN).move_to([1.85, -0.55, 0])
        self.play(FadeIn(foot), FadeIn(f_lab), run_time=0.7)

        t1 = txt("相交成直角，就说两条直线互相垂直", size=27, color=GOLD)
        t1.move_to([0.0, 2.62, 0])
        self.play(FadeIn(t1, shift=UP * 0.06), run_time=0.8)

        # 点到直线的距离：垂线段最短
        p = [-5.0, 1.45, 0]
        pd = Dot(p, radius=0.1, color=RED)
        p_lab = txt("P", size=26, color=RED).move_to([-4.68, 1.85, 0])
        self.play(FadeIn(pd), FadeIn(p_lab), run_time=0.6)

        va = Line(p, [-5.0, -0.95, 0], color=RED, stroke_width=3)
        self.play(Create(va), run_time=0.8)
        mark = Polygon([-5.0, -0.95, 0], [-5.0 + 0.26, -0.95, 0],
                       [-5.0 + 0.26, -0.95 + 0.26, 0], [-5.0, -0.95 + 0.26, 0],
                       color=RED, stroke_width=1.8)
        self.play(Create(mark), run_time=0.5)

        s1 = Line(p, [-2.1, -0.95, 0], color=DIM, stroke_width=2.4)
        s2 = Line(p, [-6.6, -0.95, 0], color=DIM, stroke_width=2.4)
        self.play(Create(s1), Create(s2), run_time=1.0)

        n1 = txt("垂线段最短", size=30, color=RED).move_to([-3.35, -1.7, 0])
        n2 = txt("它的长度就是点到直线的距离", size=25, color=DIM).move_to([-1.1, -2.38, 0])
        self.play(FadeIn(n1, shift=UP * 0.08), run_time=0.7)
        self.play(FadeIn(n2, shift=UP * 0.06), run_time=0.7)
        self.finish_section()

    # ---------------- 6. 总结 ---------------- 16.5
    def scene_summary(self):
        self.section(6, "四个词，记住线与角")

        rows = VGroup(
            label_box("① 线段 · 射线 · 直线", size=27, color=GOLD),
            label_box("② 锐角 · 直角 · 钝角 · 平角 · 周角", size=27, color=CHALK),
            label_box("③ 平行不相交 · 垂直成直角", size=27, color=GREEN),
        ).arrange(DOWN, buff=0.26).move_to([0, 1.75, 0])
        for r in rows:
            self.play(FadeIn(r, shift=RIGHT * 0.08), run_time=0.6)
            self.wait(0.6)

        # 三角尺画平行线：一靠、二移、三画
        given = Line([-5.3, -1.95, 0], [-1.7, -1.95, 0], color=CHALK, stroke_width=3.2)
        tri = Polygon([-4.95, -1.95, 0], [-3.55, -1.95, 0], [-4.95, -0.75, 0],
                      color=GOLD, stroke_width=2.2,
                      fill_color=GOLD, fill_opacity=0.14)
        self.play(Create(given), run_time=0.8)
        self.play(FadeIn(tri, scale=0.92), run_time=0.9)

        l1 = txt("一靠：靠紧已知直线", size=24, color=GOLD).move_to([3.95, -0.85, 0])
        self.play(FadeIn(l1, shift=RIGHT * 0.06), run_time=0.6)
        self.wait(0.7)

        self.play(tri.animate.shift(UP * 0.95 + RIGHT * 0.35), run_time=1.1)
        l2 = txt("二移：平移到要画的位置", size=24, color=GOLD).move_to([3.95, -1.55, 0])
        self.play(FadeIn(l2, shift=RIGHT * 0.06), run_time=0.6)
        self.wait(0.7)

        new_line = DashedLine([-5.3, -1.0, 0], [-1.7, -1.0, 0],
                              color=BLUE, stroke_width=2.6)
        self.play(Create(new_line), run_time=1.1)
        l3 = txt("三画：沿尺边画出来", size=24, color=BLUE).move_to([3.95, -2.25, 0])
        self.play(FadeIn(l3, shift=RIGHT * 0.06), run_time=0.6)
        self.wait(1.6)
        self.finish_section()

    def construct(self):
        self.scene_story()
        self.clear_stage()
        self.scene_lines()
        self.clear_stage()
        self.scene_angle()
        self.clear_stage()
        self.scene_kinds()
        self.clear_stage()
        self.scene_parallel()
        self.clear_stage()
        self.scene_perp()
        self.clear_stage()
        self.scene_summary()
        self.clear_stage(0.8)