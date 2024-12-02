class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:        
        q = []
        n = len(nums1)
        ans = 0
        for i in reversed(range(n)):            
            cur = nums1[i] - nums2[i] - diff
            loc = bisect.bisect_left(q, cur)
            ans += len(q) - loc
            bisect.insort(q, cur + diff)           
        return ans