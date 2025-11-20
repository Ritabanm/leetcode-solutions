class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        even = sorted(nums[::2], reverse = True)
        odd = sorted(nums[1::2])
        for i in range(len(nums)):
            if i%2==0:
                nums[i] = even.pop()
            else:
                nums[i] = odd.pop()
        return nums