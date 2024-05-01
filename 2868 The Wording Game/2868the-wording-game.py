class Solution:
    def canAliceWin(self, a: List[str], b: List[str]) -> bool:
        mapa, mapb = {}, {}
        for w in a:
            mapa[w[0]] = w
        for w in b:
            mapb[w[0]] = w
        
        def dfs(word, turna):
            if turna:
                char = word[0]
                candis = []
                for nx in [char, chr(ord(char) + 1)]:
                    if nx in mapb and mapb[nx] > word:
                        candis.append(mapb[nx])
                if len(candis) == 0:
                    return True
                for w in candis:
                    if dfs(w, not turna):
                        return False
                return True
            else:
                char = word[0]
                candis = []
                for nx in [char, chr(ord(char) + 1)]:
                    if nx in mapa and mapa[nx] > word:
                        candis.append(mapa[nx])
                if len(candis) == 0:
                    return True
                for w in candis:
                    if dfs(w, not turna):
                        return False
                return True
        return dfs(a[0], True)