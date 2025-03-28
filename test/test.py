import unittest
from avl_priority_queue import is_tree_balanced, BinaryTree

class TestBinaryTree(unittest.TestCase):
    def test_tree_balanced(self):
        root = BinaryTree(3)
        root.left = BinaryTree(9)
        root.right = BinaryTree(20)
        root.left.left = BinaryTree(8)
        self.assertTrue(is_tree_balanced(root))

    def test_tree_balanced222(self):
        root = BinaryTree(24)
        root.left = BinaryTree(18)
        root.right = BinaryTree(70)
        root.left.left = BinaryTree(7)
        root.left.right = BinaryTree(50)
        root.right.left = BinaryTree(64)
        self.assertTrue(is_tree_balanced(root))

    def test_tree_balanced333(self):
        root = BinaryTree(90)
        root.right = BinaryTree(102)
        root.right.right = BinaryTree(250)
        self.assertFalse(is_tree_balanced(root))



    if __name__ == '__main__':
        unittest.main()