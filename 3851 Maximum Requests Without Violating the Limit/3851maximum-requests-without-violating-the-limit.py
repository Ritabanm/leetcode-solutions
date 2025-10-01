class Solution:
    def maxRequests(self, requests: list[list[int]], k: int, window: int) -> int:
        removed, d = 0, defaultdict(list)
        for user, time in requests:
            d[user].append(time)
        
        for times in d.values():
            times.sort()
            queue = deque()

            for time in times:
                queue.append(time)
                if len(queue)<=k:
                    continue
                
                elif queue[~0]>queue[0]+window:
                    queue.popleft()
                else:
                    queue.pop()
                    removed+=1
        return len(requests)-removed