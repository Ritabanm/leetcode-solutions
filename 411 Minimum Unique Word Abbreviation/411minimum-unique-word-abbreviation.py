class TrieNode:

    def __init__(self):
        self.children = {}


class Trie:

    def __init__(self):
        self.root = TrieNode()

    
    def add(self, word):
        node = self.root

        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()

            node = node.children[c]


    def good(self, word):
        node = self.root

        @cache
        def calc(index, node):
            if index == len(word):
                return False

            if word[index].isnumeric():
                num = ""
                while index < len(word) and word[index].isnumeric():
                    num += word[index]
                    index += 1
                
                num = int(num)
                best = True

                q = deque()
                q.append(node)
                level = num

                while level:
                    nxt = deque()

                    while q:
                        cur_node = q.popleft()

                        for nxt_node in cur_node.children.values():

                            nxt.append(nxt_node)

                    q = nxt
                    level -= 1

               

                for nxt_node in q:
                    best &= calc(index, nxt_node)
                    if not best: return False

                return best






            else:
                if word[index] in node.children:
                    return calc(index + 1, node.children[word[index]])

                return True

        

        return calc(0, node)


class Solution:
    def minAbbreviation(self, target: str, dictionary: List[str]) -> str:
        dictionary = [d for d in dictionary if len(d) == len(target)]


        T = Trie()
        for x in dictionary:
            T.add(x)


        
        N = len(target)
        s = set()
        def calc(index, cur):
            if index == N:
                s.add(cur)
                return

            if cur[-1].isnumeric():
                calc(index + 1, cur + target[index])
                return

            for j in range(index, N):
                calc(j + 1, cur + str(j - index + 1))

            calc(index + 1, cur + target[index])
    
        

        for i in range(N):
            calc(i + 1, str(i + 1))

        calc(1, target[0])

        arr = sorted(list(s), key=lambda x: (len(x), x))

        
        for x in arr:
            if T.good(x):
                
                return x

        return target
            


        