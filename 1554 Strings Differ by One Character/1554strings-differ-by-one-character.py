class Solution:
    def differByOne(self, dict: List[str]) -> bool:
        n, m = len(dict), len(dict[0])
        hashes = [0] * n
        MOD = 150
        
        for i in range(n):
            for j in range(m):
                hashes[i] = (26 * hashes[i] + (ord(dict[i][j]) - ord('a'))) % MOD
        
        base = 1
        for j in range(m - 1, -1, -1):        
            seen = collections.defaultdict(list)
            for i in range(n):
                rem = dict[i][:j] + dict[i][j+1:]
                new_h = (hashes[i] - base * (ord(dict[i][j]) - ord('a'))) % MOD
                # if any(filter(lambda x:x==rem, seen[new_h])): 
                if len(list(filter(lambda x:x==rem, seen[new_h]))) > 0:
                    return True 
                seen[new_h].append(rem)
            base = 26 * base % MOD
        return False