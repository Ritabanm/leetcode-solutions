class Solution:
    def maxProfit(self, workers: List[int], tasks: List[List[int]]) -> int:
      workers_tasks = defaultdict(list)
      tasks_cnt = Counter()

      total_profit = 0

      for skill, profit in tasks:
        # Store profits in max_heap for a particular worker/skill
        heapq.heappush(workers_tasks[skill], -profit)
        # Keep track of tasks/profits available
        tasks_cnt[profit] += 1

      for worker in workers:
        if worker in workers_tasks and len(workers_tasks[worker]) > 0:
          popped_profit = heapq.heappop(workers_tasks[worker])
          popped_profit = -popped_profit
          total_profit += popped_profit
          
          tasks_cnt[popped_profit] -= 1

          if tasks_cnt[popped_profit] == 0:
            del tasks_cnt[popped_profit]

      # Additional worker
      if tasks_cnt:
        total_profit += max(tasks_cnt.keys())

      return total_profit