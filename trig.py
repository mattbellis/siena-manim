import math
import numpy as np



from manim import *

class SienaIntro(Scene):
	def construct(self):
		sienacollege = Text("Siena College").set_color(GREEN_E).scale(2)
		triangle = Triangle().set_color(YELLOW_E).scale(1.50)
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

		
		TrigTips= Text("Trig Tips").set_color(BLUE)
		self.play(FadeIn(TrigTips))
		self.wait(3)
		self.play(FadeOut(TrigTips))
		
		dot = Dot()
		self.play(ShowCreation(dot))
		dot.shift(RIGHT*2)
		zero = Tex("$0$").next_to(dot)
		self.play(Write(zero))
		
		self.wait()
		angle1 = math.radians(90)
		arc1 = Arc(radius=2,angle=angle1).set_color(RED)
		self.play(ShowCreation(arc1))
		two = Tex("$90^{\\circ}\\text{ or }\\frac{\\pi}{2}$").next_to(arc1).set_color(RED)
		two.shift(RIGHT)
		self.play(Write(two))

		self.wait()
		angle2 = math.radians(180)
		arc2 = Arc(radius = 2, angle = angle2).set_color(BLUE)
		self.play(ShowCreation(arc2))
		three = Tex("$180^{\\circ}\\text{ or }\\pi$").next_to(arc2).set_color(BLUE)
		three.shift(LEFT*8)
		self.play(Write(three))

		self.wait()
		angle3 = math.radians(270)
		arc3 = Arc(radius=2,angle=angle3).set_color(YELLOW)
		self.play(ShowCreation(arc3))
		four = Tex("$270^{\\circ}\\text{ or }\\frac{3\\pi}{2}$").next_to(arc3).set_color(YELLOW)
		four.shift(LEFT*8+DOWN)
		self.play(Write(four))

		self.wait()
		angle4 = math.radians(360)
		arc4 = Arc(radius=2,angle=angle4).set_color(PURPLE)
		self.play(ShowCreation(arc4))
		five = Tex("$360^{\\circ} \\text{ or } 2\\pi$").set_color(PURPLE)
		five.shift(DOWN+RIGHT*4)
		self.play(Write(five))
		





#conclusion from word problems
