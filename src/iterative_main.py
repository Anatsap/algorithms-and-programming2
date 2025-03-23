from queue import Queue


class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def bfs(node):
        with open('tree.txt', 'r') as file:
            print(file.readlines())
            print(file.readline().split())
        q = Queue()
        visited = []
        visited.append(node)
        q.put(file.readline().split())

        while q:
            s = q.get()
            print(s, end = " ")

            for n in node[s]:
                if n not in visited:
                    visited.append(n)
                    q.put(n)

def is_tree_balanced(node):
    if node is None:
        return 0

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

        dicti[id(node)] = max(h_left, h_right ) + 1
        if abs(h_left - h_right) > 1:
            return False

    return True

# if __name__ == "__main__":
#     root = BinaryTree(1)
#     root.left = BinaryTree(2)
#     root.right = BinaryTree(3)
#     root.left.left = BinaryTree(4)
#     root.left.right = BinaryTree(5)
tree_node = bfs()
print(is_tree_balanced())
