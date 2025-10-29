class Solution:
    def getHint(self, secret, guess):
        h = Counter(secret)
        bulls = cows = 0
        for idx, ch in enumerate(guess):
            if ch in h:
                if ch == secret[idx]:
                    bulls+=1
                    cows-=int(h[ch]<=0)
                else:
                    cows+=int(h[ch]>0)
                h[ch]-=1
        return "{}A{}B".format(bulls,cows)