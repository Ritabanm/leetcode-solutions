class Solution:
    def buttonWithLongestTime(self, events):
        len_events = len(events)
        
        max_time_taken_to_push = None
        button_with_max_time_taken_to_push = None

        i = 0
        while (i < len_events):
            if (i > 0):
                time_taken_to_push = events[i][1] - events[i-1][1]
            else:
                time_taken_to_push = events[i][1]
            
            if (max_time_taken_to_push is None or time_taken_to_push >= max_time_taken_to_push):
                button_with_max_time_taken_to_push = min(button_with_max_time_taken_to_push, events[i][0]) if time_taken_to_push == max_time_taken_to_push and button_with_max_time_taken_to_push is not None else events[i][0]
                max_time_taken_to_push = time_taken_to_push
            i += 1
        
        return button_with_max_time_taken_to_push