        
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        size = len(nums)
        ops = 0
        stack = []
        for index in range(size):
            # if current element is less than prev element, pop all prev elements which are greater than current element and increase operations
            while stack and stack[-1] > nums[index]:
                stack.pop()
                ops += 1
            # pop all elements which are similar to current element
            while stack and stack[-1] == nums[index]:
                stack.pop()
            # if current element is not zero, add it to track the elements in stack ( in increasing fasion. )
            if nums[index] != 0:
                stack.append(nums[index])
        # pop all elements ( elements will be in increasing manner ) and increase counter
        while stack:
            stack.pop()
            ops += 1
        return ops
