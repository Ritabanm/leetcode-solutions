class Solution:

  def numberOfNodes(self, n: int, queries: List[int]) -> int:
    is_changed = [False] * (n + 1)
    for q in queries:
      is_changed[q] = not is_changed[q]

    frontier, res = [(1, is_changed[1])], 0

    while frontier:
      new_frontier = []
      for node, is_selected in frontier:
        if is_selected:
          res += 1
        
        for next_node in [2 * node, 2 * node + 1]:
          if next_node <= n:
            new_frontier.append((next_node, is_selected ^ is_changed[next_node]))
      
      frontier = new_frontier

    return res