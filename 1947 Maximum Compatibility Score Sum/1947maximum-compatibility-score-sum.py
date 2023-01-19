class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        max_score = float('-inf')
        number_of_students = len(students)
        mentor_taken = [0]*len(mentors)
        cached_scores = {}
        def score(mentor_no, student_no):
            key = str(student_no) + str(mentor_no)
            if key in cached_scores:
                return cached_scores[key]
            total = 0
            for i in range(len(students[0])):
                if students[student_no][i] == mentors[mentor_no][i]:
                    total += 1
            cached_scores[key] = total
            return total

        def dfs(mentor_no, paired_students, student_mentor_pairings_score):
            nonlocal max_score
            if len(paired_students) == number_of_students:
                max_score = max(max_score, student_mentor_pairings_score)
                return
            for student_no in range(number_of_students):
                if not mentor_taken[mentor_no] and student_no not in paired_students:
                    mentor_taken[mentor_no] = 1
                    paired_students.append(student_no)
                    tmp = score(mentor_no,student_no)
                    student_mentor_pairings_score += tmp
                    dfs(mentor_no + 1, paired_students,student_mentor_pairings_score)
                    mentor_taken[mentor_no] = 0
                    paired_students.pop()
                    student_mentor_pairings_score -= tmp

        dfs(0,[],0)
        return max_score
        