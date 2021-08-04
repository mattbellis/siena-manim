from manim import *

class SienaIntro(Scene):
	arguments = {"camera_config":{"background_color": GREY}}

	def construct(self):
		circle_logo = Circle(fill_opacity=5).scale(3)
		circle_logo.set_fill()
		circle_logo.set_color(GREEN_E)
		text1 = Text('Siena College')
		text1.set_color(YELLOW_E)
		text1.next_to(circle_logo,0,buff=0).scale(1.5)
		text2 = Text('Dept of Physics')
		text2.next_to(text1,DOWN,buff=0).scale(1)
		self.play(DrawBorderThenFill(circle_logo, run_time=5), Write(text1, run_time=3), Write(text2,run_time=4))
		self.wait(.2)
				
		text1.scale(0.2)
		text2.scale(0.2)
		circle_logo2=circle_logo.scale(0.2)
		circle_logo2.to_corner(DR)
		text3=text1.next_to(circle_logo,0,buff=0)
		text4=text2.next_to(text3,DOWN,buff=0)

		self.play(Write(circle_logo2),Write(text3),Write(text4))
		self.wait()


#class MovingBox(Scene):
		
#	def construct(self):
		title = Text("Grouping Like Terms",color = PURPLE).scale(1.4)
		self.add(title)
		self.wait()
		self.play(FadeOut(title))
		text = MathTex("0=","x","+5","+2x").scale(2)
		self.play(Write(text))
		step1 = Text("Step 1 : Box all matching terms").to_corner(DL).scale(.6)
		step1.shift(LEFT*2)
		self.add(step1)
		self.wait()
		framebox1 = SurroundingRectangle(text[1],buff=.1).set_color(YELLOW)
		framebox2 = SurroundingRectangle(text[3],buff=.1).set_color(YELLOW)
		framebox3 = SurroundingRectangle(text[2],buff=.1).set_color(PURPLE)
		self.play(Create(framebox1))
		self.wait()
		self.play(Create(framebox2))
		self.wait()
		self.play(Create(framebox3))
		self.wait()

		step2 = Text("Step 2 : Rewrite equation so matching terms are next to each other").to_corner(DL).scale(.6)
		step1.shift(UP)
		step2.align_to(step1, LEFT)
		self.add(step2)
		self.wait()
		text.shift(UP).scale(.5)
		framebox1.next_to(text[1],0,buff=0).scale(0.5)
		framebox2.next_to(text[3],0,buff=0).scale(.5)
		framebox3.next_to(text[2],0,buff=0).scale(.5)
		text2 = MathTex("0=","x+2x","+5").scale(2)
		self.play(Write(text2))
		self.wait()
		framebox4 = SurroundingRectangle(text2[1],buff=.1).set_color(YELLOW)
		framebox5 = SurroundingRectangle(text2[2],buff=.1).set_color(PURPLE)
		self.play(Create(framebox4))
		self.wait()
		self.play(Create(framebox5))
		self.wait()
		
		step3 = Text("Step 3 : Combine all matching terms").to_corner(DL).scale(.6)
		step1.shift(UP)
		step2.shift(UP)
		step3.align_to(step2, LEFT)
		self.add(step3)
		self.wait()
		text.shift(UP)
		framebox1.shift(UP)
		framebox2.shift(UP)
		framebox3.shift(UP)
		text2.shift(UP).scale(.5)
		framebox4.next_to(text2[1],0,buff=0).scale(.5)
		framebox5.next_to(text2[2],0,buff=0).scale(.5)
		self.wait()
		text3 = MathTex("0=","3x","+5").scale(2)
		framebox6 = SurroundingRectangle(text3[1],buff=.1).set_color(YELLOW)
		framebox7 = SurroundingRectangle(text3[2],buff=.1).set_color(PURPLE)
		self.play(Write(text3))
		self.wait()
		self.play(Write(framebox6))
		self.wait()
		self.play(Write(framebox7))
		self.wait(1)

		self.play(FadeOut(text,shift=UP), FadeOut(text2,shift=UP),FadeOut(text3,shift=UP), FadeOut(framebox1,shift=UP),FadeOut(framebox2,shift=UP), FadeOut(framebox3,shift=UP),FadeOut(framebox4,shift=UP),FadeOut(framebox5,shift=UP), FadeOut(framebox6,shift=UP),FadeOut(framebox7,shift=UP))
		self.play(FadeOut(step1),FadeOut(step2),FadeOut(step3))
		self.wait()
		hints= Text("Helpful Hints",color=PURPLE).scale(1.4)
		self.play(Write(hints))
		self.wait()
		self.play(FadeOut(hints))
		self.wait()
		hint1 = Text("The variable and the power it's raised to\nare the only things that matter!")
		self.play(Write(hint1))
		self.wait(1)
		self.play(FadeOut(hint1),run_time=4)
		hint2 = Text("Always box the sign that's infront of a\nnumber or variable with it!")
		self.wait()
		self.play(Write(hint2))
		self.wait(1)
		self.play(FadeOut(hint2),run_time=4)
		self.wait()
		hint3 = Text("Only add or subtract the coefficients!\nVariables just tag along.")
		self.play(Write(hint3))
		self.wait(1)
		self.play(FadeOut(hint3),run_time=4)
		self.wait()
		hint4 = Text("Any lone variable has a one infront!")
		self.play(Write(hint4))
		self.play(FadeOut(hint4),run_time=4)
		self.wait(1)

