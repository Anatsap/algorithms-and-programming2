class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def height_subtree(node):
    if node is None:
        return -1
    left_height = height_subtree(node.left)
    right_height = height_subtree(node.right)
    h_under = max(left_height, right_height) + 1
    return h_under


def is_tree_balanced(node):
    if node is None:
        return True

    left_height = height_subtree(node.left)
    right_height = height_subtree(node.right)
    balance = left_height - right_height

    return (
        -1 <= balance <= 1
        and is_tree_balanced(node.left)
        and is_tree_balanced(node.right)
    )
root = BinaryTree(3)
root.left = BinaryTree(9)
root.right = BinaryTree(20)
root.left.left = BinaryTree(8)
print(is_tree_balanced(root))
