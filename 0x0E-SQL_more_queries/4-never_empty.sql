-- Produce a new table whose id default value will not be NULL

-- Create the table
 CREATE TABLE
IF NOT EXISTS id_not_null(
			  id INT DEFAULT 1,
			  name VARCHAR(256)
			 );
