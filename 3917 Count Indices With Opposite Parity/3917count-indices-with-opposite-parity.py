class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:
        ans=[]
        n=len(nums)
        for i in range(n-1):
            count=0
            if nums[i]%2==0:
                for j in range(i+1,n):
                    if nums[j]%2==1:
                        count+=1
            else:
                for j in range(i+1,n):
                    if nums[j]%2==0:
                        count+=1
            ans.append(count)
        ans.append(0)
        return ans               