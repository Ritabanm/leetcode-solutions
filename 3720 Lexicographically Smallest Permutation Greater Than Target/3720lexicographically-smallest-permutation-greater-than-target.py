from collections import Counter

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        def build(prefix, cnt, greater):
            nonlocal ans
            if ans:
                return
            if len(prefix) == n:
                if ''.join(prefix)>target:
                    ans=''.join(prefix)
                return
            for c in chars:
                if cnt[c] == 0:
                    continue
                if not greater and c<target[len(prefix)]:
                    continue
                cnt[c] -= 1
                build(prefix+[c], cnt, greater or c>target[len(prefix)])
                cnt[c] +=1
                if ans:
                    return
                
        n = len(s)
        counts = Counter(s)
        chars = sorted(counts)
        ans = ""
        build([], counts.copy(), False)
        return ans