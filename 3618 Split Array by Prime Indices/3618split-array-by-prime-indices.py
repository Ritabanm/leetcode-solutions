class Solution:
    def splitArray(self, nums: List[int]) -> int:
        n, sm = len(nums), sum(nums)
        for i in range(2,n):
            if isinstance(nums[i], bool):
                continue
            for i in range(i*i, n, i):
                nums[i] = False
        return abs(2*sum(nums[2:])-sm)