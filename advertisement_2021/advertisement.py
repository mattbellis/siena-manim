from manim import *
import numpy as np
#from manimlib.imports import *

class MyAnimation(Scene):
    def construct(self):
        text = Text("Would you like to learn how to do this?", font="Consolas", font_size=36)
        difference = Text(
            """
            Do you think this is interesting?\n
            Do you think this could help Siena College students?\n
            """,
            font="Arial", font_size=24,
            t2c={"Siena": YELLOW, "College": GREEN}
        )


        to_isolate = ["x_0", "v_0", "=", "a"]
        tex1 = MathTex("{x{{(t)}} = {{x_0}} + {{v_0}}{{t}} + \\frac{1}{2}a{{t^2}}}")
        tex2 = MathTex("{v^2 - {{v_0}}^2 = 2{{a}}({{x}} - {{x_0}})}",isolate=to_isolate)
        
        lines = VGroup(tex1,tex2)
        lines.arrange(DOWN, buff=1)

        for line in lines:
            line.set_color_by_tex_to_color_map({
                "t": RED,
                "v_0": TEAL,
                "x_0": YELLOW,
                })


        VGroup(text,tex1,difference).arrange(DOWN, buff=1)

        self.play(Write(text))
        self.wait(1)
        '''
        self.play(FadeIn(tex1, UP))
        self.wait(1)
        self.play(FadeIn(difference, UP))
        self.wait(3)
        #self.wait(1)

        self.play(FadeOut(text), FadeOut(difference, shift=DOWN), FadeOut(tex1, shift=LEFT))

        # Animate the other part again
        self.add(lines[0])
        self.wait(2)

        self.play(
            TransformMatchingTex(
                lines[0].copy(), lines[1],
                path_arc=90 * DEGREES,
            ),
            run_time=4
        )
        self.wait(3)

        self.play(FadeOut(tex1),FadeOut(tex2))
        ##########

        axes = Axes((-3, 10), (-1, 8))
        axes.add_coordinate_labels()
        self.play(Write(axes, lag_ratio=0.01, run_time=1))

        START = (-6,0,0)
        END =   (4,0,0)
        line1 = Line(START,END,color=BLUE);
        self.play(ShowCreation(line1))
        line2 = Line(END,(4,3,0),color=BLUE);
        self.play(ShowCreation(line2))
        line3 = Line((4,3,0),START,color=BLUE);
        self.play(ShowCreation(line3))
        self.wait(3)
        self.play(FadeOut(line1),FadeOut(line2),FadeOut(line3),FadeOut(axes))

        text2 = Text("I'm still learning this!\n\nBut it seems pretty cool!", font="Consolas", font_size=36)
        text3 = Text("Let's work on it together!", font="Consolas", font_size=36)

        VGroup(text2,text3).arrange(DOWN, buff=2)
        self.play(Write(text2))
        self.wait(1)
        self.play(FadeIn(text3, UP))
        self.wait(3)
        '''
