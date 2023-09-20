class Solution:
    def checkOverlap(self, radius: int, x_center: int, y_center: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        if x1 <= x_center <= x2 and y1 <= y_center <= y2: 
            return True # circle inside rectangle
        
        for x, y in (x1, y1), (x1, y2), (x2, y1), (x2, y2): 
            if (x - x_center)**2 + (y - y_center)**2 <= radius**2: 
                return True 
        # check edge 
        for x in [x1, x2]: 
            if x_center - radius <= x <= x_center + radius and y1 <= y_center <= y2: return True
            
        for y in [y1, y2]:
            if y_center - radius <= y <= y_center + radius and x1 <= x_center <= x2: return True 
        
        return False 