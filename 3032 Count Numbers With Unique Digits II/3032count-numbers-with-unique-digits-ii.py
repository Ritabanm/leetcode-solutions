class Solution:
    def numberCount(self, a: int, b: int) -> int:

        dp = {}

        for i in range(a, b + 1):
            number = str(i)
            is_unique = len(number) == len(set(number))

            count = 0 if not is_unique else 1

            if i == a:
                dp[i] = count
            else:
                dp[i] = dp[i-1] + count


        return dp[b]


        