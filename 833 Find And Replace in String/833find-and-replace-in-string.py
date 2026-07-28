class Solution:
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        i, result = 0, ""
        lookup = {}
        for j, src, tgt in zip(indexes, sources, targets):
            if j not in lookup and S[j:].startswith(src):
                lookup[j] = (src, tgt)
        while i < len(S):
            if i in lookup and S[i:].startswith(lookup[i][0]):
                result += lookup[i][1]
                i += len(lookup[i][0])
            else:
                result += S[i]
                i += 1
        return result