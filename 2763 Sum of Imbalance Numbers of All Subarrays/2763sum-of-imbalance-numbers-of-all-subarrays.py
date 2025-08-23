class Solution:
    def sumImbalanceNumbers(self, nums: List[int]) -> int:
        # O(n) time complexity and O(n) space complexity
        n = len(nums)
        latest = {}
        smaller_stk = []
        m1_lst = [0] * n
        k1_lst = [0] * n
        for i, num in enumerate(nums):
            k1_lst[i] = max(latest.get(num, -1), latest.get(num - 1, -1))
            while smaller_stk and smaller_stk[-1][1] >= num:
                smaller_stk.pop()
            m1_lst[i] = max(smaller_stk[-1][0], k1_lst[i])\
                            if smaller_stk else k1_lst[i]
            smaller_stk.append((i, num))
            latest[num] = i
        res = 0
        soonest = {}
        smaller_stk = []
        for i in reversed(range(n)):
            num = nums[i]
            k2 = soonest.get(num - 1, n)
            while smaller_stk and smaller_stk[-1][1] >= num:
                smaller_stk.pop()
            m2 = min(smaller_stk[-1][0], k2) if smaller_stk else k2
            smaller_stk.append((i, num))
            soonest[num] = i
            res += (i - k1_lst[i]) * (k2 - i) -\
                    (i - m1_lst[i]) * (m2 - i)
        return res
            