class Solution:
    def matchReplacement(self, s: str, sub: str, mappings: List[List[str]]) -> bool:
        maps = {a:set([]) for a in sub}
        for a,b in mappings:
            if a not in maps:
                maps[a] = set([])
            maps[a].add(b)
        m = len(sub)
        n = len(s)
        for i in range(n-m+1):
            curr = s[i:i+m]
            possible = True
            for j in range(m):
                if curr[j]==sub[j] or curr[j] in maps[sub[j]]:
                    continue
                else:
                    possible = False
                    break
            if possible:
                return True
        return False
        