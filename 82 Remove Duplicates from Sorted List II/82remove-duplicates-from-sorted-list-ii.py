class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        #sentinel
        sentinel = ListNode(0,head)

        pred = sentinel

        while head:
            if head.next and head.val == head.next.val:
                #move till end of duplicates
                while head.next and head.val == head.next.val:
                    head = head.next

                #Skip duplicates
                pred.next = head.next
            else:
                pred = pred.next

            head = head.next 
    
        return sentinel.next