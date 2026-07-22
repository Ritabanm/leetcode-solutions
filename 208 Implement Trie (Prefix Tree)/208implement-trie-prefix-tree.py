class Node():

    def __init__(self, value: str):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree():

    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insertRecursive(self.root, Node(value))

    def _insertRecursive(self, current_node, inserting_node):
        if inserting_node.value < current_node.value:
            if current_node.left is None:
                current_node.left = inserting_node
            else:
                self._insertRecursive(current_node.left, inserting_node)
        else:
            if current_node.right is None:
                current_node.right = inserting_node
            else:
                self._insertRecursive(current_node.right, inserting_node)

    def find(self, value):
        return self._findRecursive(self.root, value)

    def _findRecursive(self, node, value):
        if node is None:
            return False
        if node.value == value:
            return True
        elif value < node.value:
            return self._findRecursive(node.left, value)
        else:
            return self._findRecursive(node.right, value)

    def findPrefix(self, prefix):
        return self._findPrefixRecursive(self.root, prefix)

    def _findPrefixRecursive(self, node, prefix):
        if node is None:
            return False
        if node.value.startswith(prefix):
            return True
        elif node.value > prefix:
            return self._findPrefixRecursive(node.left, prefix)
        else:
            return self._findPrefixRecursive(node.right, prefix)


class Trie(object):

    def __init__(self):
        self.tree = BinaryTree()

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        self.tree.insert(word)

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return self.tree.find(word)

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        return self.tree.findPrefix(prefix)