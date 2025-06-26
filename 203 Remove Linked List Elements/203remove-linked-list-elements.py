class Solution:
    def removeElements(self, head, val):
        if not head:
            return None
        
        dummy = ListNode(0)
        curr = dummy
        dummy.next = head

        while curr and curr.next:
            if curr.next.val==val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return dummy.next