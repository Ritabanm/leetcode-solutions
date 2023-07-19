# Write your MySQL query statement below
SELECT 
    book_id,
    title,
    author,
    genre,
    publication_year,
    IF(
        total_copies - COUNT(CASE WHEN b.return_date IS NULL THEN 1 END) = 0, 
        COUNT(CASE WHEN b.return_date IS NULL THEN 1 END),
        NULL
    ) AS current_borrowers 
FROM   
    library_books 
JOIN  
    borrowing_records b USING(book_id)
GROUP BY 
    book_id 
HAVING 
    current_borrowers IS NOT NULL
ORDER BY 
    current_borrowers DESC,
    title ASC