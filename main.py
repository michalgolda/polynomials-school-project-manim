from manim import *


BLACK_COLOR = "#16191F"
GOLD_COLOR = "#FFB703"
WHITE_COLOR = "#FFF"

config["background_color"] = BLACK_COLOR


class NDegreeMonomialScene(Scene):
	def construct(self):
		what_does_it_mean_text = Tex(
			"Co to jest wielomian ?"
		)
		what_does_it_mean_text.scale(2)
		what_does_it_mean_text.set_color(GOLD_COLOR)

		self.play(Write(what_does_it_mean_text))
		self.wait(1)

		self.play(Unwrite(what_does_it_mean_text))

		formula = VGroup(
			MathTex(r"a", r"\cdot", r"x^", r"{n}"),
			MathTex(r"a \in R", r"a \neq 0", r"n \in N+")
		)
		formula.arrange(DOWN, buff=1.5, center=True)

		formula[0].scale(2)

		self.play(Write(formula[0]))
		self.wait(2)

		formula[1].set_color(GOLD_COLOR)
		formula[1].arrange(RIGHT, buff=1)

		coefficient_framebox = SurroundingRectangle(formula[0][0], buff=0.2)
		coefficient_framebox.set_color(GOLD_COLOR)

		self.play(Create(coefficient_framebox))
		self.wait()

		self.play(Write(formula[1][0]))
		self.wait()

		self.play(Write(formula[1][1]))
		self.wait()

		exponent_framebox = SurroundingRectangle(formula[0][3], buff=0.2)
		exponent_framebox.set_color(GOLD_COLOR)

		self.play(
			ReplacementTransform(
				coefficient_framebox,
				exponent_framebox
			)
		)
		self.wait()

		self.play(Write(formula[1][2]))
		self.wait()

		self.play(Uncreate(exponent_framebox))
		self.wait()

		self.play(ScaleInPlace(formula, 0.8))
		self.wait()

		formula.generate_target()
		formula.target.shift(2*UP)

		self.play(MoveToTarget(formula))
		self.wait()

		examples = VGroup(
			MathTex(r"\frac{1}{2}", r"x", r"^{2}"),
			MathTex(r"3", r"x", r"^{5}"),
			MathTex(r"6", r"x", r"^{1}"),
			MathTex(r"100", r"x", r"^{3}")
		)
		examples.scale(1.5)
		examples.arrange(RIGHT, buff=1.5)

		for example in examples:
			self.play(FadeToColor(example[0], GOLD_COLOR))
			self.play(FadeToColor(example[2], GOLD_COLOR))

			self.play(Create(example))
			self.wait()