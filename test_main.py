import unittest
from main import power, factorial, permutation, combination


class TestMain(unittest.TestCase):
    def test_power(self):
        # normal test
        self.assertEqual(power(2, 3), 8)
        # power of zero test
        self.assertEqual(power(2, 0), 1)
        # test for negative power
        self.assertEqual(power(2, -4), 0.0625)
        # test for negative number with even power
        self.assertEqual(power(-3, 2), 9)
        # test for negative number with odd power
        self.assertEqual(power(-3, 3), -27)

    def test_factorial(self):
        # normal factorial
        self.assertEqual(factorial(6), 720)
        # factorial of 0
        self.assertEqual(factorial(0), 1)
        # test for error
        self.assertRaises(ValueError, factorial, -3)

    def test_permutation(self):
        # normal factorial
        self.assertEqual(permutation(4, 2), 12.0)
        # error when n < r
        self.assertRaises(ValueError, permutation, 2, 4)

    def test_combination(self):
        # normal factorial
        self.assertEqual(combination(4, 2), 6.0)
        # error when n < r
        self.assertRaises(ValueError, combination, 2, 4)


if __name__ == "__main__":
    unittest.main()
