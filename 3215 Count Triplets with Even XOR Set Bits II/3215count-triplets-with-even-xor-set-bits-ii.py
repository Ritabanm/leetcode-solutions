class Solution:
    def tripletCount(self, a, b, c):
        cc = lambda x: Counter([v.bit_count() % 2 for v in x]) 
        a, b, c = cc(a), cc(b), cc(c)
        return a[0] * b[0] * c[0] + a[1] * b[1] * c[0] + a[0] * b[1] * c[1] + a[1] * b[0] * c[1]