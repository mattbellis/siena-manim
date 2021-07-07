from manim import *

class SienaIntro(Scene):
	def construct(self):
		sienacollege = Text("Siena College").set_color(GREEN)
		triangle = Triangle().set_fill(YELLOW)
		square = Square().set_fill(GREEN)
		circle = Circle().set_fill(YELLOW)
		circle2 = Circle().set_fill(YELLOW)
		physics = Text("Department of Physics and Astronomy").set_color(GOLD)
		self.play(Create(circle))
		self.play(Transform(circle, square))
		self.wait(.5)
		self.play(Transform(square, triangle))
		self.wait(.5)
		self.play(Transform(triangle, circle2))
		self.wait(.5)
		self.play(Transform(triangle, sienacollege))
		triangle.shift(UP)
		triangle.shift(UP)
		self.wait(.5)
		self.play(Transform(circle, physics))
		circle.shift(DOWN)
		self.wait()
