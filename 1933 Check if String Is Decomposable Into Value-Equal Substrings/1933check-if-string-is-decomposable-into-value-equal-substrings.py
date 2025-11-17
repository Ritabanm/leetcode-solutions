class Solution:
    def isDecomposable(self, s: str) -> bool:
        flag = False
        counts = 1
        prev = s[0]

        for x in s[1:]:
            if x == prev and counts < 3:
                counts += 1
            else:
                if counts == 1:
                    return False
                if counts == 2:
                    if flag:
                        return False
                    flag = True
                counts = 1
                prev = x

        return (flag or counts == 2) and counts > 1