from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        result = []
        q = deque()  # will store indices

        for i in range(len(nums)):
            # Remove indices outside the current window
            while q and q[0] < i - k + 1:
                q.popleft()

            # Remove elements smaller than the current one from the back
            while q and nums[q[-1]] < nums[i]:
                q.pop()

            q.append(i)

            # Append the max value to result (front of deque) once window is fully formed
            if i >= k - 1:
                result.append(nums[q[0]])

        return result
