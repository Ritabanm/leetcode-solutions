class Solution:
    def minimumIncompatibility(self, nums, k):
        length = len(nums)//k
        
        @lru_cache(None)
        def dfs(nums):
            if not nums: return 0
            
            min_val = float("inf")
            
            for i in itertools.combinations(nums,length):
                if len(set(i)) < length: continue
                    
                new_nums = list(nums)
                
                for j in i:
                    new_nums.remove(j)
                    
                min_val = min(min_val,max(i)-min(i)+dfs(tuple(new_nums)))
                
            return min_val
        
        result = dfs(tuple(nums))
        
        return result if result != float("inf") else -1

            
        
        
