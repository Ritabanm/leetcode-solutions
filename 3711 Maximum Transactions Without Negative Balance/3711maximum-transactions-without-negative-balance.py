class Solution:
    def maxTransactions(self, transactions: List[int]) -> int:
        heap,sm, pops = [1],0,0
        for cash in transactions:
            if cash>=0:
                sm+=cash
            elif sm+cash>=0:
                sm+=cash
                heappush(heap,cash)
            else:
                sm+=cash-heappushpop(heap,cash)
                pops+=1
        return len(transactions)-pops