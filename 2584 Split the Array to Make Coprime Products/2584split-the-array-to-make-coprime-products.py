class Solution:
    def findValidSplit(self, nums: List[int]) -> int:
        ans = 0
        for i, a in enumerate(nums[:-1]):
            for j, b in enumerate(nums[ans:], ans):
                if gcd(a, b) != 1:
                    ans = j
            if i == ans:
                return ans
        return -1