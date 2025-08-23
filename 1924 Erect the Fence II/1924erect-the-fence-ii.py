class Solution:
    def outerTrees(self, trees):
        # Helper function to calculate the distance between two points
        def distance(p1, p2):
            return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

        # Helper function to find the circle that passes through three points
        def circle_from_three(p1, p2, p3):
            ax, ay = p1
            bx, by = p2
            cx, cy = p3

            # Calculate the determinant (d) used to find the center of the circle
            d = 2 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by))
            if d == 0:
                return (0, 0, float('inf'))  # Points are collinear

            # Calculate the center (ux, uy) of the circle using the circumcircle formula
            ux = ((ax**2 + ay**2) * (by - cy) + (bx**2 + by**2) * (cy - ay) + (cx**2 + cy**2) * (ay - by)) / d
            uy = ((ax**2 + ay**2) * (cx - bx) + (bx**2 + by**2) * (ax - cx) + (cx**2 + cy**2) * (bx - ax)) / d
            # The radius is the distance from the center to one of the points
            radius = distance((ux, uy), p1)  

            return (ux, uy, radius)

        # Helper function to find the circle from two points
        def circle_from_two(p1, p2):
            # Midpoint between the two points
            mx, my = (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2
            # Radius is half the distance between the two points
            radius = distance(p1, p2) / 2
            return (mx, my, radius)

        # Check if a point is inside the circle
        def is_inside(circle, point):
            cx, cy, r = circle
            # Check if the point is within the radius of the circle
            return distance((cx, cy), point) <= r + 1e-5

        # Welzl's algorithm to find the minimum enclosing circle
        def welzl(points, boundary_points=[]):
            # Base cases for the recursion
            if not points or len(boundary_points) == 3:
                # If no points left or 3 boundary points are used, calculate circle
                if len(boundary_points) == 0:
                    return (0, 0, 0)  # No points to enclose
                elif len(boundary_points) == 1:
                    return (boundary_points[0][0], boundary_points[0][1], 0)  # Single point
                elif len(boundary_points) == 2:
                    return circle_from_two(boundary_points[0], boundary_points[1])  # Two points
                elif len(boundary_points) == 3:
                    return circle_from_three(boundary_points[0], boundary_points[1], boundary_points[2])  # Three points

            # Randomly select a point from the remaining points
            index = random.randrange(len(points))
            p = points[index]
            points.remove(p)  # Remove the point to find the circle without it

            # Get the minimum enclosing circle for the remaining points
            circle = welzl(points, boundary_points)

            # If the selected point is inside the circle, return the current circle
            if is_inside(circle, p):
                points.append(p)  # Re-add the point back to the list
                return circle

            # Otherwise, the selected point must be on the boundary of the new circle
            boundary_points.append(p)
            circle = welzl(points, boundary_points)  # Recur with the new boundary point
            boundary_points.pop()  # Remove the point from boundary after recursion
            points.append(p)  # Re-add the point back to the list
            return circle

        # Shuffle the input points to ensure randomness in the algorithm
        random.shuffle(trees)
        # Get the center and radius of the minimum enclosing circle
        center_x, center_y, radius = welzl(trees)

        # Return the result as a list of [x, y, r]
        return [center_x, center_y, radius]
