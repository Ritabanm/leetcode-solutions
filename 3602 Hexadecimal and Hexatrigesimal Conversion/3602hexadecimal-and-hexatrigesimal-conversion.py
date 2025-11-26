class Solution:
    def concatHex36(self, n: int) -> str:
        hex16 = "0123456789ABCDEF"
        hex36 = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        def conv(x, b, digs):
            if x == 0:
                return "0"
            s = []
            while x:
                s.append(digs[x % b])
                x //= b
            return "".join(reversed(s))
        
        return conv(n**2, 16, hex16) + conv(n**3, 36, hex36)