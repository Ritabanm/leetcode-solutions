class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        cnt = [0 for _ in range(256)]

        l,r,n, res =0,0, len(s),0
        while r<n:
            cur = ord(s[r])
            cnt[cur]+=1
            while l<=r and cnt[cur]>=k:
                res+=n-r
                cnt[ord(s[l])]-=1
                l+=1
            r+=1
        return res
        