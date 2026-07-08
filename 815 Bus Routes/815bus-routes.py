from collections import deque, defaultdict

class Solution:
    def numBusesToDestination(self, routes, source: int, target: int) -> int:
        if source == target:
            return 0  # No need to take any bus
        
        # Step 1: Build stop-to-bus map
        stop_to_buses = defaultdict(set)
        for i, route in enumerate(routes):
            for stop in route:
                stop_to_buses[stop].add(i)  # Stop is connected to bus i

        # Step 2: BFS Setup
        queue = deque([(source, 0)])  # (current stop, buses taken so far)
        visited_stops = set([source])  # Prevent revisiting stops
        visited_buses = set()  # Prevent revisiting buses

        # Step 3: BFS Traversal
        while queue:
            stop, buses_taken = queue.popleft()

            # Check all buses that pass through this stop
            for bus in stop_to_buses[stop]:
                if bus in visited_buses:
                    continue  # Skip buses we already used
                
                visited_buses.add(bus)  # Mark bus as used

                # Explore all stops this bus goes to
                for next_stop in routes[bus]:
                    if next_stop == target:
                        return buses_taken + 1  # Found the shortest path!
                    if next_stop not in visited_stops:
                        visited_stops.add(next_stop)
                        queue.append((next_stop, buses_taken + 1))  # Take another bus
        
        return -1  # If target is not reachable
