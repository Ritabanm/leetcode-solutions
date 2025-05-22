class Solution:
    def intersection(self, nums1, nums2):
        res = []
        seen =set(nums1)
        for char in nums2:
            if char in seen:
                res.append(char)
                seen.remove(char)
        return res