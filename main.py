from manim import *


BLACK_COLOR = "#16191F"
GOLD_COLOR = "#FFB703"
WHITE_COLOR = "#FFF"

config["background_color"] = BLACK_COLOR


class NDegreeMonomialScene(Scene):
	def construct(self):
		title = Tex(
			"Jednomiany n-tego stopnia"
		)
		title.scale(2)
		title.set_color(GOLD_COLOR)

		self.play(Write(title))
		self.wait(1)

		self.play(Unwrite(title))

		formula = VGroup(
			MathTex(r"a", r"\cdot", r"x^", r"{n}"),
			MathTex(r"a \in R", r"a \neq 0", r"n \in N_{+}")
		)
		formula.arrange(DOWN, buff=1.5, center=True)

		formula[0].scale(2)

		self.play(Write(formula[0]))
		self.wait(5)

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
			example[0].set_color(GOLD_COLOR)
			example[2].set_color(GOLD_COLOR)

			self.play(Create(example))
			self.wait()


class NDegreePolynomialScene(MovingCameraScene):
	def construct(self):
		title = Tex("Wielomiany n-tego stopnia")
		title.scale(2)
		title.set_color(GOLD_COLOR)

		self.play(Write(title))
		self.wait(1)

		self.play(Unwrite(title))

		formula = MathTex(
			r"a_{n} \cdot x^{n}", r"+", r"a_{n-1} \cdot x^{n-1}",
			r"+", r"a_{n-2} \cdot x^{n-2}", r"+ ... +",
			r"a_{2} \cdot x^{2}", r"+", r"a_{1} \cdot x", r"+", r"a_{0}"
		)

		self.play(Create(formula))
		self.wait(7)

		monomial = formula[0]
		monomial_framebox = SurroundingRectangle(monomial)
		monomial_framebox.set_color(GOLD_COLOR)

		self.play(Create(monomial_framebox))

		self.camera.frame.save_state()

		self.play(self.camera.frame.animate.scale(0.5).move_to(monomial))

		for i in range(2, 12, 2):
			next_monomial = formula[i]
			next_framebox_monomial = SurroundingRectangle(next_monomial)
			next_framebox_monomial.set_color(GOLD_COLOR)

			self.play(
				ReplacementTransform(
					monomial_framebox,
					next_framebox_monomial
				),
				self.camera.frame.animate.move_to(next_monomial)
			)

			monomial_framebox = next_framebox_monomial

		self.play(Uncreate(monomial_framebox))
		self.play(Restore(self.camera.frame))
		self.wait()

		self.play(Uncreate(formula))
		self.wait(3)

		marks = MathTex(r"W(x)", r"P(x)", r"Q(x)")
		marks.arrange(RIGHT, buff=1.5)
		marks.scale(1.5)

		for mark in marks:
			self.play(Write(mark))
			self.wait()

		marks.generate_target()
		marks.target.shift(2*UP)

		self.play(MoveToTarget(marks))

		example = MathTex(
			r"W(x)=-12x^{2}-8-5x^6+2x^{3}",
			r"P(x)=4x^{4}+2x^{3}-x^{2} + 2",
			r"Q(x)=2x^{10}-3x^{5}+2x^{2} + \frac{1}{2}"
		)
		example.arrange(DOWN)
		example.shift(DOWN)
		example.set_color(GOLD_COLOR)
		example.scale(1.5)

		self.play(Create(example))
		self.wait()


class PolynomialFactoringWaysScene(Scene):
	def construct(self):
		title = Tex("Rozk??ad wielomianu na czynniki")
		title.scale(1.7)
		title.set_color(GOLD_COLOR)

		self.play(Write(title))
		self.wait(1)

		self.play(Unwrite(title))

		title = Tex("Sposoby rozk??adu wielomianu na czynniki")
		title.scale(1.25)
		title.set_color(GOLD_COLOR)
		title.generate_target()
		title.target.shift(3*UP)

		self.play(Write(title))
		self.wait()

		self.play(MoveToTarget(title))
		self.wait()

		factoring_ways = VGroup(
			Tex("- wyci??gni??cie wsp??lnego czynnika przed nawias,"),
			Tex("- wzory skr??conego mno??enia,"),
			Tex("- delta,"),
			Tex("- grupowanie wyraz??w.")
		)
		factoring_ways.arrange(DOWN, buff=0.5, aligned_edge=LEFT)

		for way in factoring_ways:
			self.play(Write(way))
			self.wait()


