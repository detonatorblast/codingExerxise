import unittest
import simpleCalculator


class TestsimpleCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(simpleCalculator.add(10, 15), 25)
        self.assertEqual(simpleCalculator.add(-10, 15), 5)
        self.assertEqual(simpleCalculator.add(-10, -15), -25)

    def test_subtract(self):
        self.assertEqual(simpleCalculator.subtract(10, 15), -5)
        self.assertEqual(simpleCalculator.subtract(-10, -15), 5)
        self.assertEqual(simpleCalculator.subtract(-10, 15), -25)

    def test_multiply(self):
        self.assertEqual(simpleCalculator.multiply(2, 5), 10)
        self.assertEqual(simpleCalculator.multiply(-2, -5), 10)
        self.assertEqual(simpleCalculator.multiply(-2, 5), -10)

    def test_divide(self):
        self.assertEqual(simpleCalculator.divide(10, 5), 2)
        self.assertEqual(simpleCalculator.divide(-10, 5), -2)
        self.assertEqual(simpleCalculator.divide(-10, -5), 2)
        self.assertEqual(simpleCalculator.divide(11, 5), 2.2)

        # Test exceptions
        # self.assertRaises(ValueError, simpleCalculator.divide, 10, 0)

        # Another way to test exceptions
        with self.assertRaises(ValueError):
            simpleCalculator.divide(10, 0)


if __name__ == '__main__':
    unittest.main()
