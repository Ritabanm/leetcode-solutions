class Solution:
    def countDominantNodes(self, root: TreeNode | None) -> int:
        count = 0

        def dfs(root):
            nonlocal count

            if not root:
                return float('-inf')

            # Maximum values from left and right subtree
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)

            maxChild = max(leftMax, rightMax)

            # Current node is dominant
            if root.val >= maxChild:
                count += 1

            # Return maximum value in current subtree
            return max(root.val, maxChild)

        dfs(root)
        return count