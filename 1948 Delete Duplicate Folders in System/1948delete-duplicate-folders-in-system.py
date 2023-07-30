# \U0001d4a6\U0001d4be\U0001d4c3\U0001d4b9\U0001d4c1\U0001d4ce \U0001d4b0\U0001d4c5\U0001d4cbℴ\U0001d4c9ℯ \U0001d4be\U0001d4c9 ℋℯ\U0001d4c1\U0001d4c5\U0001d4c8\U0001f44d
class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        tree = {}
        for path in paths:
            curr = tree
            for name in path:
                curr = curr.setdefault(name, {})

        def encode(node):
            if not node:
                return "()"
            parts = []
            for key, sub in node.items():
                parts.append(key + encode(sub))
            sign = "".join(sorted(parts))
            store[sign].append(node)
            return "(" + sign + ")"

        def remove(nodes):
            for item in nodes:
                item.clear()
                item["#"] = True

        store = defaultdict(list)
        encode(tree)
        for group in store.values():
            if len(group) > 1:
                remove(group)

        def collect(node, path):
            for key, sub in list(node.items()):
                if "#" in sub:
                    continue
                new = path + [key]
                result.append(new)
                collect(sub, new)

        result = []
        collect(tree, [])
        return result