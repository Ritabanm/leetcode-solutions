with cte as (
    select *, count(*) as cnt_reactions
    from reactions
    group by user_id
)
select r.user_id, r.reaction as dominant_reaction,
round(count(*) / cnt_reactions, 2) as reaction_ratio
from reactions r
join cte c
on r.user_id = c.user_id
where cnt_reactions >= 5
group by r.user_id, r.reaction
having reaction_ratio >= 0.60
order by reaction_ratio desc, user_id;