with cta as(
    select country,winery,sum(points)pts
    from Wineries 
    group by 1,2
),
cte as(
    select country,
    concat(winery,' (',pts,')'  )winery      ,    
     rank() over(partition by country order by pts desc,winery  )rnk
     from cta
)
select country,
max(case when rnk=1 then winery end )top_winery ,
ifnull( max(case when rnk=2 then winery end )  ,'No second winery')second_winery,
   ifnull( max(case when rnk=3 then winery end )  ,'No third winery')third_winery
       from cte
       group by 1
       order by 1