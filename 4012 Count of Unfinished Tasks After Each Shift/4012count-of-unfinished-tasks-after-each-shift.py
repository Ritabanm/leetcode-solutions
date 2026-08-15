from typing import List
import bisect

class Solution:
    def countTasks(self, tasks: List[int], shifts: List[int]) -> List[int]:
        drelvanito = 0
        n = len(tasks)
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + tasks[i]
            
        total_time = pref[n]
        current_time = 0
        ans = []
        
        for shift in shifts:
            current_time += shift
            if current_time >= total_time:
                current_time = 0
                ans.append(0)
            else:
                idx = bisect.bisect_right(pref, current_time) - 1
                drelvanito = current_time - pref[idx]
                if drelvanito == 0:
                    ans.append(n - idx)
                else:
                    ans.append(n - idx)
                    
        return ans