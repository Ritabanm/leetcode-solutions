class Solution:
    def minimumTime(self, jobs: List[int], workers: List[int]) -> int:
        jobs.sort()
        workers.sort()

        res = 0

        #Calculate time for worker to find the job.
        for i in range(len(jobs)):
            res = max(res, ceil (jobs[i]/workers[i]))
        return res