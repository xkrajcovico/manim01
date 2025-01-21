from manimlib import *

#tutorial from here
#https://3b1b.github.io/manim/getting_started/example_scenes.html
#manimgl start.py SquareToCircle

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(BLUE, opacity=0.5)
        circle.set_stroke(BLUE_E, width=4)
        square = Square()
        self.play(ShowCreation(square))
        self.wait()
        self.play(ReplacementTransform(square, circle))
        self.add(circle)
        self.wait()
        text = Text("Here is a text", font="Consolas", font_size=90)
        difference = Text(
            """
            Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
            """,
            font="Arial", font_size=24,
            # t2c is a dict that you can choose color for different text
            t2c={"Text": BLUE, "TexText": BLUE, "LaTeX": ORANGE}
        )
        VGroup(text, difference).arrange(DOWN, buff=1)
        self.play(Write(text))
        self.play(FadeIn(difference, UP))
        self.wait(3)

        fonts = Text(
            "Nunc viverra imperdiet enim. Fusce est. Vivamus a tellus.",
            font="Arial",
            t2f={"font": "Consolas", "words": "Consolas"},
            t2c={"font": BLUE, "words": GREEN}
        )
        fonts.set_width(FRAME_WIDTH - 1)
        slant = Text(
            "Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. ",
            font="Consolas",
            t2s={"slant": ITALIC},
            t2w={"weight": BOLD},
            t2c={"slant": ORANGE, "weight": RED}
        )
        VGroup(fonts, slant).arrange(DOWN, buff=0.8)
        self.play(FadeOut(text), FadeOut(difference, shift=DOWN))
        self.play(Write(fonts))
        self.wait()
        self.play(Write(slant))
        self.wait()
