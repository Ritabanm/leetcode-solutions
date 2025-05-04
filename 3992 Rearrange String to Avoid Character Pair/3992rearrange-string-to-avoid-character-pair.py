class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        return ''.join([y*s.count(y), x*s.count(x), s.replace(x,'').replace(y,'')])