class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        res = []

        for num in nums:
            for i in range(num):
                if i | (i+1) == num:
                    res.append(i)
                    break
            else:
                res.append(-1)
        

        return res