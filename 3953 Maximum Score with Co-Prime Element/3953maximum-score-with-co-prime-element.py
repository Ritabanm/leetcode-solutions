class Solution:
    def maxScore(self, nums: List[int], maxVal: int) -> int:
        MX = max(max(nums), maxVal)

        mu = [0] * (MX + 1)
        mu[1] = -1
        for i in range(1, MX + 1):
            for j in range(2 * i, MX + 1, i):
                mu[j] -= mu[i]


        mk = [0] * (MX + 1)
        D = [[] for _ in range(MX + 1)]
        for i in range(2, MX + 1):
            if mk[i]: continue
            for j in range(i, MX + 1, i):
                D[j].append(i)
                if j % (i * i) == 0: mk[j] = 1


        cnt = [0]*(MX+1)
        for e in nums: cnt[e] += 1

        frq = [0]*(MX+1)
        for i in range(2, MX+1):
            for j in range(i, MX+1, i): frq[i] += cnt[j]

        # print(mu)
        # print(D)
        # print(cnt)
        # print(frq)


        res = 0 if cnt[1] == 0 else 1
        for i in range(MX, 1, -1):
            if i <= res: break
            if cnt[i] == 0 and i > maxVal: continue

            t = 0
            for d in D[i]:
                t += mu[d] * frq[d]

            if cnt[i]: t -= 1
            else: t = max(t, 1)
            # print(i, t)
            res = max(res, i-t)

        return res