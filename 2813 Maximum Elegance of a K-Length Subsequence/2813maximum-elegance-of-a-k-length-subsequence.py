class Solution:
    def findMaximumElegance(self, items: List[List[int]], k: int) -> int:
        # Sort items by profit
        items.sort(key=lambda x: -x[0])
        total_profit = 0
        distinct = 0
        # to track unqiue categories
        seen = set()
        # will store duplicates categories
        duplicates = []
        n = len(items)

        # pick first k items to ensure high total profit
        for i in range(min(k, n)):
            profit, category = items[i]
            total_profit += profit
            if category in seen:
                heapq.heappush(duplicates, profit)
            else:
                seen.add(category)
                distinct += 1
        max_elegance = total_profit + distinct*distinct
        # for remaining items 
        for i in range(k, len(items)):
            profit, category = items[i]
            if category not in seen and duplicates:
                # remove duplicate with lowest profit
                smallest_profit = heapq.heappop(duplicates)
                total_profit += profit-smallest_profit
                seen.add(category)
                distinct += 1
                max_elegance = max(max_elegance, total_profit+distinct*distinct)
        
        return max_elegance