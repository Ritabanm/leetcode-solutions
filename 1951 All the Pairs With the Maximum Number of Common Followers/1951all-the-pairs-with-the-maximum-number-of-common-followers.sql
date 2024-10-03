
with t as (
    select 
        count(*) as c, 
        r1.user_id as user1_id, 
        r2.user_id as user2_id
    from relations as r1 
    join relations as r2
    on r1.follower_id = r2.follower_id 
    and r1.user_id < r2.user_id
    group by r1.user_id, r2.user_id
), 

t1 as (
    select 
        max(c) as mx 
    from t
)

select 
    user1_id, 
    user2_id
from t  
where c = (select mx from t1)


