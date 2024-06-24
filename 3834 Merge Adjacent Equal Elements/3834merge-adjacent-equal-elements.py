class Solution:
    def mergeAdjacent(self, nums: List[int]) -> List[int]:
        s = []
        for num in nums:
            while s and s[-1]==num:
                num+=s.pop()
            s.append(num)
        return s