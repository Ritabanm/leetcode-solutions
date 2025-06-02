class Solution:
    def checkArray(self, nums: List[int], k: int) -> bool:
        curr=0
        for i,a in enumerate(nums):
            if curr>a:
                return False

            nums[i],curr=a-curr,a
            if i>=k-1:
                curr-=nums[i-k+1]

        return curr==0            