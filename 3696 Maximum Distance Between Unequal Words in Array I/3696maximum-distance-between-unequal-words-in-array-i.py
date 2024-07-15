class Solution:
    def maxDistance(self, words: List[str]) -> int:
        res = 0
        for i in range(len(words) - 1):
            if words[i] != words[-1]:
                res = max(res, (len(words) -1) - i + 1)
                break
        
        for i in range(len(words) - 1, -1, -1):
            if words[i] != words[0]:
                res = max(res, i - 0 + 1)
        
        return res