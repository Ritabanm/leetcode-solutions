class Solution(object):
    def sortString(self, s):
        dict = {}
        for s1 in s:
            dict[s1] = dict.get(s1, 0)+1
        list1 = sorted(list(set(s)))
        
        result = ''
        while len(result) < len(s):
            for l in list1:
                if l in dict and dict[l] != 0:
                    result += l
                    dict[l] -= 1
            
            for l in list1[::-1]:
                if l in dict and dict[l] != 0:
                    result += l
                    dict[l] -= 1
                        
        return result