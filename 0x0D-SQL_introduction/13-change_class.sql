-- Connect to the MySQL server with sufficient privileges
-- This script deletes all records with a score <= 5 in the table second_table of the database hbtn_0c_0

USE hbtn_0c_0 ;

DELETE FROM second_table
WHERE score <= 5;
