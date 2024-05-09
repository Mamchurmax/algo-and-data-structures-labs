import unittest
from src.rabin_karp import *


class TestFiniteAutomata(unittest.TestCase):
    def test_normal_case(self):
        result = rabin_karp("aaaacabaabcadacab", "acab")
        self.assertEqual(result, [3, 13])

    def test_normal_case2(self):
        result = rabin_karp("asdghjasdasdeerasd", "asd")
        self.assertEqual(result, [0, 6, 9, 15])

    def test_no_needle_in_haystack(self):
        result = rabin_karp("kjfasdfkjsdgjkas", "nnn")
        self.assertEqual(result, [])

    def test_empty(self):
        result = rabin_karp("", "")
        self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()