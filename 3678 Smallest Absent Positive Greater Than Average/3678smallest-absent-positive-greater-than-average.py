class Solution:
    def smallestAbsent(self, nums: List[int], mx = 102) -> int:

        mean = int(sum(nums) / len(nums)) + 1       # <-- 1)
        initial = mean if mean > 1 else 1

        for num in range(initial, mx):              # <-- 2)
            if num in nums: continue
            return num