class Solution:
    def deleteAndEarn(self, nums):
        if not nums:
            return 0
    
        max_num = max(nums)
        points = [0]*(max_num+1)
        for num in nums:
            points[num]+=num
        
        prev_p, prev = 0, points[0]
        
        for i in range(1, max_num+1):
            current = max(prev, prev_p + points[i])
            prev_p, prev = prev, current
        return prev
    