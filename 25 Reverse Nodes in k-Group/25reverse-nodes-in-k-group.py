class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # Step 1: Count total nodes
        def countNodes(node):
            count = 0
            while node:
                count += 1
                node = node.next
            return count
        
        total_nodes = countNodes(head)
        
        # Step 2: Reverse k-group nodes
        dummy = ListNode(0)
        dummy.next = head
        prev_group_end = dummy
        curr = head
        
        while total_nodes >= k:
            prev = None
            tail = curr
            
            # Reverse k nodes
            for _ in range(k):
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            
            # Connect reversed group to previous group
            prev_group_end.next = prev
            tail.next = curr  # Connect end of reversed group to remaining list
            
            # Move prev_group_end forward for next group
            prev_group_end = tail
            total_nodes -= k
        
        return dummy.next
