# Write your MySQL query statement below
With t1 as (Select account_id, sum(amount) income, date_format(day, '%Y%m') month_of,A.max_income max_income
from transactions
join accounts a
using(account_id)
where type='Creditor'
group by account_id,date_format(day, '%Y-%m'))

Select distinct account_id from (Select t1.*, coalesce(lead(income) over(partition by t1.account_id order by month_of asc ),0) as next_income, lead(month_of) over(partition by t1.account_id order by month_of asc) next_month
from t1) a
where income>max_income and next_income>max_income
and PERIOD_DIFF(next_month, month_of)=1