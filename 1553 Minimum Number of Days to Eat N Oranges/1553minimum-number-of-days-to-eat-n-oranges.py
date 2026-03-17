class Solution:
    def minDays(self, n: int) -> int:
	    # Use a queue for our BFS.
        q = collections.deque([])
		# Append the initial number of oranges starting at 0 days.
        q.append((n, 0))
        seen = set()
        while q:
            oranges, days = q.popleft()
			# First to hit 0 will be our shortest path, return the days it took.
            if oranges <= 3:
			    # We know the min from 3 is either 2 or 1.
                return days + min(2, oranges)
			# If true and not used add to the q.
            if oranges % 2 == 0:
                if oranges/2 not in seen:
                    q.append((oranges/2, days+1))
                    seen.add(oranges/2)
			# If true and not used add to the q.
            if oranges % 3 == 0:
                if oranges-(2*(oranges/3)) not in seen:
                    q.append((oranges-(2*(oranges/3)), days+1))
                    seen.add(oranges-(2*(oranges/3)))
            # If not used add to the q.
            if oranges-1 not in seen:
                q.append((oranges-1, days+1))
                seen.add(oranges-1)