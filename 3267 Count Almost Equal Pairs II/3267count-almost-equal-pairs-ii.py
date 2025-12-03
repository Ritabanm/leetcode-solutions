class Solution:
    def countPairs(self, A: List[int]) -> int:
        def adj(x):
            s = list(str(x))
            n = len(s)
            ans = set()
            for i, j in combinations_with_replacement(range(n), 2):
                s[i], s[j] = s[j], s[i]
                for k, l in combinations_with_replacement(range(n), 2):
                    s[k], s[l] = s[l], s[k]
                    ans.add(int("".join(s)))
                    s[k], s[l] = s[l], s[k]
                s[i], s[j] = s[j], s[i]
            return ans

        A.sort(reverse=True)
        ans = 0
        count = Counter()
        for x in A:
            ans += count[x]
            for y in adj(x):
                count[y] += 1
        return ans