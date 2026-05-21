# Write your MySQL query statement below
select c.candidate_id
from candidates as c
inner join rounds as r
on c.interview_id = r.interview_id
where c.years_of_exp>=2
group by c.candidate_id
having sum(r.score)>15;
