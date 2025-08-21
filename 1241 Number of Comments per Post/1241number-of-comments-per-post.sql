
with posts as (
    select
        distinct sub_id  
    from Submissions 
    where parent_id is null
)

select 
    p.sub_id as post_id, 
    ifnull(count(distinct s.sub_id), 0) as number_of_comments 
from posts as p 
left join Submissions as s 
on p.sub_id = s.parent_id  
group by p.sub_id
order by post_id 

