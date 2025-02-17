class Node:
    def __init__(self, count):
        self.count = count
        self.keys = set()  # Store keys with this count
        self.prev = None
        self.next = None

class AllOne:
    def __init__(self):
        self.key_count = {}  # Maps key -> count
        self.count_map = {}  # Maps count -> Node
        self.head = Node(float('-inf'))  # Dummy head (smallest count)
        self.tail = Node(float('inf'))   # Dummy tail (largest count)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _insert_node_after(self, new_node, prev_node):
        new_node.prev = prev_node
        new_node.next = prev_node.next
        prev_node.next.prev = new_node
        prev_node.next = new_node

    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        del self.count_map[node.count]

    def inc(self, key: str) -> None:
        count = self.key_count.get(key, 0)
        self.key_count[key] = count + 1
        
        curr_node = self.count_map.get(count)
        new_count = count + 1

        if new_count not in self.count_map:
            new_node = Node(new_count)
            self.count_map[new_count] = new_node
            self._insert_node_after(new_node, curr_node or self.head)

        self.count_map[new_count].keys.add(key)

        if curr_node:
            curr_node.keys.remove(key)
            if not curr_node.keys:
                self._remove_node(curr_node)

    def dec(self, key: str) -> None:
        if key not in self.key_count:
            return
        
        count = self.key_count[key]
        if count == 1:
            del self.key_count[key]
        else:
            self.key_count[key] = count - 1

        curr_node = self.count_map[count]
        new_count = count - 1

        if new_count > 0 and new_count not in self.count_map:
            new_node = Node(new_count)
            self.count_map[new_count] = new_node
            self._insert_node_after(new_node, curr_node.prev)

        if new_count > 0:
            self.count_map[new_count].keys.add(key)

        curr_node.keys.remove(key)
        if not curr_node.keys:
            self._remove_node(curr_node)

    def getMaxKey(self) -> str:
        return "" if self.head.next == self.tail else next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        return "" if self.head.next == self.tail else next(iter(self.head.next.keys))
