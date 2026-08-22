# Write your MySQL query statement below
with cte as (select team_name, (wins * 3 + draws) points, rank() over(order by (wins * 3 + draws) desc) position from TeamStats)

select *,case when position<=ceil((count(*) over()/3)) then 'Tier 1' 
when position<=ceil((2 * count(*) over()/3)) then 'Tier 2'
else 'Tier 3' end tier from cte
 order by 2 desc, 1