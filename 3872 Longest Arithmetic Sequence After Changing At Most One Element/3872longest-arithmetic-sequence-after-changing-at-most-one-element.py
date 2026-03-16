class Solution:
    def longestArithmetic(self, nums: List[int]) -> int:

        def makePref(arr: List[int]) -> List[int]:
            pref = [1] * n
            for i, (x, y) in enumerate(pairwise(arr)):
                if x == y: pref[i + 1] = pref[i] + 1
            return pref        


        n = len(nums) - 1
        diff = [y - x for x, y in pairwise(nums)]
 
        left = makePref(diff)
        ans = max(left) + 2        
        if ans == n + 2:  return n + 1        
        rght = makePref(diff[::-1])[::-1]

        for i in range(n - 1):
            delta, isOdd = divmod(diff[i] + diff[i+1], 2)
            if isOdd: continue

            curLen = 2
            if i > 0 and diff[i - 1] == delta:
                curLen+= left[i - 1]
            if i < n - 2 and diff[i+2] == delta:
                curLen+= rght[i + 2]
            if curLen >= ans: 
                ans = curLen + 1

        return ans