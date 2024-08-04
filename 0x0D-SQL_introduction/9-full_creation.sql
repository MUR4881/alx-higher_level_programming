-- Create a new table and insert multiple row into it
-- Create a table second_table in the database
CREATE TABLE IF NOT EXISTS second_table (
	id INT,
	name VARCHAR(256),
	score INT
	);

-- store rows/records into the newly created table
INSERT INTO second_table 
	VALUES(1, 'John', 10),
		(2, 'Alex', 3),
		(3, 'Bob', 14),
		(4, 'George', 8);
