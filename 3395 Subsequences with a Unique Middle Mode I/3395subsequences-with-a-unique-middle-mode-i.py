class Solution:
    def subsequencesWithMiddleMode(self, A: List[int]) -> int:
        MOD = 10**9 + 7
        N = len(A)
        ans = 0
        pre = Counter()
        suf = Counter(A)

        # P = sum pre[x]^2
        # Q = sum suf[x]^2
        # U = sum pre[x] suf[x]
        # V = sum pre[x]^2 suf[x]
        # W = sum pre[x] suf[x]^2
        P = U = V = W = 0
        Q = sum(v * v for v in suf.values())

        for i, v in enumerate(A):
            # suf[v]--
            P -= pre[v] ** 2
            Q -= suf[v] ** 2
            U -= pre[v] * suf[v]
            V -= pre[v] ** 2 * suf[v]
            W -= pre[v] * suf[v] ** 2
            suf[v] -= 1
            P += pre[v] ** 2
            Q += suf[v] ** 2
            U += pre[v] * suf[v]
            V += pre[v] ** 2 * suf[v]
            W += pre[v] * suf[v] ** 2

            # Add freq(A[i]) >= 2 cases
            left = i
            right = N - 1 - i
            ans += comb(left, 2) * comb(right, 2)
            ans -= comb(left - pre[v], 2) * comb(right - suf[v], 2)

            # Subtract 221 and 32 cases:
            left1 = left - pre[v]
            right1 = right - suf[v]
            P1 = P - pre[v] ** 2
            Q1 = Q - suf[v] ** 2
            U1 = U - pre[v] * suf[v]
            V1 = V - pre[v] ** 2 * suf[v]
            W1 = W - pre[v] * suf[v] ** 2

            ans -= (P1 - left1) * suf[v] * (right1) // 2
            ans -= (Q1 - right1) * pre[v] * (left1) // 2
            ans -= U1 * (pre[v] * right - 2 * pre[v] * suf[v] + suf[v] * left)
            ans -= V1 * (-suf[v])
            ans -= W1 * (-pre[v])

            # pre[v]++
            P -= pre[v] ** 2
            Q -= suf[v] ** 2
            U -= pre[v] * suf[v]
            V -= pre[v] ** 2 * suf[v]
            W -= pre[v] * suf[v] ** 2
            pre[v] += 1
            P += pre[v] ** 2
            Q += suf[v] ** 2
            U += pre[v] * suf[v]
            V += pre[v] ** 2 * suf[v]
            W += pre[v] * suf[v] ** 2

        return ans % MOD