class Solution:
    def aggregateTimeSeries(self, series1: list[list[int]], series2: list[list[int]]) -> list[list[int]]:
        # Get all unique timestamps from both series
        timestamps = sorted(list(set(t for t, _ in series1) | set(t for t, _ in series2)))
        
        n1, n2 = len(series1), len(series2)
        i, j = 0, 0
        ans = []
        
        for t in timestamps:
            # Move i forward until series1[i][0] >= t
            while i < n1 and series1[i][0] < t:
                i += 1
            # Move j forward until series2[j][0] >= t
            while j < n2 and series2[j][0] < t:
                j += 1
                
            # The value comes from the next available timestamp (at index i or j if they exist and are >= t)
            val1 = series1[i][1] if i < n1 else 0
            val2 = series2[j][1] if j < n2 else 0
            
            ans.append([t, val1 + val2])
            
        return ans