import compress
import unittest


class TestCompress(unittest.TestCase):

    def test_compress(self):
        self.assertEqual(compress.compress("AAAABBAAA"), "A4B2A3")
        self.assertEqual(compress.compress('AAABCCDDDDE'), 'A3BC2D4E')
        self.assertEqual(compress.compress('1113'), '133')


if __name__ == '__main__':
    unittest.main()