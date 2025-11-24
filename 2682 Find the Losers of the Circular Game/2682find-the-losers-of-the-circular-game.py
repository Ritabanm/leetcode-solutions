class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        seen = [False]*n
        curr, step = 0,1
        while True:
            seen[curr]= True
            nxt = (curr+step*k)%n
            if seen[nxt]:
                break
            curr = nxt
            step+=1
        return [i+1 for i,v in enumerate(seen) if not v
        ]