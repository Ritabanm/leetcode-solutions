# Write your MySQL query statement below
select gender, day, SUM(score_points) over(partition by gender order by gender, day) as total from Scores