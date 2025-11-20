class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        alp = [ord(s[0]), ord(s[3])]
        li = [chr(i) for i in range(alp[0], alp[1] + 1)]

        l = []
        for i in range(len(li)):
            for j in range(int(s[1]), int(s[4]) + 1):
                l.append(li[i] + str(j))
        return l