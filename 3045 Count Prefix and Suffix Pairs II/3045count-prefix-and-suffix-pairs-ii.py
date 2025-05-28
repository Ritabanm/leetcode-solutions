class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.count = 0

   
class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        
        root = TrieNode()
        res = 0
        for w in words:
            x = root
            reversed_w = w[::-1]  # Reversed version of the word
            for i in range(len(w)):
                key = (w[i], reversed_w[i])
                x = x.children[key]
                res += x.count
            x.count += 1
        return res