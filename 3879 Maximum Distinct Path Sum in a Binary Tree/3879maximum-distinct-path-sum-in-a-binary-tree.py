# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSum(self, root: Optional[TreeNode]) -> int:
        # dfs from every node, visiting all other nodes

        g = defaultdict(list) # node -> list of adj nodes

        def makeG(node):
            for ch in [node.left, node.right]:
                if ch:
                    g[node].append(ch)
                    g[ch].append(node)
                    makeG(ch)
        makeG(root)

        used = set() # used values
        seen = set() # basically our path
        res = -inf
        def dfs(node, currSum):
            nonlocal res
            used.add(node.val)
            seen.add(node)
            res = max(res, currSum)
            for adj in g[node]:
                if adj not in seen and adj.val not in used:
                    dfs(adj, currSum + adj.val)
            used.remove(node.val)
            seen.remove(node)
        
        def getScores(node):
            dfs(node, node.val)
            for ch in [node.left, node.right]:
                if ch:
                    getScores(ch)
        getScores(root)

        return res

            
