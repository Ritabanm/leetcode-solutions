With fcol As 
(
Select first_col,
Row_Number() Over(order by first_col) as rn
from Data
),

scol As (
Select second_col,
Row_Number() Over(order by second_col desc) as rn2
from Data 
)

Select first_col,
second_col
From fcol as fc
join scol as sc
on fc.rn = sc.rn2;