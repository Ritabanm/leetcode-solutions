class Solution:
    def nimGame(self, piles: List[int]) -> bool:
        n = len(piles)
        @cache
        def dp(piles):
            # if someone can win in its turn, piles is a tuple, 
            end = True
            for i in range(n):
                if piles[i] > 0:
                    end = False
                    break
            if end:
                return False
            # there are still things that the player can do
            new_piles = list(piles)
            for i in range(len(new_piles)):
                cnt = new_piles[i]
                for j in range(1, cnt+1):
                    new_piles[i] -= j
                    # as long as in one case, the other player lose, then current player win!
                    tmp = dp(tuple(new_piles))
                    if not tmp:
                        return True
                    new_piles[i] += j
            return False
        
        return dp(tuple(piles))
        