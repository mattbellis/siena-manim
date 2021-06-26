from manim import *


class Shapes(Scene):
	def construct(self):
		circle = Circle()
		square = Square()
#		triangle = Triangle()
		circle.shift(RIGHT)
		square.shift(UP)
#		triangle.shift(LEFT)

		self.add(circle)
		self.play(FadeIn(circle))
		self.add(Text("Circle").scale(0.5).to_edge(UL).set_color(BLUE))
		self.wait(1)
#		self.add(triangle)
	#	self.play(FadeIn(triangle))
	#	self.add(Text("Triangle").scale(0.5).next_to(self.mobjects[-1],DOWN).set_color(RED))	
		self.wait(1)
		self.add(square)
		self.play(FadeIn(square))
		self.add(Text("Square").scale(0.5).to_edge(UL[-1],DOWN).set_color(WHITE))
		self.wait(1)
		
	
		circle.set_stroke(color = BLUE, width = 10)
		square.set_stroke(color = WHITE, width = 10)
	#	triangle.set_stroke(color = RED, width = 10)
		self.wait(1)
		square.set_fill(color = WHITE, opacity=0.8)
		circle.set_fill(color = BLUE, opacity=0.8)
	#	triangle.set_fill(color = RED, opacity = 0.8)
		self.wait(2)
		
		self.play(FadeOut(square, circle), run_time = 3)
		
