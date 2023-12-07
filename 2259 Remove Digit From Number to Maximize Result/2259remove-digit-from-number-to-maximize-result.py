class Solution:
    def removeDigit(self, number: str, digit: str) -> str:

        ln = len(number)

        res = -1

        for ind, num in enumerate(number):

            if num == digit:

                res = ind

                if ind != ln-1 and number[ind+1] > digit:

                    return number[:ind] + number[ind+1:]


        return number[:res] + number[res+1:]

                

            


        
        