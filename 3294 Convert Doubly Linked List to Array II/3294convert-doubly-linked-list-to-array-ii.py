"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
"""
class Solution:
    def toArray(self, node: 'Optional[Node]') -> List[int]: 
        if not node:  # 🚨 Edge case handling!
            return []
            
        array = collections.deque()  # 🎒 Our magical bag
        
        # 🔙 Collect all nodes BEFORE current (including current)
        curr = node 
        while curr: 
            array.appendleft(curr.val)  # 👈 Add to left side
            curr = curr.prev 
        
        # 🔜 Collect all nodes AFTER current  
        curr = node.next if node else None 
        while curr: 
            array.append(curr.val)  # 👉 Add to right side
            curr = curr.next 
            
        return list(array)  # 🎯 Convert to final array!