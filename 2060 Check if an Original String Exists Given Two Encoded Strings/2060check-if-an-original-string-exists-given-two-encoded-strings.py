from functools import cache


class Solution:
    def possiblyEquals(self, s1: str, s2: str) -> bool:
        def tokenize(s):
            # tokenize the string into contiguous
            # alpha and digit subsequences
            result = []
            number = []
            for c in s:
                if c.isdigit():
                    number.append(c)
                else:
                    if number:
                        result.append("".join(number))
                        number.clear()
                    result.append(c)
            if number:
                result.append("".join(number))
            
            return result
        
        
        @cache
        def get_numbers(s):
            # get possible numbers 
            # from the digit sequence
            result = [int(s)]
            if len(s) == 2:
                result.append(int(s[0]) + int(s[1]))
            elif len(s) == 3:
                result.append(int(s[0]) + int(s[1:]))
                result.append(int(s[0]) + int(s[1]) + int(s[2]))
                result.append(int(s[:2]) + int(s[2]))
            
            return result
        
        
        # pre-process the strings
        s1 = tokenize(s1)
        s2 = tokenize(s2)
        n1 = len(s1)
        n2 = len(s2)

        
        @cache
        def dp_top_down(offset, i1, i2):
            if offset > 0:
                # there is offset from s1
                if i2 == n2:
                    # s2 ran out
                    return False
                elif s2[i2].isalpha():
                    # next token in s2 is a letter
                    return dp_top_down(offset - 1, i1, i2 + 1)
                else:
                    # next token in s2 is a number
                    for num2 in get_numbers(s2[i2]):
                        if dp_top_down(offset - num2, i1, i2 + 1):
                            return True
            elif offset < 0:
                # there is offset from s2
                if i1 == n1:
                    # s1 ran out
                    return False
                elif s1[i1].isalpha():
                    # next token in s1 is a letter
                    return dp_top_down(offset + 1, i1 + 1, i2)
                else:
                    # next token in s1 is a number
                    for num1 in get_numbers(s1[i1]):
                        if dp_top_down(offset + num1, i1 + 1, i2):
                            return True
            elif i1 == n1:
                if i2 == n2:
                    # both s1 and s2 ran out
                    return True
                else:
                    # s1 ran out, but not s2
                    return False
            elif i2 == n2:
                # s2 ran out, but not s1
                return False
            elif s1[i1].isalpha():
                if s2[i2].isalpha():
                    if s1[i1] == s2[i2]:
                        # next tokens are equal letters
                        return dp_top_down(0, i1 + 1, i2 + 1)
                    else:
                        # next tokens are different letters
                        return False
                else:
                    # next token in s1 is a letter
                    # next token in s2 is a number
                    for num2 in get_numbers(s2[i2]):
                        if dp_top_down(-num2 + 1, i1 + 1, i2 + 1):
                            return True
            elif s2[i2].isalpha():
                # next token in s1 is a number
                # next token in s2 is a letter
                for num1 in get_numbers(s1[i1]):
                    if dp_top_down(num1 - 1, i1 + 1, i2 + 1):
                        return True
            else:
                # next tokens are numbers
                # generate all possible combinations
                for num1 in get_numbers(s1[i1]):
                    for num2 in get_numbers(s2[i2]):
                        if dp_top_down(num1 - num2, i1 + 1, i2 + 1):
                            return True
            
            # none of the above worked
            return False
        
        
        # initial conditions: no leftover, 
        # start from the first tokens in s1 and s2
        return dp_top_down(0, 0, 0)