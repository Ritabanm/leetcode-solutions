class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:

        buy,sell  = [], []                                                              # <-- 1

        for price,amt,order in orders:                                                  # <-- 2
            if order: heappush(sell, ( price, amt))                                     #
            else    : heappush(buy , (-price, amt))                                     #
            
            while buy and sell and -buy[0][0] >= sell[0][0]:                            # <-- 3
                                                                                        #
                (buyPrice,buyAmt), (sellPrice,sellAmt) = heappop(buy), heappop(sell)    #
                                                                                        #
                if   buyAmt > sellAmt: heappush(buy , (buyPrice , buyAmt -sellAmt))     #
                elif buyAmt < sellAmt: heappush(sell, (sellPrice, sellAmt- buyAmt))     #

        return sum(amt for _,amt in buy+sell)% (1000000007)                             # <-- 4