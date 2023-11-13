import unittest
from math_quiz import generate_random_integer, generate_random_operator, perform_arithmetic_operation

class TestMathQuizFunctions(unittest.TestCase):

    def test_generate_random_integer(self):
        result = generate_random_integer(1, 10)
        self.assertTrue(1 <= result <= 10)

    def test_generate_random_operator(self):
        result = generate_random_operator()
        self.assertIn(result, ['+', '-', '*'])

    def test_perform_arithmetic_operation(self):
        num1, num2, operator = 5, 3, '+'
        problem, result = perform_arithmetic_operation(num1, num2, operator)
        self.assertEqual(problem, "5 + 3")
        self.assertEqual(result, 8)

if __name__ == '__main__':
    unittest.main()
