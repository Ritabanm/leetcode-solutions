class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        p_list = p.split("*")
        idx = s.find(p_list[0])
        if idx==-1: return False
        return p_list[1] in s[idx+len(p_list[0]):]