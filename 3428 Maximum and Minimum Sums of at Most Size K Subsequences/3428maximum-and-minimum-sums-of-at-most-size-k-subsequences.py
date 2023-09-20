from typing import List

class Solution:
    def minMaxSums(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        # Precompute combination values
        comb = [[0] * (k + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            comb[i][0] = 1
            for j in range(1, min(i, k) + 1):
                comb[i][j] = (comb[i - 1][j - 1] + comb[i - 1][j]) % MOD
        
        # Sort the array
        nums.sort()
        total = 0
        
        # Calculate contributions of each element as min and max
        for i in range(n):
            for r in range(1, k + 1):
                if r > n:
                    break
                
                # Contribution as the minimum
                min_contribution = comb[n - 1 - i][r - 1]
                total = (total + (nums[i] * min_contribution) % MOD) % MOD
                
                # Contribution as the maximum
                max_contribution = comb[i][r - 1]
                total = (total + (nums[i] * max_contribution) % MOD) % MOD

        return total