class Solution:
    def maxFixedPoints(self, nums: list[int]) -> int:
        arr = []
        n = len(nums)
        for i in range(n):
            if nums[i]<=i:
                arr.append((i-nums[i], nums[i]))
        arr.sort()
        lis = []
        for d,val in arr:
            idx = bisect.bisect_left(lis, val)
            if idx == len(lis):
                lis.append(val)
            else:
                lis[idx]=val
        return len(lis)