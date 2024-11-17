class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode):
        if not root:
            return []

        def isLeaf(node):
            return node.left is None and node.right is None

        def addLeftBoundary(node):
            while node:
                if not isLeaf(node):
                    boundary.append(node.val)
                node = node.left if node.left else node.right

        def addRightBoundary(node):
            stack = []
            while node:
                if not isLeaf(node):
                    stack.append(node.val)
                node = node.right if node.right else node.left
            # Add the right boundary in reverse order
            while stack:
                boundary.append(stack.pop())

        def addLeaves(node):
            if isLeaf(node):
                boundary.append(node.val)
                return
            if node.left:
                addLeaves(node.left)
            if node.right:
                addLeaves(node.right)

        # Initialize boundary with root value
        boundary = [root.val] if not isLeaf(root) else []

        # Add left boundary
        if root.left:
            addLeftBoundary(root.left)

        # Add leaves
        addLeaves(root)

        # Add right boundary
        if root.right:
            addRightBoundary(root.right)

        return boundary
