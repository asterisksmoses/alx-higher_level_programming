-- Connect to the MySQL server with enough user as privileges
-- This script displays the number of records with id = 89 in the table first_table of the database hbtn_0c_0

USE hbtn_0c_0;

SELECT COUNT(*) AS record_count
FROM first_table
WHERE id = 89;
