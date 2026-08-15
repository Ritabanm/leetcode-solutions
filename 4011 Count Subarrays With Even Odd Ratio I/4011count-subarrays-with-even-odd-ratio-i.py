class Solution:
    def countRatioSubarrays(self, nums, a, b):
        n = len(nums)
        ans = 0
        for i in range(n):
            e_count = 0
            o_count = 0
            for j in range(i,n):
                if nums[j]%2==0:
                    e_count+=1
                else:
                    o_count+=1
                if o_count>0 and e_count*b<=o_count*a:
                    ans+=1
        return ans