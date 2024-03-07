class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        MODS = (10**9 + 7, 10**9 + 9)
        BASES = (100237, 199777)
        
        def has_unique(L: int) -> bool:
            if L == 0: return False
            
            # Precompute base^L % mod
            p1, p2 = pow(BASES[0], L, MODS[0]), pow(BASES[1], L, MODS[1])
            
            # Compute initial window hashes
            h1, h2 = 0, 0
            for x in nums[:L]:
                h1 = (h1 * BASES[0] + x) % MODS[0]
                h2 = (h2 * BASES[1] + x) % MODS[1]
                
            # Slide window and record hash frequencies
            counts = Counter([(h1, h2)])
            for i in range(L, n):
                h1 = (h1 * BASES[0] + nums[i] - nums[i - L] * p1) % MODS[0]
                h2 = (h2 * BASES[1] + nums[i] - nums[i - L] * p2) % MODS[1]
                counts[(h1, h2)] += 1
                
            # If any hash value has a frequency of exactly 1, a unique subarray exists
            return 1 in counts.values()

        # Binary search for the minimum working length
        low, high = 1, n
        while low < high:
            mid = (low + high) // 2
            if has_unique(mid):
                high = mid
            else:
                low = mid + 1
        return low
        