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
		self.play(Write(wordprob),run_time=5)
		self.wait()
		self.play(FadeOut(wordprob))
		self.wait()		
		prob1 = Text("If you want to know your position, after some time has\npassed, you take your starting position, add it to your\nstarting velocity multiplied by the time that has passed,\nthen add one-half the acceleration multiplied by the\ntime that has passed squared.").scale(.7)
		math1 = MathTex("X","(t)","=","X_{0}","+","V_{0}","t","+",".5","a","t^2").next_to(prob1,DOWN*4).scale(2)
		prob1[0:28].set_color(BLUE)
		prob1[28:51].set_color(YELLOW)
		prob1[51:79].set_color(RED)
		prob1[79:106].set_color(GREEN)
		prob1[106:139].set_color(PURPLE)
		prob1[139:154].set_color(ORANGE)
		prob1[154:169].set_color(PINK)
		prob1[169:210].set_color(BLUE)
		self.play(Write(prob1[0:28]))
		math1[0].set_color(BLUE)
		math1[1].set_color(YELLOW)
		math1[3].set_color(RED)
		math1[5].set_color(GREEN)
		math1[6].set_color(PURPLE)
		math1[8].set_color(ORANGE)
		math1[9].set_color(PINK)
		math1[10].set_color(BLUE)
		self.play(Write(math1[0])) 
		self.wait()
		self.play(Write(prob1[28:51]))
		self.play(Write(math1[1]))
		self.wait()
		self.play(Write(math1[2]))
		self.play(Write(prob1[51:79]))
		self.play(Write(math1[3]))
		self.wait()
		self.play(Write(math1[4]))
		self.play(Write(prob1[79:106]))
		self.play(Write(math1[5]))
		self.wait()
		self.play(Write(prob1[106:139]))
		self.play(Write(math1[6]))
		self.wait()
		self.play(Write(math1[7]))
		self.play(Write(prob1[139:154]))
		self.play(Write(math1[8]))
		self.wait()
		self.play(Write(prob1[154:169]))
		self.play(Write(math1[9]))
		self.wait()
		self.play(Write(prob1[169:210]))
		self.play(Write(math1[10]))
		self.wait()
