-- Connect to your MySQL server with enough privileges
-- This script computes the average score of all records in the table second_table of the database hbtn_0c_0

USE hbtn_0c_0;

SELECT * FROM second_table;

SELECT AVG(score) AS average
FROM second_table
WHERE score IS NOT NULL;
