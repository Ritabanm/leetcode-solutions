class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:

        # adj[node] -> [adj nodes]
        adj = []
        for _ in range(n + 1):
            adj.append([])
        
        # populate the above map
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        # dfs to find the path between node 1 and the target node, don't go back to the source
        # since there are no cycles, all we need to do is not go back to the source to avoid revising nodes
        res_path = []
        curr_path = []
        def dfs(node: int, source: int):

            # push the current node onto the stack
            curr_path.append(node)

            # if the current node is the target, we can stop
            if node == target:
                for n in curr_path: res_path.append(n)
                return
            
            # otherwise, dfs adjacent nodes
            for adj_node in adj[node]:
                if adj_node != source:
                    dfs(adj_node, node)
            
            # pop the current node off as we go up the stack frame
            curr_path.pop()
        
        # spawn the dfs
        dfs(1, -1)

        # if there are fewer timesteps than jumps, we return a probability of 0
        if t < (len(res_path) - 1):
            return 0
        
        # if there are more timesteps than jumps and it's possible to go past the target, we return a probability of 0
        if t > (len(res_path) - 1) and len(adj[target]) > 1:
            return 0
        
        # edge case: if the target is 1 and we have children, we return a probability of 0
        if t > 0 and target == 1 and len(adj[1]) > 0:
            return 0
        
        # for each node in the path, see the probability of jumping to the next node given that we can't jump to the previous node
        res = 1
        for i in range(len(res_path) - 1):
            
            # grab the nodes, dummy index for previous node
            prev_node = -1
            curr_node = res_path[i]
            next_node = res_path[i + 1]

            # replace previous node if we can
            if i != 0:
                prev_node = res_path[i - 1]
            
            # count the number of adjacent nodes we have from the curr node such that they aren't the previous node
            possible_jumps = 0
            for adj_node in adj[curr_node]:
                if adj_node != prev_node:
                    possible_jumps += 1
            
            # update res
            res *= (1 / possible_jumps)
        
        return res