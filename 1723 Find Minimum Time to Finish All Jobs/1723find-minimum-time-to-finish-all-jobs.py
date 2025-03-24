class Solution:
    def minimumTimeRequired(self, jobs, k):
        def can_assign(jobs, k, max_time):
            workers = [0] * k
            return dfs(jobs, workers, 0, max_time, k)
        
        def dfs(jobs, workers, idx, max_time, k):
            if idx == len(jobs):
                return True
            for i in range(k):
                if workers[i] + jobs[idx] <= max_time:
                    workers[i] += jobs[idx]
                    if dfs(jobs, workers, idx + 1, max_time, k):
                        return True
                    workers[i] -= jobs[idx]
                if workers[i] == 0:
                    break
            return False
        
        left, right = max(jobs), sum(jobs)
        while left < right:
            mid = (left + right) // 2
            if can_assign(jobs, k, mid):
                right = mid
            else:
                left = mid + 1
        return left