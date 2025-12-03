# Write your MySQL query statement below
WITH
    userCateogries AS(
        SELECT user_id, 
               category
        FROM ProductPurchases
        JOIN ProductInfo
        on ProductPurchases.product_id = ProductInfo.product_id
    ),
    sameUserWithTwoDiffCat AS(
        SELECT distinct(u1.user_id),
               u1.category as cat1,
               u2.category as cat2
        FROM userCateogries as u1, userCateogries as u2
        where u1.user_id = u2.user_id and u1.category < u2.category
    )

select cat1 as category1, cat2 as category2, count(*) as customer_count
from sameUserWithTwoDiffCat 
group by cat1, cat2
having customer_count > 2
order by customer_count desc, category1, category2;