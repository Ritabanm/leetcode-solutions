import heapq

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # Sort meetings by start time
        meetings.sort()
        
        # Min-heap to track (end_time, room_number)
        occupied_rooms = []
        
        # Min-heap for available rooms sorted by room number
        available_rooms = list(range(n))
        heapq.heapify(available_rooms)
        
        # Track meetings held in each room
        meeting_count = [0] * n 
        
        for start, end in meetings:
            duration = end - start
            
            # Free up rooms that have finished their meetings
            while occupied_rooms and occupied_rooms[0][0] <= start:
                _, room = heapq.heappop(occupied_rooms)
                heapq.heappush(available_rooms, room)
            
            # Assign the lowest-numbered available room
            if available_rooms:
                room = heapq.heappop(available_rooms)
                heapq.heappush(occupied_rooms, (end, room))
            else:
                # Delay the meeting until a room is free
                end_time, room = heapq.heappop(occupied_rooms)
                heapq.heappush(occupied_rooms, (end_time + duration, room))
            
            meeting_count[room] += 1
        
        # Find the room with the most meetings
        max_meetings = max(meeting_count)
        return meeting_count.index(max_meetings)  # Return lowest index in case of tie
