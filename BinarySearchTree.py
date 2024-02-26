##################################
# Name: Slavic Heath
# Binary Search Tree

#####################################

from rand_list import *


class TreeNode:
    def __init__(self, item):
        self.key = item
        self.left = None
        self.right = None

    def get_key(self):
        return self.key

    def __str__(self):
        return str(self.key)

    def is_leaf(self):
        return self.left is None and self.right is None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def find(self, key):
        if self.root is None:  # tree is empty
            return 0
        else:
            return self.search(self.root, key)

    def search(self, current_node, key):
        current_key = current_node.get_key()
        if current_key == key:
            return 1
        elif key > current_key and current_node.right:
            return 1 + self.search(current_node.right, key)
        elif key < current_key and current_node.left:
            return 1 + self.search(current_node.left, key)
        else:
            return 0

    def store(self, key):
        if self.root is None:  # empty BST
            self.root = TreeNode(key)
        else:  # non-empty tree
            self._add_node(self.root, key)

    def _add_node(self, current_node, item):
        if item > current_node.get_key():  # add to right sub-tree
            if current_node.right is None:
                current_node.right = TreeNode(item)
            else:
                self._add_node(current_node.right, item)
        elif item < current_node.get_key():  # add to left sub-tree
            if current_node.left is None:
                current_node.left = TreeNode(item)
            else:
                self._add_node(current_node.left, item)

    def get_node_count(self):
        def count_nodes(node):
            if node is None:
                return 0
            else:
                return count_nodes(node.left) + 1 + count_nodes(node.right)

        return count_nodes(self.root)

    def get_height(self):
        # Count the maximum number of edges between any leaf node and the root node

        def get_node_height(node):
            # handle leaf node cases
            if node is None:
                return 0
            elif node.left is None and node.right is None:
                return 0
            else:
                return (
                        max(
                            get_node_height(node.left),
                            get_node_height(node.right),
                        )
                        + 1
                )

        return get_node_height(self.root)

    def __str__(self):
        if self.root:
            return self._pretty_print(self.root, 0)

    def _pretty_print(self, current_node, offset):
        spacer = 5
        print_string = ""
        if current_node.right:
            print_string += self._pretty_print(current_node.right, offset + spacer)

        if not current_node.is_leaf():
            print_string += "\n" + ' ' * offset + str(current_node) + '-' * spacer
        else:
            print_string += "\n" + ' ' * offset + str(current_node)

        if current_node.left:
            print_string += self._pretty_print(current_node.left, offset + spacer)

        return print_string


def main():
    t = BinarySearchTree()
    a = [70, 89, 65, 74, 34, 49, 109, 120, 66, 17, 167]
    # a = ["apple", "ball", "cat", "croak","ant", "aardvark", "duck"]

    for r in a:
        t.store(r)
    print(t)
    print("There are ", t.get_node_count(), " Nodes in the tree!")
    print("The height of the Tree is", t.get_height())
    print("Looking for the key 120 in the Tree: Compared  ", t.find(34), " Nodes")
    print("Looking for the key 2 in the Tree: Compared ", t.find(2), " Nodes")

    N = 16
    tree = BinarySearchTree()
    for val in range(N):
        tree.store(random.randint(0, 100))
    print(tree)
    print("There are ", tree.get_node_count(), " Nodes in the tree!")
    print("The height of the Tree is", tree.get_height())
    print("Looking for the key 50 in the Tree: Compared  ", tree.find(50), " Nodes")
    print("Looking for the key 70 in the Tree: Compared ", tree.find(70), " Nodes")

    test_num = 10
    avg_num = 0
    avg_height = 0
    avg_size = 0
    for rep in range(test_num):
        new_t = BinarySearchTree()
        N = 8000
        for i in range(N):
            new_t.store(random.randint(0, 1000))
        avg_num += new_t.find(50)
        avg_height += new_t.get_height()
        avg_size += new_t.get_node_count()
    print('\n')
    print("average number of nodes examined during searches: ", avg_num / test_num)
    print("average height of the tree: ", avg_height / test_num)
    print("average size of the tree", avg_size / test_num)


main()
