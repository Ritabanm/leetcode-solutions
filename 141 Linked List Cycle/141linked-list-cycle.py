"""
class Solution:
    def hasCycle(self, head):
        if not head:
            return None
        
        slow = head
        fast = head.next
        while slow!=fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True"""

class Solution:
    def hasCycle(self, head):
        if not head:
            return None
        slow = head
        fast = head.next
        while slow!=fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True