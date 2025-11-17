class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        N = len(nums1)
        MOD = 10 ** 9 + 7

        s = sorted(nums1)


        diff = []
        optimal = 0
        for a, b in zip(nums1, nums2):
            diff.append(abs(a - b))

            mn = abs(a - b)

            index = bisect_left(s, b)
            if 0 <= index < N:
                mn = min(mn, abs(s[index] - b))
                
            index += 1
            if 0 <= index < N:
                mn = min(mn, abs(s[index] - b))

            index2 = bisect_right(s, b)
            if 0 <= index2 < N:
                mn = min(mn, abs(s[index2] - b))
            
            index2 -= 1
            if 0 <= index2 < N:
                mn = min(mn, abs(s[index2] - b))

            optimal = max(optimal, abs(mn - abs(a - b)))


        return (sum(diff) - optimal) % MOD