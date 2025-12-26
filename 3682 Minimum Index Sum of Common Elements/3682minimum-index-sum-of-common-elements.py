class Solution:
    def minimumSum(self, nums1: List[int], nums2: List[int]) -> int:

        d, ans = defaultdict(), inf

        for idx, num1 in enumerate(nums1):
            if num1 in d: continue
            d[num1] = idx

        for idx, num2 in enumerate(nums2):
            if num2 in d:
                sm = idx + d[num2]
                ans = sm if sm < ans else ans

        return -1 if ans == inf else ans   