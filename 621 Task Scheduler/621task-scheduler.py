from collections import Counter
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Step 1: Count the frequency of each task
        task_counts = Counter(tasks)
        max_freq = max(task_counts.values())
        
        # Step 2: Find how many tasks have the max frequency
        max_count = sum(1 for count in task_counts.values() if count == max_freq)
        
        # Step 3: Calculate the minimum intervals needed
        # (max_freq - 1) is the number of partitions between the most frequent tasks
        # (n + 1) is the size of each partition (including the task itself + idle times)
        # We add `max_count` to account for the most frequent tasks themselves in the last row.
        part_count = max_freq - 1
        part_length = n + 1
        empty_slots = part_count * part_length + max_count
        
        # Step 4: The result is the maximum of the number of tasks and the calculated time
        return max(len(tasks), empty_slots)
