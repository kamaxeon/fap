import unittest

from app.calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_calculator_addition_method_returns_correct_result(self):
        calc = Calculator()
        result = calc.addition(2,2)
        self.assertEqual(4, result)

    def test_calculator_subtraction_method_returns_correct_result(self):
        calc = Calculator()
        result = calc.substraction(4,2)
        self.assertEqual(2, result)

    def test_calculator_division_method_returns_correct_result(self):
        calc = Calculator()
        result = calc.division(5,2)
        self.assertEqual(2.5, result)
