class Solution:
    def passwordStrength(self, password: str) -> int:
        new_p = set(password)
        ans = 0
        for i in new_p:
            if 'a'<=i<='z':
                ans+=1
            elif 'A'<=i<='Z':
                ans+=2
            elif '0'<=i<='9':
                ans+=3
            else:
                ans+=5
        return ans