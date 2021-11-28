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

		
		Title= Text("Selecting A Kinematic Formula").set_color(BLUE)
		self.play(GrowFromCenter(Title))
		self.wait(3)
		self.play(FadeOut(Title))

		prob1 = Tex("Example Problem").scale(.7)
		prob1.to_corner(UL)
		self.play(Write(prob1))
		words1 = Text("A race car starting from rest accelerates uniformly at a rate of\n4.9 meters per second squared. What is the cars speed after\nit has travelled 200 meters?").scale(.6)
		words1.next_to(prob1,DOWN+RIGHT*1.5)
		self.play(Write(words1,run_time=6))
		self.wait(2)
		self.remove(prob1,words1)
		step1 = Text("Step 1: Identify givens").set_color(BLUE)
		self.play(Write(step1))
		self.wait()
		self.remove(step1)
		self.add(prob1,words1)

		#Step 1:Givens
		self.wait()
		givens1= Tex("Givens:").scale(.8)
		givens1.next_to(prob1,DOWN*8)
		self.play(FadeIn(givens1))
		self.wait()
		words1[8:24].set_color(RED)
		self.wait()
		vi1= Tex("$v_{i} = 0$").scale(.8).set_color(RED)
		vi1.next_to(givens1,DOWN)
		self.play(FadeIn(vi1))
		self.wait()

		words1[24:78].set_color(BLUE)
		self.wait()
		a1 = Tex("$a = 4.9 \\frac{m}{s^2}$").scale(.8).set_color(BLUE).next_to(vi1,DOWN)
		self.play(FadeIn(a1))
		self.wait()

		words1[107:125].set_color(PINK)
		self.wait()
		d1 = Tex("$d = 200 m$").next_to(a1,DOWN).set_color(PINK).scale(.8)
		self.play(FadeIn(d1))
		self.wait()


		#Step 2: Unknowns
		self.remove(prob1,words1,givens1,vi1,a1,d1)
		step2 = Tex("Step 2: Identify unknowns").set_color(BLUE)
		tip = Tex("What are you trying to find?")
		self.play(Write(step2))
		tip.shift(DOWN)
		self.play(Write(tip))
		self.wait(2)

		self.remove(step2,tip)
		self.add(prob1,words1,givens1,vi1,a1,d1)
		unknown = Tex("Unknown:").scale(.8).next_to(d1,DOWN*1.2)
		self.play(FadeIn(unknown))
		self.wait()
		words1[78:97].set_color(GREEN)
		self.wait()
		vf1 = Tex("$v_{f} = ?$").next_to(unknown,DOWN).set_color(GREEN)
		self.play(FadeIn(vf1))
		self.wait(2)

		#Step 3: Select the right equation
		self.remove(prob1,words1,givens1,vi1,a1,d1,unknown,vf1)
		step3 = Tex("Step 3: Select the best equation").set_color(BLUE)
		self.play(Write(step3))
		tip2 = Text("This will be the equation that contains\nonly your givens and the unknown").next_to(step3,DOWN).scale(.7)
		self.play(Write(tip2))
		self.wait(2)

		self.remove(step3,tip2)
		self.add(prob1,words1,givens1,vi1,a1,d1,unknown,vf1)
		options = Tex("Equations:").next_to(givens1,RIGHT*3).scale(.8)
		eq1 = MathTex("v_{f}"," ="," v_{i}"," +"," a"," t").scale(.8).next_to(options,DOWN)
		eq2 = MathTex("d"," ="," v_{i}"," t"," +"," \\frac{1}{2}"," a"," t^{2}").scale(.8).next_to(eq1,DOWN)
		eq3 = MathTex("v_{f}^{2}"," ="," v_{i}^{2}"," +"," 2"," a"," d").scale(.8).next_to(eq2,DOWN)
		self.play(FadeIn(options))
		self.add(eq1,eq2,eq3)
		self.wait()

		#Selecting Equations
		framebox1 = SurroundingRectangle(vi1,buff=.1).set_color(RED)
		self.play(Create(framebox1))
		self.wait()
		eq1[2].set_color(RED)
		self.wait()
		eq2[2].set_color(RED)
		self.wait()
		eq3[2].set_color(RED)
		self.wait(2)
		framebox2 = SurroundingRectangle(a1,buff=.1).set_color(BLUE)		
		self.play(Create(framebox2))
		self.wait()
		eq1[4].set_color(BLUE)
		self.wait()
		eq2[6].set_color(BLUE)
		self.wait()
		eq3[5].set_color(BLUE)
		self.wait(2)
		framebox3 = SurroundingRectangle(d1,buff=.1).set_color(PINK)
		self.play(Create(framebox3))
		self.wait()
		eq2[0].set_color(PINK)
		self.wait()
		eq3[6].set_color(PINK)
		self.wait(2)
		framebox4 = SurroundingRectangle(vf1,buff=.1).set_color(GREEN)		
		self.play(Create(framebox4))
		self.wait()
		eq1[0].set_color(GREEN)
		self.wait()
		eq3[0].set_color(GREEN)
		self.wait(2)
		
		framebox5 = SurroundingRectangle(eq3,buff=.1)
		self.play(Create(framebox5))
		self.wait(2)
		eq3.scale(1.5)
		framebox5.scale(1.5)
		eq3.move_to(UP+RIGHT*3)
		framebox5.move_to(UP+RIGHT*3)
		self.wait()
		last = Text("This is the best equation to use because it only\ncontains given variables and the unknown.\nThe other two equations include time which we\ndo not know.").scale(.5).set_color(YELLOW)
		last.next_to(eq3,DOWN*2)
		self.play(Write(last,run_time=4))
		self.wait(2)
		self.remove(last,prob1,words1,givens1,vi1,a1,d1,unknown,vf1,framebox1,framebox2,framebox3,framebox4,framebox5,eq1,eq2,eq3,options)

		#step 4: plug in and solve
		step4 = Text("Now all you have to do is plug your givens\ninto the equation and solve for the unknown!!").set_color(BLUE)
		self.play(Write(step4))
		self.wait(2)
		self.remove(step4)
		self.wait()		


		self.remove(triangle_logo)
		self.remove(circle_logo)
		self.remove(square)

		self.wait()
		end_sienacollege = Text("Siena College").set_color(GREEN_E).scale(1.5)
		end_circle = Circle(fill_opacity=5).set_color(YELLOW_E).set_fill().scale(3)
		self.play(GrowFromCenter(end_circle))
		self.play(GrowFromCenter(end_sienacollege))
		self.wait(2)
