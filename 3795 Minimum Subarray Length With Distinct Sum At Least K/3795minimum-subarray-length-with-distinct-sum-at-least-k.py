class Solution:
    def minLength(self,nums,k):
        tot = 0
        seen = defaultdict(int)
        l = 0
        min_len = inf
        for r in range(len(nums)):
            seen[nums[r]]+=1
            if seen[nums[r]]==1:
                tot+=nums[r]
            while tot>=k:
                min_len = min(min_len, r-l+1)
                seen[nums[l]]-=1
                if seen[nums[l]]==0:
                    del seen[nums[l]]
                    tot-=nums[l]
                l+=1
        return min_len if min_len!=inf else -1