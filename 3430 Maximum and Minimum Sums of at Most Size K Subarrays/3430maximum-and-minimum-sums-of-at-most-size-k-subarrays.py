class Solution:
    @staticmethod
    def get_min_sum(nums, k):
        min_sum = curr_sum = 0
        queue = deque()
        for i, num in enumerate(nums):
            if i >= k:
                queue[0][1] -= 1
                curr_sum -= queue[0][0]
                if queue[0][1] == 0:
                    queue.popleft()
            curr_len = 1
            curr_sum += num
            while queue and queue[-1][0] > num:
                prev_num, prev_len = queue.pop()
                curr_sum += num * prev_len - prev_num * prev_len
                curr_len += prev_len
            queue.append([num, curr_len])
            min_sum += curr_sum            
        return min_sum

    def minMaxSubarraySum(self, nums: List[int], k: int) -> int:
        min_sum = self.get_min_sum(nums, k)
        max_sum = -self.get_min_sum([-x for x in nums], k)
        return min_sum + max_sum