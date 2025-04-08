import threading

class BoundedBlockingQueue(object):

    def __init__(self, capacity: int):
        self.dq = deque()
        self.capacity = capacity
        self.cond = threading.Condition()

    def enqueue(self, element: int) -> None:
        with self.cond:
            self.cond.wait_for(lambda: len(self.dq) < self.capacity)
            self.dq.appendleft(element)
            self.cond.notify_all()
        

    def dequeue(self) -> int:
        with self.cond:
            self.cond.wait_for(lambda: len(self.dq) > 0)
            v = self.dq.pop()
            self.cond.notify_all()
            return v

    def size(self) -> int:
        return len(self.dq)