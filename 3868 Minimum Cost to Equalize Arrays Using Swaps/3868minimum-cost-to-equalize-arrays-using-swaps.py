class Solution:
    def minCost(self, nums1, nums2):
        
        from collections import defaultdict
        
        hash1 = defaultdict(int)
        hash_total = defaultdict(int)

        for num in nums1:
            hash1[num] += 1
            hash_total[num] += 1

        for num in nums2:
            hash1[num] -= 1
            hash_total[num] += 1

        for val in hash_total.values():
            if val % 2 != 0:
                return -1

        ans = 0

        for diff in hash1.values():
            ans += abs(diff) // 2

        return ans // 2