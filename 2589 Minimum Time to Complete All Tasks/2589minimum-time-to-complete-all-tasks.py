class Solution:
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        tasks.sort(key = lambda x: x[1])
        tot = 0
        used = [0] * 2001
        for curr_task in tasks:
            s, e, d = curr_task
            up = sum(used[s:e + 1])
            remain = d - up
            if remain <= 0:
                continue
            else:
                for i in range(remain):
                    while(used[e - i] == 1):
                        e -= 1
                    used[e-i] = 1
        return sum(used)