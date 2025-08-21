class Solution:
    def findMaximalUncoveredRanges(self, n: int, ranges: List[List[int]]) -> List[List[int]]:
        if not ranges:
            return [[0, n-1]]
        ranges.sort()
        res = list()
        last_e = ranges[0][1]
        for index, r in enumerate(ranges):
            if index == 0: 
                if r[0] > 0:
                    res.append([0, r[0]-1])
            
            if r[0] <= last_e + 1:
                if r[1] > last_e:
                    last_e = r[1]
            else:
                res.append([last_e+1, r[0]-1])
                last_e = r[1]

            if index == len(ranges) - 1:
                if n > last_e + 1:
                    res.append([last_e+1, n-1])

        return res

