from src.in_order_traversal_successor import *
import unittest


class TestFindSuccessor(unittest.TestCase):
    def test_find_successor_with_right_child(self):
        root = BinaryTree(10)
        root.left = BinaryTree(5)
        root.left.left = BinaryTree(3)
        root.left.right = BinaryTree(7)
        root.right = BinaryTree(15)
        root.right.right = BinaryTree(20)
        root.right.right.left = BinaryTree(12)

        node_5 = root.left
        successor = find_successor(root, node_5)
        if successor:
            self.assertEqual(successor.value, 7)
        else:
            self.fail("Successor is None")

    def test_find_successor_with_no_successor(self):
        root = BinaryTree(10)
        root.left = BinaryTree(5)
        root.left.left = BinaryTree(3)
        root.left.right = BinaryTree(7)
        root.right = BinaryTree(15)
        root.right.right = BinaryTree(20)
        root.right.right.left = BinaryTree(12)

        node_20 = root.right.right
        successor = find_successor(root, node_20)
        self.assertIsNone(successor)


if __name__ == "__main__":
    unittest.main()
