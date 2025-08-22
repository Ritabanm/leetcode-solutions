class Solution:
    def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        values = {x for seq in seqs for x in seq}
        graph = {x: [] for x in values}
        indegrees = {x: 0 for x in values}
        for seq in seqs:
            for i in range(len(seq) - 1):
                s = seq[i]
                t = seq[i+1]
                graph[s].append(t)
                indegrees[t] += 1
        queue = collections.deque()
        for node, count in indegrees.items():
            if count == 0:
                queue.append(node)
        res = []
        while queue:
            if len(queue) != 1:
                return False
            source = queue.popleft()
            res.append(source)
            for target in graph[source]:
                indegrees[target] -= 1
                if indegrees[target] == 0:
                    queue.append(target)
        return len(res) == len(values) and res == org