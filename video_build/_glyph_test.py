# -*- coding: utf-8 -*-
from manim import *


class GlyphTest(Scene):
    def construct(self):
        self.camera.background_color = "#0f1220"
        t = Text("l  ℓ  L  ½  π", font="Microsoft YaHei", font_size=90, color="#f4efe2")
        self.add(t)
        self.wait(0.2)