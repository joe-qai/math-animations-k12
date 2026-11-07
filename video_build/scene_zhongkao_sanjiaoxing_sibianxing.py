# -*- coding: utf-8 -*-
"""中考专题 4：三角形与四边形。全等、相似、特殊四边形、中位线、辅助线。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


def P(x, y):
    return np.array([float(x), float(y), 0.0])


def tri(a, b, c, color=CHALK, w=2.6, fill=None):
    p = Polygon(P(*a), P(*b), P(*c), color=color, stroke_width=w)
    if fill:
        p.set_fill(fill, opacity=0.12)
    return p


def label_at(s, pt, dx=0.0, dy=0.0, color=CHALK, size=19):
    return txt(s, size=size, color=color).move_to(P(pt[0] + dx, pt[1] + dy))


class ZhongkaoSanjiaoxingSibianxingScene(NarratedScene):
    lesson = "zhongkao-sanjiaoxing-sibianxing"

    def clear_stage(self, run_time: float = 0.5):
        keep = {id(self._track), id(self._fill)}
        junk = [m for m in self.mobjects if id(m) not in keep]
        if junk:
            self.play(*[FadeOut(m) for m in junk], run_time=run_time)
        self.cur_title = None
        self.cur_sub = None

    # ---------------- 0. 几何两条主线 ---------------- 27.6
    def scene_intro(self):
        self.section(0, "三角形与四边形：几何的两条主线")

        chips = [(-4.75, "全等", GOLD), (-1.6, "相似", GREEN),
                 (1.6, "特殊四边形", BLUE), (4.75, "辅助线", ORANGE)]
        for cx, name, col in chips:
            c = label_box(name, size=22, color=col).move_to([cx, 1.65, 0])
            self.play(FadeIn(c, shift=UP * 0.04), run_time=0.7)
        self.wait(0.5)

        rows = [
            ("全等是工具：证线段相等、角相等", CHALK),
            ("相似是压轴核心：把线段关系变成方程", CHALK),
            ("特殊四边形：判定与性质必须分清", CHALK),
            ("辅助线：从条件和结论的差距倒推", RED),
        ]
        y = 0.6
        for s, col in rows:
            t = txt(s, size=23, color=col).move_to([0, y, 0])
            self.play(FadeIn(t, shift=UP * 0.04), run_time=0.7)
            y -= 0.66
        self.wait(0.5)

        box = label_box("先找条件，再写判定", size=23, color=GOLD)
        box.move_to([0, -2.45, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.0)
        self.wait(11.0)
        self.finish_section()

    # ---------------- 1. 全等 ---------------- 28.1
    def scene_congruent(self):
        self.section(1, "全等：五种判定与书写")

        A, B, C = (-5.9, -1.5), (-2.9, -1.5), (-5.15, 0.75)
        D, E, F = (0.3, -1.5), (3.3, -1.5), (1.05, 0.75)
        self.play(Create(tri(A, B, C)), Create(tri(D, E, F, color=BLUE)), run_time=1.1)
        self.play(FadeIn(label_at("A", A, -0.28, -0.12)),
                  FadeIn(label_at("B", B, 0.28, -0.12)),
                  FadeIn(label_at("C", C, 0.0, 0.24)),
                  FadeIn(label_at("D", D, -0.28, -0.12, BLUE)),
                  FadeIn(label_at("E", E, 0.28, -0.12, BLUE)),
                  FadeIn(label_at("F", F, 0.0, 0.24, BLUE)), run_time=0.7)
        self.wait(0.4)

        eq = txt("△ABC ≌ △DEF", size=28, color=GOLD).move_to([2.1, 1.85, 0])
        self.play(FadeIn(eq, shift=UP * 0.04), run_time=0.8)
        note = txt("对应顶点写在对应位置", size=20, color=DIM).move_to([2.1, 1.3, 0])
        self.play(FadeIn(note), run_time=0.6)
        self.wait(0.4)

        crit = txt("SSS    SAS    ASA    AAS    HL", size=27, color=GREEN)
        crit.move_to([0, -2.05, 0])
        self.play(FadeIn(crit, shift=UP * 0.04), run_time=0.9)
        self.wait(0.4)

        bad = txt("边边角 SSA 不成立：两边和其中一边的对角", size=22, color=RED)
        bad.move_to([0, -2.75, 0])
        self.play(FadeIn(bad, shift=UP * 0.04), run_time=0.85)
        self.wait(11.0)
        self.finish_section()

    # ---------------- 2. 相似 ---------------- 26.5
    def scene_similar(self):
        self.section(2, "相似：判定与两个比")

        A = (-6.0, 1.2)
        B = (-1.6, -1.4)
        C = (-6.6, -1.4)
        self.play(Create(tri(A, B, C)), run_time=1.0)
        D = P((A[0] + C[0]) / 2, (A[1] + C[1]) / 2)
        E = P((A[0] + B[0]) / 2, (A[1] + B[1]) / 2)
        self.play(FadeIn(Dot(D, radius=0.06, color=GOLD)),
                  FadeIn(Dot(E, radius=0.06, color=GOLD)), run_time=0.6)
        self.play(Create(Line(D, E, color=GOLD, stroke_width=3.0)), run_time=0.8)
        self.play(FadeIn(label_at("A", A, -0.28, 0.1)),
                  FadeIn(label_at("B", B, 0.26, -0.14)),
                  FadeIn(label_at("C", C, -0.3, -0.16)),
                  FadeIn(label_at("D", D, -0.28, -0.16, GOLD)),
                  FadeIn(label_at("E", E, 0.24, 0.1, GOLD)), run_time=0.7)
        self.wait(0.4)

        rel = txt("DE ∥ BC  ⇒  △ADE ∽ △ABC", size=24, color=GREEN)
        rel.move_to([-4.0, -2.05, 0])
        self.play(FadeIn(rel, shift=UP * 0.04), run_time=0.85)
        self.wait(0.4)

        rows = [
            ("两角对应相等", GREEN),
            ("两边成比例且夹角相等", GREEN),
            ("三边成比例", GREEN),
            ("周长比 = 相似比", GOLD),
            ("面积比 = 相似比²", RED),
        ]
        y = 2.2
        for s, col in rows:
            t = txt(s, size=22, color=col).move_to([3.3, y, 0])
            self.play(FadeIn(t, shift=RIGHT * 0.04), run_time=0.7)
            y -= 0.72
        self.wait(0.5)

        box = label_box("面积比不是相似比", size=22, color=RED).move_to([3.3, -1.75, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.0)
        self.wait(8.5)
        self.finish_section()

    # ---------------- 3. 特殊四边形 ---------------- 25.9
    def scene_quads(self):
        self.section(3, "特殊四边形：一条判定链")

        # 平行四边形
        para = Polygon(P(-5.7, 0.0), P(-3.5, 0.0), P(-2.8, 1.35), P(-5.0, 1.35),
                       color=GOLD, stroke_width=2.6)
        rec = Rectangle(width=2.2, height=1.3, color=GREEN, stroke_width=2.6)
        rec.move_to(P(-1.9, 0.7))
        rho = Polygon(P(-5.4, -0.9), P(-3.3, -0.9), P(-4.1, -2.25), P(-6.2, -2.25),
                      color=BLUE, stroke_width=2.6)
        sq = Square(side_length=1.35, color=ORANGE, stroke_width=2.6)
        sq.move_to(P(-1.9, -1.55))

        self.play(Create(para), run_time=0.8)
        self.play(FadeIn(txt("平行四边形", size=21, color=GOLD).move_to([-4.3, 1.78, 0])),
                  run_time=0.5)
        self.play(Create(rec), FadeIn(txt("矩形", size=21, color=GREEN).move_to([-1.9, 1.72, 0])),
                  run_time=0.8)
        self.play(Create(rho), FadeIn(txt("菱形", size=21, color=BLUE).move_to([-4.3, -2.62, 0])),
                  run_time=0.8)
        self.play(Create(sq), FadeIn(txt("正方形", size=21, color=ORANGE).move_to([-1.9, -2.62, 0])),
                  run_time=0.8)
        self.wait(0.4)

        rows = [
            ("平行四边形：两组对边平行 / 一组平行且相等 / 对角线互相平分", GOLD),
            ("矩形：加一个直角，或对角线相等", GREEN),
            ("菱形：加一组邻边相等，或对角线垂直", BLUE),
            ("正方形：既是矩形又是菱形", ORANGE),
        ]
        y = 2.15
        for s, col in rows:
            t = txt(s, size=20, color=col).move_to([3.35, y, 0])
            if t.width > 6.3:
                t.scale_to_fit_width(6.3)
            self.play(FadeIn(t, shift=RIGHT * 0.04), run_time=0.8)
            y -= 1.0
        self.wait(0.5)

        box = label_box("判定与性质，别混着用", size=21, color=RED).move_to([3.35, -2.4, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.0)
        self.wait(7.0)
        self.finish_section()

    # ---------------- 4. 中位线 ---------------- 26.9
    def scene_midline(self):
        self.section(4, "中位线：隐形的送分点")

        A = (-6.0, 1.1)
        B = (-1.8, -1.35)
        C = (-6.5, -1.35)
        self.play(Create(tri(A, B, C)), run_time=1.0)
        D = P((A[0] + B[0]) / 2, (A[1] + B[1]) / 2)
        E = P((A[0] + C[0]) / 2, (A[1] + C[1]) / 2)
        self.play(Create(Line(D, E, color=GOLD, stroke_width=3.0)),
                  FadeIn(Dot(D, radius=0.06, color=GOLD)),
                  FadeIn(Dot(E, radius=0.06, color=GOLD)), run_time=0.9)
        self.play(FadeIn(label_at("A", A, -0.28, 0.1)),
                  FadeIn(label_at("B", B, 0.26, -0.14)),
                  FadeIn(label_at("C", C, -0.3, -0.16)),
                  FadeIn(label_at("D", D, 0.22, 0.08, GOLD)),
                  FadeIn(label_at("E", E, -0.28, -0.16, GOLD)), run_time=0.7)
        self.wait(0.4)

        f = txt("DE ∥ BC，DE = ½ BC", size=26, color=GREEN).move_to([-4.2, -2.05, 0])
        self.play(FadeIn(f, shift=UP * 0.04), run_time=0.85)
        self.wait(0.4)

        rows = [
            ("三角形中位线：平行第三边，等于它的一半", GOLD),
            ("梯形中位线：等于两底和的一半", GOLD),
            ("中点四边形：一定是平行四边形", BLUE),
            ("一个中点：倍长中线，构造全等", GREEN),
        ]
        y = 2.2
        for s, col in rows:
            t = txt(s, size=21, color=col).move_to([3.35, y, 0])
            if t.width > 6.3:
                t.scale_to_fit_width(6.3)
            self.play(FadeIn(t, shift=RIGHT * 0.04), run_time=0.8)
            y -= 0.95
        self.wait(0.5)

        box = label_box("两个中点先连中位线", size=21, color=RED).move_to([3.35, -2.1, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.0)
        self.wait(9.0)
        self.finish_section()

    # ---------------- 5. 辅助线 ---------------- 22.3
    def scene_aux(self):
        self.section(5, "辅助线：缺什么补什么")

        # 角平分线 + 两边垂线
        O = P(-4.9, -1.7)
        self.play(Create(Line(O, P(-1.9, -1.7), color=CHALK, stroke_width=2.4)),
                  Create(Line(O, P(-4.0, 0.75), color=CHALK, stroke_width=2.4)),
                  run_time=0.9)
        ang = 70.0
        self.play(Create(Arc(radius=1.5, start_angle=0, angle=ang * DEGREES,
                             arc_center=O, color=DIM, stroke_width=2.0)), run_time=0.7)
        bis = Line(O, P(O[0] + 2.9 * np.cos(ang / 2 * DEGREES),
                        O[1] + 2.9 * np.sin(ang / 2 * DEGREES)), color=GOLD, stroke_width=3.0)
        self.play(Create(bis), run_time=0.8)
        Pt = P(O[0] + 2.1 * np.cos(ang / 2 * DEGREES), O[1] + 2.1 * np.sin(ang / 2 * DEGREES))
        self.play(FadeIn(Dot(Pt, radius=0.07, color=GOLD)), run_time=0.5)
        foot1 = P(Pt[0], -1.7)
        self.play(Create(Line(Pt, foot1, color=GREEN, stroke_width=2.0)), run_time=0.7)
        self.wait(0.4)

        note = txt("角平分线上的点到两边距离相等", size=21, color=GREEN)
        note.move_to([-3.4, -2.45, 0])
        self.play(FadeIn(note, shift=UP * 0.04), run_time=0.85)
        self.wait(0.4)

        rows = [
            ("见中点：中位线 / 倍长中线", GOLD),
            ("见角平分线：向两边作垂线", GOLD),
            ("见等腰：作底边上的高", BLUE),
            ("见线段和差：截长补短", GREEN),
        ]
        y = 2.15
        for s, col in rows:
            t = txt(s, size=22, color=col).move_to([3.3, y, 0])
            self.play(FadeIn(t, shift=RIGHT * 0.04), run_time=0.75)
            y -= 0.85
        self.wait(0.5)

        box = label_box("辅助线从差距倒推", size=21, color=RED).move_to([3.3, -1.9, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.0)
        self.wait(6.0)
        self.finish_section()

    # ---------------- 6. 易错点 ---------------- 18.9
    def scene_traps(self):
        self.section(6, "四个易错点")

        rows = [
            ("① 用边边角判全等", "SSA 不成立"),
            ("② 对应顶点写错", "△ABC ≌ △DEF 要对齐"),
            ("③ 面积比当相似比", "面积比是相似比的平方"),
            ("④ 判定与性质混用", "拿结论当条件"),
        ]
        y = 1.85
        for a, b in rows:
            ta = txt(a, size=23, color=RED).move_to([-2.7, y, 0])
            tb = txt(b, size=20, color=DIM).move_to([3.5, y, 0])
            self.play(FadeIn(ta, shift=RIGHT * 0.04), run_time=0.6)
            self.play(FadeIn(tb, shift=RIGHT * 0.04), run_time=0.6)
            y -= 0.86
        self.wait(0.8)

        box = label_box("先找条件，再写判定", size=27, color=GOLD)
        box.move_to([0, -2.45, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.1)
        self.wait(6.0)
        self.finish_section()

    def construct(self):
        self.scene_intro()
        self.clear_stage()
        self.scene_congruent()
        self.clear_stage()
        self.scene_similar()
        self.clear_stage()
        self.scene_quads()
        self.clear_stage()
        self.scene_midline()
        self.clear_stage()
        self.scene_aux()
        self.clear_stage()
        self.scene_traps()
        self.clear_stage(0.8)