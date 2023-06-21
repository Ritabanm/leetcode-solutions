class Solution:
    def findLatestTime(self, time_str):
        len_time_str = len(time_str)
        
        ret_val = ''

        i = 0
        while (i < len_time_str):
            c = time_str[i]
            if (c == '?'):
                if (i == 0):
                    if (time_str[i+1] == '?'):
                        ret_val += '1'
                    elif (time_str[i+1] in ('0', '1')):
                        ret_val += '1'
                    else:
                        ret_val += '0'
                elif (i == 1):
                    if (time_str[i-1] == '?'):
                        ret_val += '1'
                    elif (time_str[i-1] in ('0')):
                        ret_val += '9'
                    elif (time_str[i-1] in ('1')):
                        ret_val += '1'
                    else:
                        ret_val += '0'
                elif (i == 3):
                    ret_val += '5'
                elif (i == 4):
                    ret_val += '9'
            else:
                ret_val += c

            i += 1

        return ret_val