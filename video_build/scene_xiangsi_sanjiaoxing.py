# -*- coding: utf-8 -*-
"""相似三角形：形状相同，大小可以不同。八年级下。"""

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


def P(x, y):
    return np.array([float(x), float(y), 0.0])


def tri(A, B, C, color=CHALK, width=3.0, fill=0.06) -> Polygon:
    return Polygon(P(*A), P(*B), P(*C), color=color, stroke_width=width,
                   fill_color=color, fill_opacity=fill)


def vlabel(ch, pos, color=CHALK, size=25) -> Text:
    return txt(ch, size=size, color=color).move_to(P(*pos))


def ang_arc(O, dA, dB, color=GOLD, radius=0.5, width=2.4) -> Arc:
    """以 O 为顶点、沿 dA 与 dB 两个方向画角弧（取两者之间的较小角）。"""
    o = P(*O)
    ua = P(*dA)
    ua = ua / np.linalg.norm(ua)
    ub = P(*dB)
    ub = ub / np.linalg.norm(ub)
    a1 = math.atan2(ua[1], ua[0])
    a2 = math.atan2(ub[1], ub[0])
    delta = a2 - a1
    while delta > math.pi:
        delta -= 2 * math.pi
    while delta < -math.pi:
        delta += 2 * math.pi
    return Arc(radius=radius, start_angle=a1, angle=delta, arc_center=o,
               color=color, stroke_width=width)


