class Solution:
    def minimumKeypresses(self, s: str) -> int:
        c = collections.Counter(s)
        ans = cnt = 0
        for i,freq in enumerate(sorted(c.values(), reverse = True)):
            if i%9==0:
                cnt +=1
            ans += cnt*freq
        return ans