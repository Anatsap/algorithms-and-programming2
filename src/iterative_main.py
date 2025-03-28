from queue import Queue
import os

class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def insert(root, key):
    if root is None:
        return BinaryTree(key)

    current = root
    while True:
        if key < current.value:
            if current.left is None:
                current.left = BinaryTree(key)
                break
            else:
                current = current.left
        elif key > current.value:
            if current.right is None:
                current.right = BinaryTree(key)
                break
            else:
                current = current.right
    return root


def bfs(root):
    q = Queue()
    visited = []
    q.put(root)

    while not q.empty():
        s = q.get()
        visited.append(s.value)

        if s.left:
            q.put(s.left)
        if s.right:
            q.put(s.right)
    return visited


def is_tree_balanced(node):
    if node is None:
        raise ValueError("Tree is empty")
    stack1 = []
    stack2 = []
    dicti = {}
    stack1.append(node)
    while stack1:
        node = stack1.pop()
        stack2.append(node)
        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)

    while stack2:
        h_left = 0
        h_right = 0

        node = stack2.pop()
        if node.left is not None:
            h_left = dicti.get(id(node.left), 0)
        if node.right is not None:
            h_right = dicti.get(id(node.right), 0)


        if abs(h_left - h_right) > 1:
            return False

    return True
file_path = "empty_tree.txt"
if os.stat(file_path).st_size == 0:
    print("File is empty, you can not create the tree")
else:
    with open(file_path, "r") as file:
        root = None
        for line in file:
            nodes = line.strip().split()
            for value in nodes:
                if value == "None":
                    continue
                if root is None:
                    root = BinaryTree(int(value))
                else:
                    root = insert(root, int(value))

    if root is None:
        print("File contains only None, you can not create the tree")
    else:
        print("Breadth First Search: ", bfs(root))
        print("Self-balancing tree: ", is_tree_balanced(root))

