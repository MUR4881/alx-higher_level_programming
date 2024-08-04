-- List all records of the table second_table
-- List all records of the table second_table  Where names exists
SELECT score, name FROM second_table
	WHERE name IS NOT NULL
	ORDER BY score DESC;
