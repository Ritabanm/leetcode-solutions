class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        # A mapping of nodes to (leaf, distance) pairs
        self.nodesToLeavesAndDistances = {}
        # A mapping of leaves to the associated path to the root
        self.leavesToPaths = {}

        # Leaves are all nodes in the range [0, n-1] 
        # that do not appear as a parent
        leaves = []
        allParents = set(parent)
        for i in range(n): 
            if i not in allParents: 
                leaves.append(i)
        
        # Iteratively construct the path from each leaf to the root
        for leaf in leaves: 
            self.nodesToLeavesAndDistances[leaf] = (leaf, 0)
            path = [leaf]
            cur = parent[leaf]
            prev = leaf
            # Update the leaf associated with each node along the path 
            # as well as its distance to the current leaf
            while cur != -1: 
                path.append(cur)
                self.nodesToLeavesAndDistances[cur] = (leaf, self.nodesToLeavesAndDistances[prev][1] + 1)
                prev = cur
                cur = parent[cur]
            self.leavesToPaths[leaf] = tuple(path)


    def getKthAncestor(self, node: int, k: int) -> int:
        # Transform the problem from 'find the kth ancestor of node' 
        # to 'find the k + dist ancestor of the node's stored leaf'
        leaf, dist = self.nodesToLeavesAndDistances[node]
        distFromLeaf = k + dist
        # Return -1 if there aren't enough nodes in the stored path
        if distFromLeaf >= len(self.leavesToPaths[leaf]):
            return -1
        return self.leavesToPaths[leaf][distFromLeaf]
        


# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)