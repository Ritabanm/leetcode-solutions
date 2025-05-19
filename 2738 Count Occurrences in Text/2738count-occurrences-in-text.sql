# Write your MySQL query statement below
select 'bull' as word, 
sum(content Like '% bull %') as count
from files union all
select 'bear' as word, sum(content like '% bear %') as count
from files
