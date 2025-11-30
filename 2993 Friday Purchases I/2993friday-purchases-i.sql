# Write your MySQL query statement below
select WEEK(purchase_date) - 43 as week_of_month, purchase_date, sum(amount_spend) as total_amount
from purchases
where purchase_date>='2023-11-01' and purchase_date<'2023-12-01' and DAYOFWEEK(purchase_date)=6
group by 1
order by 1 ASC