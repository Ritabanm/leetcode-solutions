# Write your MySQL query statement below
# Write your MySQL query statement below
SELECT s1.student_name member_A, s2.student_name member_B, s3.student_name member_C
FROM SchoolA s1
JOIN SchoolB s2
    ON s1.student_id<>s2.student_id
JOIN SchoolC s3 
     ON   s2.student_id<>s3.student_id AND s1.student_id<>s3.student_id
     AND s1.student_name<>s2.student_name AND s1.student_name<>s3.student_name AND s2.student_name<>s3.student_name
  