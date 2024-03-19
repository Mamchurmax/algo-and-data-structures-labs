from src.heap_based_priority_queue import *
import unittest


class TestPriorityQueue(unittest.TestCase):

    def test_case_1(self):
        queue = PriorityQueue()

        queue.insert('third', 3)
        queue.insert('first', 1)
        queue.insert('eight', 8)
        queue.insert('eight', 8)
        queue.insert('fourth', 4)
        queue.insert('eight', 8)
        self.assertEqual(queue.show(), ['eight', 'eight', 'eight', 'first', 'fourth', 'third'])

    def test_case_2(self):
        queue = PriorityQueue()

        queue.insert('third', 3)
        queue.insert('first', 1)
        queue.insert('eight', 8)
        queue.insert('eight', 8)
        queue.insert('fourth', 4)
        queue.insert('eight', 8)

        queue.delete_root()
        queue.delete_root()
        self.assertEqual(queue.show(), ['eight', 'fourth', 'third', 'first'])

    def test_empty_queue(self):
        queue = PriorityQueue()
        queue.insert('first', 1)
        queue.delete_root()
        self.assertEqual(queue.show(), None)
