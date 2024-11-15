class Solution:
    def numberOfWays(self, n: int, limit: List[int]) -> int:
        # 1. Identify critical points where S(x) or S(n-x) changes
        nums = set([0, 1, n-1, n])
        for val in limit:
            if val < n:
                nums.add(val)
                nums.add(val + 1)
                nums.add(n - val)
                nums.add(n - val - 1)
        
        nums = sorted(list(nums))
        mapping = {num: i for i, num in enumerate(nums)}
        
        # 2. Precompute suffix sums to find S(k) in O(1)
        # count[i] stores the number of colors with limit >= nums[i]
        count = [0] * len(nums)
        for val in limit:
            count[mapping[min(val, n)]] += 1
            
        for i in range(len(count) - 2, -1, -1):
            count[i] += count[i + 1]
            
        ans = 0
        mod = 10**9 + 7
        
        # 3. Iterate through intervals [nums[i-1], nums[i])
        for i in range(1, len(nums) - 1):
            # Calculate S(x) and S(n-x) for this interval
            # The current x-range is [nums[i-1], nums[i]-1]
            # S(x) is constant at count[i]
            c1 = count[i] 
            
            # Find the index for n-x. 
            # When x = nums[i], n-x = n - nums[i]
            j = mapping[n - nums[i]]
            c2 = count[j]
            
            # Ways = S(x)*S(n-x) - min(S(x), S(n-x))
            ways_per_split = (c1 * c2 - min(c1, c2))
            
            # Multiply by the number of split points in this interval
            interval_len = nums[i] - nums[i-1]
            ans = (ans + interval_len * ways_per_split) % mod
            
        return ans