with temp
as
(select gold_medal as user_id,contest_id,'gold' as medal
from Contests
union all
select silver_medal as user_id,contest_id,'silver' as medal
from Contests
union all
select bronze_medal as user_id,contest_id,'bronze' as medal
from Contests),

#user won any medal in three or more consecutive contests
cond1 as
(select distinct user_id
from temp
where (user_id,contest_id+1) in (select user_id,contest_id from temp)
and (user_id,contest_id+2) in (select user_id,contest_id from temp)),

#user won the gold medal in three or more different contests (not necessarily #consecutive)
cond2 as
(select user_id,medal
from temp
where medal = 'gold'
group by 1,2
having count(contest_id) >= 3)

select name,mail
from Users
where user_id in (select user_id from cond1
                  union
                  select user_id from cond2)