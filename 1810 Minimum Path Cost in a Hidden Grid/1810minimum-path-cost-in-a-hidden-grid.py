# """
# This is GridMaster's API interface.
# You should not implement it, or speculate about its implementation
# """
#class GridMaster(object):
#    def canMove(self, direction: str) -> bool:
#        
#
#    def move(self, direction: str) -> int:
#        
#
#    def isTarget(self) -> None:
#        
#

import heapq
import copy

class Solution(object):
    def findShortestPath(self, master: 'GridMaster') -> int:
        """
        we can easily solve this problem using heap and visited set
        """
        heap = []
        visited = {(0,0)}
        direction = {'U': (0,-1), 'D': (0,1), 'L': (-1, 0), 'R': (1, 0)}
        heapq.heappush(heap, (0, 0, 0, copy.copy(master)))
        while len(heap):
            cost, i, j, master = heapq.heappop(heap)
            if master.isTarget():
                return cost
            for key, value in direction.items():
                if master.canMove(key) and (i+value[0], j+value[1]) not in visited:
                    master_copy = copy.copy(master)
                    x = master_copy.move(key)
                    heapq.heappush(heap, (x+cost, i+value[0], j+value[1], master_copy))
                    visited.add((i+value[0], j+value[1]))
        return -1

