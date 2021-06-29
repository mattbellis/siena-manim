from manim import *


class Shapes(Scene):
	def construct(self):
		circle = Circle()
		circle.set_color(BLUE)
		square = Square()
		square.set_color(WHITE)
		triangle = Triangle()
		triangle.set_color(RED)
		circle.shift(RIGHT)
		square.shift(UP)
		triangle.shift(LEFT)

		self.play(FadeIn(circle))
		self.add(Text("Circle").scale(0.5).to_edge(UL).set_color(BLUE))
		self.wait(1)
		self.play(FadeIn(triangle))
		self.add(Text("Triangle").scale(0.5).to_edge(DL).set_color(RED))	
		self.wait(1)
		self.play(FadeIn(square))
		self.add(Text("Square").scale(0.5).to_edge(UR).set_color(WHITE))
		self.wait(1)
		
	
		circle.set_stroke(color = BLUE, width = 10)
		square.set_stroke(color = WHITE, width = 10)
		triangle.set_stroke(color = RED, width = 10)
		self.wait(1)
		square.set_fill(color = WHITE, opacity=0.8)
		circle.set_fill(color = BLUE, opacity=0.8)
		triangle.set_fill(color = RED, opacity = 0.8)
		self.wait(2)
		
		self.play(FadeOut(square), run_time = 3)
		self.play(FadeOut(circle), run_time = 3)
		self.play(FadeOut(triangle), run_time = 3)
