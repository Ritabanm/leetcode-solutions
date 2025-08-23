# Definition for BigArray.
# class BigArray:
#     def at(self, index: long) -> int:
#         pass
#     def size(self) -> long:
#         pass
class Solution(object):
    def __init__(self):
        self.num = 2

    def countBlocks(self, nums: Optional['BigArray']) -> int:
        start = 0
        end = nums.size() - 1
        startval = nums.at(start)
        endval = nums.at(end)
        if (startval == endval):
            return 1
        self.countBlocksRecurse(nums, start, end, startval, endval)
        return self.num
        
    def countBlocksRecurse(self, nums, start, end, startval, endval):
        if (end - start <= 1):
            return
        mid = (start + end) // 2
        midval = nums.at(mid)
        if midval != startval:
            self.countBlocksRecurse(nums, start, mid, startval, midval)
        if midval != endval:
            self.countBlocksRecurse(nums, mid, end, midval, endval)
        if (midval != startval and midval != endval):
            self.num += 1