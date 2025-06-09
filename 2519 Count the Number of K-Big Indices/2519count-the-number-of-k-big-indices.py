from sortedcontainers import SortedList
class Solution:
    def kBigIndices(self, nums: List[int], k: int) -> int:
        seen = SortedList()
        from_left = []
        for x in nums:
            from_left.append(seen.bisect_left(x))
            seen.add(x)
        seen = SortedList()
        from_right = []
        for x in reversed(nums):
            from_right.append(seen.bisect_left(x))
            seen.add(x)
        from_right = from_right[::-1]

        ans = 0
        for i in range(len(nums)):
            if from_left[i] >= k and from_right[i] >= k:
                ans += 1
        return ans