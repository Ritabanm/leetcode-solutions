-- Write your PostgreSQL query statement below
WITH left_max AS (
  SELECT id, height,
         MAX(height) OVER (ORDER BY id ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS max_left
  FROM Heights
),
right_max AS (
  SELECT id,
         MAX(height) OVER (ORDER BY id DESC ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS max_right
  FROM Heights
),
combined AS (
  SELECT l.id,
         l.height,
         l.max_left,
         r.max_right,
         GREATEST(LEAST(l.max_left, r.max_right) - l.height, 0) AS water
  FROM left_max l
  JOIN right_max r ON l.id = r.id
)
SELECT SUM(water) AS total_trapped_water
FROM combined;