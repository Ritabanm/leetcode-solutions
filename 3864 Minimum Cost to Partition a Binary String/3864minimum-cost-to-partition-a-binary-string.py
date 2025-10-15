class Solution:
    def minCost(self, s: str, encCost: int, flatCost: int) -> int:
        def segCost(s1):
            X = s1.count("1")
            if X==0:
                return flatCost
            else:
                L = len(s1)
                ans = L*X*encCost
                if L%2==0:
                    ans = min(ans, segCost(s1[:L//2]) + segCost(s1[L//2:]))
                return ans
        return segCost(s)