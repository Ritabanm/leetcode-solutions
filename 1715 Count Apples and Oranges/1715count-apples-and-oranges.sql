# Write your MySQL query statement below
WITH CTE AS
(
SELECT
    SUM(Boxes.apple_count) AS box_apple_cnt,
    SUM(Chests.apple_count) AS chest_apple_cnt,
    SUM(Boxes.orange_count) AS box_orange_cnt, 
    SUM(Chests.orange_count) AS chest_orange_cnt
FROM
Boxes LEFT JOIN Chests
ON Chests.chest_id = Boxes.chest_id
)
SELECT 
    IFNULL(box_apple_cnt,0) + IFNULL(chest_apple_cnt,0) AS apple_count,
    IFNULL(box_orange_cnt,0) + IFNULL(chest_orange_cnt,0) AS orange_count
FROM cte