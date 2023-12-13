class Solution:
    def filterOccupiedIntervals(self, occupiedIntervals: List[List[int]], freeStart: int, freeEnd: int) -> List[List[int]]:
        occupiedIntervals.sort()
        merged = []
        i = 0
        while i < len(occupiedIntervals):
            j = i
            while j < len(occupiedIntervals) and occupiedIntervals[i][1] >= occupiedIntervals[j][0] - 1:
                occupiedIntervals[i][1] = max(occupiedIntervals[i][1], occupiedIntervals[j][1])
                j += 1
            merged.append(occupiedIntervals[i])
            i = j

        ans = []
        i = 0
        while i < len(merged) and merged[i][1] < freeStart: 
            ans.append(merged[i])
            i += 1
        if i == len(merged): return ans
        if freeStart > merged[i][0]: 
            ans.append([merged[i][0], freeStart - 1])
            
        j = i
        while j < len(merged) and merged[j][1] <= freeEnd: j += 1
        if j == len(merged): return ans
        if freeEnd < merged[j][1]:
            if freeEnd >= merged[j][0]: ans.append([freeEnd + 1, merged[j][1]])
            else: ans.append(merged[j])

        ans.extend(merged[j+1:])
        return ans