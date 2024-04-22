import unittest
from src.labyrinth import *


class MyTestCase(unittest.TestCase):

    def test_empty_output(self):
        input_file = 'C:/Projects/algo-and-data-structures-labs/resources/lab5/empty_input.txt'
        output_file = 'C:/Projects/algo-and-data-structures-labs/resources/lab5/empty_output.txt'
        input_data = read_input(input_file, output_file)
        file = open(output_file)
        output = file.read()
        file.close()
        self.assertEqual(str(input_data), output)

    def test_given_example(self):
        input_file = 'C:/Projects/algo-and-data-structures-labs/resources/lab5/input.txt'
        output_file = 'C:/Projects/algo-and-data-structures-labs/resources/lab5/output.txt'
        start, goal, size, lab = read_input(input_file, output_file)
        result = labyrinth(start, goal, size, lab)
        file = open("C:/Projects/algo-and-data-structures-labs/resources/lab5/output.txt")
        shortest_path = int(file.readline())
        file.close()
        self.assertEqual(result, shortest_path)

    def test_no_path(self):
        start = (0, 0)
        goal = (2, 2)
        size = (3, 3)
        lab = [
            [1, 0, 1],
            [0, 0, 0],
            [1, 0, 1]
        ]
        expected_distance = None
        self.assertEqual(labyrinth(start, goal, size, lab), expected_distance)

    def test_large_labyrinth(self):
        start = (0, 0)
        goal = (999, 999)
        size = (1000, 1000)
        lab = [[1] * 1000 for _ in range(1000)]
        expected_distance = 1998
        self.assertEqual(labyrinth(start, goal, size, lab), expected_distance)


if __name__ == '__main__':
    unittest.main()
