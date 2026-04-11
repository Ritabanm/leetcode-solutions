class Solution:
    def firstUniqueEven(self, nums):
        ctr = Counter(nums)
        for num, cnt in ctr.items():
            if not num%2 and cnt==1:
                return num
        return -1