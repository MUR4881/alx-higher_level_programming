-- Produce a new table whose id default value is 1 and must be unique

-- Create the table
 CREATE TABLE
IF NOT EXISTS unique_id(
			  id INT UNIQUE DEFAULT 1,
			  name VARCHAR(256)
			 );
