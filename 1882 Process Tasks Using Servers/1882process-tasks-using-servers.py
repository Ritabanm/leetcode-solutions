class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        res = []
        up = [(w, id) for id, w in enumerate(servers)]
        heapify(up)
        pre = []

        for time, task in enumerate(tasks):
            while pre and pre[0][0] == time:
                _, w, id = heappop(pre)
                heappush(up, (w, id))

            if len(up) > 0:
                w, id = heappop(up)
                heappush(pre, (time + task, w, id))
                res.append(id)
            else:
                finishTime, w, id = heappop(pre)
                heappush(pre, (finishTime + task, w, id))
                res.append(id)

        return res