class ExamplePolynomialFactoringScene(Scene):
	def construct(self):
		formula = VGroup(
			MathTex(
				r"P(x)=", r"(x^{2} + 2x + 1)", r"(3x^{2} + 2x - 1)"
			),
			MathTex(
				r"P(x)=", r"(x + 1)^{2}", r"(3x^{2} + 2x - 1)"
			),
			MathTex(
				r"x = -2 \pm \sqrt{4 - 4 \cdot 3 \cdot (-1)}",
				r"x = -1 \vee x = \frac{1}{3}"
			),
			MathTex(
				r"P(x)=", r"(x + 1)^{2}", r"(x + 1)(x - \frac{1}{3})"
			)
		)
		formula.scale(1)
		formula.arrange(DOWN)
		formula.shift(UP)

		formula[0][1].set_color(GOLD_COLOR)

		self.play(Create(formula[0]))
		self.wait()

		formula[1][1].set_color(GOLD_COLOR)

		self.play(Create(formula[1]))
		self.wait()

		self.play(ApplyMethod(formula[0][1].set_color, WHITE_COLOR))
		self.wait()

		self.play(ApplyMethod(formula[1][1].set_color, WHITE_COLOR))
		self.wait()

		self.play(ApplyMethod(formula[1][2].set_color, GOLD_COLOR))
		self.wait()

		formula[2].set_color(GOLD_COLOR)
		formula[2].scale(0.75)
		formula[2].arrange(DOWN)

		self.play(Create(formula[2]))
		self.wait()

		formula[3].shift(DOWN)
		formula[3][2].set_color(GOLD_COLOR)

		self.play(Create(formula[3]))
		self.wait(4)

		self.play(Uncreate(formula))

		factored_polynomial = MathTex(r"P(x)=", r"(x + 1)^{2}", r"(x + 1)(x - \frac{1}{3})")
		factored_polynomial.set_color(GOLD_COLOR)

		self.play(Create(factored_polynomial))
		self.wait()


class FirstExerciseScene(Scene):
	def construct(self):
		exercise_number = Tex("Zadanie 1")
		exercise_number.scale(1)
		exercise_number.set_color(GOLD_COLOR)
	
		exercise_description = VGroup(
			Tex("Rowi???? r??wnanie"),
			MathTex(r"(x^{3} - 8)(x - 5)(2x + 1) = 0")
		)
		exercise_description.arrange(RIGHT, buff=0.25)
		exercise_description.scale(0.85)

		text_group = VGroup(
			exercise_number,
			exercise_description
		)
		text_group.arrange(DOWN, buff=0.25, aligned_edge=LEFT)

		self.play(Write(text_group))
		self.wait()

		text_group.generate_target()
		text_group.target.shift(3*UP)
		text_group.target.shift(2*LEFT)

		self.play(MoveToTarget(text_group))
		self.wait(2)


class SecondExerciseScene(Scene):
	def construct(self):
		exercise_number = Tex("Zadanie 2")
		exercise_number.scale(1)
		exercise_number.set_color(GOLD_COLOR)
	
		exercise_description = VGroup(
			Tex("Sprawd??, czy podane wielomiany W(x) i F(x) s?? r??wne."),
			MathTex(
				r"W(X) = (2x - 1)^{2}(x + 3)", 
				r"F(x) = 4x^{3} + 12x^{2} + x + 3"
			).arrange(RIGHT, buff=0.5)
		)
		exercise_description.arrange(DOWN, buff=0.25)
		exercise_description.scale(0.85)

		text_group = VGroup(
			exercise_number,
			exercise_description
		)
		text_group.arrange(DOWN, buff=0.25, aligned_edge=LEFT)

		self.play(Write(text_group))
		self.wait()

		text_group.generate_target()
		text_group.target.shift(2.5*UP)
		text_group.target.shift(1.2*LEFT)

		self.play(MoveToTarget(text_group))
		self.wait(2)