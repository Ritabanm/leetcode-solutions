class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        smallestlen = float('inf')
        tmp = [] 
        for i in range(len(s)):
            for j in range(i, len(s)):
                substr = s[i: j + 1]
                if substr.count("1") == k:
                    tmp.append(substr)
                    smallestlen = min(smallestlen, len(substr))
        tmp.sort()
        print(tmp)
        if smallestlen:
            for t in tmp:
                if len(t) == smallestlen:
                    return t.lstrip("0")
        if tmp:
            return tmp[0].lstrip("0")
        return ""


