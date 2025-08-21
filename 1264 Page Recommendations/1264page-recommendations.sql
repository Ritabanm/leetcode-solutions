with cte as(select user1_id as user_id from Friendship where user2_id=1
union all
select user2_id from Friendship where user1_id=1)
select distinct page_id as recommended_page from likes 
where user_id in (select * from cte) and page_id not in (select page_id from likes where user_id=1);




