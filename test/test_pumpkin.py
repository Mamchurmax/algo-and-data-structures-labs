import unittest
from src.pumpkin import pumpkin


class TestPumpkin(unittest.TestCase):
    def test_value_1(self):
        expected = [1, 2, 3, 4, 5, 10, 9, 8, 7, 6, 11, 12, 13, 14, 15, 20, 19, 18, 17, 16, 21, 22, 23, 24, 25]
        self.assertEqual(pumpkin(5, 5), expected)

    def test_value_2(self):
        expected = [1, 2, 3, 4, 8, 7, 6, 5]
        self.assertEqual(pumpkin(2, 4), expected)

    def test_value_3(self):
        expected = [1, 2, 3, 4, 5, 6]
        self.assertEqual(pumpkin(1, 6), expected)


if __name__ == '__main__':
    unittest.main()
