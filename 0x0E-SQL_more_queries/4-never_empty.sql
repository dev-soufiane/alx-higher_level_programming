-- Script that creates the table id_not_null on your MySQL server
-- The database name will be passed as an argument of the mysql command
-- If the table id_not_null already exists, your script should not fail
CREATE TABLE IF NOT EXISTS id_not_null (id INT DEFAULT '1', name VARCHAR(256));
