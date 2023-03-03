from collections import deque
from typing import List


# ---------- Trie Node ----------
class Node:
    __slots__ = ("child", "cnt")
    def __init__(self):
        self.child = [None, None]   # 0 and 1 branches
        self.cnt = 0                # how many numbers pass here


# ---------- Binary Trie ----------
class Trie:
    def __init__(self):
        self.root = Node()
        self.BITS = 20   # enough for nums up to 10^6

    # insert prefix xor
    def add(self, val: int):
        node = self.root
        for i in range(self.BITS, -1, -1):
            bit = (val >> i) & 1
            if not node.child[bit]:
                node.child[bit] = Node()
            node = node.child[bit]
            node.cnt += 1

    # remove prefix xor (when sliding window moves)
    def delete(self, val: int):
        node = self.root
        for i in range(self.BITS, -1, -1):
            bit = (val >> i) & 1
            node = node.child[bit]
            node.cnt -= 1

    # find max XOR with val
    def query(self, val: int) -> int:
        node = self.root
        ans = 0
        
        for i in range(self.BITS, -1, -1):
            bit = (val >> i) & 1
            want = 1 - bit
            
            if node.child[want] and node.child[want].cnt > 0:
                ans |= (1 << i)
                node = node.child[want]
            else:
                node = node.child[bit]
                
        return ans


# ---------- Main Solution ----------
class Solution:
    def maxXor(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        # 1) prefix XOR array
        px = [0] * (n + 1)
        for i in range(n):
            px[i+1] = px[i] ^ nums[i]
        
        trie = Trie()
        
        # monotonic deques to track window min/max
        minDeque = deque()
        maxDeque = deque()
        
        left = 0
        ans = 0
        
        for right in range(n):
            
            # maintain increasing deque (min)
            while minDeque and nums[minDeque[-1]] >= nums[right]:
                minDeque.pop()
            minDeque.append(right)
            
            # maintain decreasing deque (max)
            while maxDeque and nums[maxDeque[-1]] <= nums[right]:
                maxDeque.pop()
            maxDeque.append(right)
            
            # add prefix for starting index = right
            trie.add(px[right])
            
            # shrink window if max-min > k
            while nums[maxDeque[0]] - nums[minDeque[0]] > k:
                trie.delete(px[left])
                left += 1
                
                if minDeque[0] < left:
                    minDeque.popleft()
                if maxDeque[0] < left:
                    maxDeque.popleft()
            
            # query best XOR for subarray ending at right
            ans = max(ans, trie.query(px[right + 1]))
        
        return ans