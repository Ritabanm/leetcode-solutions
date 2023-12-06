import functools

class Solution:
    def minCostGoodCaption(self, caption: str) -> str:

        def edit(caption): # aab -> (1, aaa)
            n = len(caption)
            distance = float(inf)
            string = ""
            for target in sorted(caption):
                d = sum(abs(ord(c) - ord(target)) for c in caption)
                if d < distance:
                    distance = d
                    string = target * n
            return distance, string

        @functools.lru_cache(maxsize=1000) # 10000 -> memory limit exceeded
        def f(caption):
            n = len(caption)
            if n < 3: # 0, 1, 2
                return 0, caption
            elif n < 6: # 3, 4, 5
                return edit(caption)
            elif n == 6:
                d1, s1 = edit(caption[:3])
                d2, s2 = edit(caption[3:])
                return d1 + d2, s1 + s2
            elif n == 7:
                d11, s11 = edit(caption[:3]) # 3
                d12, s12 = edit(caption[3:]) # 4
                d21, s21 = edit(caption[:4]) # 4
                d22, s22 = edit(caption[4:]) # 3
                d1 = d11 + d12
                d2 = d21 + d22
                s1 = s11 + s12
                s2 = s21 + s22
                ds = [(d1, s1), (d2, s2)]
                ds.sort(key = lambda ds:ds[1])
                ds.sort(key = lambda ds:ds[0])
                return ds[0]
                # if d1 < d2:
                #     return s1
                # elif d1 > d2:
                #     return s2
                # else:
                #     return min(s1, s2)
            else:
                d11, s11 = edit(caption[:3]) # 3
                d12, s12 = f(caption[3:]) # 5
                d21, s21 = edit(caption[:4]) # 4
                d22, s22 = f(caption[4:]) # 4
                d31, s31 = edit(caption[:5]) # 5
                d32, s32 = f(caption[5:]) # 3
                d1 = d11 + d12
                d2 = d21 + d22
                d3 = d31 + d32
                s1 = s11 + s12
                s2 = s21 + s22
                s3 = s31 + s32
                ds = [(d1, s1), (d2, s2), (d3, s3)]
                ds.sort(key = lambda ds:ds[1])
                ds.sort(key = lambda ds:ds[0])
                return ds[0]
        
        if len(caption) < 3:
            return ""
        d, s = f(caption)
        return s