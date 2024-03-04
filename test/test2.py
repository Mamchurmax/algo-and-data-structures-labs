import unittest
from src.main2 import triplet


class TestTriplet(unittest.TestCase):
    def test_triplet_exist(self):
        self.assertEqual(triplet([1, 3, 5, 7, 8, 1, 23], 20), True)

    def test_triplets_not_exist(self):
        self.assertEqual(triplet([1, 3, 5, 7, 8, 1, 23], 40), False)


if __name__ == '__main__':
    unittest.main()
