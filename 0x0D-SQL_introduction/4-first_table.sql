-- Connect to your MySQL server with enough privileges
-- Create a table called 'first_table' in the current database of MySQL server

CREATE DATABASE IF NOT EXISTS hbtn_0c_0;

USE hbtn_0c_0;

CREATE TABLE IF NOT EXISTS first_table (
	id INT,
	name VARCHAR(256)
);
