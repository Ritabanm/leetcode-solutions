class Solution:
    def canMakePalindromeQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        
        n = len(s) // 2
        s1, s2 = s[0:n], s[n:2*n][::-1]
        
        pos_len = [0] * n
        pre = 0
        for j in range(n+1):
            if j == n or s1[j] != s2[j]:
                for i in range(pre, j):
                    pos_len[i] = j-i
                pre = j+1
        
        psum1 = [None] * n
        cur_cnt = [0] * 26
        for i in range(n):
            cur_cnt[ord(s1[i]) - ord('a')] += 1
            psum1[i] = cur_cnt.copy()
        
        psum2 = [None] * n
        cur_cnt = [0] * 26
        for i in range(n):
            cur_cnt[ord(s2[i]) - ord('a')] += 1
            psum2[i] = cur_cnt.copy()
        
        def p(a, b):
            # if s1[a..b] == s2[a..b]
            if a > b:
                return True
            return pos_len[a] >= b-a+1
        
        def f(a, b):
            # if s1[a..b] and s2[a..b] have same letters. i.e. can be rearranged to be equal.
            if a > b:
                return True
            for i in range(26):
                c1 = psum1[b][i] - (0 if a == 0 else psum1[a-1][i])
                c2 = psum2[b][i] - (0 if a == 0 else psum2[a-1][i])
                if c1 != c2:
                    return False
            return True
        def e1(a, b, c, d, rev):
            if rev:
                return e2(a, b, c, d, False)
            if c > d:
                return True
            for i in range(26):
                c1 = psum1[b][i] - (0 if a == 0 else psum1[a-1][i])
                c2 = psum2[d][i] - (0 if c == 0 else psum2[c-1][i])
                if c1 < c2:
                    return False
            return True
        
        def e2(a, b, c, d, rev):
            if rev:
                return e1(a, b, c, d, False)
            if c > d:
                return True
            for i in range(26):
                c1 = psum2[b][i] - (0 if a == 0 else psum2[a-1][i])
                c2 = psum1[d][i] - (0 if c == 0 else psum1[c-1][i])
                if c1 < c2:
                    return False
            return True
        
        res = []
        for a, b, c, d in queries:
            c, d = 2*n-1-d, 2*n-c-1
            rev = False
            if a > c:
                a, b, c, d = c, d, a, b
                rev = True

            if c > b:
                res.append( p(0, a-1) and p(b+1, c-1) and p(d+1, n-1) and f(a, b) and f(c, d) )
            elif d > b:
                res.append( p(0, a-1) and p(d+1, n-1) and e1(a, b, a, c-1, rev) and e2(c, d, b+1, d, rev) and f(a, d) )
            else:
                res.append( p(0, a-1) and p(b+1, n-1) and e1(a, b, a, c-1, rev) and e1(a, b, d+1, b, rev) and f(a, b) )
        
        return res