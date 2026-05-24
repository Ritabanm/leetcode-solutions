from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: TreeNode):
        if not root:
            return []

        result = []
        queue = deque([root])
        left_to_right = True

        while queue:
            level_size = len(queue)
            level_nodes = deque()  # Using deque for efficient front/back appends

            for _ in range(level_size):
                node = queue.popleft()
                
                # Append based on direction
                if left_to_right:
                    level_nodes.append(node.val)
                else:
                    level_nodes.appendleft(node.val)

                # Add child nodes for next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(list(level_nodes))  # Convert deque to list
            left_to_right = not left_to_right  # Toggle direction
        
        return result
