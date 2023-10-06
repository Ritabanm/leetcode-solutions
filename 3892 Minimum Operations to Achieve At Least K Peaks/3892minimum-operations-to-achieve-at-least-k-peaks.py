class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        n = len(nums)
        
        # 1. Base Case: Zero peaks required
        if k == 0:
            return 0
        
        # 2. Impossible Case: Cannot have more than n//2 non-adjacent peaks
        # For n=1, max peaks is 0. For n=2, max peaks is 1.
        if k > n // 2 or (n == 1 and k > 0):
            return -1

        # 3. Precompute cost to make each index i a peak based on original neighbors
        # This is safe because we only pick non-adjacent indices as peaks.
        costs = []
        for i in range(n):
            left = nums[(i - 1) % n]
            right = nums[(i + 1) % n]
            costs.append(max(0, max(left, right) + 1 - nums[i]))

        def solve_linear(arr, target_k):
            """Standard DP to find min cost for target_k non-adjacent elements in arr."""
            m = len(arr)
            if target_k <= 0: return 0
            if target_k > (m + 1) // 2: return float('inf')

            # Space-optimized DP: prev1 is dp[i-1], prev2 is dp[i-2]
            prev2 = [0] + [float('inf')] * target_k
            prev1 = [0] + [float('inf')] * target_k
            curr = [0] + [float('inf')] * target_k

            for i in range(1, m + 1):
                cost = arr[i-1]
                # Optimization: j only needs to go up to max possible peaks in first i items
                limit = min(target_k, (i + 1) // 2)
                for j in range(1, limit + 1):
                    # Option 1: Don't pick current index i (inherit from prev1)
                    # Option 2: Pick current index i (cost + dp from i-2)
                    v1 = prev1[j]
                    v2 = prev2[j-1] + cost
                    curr[j] = v1 if v1 < v2 else v2
                
                # Reset values beyond limit for next iterations
                for j in range(limit + 1, target_k + 1):
                    curr[j] = float('inf')
                
                # Rotate pointers for space optimization
                prev2, prev1, curr = prev1, curr, prev2
                
            return prev1[target_k]

        # 4. Handle Circularity via two linear DP scenarios
        # Scenario A: Index 0 is NOT a peak. Pick k peaks from indices [1...n-1].
        res1 = solve_linear(costs[1:], k)

        # Scenario B: Index 0 IS a peak. 
        # This forces index 1 and index n-1 to NOT be peaks.
        # Pick k-1 peaks from the remaining valid indices [2...n-2].
        res2 = costs[0] + solve_linear(costs[2:-1], k - 1)

        ans = min(res1, res2)
        return int(ans) if ans != float('inf') else -1



