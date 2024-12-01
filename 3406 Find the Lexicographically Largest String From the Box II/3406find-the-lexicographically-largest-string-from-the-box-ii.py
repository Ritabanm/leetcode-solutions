class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        
        n, mx, i = len(word), word[-1],-1
        k = n-numFriends+1
        mx_pair = ''.join(max(pairwise(word)))
        while i<n:
            i = word.find(mx_pair, i+1)
            if i==-1:
                break
            mx = max(mx, word[i:i+k])
        return mx