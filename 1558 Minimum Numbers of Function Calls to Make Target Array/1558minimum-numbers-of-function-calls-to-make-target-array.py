class Solution:
    def minOperations(self, nums: List[int]) -> int:
        x = sum(nums)
        count = 0
        while x != 0:
            for i in range(len(nums)):
                if nums[i] % 2 != 0:
                    count += 1
                    x -= 1
            if x != 0:
                for i in range(len(nums)):
                    if nums[i] != 0:
                        nums[i] //= 2
                        x -= nums[i]
                count += 1
        return count