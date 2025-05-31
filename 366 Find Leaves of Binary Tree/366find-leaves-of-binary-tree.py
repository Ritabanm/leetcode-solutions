class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        # Stores parent nodes for each child node
        parent_map = defaultdict(list)
        # List to hold current leaves
        leaves = []

        # BFS queue initialization, starting with the root
        queue = deque([root])

         # Traverse the tree using BFS, record parent nodes and find initial leaves
        while queue:
            node = queue.popleft()
            if node.left:
                parent_map[node.left].append(node)
                queue.append(node.left)
            if node.right:
                parent_map[node.right].append(node)
                queue.append(node.right)

            # If the node is a leaf (no children), add it to the leaves list
            if not node.left and not node.right:
                leaves.append(node)

        result = []

        # Process each round of leaves        
        while leaves:
            current_leaves = []
            next_leaves = []

            # Remove current leaves and check their parents
            for leaf in leaves:
                current_leaves.append(leaf.val)
                for parent in parent_map[leaf]:
                    # Remove the leaf from its parent
                    if parent.left == leaf:
                        parent.left = None
                    if parent.right == leaf:
                        parent.right = None
                    # If the parent becomes a new leaf, add it to the next round
                    if not parent.left and not parent.right:
                        next_leaves.append(parent)
            
            # Add current leaves to the result and move to the next round
            result.append(current_leaves)
            leaves = next_leaves
        
        return result
     
        