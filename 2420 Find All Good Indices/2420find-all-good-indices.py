class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        inc = list(accumulate((n2 > n1 for n1, n2 in zip(nums, nums[1:])), initial = 0))
        dec = list(accumulate((n2 < n1 for n1, n2 in zip(nums, nums[1:])), initial = 0))
        return [i for i in range(k, len(nums) - k) if inc[i - 1] == inc[i - k] and dec[i + k] == dec[i + 1]]