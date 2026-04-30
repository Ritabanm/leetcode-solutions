class Solution:
    def sortVowels(self, s: str) -> str:

        d = defaultdict(int)
        ans = []

        for ch in s:
            if ch in 'aeiou': d[ch]+= 1

        d = sorted(d.items(), key = lambda x: -x[1])
        vowels = iter(''.join(ch * cnt for ch, cnt in d))

        for ch in s:
            if ch in 'aeiou': ans.append(next(vowels))
            else: ans.append(ch)

        return ''.join(ans)
        