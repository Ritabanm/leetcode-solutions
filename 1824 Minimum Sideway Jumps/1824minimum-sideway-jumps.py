class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        n = len(obstacles)
        Table = [1,0,1]

        prev_obs = obstacles[1]-1
        if obstacles[1]: Table[prev_obs] = inf

        for i in range(2,n):
            obs = obstacles[i]-1

            if obs>=0: Table[obs] = inf
            if prev_obs >=0 and prev_obs != obs:
                Table[prev_obs] = 1 + min(Table[(prev_obs+1)%3], Table[(prev_obs+2)%3])
            prev_obs = obs
        return min(Table)