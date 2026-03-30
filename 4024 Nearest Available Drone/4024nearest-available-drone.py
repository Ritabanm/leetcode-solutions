
class Solution:
    def nearestDrone(self, drones: list[list[int]], target: list[int]) -> int:

        res, (tx, ty) = (inf, -1), target

        for i, (x, y, r) in enumerate(drones):
            
            dist = abs(tx - x) + abs(ty - y)
            if dist > r: continue
            if dist < res[0]:
                res = (dist, i)

        return res[1]