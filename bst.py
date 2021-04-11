class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BST:
    def __init__(self):
        self.root = None

    def next(self, value):
        """
        Finding the minimum element in the tree that is greater than value, or None if there is no such element.
        """
        node = self.root
        min_node = None
        minimum = float('inf')
        while node:
            if node.data > value:
                if node.data < minimum:
                    min_node = node
                    minimum = node.data
                node = node.left
            else:
                node = node.right
        return min_node

    def prev(self, value):
        """
        Finding the maximum element in the tree that is less than value, or None if there is no such element.
        """
        node = self.root
        max_node = None
        maximum = -float('inf')
        while node:
            if node.data < value:
                if node.data > maximum:
                    max_node = node
                    maximum = node.data
                node = node.right
            else:
                node = node.left
        return max_node

    def exists(self, value):
        """
        Checks the existence of a number with the value in the tree.
        """
        node = self.root
        while node is not None:
            if value == node.data:
                return True
            if value < node.data:
                node = node.left
            else:
                node = node.right
        return False

    def insert_node(self, node, value):
        """
        Inserts a new node  into the tree at the correct location.
        """
        if node is None:
            return Node(value)

        if value < node.data:
            node.left = self.insert_node(node.left, value)
        else:
            node.right = self.insert_node(node.right, value)

        return node

    def insert(self, value):
        """
        Inserts a new node that contains the given value into the tree at the correct location.
        """
        self.root = self.insert_node(self.root, value)

    @staticmethod
    def minimum(node):
        """
        Finds the smallest node by data.
        """
        while node.left is not None:
            node = node.left
        return node

    def delete_node(self, node, value):
        """
        Deletes the node from tree.
        """
        if node is None:
            return node

        if value < node.data:
            node.left = self.delete_node(node.left, value)
        elif value > node.data:
            node.right = self.delete_node(node.right, value)
        elif node.left is not None and node.right is not None:
            node.data = self.minimum(node.right).data
            node.right = self.delete_node(node.right, node.data)
        else:
            if node.left is not None:
                node = node.left
            elif node.right is not None:
                node = node.right
            else:
                node = None

        return node

    def delete(self, value):
        """
        Deletes the node with value from tree.
        """
        self.root = self.delete_node(self.root, value)

    def inorder(self, node):
        """
        Prints inorder from node.
        """
        if node is not None:
            self.inorder(node.left)
            print(node.data, end=" ")
            self.inorder(node.right)

    def inorder_from_root(self):
        """
        Prints inorder from root.
        """
        self.inorder(self.root)
        print()

    def to_list(self, node):
        if node is not None:
            for i in self.to_list(node.left):
                yield i
            yield node.data
            for i in self.to_list(node.right):
                yield i

    def to_list_from_root(self):
        return list(self.to_list(self.root))

