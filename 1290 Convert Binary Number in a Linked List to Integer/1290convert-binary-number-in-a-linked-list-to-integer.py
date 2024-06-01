class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        num = head.val
        while head.next:
            num = num*2 + head.next.val
            head= head.next
        return num