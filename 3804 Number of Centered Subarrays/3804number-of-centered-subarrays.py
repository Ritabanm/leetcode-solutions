class Solution:
    def centeredSubarrays(self, nums: List[int]) -> int:

        n, seen, ans = len(nums), set(), 0

        for i in range(n):
            sm = 0

            for j in range(i, n):
                sm+= nums[j]
                seen.add(nums[j])
                ans+= sm in seen
            seen.clear()
        return ans