from collections import defaultdict 
from collections import Counter


class Solution:
    def countCompleteSubstrings(self, word: str, k: int) -> int:
        
        #check for valid substring
        def checker(ctrseen):
            for value in ctrseen.values():
                if k != value:
                    return False
            return True
        
        # preprocess into possibly smaller valid strings
        res = []
        start = 0
        for idx in range(len(word)):
            if idx and abs(ord(word[idx]) - ord(word[idx-1])) > 2:
                res.append(word[start:idx])
                start = idx
        res.append(word[start:])
        
        # use sliding windows of k*1.. k*2.. k*3.. 
        def wordProcessor(word):
            count = 0
            for uniques in range(1, min(len(word)//k, 26)+1):
                dk = defaultdict(int)
                for start in range(0, len(word)):
                    if start + uniques*k > len(word):
                        break
                    if not start:
                        dk = Counter(word[start:start + uniques*k])
                    else:
                        dk[word[start-1]] -= 1
                        if not dk[word[start-1]]:
                            del dk[word[start-1]]
                        dk[word[start + uniques*k - 1]] += 1
                    if checker(dk):
                        count += 1
            return count

        final = 0
        for w in res:
            final += wordProcessor(w)
        return final