class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        @cache
        def f(n, sm):
            if sm < 0: return 0
            if sm == 0: return 1
            sn = str(n)
            if len(sn) == 1: return int(n >= sm)
            res = f(int(sn[1:]), sm - int(sn[0]))
            for i in range(min(sm + 1, int(sn[0]))): 
                res += f(int('9' * (len(sn) - 1)), sm - i)
            # print(n, sm, res)
            return res
        
        return sum((f(int(num2), sm) - f(int(num1) - 1, sm) for sm in range(min_sum, max_sum + 1))) % int(1e9 + 7)

# With comments version 
class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        @cache
        def f(n, sm):
            """Answers the question how many numbers less than 
            or equal to n have digits that add up to sm.
            """
            if sm < 0: return 0  # impossible so return 0
            if sm == 0: return 1 # only 0 will work
            sn = str(n)          # string version of n to make the rest easier
            
            # ie with n == 9 and sm == 6, only 6 will work
            if len(sn) == 1: return int(n >= sm) 
            
            # if the first digit is fixed then the rest of the digits
            # must not represent a greater number than they currently do
            res = f(int(sn[1:]), sm - int(sn[0])) 

            # If the first digit is less than it is, then the rest can be up to 9999...
            for i in range(min(sm + 1, int(sn[0]))): 
                res += f(int('9' * (len(sn) - 1)), sm - i)

            return res
            
        # With a max of 400 sm's, we will go through each one. 
        return sum((f(int(num2), sm) - f(int(num1) - 1, sm) for sm in range(min_sum, max_sum + 1))) % int(1e9 + 7)