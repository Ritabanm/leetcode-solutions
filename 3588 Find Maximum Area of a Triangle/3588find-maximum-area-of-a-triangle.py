class Solution:
  def maxArea(self, coords: List[List[int]]) -> int:
    x_data, y_data = defaultdict(list), defaultdict(list)
    x_max, y_max, x_min, y_min = 0, 0, float('inf'), float('inf')
    for x, y in coords:
      x_max, y_max = max(x, x_max), max(y, y_max)
      x_min, y_min = min(x, x_min), min(y, y_min)
      x_data[x].append(y)
      y_data[y].append(x)

    res = 0
    for x, ys in x_data.items():
      if len(ys) > 1:
        t = (max(ys) - min(ys)) * max(x_max - x, x - x_min)
        res = max(t, res)

    for y, xs in y_data.items():
      if len(xs) > 1:
        t = (max(xs) - min(xs)) * max(y_max - y, y - y_min)
        res = max(t, res)

    return res if res != 0 else -1