class Solution:
    def minTotalTime(self, forward, backward, queries):
        f, b = [0], [0]

        for fc,bc in zip(forward,backward):
            f.append(f[-1]+fc)
            b.append(b[-1]+bc)

        n = len(forward)

        cur, steps = 0, 0 

        for q in queries:
            frw, bck = float("inf"), float("inf")

            if cur < q:
                frw = f[q] - f[cur]
            else:
                frw = f[n] - (f[cur] - f[q])

            if cur < q:
                bck = b[n] - (-b[cur+1]+b[q+1])
            else:
                bck = b[cur+1] - b[q+1]

            cur = q 
            steps += min(frw,bck)

        return steps