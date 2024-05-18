import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
import unittest
from src.gamsrv import *


class MyTestCase(unittest.TestCase):
    def test_case_example_1(self):
        ping('../resources/lab6/gamsrv_1.in.txt',
             '../resources/lab6/gamsrv_1.output.txt')
        file = open('../resources/lab6/gamsrv_1.output.txt', 'r')
        result = int(file.readline())
        file.close()
        self.assertEqual(result, 1004)

    def test_case_example_2(self):
        ping('../resources/lab6/gamsrv_2.in.txt',
             '../resources/lab6/gamsrv_2.output.txt')
        file = open('../resources/lab6/gamsrv_2.output.txt', 'r')
        result = int(file.readline())
        file.close()
        self.assertEqual(result, 105)

    def test_case_example_3(self):
        ping('../resources/lab6/gamsrv_3.in.txt',
             '../resources/lab6/gamsrv_3.output.txt')
        file = open('../resources/lab6/gamsrv_3.output.txt', 'r')
        result = int(file.readline())
        file.close()
        self.assertEqual(result, 10000000002)

    def test_empty_input(self):
        ping('../resources/lab6/gamsrv_empty.in.txt',
             '../resources/lab6/gamsrv_empty.output.txt')
        file = open('../resources/lab6/gamsrv_empty.output.txt', 'r')
        result = file.readline()
        file.close()
        self.assertEqual(result, 'None')


if __name__ == '__main__':
    unittest.main()
