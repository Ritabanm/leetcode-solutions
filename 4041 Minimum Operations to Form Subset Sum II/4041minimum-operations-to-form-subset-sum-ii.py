class Solution:
    def minOperations(self, nums, sum):
        n = len(nums)

        options = []

        for x in nums:
            dist = {x:0}

            q = deque([x])

            while q:
                v = q.popleft()
                d = dist[v] if v in dist else 0

                nv = v*2

                if nv <= sum and nv not in dist:
                    dist[nv] = d+1
                    q.append(nv)

                nv = v//2

                if nv > 0 and nv not in dist:
                    dist[nv] = d+1 
                    q.append(nv)

            options.append(list(dist.items()))



        dp = [[-1]*(sum+1) for _ in range(n)]

        def function(idx,target):
            if target == 0:
                return 0 

            if idx == n:
                return float("inf")

            if dp[idx][target] != -1:
                return dp[idx][target]

            ans = function(idx+1,target)

            for op1,op2 in options[idx]:
                if target-op1 < 0:
                    continue 

                ans = min(ans,op2+function(idx+1,target-op1))

            dp[idx][target] = ans 

            return ans 

        val = function(0,sum)

        return val if val != float("inf") else -1