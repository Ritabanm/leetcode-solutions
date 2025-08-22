class Solution:
    def cheapestJump(self, coins: List[int], maxJump: int) -> List[int]:
        if coins[-1] == -1: return []
        n = len(coins)

        # 1. We will go from right to left, calculating cost of getting to the end.
        cost = [inf]*n
        cost[-1] = 0

        # Monotonic queue for indices that we've seen so far.
        # From head to tail indices are decreasing, and the cost of getting from
        # them to the end is increasing.
        queue = deque([n-1])
        for i in range(n-2, -1, -1):
            if coins[i] == -1: continue
            # Remove indices that are too far
            while queue and queue[0] > i + maxJump:
                queue.popleft()
            # No indices left, means there was a large gap of -1s
            if not queue: return []
            # We should always jump to the head of the queue, because it has lowest cost
            cost[i] = coins[i] + cost[queue[0]]
            # Remove items from the tail that are worse than current,
            # i.e. they have higher cost and longer to go.
            while queue and cost[queue[-1]] >= cost[i]:
                queue.pop()
            queue.append(i)
        min_cost = cost[0]
        if min_cost == inf: return []

        # 2. Now that we know the cost of getting to the end from each index,
        # we should simply pick the first index that has the optimal cost each time.
        ans = []
        for i in range(n):
            if cost[i] == min_cost:
                ans.append(i+1)
                min_cost -= coins[i]
        return ans
        
        
        