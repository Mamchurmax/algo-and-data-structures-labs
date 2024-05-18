import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
import unittest
from src.islands import *


class MyTestCase(unittest.TestCase):
    def test_normal_case(self):
        input_file = "../resources/lab8/islands.csv"
        matrix = read_input(input_file)
        result = min_cable_length(matrix)
        self.assertEqual(result, 20)

    def test_empty_input(self):
        input_file = "../resources/lab8/no_islands.csv"
        matrix = read_input(input_file)
        result = min_cable_length(matrix)
        self.assertEqual(result, 0)

    def test_normal_case_2(self):
        input_file = "../resources/lab8/islands2.csv"
        matrix = read_input(input_file)
        result = min_cable_length(matrix)
        self.assertEqual(result, 17)


if __name__ == '__main__':
    unittest.main()
