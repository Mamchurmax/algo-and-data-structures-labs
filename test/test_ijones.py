from src.ijones import *
import unittest


class MyTestCase(unittest.TestCase):
    def test_given_1(self):
        input_file = "C:/Projects/algo-and-data-structures-labs/resources/lab9/ijones.in.txt"
        output_file = "C:/Projects/algo-and-data-structures-labs/resources/lab9/ijones.out.txt"
        indiana_jones(input_file, output_file)
        file = open(output_file, 'r')
        result = file.readline()
        file.close()
        self.assertEqual(result, "5")

    def test_given_2(self):
        input_file = "C:/Projects/algo-and-data-structures-labs/resources/lab9/ijones2.in.txt"
        output_file = "C:/Projects/algo-and-data-structures-labs/resources/lab9/ijones2.out.txt"
        indiana_jones(input_file, output_file)
        with open(output_file, 'r') as f:
            result = f.readline()
        self.assertEqual(result, "2")

    def test_given_3(self):
        input_file = "C:/Projects/algo-and-data-structures-labs/resources/lab9/ijones3.in.txt"
        output_file = "C:/Projects/algo-and-data-structures-labs/resources/lab9/ijones3.out.txt"
        indiana_jones(input_file, output_file)
        with open(output_file, 'r') as f:
            result = f.readline()
        self.assertEqual(result, "201684")


if __name__ == '__main__':
    unittest.main()
