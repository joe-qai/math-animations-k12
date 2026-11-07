# -*- coding: utf-8 -*-
from manim import *


class TestGlyph(Scene):
    def construct(self):
        t1 = Text("√2 ≈ 1.414　√9 = 3　−√16 = −4", font="Microsoft YaHei", font_size=48)
        t2 = Text("³√8 = 2　³√−27 = −3　a ≥ 0　a ≠ 0", font="Microsoft YaHei", font_size=48)
        t3 = Text("√(a²) = |a|　(√a)² = a　±3", font="Microsoft YaHei", font_size=48)
        g = VGroup(t1, t2, t3).arrange(DOWN, buff=0.8)
        self.add(g)
        self.wait(1.0)