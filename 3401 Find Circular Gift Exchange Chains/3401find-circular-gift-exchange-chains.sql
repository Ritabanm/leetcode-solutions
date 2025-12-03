WITH RECURSIVE I as (
    SELECT * FROM SecretSanta WHERE receiver_id NOT IN 
    (SELECT receiver_id FROM SecretSanta GROUP BY 1 HAVING COUNT(*) > 1)
), CTE as (
    SELECT giver_id, receiver_id, gift_value, 1 as n, giver_id as s FROM I
    UNION ALL
    SELECT s.giver_id, s.receiver_id, c.gift_value + s.gift_value, n + 1, s FROM CTE c
    JOIN I s ON(s.giver_id = c.receiver_id AND s != c.receiver_id)
)

SELECT ROW_NUMBER() OVER() as chain_id, * FROM (
    SELECT DISTINCT MAX(n) as chain_length, MAX(gift_value) as total_gift_value FROM CTE
    GROUP BY s
    ORDER BY chain_length DESC, total_gift_value DESC
) r
