"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""
class Node:
    def __init__(self, val: int, next: 'Node' = None):
        self.val = val
        self.next = next

class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        new_node = Node(insertVal)

        # Case 1: Empty list
        if not head:
            new_node.next = new_node
            return new_node

        # Case 2: Inserting in a non-empty list
        prev, curr = head, head.next
        while True:
            # Normal insertion between prev and curr
            if prev.val <= insertVal <= curr.val:
                break

            # Handle circular wrap-around case
            if prev.val > curr.val:
                if insertVal >= prev.val or insertVal <= curr.val:
                    break

            prev, curr = curr, curr.next

            # Full loop: all nodes are the same
            if prev == head:
                break

        # Insert new_node between prev and curr
        prev.next = new_node
        new_node.next = curr

        return head

