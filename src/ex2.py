
class Node:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.left = None
        self.right = None
        self.height = 1
    def __str__(self):
        return f"({self.id}: {self.name})"

class AVLTree1:
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

    def insert(self, root, id, name):
        if not root:
            return Node(id, name)

        stack = []
        current = root
        parent = None
        while current:
            stack.append(current)
            parent = current
            if id < current.id:
                current = current.left
            else:
                current = current.right

        new_node = Node(id, name)
        if id < parent.id:
            parent.left = new_node
        else:
            parent.right = new_node

        while stack:
            node = stack.pop()
            node.height = 1 + max(self.height(node.left), self.height(node.right))
            balance = self.balance(node)

            if balance > 1:
                if id < node.left.id:
                    return self.right_rotate(node)
                else:
                    node.left = self.left_rotate(node.left)
                    return self.right_rotate(node)

            if balance < -1:
                if id > node.right.id:
                    return self.left_rotate(node)
                else:
                    node.right = self.right_rotate(node.right)
                    return self.left_rotate(node)

        return root

    def delete(self, root, id):
        node_to_delete = self.search(root, id)
        if not node_to_delete:
            print(f"Node with id {id} not found.")
            return root

        parent = None
        current = root

        while current and current.id != id:
            parent = current
            if id < current.id:
                current = current.left
            else:
                current = current.right

        if not current.left or not current.right:
            child = current.left if current.left else current.right

            if not parent:
                root = child
            else:
                if parent.left == current:
                    parent.left = child
                else:
                    parent.right = child
        else:
            successor = self.min_id_node(current.right)
            current.id = successor.id
            current.name = successor.name
            parent = current
            temp = current.right
            while temp and temp.id != successor.id:
                parent = temp
                temp = temp.left

            if parent.left == successor:
                parent.left = successor.right
            else:
                parent.right = successor.right
        node = parent
        while node:
            node.height = 1 + max(self.height(node.left), self.height(node.right))
            balance = self.balance(node)

            if balance > 1:
                if self.balance(node.left) >= 0:
                    node = self.right_rotate(node)
                else:
                    node.left = self.left_rotate(node.left)
                    node = self.right_rotate(node)

            if balance < -1:
                if self.balance(node.right) <= 0:
                    node = self.left_rotate(node)
                else:
                    node.right = self.right_rotate(node.right)
                    node = self.left_rotate(node)

            if node == root:
                break
            node = parent
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

    def min_id_node(self, root):
        current = root
        while current.left:
            current = current.left
        return current

    def search(self, root, id):
        current = root
        while current:
            if id == current.id:
                return current
            elif id < current.id:
                current = current.left
            else:
                current = current.right
        return None


    def insert_id(self, id, name):
        self.root = self.insert(self.root, id, name)

    def delete_id(self, id):
        self.root = self.delete(self.root, id)
        if self.root is None:
            print("The tree is now empty.")

    def search_id(self, id):
        return self.search(self.root, id)

    def search_min_id(self):
        if self.root is None:
            return None
        return self.min_id_node(self.root)

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
                traversal.append((str(node)))
                node = node.right

        return traversal

if __name__ == '__main__':
    nodes = AVLTree1()
    while True:
        u = input("Write what you want to do? ")
        if u == "add":
            add = input("Add id and name: ").split(",")
            nodes.insert_id(add[0], add[1])
        if u == "show":
            nodes.get_nodes()
        if u == "delt":
            delt =input("Delete one id: ")
            nodes.delete_id(delt[0])
        if u == "ls":
            # ls = input("Show me all ids and names: ")
            nodes.get_nodes()
            print("Tree after deletion:", nodes.get_nodes())


