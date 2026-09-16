class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        minimum = inf
        allowed = []
        for i in range(x, len(nums)):
            insort(allowed, nums[i-x])
            at = bisect_left(allowed, nums[i])
            if at > 0:
                minimum = min(minimum, nums[i] - allowed[at-1])
            if at < len(allowed):
                minimum = min(minimum, allowed[at] - nums[i])
        return minimum