class Solution:
    def partitionString(self, s: str) -> List[str]:
        n = len(s)
        root = Trie()  # initialize the trie root
        start, ans = 0, []  # start pointer, and answer list
        
        while start < n:
            # Step 1: initialize the trie search
            node, end = root, start 
            while end < n and s[end] in node.children:
                node = node.children[s[end]]
                end += 1 
            if end == n: break  # reached the end of string, stop
            # found substr by closed range [start, end]
            substr = s[start: end+1]
            ans.append(substr)

            # Step 2: insert this new substring into the trie for future
            node = root
            for c in substr:
                if c not in node.children:
                    node.children[c] = Trie()
                node = node.children[c]
            # move start forward to the next block
            start += len(substr)
            
        return ans
        
class Trie:
    def __init__(self):
        self.children = {}  # maps char → child Trie