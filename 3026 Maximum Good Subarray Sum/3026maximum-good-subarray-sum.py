class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        ans = -inf

        prefix_sum = 0
        seen = defaultdict(lambda: inf)
        for n in nums:
            seen[n] = min(seen[n], prefix_sum)
            
            prefix_sum += n

            ans = max(ans, prefix_sum - seen[k + n], \
                           prefix_sum - seen[n - k])
                
        return ans if ans != -inf else 0