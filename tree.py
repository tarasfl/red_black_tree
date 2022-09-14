class Node:

    def __init__(self, key):
        self.right = None
        self.left = None
        self.key = key
        self.red = True


class Tree:
    def __init__(self):
        self.null = Node(None)
        self.null.right = None
        self.null.left = None
        self.null.red = False
        self.root = self.null

    # Current - node from which start iteration

    def insert_element(self, key, current=None):
        new_element = Node(key)
        new_element.right = self.null
        new_element.left = self.null
        new_element.red = True

        if current is None:
            current = self.root

        if self.root == self.null:
            new_element.red = False
            self.root = new_element
            self.balance_tree(new_element)
            return new_element

        elif key < current.key:
            if current.left == self.null:
                current.left = new_element
                self.balance_tree(new_element)
                return new_element
            else:
                current = current.left
                return self.insert_element(key, current)

        elif key > current.key:
            if current.right == self.null:
                current.right = new_element
                self.balance_tree(new_element)
                return current.right
            else:
                current = current.right
                return self.insert_element(key, current)

    # insert parent
    def rotate_left(self, node):
        print("rotate left")
        # node parent element of rotation
        if node.right != self.null:
            new_parent = node.right             # element to exchange with

            if node == self.root:
                self.root = new_parent
            else:
                node_parent = self.find_parent(node.key, self.root)
                if node_parent.left == node:
                    node_parent.left = new_parent
                elif node_parent.right == node:
                    node_parent.right = new_parent

            node.right = new_parent.left        # make left element of new parent as right element of node
            new_parent.left = node              # make node as left element of new parent

    def rotate_right(self, node):
        # node parent element of rotation
        if node.left != self.null:
            new_parent = node.left  # element to exchange with
            if node == self.root:
                self.root = new_parent
            else:
                node_parent = self.find_parent(node.key, self.root)
                if node_parent.left == node:
                    node_parent.left = new_parent
                elif node_parent.right == node:
                    node_parent.right = new_parent

            node.left = new_parent.right  # make right element of new parent as left element of node
            new_parent.right = node  # make node as right element of new parent

    # actual insertion case 1
    def balance_tree(self, node):
        parent = self.find_parent(node.key)

        if parent is None:
            node.red = False
        else:
            self.case_2(node)

    # case 2
    def case_2(self, node):
        parent = self.find_parent(node.key)
        if not parent.red:
            return None
        else:
            self.red_conflict(node)

    # case 3
    def red_conflict(self, node):
        uncle = self.find_uncle(node)
        parent = self.find_parent(node.key)
        grandparent = self.find_grandparent(node.key)

        if uncle and uncle.red:
            parent.red = False
            uncle.red = False
            grandparent.red = True
            self.balance_tree(grandparent)
        else:
            self.case_4(node)

    def case_4(self, node):
        parent = self.find_parent(node.key)
        grandparent = self.find_grandparent(node.key)

        if node is parent.right and parent is grandparent.left:
            self.rotate_left(parent)
        elif node is parent.left and parent is grandparent.right:
            self.rotate_right(parent)
        self.case_5(node)

    def case_5(self, node):
        parent = self.find_parent(node.key)
        grandparent = self.find_grandparent(node.key)

        parent.red = False
        grandparent.red = True

        if node is parent.left and parent is grandparent.left:
            self.rotate_right(grandparent)
        else:
            self.rotate_left(grandparent)

    def find_uncle(self, node):
        grandparent = self.find_grandparent(node.key)
        parent = self.find_parent(node.key)

        if grandparent is not None:
            if grandparent.left is parent:
                return grandparent.right
            else:
                return grandparent.left
        return None

    def find_parent(self, key, current=None):
        if current is None:
            current = self.root
        if key == current.key:
            return None
        elif key < current.key and current.left is not None:
            if key == current.left.key:
                return current
            else:
                current = current.left
                return self.find_parent(key, current)
        elif key > current.key and current.right is not None:
            if key == current.right.key:
                return current
            else:
                current = current.right
                return self.find_parent(key, current)

    def find_grandparent(self, key, current=None):
        if current is None:
            current = self.root
        if key == current.key:
            return None

        parent = self.find_parent(key, current)
        grandparent = self.find_parent(parent.key)
        return grandparent

    def print_tree(self, node=None):
        if node is None:
            node = self.root
        if node.left is not None:
            self.print_tree(node.left)

        print(node.key, '      red:', node.red),
        if node.right is not None:
            self.print_tree(node.right)


if __name__ == '__main__':
    tree = Tree()

    node10 = tree.insert_element(10)
    tree.insert_element(15)
    tree.insert_element(17)

    tree.print_tree()
