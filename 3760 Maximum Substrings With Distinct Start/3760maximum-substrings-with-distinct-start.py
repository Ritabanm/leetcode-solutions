class Solution:
    def maxDistinct(self, s: str) -> int:
        n = len(s)
        used = set()

        @cache
        def helper(pointer):
            nonlocal used
            curr = s[pointer]
            # print('\t' * pointer, curr)
            if s[pointer] in used:
                return -1
            # not used
            best = 1
            used.add(s[pointer])
            for next_try in range(pointer + 1, n):
                future = helper(next_try)
                if future > 0:
                    best = max(best, future + 1)
            used.remove(s[pointer])
            return best

        return helper(0)