-- Write the SQL that displays the total number of books published by each publisher.

SELECT p.publisher_name, COUNT(b.book_id) as total_published_books  
FROM publisher p   
JOIN book b   
ON p.publisher_id = b.publisher_id  
GROUP BY p.publisher_name;  
 
-- Write the SQL that displays the books that have more than one author. 

SELECT b.title as book_title, COUNT(ba.author_id) as author_count  
FROM book b   
JOIN book_author ba   
    ON b.book_id = ba.book_id   
GROUP BY b.book_id, b.title  
HAVING COUNT(ba.author_id) > 1;  

-- Write the SQL that displays a list of authors that have not written any award-winning books.

SELECT a.first_name, a.last_name  
FROM author a  
JOIN book_author ba   
    ON a.author_id = ba.author_id   
LEFT JOIN book_award bw   
    ON ba.book_id = bw.book_id   
WHERE bw.award_id IS NULL;  