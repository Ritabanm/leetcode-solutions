class Solution:
    def detectCycle(self, head):

        node_seen = set()
        node = head

        while node and node is not None:
            if node in node_seen:
                return node
            else:
                node_seen.add(node)
                node = node.next
        return node