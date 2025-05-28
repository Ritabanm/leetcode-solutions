class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        minDistance = []
        idx1 = -1
        idx2 = -1

        for i in range(len(wordsDict)):
            if wordsDict[i] == word1:
                idx1 = i
            elif wordsDict[i] == word2:
                idx2 = i
            if(idx1 != -1 and idx2 != -1):
                minDistance.append(abs(idx1 - idx2))
                
        return min(minDistance)    
                
        