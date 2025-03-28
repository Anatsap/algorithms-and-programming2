from queue import Queue

class Node:
    def __init__(self, priority, parent = None):
        self.queue = Queue()
        self.priority = priority
        self.left = None
        self.right = None
        self.parent = parent

class AVL_Priority_Queue:
    def __init__(self):
        self.root = None

    def left_height(self):
        return 0 if self.left is None else self.left.height

    def right_height(self):
        return 0 if self.right is None else self.right.height

    def balance_factor(self):
        return self.left_height() - self.right_height()

    def update_heigth(self):
        self.height = 1 + max(self.left_height(), self.right_height())

    def set_left(self, node):
        self.left = node
        if node is not None:
            node.parent = self
        self.update_heigth()

    def set_right(self, node):
        self.right = node
        if node is not None:
            node.parent = self
        self.update_heigth()

    def is_left_child(self):
        return self.parent is not None and self.parent.left == self

    def is_right_child(self):
        return self.parent is not None and self.parent.right == self

    def rotate_left(self, a):
        b = a.right
        a.set_right(b.left)
        b.set_left(a)
        return b

    def rotate_right(self, a):
        b = a.left
        a.set_left(b.right)
        b.set_right(a)
        return b

        # Inside the AVLTree class

    def rebalance(self, node):
        if node is None:
            return None
        balance = node.balance_factor()
        if abs(balance) <= 1:
            return node
        if balance == 2:
            if node.left.balance_factor() == -1:
                node.set_left(self.rotate_left(node.left))
            return self.rotate_right(node)
        if node.right.balance_factor() == 1:
            node.set_right(self.rotate_right(node.right))
        return self.rotate_left(node)

    def add(self, value):
        parent = None
        current = self.root
        while current is not None:
            parent = current
            if value < current.value:
                current = current.left
            else:
                current = current.right
        new_node = Node(value, parent)
        if parent is None:
            self.root = new_node
        else:
            if value < parent.value:
                parent.left = new_node
            else:
                parent.right = new_node
        self.restore_balance(new_node)

        # Inside the AVLTree class

    def restore_balance(self, node):
        current = node
        while current is not None:
            current.set_left(self.rebalance(current.left))
            current.set_right(self.rebalance(current.right))
            current.update_heigth()
            current = current.parent
        self.root = self.rebalance(self.root)
        self.root.parent = None


if __name__ == '__main__':
    myQueue = AVL_Priority_Queue()
    myQueue.add(12)
    myQueue.add(1)
    myQueue.add(14)
    myQueue.add(7)
    print(myQueue)
    while not myQueue.isEmpty():
        print(myQueue.delete())