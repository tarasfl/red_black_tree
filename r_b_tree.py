class Node:
    def __init__(self, key):
        self.red = False
        self.left = None
        self.right = None
        self.parent = None
        self.key = key


class Tree:
    def __init__(self):
        self.null = Node(None)
        self.null.right = None
        self.null.left = None
        self.null.red = False
        self.root = self.null

    def find_parent(self, key, current):
        if key < current.key:
            current = current.left
        elif key > current.key:
            current = current.right

    def insert(self, key):
        new_node = Node(key)

        new_node.right = self.null
        new_node.left = self.null
        new_node.parent = None
        new_node.red = True

        current = self.root
        parent = self.find_parent(key, current)


