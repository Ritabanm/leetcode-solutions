from collections import Counter

class Solution:
    def findLonely(self, nums: list[int]) -> list[int]:
        freq = Counter(nums)
        ans = []
        for x in nums:
            if freq[x] == 1 and x-1 not in freq and x+1 not in freq:
                ans.append(x)
        return ans