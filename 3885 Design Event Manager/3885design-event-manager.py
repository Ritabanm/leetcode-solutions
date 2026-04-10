class EventManager:

    def __init__(self, events: list[list[int]]):

        self.priorities = defaultdict(lambda:0, events)

        self.heap = [(-priority, indx) for indx, priority in events]
        heapify(self.heap)

        return


    def updatePriority(self, eventId: int, newPriority: int) -> None:

        self.priorities[eventId] = newPriority
        heappush(self.heap, (-newPriority, eventId))

        return


    def pollHighest(self) -> int:

        while self.heap:
            priority,indx = heappop(self.heap)

            if self.priorities[indx] == -priority:
                del self.priorities[indx]
                return indx

        return -1