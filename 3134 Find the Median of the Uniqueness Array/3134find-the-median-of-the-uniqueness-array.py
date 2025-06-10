class Solution:
    def medianOfUniquenessArray(self, nums: List[int]) -> int:
        def count_subarrays(nums, mid): 
            ans = ii = 0 
            seen = defaultdict(int)
            for i, x in enumerate(nums): 
                seen[x] += 1
                while ii <= i and len(seen) > mid: 
                    seen[nums[ii]] -= 1
                    if seen[nums[ii]] == 0: seen.pop(nums[ii])
                    ii += 1
                ans += i - ii + 1
            return ans 
        
        n = len(nums)
        lo, hi = 0, n
        while lo < hi: 
            mid = (lo + hi) // 2
            if count_subarrays(nums, mid) < (n * (n + 1) // 2 + 1) // 2: 
                lo = mid + 1
            else: 
                hi = mid 
        return lo