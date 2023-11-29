class Solution:
    def mergeCharacters(self, s: str, k: int) -> str:
        res = []
        last_index = {}
        for char in s:
            if char in last_index and len(res)-last_index[char]<=k:
                continue
            last_index[char] = len(res)
            res.append(char)
        return "".join(res)