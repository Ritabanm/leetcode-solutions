class Solution:
    def postorderTraversalHelper(self, currentNode, result):
        # Base case: if the node is null, return
        if not currentNode:
            return
        # Traverse left subtree
        self.postorderTraversalHelper(currentNode.left, result)
        # Traverse right subtree
        self.postorderTraversalHelper(currentNode.right, result)
        # Add the current node's value to the result list
        result.append(currentNode.val)

    def postorderTraversal(self, root):
        result = []
        # Start traversal from root
        self.postorderTraversalHelper(root, result)
        return result