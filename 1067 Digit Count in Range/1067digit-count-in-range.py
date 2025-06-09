class Solution:
    def digitsCount(self, d: int, low: int, high: int) -> int:

        def helper(num):

            ans, step, n = 0, 1, 0

            while num:

                num, t = divmod(num,10)
                ans+= (num-(d==0))*step + step*(t>d) + (n+1)*(t==d)

                n+= t*step

                step*= 10

            return ans
        
        return helper(high) - helper(low-1)