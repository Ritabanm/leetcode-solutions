class Solution:
    def minSwaps(self, nums: List[int], forbidden: List[int]) -> int:
        n = len(nums)
    
        # 1. Feasibility Check: Can we even place all these numbers?
        # Total count of value X + count of spots where X is forbidden <= Total size
        nums_counts = Counter(nums)
        forb_counts = Counter(forbidden)
        
        # We only care about values present in nums
        for val, count in nums_counts.items():
            if count + forb_counts[val] > n:
                return -1
                
        # 2. Count "Bad" indices (where nums[i] == forbidden[i])
        bad_values = []
        for i in range(n):
            if nums[i] == forbidden[i]:
                bad_values.append(nums[i])
        
        K = len(bad_values)
        if K == 0:
            return 0
            
        # 3. Calculate max frequency among conflict values
        bad_counts = Counter(bad_values)
        max_freq = max(bad_counts.values())
        
        # Apply the math-based result
        # (K + 1) // 2 is the same as ceil(K/2)
        return max((K + 1) // 2, max_freq)