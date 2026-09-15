class Solution:
    def climbStairs(self, n):

        #Edge case: Only 1 step available.
        if n==1:
            return 1
        
        #Variables: first,second, third
        #Algorithm: fibonacci sequence: third step = first + second step count

        first = 1
        second = 2
        for i in range(3, n+1):
            third = first + second
            first = second
            second = third
        return second

        #T:O(N), S: O(1)