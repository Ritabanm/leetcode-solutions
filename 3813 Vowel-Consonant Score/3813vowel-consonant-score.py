class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        ac, vc = 0,0
        for ch in s:
            ac+=ch.isalpha()
            vc+=ch in 'aeiou'
        return 0 if ac==vc else vc//(ac-vc)