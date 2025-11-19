class Solution:
    def countSubranges(self, nums1, nums2):
        n, mod = len(nums1), 10**9+7 

        @lru_cache(None)
        def function(i,total):
            if i >= n:
                return total == 0 

            res = 0 

            if total == 0:
                res += 1 

            res += function(i+1,total+nums1[i]) + function(i+1,total-nums2[i])

            return res 
        
        return sum([function(i+1,nums1[i]) + function(i+1,-nums2[i]) for i in range(n)])%mod