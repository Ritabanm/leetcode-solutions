WITH withRanking AS (
    SELECT
        *,
        RANK() OVER (
            PARTITION BY state
            ORDER BY fraud_score DESC
        ) AS fraud_row
    FROM Fraud
),
total AS (
    SELECT
        state,
        COUNT(*) AS total
    FROM Fraud
    GROUP BY 1
),
cutOff AS (
    SELECT
        state,
        total,
        1  AS cut_off
    FROM total
),
rankingAndCutOff AS (
    SELECT
        W.*,
        C.cut_off
    FROM withRanking AS W
    LEFT OUTER JOIN cutoff AS C
        ON W.state = C.state
),
final AS (
    SELECT 
        policy_id,
        state,
        fraud_score 
    FROM rankingAndCutOff
    WHERE fraud_row <= cut_off
)
-- SELECT * FROM withRanking ORDER BY fraud_row
-- SELECT * FROM cutOff
-- SELECT * FROM rankingAndCutOff
SELECT * FROM final ORDER BY state ASC, fraud_score DESC, policy_id ASC