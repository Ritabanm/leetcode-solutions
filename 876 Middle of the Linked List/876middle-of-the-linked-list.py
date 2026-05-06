class Solution:
    def middleNode(self, head):
        if not head:
            return None
        
        f = s = head

        while f and f.next:
            s = s.next
            f = f.next.next
        return s