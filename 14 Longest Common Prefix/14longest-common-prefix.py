class Solution:
    def longestCommonPrefix(self, strs):
        
        if not strs:
            return ""
        res = ""
        for i in range(len(strs[0])):
            for s in strs:
                if i==len(s) or s[i]!=strs[0][i]:
                    return res
            res+=strs[0][i]
        return res

"""class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        
        #Storing final result in res
        res = ""

        for i in range(len(strs[0])):
            for s in strs:
                #terminating the loop if index exceeds bounds or character mismatch
                if i==len(s) or s[i]!=strs[0][i]:
                    return res
            res+= strs[0][i]
        return res
"""