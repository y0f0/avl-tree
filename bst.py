class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.height = 1


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

    def insert_node(self, root, key):

        if not root:
            return Node(key)
        elif key < root.data:
            root.left = self.insert_node(root.left, key)
        else:
            root.right = self.insert_node(root.right, key)

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        balance = self.getBalance(root)

        if balance > 1 and key < root.left.data:
            return self.rightRotate(root)

        if balance < -1 and key > root.right.data:
            return self.leftRotate(root)

        if balance > 1 and key > root.left.data:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        if balance < -1 and key < root.right.data:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    def insert(self, value):
        """
        Inserts a new node that contains the given value into the tree at the correct location.
        """
        self.root = self.insert_node(self.root, value)

    def delete_node(self, root, key):

        if not root:
            return root

        elif key < root.data:
            root.left = self.delete_node(root.left, key)

        elif key > root.data:
            root.right = self.delete_node(root.right, key)

        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp

            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self.getMinValueNode(root.right)
            root.data = temp.data
            root.right = self.delete_node(root.right, temp.data)

        if root is None:
            return root

        root.height = 1 + max(self.getHeight(root.left),
                            self.getHeight(root.right))

        balance = self.getBalance(root)

        if balance > 1 and self.getBalance(root.left) >= 0:
            return self.rightRotate(root)

        if balance < -1 and self.getBalance(root.right) <= 0:
            return self.leftRotate(root)

        if balance > 1 and self.getBalance(root.left) < 0:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        if balance < -1 and self.getBalance(root.right) > 0:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    def delete(self, value):
        """
        Deletes the node with value from tree.
        """
        self.root = self.delete_node(self.root, value)

    def leftRotate(self, z):

        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.getHeight(z.left),
                         self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                         self.getHeight(y.right))

        return y

    def rightRotate(self, z):

        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.getHeight(z.left),
                          self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                          self.getHeight(y.right))

        return y

    def getHeight(self, root):
        if not root:
            return 0

        return root.height

    def getBalance(self, root):
        if not root:
            return 0

        return self.getHeight(root.left) - self.getHeight(root.right)

    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root

        return self.getMinValueNode(root.left)

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

