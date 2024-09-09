class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        changes_points = defaultdict(int)
        ret = []
        for s in segments:
            changes_points[s[0]] += s[2]
            changes_points[s[1]] -= s[2]
        color = 0
        for cr_pos in sorted(changes_points):
            if color != 0:
                ret.append([prev_pos, cr_pos, color])
            prev_pos = cr_pos
            color += changes_points[cr_pos]
        return ret