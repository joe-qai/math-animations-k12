# -*- coding: utf-8 -*-
"""可能性：一定/可能/不可能、可能性大小。北师大版四年级上册。"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import *  # noqa: F401,F403


def ball_box(x: float, y: float, reds: int, yellows: int, size: float = 1.0):
    """一个装球的盒子，红球在前、黄球在后。"""
    w, h = 2.35 * size, 1.85 * size
    box = Rectangle(width=w, height=h, color=DIM, stroke_width=2.5,
                    fill_color="#151a2b", fill_opacity=1.0)
    box.move_to([x, y, 0])

    total = reds + yellows
    per_row = 5
    rows = (total + per_row - 1) // per_row if total else 0
    balls = VGroup()
    r_ball = 0.17 * size
    for i in range(total):
        r = i // per_row
        c = i % per_row
        cnt = min(per_row, total - r * per_row)
        bx = x + (c - (cnt - 1) / 2) * 0.42 * size
        by = y + ((rows - 1) / 2 - r) * 0.46 * size
        col = RED if i < reds else GOLD
        balls.add(Circle(radius=r_ball, color=col, stroke_width=0,
                         fill_color=col, fill_opacity=1.0).move_to([bx, by, 0]))
    return VGroup(box, balls)


def bar(x0: float, y: float, units: float, color: str, label: str, unit: float = 0.55):
    rect = Rectangle(width=units * unit, height=0.46, color=color, stroke_width=0,
                     fill_color=color, fill_opacity=0.85)
    rect.move_to([x0 + units * unit / 2, y, 0])
    lab = txt(label, size=24, color=color).next_to(rect, LEFT, buff=0.22)
    cnt = txt(str(int(units)), size=24, color=color).next_to(rect, RIGHT, buff=0.16)
    return VGroup(rect, lab, cnt)


class KenengxingScene(NarratedScene):
    lesson = "kenengxing"

    def clear_stage(self, run_time: float = 0.5):
        keep = {id(self._track), id(self._fill)}
        junk = [m for m in self.mobjects if id(m) not in keep]
        if junk:
            self.play(*[FadeOut(m) for m in junk], run_time=run_time)
        self.cur_title = None
        self.cur_sub = None

    # ---------------- 0. 抛硬币 ---------------- 15.2
    def scene_coin(self):
        self.section(0, "抛一枚硬币，说不准")

        coin = Circle(radius=0.92, color=GOLD, stroke_width=4,
                      fill_color=GOLD, fill_opacity=0.12).move_to([-3.7, 1.15, 0])
        face = txt("正", size=58, color=GOLD).move_to([-3.7, 1.15, 0])
        self.play(Create(coin), FadeIn(face), run_time=1.0)
        self.play(Transform(face, txt("反", size=58, color=BLUE).move_to([-3.7, 1.15, 0])),
                  run_time=1.0)
        self.play(Transform(face, txt("正", size=58, color=GOLD).move_to([-3.7, 1.15, 0])),
                  run_time=0.9)

        q = txt("落下来是哪一面？", size=26, color=CHALK).move_to([-3.7, -0.15, 0])
        self.play(FadeIn(q, shift=UP * 0.05), run_time=0.7)

        rows = VGroup(
            txt("明天会不会下雨", size=27, color=CHALK),
            txt("掷骰子掷出几点", size=27, color=CHALK),
            txt("抽奖能不能中", size=27, color=CHALK),
        ).arrange(DOWN, buff=0.38, aligned_edge=LEFT).move_to([3.1, 1.2, 0])
        for r in rows:
            self.play(FadeIn(r, shift=RIGHT * 0.06), run_time=0.6)

        note = txt("说不准的事情，叫随机事件", size=28, color=GREEN)
        note.move_to([0.6, -1.55, 0])
        self.play(FadeIn(note, shift=UP * 0.07), run_time=0.9)
        self.wait(0.8)

        stat = VGroup(
            txt("抛 1000 次", size=27, color=DIM),
            txt("正面约 500 次，反面约 500 次", size=27, color=GOLD),
        ).arrange(DOWN, buff=0.22).move_to([0.6, -2.55, 0])
        self.play(FadeIn(stat[0], shift=UP * 0.05), run_time=0.7)
        self.play(FadeIn(stat[1], shift=UP * 0.05), run_time=0.9)
        self.wait(1.6)
        self.finish_section()

    # ---------------- 1. 三种事件 ---------------- 18.7
    def scene_three(self):
        self.section(1, "一定、可能、不可能")

        items = [
            ("一定", GREEN, "太阳从东边升起", "确定事件"),
            ("不可能", RED, "太阳从西边升起", "确定事件"),
            ("可能", GOLD, "明天会下雨", "不确定事件"),
        ]
        y = 1.9
        for tag, col, text, kind in items:
            box = label_box(tag, size=28, color=col).move_to([-4.2, y, 0])
            line = txt(text, size=30, color=CHALK).move_to([0.9, y, 0])
            k = txt(kind, size=23, color=DIM).move_to([4.35, y, 0])
            self.play(FadeIn(box, scale=0.96), run_time=0.6)
            self.play(FadeIn(line, shift=RIGHT * 0.06), run_time=0.65)
            self.play(FadeIn(k, shift=LEFT * 0.05), run_time=0.6)
            self.wait(0.8)
            y -= 1.15

        note1 = txt("一定发生、不可能发生，都是确定事件", size=25, color=DIM)
        note2 = txt("可能发生也可能不发生，叫不确定事件", size=25, color=DIM)
        note1.move_to([0, -1.85, 0])
        note2.move_to([0, -2.4, 0])
        self.play(FadeIn(note1, shift=UP * 0.05), run_time=0.8)
        self.play(FadeIn(note2, shift=UP * 0.05), run_time=0.8)
        self.wait(1.2)
        self.wait(2.2)
        self.finish_section()

    # ---------------- 2. 摸球 ---------------- 16.7
    def scene_balls(self):
        self.section(2, "盒子里摸球")

        cases = [
            (5, 0, "全是红球", "摸出红球：一定", GREEN),
            (0, 4, "没有红球", "摸出红球：不可能", RED),
            (3, 2, "有红有黄", "摸出红球：可能", GOLD),
        ]
        for idx, (reds, yellows, cond, verdict, col) in enumerate(cases):
            grp = ball_box(-3.6, 0.85, reds, yellows, size=1.05)
            self.play(FadeIn(grp), run_time=0.8)
            self.wait(0.5)

            c = txt(cond, size=26, color=DIM).move_to([2.5, 1.5, 0])
            v = txt(verdict, size=31, color=col).move_to([2.5, 0.65, 0])
            self.play(FadeIn(c, shift=RIGHT * 0.05), run_time=0.6)
            self.play(FadeIn(v, shift=RIGHT * 0.05), run_time=0.7)
            self.wait(1.5)
            if idx < len(cases) - 1:
                self.play(FadeOut(grp), FadeOut(c), FadeOut(v), run_time=0.45)

        tip = txt("一定、可能、不可能，说的都是同一种球", size=26, color=CHALK)
        tip.move_to([0, -2.3, 0])
        self.play(FadeIn(tip, shift=UP * 0.06), run_time=0.8)
        self.wait(1.0)
        self.finish_section()

    # ---------------- 3. 可能性有大有小 ---------------- 13.6
    def scene_bigger(self):
        self.section(3, "谁多，谁的可能性大")

        grp = ball_box(-3.9, 1.0, 5, 1, size=1.0)
        self.play(FadeIn(grp), run_time=0.8)
        self.wait(0.8)

        b1 = bar(-3.9, -0.55, 5, RED, "红球")
        b2 = bar(-3.9, -1.25, 1, GOLD, "黄球")
        self.play(FadeIn(b1, shift=UP * 0.05), run_time=0.7)
        self.play(FadeIn(b2, shift=UP * 0.05), run_time=0.7)
        self.wait(0.8)

        t1 = txt("摸到红球的可能性大", size=28, color=RED).move_to([2.4, 2.0, 0])
        t2 = txt("摸到黄球的可能性小", size=28, color=GOLD).move_to([2.4, 1.35, 0])
        self.play(FadeIn(t1, shift=RIGHT * 0.05), run_time=0.8)
        self.wait(0.5)
        self.play(FadeIn(t2, shift=RIGHT * 0.05), run_time=0.8)
        self.wait(0.6)

        note = txt("哪种球多，摸到哪种球的可能性就大", size=26, color=CHALK)
        note.move_to([0, -2.3, 0])
        self.play(FadeIn(note, shift=UP * 0.06), run_time=0.8)
        self.wait(1.5)
        self.finish_section()

    # ---------------- 4. 数量相同 ---------------- 14.4
    def scene_same(self):
        self.section(4, "一样多，可能性就一样")

        grp = ball_box(-3.9, 1.35, 3, 3, size=0.95)
        self.play(FadeIn(grp), run_time=0.8)
        self.wait(0.6)

        b1 = bar(-3.9, -0.35, 3, RED, "红球")
        b2 = bar(-3.9, -1.05, 3, GOLD, "黄球")
        self.play(FadeIn(b1), FadeIn(b2), run_time=0.8)
        self.wait(0.8)

        eq = VGroup(
            txt("3 个红球 = 3 个黄球", size=27, color=CHALK),
            txt("可能性一样大", size=30, color=GREEN),
        ).arrange(DOWN, buff=0.3).move_to([2.15, 2.05, 0])
        self.play(FadeIn(eq[0], shift=UP * 0.05), run_time=0.7)
        self.play(FadeIn(eq[1], shift=UP * 0.05), run_time=0.9)
        self.wait(0.7)

        note = txt("可能性的大小，比的是数量的多少", size=26, color=DIM)
        note.move_to([0, -1.95, 0])
        self.play(FadeIn(note, shift=UP * 0.06), run_time=0.8)
        self.wait(1.6)
        self.finish_section()

        note = txt("可能性的大小，比的是数量的多少", size=26, color=DIM)
        note.move_to([0, -1.95, 0])
        self.play(FadeIn(note, shift=UP * 0.06), run_time=0.8)
        self.wait(1.6)
        self.finish_section()

    # ---------------- 5. 三个易错点 ---------------- 13.9
    def scene_warn(self):
        self.section(5, "三个易错点")

        items = [
            ("可能发生 = 一定发生", "可能不等于一定"),
            ("可能性小 = 不可能", "小不等于不可能"),
            ("红球多就一定摸到红球", "摸一次只能摸一个，不一定"),
        ]
        y = 1.7
        for bad_s, note in items:
            bad = txt(bad_s, size=29, color=RED).move_to([-3.3, y, 0])
            n = txt(note, size=25, color=GREEN).move_to([3.15, y, 0])
            cross = Line(bad.get_left() + [-0.12, -0.13, 0],
                         bad.get_right() + [0.12, 0.15, 0],
                         color=RED, stroke_width=3)
            self.play(FadeIn(bad, shift=RIGHT * 0.05), run_time=0.6)
            self.play(Create(cross), run_time=0.45)
            self.play(FadeIn(n, shift=RIGHT * 0.05), run_time=0.55)
            self.wait(0.9)
            y -= 1.3

        tip = txt("说可能，就要说清：哪种多，可能性就大", size=26, color=GOLD)
        tip.move_to([0, -2.4, 0])
        self.play(FadeIn(tip, shift=UP * 0.07), run_time=0.9)
        self.wait(1.6)
        self.finish_section()

    # ---------------- 6. 总结 ---------------- 14.7
    def scene_summary(self):
        self.section(6, "三句话")

        rows = VGroup(
            label_box("① 事情分一定、可能、不可能", size=26, color=GOLD),
            label_box("② 数量多的，可能性就大", size=26, color=CHALK),
            label_box("③ 数量相同，可能性相同", size=26, color=GREEN),
        ).arrange(DOWN, buff=0.3).move_to([0, 1.4, 0])
        for r in rows:
            self.play(FadeIn(r, shift=RIGHT * 0.07), run_time=0.65)
            self.wait(0.6)

        demo = txt("5 红 1 黄 → 红球可能性大", size=28, color=RED)
        demo.move_to([0, -1.25, 0])
        self.play(FadeIn(demo, shift=UP * 0.06), run_time=0.85)
        self.wait(0.8)

        end = txt("会用可能说话，就学会了预测", size=28, color=GOLD)
        end.move_to([0, -2.15, 0])
        self.play(FadeIn(end, shift=UP * 0.06), run_time=0.8)
        self.wait(1.8)
        self.finish_section()

    def construct(self):
        self.scene_coin()
        self.clear_stage()
        self.scene_three()
        self.clear_stage()
        self.scene_balls()
        self.clear_stage()
        self.scene_bigger()
        self.clear_stage()
        self.scene_same()
        self.clear_stage()
        self.scene_warn()
        self.clear_stage()
        self.scene_summary()
        self.clear_stage(0.8)