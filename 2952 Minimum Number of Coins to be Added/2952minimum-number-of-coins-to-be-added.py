class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        coins.sort()
        total = 0

        coin = summ = 0
        for x in range(1,target+1):
            if coin<len(coins) and coins[coin]<=x:
                summ += coins[coin]
                coin += 1
            elif summ<x:
                summ += x
                total += 1
        
        return total