class Solution:
    def memLeak(self, a: int, b: int) -> List[int]:
        t = 0
        while a>0 or b>0:
            if a>=b and a-(t+1)>=0:
                t+=1
                a-=t
            elif b-(t+1)>=0:
                t+=1
                b-=t
            else:
                break
        return [t+1,a,b]

        