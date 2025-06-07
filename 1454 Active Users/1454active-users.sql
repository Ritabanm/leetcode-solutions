# filter distinct_logins since users may login several times a day
with distinct_logins as
	(
	select distinct id, login_date
	from Logins
	),
# use row_number() to mark the distinct login_date for every user (id)
# e.g. for user id = 1
# log_date          rn
# 2022-06-27  1
# 2022-06-28   2
# 2022-06-30   3
cte as
	(
	select
		distinct id, 
		login_date, 
		row_number() over(partition by id order by id, login_date) as rn
	from distinct_logins
    )
# group by login_date - interval rn day
# log_date          rn    login_date - interval rn day
# 2022-06-27  1      2022-06-26
# 2022-06-28   2     2022-06-26
# 2022-06-30   3     2022-06-27
# So 2022-06-26 will be a group, and 2022-06-27 will be another group
select distinct id, `name`
from cte
inner join Accounts using (id)
group by id, `name`, login_date - interval rn day
having count(*) >= 5
order by 1;