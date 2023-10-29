class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        ans = float('-inf')
        nums1.sort()
        nums2.sort()

        def check(diff):
            idx = 0
            for num2 in nums2:
                num1 = num2 + diff
                while idx < m and nums1[idx] != num1:
                    idx += 1
                if idx >= m:
                    return False
                idx += 1
            return True

        for diff in [nums1[0] - nums2[0], nums1[1] - nums2[0], nums1[2] - nums2[0]]:
            if check(diff):
                ans = max(ans, diff)
        return -ans