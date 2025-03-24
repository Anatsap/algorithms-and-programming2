from queue import Queue


class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def insert(root, key):
    if root is None:
        return BinaryTree(key)
    if root.value == key:
        return root
    if root.value < key:
        root.right = insert(root.right, key)
    else:
        root.left = insert(root.left, key)

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
        return 0
    stack = [(node, 0)]

    dicti_height = {}
    while stack:
        current, depth = stack.pop()

        if current is not None:
            dicti_height[current] = depth

            stack.append((current.left, depth + 1))
            stack.append((current.right, depth + 1))

    stack = [node]

    while stack:
        current = stack.pop()

        h_left = dicti_height.get(current.left, 0)
        h_right = dicti_height.get(current.right, 0)

        if abs(h_left - h_right) > 1:
            return False
        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)
    return True


with open("tree.txt", "r") as file:
    root_value = int(file.readline().strip())
    root = BinaryTree(root_value)

    for line in file:
        nodes = line.strip().split()
        for value in nodes:
            if value != "None":
                root = insert(root, int(value))


print("Breadth First Search: ", bfs(root))
print("Self-balancing tree: ", is_tree_balanced(root))
