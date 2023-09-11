class Solution:
    def maximumPossibleSize(self, nums: List[int]) -> int:
        stack = []

        for num in nums:
            if stack and num<stack[-1]:
                continue
            stack.append(num)
        return len(stack)