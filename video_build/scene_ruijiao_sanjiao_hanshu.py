# -*- coding: utf-8 -*-
"""锐角三角函数：正弦、余弦、正切的定义，特殊角，变化规律与同角关系。九年级下。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


def P(x, y):
    return np.array([float(x), float(y), 0.0])


def right_mark(vertex, d1, d2, size: float = 0.2, color=CHALK) -> Mobject:
    return Polygon(vertex + d1 * size, vertex + d1 * size + d2 * size,
                   vertex + d2 * size, color=color, stroke_width=2.0)


def fracm(num: str, den: str, size: int = 24, color=GOLD, gap: float = 0.08) -> VGroup:
    """竖排分式。"""
    n = txt(num, size=size, color=color)
    d = txt(den, size=size, color=color)
    w = max(n.width, d.width) + 0.26
    line = Line(P(-w / 2, 0), P(w / 2, 0), color=color, stroke_width=2.0)
    n.next_to(line, UP, buff=gap)
    d.next_to(line, DOWN, buff=gap)
    return VGroup(n, line, d)


class RuijiaoSanjiaoHanshuScene(NarratedScene):
    lesson = "ruijiao-sanjiao-hanshu"

    def clear_stage(self, run_time: float = 0.5):
        keep = {id(self._track), id(self._fill)}
        junk = [m for m in self.mobjects if id(m) not in keep]
        if junk:
            self.play(*[FadeOut(m) for m in junk], run_time=run_time)
        self.cur_title = None
        self.cur_sub = None

    # ---------------- 0. 角度一定，比值不变 ---------------- 30.5
    def scene_intro(self):
        self.section(0, "角度一定，比值不变")

        cards = [(-4.35, "推车上坡", GOLD), (0.0, "放风筝", GREEN), (4.35, "梯子靠墙", BLUE)]
        for cx, name, col in cards:
            t = txt(name, size=24, color=col).move_to([cx, 2.55, 0])
            self.play(FadeIn(t, shift=UP * 0.04), run_time=0.7)

        # 斜坡
        cx = -4.35
        tri = Polygon(P(cx - 1.6, -1.15), P(cx + 1.6, -1.15), P(cx + 1.6, 0.65),
                      color=CHALK, stroke_width=2.6)
        self.play(Create(tri), run_time=0.9)
        self.play(Create(right_mark(P(cx + 1.6, -1.15), LEFT, UP, 0.18, DIM)), run_time=0.5)
        arc = Arc(radius=0.55, start_angle=0, angle=39 * DEGREES,
                  arc_center=P(cx - 1.6, -1.15), color=GOLD, stroke_width=2.4)
        self.play(Create(arc), run_time=0.6)
        self.play(FadeIn(txt("坡角", size=19, color=GOLD).move_to([cx - 0.55, -0.85, 0])), run_time=0.5)

        # 风筝
        cx = 0.0
        kite = Polygon(P(cx - 0.4, 1.5), P(cx, 1.95), P(cx + 0.4, 1.5), P(cx, 1.0),
                       color=GOLD, stroke_width=2.4)
        self.play(Create(kite), run_time=0.9)
        ground = Line(P(cx - 1.9, -1.15), P(cx + 1.9, -1.15), color=DIM, stroke_width=2.2)
        self.play(Create(ground), run_time=0.5)
        strl = Line(P(cx - 1.75, -1.15), P(cx, 1.1), color=CHALK, stroke_width=2.0)
        self.play(Create(strl), run_time=0.7)
        arc2 = Arc(radius=0.6, start_angle=0, angle=50 * DEGREES,
                   arc_center=P(cx - 1.75, -1.15), color=GREEN, stroke_width=2.2)
        self.play(Create(arc2), run_time=0.6)

        # 梯子
        cx = 4.35
        wall = Line(P(cx + 1.1, -1.15), P(cx + 1.1, 2.1), color=DIM, stroke_width=2.4)
        floor = Line(P(cx - 1.4, -1.15), P(cx + 1.4, -1.15), color=DIM, stroke_width=2.2)
        self.play(Create(wall), Create(floor), run_time=0.7)
        lad = Line(P(cx - 1.05, -1.15), P(cx + 1.1, 1.95), color=CHALK, stroke_width=3.0)
        self.play(Create(lad), run_time=0.8)
        u = np.array([2.15, 3.1, 0.0])
        u = u / np.linalg.norm(u)
        nrm = np.array([-u[1], u[0], 0.0])
        for k in range(1, 7):
            p = P(cx - 1.05, -1.15) + u * (k * 0.46)
            l = Line(p - nrm * 0.19, p + nrm * 0.19, color=CHALK, stroke_width=2.0)
            self.play(Create(l), run_time=0.18)
        arc3 = Arc(radius=0.52, start_angle=0, angle=55 * DEGREES,
                   arc_center=P(cx - 1.05, -1.15), color=BLUE, stroke_width=2.2)
        self.play(Create(arc3), run_time=0.6)
        self.wait(0.5)

        d = txt("角度固定，两条边的比值就固定", size=26, color=CHALK).move_to([0, -2.0, 0])
        self.play(FadeIn(d, shift=UP * 0.04), run_time=0.95)

        box = label_box("比值只随角的大小改变，与三角形大小无关", size=23, color=GOLD)
        box.move_to([0, -2.85, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.05)
        self.wait(15.5)
        self.finish_section()

    # ---------------- 1. 定义 ---------------- 26.0
    def scene_def(self):
        self.section(1, "正弦、余弦、正切")

        C = P(-5.05, -1.15)
        A = P(-1.55, -1.15)
        B = P(-5.05, 1.55)
        tri = Polygon(A, B, C, color=CHALK, stroke_width=2.8)
        self.play(Create(tri), run_time=1.1)
        self.play(Create(right_mark(C, UP, RIGHT, 0.2, DIM)), run_time=0.6)

        lC = txt("C", size=22, color=DIM).move_to(C + LEFT * 0.3 + DOWN * 0.24)
        lA = txt("A", size=22, color=GOLD).move_to(A + RIGHT * 0.26 + DOWN * 0.24)
        lB = txt("B", size=22, color=CHALK).move_to(B + LEFT * 0.3 + UP * 0.2)
        self.play(FadeIn(lC), FadeIn(lA), FadeIn(lB), run_time=0.7)

        arc = Arc(radius=0.85, start_angle=142.4 * DEGREES, angle=37.6 * DEGREES, arc_center=A,
                  color=GOLD, stroke_width=2.6)
        self.play(Create(arc), run_time=0.7)
        self.wait(0.3)

        # 三条边的名字
        self.play(FadeIn(txt("对边 a", size=22, color=BLUE).move_to([-5.62, 0.2, 0])), run_time=0.6)
        self.play(FadeIn(txt("邻边 b", size=22, color=GREEN).move_to([-3.3, -1.52, 0])), run_time=0.6)
        self.play(FadeIn(txt("斜边 c", size=22, color=RED).move_to([-2.45, 0.92, 0])), run_time=0.6)
        self.wait(0.9)

        rows = [
            ("sinA =", "对边", "斜边", "a / c", BLUE),
            ("cosA =", "邻边", "斜边", "b / c", GREEN),
            ("tanA =", "对边", "邻边", "a / b", GOLD),
        ]
        y = 1.75
        for lab, num, den, short, col in rows:
            g = VGroup(
                txt(lab, size=27, color=col),
                fracm(num, den, 24, col),
                txt("=", size=27, color=col),
                txt(short, size=27, color=col),
            ).arrange(RIGHT, buff=0.2).move_to([2.9, y, 0])
            self.play(FadeIn(g, shift=RIGHT * 0.04), run_time=1.0)
            y -= 1.35
        self.wait(0.8)

        note = txt("三个比值只和角 A 的大小有关", size=23, color=RED).move_to([2.9, -2.4, 0])
        self.play(FadeIn(note, shift=UP * 0.04), run_time=0.95)
        self.wait(9.0)
        self.finish_section()

    # ---------------- 2. 特殊角 ---------------- 32.7
    def scene_special(self):
        self.section(2, "特殊角的三角函数值")

        cw, chh = 1.5, 0.66
        ox, oy = -6.0, 2.0
        head = ["角 A", "30°", "45°", "60°"]
        body = [
            ["sinA", "1/2", "√2/2", "√3/2"],
            ["cosA", "√3/2", "√2/2", "1/2"],
            ["tanA", "√3/3", "1", "√3"],
        ]
        cells = VGroup()
        colors = {}
        for r, row in enumerate([head] + body):
            for c, val in enumerate(row):
                sq = Rectangle(width=cw, height=chh)
                sq.move_to([ox + c * cw + cw / 2, oy - r * chh - chh / 2, 0])
                sq.set_color(DIM).set_stroke(width=1.4)
                col = CHALK if r == 0 else (GOLD if c == 0 else CHALK)
                if r > 0 and c == 0:
                    col = [BLUE, GREEN, GOLD][r - 1]
                tt = txt(val, size=24, color=col).move_to(sq)
                cells.add(sq, tt)
                if r > 0 and c > 0:
                    colors[(r, c)] = (sq, tt)
        self.play(FadeIn(cells), run_time=1.5)
        self.wait(0.8)

        self.play(colors[(1, 1)][0].animate.set_color(GOLD).set_fill(GOLD, 0.18),
                  colors[(1, 2)][0].animate.set_color(GOLD).set_fill(GOLD, 0.18),
                  colors[(1, 3)][0].animate.set_color(GOLD).set_fill(GOLD, 0.18),
                  run_time=0.8)
        self.wait(1.0)

        t1 = txt("正弦：1/2 → √2/2 → √3/2，依次变大", size=24, color=GOLD)
        t1.move_to([3.4, 1.55, 0])
        self.play(FadeIn(t1, shift=UP * 0.04), run_time=0.9)
        t2 = txt("余弦正好倒过来", size=24, color=GREEN).move_to([3.4, 0.65, 0])
        self.play(FadeIn(t2, shift=UP * 0.04), run_time=0.9)
        t3 = txt("正切：√3/3 → 1 → √3", size=24, color=BLUE).move_to([3.4, -0.25, 0])
        self.play(FadeIn(t3, shift=UP * 0.04), run_time=0.9)
        self.wait(0.7)

        box = label_box("这三组值必须默写到条件反射", size=24, color=RED)
        box.move_to([3.4, -1.85, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.0)
        self.wait(14.0)
        self.finish_section()

    # ---------------- 3. 变化规律 ---------------- 30.5
    def scene_trend(self):
        self.section(3, "锐角越大，谁大谁小")

        ax = Axes(x_range=[0, 90, 30], y_range=[0, 1, 0.5], x_length=6.0, y_length=2.9,
                  axis_config={"color": DIM, "stroke_width": 2.0,
                               "include_numbers": False, "tip_length": 0.16})
        ax.move_to([-3.0, -0.35, 0])
        self.play(Create(ax), run_time=1.1)

        for xv in (0, 30, 45, 60, 90):
            lab = txt(str(xv), size=18, color=DIM)
            lab.next_to(ax.c2p(xv, 0), DOWN, buff=0.16)
            self.add(lab)
        for yv in (0.5, 1.0):
            lab = txt(str(yv), size=18, color=DIM)
            lab.next_to(ax.c2p(0, yv), LEFT, buff=0.14)
            self.add(lab)
        xl = txt("角度", size=21, color=DIM).next_to(ax.c2p(90, 0), DOWN, buff=0.42)
        self.play(FadeIn(xl), run_time=0.5)

        s_curve = ax.plot(lambda d: np.sin(d * DEGREES), x_range=[0, 90], color=GOLD, stroke_width=3.0)
        c_curve = ax.plot(lambda d: np.cos(d * DEGREES), x_range=[0, 90], color=GREEN, stroke_width=3.0)
        self.play(Create(s_curve), run_time=1.3)
        self.play(Create(c_curve), run_time=1.3)

        ls = txt("sin", size=24, color=GOLD).move_to(ax.c2p(78, 0.95) + UP * 0.22)
        lc = txt("cos", size=24, color=GREEN).move_to(ax.c2p(20, 0.98) + UP * 0.22)
        self.play(FadeIn(ls), FadeIn(lc), run_time=0.7)

        dot = Dot(ax.c2p(45, np.sin(45 * DEGREES)), radius=0.06, color=RED)
        dl = DashedLine(ax.c2p(45, 0), ax.c2p(45, np.sin(45 * DEGREES)), color=RED,
                        stroke_width=1.8, dash_length=0.1)
        self.play(Create(dl), FadeIn(dot), run_time=0.7)
        self.wait(0.8)

        rows = [
            ("锐角变大：sin 变大，cos 变小", CHALK),
            ("tan 也变大，可以大于 1", CHALK),
            ("0 < sinA < 1，0 < cosA < 1", GOLD),
        ]
        y = 1.85
        for s, col in rows:
            t = txt(s, size=24, color=col).move_to([3.7, y, 0])
            self.play(FadeIn(t, shift=RIGHT * 0.04), run_time=0.9)
            y -= 0.82
        self.wait(0.7)

        note = txt("直角边一定比斜边短，所以 sin、cos 不会大于 1", size=21, color=RED)
        note.move_to([3.7, -1.6, 0])
        self.play(FadeIn(note, shift=UP * 0.04), run_time=0.95)
        self.wait(11.0)
        self.finish_section()

    # ---------------- 4. 同角关系 ---------------- 24.9
    def scene_relation(self):
        self.section(4, "两条常用关系")

        f1 = txt("sin²A + cos²A = 1", size=40, color=GOLD).move_to([-2.6, 1.85, 0])
        self.play(FadeIn(f1, scale=0.98), run_time=1.0)
        self.wait(0.6)

        f2 = txt("tanA = sinA / cosA", size=34, color=GREEN).move_to([-2.6, 0.55, 0])
        self.play(FadeIn(f2, scale=0.98), run_time=1.0)
        self.wait(0.6)

        f3 = txt("sinA = cos(90° − A)", size=34, color=BLUE).move_to([-2.6, -0.75, 0])
        self.play(FadeIn(f3, scale=0.98), run_time=1.0)
        self.wait(0.8)

        note = txt("第一条就是勾股定理除以斜边的平方", size=22, color=DIM)
        note.move_to([-2.6, -1.85, 0])
        self.play(FadeIn(note, shift=UP * 0.04), run_time=0.9)
        self.wait(0.6)

        # 右侧小三角形：互余
        cx = 3.6
        C = P(cx - 1.0, -1.25)
        A = P(cx + 0.9, -1.25)
        B = P(cx - 1.0, 1.15)
        tri = Polygon(A, B, C, color=CHALK, stroke_width=2.4)
        self.play(Create(tri), run_time=0.9)
        self.play(Create(right_mark(C, UP, RIGHT, 0.16, DIM)), run_time=0.5)
        la = txt("A", size=20, color=GOLD).move_to(A + RIGHT * 0.22 + DOWN * 0.2)
        lb = txt("B", size=20, color=BLUE).move_to(B + UP * 0.22)
        self.play(FadeIn(la), FadeIn(lb), run_time=0.6)
        ar = Arc(radius=0.5, start_angle=128.4 * DEGREES, angle=51.6 * DEGREES, arc_center=A,
                 color=GOLD, stroke_width=2.0)
        br = Arc(radius=0.42, start_angle=270 * DEGREES, angle=38 * DEGREES,
                 arc_center=B, color=BLUE, stroke_width=2.0)
        self.play(Create(ar), Create(br), run_time=0.7)
        self.wait(0.6)

        tip = txt("A 的对边正好是 B 的邻边", size=21, color=CHALK).move_to([3.6, -2.15, 0])
        self.play(FadeIn(tip, shift=UP * 0.04), run_time=0.9)
        self.wait(7.0)
        self.finish_section()

    # ---------------- 5. 例题 ---------------- 33.2
    def scene_example(self):
        self.section(5, "例：斜边 13，直角边 5")

        C = P(-4.9, -1.35)
        A = P(-1.1, -1.35)
        B = P(-4.9, 1.2)
        tri = Polygon(A, B, C, color=CHALK, stroke_width=2.8)
        self.play(Create(tri), run_time=1.0)
        self.play(Create(right_mark(C, UP, RIGHT, 0.18, DIM)), run_time=0.5)
        lC = txt("C", size=21, color=DIM).move_to(C + LEFT * 0.28 + DOWN * 0.2)
        lA = txt("A", size=21, color=GOLD).move_to(A + RIGHT * 0.24 + DOWN * 0.2)
        lB = txt("B", size=21, color=CHALK).move_to(B + LEFT * 0.28 + UP * 0.18)
        self.play(FadeIn(lC), FadeIn(lA), FadeIn(lB), run_time=0.7)

        self.play(FadeIn(txt("5", size=23, color=BLUE).move_to([-5.28, 0.0, 0])), run_time=0.5)
        self.play(FadeIn(txt("13", size=23, color=RED).move_to([-2.72, 0.62, 0])), run_time=0.5)
        self.play(FadeIn(txt("12", size=23, color=GREEN).move_to([-3.0, -1.68, 0])), run_time=0.5)
        self.wait(0.7)

        step1 = txt("AC² = 13² − 5² = 144，AC = 12", size=24, color=CHALK)
        step1.move_to([3.0, 1.85, 0])
        self.play(FadeIn(step1, shift=UP * 0.04), run_time=0.95)
        self.wait(0.7)

        rows = [
            ("sinA = 5/13", BLUE),
            ("cosA = 12/13", GREEN),
            ("tanA = 5/12", GOLD),
        ]
        y = 0.55
        for s, col in rows:
            t = txt(s, size=31, color=col).move_to([3.0, y, 0])
            self.play(FadeIn(t, shift=UP * 0.04), run_time=0.85)
            y -= 0.95
        self.wait(0.8)

        box = label_box("先认清边：对边、邻边、斜边", size=23, color=RED)
        box.move_to([3.0, -2.35, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.05)
        self.wait(12.5)
        self.finish_section()

    # ---------------- 6. 易错点 ---------------- 28.2
    def scene_traps(self):
        self.section(6, "四个易错点")

        rows = [
            ("① 对边邻边找错", "先看清是哪个角"),
            ("② sinA 拆成 sin 乘 A", "sinA 是一个整体"),
            ("③ 算出 sin 大于 1", "正弦余弦一定小于 1"),
            ("④ 特殊角的值记混", "30°、45°、60° 反复默写"),
        ]
        y = 1.85
        for a, b in rows:
            ta = txt(a, size=23, color=RED).move_to([-2.6, y, 0])
            tb = txt(b, size=21, color=DIM).move_to([3.6, y, 0])
            self.play(FadeIn(ta, shift=RIGHT * 0.04), run_time=0.65)
            self.play(FadeIn(tb, shift=RIGHT * 0.04), run_time=0.65)
            y -= 0.86
        self.wait(1.0)

        box = label_box("定角，认边，写比值", size=27, color=GOLD)
        box.move_to([0, -2.45, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.1)
        self.wait(13.0)
        self.finish_section()

    def construct(self):
        self.scene_intro()
        self.clear_stage()
        self.scene_def()
        self.clear_stage()
        self.scene_special()
        self.clear_stage()
        self.scene_trend()
        self.clear_stage()
        self.scene_relation()
        self.clear_stage()
        self.scene_example()
        self.clear_stage()
        self.scene_traps()
        self.clear_stage(0.8)