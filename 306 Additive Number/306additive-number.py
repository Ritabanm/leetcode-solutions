class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        for i in range(1, n):
            if num[0] == '0' and i > 1:
                break
            for j in range(i+1, n):
                if num[i] == '0' and j - i > 1:
                    break
                num1, num2 = num[:i], num[i:j]
                k = j
                while k < n:
                    num3 = str(int(num1) + int(num2))
                    if not num.startswith(num3, k):
                        break
                    k += len(num3)
                    num1, num2 = num2, num3
                if k == n:
                    return True
        return False