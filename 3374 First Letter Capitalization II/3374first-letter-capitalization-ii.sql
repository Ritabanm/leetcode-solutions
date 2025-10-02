-- Write your PostgreSQL query statement below
WITH CTE1 AS(
	SELECT content_id, content_text,  replace(content_text,'-','  ') AS new_text
	FROM user_content 
),
cte2 as(
    select content_id, content_text, string_to_array( new_text , ' ' ) as new_text
    from cte1
),
cte3 as(
    select content_id, content_text, unnest( new_text ) as new_text
    from cte2
),
cte4 as (
    select content_id, content_text, 
    
    case when
    
    new_text = '' then '-'
    else new_text
    
    end as new_text

    from cte3
),
cte5 as (
    select content_id, content_text, upper(substr(new_text,1,1)) || lower(substr(new_text,2,length(new_text)-1)) as new_text
    from cte4
),
cte6 as(
    select content_id, content_text, string_agg(new_text,' ') as new_text
    from cte5
    group by content_id, content_text
    order by content_id
),
cte7 as(
    select content_id, content_text as original_text, replace(new_text, ' - ','-') as converted_text
    from cte6
)

select * from cte7
