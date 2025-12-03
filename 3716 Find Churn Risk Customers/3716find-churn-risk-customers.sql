-- Write your PostgreSQL query statement below
with users_info as (
    select user_id,
           last_value(plan_name) over (partition by user_id order by event_date) as current_plan,
           last_value(monthly_amount) over (partition by user_id order by event_date) as current_monthly_amount,
           last_value(monthly_amount) over (partition by user_id order by event_date) / max(monthly_amount) over (partition by user_id)::numeric as current_plan_share,
           max(event_date) over (partition by user_id) - min(event_date) over(partition by user_id) as days_as_subscriber,
           last_value(event_type) over (partition by user_id) as last_action,
           max(monthly_amount) over (partition by user_id) as max_historical_amount      
    from subscription_events
),
downgrades as (
    select user_id
    from subscription_events
    where event_type = 'downgrade'
)
select user_id, 
       current_plan,
       current_monthly_amount,
       max_historical_amount,
       days_as_subscriber
from users_info
where current_plan_share < 0.5
      and last_action <> 'cancel'
      and days_as_subscriber >= 60
      and user_id in (select user_id from downgrades)
order by days_as_subscriber desc, user_id asc
