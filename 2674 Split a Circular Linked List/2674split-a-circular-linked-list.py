class Solution:
    def splitCircularLinkedList(self, list: ListNode) -> List[ListNode]:
        
        slow = fast = list

        while fast.next != list and fast.next.next != list: # find the snip nodes
             slow, fast = slow.next, fast.next.next

        if fast.next.next == list: fast = fast.next         # account for even-length list

        fast.next, slow.next = slow. next, list             # patch the circular lists

        return [list, fast.next]                            # return the heads