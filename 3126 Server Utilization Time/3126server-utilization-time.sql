-- Write your PostgreSQL query statement below
-- formatted for ease in reading

select
  floor(
    (
      sum(
        EXTRACT(
          EPOCH
          FROM
            status_time
        )
      ) filter (
        where
          session_status = 'stop'
      ) - sum(
        EXTRACT(
          EPOCH
          FROM
            status_time
        )
      ) filter (
        where
          session_status = 'start'
      )
    ) / 3600 / 24
  ) as total_uptime_days
from
  servers;