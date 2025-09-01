class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        ans = []
        for i, (x, l) in enumerate(positions): 
            val = 0
            for ii in range(i): 
                xx, ll = positions[ii]
                if xx < x+l and x < xx+ll: val = max(val, ans[ii])
            ans.append(val + l)
        for i in range(1, len(ans)): ans[i] = max(ans[i-1], ans[i])
        return ans