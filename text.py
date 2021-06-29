from manim import *


class MovingBox(Scene):
		
	def construct(self):
		title = Text("Simplifying Equations",color = PURPLE).scale(1.4)
		self.add(title)
		self.wait()
		self.play(FadeOut(title))
		text = MathTex("0=","x","+5","+2x")
		self.play(Write(text))
		step1 = Text("Step 1 : Box all matching variables").to_corner(UL)
		self.add(step1)
		self.wait()
		framebox1 = SurroundingRectangle(text[1],buff=.1).set_color(YELLOW)
		framebox2 = SurroundingRectangle(text[3],buff=.1).set_color(YELLOW)
		framebox3 = SurroundingRectangle(text[2],buff=.1).set_color(BLUE)
		self.play(Create(framebox1))
		self.wait()
		self.play(Create(framebox2))
		self.wait()
		self.play(Create(framebox3))
		self.wait()
		
