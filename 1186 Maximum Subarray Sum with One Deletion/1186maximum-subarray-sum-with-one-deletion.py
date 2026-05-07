class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        # summation with possible skips
        skip = nums[0]
        # summation without skips
        noskip = nums[0]
        # holder for maximal value
        maxv = nums[0]
        for num in nums[1:]:
            # reset skip if negative
            if skip < 0: skip = 0
            # if num is positive just add. otherwise take the maximum between adding it,
            # and skipping it - represented by noskip that currently is on previous position
            skip = skip + num if num >= 0 else max(skip + num, noskip) 
            # reset noskip if negative
            if noskip < 0: noskip = 0
            # always add
            noskip += num                
            # track maximum
            maxv = max(maxv, noskip, skip)

        return maxv            
    