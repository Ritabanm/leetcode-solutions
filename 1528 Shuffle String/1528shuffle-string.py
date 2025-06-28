class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        outcome =""
        for i in range(len(s)):
            outcome = outcome+s[indices.index(i)]
        return outcome