class Solution:
    def beautifulSplits(self, nums: List[int]) -> int:

        nums = ''.join([chr(100 + n) for n in nums])
        
        b = 0
        n = len(nums)
        for i in range(n):
            num1 = nums[:i + 1]

            for j in range(i + 1, n- 1):
                num2 = nums[i+ 1: j + 1]
                num3 = nums[j + 1:]

                if num2.startswith(num1) or num3.startswith(num2):
                    b +=1
                



        return b


        