class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        m, n = len(encoded1), len(encoded2)
        i = j = 0
        result = []
        while i < m and j < n:
            val = encoded1[i][0] * encoded2[j][0]
            if encoded1[i][1] == encoded2[j][1]:
                result.append([val, encoded1[i][1]])
                i += 1
                j += 1
            elif encoded1[i][1] > encoded2[j][1]:
                result.append([val, encoded2[j][1]])
                encoded1[i][1] -= encoded2[j][1]
                j += 1
            else:
                result.append([val, encoded1[i][1]])
                encoded2[j][1] -= encoded1[i][1]
                i += 1
            if len(result) > 1 and result[-1][0] == result[-2][0]:
                result[-2][1] += result[-1][1]
                result.pop()
        return result