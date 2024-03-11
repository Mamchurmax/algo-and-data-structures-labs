class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def find_left_leaf(node):
    while node.left:
        node = node.left
    return node


def find_successor(root: BinaryTree, node: BinaryTree) -> BinaryTree:
    if node.right:
        return find_left_leaf(node.right)
    else:
        while node.parent and node.parent.right == node:
            node = node.parent
        return node.parent
