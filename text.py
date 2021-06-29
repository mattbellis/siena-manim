from manim import *

class MovingBox(Scene):
	def construct(self):
		text = MathTex("0" = "x","+", "5","+","2x")
		self.play(Write(text))
		framebox1 = SurroundingCircle(text[1],buff=.1)
		framebox2 = SurroundingCircle(text[5],buff=.1)
		framebox3 = SurroundingRectangle(text[3],buff=.1)
		self.play(Create(framebox1))
		self.wait()
		self.play(Create(framebox2))
		self.wait()
		self.play(Create(framebox3))
		self.wait()
