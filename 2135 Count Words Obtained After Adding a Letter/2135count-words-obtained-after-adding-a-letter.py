class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        sd = dict()
        for s in startWords:
            sd["".join(sorted(s))] = s
        ans = 0
        for t in targetWords:
            flag = False
            for j in range(len(t)):
                pattern = "".join(sorted(t[:j] + t[j + 1:]))
                if pattern in sd:
                    flag = True
                    break
            if flag:
                ans += 1
        return ans