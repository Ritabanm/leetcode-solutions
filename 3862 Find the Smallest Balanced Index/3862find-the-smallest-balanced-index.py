class Solution:
    def smallestBalancedIndex(self, nums: list[int]) -> int:
        n,l,r = len(nums), sum(nums),1
        for i in range(n-1,-1,-1):
            l-=nums[i]
            if l>r:
                r*=nums[i]
            elif l<r:
                break
            else:
                return i
        return -1