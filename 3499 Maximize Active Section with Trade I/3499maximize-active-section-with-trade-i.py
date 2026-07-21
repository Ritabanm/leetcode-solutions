class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        
        grps = [len(list(g)) for k, g in groupby(s) if k == '0']

        return s.count('1') + max(map(sum, pairwise(grps)), default = 0)
        