class Solution:
    def removeTrailingZeros(self, num_str):
        len_num_str = len(num_str)
        len_trailing_zeros = 0
        i = len_num_str - 1
        while (i >= 0):
            if (num_str[i] == '0'):
                len_trailing_zeros += 1
            else:
                break

            i -= 1
        
        return num_str[:len_num_str-len_trailing_zeros]