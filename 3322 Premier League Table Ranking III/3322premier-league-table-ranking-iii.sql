WITH withCalculations AS (
    SELECT
        season_id,
        team_id,
        team_name,
        wins * 3 + draws AS points,
        goals_for - goals_against AS goal_difference
    FROM SeasonStats
),
withRanking AS (
    SELECT
        *,
        ROW_NUMBER() OVER (
            PARTITION BY season_id
            ORDER BY points DESC, goal_difference DESC, team_name ASC
        ) AS "position"
    FROM withCalculations
)
-- SELECT * FROM withCalculations
SELECT * FROM withRanking