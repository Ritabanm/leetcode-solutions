class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, 
                       hBars: List[int], vBars: List[int]) -> int:

        def find_max(bars):
            bars.sort()
            s = ''.join([str(int(y - x == 1)) for x,y in pairwise(bars)])
            return max(map(len,s.split('0')))+2
            
        return pow(min(find_max(hBars), find_max(vBars)),2)