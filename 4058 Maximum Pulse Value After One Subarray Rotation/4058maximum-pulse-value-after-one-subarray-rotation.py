class Solution:
    def maxValue(self, nums: List[int]) -> int:

        prefSum, parity = 0, 0
        mn, mx = 0, [0, -inf]
        nums[1::2] = [-num for num in nums[1::2]]

        for num in nums:
            parity^= 1
            prefSum+= num
            mn = min(mn, prefSum - mx[parity])
            mx[parity] = max(mx[parity], prefSum)

        ans = prefSum - mn - mn    
        return ans