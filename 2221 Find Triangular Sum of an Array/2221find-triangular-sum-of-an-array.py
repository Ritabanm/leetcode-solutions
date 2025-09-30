class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        if len(nums)<=2:
            return sum(nums)%10
        else:
            D =[]
            for i in range(len(nums)-1):
                if i!=0:
                    nums = D[:]
                D = []
                for i in range(len(nums)-1):
                    D.append((nums[i]+nums[i+1])%10)
            if D== []:
                return 0
             
            else:
                return D[0]