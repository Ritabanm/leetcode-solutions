class Solution:
    def minimumCosts(self, regular: List[int], express: List[int], 
                           expressCost: int) -> List[int]:
        ans = []
        reg, exp = 0, expressCost

        for r, e in zip(regular, express):
            reg = min(exp + e, reg + r)
            exp = min(exp + e, reg + expressCost)

            ans.append(min(exp, reg))

        return ans