class Solution:    
    def check(selff, points, i, res) :
        return points[i][0] <= res and points[i][1] <= res
    
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        n = len(points)
        for i in range(n) :
            points[i][0] = abs(points[i][0])
            points[i][1] = abs(points[i][1])
            
        left, right, res = 0, 10 ** 9, 0
        
        while left <= right :
            mid = left + (right - left) // 2
            temp, flag = {}, 1
            
            for i in range(n) :
                if points[i][0] <= mid and points[i][1] <= mid :
                    temp[s[i]] = temp.get(s[i], 0) + 1
                    
            for val in temp.values() :
                if val > 1:
                    flag = 0
                    break

            if flag :
                res = mid
                left = mid + 1

            else :
                right = mid - 1
            
        ans = 0
        for i in range(n) :
            if self.check(points, i, res) :
                ans += 1

        return ans