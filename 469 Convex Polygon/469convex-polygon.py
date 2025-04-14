class Solution:

	def _get_pos(self, p1x: int, p1y: int, p2x: int, p2y: int, p3x: int, p3y: int) -> int:
		return (p2x - p1x)*(p3y - p1y) - (p3x - p1x)*(p2y - p1y)

	def isConvex(self, points: list[list[int]]) -> bool:
		points += points[:2]

		a, b, c = points[:3]
		prev_pos = self._get_pos(*a, *b, *c)
		for x in points[3:]:
			point_pos = self._get_pos(*b, *c, *x)
			if point_pos != 0: # three points not on line
				if point_pos*prev_pos < 0:
					return False
				prev_pos = point_pos
			a, b, c = b, c, x
		return True