class Solution:
    def findCoins(self, numWays: List[int]) -> List[int]:

        numWays = [1] + numWays
        n, res = len(numWays), []

        for left in range(1, n):
            if numWays[left] > 1: return []
            if numWays[left] == 0: continue

            res.append(left)
            rght = n - 1
            
            while rght >= left:
                numWays[rght] -= numWays[rght - left]
                if numWays[rght] < 0:   return []
                rght -= 1

        return res