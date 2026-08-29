class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        column_items = collections.defaultdict(list)
        queue = collections.deque([(0, root)])
        min_x = float('inf')
        max_x = float('-inf')
        res = []
        while queue:
            x, node = queue.popleft()
            column_items[x].append(node.val)
            min_x = min(min_x,x)
            max_x = max(max_x,x)

            if node.left:
                queue.append((x-1,node.left))
            if node.right:
                queue.append((x+1, node.right))

        for level in range(min_x, max_x+1):
            res.append(column_items[level])
        return res