class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        s1 = set(nums1)
        s2 = set(nums2)
        common = s1&s2
        if common:
            return min(common)
        n1,n2 =min(nums1),min(nums2)
        return min(n1*10+n2, n2*10+n1)