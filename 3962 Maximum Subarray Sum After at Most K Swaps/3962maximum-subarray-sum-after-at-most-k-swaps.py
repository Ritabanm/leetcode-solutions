from typing import List
import heapq

class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        n = len(nums)

        # Base case: no swaps or single element → plain Kadane
        ans = -10**18
        if k == 0 or n == 1:
            sm = 0
            for x in nums:
                sm += x
                ans = max(ans, sm)
                if sm < 0:
                    sm = 0
            return ans

        cnt = 0
        cur_nonneg_sum = 0
        pref = [0] * (n + 1)

        for i in range(n):
            if nums[i] >= 0:
                cur_nonneg_sum += nums[i]
            else:
                cnt += 1
            pref[i + 1] = pref[i] + nums[i]
            ans = max(ans, nums[i])

        # If number of negatives ≤ k, we can fix all of them
        if cnt <= k:
            return cur_nonneg_sum

        # dp[i][j] = sum of up to k smallest negatives in [i..j],
        # but only updated when nums[j] >= 0 (matching C++ behavior)
        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            pq = []      # max-heap via negatives
            sm = 0
            for j in range(i, n):
                if nums[j] >= 0:
                    dp[i][j] = sm
                    continue

                if len(pq) < k:
                    heapq.heappush(pq, -nums[j])
                    sm += nums[j]
                else:
                    if -pq[0] > nums[j]:
                        sm -= -pq[0]
                        heapq.heapreplace(pq, -nums[j])
                        sm += nums[j]
                # dp[i][j] stays unchanged for negative nums[j]

        # Combine results
        for i in range(n):
            pqmax = []   # min-heap for up to k largest positives
            sm = 0

            # left side [0..i-1]
            for j in range(i):
                if nums[j] < 0:
                    continue
                if len(pqmax) < k:
                    heapq.heappush(pqmax, nums[j])
                    sm += nums[j]
                else:
                    if pqmax[0] < nums[j]:
                        sm -= pqmax[0]
                        heapq.heapreplace(pqmax, nums[j])
                        sm += nums[j]

            # right side [n-1..i+1]
            for j in range(n - 1, i, -1):
                cur = pref[j + 1] - pref[i]   # sum of subarray [i..j]
                cur -= dp[i][j]               # subtract selected negatives
                cur += sm                     # add selected positives outside
                ans = max(ans, cur)

                if nums[j] < 0:
                    continue

                if len(pqmax) < k:
                    heapq.heappush(pqmax, nums[j])
                    sm += nums[j]
                else:
                    if pqmax[0] < nums[j]:
                        sm -= pqmax[0]
                        heapq.heapreplace(pqmax, nums[j])
                        sm += nums[j]

                if pqmax:
                    ans = max(ans, sm)

        return ans