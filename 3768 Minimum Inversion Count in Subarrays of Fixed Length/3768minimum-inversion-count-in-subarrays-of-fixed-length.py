class Solution:
    def minInversionCount(self, nums: List[int], k: int) -> int:
        if k ==1 :
            return 0
        
        win = SortedList()
        inversions = 0
        for i in range(k):
            to_add =len(win)-win.bisect_right(nums[i])
            inversions+=to_add
            win.add(nums[i])
        
        res = inversions
        for i in range(k, len(nums)):
            out = nums[i-k]
            to_sub = win.bisect_left(out)
            inversions-=to_sub
            win.remove(out)

            inc = nums[i]
            to_add = len(win)-win.bisect_right(inc)
            inversions+=to_add
            win.add(inc)
            res = min(res, inversions)
        return res