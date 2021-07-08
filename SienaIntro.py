from manim import *

class SienaIntro(Scene):
	def construct(self):
		sienacollege = Text("Siena College").set_color(GREEN_E).scale(2)
		triangle = Triangle().set_color(YELLOW_E).scale(3.45)
		square = Square().set_color(GREEN_E).scale(3)
		circle = Circle(fill_opacity=5).set_color(YELLOW_E).set_fill().scale(3)
		circle2 = Circle().set_color(GREEN_E).scale(3)
		physics = Text("Department of Physics and Astronomy").set_color(YELLOW_E)
		physics.next_to(sienacollege,DOWN,buff=0).scale(1)	
		self.play(Create(circle))
		self.play(Transform(circle, square))
		self.wait(.5)
		self.play(Transform(square, triangle))
		self.wait(.5)
		self.play(Transform(triangle, circle2))
		self.wait(.5)
		
		triangle_logo= triangle.scale(0.2)
		circle_logo= circle.scale(0.2)
		circle_logo.to_corner(DR)
		triangle_logo.to_corner(DR)
	#	self.play(FadeOut(circle))
	#	self.play(FadeOut(square))
		self.play(Transform(square, sienacollege))
		self.wait(.5)
		self.play(Write(physics))
		self.wait()
		self.play(FadeOut(physics))
		square.scale(0.15).next_to(circle,0,buff=0)
		self.wait()
