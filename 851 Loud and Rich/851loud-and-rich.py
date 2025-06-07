class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        N = len(quiet)
        
        # final result
        result = list(range(0, N))
        
        # richer_count[i]: number of people richer than person `i`
        richer_count = [0] * N
        
        # graph[i]: a list, all the person that person `i` is richer than
        graph = [[] for i in range(0, N)]
        
        for r in richer:
            richer_count[r[1]] += 1
            graph[r[0]].append(r[1])
        
        # BFS, starting nodes
        stack = [i for i in range(0, N) if richer_count[i] == 0]
                
        while len(stack) > 0:
            top = stack[-1]
            stack.pop()
            
            for n in graph[top]:
                richer_count[n] -= 1
                if richer_count[n] == 0:
                    stack.append(n)
                
                if quiet[result[n]] > quiet[result[top]]:
                    result[n] = result[top]
        
        return result