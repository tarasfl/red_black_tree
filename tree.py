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
            return new_element

        elif key < current.key:
            if current.left == self.null:
                current.left = new_element
                return new_element
            else:
                current = current.left
                return self.insert_element(key, current)

        elif key > current.key:
            if current.right == self.null:
                current.right = new_element
                return current.right
            else:
                current = current.right
                return self.insert_element(key, current)

    # insert parent
    def rotate_left(self, node):
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

            if new_parent.left != self.null:
                left_child = new_parent.left    # left child of element to exchange with
                node.right = left_child         # make left element of new parent as right element of node
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

            if new_parent.right != self.null:
                right_child = new_parent.right  # right child of element to exchange with
                node.left = right_child  # make right element of new parent as left element of node
            new_parent.right = node  # make node as right element of new parent

    def balance_tree(self):
        pass

    # actual insertion case 1
    def color_question(self, node):
        parent = self.find_parent(node.key)

        if parent is None:
            node.red = False
        else:
            self.case_2(node)

    # case 2
    def case_2(self, node):
        parent = self.find_parent(node.key)
        if not parent.red:
            return
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
            self.color_question(grandparent)
        else:
            self.case_4(node)

    def case_4(self, node):
        parent = self.find_parent(node.key)
        grandparent = self.find_grandparent(node.key)

        if node is parent.right and parent is grandparent.left:
            self.rotate_left(parent)

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


def inorder(node):
    if node:
        inorder(node.left)
        print(node.key, '  ', node.red)
        inorder(node.right)


if __name__ == '__main__':
    tree = Tree()

    tree.insert_element(10)
    tree.insert_element(15)
    node7 = tree.insert_element(7)
    node8 = tree.insert_element(8)
    node5 = tree.insert_element(5)
    node6 = tree.insert_element(6)
    tree.insert_element(2)

    print(tree.find_parent(node6))

    # inorder(tree.root)
