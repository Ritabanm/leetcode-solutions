class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        n = len(nums)
        peakCount = [0] * n
        ans = 0
        for i in range(n):
            smaller = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    smaller += 1
                    ans += peakCount[j]
                else:
                    peakCount[j] += smaller
        return ans