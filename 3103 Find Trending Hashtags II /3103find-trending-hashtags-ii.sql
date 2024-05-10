-- Write your PostgreSQL query statement below
with cte as (select user_id, tweet_id,unnest(string_to_array(tweet,' ')) as tweet
from tweets
where date_trunc('month', tweet_date)='2024-02-01'
),
cte1 as (select user_id, tweet_id, tweet
from cte
where tweet like '#%'
),
cte2 as (
    select  tweet as hashtag,count(*) as total_count, 
     row_number() over (order by count(*) desc, tweet desc ) as rank
    from cte1
    group by  hashtag
)
    select hashtag, total_Count as count
    from cte2
    where rank<=3
    order by total_count desc, hashtag desc
 
; 