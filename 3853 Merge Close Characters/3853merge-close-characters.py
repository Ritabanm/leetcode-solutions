class Solution:
    def mergeCharacters(self, s: str, k: int) -> str:
        result = []
        lastk = Counter()
        for char in s:
            if lastk[char]>0:
                continue
            result.append(char)
            lastk[char]+=1
            if len(result)>k:
                drop = result[-k-1]
                lastk[drop]-=1
        return "".join(result)