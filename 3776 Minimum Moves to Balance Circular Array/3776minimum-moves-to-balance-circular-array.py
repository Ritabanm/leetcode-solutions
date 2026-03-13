class Solution:
    def minMoves(self, balance: List[int]) -> int:
        if sum(balance)<0: 
            return -1
        n=len(balance)
        I=0
        while I<n and 0<=balance[I]:
            I+=1
        if I==n:
            return 0
        k=-balance[I]
        answ=0
        i=0
        while k:
            i+=1
            q=min(k,balance[(n+I-i)%n]+balance[(I+i)%n])
            answ+=i*q
            k-=q
        return answ