class Solution:
    def countPairs(self, n, edges, queries):
        dict1, dict2, result = [0]*(n+1), defaultdict(int), []

        for a,b in edges:
            dict1[a] += 1 
            dict1[b] += 1 
            dict2[(min(a,b),max(a,b))] += 1 

        ans = sorted(dict1)

        for q in queries:
            total, left, right = 0, 1, n
            while left < right:
                if ans[left] + ans[right] > q:
                    total += right-left 
                    right -= 1 
                else:
                    left += 1 
            for u,v in dict2:
                if dict1[u] + dict1[v] > q and dict1[u] + dict1[v] - dict2[(u,v)] <= q:
                    total -= 1 
            result.append(total)

        return result 