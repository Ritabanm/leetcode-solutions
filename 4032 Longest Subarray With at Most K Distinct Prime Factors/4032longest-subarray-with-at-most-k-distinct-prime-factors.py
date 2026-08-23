class Solution:
    def longestSubarray(self, nums, k):
        n = len(nums)

        
        def function(x):
            res = set()

            for d in range(2,int(math.sqrt(x))+1):
                while x > 1 and x%d == 0:
                    res.add(d)
                    x = x//d 

            if x > 1:
                res.add(x)

            return res 

        
        d = defaultdict(int)

        max_val, left = 0, 0 

        for right in range(n):
            f = function(nums[right])

            for e in f:
                d[e] += 1

            while left <= right and len(d) > k:
                f = function(nums[left])

                for e in f:
                    d[e] -= 1  

                    if d[e] == 0:
                        del d[e]

                left += 1 

            max_val = max(max_val,right-left+1)
            
        return max_val