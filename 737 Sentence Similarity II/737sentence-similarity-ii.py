class DJS:
    def __init__(self):
        self._d = {}
    
    def _safe_make_set(self, a):
        if a not in self._d:
            self._d[a] = a

    def find(self, a):
        aa = self._d[a]
        if a == aa:
            return a
        self._d[a] = self.find(aa)
        return self._d[a]
    
    def union(self, a, b):
        self._safe_make_set(a)
        self._safe_make_set(b)
        aa = self.find(a)
        bb = self.find(b)
        if aa != bb:
            self._d[aa] = bb
    
    def is_in_one_group(self, a, b):
        if a not in self._d or b not in self._d:
            return False
        return self.find(a) == self.find(b)

class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        
        djs = DJS()
        for a, b in similarPairs:
            djs.union(a, b)

        for a, b in zip(sentence1, sentence2):
            if a != b and not djs.is_in_one_group(a, b):
                return False
        return True