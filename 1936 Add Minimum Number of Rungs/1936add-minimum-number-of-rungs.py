class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        h = 0
        solution = 0
        for r in rungs:
            if (r-h)%dist ==0:
                solution+=(r-h)//dist-1
            else:
                solution += (r-h)//dist
            h = r
        return solution