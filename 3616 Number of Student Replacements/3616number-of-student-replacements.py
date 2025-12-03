class Solution:
    def totalReplacements(self, ranks: List[int]) -> int:
        c=-1
        val=10**5+1
        for r in ranks:
            if r<val:
                c+=1
                val=r
        return c