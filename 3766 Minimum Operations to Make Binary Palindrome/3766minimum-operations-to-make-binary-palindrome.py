class Solution:
    def minOperations(self, nums: List[int]) -> List[int]:
        def isBinaryPalindrome(num):
            conversion = bin(num)[2:]
            return conversion == conversion[::-1]
        res = []
        for i in range(len(nums)):
            step = 0
            while True:
                if isBinaryPalindrome(nums[i]+step):
                    res.append(step)
                    break
                if nums[i]-step>=0 and isBinaryPalindrome(nums[i]-step):
                    res.append(step)
                    break
                step+=1
        return res