"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        cur = root  # Start at the root of the tree

        while cur.left:  # Process each level as long as there are child nodes
            nxt = cur.left  # The first node of the next level
            
            while cur:  # Process all nodes in the current level
                cur.left.next = cur.right  # Connect the left child to the right child
                
                if cur.next:  # If there's a next node, connect the right child to the left child of the next node
                    cur.right.next = cur.next.left
                
                cur = cur.next  # Move to the next node in the current level
            
            cur = nxt  # Move down to the next level

        return root
