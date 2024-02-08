class Solution:
    def scoreDifference(self, nums: List[int]) -> int:
        d = 0
        c = 1
        for i,v in enumerate(nums):
            if v%2!=0:
                c*=-1
            if (i+1)%6==0:
                c*=-1
            d+=v*c
        return d