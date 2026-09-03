"""class Solution:
    def reverseList(self, head):
        if not head:
            return None
        prev = None
        curr = head
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        return prev"""
class Solution:
    def reverseList(self, head):
        if not head:
            return None
        prev = None
        curr = head
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        return prev