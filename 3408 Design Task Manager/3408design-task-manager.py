class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.global_tasks = {}
        self.max_heap = []

        for userId, taskId, priority in tasks:
            self.add(userId, taskId, priority)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.global_tasks[taskId] = (priority, userId)
        heappush(self.max_heap, (-priority, -taskId, userId))

    def edit(self, taskId: int, newPriority: int) -> None:
        priority, userId = self.global_tasks[taskId]
        self.global_tasks[taskId] = (newPriority, userId)
        heappush(self.max_heap, (-newPriority, -taskId, userId))
        
    def rmv(self, taskId: int) -> None:
        priority, userId = self.global_tasks.pop(taskId)

    def execTop(self) -> int:
        while self.max_heap:
            neg_priority, neg_taskId, userId = heappop(self.max_heap)
            priority, taskId = -neg_priority, -neg_taskId

            if taskId in self.global_tasks and self.global_tasks[taskId] == (priority, userId):
                del self.global_tasks[taskId]

                return userId
        return -1


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()