class Solution:
    def getProbability(self, balls: List[int]) -> float:
        fact = [1]
        for i in range(1, 49):
            fact.append(fact[-1] * i)
        
        def find_total_ways(box):
            total_balls = sum(box)
            ans = fact[total_balls]
            for count in box:
                ans //= fact[count]
            return ans
        
        def backtrack(idx, box_1, box_2):
            if idx == len(balls): 
                if len(box_1) == len(box_2) and sum(box_1) == sum(box_2):
                    return find_total_ways(box_1) * find_total_ways(box_2)
                else:
                    return 0
            ans = 0

            for count1 in range(balls[idx] + 1):
                count2 = balls[idx] - count1
                if count1: box_1.append(count1)
                if count2: box_2.append(count2)
                ans += backtrack(idx + 1, box_1, box_2)
                if count1: box_1.pop()
                if count2: box_2.pop()
            
            return ans
        
        total = find_total_ways(balls)
        valid = backtrack(0, [], [])
        return valid / total