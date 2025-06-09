class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        # get frequencies of unique denominations in coins 
        coin_frequencies = collections.Counter(coins)
        # get sorted list of the unique denominations in coin_frequencies
        # for greedy approach, it must be sorted 
        coin_keys = sorted(list(coin_frequencies.keys()))
        # largest coin combination so far that we have found 
        largest = 0
        # for coin in sorted coin keys 
        for coin in coin_keys : 
            # if we run into a point where a coin is out of reach of contiguous advancement, 
            if coin > largest+1 : 
                # break because we will not make it to there 
                break
            else : 
                # otherwise, increment largest by coin_frequencies[coin] * coin
                largest += (coin_frequencies[coin] * coin)
        # account for the case of zero coins based on problem examples 
        return largest + 1