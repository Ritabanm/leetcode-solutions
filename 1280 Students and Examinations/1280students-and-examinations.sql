select s.student_id, s.student_name, sub.subject_name, count(E.subject_name) as attended_exams
from students s
cross join subjects sub
left join examinations e on s.student_id = E.student_id and sub.subject_name = e.subject_name
group by S.student_id, S.student_name, Sub.subject_name
order by S.student_id, Sub.subject_name




