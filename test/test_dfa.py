import unittest
from src.dfa import *


class MyTestCase(unittest.TestCase):
    def test_normal_case1(self):
        result = search_dfa("abxabcabcaby", "abcaby")
        self.assertEqual(result, [6])

    def test_normal_case2(self):
        result = search_dfa("sdadsadasdasdsa", "das")
        self.assertEqual(result, [6, 9])

    def test_no_matches(self):
        result = search_dfa("нот еверейдж нот інгліш вордс", "just average english words")
        self.assertEqual(result, [])

    def test_empty_haystack(self):
        result = search_dfa("", "abc")
        self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()
