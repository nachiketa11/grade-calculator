import unittest
from unittest.mock import patch

import grade_calculator as calculator


class GradeCalculatorInputTests(unittest.TestCase):
    def test_grade_boundaries(self):
        expected = {
            100: ("O", "Outstanding"),
            90: ("O", "Outstanding"),
            89.99: ("A+", "Excellent"),
            80: ("A+", "Excellent"),
            70: ("A", "Very Good"),
            60: ("B+", "Good"),
            50: ("B", "Average"),
            40: ("C", "Satisfactory"),
            39.99: ("F", "Fail"),
            0: ("F", "Fail"),
        }
        for percentage, result in expected.items():
            with self.subTest(percentage=percentage):
                self.assertEqual(calculator.get_grade(percentage), result)

    def test_marks_reject_nan_and_infinity_then_accept_valid_value(self):
        with patch("builtins.input", side_effect=["nan", "inf", "-inf", "8.5"]), patch("builtins.print"):
            self.assertEqual(calculator.get_marks("Math", 10), 8.5)

    def test_marks_reject_out_of_range_values(self):
        with patch("builtins.input", side_effect=["-1", "11", "7"]), patch("builtins.print"):
            self.assertEqual(calculator.get_marks("Math", 10), 7.0)

    def test_max_marks_reject_non_finite_and_non_positive_values(self):
        with patch("builtins.input", side_effect=["nan", "inf", "0", "-2", "100"]), patch("builtins.print"):
            self.assertEqual(calculator.get_positive_float("Maximum marks: "), 100.0)

    def test_subject_count_requires_positive_integer(self):
        with patch("builtins.input", side_effect=["0", "-3", "2"]), patch("builtins.print"):
            self.assertEqual(calculator.get_positive_int("Subjects: "), 2)

    def test_invalid_text_is_retried(self):
        with patch("builtins.input", side_effect=["abc", "5"]), patch("builtins.print"):
            self.assertEqual(calculator.get_marks("Math", 10), 5.0)


if __name__ == "__main__":
    unittest.main()
