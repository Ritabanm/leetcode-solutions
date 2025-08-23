class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        answer = [-1]
        stack = [(0, 0)]    # contains select cars of the current fleet
        idx = -1            # index of the car at front of current fleet
        
        for i in range(len(cars) - 2, -1, -1):
            b1, m1, b2, m2 = *cars[i], *cars[idx]

            # get collision time of cars[i] with car at front of current fleet
            t = (b2 - b1) / (m1 - m2) if m1 > m2 else -1
            
            # cars[i] cannot collide with the current fleet in front of it
            if t == -1:

                # create a new fleet with cars[i] as the car at the front of the fleet
                stack = [(0, 0)]
                idx = i

            else:

                # find when cars[i] collides with the current fleet in front of it
                for k, (j, t_front) in enumerate(stack):

                    # cars[i] collides with current fleet when cars[stack[k - 1][0]]
                    # (or cars[idx] when k == 0) is at front of fleet
                    if t >= t_front:

                        # cars following cars[i] cannot collide with current fleet
                        # when cars in stack[k:] are at front of fleet
                        stack = stack[:k] + [(i, t), (0, 0)]
                        break
                    
                    # get collision time of cars[i] and cars[stack[k][0]] 
                    # assuming cars[stack[k][0]] hasn't yet collided with
                    # cars[stack[k - 1][0]] (or cars[idx] when k == 0)
                    else:
                        b2, m2 = cars[j]
                        t = (b2 - b1) / (m1 - m2)

            answer.insert(0, t)
        
        return answer