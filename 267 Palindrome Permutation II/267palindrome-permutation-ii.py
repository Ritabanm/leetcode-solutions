class Solution:
    def __init__(self):
        self.ans = []
        
    def generate(self, counter, mid, n):
        if not n:
            self.ans.append(mid)
            return
        for i in counter:
            if counter[i] > 0:
                counter[i] -= 2
                self.generate(counter, i + mid + i, n-2)
                counter[i] += 2
        
    def generatePalindromes(self, s: str) -> List[str]:
        counter = collections.Counter(s)
        cnt = 0
        c = None
        n = len(s)
        for i in counter:
            if counter[i] % 2:
                cnt += 1
                c = i
        if cnt > 1:
            return []
        else:
            if cnt:
                counter[c] -= 1
                self.generate(counter, c, n-1)
            else:
                self.generate(counter, '', n)
            return self.ans