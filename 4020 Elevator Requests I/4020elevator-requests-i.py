class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        totalTime = 0
        curr=0
        for req in requests:
            if curr == req:
                continue
            else:
                totalTime+=abs(curr-req)
                curr=req
        return totalTime