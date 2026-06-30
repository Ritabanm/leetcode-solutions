class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        init = float('inf')

        def helper_multiply():
            start = mid = finish = -init
            ans = -init
            for val in nums:
                new_start = max(start + val, val)
                new_mid = max(start + val*k, mid + val*k, val*k)
                new_finish = max(mid + val, finish + val, val)
                start, mid, finish = new_start, new_mid, new_finish
                ans = max(ans, start, mid, finish)
            return ans

        def helper_divide():
            def divider(x):
                if x >= 0:
                    return x // k
                else:
                    return -((-x) // k)

            start = mid = finish = -init
            ans = -init

            for val in nums:
                new_val = divider(val)

                new_start = max(start + val, val)
                new_mid = max(start + new_val, mid + new_val, new_val)
                new_finish = max(mid + val, finish + val, val)

                start, mid, finish = new_start, new_mid, new_finish
                ans = max(ans, start, mid, finish)

            return ans

        return max(helper_multiply(), helper_divide())
        