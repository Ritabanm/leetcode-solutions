"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        
        self.first = None
        self.last = None
        
        self.inorder_link(root)
        
        # Connect the first and last nodes to make it circular
        self.first.left = self.last
        self.last.right = self.first
        
        return self.first
    
    def inorder_link(self, node):
        if node:
            # Traverse the left subtree
            self.inorder_link(node.left)
            
            # Process the current node
            if not self.last:
                # This is the first node
                self.first = node
            else:
                # Link the previous node (self.last) with the current node
                node.left = self.last
                self.last.right = node
            
            # Update self.last to the current node
            self.last = node
            
            # Traverse the right subtree
            self.inorder_link(node.right)
