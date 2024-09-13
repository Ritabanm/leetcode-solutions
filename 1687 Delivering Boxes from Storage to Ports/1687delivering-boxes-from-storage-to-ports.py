class Solution:
    def boxDelivering(self, boxes: List[List[int]], portsCount: int, maxBoxes: int, maxWeight: int) -> int:
        n = len(boxes)

        @lru_cache(None)
        def dp(idx):
            # End case, No trips if we already delivered all
            if idx==n:
                return 0
            # Keeps track of the initial starting position for the recursion
            start = idx
            # Tracks the weight of boxes in current recursion
            weight = 0
            # Number of trips for current recursion
            trips = 1
            # Last port visited
            last = None
            # Starting Index of last port visited
            lastidx = -1
            while(idx<n):
                weight+=boxes[idx][1]
                # If the port is different, add a trip and updates the last port values
                if boxes[idx][0]!=last:
                    trips+=1
                    last = boxes[idx][0]
                    lastidx = idx
                # If weight exceeds, break since we cannot handle the current port
                if weight>maxWeight:
                    break
                # If the number of boxes reached the threshold, break since we are at capacity
                if (idx-start+1)==maxBoxes:
                    idx+=1
                    break
                idx+=1
            
            # Case 1: Keeping the boxes in current iteration greedily
            res = trips+ dp(idx)
            # Case 2: If the next port matches the last one, we can try to put those boxes in next trip
            # We should make sure we put at least 1 box in this trip though so compare lastidx with start
            if idx<n and last == boxes[idx][0] and lastidx!=start:
                res = min(res, trips-1 + dp(lastidx))
            return res
        
        return dp(0)