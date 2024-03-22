class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        p = []
        r = []

        for i in range(1, m+1):
            p.append(i)
        for i in queries:
            r.append(p.index(i))
            p.remove(i)
            p.insert(0, i)
        return r