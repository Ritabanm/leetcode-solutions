class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:

        if not k: return -(nums1 != nums2)

        sm = smAbs = 0

        for i in range(len(nums1)):

            diff = nums1[i]-nums2[i] 

            if diff%k: return -1
            quo = diff//k

            sm   += quo
            smAbs+= abs(quo)

        return -1 if sm else smAbs//2