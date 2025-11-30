class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        currentSwaps = 0
        swappedSwaps = 0
        for i in range(len(nums1)-1):
            notCurrentValid = nums1[i] > nums1[-1] or nums2[i] > nums2[-1]
            notSwappedValid = nums1[i] > nums2[-1] or nums2[i] > nums1[-1]
            
            if notCurrentValid and notSwappedValid:
                return -1
            
            if notCurrentValid:
                currentSwaps += 1  
            elif notSwappedValid:
                swappedSwaps += 1
        
        return min(currentSwaps, swappedSwaps + 1)
                     