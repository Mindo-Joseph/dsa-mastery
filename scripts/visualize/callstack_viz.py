#!/usr/bin/env python3
"""
Callstack Visualization using Manim

Generates beautiful animations showing:
- Function call stack
- Variable states
- Array/data structure changes
- Algorithm execution flow

Usage:
    manim callstack_viz.py TwoPointersScene -pql
"""

from manim import *
import json
from pathlib import Path


class CallStackFrame(VGroup):
    """Visual representation of a single stack frame"""

    def __init__(self, function_name, variables, **kwargs):
        super().__init__(**kwargs)

        # Frame border
        self.frame = Rectangle(
            width=4,
            height=1 + 0.3 * len(variables),
            color=BLUE,
            fill_opacity=0.1
        )

        # Function name
        self.func_name = Text(
            function_name,
            font_size=20,
            weight=BOLD
        ).next_to(self.frame.get_top(), DOWN, buff=0.1)

        # Variables
        self.var_texts = VGroup()
        for i, (name, value) in enumerate(variables.items()):
            var_text = Text(
                f"{name}: {value}",
                font_size=16,
                color=GREEN
            ).next_to(
                self.func_name.get_bottom() if i == 0 else self.var_texts[-1].get_bottom(),
                DOWN,
                buff=0.1,
                aligned_edge=LEFT
            )
            self.var_texts.add(var_text)

        self.add(self.frame, self.func_name, self.var_texts)


class ArrayVisualization(VGroup):
    """Visual representation of an array with pointers"""

    def __init__(self, array, pointers=None, **kwargs):
        super().__init__(**kwargs)

        self.array = array
        self.boxes = VGroup()
        self.values = VGroup()

        # Create array boxes
        for i, val in enumerate(array):
            box = Square(side_length=0.8, color=WHITE)
            if i > 0:
                box.next_to(self.boxes[-1], RIGHT, buff=0)

            value_text = Text(str(val), font_size=24)
            value_text.move_to(box.get_center())

            index_text = Text(str(i), font_size=16, color=GRAY)
            index_text.next_to(box, DOWN, buff=0.1)

            self.boxes.add(box)
            self.values.add(value_text)
            self.add(box, value_text, index_text)

        # Add pointers
        self.pointer_arrows = {}
        self.pointer_labels = {}

        if pointers:
            for name, index in pointers.items():
                self.add_pointer(name, index)

    def add_pointer(self, name, index, color=YELLOW):
        """Add a pointer arrow above array element"""
        arrow = Arrow(
            start=self.boxes[index].get_top() + UP * 0.5,
            end=self.boxes[index].get_top(),
            color=color,
            buff=0.1
        )
        label = Text(name, font_size=16, color=color)
        label.next_to(arrow, UP, buff=0.1)

        self.pointer_arrows[name] = arrow
        self.pointer_labels[name] = label

        self.add(arrow, label)
        return arrow, label

    def move_pointer(self, name, new_index):
        """Animate pointer movement"""
        arrow = self.pointer_arrows[name]
        label = self.pointer_labels[name]

        new_arrow = Arrow(
            start=self.boxes[new_index].get_top() + UP * 0.5,
            end=self.boxes[new_index].get_top(),
            color=arrow.get_color(),
            buff=0.1
        )

        return AnimationGroup(
            Transform(arrow, new_arrow),
            label.animate.move_to(new_arrow.get_top() + UP * 0.3)
        )


