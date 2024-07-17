class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if len(dist)>math.ceil(hour):
            return -1

        min_speed = float('inf')
        right = 10**9
        left = 1
        
        while left < right:
            # print(left, right)
            middle = (left + right)//2
            tm = 0
            for i, d in enumerate(dist):
                if i == len(dist)-1:
                    tm += d/middle
                    break
                tm += math.ceil(d/middle)
            if tm <= hour:
                right = middle
            else:
                left = middle+1
            # if left == right-1:
            #     break
        
        return left
            