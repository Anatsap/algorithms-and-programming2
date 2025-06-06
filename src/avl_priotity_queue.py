from collections import deque
class Node:
    def __init__(self, value, payload):
        self.value = value
        self.payload = payload
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if not node:
            return 0
        return node.height

    def balance(self, node):
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)

    def insert(self, root, value, payload):
        if not root:
            return Node(value, payload)
        elif value < root.value:
            root.left = self.insert(root.left, value, payload)
        else:
            root.right = self.insert(root.right, value, payload)

        root.height = 1 + max(self.height(root.left), self.height(root.right))
        balance = self.balance(root)

        if balance > 1 and value < root.left.value:
            return self.right_rotate(root)


        if balance < -1 and value > root.right.value:
            return self.left_rotate(root)


        if balance > 1 and value > root.left.value:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)


        if balance < -1 and value < root.right.value:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def delete(self, root, value):
        if not root:
            return root

        if value < root.value:
            root.left = self.delete(root.left, value)
        elif value > root.value:
            root.right = self.delete(root.right, value)
        else:
            if not root.left:
                temp = root.right
                root = None
                return temp
            elif not root.right:
                temp = root.left
                root = None
                return temp

            temp = self.min_value_node(root.right)
            root.value = temp.value
            root.right = self.delete(root.right, temp.value)

        if not root:
            return root

        root.height = 1 + max(self.height(root.left), self.height(root.right))
        balance = self.balance(root)

        if balance > 1 and self.balance(root.left) >= 0:
            return self.right_rotate(root)

        if balance < -1 and self.balance(root.right) <= 0:
            return self.left_rotate(root)


        if balance > 1 and self.balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        if balance < -1 and self.balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y

    def min_value_node(self, root):
        current = root
        while current.left:
            current = current.left
        return current

    def search(self, root, value):
        if not root or root.value == value:
            return root
        if root.value < value:
            return self.search(root.right, value)
        return self.search(root.left, value)


    def insert_value(self, value, payload):
        self.root = self.insert(self.root, value, payload)

    def delete_value(self, value):
        self.root = self.delete(self.root, value)

    def search_value(self, value):
        return self.search(self.root, value)

    def search_min_value(self):
        if self.root is None:
            return None
        return self.min_value_node(self.root)

    def get_nodes(self):
        traversal = []

        node = self.root
        stack = []
        while node or stack:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                traversal.append(node)
                node = node.right

        return traversal


class PriorityQueue:

    def __init__(self):
        self.tree = AVLTree()

    def put(self, value, priority):
        node = self.tree.search_value(priority)
        if node is not None:
            node.payload.append(value)
        else:
            payload = deque()
            payload.append(value)
            self.tree.insert_value(priority, payload)

    def get(self):
        node = self.tree.search_min_value()
        if node is None:
            raise RuntimeError("Queue is empty")

        value = node.payload.popleft()

        if len(node.payload) == 0:
            self.tree.delete_value(node.value)

        return  value


    def all_queue(self):
        elements = []
        for node in self.tree.get_nodes():
            elements.extend(list(node.payload))
        return elements

if __name__ == '__main__':
    tree = PriorityQueue()

    tree.put(30, 2)
    tree.put(40, 1)
    tree.put(8, 0)
    tree.put(60, 0)
    tree.put(55, 3)

    print(tree.all_queue())
    print(tree.get())
    print(tree.get())
    print(tree.get())
    print(tree.get())
    print(tree.get())
    print(tree.all_queue())

