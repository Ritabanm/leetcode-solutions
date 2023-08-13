class Solution:
    def maximumLength(self, s: str) -> int:
        n = len(s)
        def is_special(sub):
            return all(c==sub[0] for c in sub)
        for length in range(n,0,-1):
            substr_count ={}
            for i in range(n-length + 1):
                substring = s[i:i+length]
                if is_special(substring):
                    if substring in substr_count:
                        substr_count[substring]+=1
                    else:
                        substr_count[substring]=1
            for sub, count in substr_count.items():
                if count>=3:
                    return length
        return -1