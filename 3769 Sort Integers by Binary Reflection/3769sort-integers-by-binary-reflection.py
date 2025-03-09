class Solution:
    def sortByReflection(self, nums):
        arr  = []
        for i in range(len(nums)):
            bn = bin(nums[i])[2:]
            rev = bn[::-1]
            val = int(rev,2)
            arr.append((val, nums[i]))
        arr.sort()
        ans = []
        for b, i in arr:
            ans.append(i)
        return ans