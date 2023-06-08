class SnapshotArray:
    # O(length)/O(length)
    def __init__(self, length: int):
        self.snap_id = 0
        self.history = [[(self.snap_id, 0)] for _ in range(length)]

    # O(1)/O(1)
    def set(self, index: int, val: int) -> None:
        self.history[index].append((self.snap_id, val))

    # O(1)/O(1)
    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1
        
    # Solvetime: O(n)/O(1)
    def get(self, index: int, snap_id: int) -> int:
        for id, val in reversed(self.history[index]):
            if id <= snap_id:
                return val        
