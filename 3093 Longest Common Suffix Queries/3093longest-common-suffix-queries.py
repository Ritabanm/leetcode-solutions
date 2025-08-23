class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        class TrieNode:
            def __init__(self, c, i, n):
                self.c = c
                self.i = i
                self.n = n
                self.children = {}
                
        class Trie:
            def __init__(self):
                self.root = TrieNode('', inf, inf)
            
            def update(self, word, i, n):
                curr = self.root
                if n < curr.n:
                    curr.i = i
                    curr.n = n
                for c in word:
                    if c in curr.children:
                        curr = curr.children[c]
                        if n < curr.n:
                            curr.i = i
                            curr.n = n
                    else:
                        curr.children[c] = TrieNode(c, i, n)
                        curr = curr.children[c]
            
            def get_index(self, word):
                curr = self.root
                i = curr.i
                for c in word:
                    if c not in curr.children:
                        return i
                    curr = curr.children[c]
                    i = curr.i
                return i
                
        trie = Trie()
        for i, word in enumerate(wordsContainer):
            trie.update(word[::-1], i, len(word))
            
        ans = []
        for i, word in enumerate(wordsQuery):
            ans.append(trie.get_index(word[::-1]))
        
        return ans
                