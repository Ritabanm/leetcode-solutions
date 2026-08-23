class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        sum_l = sum(map(int,filter(str.isdigit,num[:n//2])))
        sum_r = sum(map(int,filter(str.isdigit,num[n//2:])))
        turns_l = num[:n//2].count('?')
        turns_r = num[n//2:].count('?')
        
        #CASE 1
        sum_diff = abs(sum_l - sum_r)
        actual_turns = 0
        # CASE 2
        if turns_l != turns_r:
            actual_turns = abs(turns_r - turns_l)

            if turns_l > turns_r:
                sum_diff = sum_l - sum_r
            else:
                sum_diff = sum_r - sum_l


            if actual_turns % 2 == 1 or sum_diff > 0 or (sum_diff == 0 and actual_turns > 0):
                return True
            sum_diff = abs(sum_diff)
        # Bob wins if: sum_a + sum_b == |sum_diff|
        return sum_diff != 9*(actual_turns//2) or sum_diff % 9 != 0