class Solution:
    def maxSum(self, nums: List[int]) -> int:
        nums.sort()
        arr = []
        def digFindMax(num):
            b = 0
            while num>0:
                b = max(b, num%10)
                num//=10
                if b==9:
                    return b
            return b
        
        for i in range(0, len(nums)):
            arr.append(digFindMax(nums[i]))
        res = -1

        l = 1

        for i in range(len(nums)-1, -1,-1):
            for j in range(len(nums)-1-l, -1, -1):
                if arr[j]==arr[i]:
                    res = max(res, nums[i]+nums[j])
            l+=1
        return res