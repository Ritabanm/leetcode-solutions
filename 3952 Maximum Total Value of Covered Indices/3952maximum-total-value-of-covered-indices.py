class Solution:
    def maxTotal(self, nums: List[int], s: str) -> int:


        prev = None
        ans = 0

        @cache
        def dp(i, prev):

            if i >= len(nums):
                return 0

            ans = 0
            if prev == None:
                if s[i] == "1":
                    ans = nums[i] + dp(i + 1, prev)
                else:
                    ans = dp(i + 1, i)
            else:
                if s[i] == "0":
                    ans = dp(i + 1, i)
                else:
                    ans = max(ans, nums[prev] + dp(i + 1, i))
                    ans = max(ans, nums[i] + dp(i + 1, None))

            return ans

        return (dp(0, None))