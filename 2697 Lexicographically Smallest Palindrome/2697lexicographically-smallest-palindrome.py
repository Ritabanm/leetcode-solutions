class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        s_list = list(s)
        l,r = 0, len(s_list)-1
        while l<r:
            if ord(s_list[l]) < ord(s_list[r]):
                s_list[r] = s_list[l]
            elif ord(s_list[l]) > ord(s_list[r]):
                s_list[l] = s_list[r]
            l+=1
            r-=1
        new_s = ''.join(s_list)
        return new_s        