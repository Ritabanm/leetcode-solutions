class Solution:
    def checkEquivalence(self, root1: 'Node', root2: 'Node') -> bool:

        def dfs(node):

            ctr[node.val]+= inc

            if node.left : dfs(node.left )
            if node.right: dfs(node.right)

            return    


        ctr, inc = Counter(), 1
        dfs(root1)

        inc = -1
        dfs(root2)

        return not(ctr - Counter())     # Subtracting the null Counter
                                        # voids the zero values in ctr