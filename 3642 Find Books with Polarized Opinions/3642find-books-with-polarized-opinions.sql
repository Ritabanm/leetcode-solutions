# Write your MySQL query statement below
select b.book_id, title, author, genre, pages,
max(session_rating) - min(session_rating) as rating_spread, 
round((count(case when session_rating <= 2 then 1 end) + 
count(case when session_rating >= 4 then 1 end)) / count(session_id), 2) as polarization_score
from books b
inner join reading_sessions r
on b.book_id = r.book_id
group by r.book_id
having count(session_id) >= 5
and max(session_rating) >= 4
and min(session_rating) <= 2
and polarization_score >= 0.60
order by polarization_score desc, title desc;