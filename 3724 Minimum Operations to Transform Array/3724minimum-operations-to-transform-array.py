class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        base = 0
        for i in range(n):
            base +=abs(nums1[i]-nums2[i])
        last = nums2[-1]
        ans = float('inf')
        for j in range(n):
            n1,n2=nums1[j], nums2[j]
            ans =min(ans, base + (max(n1,n2,last)-min(n1,n2,last))-abs(n1-n2)+1)
        return ans