# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        
        seen = set(nodes)

        def dfs(root):
            if root in seen:
                return root

            if not root:
                return None

            left = dfs(root.left)
            right = dfs(root.right)

            if left and right:
                return root
            
            if left and not right:
                return left
        
            if right and not left:
                return right
            
            return None

        return dfs(root)






        
        
        
        
        
        
        
        # seen = set(nodes)
        # for n in nodes:
        #     seen.add(n.val)

        # ans = None
        # counter = len(seen)




        # def dfs(root, counter):
        #     nonlocal ans
        #     if not root:
        #         return counter  

        #     left = counter - dfs(root.left, counter)
        #     right = counter - dfs(root.right, counter)

        #     if root.val in seen:
        #         counter -= 1

        #     if left:
        #         counter -= left
            
        #     if right:
        #         counter -= right

        #     if counter <= 0:
        #         ans = root

        #     return counter

        # dfs(root, counter)

        # return ans

        