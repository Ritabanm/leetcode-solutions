class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        
        lampsOnSet = set()
        # indicates ILLUMINATED lines
        rowHmap = defaultdict(int)
        colHmap = defaultdict(int)
        pDiagHmap = defaultdict(int)
        nDiagHmap = defaultdict(int)
        result = []
        
        # Turning everything on
        for r, c in lamps:
            if (r, c) not in lampsOnSet:
                lampsOnSet.add((r, c))
                # extra +1's means there are multiple lights illuminating that line
                rowHmap[r] += 1
                colHmap[c] += 1
                pDiagHmap[r+c] += 1
                nDiagHmap[r-c] += 1
        
        for r, c in queries:
            # checking if the cell is illuminated
            if (
                rowHmap.get(r, 0) > 0
                or colHmap.get(c, 0) > 0
                or pDiagHmap.get(r+c, 0) > 0
                or nDiagHmap.get(r-c, 0) > 0
            ):
                result.append(1)

                # Turning cells off
                for dr, dc in [[0,0], [0,1], [0,-1], [1,0], [-1,0], [-1,-1], [-1,1], [1,-1], [1,1]]:
                    nr = r + dr
                    nc = c + dc
                    if (nr, nc) in lampsOnSet:
                        lampsOnSet.remove((nr, nc))
                        rowHmap[nr] -= 1
                        colHmap[nc] -= 1
                        pDiagHmap[nr+nc] -= 1
                        nDiagHmap[nr-nc] -= 1
            else:
                result.append(0)
        
        return result

