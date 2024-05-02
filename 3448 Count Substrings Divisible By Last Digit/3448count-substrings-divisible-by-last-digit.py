class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        def solve(d):
            rem_cnt = defaultdict(int)
            rem_cnt[0] = 1
            pref_rem = 0
            res = 0
            for i, c in enumerate(s):
                nrc = defaultdict(int)
                for rem, cnt in rem_cnt.items():
                    nrc[rem*10 % d] += cnt
                pref_rem = (pref_rem * 10 + int(c)) % d
                
                if int(c) == d:
                    res += nrc[pref_rem]
                
                rem_cnt = nrc
                rem_cnt[pref_rem] += 1
                
            return res
        res = 0
        for d in range(1, 10):
            res += solve(d)
        
        return res