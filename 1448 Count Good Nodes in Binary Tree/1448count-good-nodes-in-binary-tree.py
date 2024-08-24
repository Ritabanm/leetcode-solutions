class Solution:
    def goodNodes(self, root):
        def dfs(node, max_sofar):
            nonlocal num_good_nodes
            if max_sofar<=node.val:
                num_good_nodes+=1
            if node.right:
                dfs(node.right, max(node.val, max_sofar))
            if node.left:
                dfs(node.left, max(node.val, max_sofar))
        num_good_nodes = 0
        dfs(root, float("-inf"))
        return num_good_nodes