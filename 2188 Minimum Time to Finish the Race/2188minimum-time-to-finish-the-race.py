class Solution:
    def minimumFinishTime(self, tires: List[List[int]], changeTime: int, numLaps: int) -> int:
        dp = [float('inf') for i in range(numLaps+1)] # best time taken to complete i laps
        # base case when 0 laps done 0 time taken
        dp[0]=0
        firstUncompletedLap = 1
        # base case precompuation, for laps without changing tires
        for f,r in tires:
            cumLapTime,ratio_term = 0,1
            for lap in range(1,numLaps+1):
                curLapTime = f*ratio_term
                if curLapTime > changeTime+dp[1]: # early break if continuing is worse than changing tires
                    firstUncompletedLap = max(firstUncompletedLap,lap)
                    break
                cumLapTime += curLapTime 
                dp[lap] = min(dp[lap],cumLapTime)
                ratio_term*=r

        for lapDone in range(firstUncompletedLap,numLaps+1):
            for lap in range(1,firstUncompletedLap): # iterate maximum without changing tires
                dp[lapDone] = min(dp[lapDone],changeTime+dp[lap]+dp[lapDone-lap])
        return dp[numLaps]
       