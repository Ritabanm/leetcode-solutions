mx = lambda x, y: x if x > y else y

class Solution:
    def longestBalanced(self, nums: List[int]) -> int:

        n, left, ans = len(nums), 0, -1

        for left in range(n):
            if left >= n - ans: break
            oddsEvn = {0: set(), 1: set()}

            for rght, num in enumerate(nums[left:]):
                oddsEvn[num % 2].add(num)

                if len(oddsEvn[0]) == len(oddsEvn[1]):
                    ans = mx(ans, rght)

        return ans + 1