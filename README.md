# Technical Exercises

## Table of Contents

- [Python Exercise](#python-exercise)
- [SQL Exercise](#sql-exercise)


## Python Exercise

### Overview 

This project is created to fulfill the following requirements:

    Create a Python script that does the following:

    1. Retrieve data about Star Wars characters from the https://swapi.dev/api/people API. No authentication is
    needed.

    2. Output a list of the female characters to a text file. Each row in the file should include a row number as well as
    a character's name, ID number, and eye color.

**Important note: If you don't see the output file after running the script, check if you're looking in the right directory. The output file will be created in the directory where the script was run.**

### Features 

    Retrieves female Star Wars characters from ALL pages in the https://swapi.dev/api/people API.
    Includes a header row displaying the column names.

### Requirements

    Python version 3.5 and later
    Install `requests` library


### Output Results

**`Row_Number, Name, ID, Eye_Color`**  
`1, Leia Organa, 5, brown`  
`2, Beru Whitesun lars, 7, blue`  
`3, Mon Mothma, 28, blue`  
`4, Padmé Amidala, 35, brown`  
`5, Shmi Skywalker, 43, brown`  
`6, Ayla Secura, 46, hazel`  
`7, Adi Gallia, 55, blue`  
`8, Cordé, 61, brown`  
`9, Luminara Unduli, 64, blue`  
`10, Barriss Offee, 65, blue`  
`11, Dormé, 66, brown`  
`12, Zam Wesell, 70, yellow`  
`13, Taun We, 73, black`  
`14, Jocasta Nu, 74, blue`  
`15, R4-P17, 75, red, blue`  
`16, Shaak Ti, 78, black`  
`17, Sly Moore, 82, white`  


------------------------------------------------------------------------------------

## SQL Exercise 

**SQL Exercise Answers**

Write the SQL that displays the total number of books published by each publisher.

    SELECT p.publisher_name, COUNT(b.book_id) as total_published_books  
    FROM publisher p   
    JOIN book b   
    ON p.publisher_id = b.publisher_id  
    GROUP BY p.publisher_name;  
 
Write the SQL that displays the books that have more than one author. 

    SELECT b.title as book_title, COUNT(ba.author_id) as author_count  
    FROM book b   
    JOIN book_author ba   
        ON b.book_id = ba.book_id   
    GROUP BY b.book_id, b.title  
    HAVING COUNT (ba.author_id) > 1;  

Write the SQL that displays a list of authors that have not written any award-winning books.

    SELECT a.first_name, a.last_name  
    FROM author a  
    JOIN book_author ba   
        ON a.author_id = ba.author_id   
    LEFT JOIN book_award bw   
        ON ba.book_id = bw.book_id   
    WHERE bw.award_id IS NULL;  
