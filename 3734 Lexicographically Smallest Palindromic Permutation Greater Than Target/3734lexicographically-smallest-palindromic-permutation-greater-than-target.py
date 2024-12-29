class Solution:
    def lexPalindromicPermutation(self, S, T):
        N = len(S)
        count = Counter(S)
        
        odds = "".join(c for c in count if count[c] & 1)
        if len(odds) != N & 1:
            return ""
        for c in count:
            count[c] //= 2
        
        def check(left_half):
            nonlocal ans
            cand = left_half + odds + left_half[::-1]
            if cand > T and (ans == "" or cand < ans):
                ans = cand

        ans = ""
        for i, t in enumerate(T):
            if i >= N // 2:
                check(T[:i])
                break
            
            for c in sorted(count):
                if c > t and count[c]:
                    count[c] -= 1
                    left = T[:i] + c + "".join(x * count[x] for x in sorted(count))
                    check(left)
                    count[c] += 1
                    break
            
            count[t] -= 1
            if count[t] < 0:
                break
        
        return ans