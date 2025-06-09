class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        l1 = []
        l2 = []

        for s in word1:
            for c in s:
                l1.append(c)
        for s in word2:
            for c in s:
                l2.append(c)
        
        if len(l1)!=len(l2):
            return False
        
        for i in range(len(l1)):
            if l1[i]!=l2[i]:
                return False
        return True