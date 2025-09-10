class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        def solve(num):
            if num ==2:
                return -1
            mini = num
            for i in range(31):
                a = num-(1<<i)
                if (a| (a+1))==num:
                    mini = min(mini,a)
            return mini
        return [solve(num) for num in nums]