class Solution:
    def makeArrayPositive(self, nums: List[int]) -> int:
        cnt = 0
        lo = sum(nums[:2]) # maintain the lowest subarray sum seen so far
        for i in range(2, len(nums)):
            val = nums[i]
            curr_triplet = val + nums[i-1] + nums[i-2]
            lo = min(lo + val, curr_triplet)
            if lo <= 0:
                nums[i] = lo = 10**18
                cnt += 1
        return cnt