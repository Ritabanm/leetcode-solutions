from collections import defaultdict, deque
class Solution:
    def verticalTraversal(self, root):
        column_table = defaultdict(list)
        queue = deque([(root, 0,0)])
        while queue:
            node, row, col = queue.popleft()
            if node:
                column_table[col].append((row, node.val))
                queue.append((node.left, row+1,col-1))
                queue.append((node.right, row+1, col+1))
        return [[val for row, val in sorted(column_table[col])]
        for col in sorted(column_table.keys())]
