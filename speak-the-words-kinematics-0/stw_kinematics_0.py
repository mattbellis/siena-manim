from manim import *

class stw_kinematics_0(Scene):
	def construct(self):
		title = Tex(r"Kinematics")

		explanation0 = Tex(r"If you want to know your position, after some time has passed, ",color=BLUE)
		explanation1 = Tex(r"you take your starting position, ")
		explanation2 = Tex(r"add to it your starting velocity multiplied by the time that has passed, ")
		explanation3 = Tex(r"then add one-half the acceleration multiplied by the time that has passed squared.")

		VGroup(title, explanation0, explanation1,explanation2,explanation3   ).arrange(DOWN)
		self.play(
			Write(title),
			FadeInFrom(explanation0, UP),
			FadeInFrom(explanation1, UP),
			FadeInFrom(explanation2, UP),
			FadeInFrom(explanation3, UP),
		)
		self.wait()

