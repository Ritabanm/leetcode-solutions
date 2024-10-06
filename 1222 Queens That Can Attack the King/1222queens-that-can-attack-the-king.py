class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        directions = [
            [0,1],  [1,0], [1,1],
            [0,-1], [-1,0],[-1,-1],
            [-1,1], [1,-1]
        ]
        
        # reformat queens positions
        qs = set( [f"{i}_{j}" for i, j in queens] )
        ret = []

        step = 1
        while directions:
            pos_to_remove = set()
            for pos, d in enumerate(directions):
                #print(step, d, directions)
                
                check_pos = [king[0]+ d[0]*step, king[1] + d[1]*step]                
                # if check_pos outside board - remove it
                if  not 8 >= check_pos[0] >= 0 or not 8 >= check_pos[1] >= 0:                    
                    pos_to_remove.add(pos)
                    #print(f"\tout")
                elif f"{check_pos[0]}_{check_pos[1]}" in qs:
                    #print(f"\tmatch")
                    pos_to_remove.add(pos)
                    ret.append( check_pos )
                
            directions = [d for p, d in enumerate(directions) if not p in pos_to_remove]
                     
            step+=1
        return ret