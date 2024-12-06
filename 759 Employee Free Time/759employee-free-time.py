class Solution(object):
    def employeeFreeTime(self, avails):
        ans = []
        pq = [(emp[0].start, ei, 0) for ei, emp in enumerate(avails)]
        heapq.heapify(pq)
        anchor = min(iv.start for emp in avails for iv in emp)
        while pq:
            t, e_id, e_jx = heapq.heappop(pq)
            if anchor < t:
                ans.append(Interval(anchor, t))
            anchor = max(anchor, avails[e_id][e_jx].end)
            if e_jx + 1 < len(avails[e_id]):
                heapq.heappush(pq, (avails[e_id][e_jx+1].start, e_id, e_jx+1))

        return ans