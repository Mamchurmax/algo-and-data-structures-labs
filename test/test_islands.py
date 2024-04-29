import unittest
from src.islands import *


class MyTestCase(unittest.TestCase):
    def test_normal_case(self):
        input_file = "C:/Projects/algo-and-data-structures-labs/resources/lab8/islands.csv"
        matrix = read_input(input_file)
        result = prim(matrix)
        self.assertEqual(result, 5)

    def test_empty_input(self):
        input_file = "C:/Projects/algo-and-data-structures-labs/resources/lab8/no_islands.csv"
        matrix = read_input(input_file)
        result = prim(matrix)
        self.assertEqual(result, -1)

    def test_normal_case_2(self):
        input_file = "C:/Projects/algo-and-data-structures-labs/resources/lab8/islands2.csv"
        matrix = read_input(input_file)
        result = prim(matrix)
        self.assertEqual(result, 6)

    def test_normal_case_3(self):
        input_file = "C:/Projects/algo-and-data-structures-labs/resources/lab8/islands3.csv"
        matrix = read_input(input_file)
        result = prim(matrix)
        self.assertEqual(result, 21)


if __name__ == '__main__':
    unittest.main()
