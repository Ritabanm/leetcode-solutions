class Solution:
    def buildWall(self, height: int, width: int, bricks: List[int]) -> int:
        bricks=[brick for brick in bricks if brick<=width]
        bricks.sort()
        self.layouts=[]
        def create_all_layouts(current_width,current):
            if current_width<0:
                return
            if current_width==0:
                self.layouts.append(tuple(current.copy()))
                return
            for brick in bricks:
                current.append(brick)
                create_all_layouts(current_width-brick,current)
                current.pop()
        
        create_all_layouts(width,[])

        @cache
        def compare_adjacent_layouts(row1, row2):
            joints=set()
            total=0
            for brick in row1[:-1]:
                total+=brick
                joints.add(total)
            total=0
            for brick in row2[:-1]:
                total+=brick
                if total in joints: return False
            return True

        
        @cache
        def dfs(current_height,previous_layout):
            # print(f"current height {current_height}")
            if current_height==height: return 1
            ans=0
            walls=[]
            # create_all_layouts(width,[],walls)
            # print(f"walls at {current_height} is {walls}")
            for layout in self.layouts:
                if compare_adjacent_layouts(previous_layout,layout):
                    # print(f"{current_height} has valid wall {previous} and  {wall}")
                    ans+=dfs(current_height+1,layout)
            return ans
        return dfs(0,())%(10**9+7)