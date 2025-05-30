class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l1 = 0
        l2 =0

        for i in range(len(nums1)):
            if nums1[i] in nums2:
                l1+=1
        for i in range(len(nums2)):
            if nums2[i] in nums1:
                l2+=1
        return [l1, l2]