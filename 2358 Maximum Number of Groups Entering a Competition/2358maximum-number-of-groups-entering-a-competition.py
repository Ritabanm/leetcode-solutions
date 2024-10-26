class Solution:
    def maximumGroups(self, grades: list[int]) -> int:
        grades.sort()
        groups, prev, curr, cnt = 0, 0, 0, 0
        for grade in grades:
            curr += grade
            cnt += 1
            if cnt > groups and curr > prev:
                groups += 1
                prev = curr
                curr = 0
                cnt = 0
        return groups