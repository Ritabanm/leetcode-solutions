class Solution:
    def countCollisions(self, directions: str) -> int:
        has_stationary, right, collisions = False, 0, 0
        for direction in directions:
            if direction == 'R':
			    # Just record number of right-moving cars. We will resolve them when we encounter a left-moving/stationary car.
                right += 1
            elif direction == 'L' and (has_stationary or right > 0): 
			    # Left-moving cars which don't have any existing right-moving/stationary cars to their left can be ignored. They won't hit anything.
				# But if there are right-moving/stationary cars, it will result in collisions and we can resolve them.
				# We reset right to 0 because they have collided and will become stationary cars.
                collisions += 1 + right
                right = 0
                has_stationary = True
            elif direction == 'S':
			    # Resolve any right-moving cars and reset right to 0 because they are now stationary.
                collisions += right
                right = 0
                has_stationary = True
        return collisions