class TwoPointersScene(Scene):
    """
    Example visualization for Two Pointers pattern
    Demonstrates Two Sum II problem
    """

    def construct(self):
        # Title
        title = Text("Two Pointers - Two Sum II", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait()

        # Problem statement
        problem = Text(
            "Find two numbers that sum to target = 9",
            font_size=20,
            color=GRAY
        )
        problem.next_to(title, DOWN)
        self.play(FadeIn(problem))
        self.wait()

        # Array
        array = [2, 7, 11, 15]
        target = 9

        arr_viz = ArrayVisualization(
            array,
            pointers={"left": 0, "right": 3}
        )
        arr_viz.shift(UP * 1)

        self.play(Create(arr_viz))
        self.wait()

        # Callstack
        stack_title = Text("Call Stack", font_size=24).to_edge(LEFT).shift(DOWN * 0.5)
        self.play(Write(stack_title))

        # Initial stack frame
        frame1 = CallStackFrame(
            "two_sum()",
            {"left": 0, "right": 3}
        )
        frame1.next_to(stack_title, DOWN, aligned_edge=LEFT)
        self.play(FadeIn(frame1))
        self.wait()

        # Iteration 1
        sum_text = Text(
            "sum = 2 + 15 = 17 > 9",
            font_size=20,
            color=RED
        ).next_to(arr_viz, DOWN, buff=0.5)

        self.play(Write(sum_text))
        self.wait()

        # Update frame
        frame2 = CallStackFrame(
            "two_sum()",
            {"left": 0, "right": 3, "sum": 17}
        )
        frame2.move_to(frame1.get_center())

        self.play(Transform(frame1, frame2))
        self.wait()

        # Move right pointer
        action1 = Text(
            "sum > target → right--",
            font_size=18,
            color=YELLOW
        ).next_to(sum_text, DOWN)

        self.play(Write(action1))
        self.play(arr_viz.move_pointer("right", 2))
        self.play(FadeOut(sum_text), FadeOut(action1))
        self.wait()

        # Iteration 2
        sum_text2 = Text(
            "sum = 2 + 11 = 13 > 9",
            font_size=20,
            color=RED
        ).next_to(arr_viz, DOWN, buff=0.5)

        self.play(Write(sum_text2))

        frame3 = CallStackFrame(
            "two_sum()",
            {"left": 0, "right": 2, "sum": 13}
        )
        frame3.move_to(frame1.get_center())
        self.play(Transform(frame1, frame3))
        self.wait()

        # Move right pointer again
        action2 = Text(
            "sum > target → right--",
            font_size=18,
            color=YELLOW
        ).next_to(sum_text2, DOWN)

        self.play(Write(action2))
        self.play(arr_viz.move_pointer("right", 1))
        self.play(FadeOut(sum_text2), FadeOut(action2))
        self.wait()

        # Iteration 3 - Found!
        sum_text3 = Text(
            "sum = 2 + 7 = 9 ✓",
            font_size=20,
            color=GREEN
        ).next_to(arr_viz, DOWN, buff=0.5)

        self.play(Write(sum_text3))

        frame4 = CallStackFrame(
            "two_sum()",
            {"left": 0, "right": 1, "sum": 9}
        )
        frame4.move_to(frame1.get_center())
        self.play(Transform(frame1, frame4))
        self.wait()

        # Highlight solution
        solution_boxes = VGroup(
            arr_viz.boxes[0].copy().set_color(GREEN),
            arr_viz.boxes[1].copy().set_color(GREEN)
        )

        self.play(
            Create(solution_boxes),
            rate_func=there_and_back
        )

        # Result
        result = Text(
            "return [1, 2]  (1-indexed)",
            font_size=24,
            color=GREEN
        ).next_to(sum_text3, DOWN, buff=0.5)

        self.play(Write(result))
        self.wait(2)

        # Complexity analysis
        complexity = VGroup(
            Text("Time Complexity: O(n)", font_size=20, color=BLUE),
            Text("Space Complexity: O(1)", font_size=20, color=BLUE)
        ).arrange(DOWN, aligned_edge=LEFT)

        complexity.to_edge(RIGHT).shift(UP)

        self.play(FadeIn(complexity))
        self.wait(3)

        # Fade out
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )


class RecursionTreeScene(Scene):
    """
    Visualization for recursive algorithms
    Shows call tree and stack frames
    """

    def construct(self):
        title = Text("Recursion Call Tree", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))

        # Example: Fibonacci
        subtitle = Text("Example: fibonacci(4)", font_size=24, color=GRAY)
        subtitle.next_to(title, DOWN)
        self.play(FadeIn(subtitle))
        self.wait()

        # Build recursion tree
        # TODO: Implement tree visualization

        self.wait(2)


class ComplexityComparisonScene(Scene):
    """
    Side-by-side comparison of O(n²) vs O(n) solutions
    """

    def construct(self):
        title = Text("Complexity Comparison: O(n²) vs O(n)", font_size=32)
        title.to_edge(UP)
        self.play(Write(title))

        # TODO: Implement graph showing execution time growth

        self.wait(2)


if __name__ == "__main__":
    # Example usage:
    # manim callstack_viz.py TwoPointersScene -pql
    pass
