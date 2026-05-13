class Solution(object):
    def captureForts(self, forts):
        def solve(arr):
            max_ = 0
            count, flag = 0, False
            for num in arr:
                if num == 1: 
                    count, flag = 0, True
                elif num == -1: 
                    max_, count, flag = max(max_, count), 0, False
                else: 
                    if flag: count += 1
            return max_
        return max(solve(forts), solve(forts[::-1]))