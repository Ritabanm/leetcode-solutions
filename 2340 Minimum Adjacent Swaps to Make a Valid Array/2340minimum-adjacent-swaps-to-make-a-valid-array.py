class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        mi = min(nums)                                     # find minimum
        idx1 = nums.index(mi)                              # locate the first mi from the left side
        
        nums = [nums[idx1]] + nums[:idx1] + nums[idx1+1:]  # make the swaps & update `nums`
        
        mx = max(nums)                                     # find maximum 
        idx2 = nums[::-1].index(mx)                        # locate the first mx from the right side
        return idx1 + idx2                                 # return total swaps needed