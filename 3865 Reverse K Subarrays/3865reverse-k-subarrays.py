class Solution:
    def reverseSubarrays(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        size = n//k
        stack = []
        for beg in range(0,n, size):
            for i in range(beg, beg+size):
                stack.append(nums[i])
            for j in range(beg, beg+size):
                nums[j] = stack.pop()
        return nums