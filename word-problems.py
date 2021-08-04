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



		wordprob = Text("Equation Explainers").set_color(BLUE)
		self.play(Write(wordprob),run_time=7)
		self.wait()
		self.play(FadeOut(wordprob))
		self.wait()		
		prob1 = Text("If you want to know your position,").scale(.7).set_color(BLUE)
		prob2 = Text("after some time has passed,").scale(.7).set_color(YELLOW)
		prob3 = Text("you take your starting position,").scale(.7).set_color(RED)
		prob4 = Text(" add it to your starting velocity").scale(.7).set_color(GREEN)
		prob5 = Text(" multiplied by the time that has passed,").scale(.7).set_color(PURPLE)
		prob6 = Text("then add one-half").scale(.7).set_color(ORANGE)
		prob7 = Text(" the acceleration ").scale(.7).set_color(PINK)
		prob8 = Text("multiplied by the time that has passed squared.").scale(.7).set_color(BLUE)
		math1 = MathTex("X","(t)","=","X_{0}","+","V_{0}","t","+",".5","a","t^2").next_to(prob1,DOWN*4)
		self.play(Write(prob1))
		math1[0].set_color(BLUE)
#		math1[1].set_color(YELLOW)
#		math1[2].set_color(RED)
#		math1[3].set_color(GREEN)
		self.play(Write(math1[0]) 
		self.wait()
#		self.play(Write(prob2))
#		self.play(Write(math1[1])
#		self.play(Write(prob3))
#		self.play(Write(math1[2])
#		self.wait()