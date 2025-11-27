class Solution:
    def minimumScore(self, s, t):
        def scan(s,t):
            ans, i = [0], 0

            for c in s:
                if i < len(t) and t[i] == c:
                    i += 1
                ans.append(i)

            return ans

        r1 = scan(s,t)
        r2 = reversed(scan(s[::-1],t[::-1]))
        max_val = max([i+j for i,j in zip(r1,r2)])

        return max(0,len(t)-max_val)

        

        







        