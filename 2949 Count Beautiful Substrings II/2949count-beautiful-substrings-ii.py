class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        nvowels = 0
        for a in s:
            if a in 'aeiou':nvowels += 1
        nconsonants = n - nvowels
        maxx = min(nvowels,nconsonants)
        
        res = 0
        currv,currc = 0,0
        l = 1
        while (l*l) % (k*4) !=0:
            l += 1
        diffdict = {0:{l-1:1}}
        for i,a in enumerate(s):
            rem = i % l
            if a in 'aeiou':currv += 1
            else:currc += 1
            diff = currv - currc
            if diff in diffdict:
                if rem in diffdict[diff]:
                    res += diffdict[diff][rem]
            else:
                diffdict[diff] = {}
            if rem not in diffdict[diff]:
                diffdict[diff][rem] = 0
            diffdict[diff][rem] += 1
        return res