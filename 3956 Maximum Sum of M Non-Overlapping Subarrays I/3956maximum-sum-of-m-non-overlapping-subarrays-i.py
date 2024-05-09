class Solution:
    def maximumSum(self, nums: List[int], m: int, l: int, r: int) -> int:
        NEG = -4 * 10**18
        n = len(nums)

        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + nums[i]

        prev_dp = [0] * (n + 1)
        curr_dp = [NEG] * (n + 1)

        ans = NEG

        for take in range(1, m + 1):
            curr_dp = [NEG] * (n + 1)

            dq = deque()

            for i in range(1, n + 1):
                curr_dp[i] = curr_dp[i - 1]
                pos = i - l

                if pos >= 0:

                    val = prev_dp[pos] - pref[pos]

                    while dq:
                        last = dq[-1]
                        if prev_dp[last] - pref[last] >= val:
                            break
                        dq.pop()

                    dq.append(pos)

                while dq and dq[0] < i - r:
                    dq.popleft()

                if dq:
                    start = dq[0]
                    candidate =prev_dp[start]-pref[start]+pref[i]
                    curr_dp[i] = max(curr_dp[i], candidate)

            ans = max(ans, curr_dp[n])

            prev_dp, curr_dp = curr_dp, prev_dp

        return ans