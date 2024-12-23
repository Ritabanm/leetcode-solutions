class Solution:
    def minEnergy(self, n: int, brightness: int, intervals: list[list[int]]) -> int:
        intervals.sort()
        time, (beg,end)=0, intervals[0]
        for left,right in intervals:
            if end<left:
                time+=end-beg+1
                beg,end = left,right
            elif end<right:
                end = right
        return ceil(brightness/3)*(time+end-beg+1)