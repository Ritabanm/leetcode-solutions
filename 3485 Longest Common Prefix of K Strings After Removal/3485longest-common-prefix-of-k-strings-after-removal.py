class Trie:
    def __init__(self, count):
        self.child = [None]*26
        self.count = count
        self.k_ans = None
    def insert(self, input, start=0):
        self.k_ans = None
        if start == len(input):
            return
        index = ord(input[start]) - ord('a')
        if not self.child[index]:
            self.child[index] = Trie(0)
        self.child[index].count += 1
        self.child[index].insert(input, start+1)
    def remove(self, input, start=0):
        self.k_ans = None
        if start == len(input):
            return
        index = ord(input[start]) - ord('a')
        if not self.child[index]:
            return
        if self.child[index].count == 1:
            self.child[index] = None
            return
        self.child[index].count -= 1
        self.child[index].remove(input, start+1)
    def countK(self, k):
        if self.k_ans:
            return self.k_ans
        ans = 0
        for i in range(26):
            if not self.child[i]:
                continue
            if self.child[i].count >= k:
                ans = max(ans, 1+self.child[i].countK(k))
        self.k_ans = ans
        return ans

class Solution:
    def longestCommonPrefix(self, words: List[str], k: int) -> List[int]:
        trie = Trie(0)

        for word in words:
            trie.insert(word)

        ans = []

        for word in words:
            trie.remove(word)
            ans.append(trie.countK(k))
            trie.insert(word)

        return ans
        
        