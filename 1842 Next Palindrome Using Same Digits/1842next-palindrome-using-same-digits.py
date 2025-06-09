class Solution:
    def nextPalindrome(self, num: str) -> str:
        def nextPermutation(nums):
            n = len(nums)
            right = len(nums) - 1
            while right > 0 and nums[right-1] >= nums[right]:
                right -= 1
            if right == 0:
                nums.reverse()
                return
            pivot = nums[right - 1]
            for i in range(n - 1, right - 1, -1):
                if nums[i] > pivot:
                    next_idx = i
                    break
            nums[right - 1], nums[next_idx] = nums[next_idx], nums[right - 1]
            left = right
            right = n - 1
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        nums = list(map(int, num[:len(num)//2]))
        if nums == sorted(nums, reverse = True): return ""
        nextPermutation(nums)
        nums = "".join(map(str, nums))
        return nums+["",num[len(num)//2]][len(num)%2]+nums[::-1]