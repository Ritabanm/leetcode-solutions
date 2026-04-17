class Solution:
    def checkPartitioning(self, s: str) -> bool:
        first = ""
        for i in range(len(s)):
            first += s[i]
            if first != first[::-1]:
                continue
            second = ""
            for j in range(i + 1, len(s)):
                second += s[j]
                if second != second[::-1]:
                    continue
                third = s[j + 1:]
                if first and second and third:
                    if first == first[::-1] and second == second[::-1] and third == third[::-1] and len(first) + len(second) + len(third) == len(s):
                        #print(first, second, third)
                        return True
        return False