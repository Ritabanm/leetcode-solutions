class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        day = 1
        task_map = {}

        for task in tasks:
            if task in task_map:
                last_performed_day = task_map[task]
                if day - last_performed_day <= space:
                    day = last_performed_day + space + 1
            
            task_map[task] = day
            # print(day, task, task_map)
            day += 1
            

        return day -1 # since day starts at one