class XiangsiSanjiaoxingScene(NarratedScene):
    lesson = "xiangsi-sanjiaoxing"

    def clear_stage(self, run_time: float = 0.5):
        keep = {id(self._track), id(self._fill)}
        junk = [m for m in self.mobjects if id(m) not in keep]
        if junk:
            self.play(*[FadeOut(m) for m in junk], run_time=run_time)
        self.cur_title = None
        self.cur_sub = None

    # ---------------- 0. 形状相同 ---------------- 23.9
    def scene_intro(self):
        self.section(0, "形状相同，大小可以不同")

        chips = [
            ("照片放大", "人还是那个人", -4.1, GOLD),
            ("竹竿的影子", "和小树的影子一个样", 0.0, GREEN),
            ("地图上的三角形", "按比例缩小", 4.1, BLUE),
        ]
        for name, note, cx, col in chips:
            t = label_box(name, size=24, color=col).move_to([cx, 2.3, 0])
            self.play(FadeIn(t, scale=0.97), run_time=0.75)
            n = txt(note, size=21, color=DIM).move_to([cx, 1.6, 0])
            self.play(FadeIn(n, shift=UP * 0.04), run_time=0.7)
        self.wait(1.2)

        n1 = txt("形状相同，大小不一定相同", size=28, color=CHALK).move_to([0, 0.55, 0])
        self.play(FadeIn(n1, shift=UP * 0.05), run_time=0.95)
        n2 = txt("这样的图形，叫相似图形", size=27, color=GOLD).move_to([0, -0.45, 0])
        self.play(FadeIn(n2, shift=UP * 0.04), run_time=0.95)
        self.wait(1.2)

        box = label_box("大小能变，形状不能变", size=27, color=CHALK)
        box.move_to([0, -2.3, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.1)
        self.wait(7.0)
        self.finish_section()

    # ---------------- 1. 定义与相似比 ---------------- 23.7
    def scene_def(self):
        self.section(1, "对应角相等，对应边成比例")

        A, B, C = (-6.1, -1.5), (-2.3, -1.5), (-3.5, 1.0)
        D, E, F = (-0.2, -1.5), (1.7, -1.5), (1.1, -0.25)
        t1 = tri(A, B, C, CHALK)
        t2 = tri(D, E, F, GOLD)
        self.play(Create(t1), run_time=1.0)
        self.play(Create(t2), run_time=1.0)

        names = [vlabel("A", (A[0] - 0.32, A[1] - 0.3)), vlabel("B", (B[0] + 0.32, B[1] - 0.3)),
                 vlabel("C", (C[0] - 0.05, C[1] + 0.35)),
                 vlabel("D", (D[0] - 0.32, D[1] - 0.3)), vlabel("E", (E[0] + 0.32, E[1] - 0.3)),
                 vlabel("F", (F[0] - 0.02, F[1] + 0.33))]
        self.play(LaggedStart(*[FadeIn(n, scale=0.9) for n in names], lag_ratio=0.1),
                  run_time=1.5)
        self.wait(0.8)

        arcs = [
            ang_arc(A, (B[0] - A[0], B[1] - A[1]), (C[0] - A[0], C[1] - A[1]), RED, 0.55),
            ang_arc(D, (E[0] - D[0], E[1] - D[1]), (F[0] - D[0], F[1] - D[1]), RED, 0.55),
            ang_arc(B, (A[0] - B[0], A[1] - B[1]), (C[0] - B[0], C[1] - B[1]), GOLD, 0.6),
            ang_arc(E, (D[0] - E[0], D[1] - E[1]), (F[0] - E[0], F[1] - E[1]), GOLD, 0.6),
            ang_arc(C, (A[0] - C[0], A[1] - C[1]), (B[0] - C[0], B[1] - C[1]), GREEN, 0.5),
            ang_arc(F, (D[0] - F[0], D[1] - F[1]), (E[0] - F[0], E[1] - F[1]), GREEN, 0.5),
        ]
        self.play(LaggedStart(*[Create(a) for a in arcs], lag_ratio=0.12), run_time=2.2)
        self.wait(1.0)

        rows = [
            ("对应角相等", RED),
            ("对应边成比例", GOLD),
            ("△ABC ∽ △DEF", CHALK),
            ("k = AB : DE", GREEN),
        ]
        y = 2.0
        for s, col in rows:
            t = txt(s, size=24, color=col).move_to([4.4, y, 0])
            self.play(FadeIn(t, shift=RIGHT * 0.04), run_time=0.8)
            y -= 0.85
        self.wait(1.0)

        note = txt("字母必须一一对应，A 对 D、B 对 E、C 对 F", size=22, color=RED)
        note.move_to([0, -2.5, 0])
        self.play(FadeIn(note, shift=UP * 0.04), run_time=1.0)
        self.wait(3.0)
        self.finish_section()

    # ---------------- 2. AA 判定 ---------------- 24.5
    def scene_aa(self):
        self.section(2, "判定一：两角分别相等")

        A, B, C = (-5.9, -1.4), (-1.9, -1.4), (-3.0, 0.9)
        D, E, F = (0.1, -1.4), (2.1, -1.4), (1.6, -0.35)
        t1 = tri(A, B, C, CHALK)
        t2 = tri(D, E, F, GOLD)
        self.play(Create(t1), run_time=0.9)
        self.play(Create(t2), run_time=0.9)

        names = [vlabel("A", (A[0] - 0.32, A[1] - 0.3)), vlabel("B", (B[0] + 0.32, B[1] - 0.3)),
                 vlabel("C", (C[0] - 0.05, C[1] + 0.33)),
                 vlabel("D", (D[0] - 0.32, D[1] - 0.3)), vlabel("E", (E[0] + 0.32, E[1] - 0.3)),
                 vlabel("F", (F[0] + 0.28, F[1] + 0.22))]
        self.play(LaggedStart(*[FadeIn(n, scale=0.9) for n in names], lag_ratio=0.1),
                  run_time=1.4)
        self.wait(0.6)

        arcs = [
            ang_arc(A, (B[0] - A[0], B[1] - A[1]), (C[0] - A[0], C[1] - A[1]), RED, 0.55),
            ang_arc(D, (E[0] - D[0], E[1] - D[1]), (F[0] - D[0], F[1] - D[1]), RED, 0.55),
            ang_arc(B, (A[0] - B[0], A[1] - B[1]), (C[0] - B[0], C[1] - B[1]), GOLD, 0.6),
            ang_arc(E, (D[0] - E[0], D[1] - E[1]), (F[0] - E[0], F[1] - E[1]), GOLD, 0.6),
        ]
        self.play(LaggedStart(*[Create(a) for a in arcs], lag_ratio=0.12), run_time=2.0)
        self.wait(0.9)

        head = txt("两组角分别相等 → 两个三角形相似", size=26, color=GOLD)
        head.move_to([0, 2.45, 0])
        self.play(FadeIn(head, shift=UP * 0.05), run_time=0.95)
        self.wait(0.8)

        r1 = txt("∠A = ∠D，∠B = ∠E", size=23, color=CHALK).move_to([4.5, 0.95, 0])
        self.play(FadeIn(r1, shift=UP * 0.04), run_time=0.85)
        r2 = txt("∠C、∠F 由内角和自然相等", size=21, color=GREEN).move_to([4.5, 0.15, 0])
        self.play(FadeIn(r2, shift=UP * 0.04), run_time=0.9)
        r3 = txt("所以 △ABC ∽ △DEF", size=24, color=GOLD).move_to([4.5, -0.7, 0])
        self.play(FadeIn(r3, shift=UP * 0.04), run_time=0.9)
        self.wait(1.0)

        note = txt("找角：公共角、对顶角、平行线的同位角与内错角", size=22, color=DIM)
        note.move_to([0, -2.45, 0])
        self.play(FadeIn(note, shift=UP * 0.04), run_time=0.95)
        self.wait(6.0)
        self.finish_section()

    # ---------------- 3. SAS 与 SSS ---------------- 20.8
    def scene_sss(self):
        self.section(3, "判定二、判定三")

        b1 = label_box("两边成比例，且夹角相等", size=27, color=GOLD)
        b1.move_to([0, 1.95, 0])
        self.play(FadeIn(b1, scale=0.97), run_time=1.0)
        self.wait(0.7)

        b2 = label_box("三边成比例", size=27, color=GREEN)
        b2.move_to([0, 0.7, 0])
        self.play(FadeIn(b2, scale=0.97), run_time=1.0)
        self.wait(0.9)

        w = txt("第二条一定是夹角，不能是随便一个角", size=25, color=RED)
        w.move_to([0, -0.6, 0])
        self.play(FadeIn(w, shift=UP * 0.04), run_time=0.95)
        self.wait(0.9)

        tips = txt("三条判定里，A A 用得最多：找角比算边长容易", size=24, color=DIM)
        tips.move_to([0, -1.7, 0])
        self.play(FadeIn(tips, shift=UP * 0.04), run_time=0.95)
        self.wait(1.0)

        # 判定二的形式：两边成比例 + 夹角相等
        f = txt("AB : DE = AC : DF，且 ∠A = ∠D", size=23, color=CHALK)
        f.move_to([0, -2.5, 0])
        self.play(FadeIn(f, shift=UP * 0.04), run_time=1.0)
        self.wait(2.8)
        self.finish_section()

    # ---------------- 4. 相似三角形的性质 ---------------- 21.1
    def scene_props(self):
        self.section(4, "相似三角形有哪些性质")

        rows = [
            ("对应角相等，对应边成比例", CHALK),
            ("对应高、中线、角平分线之比 = 相似比", CHALK),
            ("周长比 = 相似比", CHALK),
            ("面积比 = 相似比的平方", RED),
        ]
        y = 2.0
        for s, col in rows:
            t = txt(s, size=25, color=col).move_to([0, y, 0])
            self.play(FadeIn(t, shift=UP * 0.04), run_time=0.85)
            y -= 0.9
        self.wait(1.2)

        ex = label_box("相似比 1 : 2　→　面积比 1 : 4", size=26, color=GOLD)
        ex.move_to([0, -1.5, 0])
        self.play(FadeIn(ex, scale=0.97), run_time=1.05)
        self.wait(0.8)

        note = txt("面积比最容易漏掉平方", size=24, color=RED)
        note.move_to([0, -2.5, 0])
        self.play(FadeIn(note, shift=UP * 0.04), run_time=0.9)
        self.wait(4.6)
        self.finish_section()

    # ---------------- 5. 例题：DE ∥ BC ---------------- 32.5
    def scene_example(self):
        self.section(5, "例题：DE ∥ BC，求 BC")

        A = (-4.6, 1.75)
        B = (-6.3, -1.75)
        C = (-1.5, -1.75)
        D = (-5.28, 0.35)
        E = (-3.34, 0.35)
        big = tri(A, B, C, CHALK)
        self.play(Create(big), run_time=1.1)

        seg = Line(P(*D), P(*E), color=GOLD, stroke_width=4)
        self.play(Create(seg), run_time=1.0)

        names = [vlabel("A", (A[0] - 0.12, A[1] + 0.36)),
                 vlabel("B", (B[0] - 0.38, B[1] - 0.3)),
                 vlabel("C", (C[0] + 0.38, C[1] - 0.3)),
                 vlabel("D", (D[0] - 0.42, D[1] + 0.1)),
                 vlabel("E", (E[0] + 0.42, E[1] + 0.1))]
        self.play(LaggedStart(*[FadeIn(n, scale=0.9) for n in names], lag_ratio=0.12),
                  run_time=1.4)
        self.wait(0.7)

        ad = txt("2", size=22, color=GOLD).move_to([(A[0] + D[0]) / 2 - 0.4, (A[1] + D[1]) / 2, 0])
        db = txt("3", size=22, color=GOLD).move_to([(D[0] + B[0]) / 2 - 0.4, (D[1] + B[1]) / 2, 0])
        de = txt("4", size=22, color=GOLD).move_to([(D[0] + E[0]) / 2, D[1] + 0.32, 0])
        self.play(FadeIn(ad), FadeIn(db), FadeIn(de), run_time=0.9)
        self.wait(1.0)

        s1 = txt("DE ∥ BC → △ADE ∽ △ABC", size=24, color=CHALK).move_to([3.5, 2.05, 0])
        self.play(FadeIn(s1, shift=UP * 0.04), run_time=0.9)
        s2 = txt("相似比 = AD : AB = 2 : 5", size=24, color=GOLD).move_to([3.5, 1.2, 0])
        self.play(FadeIn(s2, shift=UP * 0.04), run_time=0.9)
        s3 = txt("DE : BC = 2 : 5", size=24, color=CHALK).move_to([3.5, 0.35, 0])
        self.play(FadeIn(s3, shift=UP * 0.04), run_time=0.9)
        self.wait(0.7)

        s4 = txt("BC = 4 × 5 ÷ 2 = 10", size=30, color=GOLD).move_to([3.5, -0.75, 0])
        self.play(FadeIn(s4, scale=0.97), run_time=1.0)
        self.wait(1.0)

        note = txt("平行 → 同位角相等 → 两角相等 → 相似", size=23, color=DIM)
        note.move_to([0, -2.6, 0])
        self.play(FadeIn(note, shift=UP * 0.04), run_time=1.0)
        self.wait(12.0)
        self.finish_section()

    # ---------------- 6. 易错点 ---------------- 21.7
    def scene_traps(self):
        self.section(6, "三个易错点")

        rows = [
            ("① 面积比不是相似比", "是相似比的平方"),
            ("② 相似式字母一一对应", "A 对 D、B 对 E、C 对 F"),
            ("③ 平行出相似有 A 型与 X 型", "看清是哪一种"),
        ]
        y = 1.9
        for a, b in rows:
            ta = txt(a, size=24, color=RED).move_to([-2.9, y, 0])
            self.play(FadeIn(ta, shift=RIGHT * 0.04), run_time=0.7)
            tb = txt(b, size=22, color=DIM).move_to([3.6, y, 0])
            self.play(FadeIn(tb, shift=RIGHT * 0.04), run_time=0.7)
            y -= 0.95
        self.wait(1.2)

        note = txt("相似比 1 : 3，面积比就是 1 : 9", size=24, color=CHALK)
        note.move_to([0, -1.3, 0])
        self.play(FadeIn(note, shift=UP * 0.04), run_time=0.95)
        self.wait(0.9)

        box = label_box("两角相等，就能判相似", size=29, color=GOLD)
        box.move_to([0, -2.35, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.1)
        self.wait(5.2)
        self.finish_section()

    def construct(self):
        self.scene_intro()
        self.clear_stage()
        self.scene_def()
        self.clear_stage()
        self.scene_aa()
        self.clear_stage()
        self.scene_sss()
        self.clear_stage()
        self.scene_props()
        self.clear_stage()
        self.scene_example()
        self.clear_stage()
        self.scene_traps()
        self.clear_stage(0.8)