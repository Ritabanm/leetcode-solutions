class Solution:
    def missingMultiple(self, nums: list[int], k: int) -> int:
        num_set = set(nums)
        i = 1
        while True:
            if k * i not in num_set:
                return k * i
            i += 1