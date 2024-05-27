class Solution:
    
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        max_num = max(nums)
        B = max_num.bit_length()

        size = 1 << B
        dp = [0] * size
        
        for num in nums:
            dp[num] = num
        
        # 1. SOS algorithm
        for i in range(B):
            for num in range(size):
                if num & (1 << i):
                    # 2. built-in max is replaced by directly compare
                    if dp[num ^ (1 << i)] > dp[num]:
                        dp[num] = dp[num ^ (1 << i)]
        
        ans = 0
        ALL = (1 << B) - 1
        for x in nums:
            cur_product = x * dp[x ^ ALL]
            if cur_product > ans:
                ans = cur_product

        return ans if ans != -math.inf else 0