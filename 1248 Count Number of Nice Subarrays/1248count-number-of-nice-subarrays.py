class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        curr_sum = 0
        subarray = 0
        prefix_sum = {curr_sum:1}

        for i in range(len(nums)):
            curr_sum+=nums[i]%2
            #Find sub-array with sum k end at i.
            if curr_sum-k in prefix_sum:
                subarray = subarray+prefix_sum[curr_sum-k]
            prefix_sum[curr_sum]=prefix_sum.get(curr_sum,0)+1
        return subarray