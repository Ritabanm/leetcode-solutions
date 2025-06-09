class LogSystem:
    def __init__(self):
        self._data = SortedList()
        self._granularity = {
            "Year": 1, "Month": 2,
            "Day": 3, "Hour": 4,
            "Minute": 5, "Second": 6,
        }
    
    def _split_timestamp(self, timestamp):
        return [int(elem) for elem in timestamp.split(':')]
    
    def _trunc(self, timestamp, granularity):
        t = self._split_timestamp(timestamp)
        index = self._granularity[granularity]
        return t[:index]

    def put(self, id: int, timestamp: str) -> None:
        t = self._split_timestamp(timestamp)
        self._data.add((t, id))

    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        a = self._trunc(start, granularity)
        b = self._trunc(end, granularity)
        b[-1] += 1
        return [
            id
            for _, id in self._data.irange(
                (a, 0), (b, 0),
                inclusive=(True, False),
            )
        ]