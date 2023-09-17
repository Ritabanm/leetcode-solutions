"""class Solution:
    def totalNumbers(self, digits):
        ans = set()
        n = len(digits)
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i!=j and i!=k and j!=k and digits[i]!=0 and digits[k]%2==0:
                        ans.add(str(digits[i]) + str(digits[j]) + str(digits[k]))
        return len(ans)"""

class Solution:
    def totalNumbers(self, digits):
        ans = set()
        n = len(digits)
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i!=j and i!=k and j!=k and digits[i]!=0 and digits[k]%2==0:
                        ans.add(str(digits[i]) + str(digits[j]) + str(digits[k]))
        return len(ans)