from manim import *

class SienaIntro(Scene):
	CONFIG = {"camera_config":{"background_color": BLACK}}

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
		self.wait(1)
