class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        current = head
        values = []

        while current:
            values.append(current.val)
            current = current.next
        
        i = 0
        j = len(values)-1

        maxSum = 0
        while (i<j):
            maxSum = max(maxSum, values[i]+values[j])
            i = i+1
            j =j-1
        return maxSum