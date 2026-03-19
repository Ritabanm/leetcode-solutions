class Solution:
    def countKeyChanges(self, s: str, ans = 0) -> int:

        for a,b in pairwise(s):
            ans+= a.lower() != b.lower()

        return ans