class Solution:
    def binarySearchableNumbers(self, nums: List[int]) -> int:
        st1 = []
        for i, x in enumerate(nums):
            while st1 and st1[-1] > x:
                st1.pop()
            st1.append(x)
        st2 = []
        for i, x in enumerate(reversed(nums)):
            while st2 and st2[-1] < x:
                st2.pop()
            st2.append(x)
        return len(set(st1) & set(st2))