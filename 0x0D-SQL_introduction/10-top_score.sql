-- Connect to your MySQL server with enough privileges
-- This script lists all the records of the table 'second_table' in a particular order

SELECT DISTINCT score, name
FROM hbtn_0c_0.second_table
ORDER BY score DESC;
