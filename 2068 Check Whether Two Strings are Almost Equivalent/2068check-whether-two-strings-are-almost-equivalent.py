class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        for i in word1:
            if abs(word1.count(i)-word2.count(i))>3:
                return False
        for i in word2:
            if abs(word2.count(i)-word1.count(i))>3:
                return False
        return True