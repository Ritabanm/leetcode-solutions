class Solution:
    def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:
        n = len(coins)
        ans = n - 1
        
        adj = [set() for i in range(n)]
        for i, j in edges:
            adj[i].add(j)
            adj[j].add(i)
                
        l = [i for i in range(n) if len(adj[i]) == 1 and coins[i] == 0]
        while l:
            nextlayer = []
            for i in l:
                # Prune leaf i
                ans -= 1
                if adj[i]:
                    j = list(adj[i])[0]
                    adj[j].remove(i)
                    adj[i].remove(j)
                    if len(adj[j]) == 1 and coins[j] == 0:
                        nextlayer.append(j)
            l = nextlayer[:]
        
        l = [i for i in range(n) if len(adj[i]) == 1]
        
        for _ in range(2):
            nextlayer = []
            for i in l:
                ans -= 1
                if adj[i]:
                    j = list(adj[i])[0]
                    adj[j].remove(i)
                    if len(adj[j]) == 1:
                        nextlayer.append(j)
            l = nextlayer[:]
            
        return 2 * max(0, ans)