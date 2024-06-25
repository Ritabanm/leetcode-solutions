class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        res = float('inf')
        ind = []
        n = len(landStartTime)
        m = len(waterStartTime)
        t = float('inf')
        c = 0
        for i,j in zip(landStartTime,landDuration):
            t = min(t, i + j)
        
        for i in range(m):
            if t < waterStartTime[i]:
                res = min(res, waterStartTime[i] + waterDuration[i])
            else:
                res = min(res, t + waterDuration[i])

        t = float('inf')
        for i,j in zip(waterStartTime,waterDuration):
            t = min(t, i + j)
            
        for i in range(n):
            if t < landStartTime[i]:
                res = min(res, landStartTime[i] + landDuration[i])
            else:
                res = min(res, t + landDuration[i])

        return res