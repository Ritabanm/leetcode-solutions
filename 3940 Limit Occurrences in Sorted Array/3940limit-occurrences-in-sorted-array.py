class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        p = nums[0]
        c_c = 0
        res = []
        for num in nums:
            if num==p:
                if c_c>=k:
                    continue
                c_c+=1
                res.append(num)
            else:
                p = num
                res.append(num)
                c_c = 1
        return res