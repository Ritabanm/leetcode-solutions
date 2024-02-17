class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        points=0
        #sliding window
        for i in range(len(calories)-k+1):
            if i==0:s=sum(calories[:k])
            else:s=s-calories[i-1]+calories[i+k-1]
            if s<lower:points-=1
            elif s>upper: points+=1
            
        return points