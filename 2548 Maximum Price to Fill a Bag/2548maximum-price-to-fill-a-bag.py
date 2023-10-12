class Solution:
    def maxPrice(self, items: List[List[int]], capacity: int) -> float:
        items = sorted(items, key=lambda x: -(x[0]/x[1]))

        cost = 0

        for item in items:
            if capacity > 0:
                if item[1] <= capacity:
                    cost += item[0]
                    capacity -= item[1]
                else:
                    ratio = item[0] / item[1]
                    print(ratio)
                    cost += capacity * ratio
                    capacity -= item[1]
                    
        if capacity > 0:
            return -1
        
        return cost