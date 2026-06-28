class Solution:
    def generateSchedule(self, n: int) -> List[List[int]]:
        ans = []

        # Impossible when n <= 4
        if n <= 4:
            return ans
        
        # [0,1],[2,3],...,[1,2],[3,4],...
        taken = [False] * n
        first = 0
        used = 0
        while used < n:
            if taken[first]:
                first = (first + 1) % n
            else:
                taken[first] = True
                ans.append([first, (first + 1) % n])
                used += 1
                first = (first + 2) % n
        
        # [1,0],[3,2],...,[2,1],[4,3],...
        taken = [False] * n
        used = 0
        while used < n:
            if taken[first]:
                first = (first + 1) % n
            else:
                taken[first] = True
                ans.append([(first + 1) % n, first])
                used += 1
                first = (first + 2) % n
        
        # [0,d],[1,d+1],...,[n−1,n−1+d]
        for d in range(2, n - 1):
            # Shift order if needed
            while first in ans[-1] or ((first + d) % n) in ans[-1]:
                first = (first + 1) % n
            for _ in range(n):
                ans.append([first, (first + d) % n])
                first = (first + 1) % n
        return ans