from functools import cmp_to_key
class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        def func(a,b):
            if max(a[0],b[0]+a[1]) < max(b[0],a[0]+b[1]):
                return 1
            elif max(a[0],b[0]+a[1]) > max(b[0],a[0]+b[1]):
                return -1
            return 0

        def isPossible(energy):
            for i in range(n):
                if energy < tasks[i][1]:
                    return False
                energy -= tasks[i][0]
            return True

        n = len(tasks)
        tasks.sort(key = cmp_to_key(func))

        left, right = tasks[-1][-1], sum([tasks[i][1] for i in range(n)])

        while left <= right:
            mid = (left+right)//2
            if isPossible(mid):
                ans = mid
                right = mid-1
            else:
                left = mid+1

        return ans