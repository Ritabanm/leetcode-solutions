from collections import deque
import heapq

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        if sum(rains) == 0:
            return 0

        already_rained = {}

        lake_occurence = {}

        for i in range(len(rains)):
            if rains[i] not in lake_occurence:
                lake_occurence[rains[i]] = deque()
            
            lake_occurence[rains[i]].append(i)

            already_rained[rains[i]] = False
        
        for i in lake_occurence:
            lake_occurence[i].popleft()
        
        heap = []

        answer = []

        for i in rains:
            if i == 0:
                if heap:
                    dried_lake = heapq.heappop(heap)[1]
                    already_rained[dried_lake] = False
                    answer.append(dried_lake)
                else:
                    answer.append(1)
            else:
                if already_rained[i]:
                    return []
                
                already_rained[i] = True

                answer.append(-1)
                heapq.heappush(heap, (lake_occurence[i].popleft() if lake_occurence[i] else float('inf'), i))

        return answer