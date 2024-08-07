-- Create a new database and a new table in the the database

-- Create the database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Change context to the new database
USE hbtn_0d_usa;

-- Create the table
 CREATE TABLE
IF NOT EXISTS states(
		     id INT PRIMARY KEY AUTO_INCREMENT,
		     name VARCHAR(256) NOT NULL
		     )
