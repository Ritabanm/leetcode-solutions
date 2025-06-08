class Solution:
    def maxPossibleScore(self, start: List[int], d: int) -> int:

        def fail_check(num):

            prev = start[0]

            for s in start[1:]:
                prev+= num
                if s < prev - d: return True
                if s > prev: prev = s
                     
            return False 


        start.sort()
        mx = start[-1] + d + 1
    
        return bisect_left(range(mx), True, key = fail_check) - 1       