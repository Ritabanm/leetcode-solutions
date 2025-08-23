from collections import defaultdict

class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        n = len(nums)
        pos = nums.index(k)
        counts = defaultdict(int)
        balance = 0
        counts[0] = 1
        for i in range(pos - 1, -1, -1):
            balance += 1 if nums[i] > k else -1
            counts[balance] += 1
        cnt = 0
        balance = 0
        for i in range(pos, n):
            if nums[i] > k:
                balance += 1
            elif nums[i] < k:
                balance -= 1
            cnt += counts[-balance] + counts[1 - balance]
        return cnt