class TodoList:
    def __init__(self):
      self.dict1 = defaultdict(set)
      self.dict2 = defaultdict(set)
      self.completed = defaultdict(set)
      self.idx = 0

    def addTask(self, userId, taskDescription, dueDate, tags):
        self.idx += 1

        self.dict1[userId].add((dueDate,taskDescription,self.idx))

        for tag in tags:
            self.dict2[(userId,tag)].add((dueDate,taskDescription,self.idx))

        return self.idx

    def getAllTasks(self, userId):
        ans = sorted([(d,t) for d,t,idx in self.dict1[userId] if idx not in self.completed[userId]])
        return [i[1] for i in ans]

    def getTasksForTag(self, userId, tag):
        result = sorted([(d,t) for d,t,idx in self.dict2[(userId,tag)] if idx not in self.completed[userId]])
        return [i[1] for i in result]

    def completeTask(self, userId, taskId):
        self.completed[userId].add(taskId)
        
        