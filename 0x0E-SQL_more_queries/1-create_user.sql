-- Connect to the MySQL server with enough privileges
-- creates the MySQL server user user_0d_1
-- user_0d_1 should have all privileges on your MySQL server

SELECT EXISTS(
	SELECT 1
	FROM mysql.user
	WHERE user = 'user_0d_1' AND host = 'localhost'
) INTO @user_exists;

IF @user_exists = 0 THEN
	CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
END IF;

GRANT CREATE, ALTER, DROP, INSERT, UPDATE, DELETE, SELECT,
REFERENCES, RELOAD on *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

FLUSH PRIVILEGES;
