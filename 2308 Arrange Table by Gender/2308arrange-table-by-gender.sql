Select user_id, gender 
From (Select user_id, gender, rank() over(partition by gender order by user_id asc) rk1, 
      Case When gender='female' then 1                                                                                      
	       When gender = 'other' then 2                                
           Else 3 End rk2
      from Genders) sub
order by rk1, rk2 