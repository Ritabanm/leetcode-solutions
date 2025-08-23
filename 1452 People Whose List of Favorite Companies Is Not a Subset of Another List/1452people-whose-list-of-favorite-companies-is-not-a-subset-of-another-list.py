class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:

        ans, n = set(), len(favoriteCompanies)

        favs = [(set(x), i) for i, x in enumerate(favoriteCompanies)]
        
        favs.sort(key = lambda x: -len(x[0]))
        
        for i, (p1, _) in enumerate(favs):
            for p2, j in favs[i + 1:]:
                if p2 < p1: ans.add(j)
                    
        return sorted(set(range(n)) - ans)