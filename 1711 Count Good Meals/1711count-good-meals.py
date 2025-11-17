class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        hmap= dict()
        m = 10**9 + 7
        c = 0
        powers = set(2**x for x in range(22))
        for i in deliciousness:
            for p in powers:
                if (p-i) in hmap:
                    c+=hmap[p-i]%m
            
            hmap[i] = hmap.get(i,0)+1
        return c%m