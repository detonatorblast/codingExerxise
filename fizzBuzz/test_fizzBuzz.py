import fizzBuzz
import unittest

class TestfizzBuzz(unittest.TestCase):

    def test_fizzbuzz(self):
        expected = [
            '1',
            '2',
            'Fizz',
            '4',
            'Buzz',
            'Fizz',
            '7',
            '8',
            'Fizz',
            'Buzz',
            '11',
            'Fizz',
            '13',
            '14',
            'FizzBuzz'
        ]
        self.assertEqual(fizzBuzz.fizzbuzz(15), expected)
        with self.assertRaises(TypeError):
            fizzBuzz.fizzbuzz('m')
