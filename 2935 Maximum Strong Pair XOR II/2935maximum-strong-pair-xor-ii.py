class TrieNode:
    def __init__(self):
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, num):
        node = self.root
        opp_node = self.root
        xor = 0
        for i in range(20):
            val = num[i]
            if val not in node.children:
                node.children[val] = (TrieNode(), 0)
            node.children[val] = (node.children[val][0], node.children[val][1] + 1)
            
            opp_val = '1' if val == '0' else '0' 

            if opp_val in opp_node.children:
                opp_node = opp_node.children[opp_val][0]
                xor = xor ^ (1<<(19-i))
            else:
                opp_node = opp_node.children[val][0]

            node = node.children[val][0]

        return xor
    
    def remove(self,num):
        node = self.root
        for i in range(20):
            val = num[i]
            node.children[val] = (node.children[val][0], node.children[val][1] - 1)
            if node.children[val][1] == 0:
                del node.children[val]
                return
            node = node.children[val][0]
        
class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        nums.sort()
        q = deque()
        trie = Trie()
        ans = 0
        
        for num in nums:
            while len(q) > 0 and num > 2*q[0]:
                trie.remove(format(q[0], '020b'))
                q.popleft()
            q.append(num)
            ans = max(ans,trie.insert(format(num, '020b')))
        
        return ans