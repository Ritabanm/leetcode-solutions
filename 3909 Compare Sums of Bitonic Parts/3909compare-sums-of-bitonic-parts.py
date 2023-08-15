class Solution:
    def compareBitonicSums(self, nums: list[int]) -> int:
        m=0
        for i in range(1,len(nums)):
            if nums[i]>nums[m]:
                m=i;
        ass=sum(nums[:m+1])
        des=sum(nums[m:])
        if ass==des:
            return -1
        return 1 if des>ass else 0