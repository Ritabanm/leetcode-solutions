class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        q = deque([])
        l = 0
        runningSum = 0
        ans = 0
        for r in range(len(chargeTimes)):
            runningSum += runningCosts[r]
            while q and chargeTimes[r] > chargeTimes[q[-1]]:
                q.pop()
            q.append(r)
            while q and chargeTimes[q[0]] + (r - l +1) * runningSum > budget:
                runningSum -= runningCosts[l]
                if q[0] == l:
                    q.popleft()
                l += 1
            ans = max(ans,r - l + 1)
        return ans 

