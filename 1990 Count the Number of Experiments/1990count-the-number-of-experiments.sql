
with platforms as (
    select 'IOS' as platform 
    union 
    select 'Android'
    union 
    select 'Web'
), 

experiment_names as (
    select 'Reading' as experiment_name
    union 
    select 'Sports'
    union 
    select 'Programming'
), 

combinations as (
    select
        platform, 
        experiment_name
    from platforms 
    join experiment_names 
), 

counts as (
    select 
        platform, 
        experiment_name, 
        count(*) as n
    from experiments
    group by platform, experiment_name 
)

select 
    c.platform, 
    c.experiment_name, 
    ifnull(n, 0) as num_experiments
from combinations as c
left join counts as c1
on c.platform = c1.platform
and c.experiment_name = c1.experiment_name 
group by c.platform, c.experiment_name
