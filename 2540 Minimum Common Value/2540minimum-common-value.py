class Solution:
    def getCommon(self, nums1,nums2):
        f = 0
        s = 0

        while f<len(nums1) and s<len(nums2):
            if nums1[f]<nums2[s]:
                f+=1
            elif nums1[f]>nums2[s]:
                s+=1
            else:
                return nums1[f]
        return -1