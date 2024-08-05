class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        sub_arr, l, cur_sum, ans  = set(), 0, 0, 0
        for r in range(len(nums)):
            while nums[r] in sub_arr:     # deleting duplciate of nums[r], if already exists 
                sub_arr.remove(nums[l])
                cur_sum -= nums[l]
                l += 1
            sub_arr.add(nums[r])          # pick nums[r]
            cur_sum += nums[r]            # update current sub-array sum
            ans = max(ans, cur_sum)       # update ans to hold max of all sub-array sums till now
        return ans