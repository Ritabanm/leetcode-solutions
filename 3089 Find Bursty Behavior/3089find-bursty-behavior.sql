# Write your MySQL query statement below
with t1 as (
    select user_id, 
        count(*)over(partition by user_id order by post_date range between interval 6 day preceding and current row) as max_7day_posts, 
        count(*)over(partition by user_id)/4 as avg_weekly_posts
    from posts
    where post_date between '2024-02-01' and '2024-02-28')

select distinct *
from t1
where max_7day_posts >= 2*avg_weekly_posts 
and (user_id, max_7day_posts) in (select user_id, max(max_7day_posts) from t1 group by 1)
order by user_id