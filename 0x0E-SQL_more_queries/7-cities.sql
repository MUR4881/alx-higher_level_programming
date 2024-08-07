-- Create a new database and a new table in the the database

-- Create the database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Change context to the new database
USE hbtn_0d_usa;

-- Create the table with foreign key to table state
 CREATE TABLE
IF NOT EXISTS cities(
		     id INT PRIMARY KEY AUTO_INCREMENT,
		     state_id INT NOT NULL,
		     name VARCHAR(256) NOT NULL,
		     FOREIGN KEY(state_id) REFERENCES states(id)
		     );
