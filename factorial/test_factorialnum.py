import unittest
from factorial import factorialnum

class TestFactorial(unittest.TestCase):

    def test_factorialnum(self):
        self.assertEqual(factorialnum.factorialfun(5), 120)


if __name__ == '__main__':
    unittest.main()

