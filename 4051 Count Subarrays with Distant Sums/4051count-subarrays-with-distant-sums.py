class Solution:
    def distantSubarrays(self, nums: list[int], goal: int, k: int) -> int:
        n = len(nums)
        if k == 0:
            return n * (n + 1) // 2

        sl = SortedList([0])
        s = res = 0

        for x in nums:
            s += x
            res += sl.bisect_right(s - goal - k)
            res += len(sl) - sl.bisect_left(s - goal + k)
            sl.add(s)

        return res