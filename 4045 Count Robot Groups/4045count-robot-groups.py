class Solution:
    def countGroups(self, position: list[int], speed: list[int], distance: int) -> int:

        count=0 # number of attached robots

        if len(position) == 1:
            return 1

        for i in range(len(position)-1,0,-1): 

            if speed[i] >= speed[i-1] and position[i] - position[i-1] > distance:

                continue
            
            else:

                speed[i-1] = speed[i] # change the speed to the right robot as they gave in the question
                count+=1
            

        return len(position) - count # return the robots by counting the combined robots as a single robot and subtract it to return the number of robots
