# -*- coding: utf-8 -*-
"""解直角三角形：已知一边一角（或两边）求其余，仰角俯角与坡度。九年级下。"""

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
    n = txt(num, size=size, color=color)
    d = txt(den, size=size, color=color)
    w = max(n.width, d.width) + 0.26
    line = Line(P(-w / 2, 0), P(w / 2, 0), color=color, stroke_width=2.0)
    n.next_to(line, UP, buff=gap)
    d.next_to(line, DOWN, buff=gap)
    return VGroup(n, line, d)


class JieZhijiaoSanjiaoxingScene(NarratedScene):
    lesson = "jie-zhijiao-sanjiaoxing"

    def clear_stage(self, run_time: float = 0.5):
        keep = {id(self._track), id(self._fill)}
        junk = [m for m in self.mobjects if id(m) not in keep]
        if junk:
            self.play(*[FadeOut(m) for m in junk], run_time=run_time)
        self.cur_title = None
        self.cur_sub = None

    # ---------------- 0. 测楼高 ---------------- 26.3
    def scene_intro(self):
        self.section(0, "站在地上，怎么量楼高")

        ground = Line(P(-6.2, -1.2), P(6.2, -1.2), color=DIM, stroke_width=2.6)
        self.play(Create(ground), run_time=0.8)

        bld = Rectangle(width=3.1, height=3.44, color=CHALK, stroke_width=2.6)
        bld.move_to([3.05, 0.52, 0])
        self.play(Create(bld), run_time=1.0)

        win = VGroup()
        for r in range(3):
            for c in range(2):
                w = Square(side_length=0.34, color=DIM, stroke_width=1.6)
                w.move_to([2.1 + c * 1.05, 1.6 - r * 1.0, 0])
                win.add(w)
        self.play(FadeIn(win), run_time=0.8)

        eye = P(-3.6, -0.7)
        self.play(FadeIn(Dot(eye, radius=0.06, color=GOLD)), run_time=0.5)
        top = P(1.5, 2.24)
        hz = DashedLine(eye, P(1.5, -0.7), color=GREEN, stroke_width=2.0, dash_length=0.11)
        self.play(Create(hz), run_time=0.9)
        sight = Line(eye, top, color=GOLD, stroke_width=2.4)
        self.play(Create(sight), run_time=0.9)

        ar = Arc(radius=0.9, start_angle=0, angle=30 * DEGREES, arc_center=eye,
                 color=GOLD, stroke_width=2.4)
        self.play(Create(ar), run_time=0.7)
        self.play(FadeIn(txt("30°", size=22, color=GOLD).move_to([-2.55, -0.42, 0])), run_time=0.5)

        dim = DoubleArrow(P(-3.6, -1.55), P(1.5, -1.55), color=BLUE, stroke_width=2.0,
                          buff=0, tip_length=0.16)
        self.play(GrowArrow(dim), run_time=0.8)
        self.play(FadeIn(txt("30 米", size=22, color=BLUE).move_to([-1.05, -1.75, 0])), run_time=0.5)

        self.play(FadeIn(txt("眼高 1.6 米", size=20, color=DIM).move_to([-4.5, -0.14, 0])), run_time=0.5)
        self.wait(0.6)

        d = txt("已知一个锐角和一条边，求其他的边", size=26, color=CHALK).move_to([-2.2, -2.45, 0])
        self.play(FadeIn(d, shift=UP * 0.04), run_time=0.95)
        box = label_box("这就是解直角三角形", size=24, color=GOLD).move_to([-2.2, -2.95, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.0)
        self.wait(11.0)
        self.finish_section()

    # ---------------- 1. 什么是解直角三角形 ---------------- 22.0
    def scene_what(self):
        self.section(1, "六个元素，再知两个")

        C = P(-5.0, -1.2)
        A = P(-1.4, -1.2)
        B = P(-5.0, 1.6)
        tri = Polygon(A, B, C, color=CHALK, stroke_width=2.8)
        self.play(Create(tri), run_time=1.1)
        self.play(Create(right_mark(C, UP, RIGHT, 0.2, DIM)), run_time=0.6)

        lC = txt("C", size=21, color=DIM).move_to(C + LEFT * 0.3 + DOWN * 0.22)
        lA = txt("A", size=21, color=GOLD).move_to(A + RIGHT * 0.28 + DOWN * 0.22)
        lB = txt("B", size=21, color=BLUE).move_to(B + LEFT * 0.3 + UP * 0.18)
        self.play(FadeIn(lC), FadeIn(lA), FadeIn(lB), run_time=0.7)

        ar = Arc(radius=0.85, start_angle=142.4 * DEGREES, angle=37.6 * DEGREES, arc_center=A,
                 color=GOLD, stroke_width=2.4)
        br = Arc(radius=0.55, start_angle=270 * DEGREES, angle=37.6 * DEGREES, arc_center=B,
                 color=BLUE, stroke_width=2.2)
        self.play(Create(ar), Create(br), run_time=0.8)
        self.wait(0.6)

        rows = [
            ("三个角：∠A、∠B、∠C = 90°", CHALK),
            ("三条边：a、b、c", CHALK),
            ("再知两个元素，且至少一个是边", GOLD),
            ("剩下的就都能求出来", GREEN),
        ]
        y = 1.75
        for s, col in rows:
            t = txt(s, size=25, color=col).move_to([3.1, y, 0])
            self.play(FadeIn(t, shift=RIGHT * 0.04), run_time=0.85)
            y -= 0.85
        self.wait(0.8)

        box = label_box("已知一边一锐角，是最常见的一类", size=23, color=GOLD)
        box.move_to([3.1, -2.35, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.0)
        self.wait(7.0)
        self.finish_section()

    # ---------------- 2. 选公式 ---------------- 29.5
    def scene_pick(self):
        self.section(2, "已知谁，求谁，选哪个式子")

        C = P(-5.4, -1.3)
        A = P(-2.4, -1.3)
        B = P(-5.4, 1.1)
        tri = Polygon(A, B, C, color=CHALK, stroke_width=2.6)
        self.play(Create(tri), run_time=1.0)
        self.play(Create(right_mark(C, UP, RIGHT, 0.18, DIM)), run_time=0.5)
        self.play(FadeIn(txt("A", size=21, color=GOLD).move_to(A + RIGHT * 0.24 + DOWN * 0.2)), run_time=0.4)
        ar = Arc(radius=0.8, start_angle=141.3 * DEGREES, angle=38.7 * DEGREES, arc_center=A,
                 color=GOLD, stroke_width=2.2)
        self.play(Create(ar), run_time=0.6)
        self.play(FadeIn(txt("a", size=21, color=BLUE).move_to([-5.75, -0.1, 0])), run_time=0.4)
        self.play(FadeIn(txt("b", size=21, color=GREEN).move_to([-3.9, -1.62, 0])), run_time=0.4)
        self.play(FadeIn(txt("c", size=21, color=RED).move_to([-3.75, 0.3, 0])), run_time=0.4)
        self.wait(0.6)

        rows = [
            ("求对边 a：a = c·sinA，a = b·tanA", BLUE),
            ("求邻边 b：b = c·cosA", GREEN),
            ("求斜边 c：c = b / cosA，c = a / sinA", RED),
        ]
        y = 1.75
        for s, col in rows:
            t = txt(s, size=24, color=col).move_to([2.85, y, 0])
            self.play(FadeIn(t, shift=RIGHT * 0.04), run_time=0.95)
            y -= 0.95
        self.wait(0.7)

        tip = txt("一个式子里只留一个未知数，就能解", size=23, color=CHALK)
        tip.move_to([2.85, -1.35, 0])
        self.play(FadeIn(tip, shift=UP * 0.04), run_time=0.9)
        self.wait(0.6)

        box = label_box("看已知谁、求谁，选含这两条边的式子", size=22, color=GOLD)
        box.move_to([2.85, -2.3, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.0)
        self.wait(10.5)
        self.finish_section()

    # ---------------- 3. 四步 ---------------- 22.5
    def scene_steps(self):
        self.section(3, "解直角三角形的四步")

        steps = [
            ("第一步", "画图，把已知条件标上去"),
            ("第二步", "看清已知哪条边、要求哪条边"),
            ("第三步", "选一个含这两条边的式子"),
            ("第四步", "解方程，按题目要求取近似"),
        ]
        y = 2.05
        prev = None
        for tag, body in steps:
            chip = txt(tag, size=22, color=GOLD)
            chip.move_to([-5.15, y, 0])
            txtb = txt(body, size=25, color=CHALK).move_to([0.15, y, 0])
            self.play(FadeIn(chip, shift=RIGHT * 0.04), run_time=0.6)
            self.play(FadeIn(txtb, shift=RIGHT * 0.04), run_time=0.7)
            if prev is not None:
                pass
            prev = y
            y -= 1.05
        self.wait(0.9)

        box = label_box("不会选式子，就回到定义：对边、邻边、斜边", size=22, color=RED)
        box.move_to([0, -2.55, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.05)
        self.wait(8.5)
        self.finish_section()

    # ---------------- 4. 仰角、俯角与坡度 ---------------- 26.0
    def scene_angles(self):
        self.section(4, "仰角、俯角与坡度")

        # 仰角
        h1 = txt("仰角：从下往上看", size=23, color=GOLD).move_to([-3.7, 2.35, 0])
        self.play(FadeIn(h1, shift=UP * 0.04), run_time=0.85)
        eye1 = P(-5.8, -0.35)
        hz1 = DashedLine(eye1, P(-2.3, -0.35), color=GREEN, stroke_width=1.8, dash_length=0.1)
        sight1 = Line(eye1, P(-2.3, 1.45), color=GOLD, stroke_width=2.2)
        self.play(Create(hz1), run_time=0.6)
        self.play(Create(sight1), run_time=0.7)
        a1 = Arc(radius=0.75, start_angle=0, angle=27.2 * DEGREES, arc_center=eye1,
                 color=GOLD, stroke_width=2.2)
        self.play(Create(a1), run_time=0.6)
        self.play(FadeIn(txt("仰角", size=18, color=GOLD).move_to([-5.0, -0.12, 0])), run_time=0.5)
        self.wait(0.6)

        # 俯角
        h2 = txt("俯角：从上往下看", size=23, color=BLUE).move_to([3.4, 2.35, 0])
        self.play(FadeIn(h2, shift=UP * 0.04), run_time=0.85)
        eye2 = P(1.4, 0.85)
        hz2 = DashedLine(eye2, P(5.6, 0.85), color=GREEN, stroke_width=1.8, dash_length=0.1)
        sight2 = Line(eye2, P(4.4, -0.55), color=BLUE, stroke_width=2.2)
        self.play(Create(hz2), run_time=0.6)
        self.play(Create(sight2), run_time=0.7)
        a2 = Arc(radius=0.7, start_angle=-26.4 * DEGREES, angle=26.4 * DEGREES, arc_center=eye2,
                 color=BLUE, stroke_width=2.2)
        self.play(Create(a2), run_time=0.6)
        self.play(FadeIn(txt("俯角", size=18, color=BLUE).move_to([2.15, 0.68, 0])), run_time=0.5)
        self.wait(0.7)

        note = txt("两个角都从水平线算起，不从竖直线算", size=23, color=RED)
        note.move_to([0, -1.45, 0])
        self.play(FadeIn(note, shift=UP * 0.04), run_time=0.9)
        self.wait(0.6)

        f = txt("坡度 i = 竖直高度 / 水平宽度 = tanα", size=28, color=GOLD)
        f.move_to([0, -2.35, 0])
        self.play(FadeIn(f, scale=0.98), run_time=1.0)
        self.wait(0.6)

        box = label_box("坡度是正切，不是正弦", size=23, color=RED).move_to([0, -2.95, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.0)
        self.wait(6.0)
        self.finish_section()

    # ---------------- 5. 例题：楼高 ---------------- 30.8
    def scene_example(self):
        self.section(5, "例：仰角 30°，距离 30 米")

        ground = Line(P(-6.3, -1.5), P(0.4, -1.5), color=DIM, stroke_width=2.4)
        self.play(Create(ground), run_time=0.7)

        eye = P(-5.3, -1.1)
        self.play(FadeIn(Dot(eye, radius=0.06, color=GOLD)), run_time=0.5)
        hz = DashedLine(eye, P(-2.0, -1.1), color=GREEN, stroke_width=1.8, dash_length=0.1)
        self.play(Create(hz), run_time=0.6)
        bld = Polygon(P(-2.0, -1.5), P(-1.3, -1.5), P(-1.3, 0.8), P(-2.0, 0.8),
                      color=CHALK, stroke_width=2.4)
        self.play(Create(bld), run_time=0.8)
        sight = Line(eye, P(-2.0, 0.8), color=GOLD, stroke_width=2.2)
        self.play(Create(sight), run_time=0.8)
        ar = Arc(radius=0.7, start_angle=0, angle=30 * DEGREES, arc_center=eye,
                 color=GOLD, stroke_width=2.2)
        self.play(Create(ar), run_time=0.6)
        self.play(FadeIn(txt("30°", size=21, color=GOLD).move_to([-4.55, -0.95, 0])), run_time=0.5)
        self.play(FadeIn(txt("30", size=21, color=BLUE).move_to([-3.65, -1.32, 0])), run_time=0.5)
        self.play(FadeIn(txt("1.6", size=20, color=DIM).move_to([-5.75, -1.06, 0])), run_time=0.5)
        self.wait(0.6)

        rows = [
            ("h = 30 · tan30° = 10√3 ≈ 17.3", GOLD),
            ("楼高 = 17.3 + 1.6 ≈ 18.9 米", GREEN),
        ]
        y = 0.15
        for s, col in rows:
            t = txt(s, size=27, color=col).move_to([3.25, y, 0])
            self.play(FadeIn(t, shift=UP * 0.04), run_time=1.0)
            y -= 1.25
        self.wait(0.8)

        note = txt("眼高别忘加，这是最容易丢分的地方", size=23, color=RED)
        note.move_to([3.25, -1.85, 0])
        self.play(FadeIn(note, shift=UP * 0.04), run_time=0.95)
        self.wait(0.5)

        box = label_box("先算三角形，再加眼高", size=24, color=GOLD).move_to([3.25, -2.65, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.0)
        self.wait(10.0)
        self.finish_section()

    # ---------------- 6. 易错点 ---------------- 27.2
    def scene_traps(self):
        self.section(6, "四个易错点")

        rows = [
            ("① 正弦余弦用反", "求邻边时错乘 sin"),
            ("② 仰角从竖直线算", "都从水平线算起"),
            ("③ 坡度当成正弦", "坡度 = tanα"),
            ("④ 单位不统一", "米和厘米先统一"),
        ]
        y = 1.85
        for a, b in rows:
            ta = txt(a, size=23, color=RED).move_to([-2.6, y, 0])
            tb = txt(b, size=21, color=DIM).move_to([3.6, y, 0])
            self.play(FadeIn(ta, shift=RIGHT * 0.04), run_time=0.65)
            self.play(FadeIn(tb, shift=RIGHT * 0.04), run_time=0.65)
            y -= 0.86
        self.wait(1.0)

        box = label_box("画图标边，选式求解，按需取近似", size=23, color=GOLD)
        box.move_to([0, -2.45, 0])
        self.play(FadeIn(box, scale=0.97), run_time=1.1)
        self.wait(12.0)
        self.finish_section()

    def construct(self):
        self.scene_intro()
        self.clear_stage()
        self.scene_what()
        self.clear_stage()
        self.scene_pick()
        self.clear_stage()
        self.scene_steps()
        self.clear_stage()
        self.scene_angles()
        self.clear_stage()
        self.scene_example()
        self.clear_stage()
        self.scene_traps()
        self.clear_stage(0.8)