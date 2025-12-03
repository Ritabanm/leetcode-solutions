class Solution:
    def findMaxSum(self, nums1: List[int], 
                         nums2: List[int], k: int) -> List[int]:

        n, sm, prev  = len(nums1), 0, 0
        heap, ans = [], [0] * n

        idx = sorted(range(n), key = lambda x: nums1[x])

        for i in idx:
            num1, num2 = nums1[i], nums2[i]
            
            if prev < num1: prv_sum = sm
            ans[i] = prv_sum
                
            prev = num1
            sm+= num2

            if len(heap) == k:
                sm-= heappushpop(heap, num2)
            else:
                heappush(heap, num2)    
            
        return ans