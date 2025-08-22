class Solution:
    def flipBinaryTree(self, root: 'Node', leaf: 'Node') -> 'Node':        
        prev, node = None, leaf
        while node: 
            if node == root:
                if prev == node.right: node.right = None
                else: node.left = None
            else: 
                if prev == node.right: node.right = node.left 
                node.left = node.parent
            node.parent, node, prev = prev, node.parent, node 
        return leaf