class Solution:
    def maxNumber(self, nums1: list[int], nums2: list[int], k: int) -> list[int]:
        def pickMax(nums, t):
            drop = len(nums) - t
            stack = []
            for num in nums:
                while drop and stack and stack[-1] < num:
                    stack.pop()
                    drop -= 1
                stack.append(num)
            return stack[:t]
    
        def merge(a, b):
            res = []
            while a or b:
                if a > b:
                    res.append(a[0])
                    a = a[1:]
                else:
                    res.append(b[0])
                    b = b[1:]
            return res
    
        m, n = len(nums1), len(nums2)
        best = [0] * k
        for x in range(max(0, k - n), min(k, m) + 1):
            y = k - x
            seq1 = pickMax(nums1, x)
            seq2 = pickMax(nums2, y)
            candidate = merge(seq1, seq2)
            if candidate > best:
                best = candidate
        return best