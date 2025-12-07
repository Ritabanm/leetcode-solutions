class Solution:
    def largestVariance(self, s: str) -> int:
        I = defaultdict(list)
        for i, a in enumerate(s):
            I[a].append(i)

        def do(a, b, A, s, ma):
            fst_a = ca = cb = 0

            for i in A:
                if s[i] == a:
                    if fst_a and cb:
                        fst_a = 0
                    else:
                        ca += 1
                        if cb < ca:  # reset start at this i
                            fst_a = 1
                            ca = 1
                            cb = 0
                else:
                    cb += 1

                if cb - ca > ma and ca:
                    ma = cb - ca

            return ma

        ma = 0
        for a in I:
            for b in I:
                if a >= b:
                    continue
                if len(I[b]) - 1 > ma or len(I[a]) - 1 > ma:
                    A = I[a] + I[b]
                    A.sort()
                if len(I[b]) - 1 > ma:
                    ma = do(a, b, A, s, ma)
                if len(I[a]) - 1 > ma:
                    ma = do(b, a, A, s, ma)
        return ma