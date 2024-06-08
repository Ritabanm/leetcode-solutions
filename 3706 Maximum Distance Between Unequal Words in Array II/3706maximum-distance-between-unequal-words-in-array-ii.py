class Solution:
    def maxDistance(self, words: List[str]) -> int:
        for i in range(len(words)//2+1):
            if words[i]!=words[0] or words[-1-i]!=words[0]:
                return len(words)-i
        return 0