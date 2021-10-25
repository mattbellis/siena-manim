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

		
		Title= Text("Radian-Degree Conversions").set_color(BLUE)
		self.play(FadeIn(Title))
		self.wait(3)
		self.play(FadeOut(Title))
		
		dot = Dot()
		dot.shift(RIGHT*2)
		self.play(ShowCreation(dot))
		zero = Tex("$0$").next_to(dot)
		zero.shift(LEFT)
		self.play(Write(zero))
		
		self.wait()
		angle1 = math.radians(90)
		arc1 = Arc(radius=2,angle=angle1).set_color(RED)
		self.play(ShowCreation(arc1))
		two = Tex("$90^{\\circ}\\text{ or }\\frac{\\pi}{2}$").set_color(RED)
		two.shift(UP*2.5)
		self.play(Write(two))

		self.wait()
		angle2 = math.radians(180)
		arc2 = Arc(radius = 2, angle = angle2).set_color(BLUE)
		self.play(ShowCreation(arc2))
		three = Tex("$180^{\\circ}\\text{ or }\\pi$").set_color(BLUE)
		three.shift(LEFT*4)
		self.play(Write(three))

		self.wait()
		angle3 = math.radians(270)
		arc3 = Arc(radius=2,angle=angle3).set_color(YELLOW)
		self.play(ShowCreation(arc3))
		four = Tex("$270^{\\circ}\\text{ or }\\frac{3\\pi}{2}$").set_color(YELLOW)
		four.shift(DOWN*2.5)
		self.play(Write(four))

		self.wait()
		angle4 = math.radians(360)
		arc4 = Arc(radius=2,angle=angle4).set_color(PURPLE)
		self.play(ShowCreation(arc4))
		five = Tex("$360^{\\circ} \\text{ or } 2\\pi$").set_color(PURPLE)
		five.shift(RIGHT*4)
		self.play(Write(five))
		self.wait(4)

		self.remove(zero,two,three,four,five)
		self.remove(dot,arc1,arc2,arc3,arc4)
		R2D = Text("Converting from radians to degrees").set_color(GREEN)
		self.play(FadeIn(R2D))
		self.wait()
		self.play(FadeOut(R2D))
		
		R2Drule = Tex("Multiply the radian value by $\\frac{180}{\\pi}$").set_color(GREEN)
		R2Drule.shift(UP*2)
		self.play(Write(R2Drule)) 
		ex = Text("Example:").scale(.5)
		ex.shift(LEFT*3)
		self.play(Write(ex))
		R2Dmath = Tex("$\\frac{3\\pi}{4} \\text{ radians} * \\frac{180^{\\circ}}{\\pi\\text{ radians}} = 135^{\\circ}$")
		R2Dmath.shift(DOWN*1.5)
		self.play(Write(R2Dmath))
		self.wait(2)


		self.remove(R2Drule,ex,R2Dmath)
		self.wait()
		D2R = Text("Converting from degrees to radians").set_color(ORANGE)
		self.play(FadeIn(D2R))
		self.wait()
		self.remove(D2R)

		D2Rrule = Tex("Multiply the degree value by $\\frac{\\pi}{180}$").set_color(ORANGE)
		D2Rrule.shift(UP*2)
		self.play(Write(D2Rrule))
		ex2 = Text("Example:").scale(.5)
		ex2.shift(LEFT*3)
		self.play(Write(ex2))
		D2Rmath = Tex("$45^{\\circ} * \\frac{\\pi\\text{ radians}}{180^{\\circ}} = \\frac{\\pi}{4}\\text{ radians}$")
		D2Rmath.shift(DOWN*1.5)
		self.play(Write(D2Rmath))
		self.wait(2)



		self.remove(D2Rrule,ex2,D2Rmath)

		self.remove(triangle_logo)
		self.remove(circle_logo)
		self.remove(square)

		self.wait()
		end_sienacollege = Text("Siena College").set_color(GREEN_E).scale(1.5)
		end_circle = Circle(fill_opacity=5).set_color(YELLOW_E).set_fill().scale(3)
		self.play(GrowFromCenter(end_circle))
		self.play(GrowFromCenter(end_sienacollege))
		self.wait(2)
