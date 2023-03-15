class Solution:
    def findMaxConsecutiveOnes(self, nums):
        max_c = 0
        curr = 0

        for num in nums:
            if num==1:
                curr+=1
                max_c = max(max_c, curr)
            else:
                curr = 0
        return max_c