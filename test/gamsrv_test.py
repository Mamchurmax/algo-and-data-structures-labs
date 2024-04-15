import unittest
from src.gamsrv import *


class MyTestCase(unittest.TestCase):
    def test_case_example_1(self):
        ping('C:/Projects/algo-and-data-structures-labs/resources/lab6/gamsrv_1.in.txt',
             'C:/Projects/algo-and-data-structures-labs/resources/lab6/gamsrv_1.output.txt')
        file = open('C:/Projects/algo-and-data-structures-labs/resources/lab6/gamsrv_1.output.txt', 'r')
        result = int(file.readline())
        file.close()
        self.assertEqual(result, 100)

    def test_case_example_2(self):
        ping('C:/Projects/algo-and-data-structures-labs/resources/lab6/gamsrv_2.in.txt',
             'C:/Projects/algo-and-data-structures-labs/resources/lab6/gamsrv_2.output.txt')
        file = open('C:/Projects/algo-and-data-structures-labs/resources/lab6/gamsrv_2.output.txt', 'r')
        result = int(file.readline())
        file.close()
        self.assertEqual(result, 10)

    def test_case_example_3(self):
        ping('C:/Projects/algo-and-data-structures-labs/resources/lab6/gamsrv_3.in.txt',
             'C:/Projects/algo-and-data-structures-labs/resources/lab6/gamsrv_3.output.txt')
        file = open('C:/Projects/algo-and-data-structures-labs/resources/lab6/gamsrv_3.output.txt', 'r')
        result = int(file.readline())
        file.close()
        self.assertEqual(result, 1000000000)

    def test_empty_input(self):
        ping('C:/Projects/algo-and-data-structures-labs/resources/lab6/gamsrv_empty.in.txt',
             'C:/Projects/algo-and-data-structures-labs/resources/lab6/gamsrv_empty.output.txt')
        file = open('C:/Projects/algo-and-data-structures-labs/resources/lab6/gamsrv_empty.output.txt', 'r')
        result = file.readline()
        file.close()
        self.assertEqual(result, 'None')


if __name__ == '__main__':
    unittest.main()
